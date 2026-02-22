# Migrate to Code, Build the UI, and Test Locally

In this section, you will migrate the agent you've created in AI Toolkit to a code-based workflow, use **GitHub Copilot Chat in Agent mode** to build a complete web UI for your agent in one go, and then test the full application locally.

The AI Toolkit provides generated code for agents created in Agent Builder. You can choose your preferred SDK as well as programming language. Once you have your code file, you'll use GitHub Copilot to build a chat UI around it and run everything on your machine.

## Step 1: Generate the Code

In Agent Builder, scroll down towards the bottom of the left side of the screen and select **View Code**.

![View code button.](../../img/view-code.png)

When prompted, select your preferred client SDK (e.g. *Microsoft Agent Framework*) and programming language (e.g. *Python*). Once the new file is created, save the file to your workspace.

## Step 2: View the Code

Before running the script, review the content of the file as there may be placeholders that must be modified before running. If you need assistance understanding the script logic, you could leverage GitHub Copilot Chat in **Ask** mode.

To access GitHub Copilot Chat, select the **Toggle Chat** icon at the top of the Visual Studio Code window.

![Toggle chat button.](../../img/toggle-chat.png)

> [!NOTE]
> If asked to log in at your first interaction with Copilot, select **Sign-in** -> **Continue with GitHub**. Then click on **Continue** to proceed with your GitHub account when redirected to the GitHub sign-in page.

Save the generated code file to your workspace as 'src/python/cora-app.py'. Be sure to have the file active so that GitHub Copilot Chat can use the file as context. Alternatively, you could reference the specific file itself in your prompt to GitHub Copilot Chat.

![GitHub Copilot Chat in Ask mode.](../../img/ghcp-ask-mode.png)

> [!NOTE]
> If you see a '+' icon besides the file name, that means cora-app.py is suggested as context by GitHub Copilot Chat, but it's not yet added. Click on the '+' icon to add the file as context.
>
> ![Suggested file as context](../../img/suggested_file_context.png)

For example try the following prompt:

```
Explain what's happening in this script.
```

If there's any changes that need to be made, you could switch to **Agent** mode and request the changes to be made. You'll be requested to approve any file changes prior to committing the file updates to the script.

### Update the Project Endpoint and Model Deployment

Before running the code, you **must** replace the placeholder values at the top of `src/python/cora-app.py` with the AI Foundry project endpoint and model deployment name you created earlier in the lab.

Open `src/python/cora-app.py` and locate these two lines near the top of the file:

```python
ENDPOINT = "https://aifoundry-aman.services.ai.azure.com/api/projects/project-aman"
MODEL_DEPLOYMENT_NAME = "gpt-5-mini-aman"
```

Replace them with your own values:

- **`ENDPOINT`** — Your AI Foundry project endpoint. You can find this in the Azure AI Foundry portal on your project's **Overview** page (it follows the format `https://<your-ai-foundry-account>.services.ai.azure.com/api/projects/<your-project-name>`).
- **`MODEL_DEPLOYMENT_NAME`** — The name of the model deployment you created earlier (e.g., `gpt-5-mini-<your-suffix>`).

For example:

```python
ENDPOINT = "https://aifoundry-jane.services.ai.azure.com/api/projects/project-jane"
MODEL_DEPLOYMENT_NAME = "gpt-5-mini-jane"
```

> [!IMPORTANT]
> If you skip this step, the agent will fail to connect to your AI Foundry model at runtime. Make sure both values match the resources you provisioned in the earlier steps of this lab.

## Step 3: Install Dependencies and Run the Agent Code

Before building a UI, first verify that the agent code itself works correctly.

1. Open a terminal in Visual Studio Code by selecting **Terminal** -> **New Terminal** from the top menu.

2. Authenticate to Azure (the agent needs access to your AI Foundry model):

   ```
   az login --use-device-code
   ```

   You'll be prompted to open a browser window and fill in a code to complete the authentication. Once back in the terminal, press **Enter** to confirm the Azure subscription selection.

3. Install the required dependencies:

   ```
   pip install -r src/python/requirements.txt
   ```

   > [!NOTE]
   > A pre-configured `src/python/cora-app.py` with the correct imports, API calls, MCP server paths, and database connection string is already included in the repository if you need a working reference.

4. Navigate to the directory where the code file is saved:

   ```
   cd src/python
   ```

5. Run the agent code:

   ```
   python cora-app.py
   ```

6. The script will run a series of pre-defined conversation turns against the Cora agent. Verify that:
   - The agent connects to your AI Foundry model successfully
   - The MCP server starts and the agent can query the product database
   - The agent responds with relevant product information

> [!TIP]
> If you encounter any errors, you can paste the error message into GitHub Copilot Chat in Agent mode and ask it to fix the issue. Agent mode is great at diagnosing and resolving runtime errors.

## Step 4: Build the Web UI with GitHub Copilot Agent Mode

With the agent code verified, you'll now use GitHub Copilot Chat in **Agent** mode to create a complete web UI for the Cora agent in one go. Agent mode can create files, edit code, and run terminal commands — all with your approval at each step.

1. Open **GitHub Copilot Chat** and switch to **Agent** mode using the mode selector at the top of the chat panel.

2. Make sure the file `src/python/cora-app.py` is referenced as context. You can add it by typing `#file` in the chat input and selecting the file, or by having it open in the editor.

3. Paste the following prompt into the chat:

   ```
   Using the Cora agent code in src/python/cora-app.py as the foundation, 
   create a complete web-based chat UI for the agent. 

   Requirements:
   - Use Chainlit or Streamlit as the UI framework
   - Create the UI file at src/python/cora-ui.py
   - The UI should have a clean, professional look suitable for a retail brand
   - Include a chat interface where users can type messages and see agent responses
   - Display "Zava" branding in the header
   - Support image attachments so customers can upload photos of their DIY projects
   - Integrate with the existing Cora agent logic and MCP server
   - Update src/python/requirements.txt with any new dependencies needed

   Also create a Dockerfile in src/python/ that packages the application 
   into a container with all dependencies.
   ```

4. Review each file creation and edit that Agent mode proposes. You will be prompted to **approve** or **reject** each change. Review carefully and click **Accept** to proceed with each step.

> [!TIP]
> The more detailed your prompt is, the better the results will be. Feel free to add additional requirements like color schemes, layout preferences, or specific features you'd like in the UI.

> [!NOTE]
> Agent mode may make multiple file changes — creating the UI file, updating requirements.txt, and creating a Dockerfile. Review each change before accepting.

## Step 5: Run and Test the UI Locally

With the UI code generated, install any new dependencies and launch the application.

1. Install the updated dependencies (in case new packages were added for the UI):

   ```
   pip install -r src/python/requirements.txt
   ```

2. Run the UI application:

   ```
   python cora-ui.py
   ```

   > [!TIP]
   > The exact run command may differ depending on the UI framework that Agent mode chose (e.g., `chainlit run cora-ui.py` for Chainlit or `streamlit run cora-ui.py` for Streamlit). Check the generated code or ask Copilot Chat for the correct command.

3. Once the application starts, open the URL displayed in the terminal (typically `http://localhost:8000` or `http://localhost:8501`) in your browser.

4. In the web UI, type a test message such as:

   ```
   What type of paint does Zava sell?
   ```

5. Verify that:
   - The chat UI loads correctly with Zava branding
   - The agent responds with relevant product information from the catalog
   - The MCP server connection is working (the agent can query the product database)

6. (Optional) If image attachments are supported, test by uploading a photo and asking the agent about it.

> [!TIP]
> If you encounter any errors, you can paste the error message into GitHub Copilot Chat in Agent mode and ask it to fix the issue.

## Key Takeaways

- Agent Builder automatically generates code for agents in multiple programming languages and SDKs, facilitating easy migration from prototype to production.
- Code files may contain placeholders that need modification before execution, requiring developers to understand and adapt the generated logic for their specific needs.
- GitHub Copilot Chat in **Agent mode** can build a complete web UI, create Dockerfiles, and update dependencies — all from a single prompt, dramatically accelerating the development workflow.
- Testing locally before deploying ensures that the agent logic, MCP server connection, and UI all work correctly together.

Click **Next** to proceed to the following section of the lab.
