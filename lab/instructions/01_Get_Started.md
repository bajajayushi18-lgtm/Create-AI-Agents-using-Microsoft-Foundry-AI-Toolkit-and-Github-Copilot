# Get started

> [!TIP]
> What is the **AI Toolkit(AITK)**? [The AI Toolkit (AITK)](https://code.visualstudio.com/docs/intelligentapps/overview) is an extension for Visual Studio Code that provides a unified interface to access and interact with various AI models and services. It allows users to easily explore, compare, and utilize different AI models from multiple providers, both proprietary and open source, hosted on several platforms, such as Github, Microsoft Foundry or even locally. With AITK, developers can streamline their Generative AI development workflow by integrating model selection, prompt engineering, and agent prototyping and testing directly within their code editor.

## Sign in to the Lab VM

As a first step, log in to the lab Virtual Machine using the credentials provided by your instructor.

> [!TIP]
> You can always click on the images to enlarge them, if needed.

## Clone the Workshop Repository

In this workshop, we will be using **Visual Studio Code** on the lab VM to work with the workshop code and resources. VS Code and the required extensions are already pre-installed on the VM.

1. Open **Visual Studio Code** from the desktop or Start menu.

2. Open the integrated terminal in VS Code (**Terminal** > **New Terminal** or `Ctrl+\``).

3. Clone the workshop repository by running:
   ```
   git clone https://github.com/testinguser2_GHCPAI04/ignite25-LAB512-prototyping-multimodal-agents-with-microsoft-foundry-and-the-ai-toolkit.git
   ```

4. Once the clone completes, open the cloned folder in VS Code: **File** > **Open Folder** and navigate to the cloned repository folder.

5. You should now see the workshop files and folders in the Explorer sidebar.

## Login to Azure

In Visual Studio Code, you should be able to see two extensions already installed: 
- The **AI Toolkit**: this is the extension we will be using to interact with various AI models and services in this lab.
- The **Azure AI Foundry** extension: it's installed as a bundle of the AI Toolkit and provides access to Microsoft Foundry hosted models. 
If they are correctly installed, you should see their icons in the left sidebar of VS Code, as per screenshot below.

![Installed extensions](../../img/installed_extensions.png)

> [!TIP]
> If you don't see the icons, click on the ellipsis (...) at the bottom of the sidebar to see the full list of installed extensions. If they are not installed, search for "AI Toolkit" and "Azure AI Foundry" in the Extensions Marketplace (Ctrl+Shift+X) and install them.

> [!WARNING]
> Please make sure you are using the correct versions of the VS Code extensions as specified by your instructor, to ensure consistency with the lab manual instructions.

Now click on the Azure AI Foundry extension icon, and then click on **Set Default Project** -> **Sign in to Azure**.

![Set Default Project](../../img/set_default_project.png)

You'll be prompted with a popup to confirm with the Azure login. Click **Allow**.

![Azure Login Popup](../../img/azure_login_popup.png)

Next, you'll be redirected to a browser window to complete the login process. Enter the Azure credentials provided by your instructor.

> [!NOTE]
> You'll be asked to confirm if you want to allow the automatic sign-in to all desktop apps and websites on the device. Click **Yes, all apps** to proceed. Then click **Done** to complete the login process and return to VS Code.

Back in VS Code, you'll be asked to select the Foundry project to use. Select the only available option, which is the project pre-deployed for this workshop.

![Select Project](../../img/select_project.png)

## Need a GitHub account?

If you need a GitHub account to access GitHub-hosted models in the AI Toolkit, follow these steps:

1. Navigate to [https://github.com/signup](https://github.com/signup).
2. Enter a personal email address, create a password, and choose a username.
3. Select your Country/Region and agree to the terms of service.
4. Click on the **Create account** button and wait for the verification email to arrive in your inbox.
5. Copy the verification code from the email and paste it into the verification field on the GitHub website. Then click on **Continue**.

> [!WARNING]
> If your personal GitHub account is a free-tier one, you will have some limitations in the range of GitHub-hosted models you can access in the AI Toolkit Model Catalog. For example, you won't be able to use the GPT-5 family of models. You can still proceed with the lab using available models (recommended: OpenAI gpt-4.1).


## Ready to start

That covers the necessary setup to work with the AI Toolkit in VScode and Microsoft Foundry hosted models. We will now move forward to begin exploring the Model Catalog and interacting with the models.
Click **Next** to proceed to the following section of the lab.