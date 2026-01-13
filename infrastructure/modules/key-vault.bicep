@description('Key Vault name')
param name string

@description('Location for resources')
param location string

@description('Environment name')
param environment string

@description('App Service principal ID for access policy')
param appServicePrincipalId string

@description('Azure OpenAI configuration secrets')
@secure()
param azureOpenAIEndpoint string

@secure()
param azureOpenAIChatDeployment string

param azureOpenAIApiVersion string

resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' = {
  name: name
  location: location
  properties: {
    sku: {
      family: 'A'
      name: 'standard'
    }
    tenantId: subscription().tenantId
    enableRbacAuthorization: true
    enabledForDeployment: false
    enabledForDiskEncryption: false
    enabledForTemplateDeployment: true
  }
  tags: {
    Environment: environment
    Service: 'DevVibeApp'
  }
}

// Secrets
resource secretEndpoint 'Microsoft.KeyVault/vaults/secrets@2023-07-01' = {
  parent: keyVault
  name: 'azure-openai-endpoint'
  properties: {
    value: azureOpenAIEndpoint
  }
}

resource secretChatDeployment 'Microsoft.KeyVault/vaults/secrets@2023-07-01' = {
  parent: keyVault
  name: 'azure-openai-chat-deployment'
  properties: {
    value: azureOpenAIChatDeployment
  }
}

resource secretApiVersion 'Microsoft.KeyVault/vaults/secrets@2023-07-01' = {
  parent: keyVault
  name: 'azure-openai-api-version'
  properties: {
    value: azureOpenAIApiVersion
  }
}

// Role assignment for App Service to read secrets
resource keyVaultSecretsUser 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(keyVault.id, appServicePrincipalId, 'Key Vault Secrets User')
  scope: keyVault
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', '4633458b-17de-408a-b874-0445c86b69e6') // Key Vault Secrets User
    principalId: appServicePrincipalId
    principalType: 'ServicePrincipal'
  }
}

output vaultUri string = keyVault.properties.vaultUri
output vaultName string = keyVault.name
output secretUriEndpoint string = secretEndpoint.properties.secretUri
output secretUriChatDeployment string = secretChatDeployment.properties.secretUri
output secretUriApiVersion string = secretApiVersion.properties.secretUri
