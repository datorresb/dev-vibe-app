// Azure App Service module
// Deploys a Linux container-based App Service with Managed Identity
// Uses Key Vault references for secrets

@description('Name of the App Service Plan')
param appServicePlanName string

@description('Name of the App Service')
param appServiceName string

@description('Azure region for the App Service')
param location string

@description('Environment tag (dev, staging, prod)')
param environment string

@description('Name of the container registry')
param containerRegistryName string

@description('Name of the Key Vault for secrets')
param keyVaultName string

// App Service Plan - Linux container hosting
resource appServicePlan 'Microsoft.Web/serverfarms@2023-01-01' = {
  name: appServicePlanName
  location: location
  kind: 'linux'
  sku: {
    name: 'B1'
    tier: 'Basic'
  }
  properties: {
    reserved: true // Required for Linux
  }
  tags: {
    Environment: environment
    Service: 'app-service-plan'
  }
}

// App Service - Container-based web app with Managed Identity
resource appService 'Microsoft.Web/sites@2023-01-01' = {
  name: appServiceName
  location: location
  kind: 'app,linux,container'
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    serverFarmId: appServicePlan.id
    httpsOnly: true
    siteConfig: {
      linuxFxVersion: 'DOCKER|${containerRegistryName}.azurecr.io/chainlit-app:latest'
      healthCheckPath: '/health'
      appSettings: [
        {
          name: 'WEBSITES_ENABLE_APP_SERVICE_STORAGE'
          value: 'false'
        }
        {
          name: 'DOCKER_REGISTRY_SERVER_URL'
          value: 'https://${containerRegistryName}.azurecr.io'
        }
        {
          name: 'DOCKER_ENABLE_CI'
          value: 'true'
        }
        {
          name: 'AZURE_OPENAI_ENDPOINT'
          value: '@Microsoft.KeyVault(VaultName=${keyVaultName};SecretName=azure-openai-endpoint)'
        }
        {
          name: 'AZURE_OPENAI_CHAT_DEPLOYMENT'
          value: '@Microsoft.KeyVault(VaultName=${keyVaultName};SecretName=azure-openai-chat-deployment)'
        }
        {
          name: 'AZURE_OPENAI_API_VERSION'
          value: '@Microsoft.KeyVault(VaultName=${keyVaultName};SecretName=azure-openai-api-version)'
        }
      ]
    }
  }
  tags: {
    Environment: environment
    Service: 'app-service'
  }
}

@description('The URL of the deployed App Service')
output appUrl string = 'https://${appService.properties.defaultHostName}'

@description('The name of the App Service')
output appName string = appService.name

@description('The principal ID of the system-assigned managed identity')
output principalId string = appService.identity.principalId
