// Main Bicep template for DevVibe App infrastructure
// Orchestrates deployment of ACR, App Service, and Key Vault

targetScope = 'resourceGroup'

@description('Environment name (dev, staging, prod)')
param environment string = 'dev'

@description('Azure region for all resources')
param location string = resourceGroup().location

@description('Azure OpenAI endpoint URL')
@secure()
param azureOpenAIEndpoint string

@description('Azure OpenAI chat deployment name')
@secure()
param azureOpenAIChatDeployment string

@description('Azure OpenAI API version')
param azureOpenAIApiVersion string = '2024-12-01-preview'

// Resource naming variables
var prefix = 'devvibeapp'
var containerRegistryName = '${prefix}${environment}acr'
var appServicePlanName = '${prefix}-${environment}-plan'
var appServiceName = '${prefix}-${environment}-app'
var keyVaultName = '${prefix}-${environment}-kv'

// Container Registry module
module containerRegistry 'modules/container-registry.bicep' = {
  name: 'containerRegistry'
  params: {
    name: containerRegistryName
    location: location
    environment: environment
  }
}

// App Service module (deployed first to get principal ID)
module appService 'modules/app-service.bicep' = {
  name: 'appService'
  params: {
    appServicePlanName: appServicePlanName
    appServiceName: appServiceName
    location: location
    environment: environment
    containerRegistryName: containerRegistry.outputs.name
    keyVaultName: keyVaultName
  }
}

// Key Vault module (needs App Service principal ID for access)
module keyVault 'modules/key-vault.bicep' = {
  name: 'keyVault'
  params: {
    name: keyVaultName
    location: location
    environment: environment
    appServicePrincipalId: appService.outputs.principalId
    azureOpenAIEndpoint: azureOpenAIEndpoint
    azureOpenAIChatDeployment: azureOpenAIChatDeployment
    azureOpenAIApiVersion: azureOpenAIApiVersion
  }
}

@description('The URL of the deployed App Service')
output appServiceUrl string = appService.outputs.appUrl

@description('The login server URL for the container registry')
output containerRegistryLoginServer string = containerRegistry.outputs.loginServer

@description('The name of the resource group')
output resourceGroupName string = resourceGroup().name

@description('Key Vault URI')
output keyVaultUri string = keyVault.outputs.vaultUri
