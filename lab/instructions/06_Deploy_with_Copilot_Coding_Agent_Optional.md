# (Optional) Deploy with GitHub Copilot Coding Agent

> [!NOTE]
> This is an **optional bonus exercise** you can complete if you still have time during the allotted lab slot, or at your own pace after the workshop. The core lab is complete after the previous section where you built the UI and tested locally. This section covers deploying the application to Azure using GitHub Copilot Coding Agent — an advanced workflow that typically takes an additional 30-60 minutes.

In this section, you will use **GitHub Copilot Coding Agent** to prepare deployment configurations, then use **GitHub Copilot Chat in Agent mode** to deploy and run the application in Azure. The agent code at `src/python/cora-app.py` and the UI you built in the previous section are your starting point.

GitHub Copilot Coding Agent is an autonomous AI agent that can understand a GitHub Issue, plan the work, write code, and open a Pull Request — all without manual intervention. By assigning an Issue to Copilot, you can delegate complex development tasks like refining the UI, adding deployment configurations, and setting up Azure infrastructure. Once the code is ready, you'll use Copilot Chat in Agent mode within VS Code to handle the actual deployment and testing.

## Step 1: Create a GitHub Issue for Copilot Coding Agent

Now you'll create a GitHub Issue that describes the work you want Copilot Coding Agent to do: prepare the Cora agent application for deployment to Azure.

1. Open your browser and navigate to your repository on GitHub.

2. Select the **Issues** tab, then click **New issue**.

3. Use the following as your Issue title:

   ```
   Prepare the Cora agent app for Azure deployment
   ```

4. In the Issue body, paste the following detailed description:

   ```markdown
   ## Context
   
   We have an AI agent called Cora built using the Microsoft Agent Framework 
   (see `src/python/cora-app.py`). Cora is a customer service agent for Zava, 
   a DIY retail company, that helps customers find products and get recommendations 
   from the product catalog.
   
   The agent uses an MCP (Model Context Protocol) server located at 
   `src/python/mcp_server/customer_sales/customer_sales.py` for querying the 
   Zava product database.
   
   ## Requirements
   
   ### 1. Web UI
   - Create a web-based chat UI for the Cora agent using **Chainlit** or **Streamlit**
   - The UI should have a clean, professional look suitable for a retail brand
   - Include a chat interface where users can type messages and see agent responses
   - Display the Zava branding (company name in the header)
   - Save the UI code in `src/python/cora-ui.py`
   
   ### 2. Dockerfile
   - Create a `Dockerfile` in `src/python/` that packages the Cora agent and UI 
     into a container
   - Use a Python base image
   - Install all dependencies from `requirements.txt`
   - Expose the appropriate port for the web UI
   - Set the entry point to run the UI application
   
   ### 3. Azure Deployment Configuration
   - Add an Azure Container Apps deployment configuration 
     (e.g., a Bicep or ARM template file) in `infra/` that includes:
     - An Azure Container Apps Environment
     - A Container App for the Cora agent UI
     - The necessary environment variables for connecting to the 
       Azure AI Foundry model endpoint
   - Update `src/python/requirements.txt` with any new dependencies
   
   ### 4. Documentation
   - Update the `README.md` or add a `DEPLOYMENT.md` with instructions on how to:
     - Build and run the container locally
     - Deploy to Azure Container Apps
   
   ## Acceptance Criteria
   - [ ] A working web UI that connects to the Cora agent
   - [ ] A Dockerfile that successfully builds
   - [ ] Azure deployment configuration files in `infra/`
   - [ ] Updated requirements.txt with all dependencies
   - [ ] Deployment documentation
   ```

> [!TIP]
> The more detailed and specific your Issue description is, the better Copilot Coding Agent will perform. Include file paths, technology preferences, and acceptance criteria to guide Copilot effectively.

## Step 2: Assign the Issue to Copilot

With your Issue created, you can now assign it to GitHub Copilot Coding Agent.

1. On the Issue page, look at the **Assignees** section in the right sidebar.

2. Click **Assignees** and select **Copilot** from the list of available assignees.

   ![Assign to Copilot](../../img/assign-copilot.png)

3. Once assigned, Copilot Coding Agent will begin working on the Issue. You will see a status indicator on the Issue showing that Copilot is actively working.

> [!NOTE]
> Copilot Coding Agent works autonomously in a secure cloud environment. It reads the Issue description, explores the repository, plans the implementation, writes the code, and creates a Pull Request. This process typically takes a few minutes.

## Step 3: Review and Merge the Pull Request

After Copilot Coding Agent completes its work, it will create a Pull Request (PR) linked to the Issue.

1. Navigate to the **Pull requests** tab in your repository. You should see a new PR created by Copilot.

2. Click on the PR to review the changes. Copilot's PR will typically include:
   - A description of what was implemented
   - The files added or modified
   - A summary of how the changes address the Issue

3. Review the code changes in the **Files changed** tab. Look for:
   - The new UI file (e.g., `src/python/cora-ui.py`)
   - The `Dockerfile` in `src/python/`
   - Azure deployment configuration in `infra/`
   - Updated `requirements.txt`

4. If you'd like to request changes, leave a comment on the PR. Copilot Coding Agent can respond to feedback and make additional changes.

5. Once you're satisfied with the changes, **approve** and **merge** the Pull Request.

> [!TIP]
> You can ask Copilot to make adjustments by leaving comments on the PR. For example: "Please change the UI framework from Streamlit to Chainlit" or "Add a health check endpoint for the container".

## Step 4: Deploy to Azure Using Agent Mode (One-Shot Prompt)

With the code merged, you can now use GitHub Copilot Chat in **Agent** mode to deploy the entire application to Azure in a single prompt. This prompt is designed to handle infrastructure provisioning, code fixes, Docker build, database restoration, and end-to-end verification — all at once.

1. First, pull the latest changes (including the merged PR from Copilot Coding Agent):

   ```bash
   git pull origin main
   ```

2. Open **GitHub Copilot Chat** in VS Code and switch to **Agent** mode.

3. Paste the following one-shot prompt. Before pasting, replace the placeholder values with your own:
   - `<UNIQUE_SUFFIX>` — a short unique identifier (e.g., your alias like `aman`)
   - `<AI_FOUNDRY_RESOURCE_GROUP>` — the resource group containing your existing AI Foundry resources
   - `<AI_FOUNDRY_ACCOUNT>` — your AI Foundry account name (e.g., `aifoundry-aman`)
   - `<AI_FOUNDRY_PROJECT>` — your AI Foundry project name (e.g., `project-aman`)
   - `<MODEL_DEPLOYMENT>` — your model deployment name (e.g., `gpt-5-mini-aman`)

   ````
   Deploy the Cora AI agent app to Azure Container Apps end-to-end. 
   Follow every step below in order. Do NOT stop to ask me questions — 
   use the information provided and the codebase to resolve issues.

   ## My environment
   - Unique suffix for resource names: <UNIQUE_SUFFIX>
   - Existing AI Foundry resource group: <AI_FOUNDRY_RESOURCE_GROUP>
   - Existing AI Foundry account: <AI_FOUNDRY_ACCOUNT>
   - Existing AI Foundry project: <AI_FOUNDRY_PROJECT>  
   - Existing model deployment: <MODEL_DEPLOYMENT>
   - Target deployment region: swedencentral

   ## Step 1 — Infrastructure (Bicep)
   Create a consolidated Bicep file at `infra/main-consolidated.bicep` 
   (with `.bicepparam`) that references the EXISTING AI Foundry resources 
   above using the `existing` keyword (cross-resource-group references) 
   and creates these NEW resources in resource group `rg-cora-agent`:
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

   CRITICAL for POSTGRES_URL: Use the short container app name as hostname 
   (e.g., `cora-db-<SUFFIX>`) and ALWAYS append `?sslmode=disable` because 
   the container PostgreSQL does not have SSL configured. Example:
   `postgresql://postgres:P@ssw0rd!@cora-db-<SUFFIX>:5432/zava?sslmode=disable`

   ## Step 2 — Deploy infrastructure
   - `az login` if needed
   - Create resource group `rg-cora-agent` in swedencentral
   - Deploy the Bicep template
   - If any role assignment fails due to existing assignments, ignore the error

   ## Step 3 — Fix code before building
   Read `src/python/cora-app.py` and ensure `src/python/cora-ui.py` is 
   consistent with it. Apply these CRITICAL fixes:

   ### 3a. Python dependencies (`src/python/requirements.txt`)
   - Pin `agent-framework` and `agent-framework-azure-ai` to the EXACT 
     same version used in `cora-app.py` (e.g., `1.0.0b260107`)
   - Do NOT include `azure-ai-agents` or `azure-ai-projects` — they 
     conflict with agent-framework
   - Do NOT cap `openai` at `<2.0.0`
   - Include: chainlit, asyncpg, azure-identity, mcp, python-dotenv, 
     azure-ai-inference, aiohttp, fastapi, httpx, uvicorn[standard], 
     jinja2, aiofiles, pandas, python-multipart

   ### 3b. Cora UI (`src/python/cora-ui.py`)
   - The agent-framework b260107 uses `Contents` (plural) not `Content`. 
     Import: `from agent_framework import ChatMessage, Contents, DataContent, 
     MCPStdioTool, TextContent`
   - Use `agent_client.create_agent(...)` — NOT `as_agent()` context manager. 
     `create_agent()` returns the agent directly, it is NOT a context manager.
   - Use `agent.run_stream([messages])` — NOT `agent.run([messages], stream=True)`
   - The MCPStdioTool `env` parameter MUST include `**os.environ` to propagate 
     the POSTGRES_URL from the container environment to the MCP subprocess
   - Support image attachments: read `message.elements`, convert images to 
     base64 DataContent, build ChatMessage with TextContent + DataContent

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

   ## Step 4 — Build & push Docker image
   - `az acr login --name <ACR_NAME>`
   - `docker build -t <ACR_NAME>.azurecr.io/cora-ui:latest src/python/`
   - `docker push <ACR_NAME>.azurecr.io/cora-ui:latest`
   - Create a new Container App revision (use `az containerapp update --revision-suffix`)

   ## Step 5 — Restore PostgreSQL database
   - Upload `data/zava_retail_2025_07_21_postgres_rls.backup` to a temp 
     Azure Storage account with anonymous blob public access enabled
   - Use `az containerapp exec` to:
     1. `curl` the backup into `/tmp/zava.backup` inside the DB container
     2. Run a bash init script that creates the `zava` database, installs 
        the `vector` extension, creates the `retail` schema, runs `pg_restore`, 
        creates `store_manager` user (password: `StoreManager123!`), grants 
        schema permissions, and enables Row Level Security policies if the 
        `rls_user_id` column exists
   - NOTE: `az containerapp exec` mangles `&` and quotes. Avoid SAS URLs. 
     Use anonymous public blob access and simple URLs without special characters.
     Upload scripts as files to blob storage and download+execute them in 
     the container to avoid shell quoting issues.
   - After DB restore, delete the temp storage account

   ## Step 6 — Verify end-to-end
   - Check the Container App revision is Healthy and Running
   - Check container logs for any MCP or DB connection errors
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
   ````

4. Review each command that Agent mode proposes. You will be prompted to **approve** or **reject** each terminal command before it runs. Review carefully and click **Continue** to proceed with each step.

> [!TIP]
> Agent mode can run terminal commands, create files, and edit code on your behalf — but it always asks for your approval before executing commands. This makes it safe to use for deployment tasks.

> [!NOTE]
> The full deployment typically takes 10-15 minutes. Agent mode will keep you updated on progress as each step finishes.

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

## Step 5: Test the Deployed Application

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

- GitHub Copilot Coding Agent can autonomously implement features from a well-written GitHub Issue — from creating UIs to adding deployment configurations.
- Writing detailed, specific Issues with clear requirements and acceptance criteria helps Copilot Coding Agent produce higher-quality results.
- Reviewing Copilot's Pull Requests is an important step — treat it like any code review, checking for correctness, security, and alignment with your requirements.
- GitHub Copilot Chat in **Agent mode** can execute deployment commands, troubleshoot errors, and manage Azure resources — all within VS Code with your approval at every step.
- Azure Container Apps provides a straightforward way to deploy containerized AI agent applications with built-in scaling and managed infrastructure.

Click **Next** to proceed to the Summary.
