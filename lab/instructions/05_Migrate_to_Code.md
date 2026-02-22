# (Optional) Deploy to Azure Using GitHub Copilot

> [!NOTE]
> This is an **optional bonus exercise** you can complete if you still have time during the allotted lab slot, or at your own pace after the workshop. The core lab is complete after the previous section where you built the UI and tested locally. This section covers deploying the application to Azure using GitHub Copilot Chat in Agent mode — an advanced workflow that typically takes an additional 30-60 minutes.

In this section, you will use **GitHub Copilot Chat in Agent mode** to deploy the Cora agent application to Azure. The agent code at `src/python/cora-app.py` and the UI you built in the previous section are your starting point. Agent mode will handle infrastructure provisioning, code fixes, Docker build, database restoration, and end-to-end verification — all from a single prompt.

## Step 1: Deploy to Azure Using Agent Mode (One-Shot Prompt)

You will use GitHub Copilot Chat in **Agent** mode to deploy the entire application to Azure in a single prompt.

1. Open **GitHub Copilot Chat** in VS Code and switch to **Agent** mode.

2. Paste the following one-shot prompt into the chat:

   ````
   Deploy the Cora AI agent app to Azure Container Apps end-to-end. 
   Follow every step below in order. Do NOT stop to ask me questions — 
   use the information provided and the codebase to resolve issues.

   ## My environment
   - Read `src/python/cora-app.py` to find the AI Foundry project endpoint 
     and model deployment name already configured in the code.
   - Read `lab/script/Lab512-arm-template.json` to find the existing 
     resource group, AI Foundry account name, and project name.
   - Derive a unique suffix from the resource names found above.
   - Target deployment region: swedencentral

   ## Step 1 — Infrastructure (Bicep)
   Create a consolidated Bicep file at `infra/main-consolidated.bicep` 
   (with `.bicepparam`) that deploys all NEW resources into the SAME 
   existing resource group where the AI Foundry account and project 
   already live. Reference the EXISTING AI Foundry resources using the 
   `existing` keyword (same resource group — no cross-resource-group 
   scoping needed) and create these NEW resources:
   - Azure Container Registry (admin enabled, Basic SKU)
   - Log Analytics workspace
   - User-assigned managed identity
   - Container Apps Environment
   - PostgreSQL Container App (`pgvector/pgvector:pg17`, internal TCP 
     ingress on port 5432, EmptyDir volume mounted at `/var/lib/postgresql/data`,
     env vars: POSTGRES_USER=postgres, POSTGRES_PASSWORD=P@ssw0rd!, PGDATA=/var/lib/postgresql/data/pgdata)
   - Cora UI Container App (external HTTPS ingress on port 8000, 
     env vars from secrets: AZURE_AI_FOUNDRY_ENDPOINT, MODEL_DEPLOYMENT_NAME, 
     POSTGRES_URL, AZURE_CLIENT_ID from managed identity)
   - Role assignments: AcrPull for the managed identity on the ACR, 
     "Cognitive Services OpenAI User" and "Cognitive Services User" for the 
     managed identity on the AI Foundry account

   CRITICAL Bicep syntax rules:
   - Do NOT use semicolons to separate object properties on a single line. 
     Bicep requires each property on its own line. For example use:
     ```bicep
     properties: {
       foo: 'bar'
       baz: 123
     }
     ```
     NOT: `properties: { foo: 'bar'; baz: 123 }`
   - For the Cora UI Container App image, use a PLACEHOLDER image 
     `mcr.microsoft.com/azuredocs/containerapps-helloworld:latest` in the 
     Bicep template. The real ACR image does not exist yet during the first 
     deployment — it will be updated in Step 4 after docker push.

   CRITICAL for POSTGRES_URL: Use the short container app name as hostname 
   (e.g., `cora-db-<SUFFIX>`) and ALWAYS append `?sslmode=disable` because 
   the container PostgreSQL does not have SSL configured. Example:
   `postgresql://postgres:P@ssw0rd!@cora-db-<SUFFIX>:5432/zava?sslmode=disable`

   ## Step 2 — Deploy infrastructure
   - `az login` if needed
   - Use the existing resource group (do NOT create a new resource group — 
     all new resources are deployed alongside the existing AI Foundry resources)
   - Deploy the Bicep template to the existing resource group
   - If any role assignment fails due to existing assignments, ignore the error

   ## Step 3 — Fix code before building
   Read `src/python/cora-app.py` and ensure `src/python/cora-ui.py` is 
   consistent with it. Apply these CRITICAL fixes:

   ### 3a. Python dependencies (`src/python/requirements.txt`)
   - Pin `agent-framework` and `agent-framework-azure-ai` to `1.0.0rc1` 
     (the latest RC version)
   - Do NOT include `azure-ai-agents` or `azure-ai-projects` — they 
     conflict with agent-framework
   - Do NOT cap `openai` at `<2.0.0`
   - Include: chainlit, asyncpg, azure-identity, mcp, python-dotenv, 
     azure-ai-inference, aiohttp, fastapi, httpx, uvicorn[standard], 
     jinja2, aiofiles, pandas, python-multipart

   ### 3b. Cora UI (`src/python/cora-ui.py`)
   The agent-framework RC1 API differs from the beta versions. Use these 
   EXACT imports and patterns:
   - Import: `from agent_framework import Content, MCPStdioTool, Message`
   - Import: `from agent_framework_azure_ai import AzureAIAgentClient` 
     (NOT `from agent_framework.azure`)
   - Create messages with: `Message(role="user", contents=[...])` 
     (NOT `ChatMessage`)
   - Create text content with: `Content.from_text("hello")` 
     (NOT `TextContent(text="hello")`)
   - Create image content with: `Content.from_data(data=raw_bytes, media_type="image/png")` 
     where `raw_bytes` is the actual `bytes` object (NOT base64-encoded). 
     Do NOT use `DataContent` — it does not exist in RC1.
   - Create the agent with: `client.as_agent(instructions=..., tools=[...])` 
     (NOT `create_agent()` — that was the beta API)
   - Stream responses with: `async for chunk in agent.run([msg], stream=True):` 
     (NOT `agent.run_stream()` — that was the beta API)
   - Each streaming chunk has a `.text` property for the text delta and 
     `.contents` for the full content list.
   - The MCPStdioTool `env` parameter MUST include `**os.environ` to propagate 
     the POSTGRES_URL from the container environment to the MCP subprocess
   - Do NOT use `ToolTypes` in any type annotations — it may not be importable 
     in all versions. Use plain `list` instead of `list[ToolTypes]`.
   - Support image attachments: read `message.elements`, read file bytes with 
     `Path(path).read_bytes()`, pass raw bytes to `Content.from_data()`

   ### 3c. Chainlit config (`src/python/.chainlit/config.toml`)
   - Chainlit v2 uses `[features.spontaneous_file_upload]` (NOT 
     `[features.multi_modal]`) to enable file/image attachments. Set:
     ```toml
     [features.spontaneous_file_upload]
     enabled = true
     accept = ["image/png", "image/jpeg", "image/gif", "image/webp"]
     max_files = 5
     max_size_mb = 20
     ```

   ### 3d. MCP server DB connection (`src/python/mcp_server/customer_sales/customer_sales_postgres.py`)
   - asyncpg does NOT reliably parse `sslmode=disable` from DSN query params. 
     Fix `create_pool()` to:
     1. Parse the POSTGRES_URL with `urllib.parse.urlparse`
     2. Extract host, port, user, password, database as explicit parameters
     3. Check for `sslmode=disable` in query params and pass `ssl=False` 
        explicitly to `asyncpg.create_pool()`
     4. Add retry logic (3 attempts with 2s backoff) for transient DNS failures 
        during container startup

   ### 3e. Dockerfile (`src/python/Dockerfile`)
   - Chainlit requires writable `/app/.files` and `/app/.chainlit` directories 
     at runtime. Before the `USER appuser` line in the Dockerfile, add:
     ```dockerfile
     RUN mkdir -p /app/.files /app/.chainlit && chown -R appuser:appuser /app
     ```
     Without this, the container will crash with "Permission denied" on startup.

   ## Step 4 — Build & push Docker image
   - `az acr login --name <ACR_NAME>`
   - `docker build -t <ACR_NAME>.azurecr.io/cora-ui:latest src/python/`
   - Test the image locally first: `docker run --rm <ACR_NAME>.azurecr.io/cora-ui:latest python -c "from agent_framework import Content, MCPStdioTool, Message; from agent_framework_azure_ai import AzureAIAgentClient; print('OK')"` 
     — this catches import errors before pushing
   - `docker push <ACR_NAME>.azurecr.io/cora-ui:latest`
   - Update the Container App with the real image: 
     `az containerapp update --name <APP_NAME> --resource-group <RG> --image <ACR_NAME>.azurecr.io/cora-ui:latest --revision-suffix v1`

   ## Step 5 — Restore PostgreSQL database
   Use an Azure Container Apps Job (NOT `az containerapp exec`) to restore the 
   database. `az containerapp exec` is unreliable for multi-command scripts 
   because it mangles `&`, quotes, and special characters.

   Steps:
   1. Create a temp Azure Storage account with anonymous blob public access enabled
   2. Upload `data/zava_retail_2025_07_21_postgres_rls.backup` to a blob container
   3. Upload a bash restore script to the same blob container. The script should:
      - `curl` the backup file from blob storage into `/tmp/zava.backup`
      - Create the `zava` database (`createdb`)
      - Install the `vector` extension (`psql -d zava -c "CREATE EXTENSION IF NOT EXISTS vector"`)
      - Create the `retail` schema
      - Run `pg_restore --no-owner --no-privileges -d zava /tmp/zava.backup` 
        (use `|| true` since pg_restore may emit non-fatal warnings)
      - Create `store_manager` user (password: `StoreManager123!`)
      - Grant schema permissions to `store_manager`
      - Enable Row Level Security policies if the `rls_user_id` column exists
   4. Create an Azure Container Apps Job in the same Container Apps Environment 
      using the `postgres:17` image (NOT `pgvector/pgvector:pg17` — the pgvector 
      image does not include `curl`). Set PGHOST, PGUSER, PGPASSWORD env vars 
      pointing to the DB container app.
   5. Configure the job to download and execute the restore script:
      `bash -c "curl -sL <SCRIPT_URL> -o /tmp/restore.sh && chmod +x /tmp/restore.sh && /tmp/restore.sh"`
   6. Start the job and wait for it to succeed
   7. Delete the temp storage account after successful restore

   ## Step 6 — Verify end-to-end
   - Wait 30 seconds after deployment, then check the Container App revision: 
     `az containerapp revision show` — confirm healthState=Healthy, runningState=Running
   - Check container logs: `az containerapp logs show --type console --tail 30`
   - Verify logs show "Your app is available at http://0.0.0.0:8000" and 
     "ManagedIdentityCredential will use App Service managed identity"
   - If the revision is NOT healthy, check logs, fix the issue, rebuild the 
     image with a new tag (v2, v3...), push, and create a new revision
   - Open the app URL in the browser
   - Confirm: agent responds to messages, image attachment button is visible, 
     and the agent can query product data from the database

   ## Important gotchas (do NOT skip these)
   - Container Apps TCP ingress does NOT support external access without a 
     custom VNET — keep DB ingress as internal
   - Container Apps in the same environment resolve each other by short app 
     name (e.g., `cora-db-<SUFFIX>`) via k8s DNS — do NOT use the full 
     internal FQDN for TCP apps
   - The `@` in passwords like `P@ssw0rd!` is safe for Python's urlparse 
     but can cause issues if passed as raw DSN to asyncpg — always parse 
     URLs and pass explicit parameters
   - Chainlit v2.x config format differs significantly from v1.x — always 
     check the installed version and use the correct section names
   - Bicep does NOT support semicolons between properties in object literals — 
     always use multi-line format with one property per line
   - The Cora UI Container App image does not exist in ACR during the first 
     Bicep deployment — use a placeholder image and update after docker push
   - Chainlit requires writable `/app/.files` directory — the Dockerfile MUST 
     create it and set ownership before switching to a non-root user
   - `az containerapp exec` is unreliable for complex scripts — prefer 
     Container Apps Jobs for database restore operations
   - The `pgvector/pgvector:pg17` Docker image does NOT include `curl` — use 
     `postgres:17` for any job that needs to download files
   - Always test the Docker image locally with a quick import check before 
     pushing to ACR — this catches Python import errors immediately
   ````

3. Review each command that Agent mode proposes. You will be prompted to **approve** or **reject** each terminal command before it runs. Review carefully and click **Continue** to proceed with each step.

> [!TIP]
> Agent mode can run terminal commands, create files, and edit code on your behalf — but it always asks for your approval before executing commands. This makes it safe to use for deployment tasks.

> [!NOTE]
> The full deployment typically takes 30-60 minutes depending on Docker build times and Azure provisioning. Agent mode will keep you updated on progress as each step finishes. Multiple revision iterations may be needed if import or permission errors are encountered.

### Key Azure Resources for Deployment

| Resource | Purpose |
|:---------|:--------|
| **Azure AI Foundry Account** | Hosts the AI models used by the Cora agent (existing) |
| **AI Foundry Project** | Organizes the AI resources for the project (existing) |
| **GPT-5-mini Deployment** | The model that powers Cora's intelligence (existing) |
| **Azure Container Registry** | Stores the Cora UI Docker image |
| **User-Assigned Managed Identity** | Authenticates the Container App to AI Foundry and ACR |
| **Container Apps Environment** | Provides the managed environment for running containers |
| **PostgreSQL Container App** | Hosts the Zava product database (pgvector) |
| **Cora UI Container App** | Runs the Chainlit web UI for the Cora agent |

## Step 2: Test the Deployed Application

Once the deployment is complete, verify that the Cora agent is running in Azure.

1. The agent should have already opened the app URL. If not, ask:

   ```
   What is the URL of the deployed Cora Container App? Open it in my browser.
   ```

2. In the web UI, test the Cora agent by typing a message such as:

   ```
   What type of paint does Zava sell?
   ```

3. Verify that:
   - The chat UI loads correctly with Zava branding
   - The agent responds with relevant product information from the catalog
   - The MCP server connection is working (the agent can query the product database)
   - An **attachment button** (paperclip icon) is visible in the chat input for sending images

4. (Optional) Test image attachment by clicking the attachment button, uploading a photo, and asking the agent about it.

## Key Takeaways

- GitHub Copilot Chat in **Agent mode** can execute deployment commands, create infrastructure-as-code files, troubleshoot errors, and manage Azure resources — all within VS Code with your approval at every step.
- A detailed, well-structured one-shot prompt enables Agent mode to handle complex multi-step deployments end-to-end with minimal manual intervention.
- Azure Container Apps provides a straightforward way to deploy containerized AI agent applications with built-in scaling and managed infrastructure.
- Deploying into the same resource group as your existing AI Foundry resources simplifies networking, role assignments, and resource management.

Click **Next** to proceed to the Summary.
