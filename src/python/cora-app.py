"""Build Agent using Microsoft Agent Framework in Python
# Run this python script
> pip install anthropic agent-framework==1.0.0b260107 agent-framework-azure-ai==1.0.0b260107
> python <this-script-path>.py
"""

import asyncio
import os

from opentelemetry.semconv_ai import SpanAttributes

# Compatibility shim for recent OpenTelemetry semantic convention changes.
# Agent Framework currently expects legacy LLM_* attribute constants.
_OTEL_SPANATTR_FALLBACKS = {
    "LLM_SYSTEM": "llm.system",
    "LLM_REQUEST_MODEL": "llm.request.model",
    "LLM_REQUEST_MAX_TOKENS": "llm.request.max_tokens",
    "LLM_REQUEST_TEMPERATURE": "llm.request.temperature",
    "LLM_REQUEST_TOP_P": "llm.request.top_p",
    "LLM_RESPONSE_MODEL": "llm.response.model",
    "LLM_TOKEN_TYPE": "llm.token_type",
}
for _name, _value in _OTEL_SPANATTR_FALLBACKS.items():
    if not hasattr(SpanAttributes, _name):
        setattr(SpanAttributes, _name, _value)

from agent_framework import MCPStdioTool, MCPStreamableHTTPTool, ToolTypes, Content
from agent_framework.azure import AzureAIAgentClient
from agent_framework.openai import OpenAIChatClient
from openai import AsyncOpenAI
from azure.identity.aio import DefaultAzureCredential

# Microsoft Foundry Agent Configuration
ENDPOINT = "https://aifoundry-aman1234.services.ai.azure.com/api/projects/project-aman1234"
MODEL_DEPLOYMENT_NAME = "gpt-5-mini-aman1234"

AGENT_NAME = "mcp-agent"
AGENT_INSTRUCTIONS = "You are Cora, an intelligent and friendly AI assistant for Zava, a home improvement brand. You help customers with their DIY projects by understanding their needs and recommending the most suitable products from Zava’s catalog.​\n\nYour role is to:​\n\n- Engage with the customer in natural conversation to understand their DIY goals.​\n\n- Ask thoughtful questions to gather relevant project details.​\n\n- Be brief in your responses.​\n\n- Provide the best solution for the customer's problem and only recommend a relevant product within Zava's product catalog.​\n\n- Search Zava’s product database to identify 1 product that best match the customer’s needs.​\n\n- Clearly explain what each recommended Zava product is, why it’s a good fit, and how it helps with their project.​\n​\nYour personality is:​\n\n- Warm and welcoming, like a helpful store associate​\n\n- Professional and knowledgeable, like a seasoned DIY expert​\n\n- Curious and conversational—never assume, always clarify​\n\n- Transparent and honest—if something isn’t available, offer support anyway​\n\nIf no matching products are found in Zava’s catalog, say:​\n“Thanks for sharing those details! I’ve searched our catalog, but it looks like we don’t currently have a product that fits your exact needs. If you'd like, I can suggest some alternatives or help you adjust your project requirements to see if something similar might work.”​"

# User inputs for the conversation
USER_INPUTS = [
    "Here’s a photo of my living room. Based on the lighting and layout, recommend a Zava eggshell paint.",
    "How much is Zava's eggshell paint?",
    "What are the current inventory levels for Zava's eggshell paint?",
]

def create_mcp_tools() -> list[ToolTypes]:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    mcp_script = os.path.join(base_dir, "mcp_server", "customer_sales", "customer_sales.py")
    mcp_script_dir = os.path.dirname(mcp_script)
    return [
        MCPStdioTool(
            name="zava-customer-sales-stdio".replace("-", "_"),
            description="MCP server for zava-customer-sales-stdio",
            command="python",
            args=[
                mcp_script,
                "--stdio",
                "--RLS_USER_ID=00000000-0000-0000-0000-000000000000",
            ],
            env={
                "POSTGRES_URL": os.environ.get("POSTGRES_URL", "postgresql://store_manager:StoreManager123!@localhost:15432/zava"),
                "PYTHONPATH": mcp_script_dir,
            }
        ),
    ]

async def main() -> None:
    async with (
        # For authentication, DefaultAzureCredential supports multiple authentication methods. Run `az login` in terminal for Azure CLI auth.
        DefaultAzureCredential() as credential,
        AzureAIAgentClient(
            project_endpoint=ENDPOINT,
            model_deployment_name=MODEL_DEPLOYMENT_NAME,
            credential=credential,
            agent_name=AGENT_NAME,
        ).as_agent(
            instructions=AGENT_INSTRUCTIONS,
            tools=[
                *create_mcp_tools(),
            ],
        ) as agent
    ):
        # Process user messages
        for user_input in USER_INPUTS:
            print(f"\n# User: '{user_input}'")
            printed_tool_calls = set()
            async for chunk in agent.run([user_input], stream=True):
                # log tool calls if any
                function_calls = [
                    c for c in chunk.contents 
                    if isinstance(c, Content) and c.type == 'function_call'
                ]
                for call in function_calls:
                    if call.call_id not in printed_tool_calls:
                        print(f"Tool calls: {call.name}")
                        printed_tool_calls.add(call.call_id)
                if chunk.text:
                    print(chunk.text, end="")
            print("")
        
        print("\n--- All tasks completed successfully ---")

    # Give additional time for all async cleanup to complete
    await asyncio.sleep(1.0)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("Program finished.")
