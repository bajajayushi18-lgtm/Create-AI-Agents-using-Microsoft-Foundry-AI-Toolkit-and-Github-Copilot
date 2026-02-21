# Deploy with GitHub Copilot Coding Agent

In this section, you will push your exported Agent Framework code to GitHub and use **GitHub Copilot Coding Agent** to build a UI and prepare the application for deployment to Azure — all by creating a GitHub Issue.

GitHub Copilot Coding Agent is an autonomous AI agent that can understand a GitHub Issue, plan the work, write code, and open a Pull Request — all without manual intervention. By assigning an Issue to Copilot, you can delegate complex development tasks like creating a UI, adding deployment configurations, and setting up Azure infrastructure.

## Step 1: Push Your Agent Framework Code to GitHub

After exporting and saving your agent code as `src/python/cora-app.py` in the previous section, you need to commit and push the code to your GitHub repository.

1. Open a terminal in Visual Studio Code by selecting **Terminal** -> **New Terminal** from the top menu.

2. Stage the new agent code file:

   ```bash
   git add src/python/cora-app.py
   ```

3. Commit the changes with a descriptive message:

   ```bash
   git commit -m "Add Cora agent exported from Agent Framework"
   ```

4. Push the commit to GitHub:

   ```bash
   git push origin main
   ```

> [!NOTE]
> If you are prompted to authenticate, follow the instructions in the terminal to complete the sign-in.

## Step 2: Create a GitHub Issue for Copilot Coding Agent

Now you'll create a GitHub Issue that describes the work you want Copilot Coding Agent to do: build a web UI for the Cora agent and prepare the application for deployment to Azure.

1. Open your browser and navigate to your repository on GitHub.

2. Select the **Issues** tab, then click **New issue**.

3. Use the following as your Issue title:

   ```
   Build a web UI for the Cora agent and prepare for Azure deployment
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

## Step 3: Assign the Issue to Copilot

With your Issue created, you can now assign it to GitHub Copilot Coding Agent.

1. On the Issue page, look at the **Assignees** section in the right sidebar.

2. Click **Assignees** and select **Copilot** from the list of available assignees.

   ![Assign to Copilot](../../img/assign-copilot.png)

3. Once assigned, Copilot Coding Agent will begin working on the Issue. You will see a status indicator on the Issue showing that Copilot is actively working.

> [!NOTE]
> Copilot Coding Agent works autonomously in a secure cloud environment. It reads the Issue description, explores the repository, plans the implementation, writes the code, and creates a Pull Request. This process typically takes a few minutes.

## Step 4: Review and Merge the Pull Request

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

## Step 5: Update Azure Resources for Deployment

To deploy the Cora agent and its UI to Azure, you need to ensure the right Azure resources are provisioned. The lab already includes an ARM template at `lab/script/Lab512-arm-template.json` that deploys the AI Foundry account and model. For the UI deployment, additional resources are needed.

You can use GitHub Copilot Chat in **Agent** mode to help update the infrastructure. Try the following prompt:

```
Review the existing ARM template at lab/script/Lab512-arm-template.json and 
the new infrastructure files created by Copilot in infra/. Help me create a 
complete deployment that includes:
1. The existing AI Foundry resources (account, project, gpt-5-mini model)
2. An Azure Container Apps Environment
3. A Container App for the Cora agent UI
4. Any necessary role assignments so the Container App can access AI Foundry

Output the result as a consolidated ARM template or Bicep file.
```

> [!NOTE]
> The resources generated by Copilot Coding Agent in the `infra/` folder may already cover what's needed. Use this step to review and consolidate all infrastructure configurations.

### Key Azure Resources for Deployment

| Resource | Purpose |
|:---------|:--------|
| **Azure AI Foundry Account** | Hosts the AI models used by the Cora agent |
| **AI Foundry Project** | Organizes the AI resources for the project |
| **GPT-5-mini Deployment** | The model that powers Cora's intelligence |
| **Azure Container Apps Environment** | Provides the managed environment for running containers |
| **Container App** | Runs the Cora agent UI as a containerized web application |

## Key Takeaways

- GitHub Copilot Coding Agent can autonomously implement features from a well-written GitHub Issue — from creating UIs to adding deployment configurations.
- Writing detailed, specific Issues with clear requirements and acceptance criteria helps Copilot Coding Agent produce higher-quality results.
- Reviewing Copilot's Pull Requests is an important step — treat it like any code review, checking for correctness, security, and alignment with your requirements.
- Azure Container Apps provides a straightforward way to deploy containerized AI agent applications with built-in scaling and managed infrastructure.

Click **Next** to proceed to the following section of the lab.
