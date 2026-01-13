// Azure Container Registry module
// Provides a private container registry for storing Docker images

@description('Name of the container registry')
param name string

@description('Azure region for the container registry')
param location string

@description('Environment tag (dev, staging, prod)')
param environment string

resource containerRegistry 'Microsoft.ContainerRegistry/registries@2023-07-01' = {
  name: name
  location: location
  sku: {
    name: 'Basic'
  }
  properties: {
    adminUserEnabled: true
  }
  tags: {
    Environment: environment
    Service: 'container-registry'
  }
}

@description('The login server URL for the container registry')
output loginServer string = containerRegistry.properties.loginServer

@description('The name of the container registry')
output name string = containerRegistry.name

@description('The resource ID of the container registry')
output resourceId string = containerRegistry.id
