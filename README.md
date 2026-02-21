# Create AI Agents using Microsoft Foundry, AI Toolkit and GitHub Copilot

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://aka.ms/MicrosoftFoundry-Ignite25)
[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=adff2f&logoColor=fff)](https://aka.ms/MicrosoftFoundryForum-Ignite25)

### Workshop Description

In this hands-on workshop, you'll use the AI Toolkit (AITK), Microsoft Foundry, and GitHub Copilot in VS Code to explore and compare the latest multimodal and reasoning models from the Model Catalog. Learn how to augment models for a real-world business scenario using prompt and context engineering. Prototype an agent using the AITK Agent Builder, equip it with the right tools via MCP, and export it to Microsoft Agent Framework code. Then, leverage GitHub Copilot Coding Agent to build a web UI and Azure deployment configuration — all from a single GitHub Issue.

### 🧠 Learning Outcomes

By the end of this session, learners will be able to:

-  Explore and compare models to select the best fit for their business scenario
-  Augment models with prompts and data to get more accurate and grounded responses 
-  Prototype an agent by combining models and instructions with tools via MCP (Model Context Protocol)
-  Export agent code and use GitHub Copilot Coding Agent to build a UI and prepare Azure deployment

### Note for Self-Learners
The lab manual provided in this repository is designed for instructor-led sessions, where a lab environment is pre-provisioned for participants, equipped with an Azure subscription, necessary resources, and a VM with Visual Studio Code and required extensions pre-installed.
However, self-learners can still complete the lab, but they'll need to set up some prerequisites on their own, including:
- An Azure subscription with a provisioned Microsoft Foundry Project and a gpt-5-mini model instance. You can use the following button to deploy the required resources:[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fmicrosoft%2Fignite25-LAB512-prototyping-multimodal-agents-with-microsoft-foundry-and-the-ai-toolkit%2Frefs%2Fheads%2Fmain%2Flab%2Fscript%2FLab512-arm-template.json)
- A GitHub account. If you don't have one follow the instructions at the end of the [Get Started](lab/instructions/01_Get_Started.md) guide to create a free GitHub account.

### 💻 Technologies Used

1. [AI Toolkit for Visual Studio Code](https://code.visualstudio.com/docs/intelligentapps/overview)
1. [GitHub Models](https://github.com/features/models)
1. [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/foundry-models-overview)
1. [MCP - Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro)
1. [GitHub Copilot](https://github.com/features/copilot)
1. [GitHub Copilot Coding Agent](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent)
1. [Microsoft Agent Framework](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/agent-framework)
1. [Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/overview)

### 🌟 Microsoft Learn MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D)

The Microsoft Learn MCP Server is a remote MCP Server that enables clients like GitHub Copilot and other AI agents to bring trusted and up-to-date information directly from Microsoft's official documentation. Get started by using the one-click button above for VSCode or access the [mcp.json](.vscode/mcp.json) file included in this repo.

For more information, setup instructions for other dev clients, and to post comments and questions, visit our Learn MCP Server GitHub repo at [https://github.com/MicrosoftDocs/MCP](https://github.com/MicrosoftDocs/MCP). Find other MCP Servers to connect your agent to at [https://mcp.azure.com](https://mcp.azure.com).

*Note: When you use the Learn MCP Server, you agree with [Microsoft Learn](https://learn.microsoft.com/en-us/legal/termsofuse) and [Microsoft API Terms](https://learn.microsoft.com/en-us/legal/microsoft-apis/terms-of-use) of Use.*

### 📚 Resources and Next Steps

| Resources          | Links                             | Description        |
|:-------------------|:----------------------------------|:-------------------|
| Microsoft Foundry Community Discord | [![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://aka.ms/MicrosoftFoundry-Ignite25)| Connect with the Microsoft Foundry Community! |
| Microsoft Learn | [https://learn.microsoft.com](https://learn.microsoft.com) | Continue learning on Microsoft Learn |

## Content Owners

<!-- TODO: Add yourself as a content owner
1. Change the src in the image tag to {your github url}.png
2. Change INSERT NAME HERE to your name
3. Change the github url in the final href to your url. -->

<table>
<tr>
    <td align="center"><a href="http://github.com/carlotta94c">
        <img src="https://github.com/carlotta94c.png" width="100px;" alt="Carlotta Castelluccio"
"/><br />
        <sub><b> Carlotta Castelluccio
</b></sub></a><br />
            <a href="https://github.com/carlotta94c" title="talk">📢</a> 
    </td>
    <td align="center"><a href="http://github.com/carlotta94c">
        <img src="https://github.com/aprilgittens.png" width="100px;" alt="April Gittens
"/><br />
        <sub><b>April Gittens
</b></sub></a><br />
            <a href="https://github.com/aprilgittens" title="talk">📢</a> 
    </td>
</tr></table>


## 🚀 Try Azure for Free!

Ready to build, experiment, or scale your next project? Kick things off with an Azure Free Trial and get access to popular services, generous monthly credits, and the tools you need to ship fast. 👉 Start your free journey here: https://aka.ms/devrelft

## Contributing

This project welcomes contributions and suggestions. For detailed contribution guidelines, including our branch protection workflow and pull request requirements, please see [CONTRIBUTING.md](CONTRIBUTING.md).

Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit [Contributor License Agreements](https://cla.opensource.microsoft.com).

When you submit a pull request, a CLA bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
