
# Provisioning infrastructure in the Azure Cloud

This document describes how to set up your infrastructure for deployment, here are presented two options:

1. Deploy automatically by running the infrastructure pipeline.
2. Run each command individually through the Azure CLI.

## Requirements

*Replace the placeholder #VALUE# with the desired value*

1. [Create an Azure subscription](https://azure.microsoft.com/en-us/free/) or use an existing one.

2. Create an Azure DevOps subscription, going to [Azure DevOps.](https://devops.azure.com/)

3. Create an [Azure DevOps project](https://docs.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops&tabs=browser).

4. Create an account in the Docker Hub [Docker Hub](https://hub.docker.com/)

5. Create a **public** [Docker Hub repository](https://docs.docker.com/docker-hub/).

> Login into [Docker Hub](https://hub.docker.com/) portal and create a repository through the user interface.

6. Install [Azure CLI](https://docs.microsoft.com/nl-nl/cli/azure/install-azure-cli).

7. Once the Azure CLI is installed, login into the Azure Cloud using the Azure CLI

> `az login`

8. Create a resource group within your subscription:

>`az group create --location westeurope --name #GROUPNAME#`

> Example: `az group create --location westeurope --name mygroupapi`

- Note 1: the `az group create` must always be run regardless of the chosen option (1 or 2)

- Note 2: we are creating a location in westeurope, for more options type: `az account list-locations`

9. In Azure DevOps, inside of your project, create a [Service Connection to the Azure Cloud](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops&tabs=yaml) by going to: Project Settings / Service Connections / Azure Resource Manager

10. In Azure DevOps, inside of your project, create a service connection to the Docker Hub, by going to: Project Settings / Service Connections / Docker registry / Docker Hub

## (Option 1) - Infrastructure Pipeline

Once you have the requirements set up, follow these small steps to have your infrastructure up and running:

1. Create the infrastructure by setting up the `infrastructure_pipeline.yml` pointing to your GitHub repository.

> In Azure DevOps go to: Pipelines / Create Pipeline. Select the `infrastructure_pipeline.yml` file from your repository and save it.

> The first time you'll be requested to Authorize GitHub to access your Azure DevOps project.

2. Run the `infrastructure_pipeline.yml` from the Azure DevOps as it will automatically run the commands from the (Option 2)

3. From the command line interface, run the command `az webapp deployment container show-cd-url -g #GROUPNAME# --name #WEBAPPNAME#` grab the returned url and add it to the [Docker Hub page as a webhook](https://docs.docker.com/docker-hub/webhooks/#:~:text=To%20create%20a%20webhook,%20visit,Provide%20a%20destination%20webhook%20URL.).

## (Option 2) - Manually through the Azure CLI

1. Create an azure app service plan (B1 - Basic)

>`az appservice plan create -g #GROUPNAME# -n #APPSERVICENAME# --is-linux --sku B1`

2. Create an azure web app attached to the previously created Azure App Service Plan

> `az webapp create --name #WEBAPPNAME# -g #GROUPNAME# --plan #APPSERVICENAME# -i #DOCKERREPOSITORY#`

*"#DOCKERREPOSITORY# -> `repository/image:tag, e.g: mydockerhubusername/pythonapiazuretemplate:latest` "*

3. Configure the repository url for Docker Hub (For Public repositories)

>`az webapp config container set --name #WEBAPPNAME# -g #GROUPNAME# -r https://index.docker.io/v1`

4. Enable Continuous deployment (Automatically updates webapp after each new image push)

>`az webapp deployment container config -g #GROUPNAME# --enable-cd true --name #WEBAPPNAME#`

The command above will give you back the url which you should add as one webhook within your Docker Hub profile.

## Build and deploy through Azure Pipelines

1. Setup the `build_pipeline.yml` pointing to your GitHub repository.

> In Azure DevOps Go to: Pipelines / Create Pipeline. Select the `build_pipeline.yml` from your repository and save it.

This pipeline will automatically run after every commit in your `develop` or `main` branch and your API in Azure will get automatically updated with the latest version of your image. You can change this behaviour by changing the `trigger` in the `build_pipeline.yml` to point to your desired branch repository.
