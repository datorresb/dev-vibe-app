# Phase 1.5: Containerization & Azure Deployment Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Containerize existing Chainlit app and deploy to Azure App Service with CI/CD

**Architecture:** Multi-stage Docker build → Azure Container Registry → App Service deployment via GitHub Actions, with MSI authentication for Azure OpenAI

**Tech Stack:** Docker, GitHub Actions, Azure Bicep, Azure App Service, Azure Container Registry

---

## Task 1: Local Containerization

**Files to create:**
- `backend/Dockerfile` - Multi-stage build with Python 3.13-slim and uv
- `backend/docker-compose.yml` - Local development with volume mounts
- `backend/.env.local` - Environment template for containerized dev
- `backend/.dockerignore` - Exclude dev files from image

**Implementation:**

1. Create Dockerfile with multi-stage build
   - Stage 1 (builder): Install dependencies with `uv`
   - Stage 2 (runtime): Copy venv, application code, expose port 8000

2. Create Docker Compose for local development
   - Single service mounting source code as read-only volumes
   - Health check configuration
   - Environment file reference

3. Create environment template with Azure OpenAI variables

4. Create .dockerignore excluding .venv, __pycache__, tests, .git

5. Add health check endpoint to `backend/chainlit_app.py`
   - FastAPI endpoint at `/health` returning JSON status

6. Test: `docker build -t chainlit-app:local .`

7. Test: `docker-compose up -d` and verify health check

8. Commit changes

---

## Task 2: Azure Infrastructure with Bicep

**Files to create:**
- `infrastructure/main.bicep` - Main orchestration template
- `infrastructure/modules/container-registry.bicep` - ACR module
- `infrastructure/modules/app-service.bicep` - App Service module
- `infrastructure/parameters.json` - Environment parameters

**Resources to provision:**
- Azure Container Registry (Basic SKU, admin enabled)
- App Service Plan (B1 tier, Linux)
- App Service (Container-based, MSI enabled)

**Implementation:**

1. Create main Bicep template
   - Parameters: environment, location, azureOpenAI config
   - Variables for resource naming (devvibeapp prefix)
   - Module references for ACR and App Service
   - Outputs: app URL, ACR login server

2. Create Container Registry module
   - Basic SKU with admin user enabled
   - Environment tagging

3. Create App Service module
   - Linux App Service Plan (B1)
   - Container app with System-Assigned Managed Identity
   - Health check path: `/health`
   - App settings for Azure OpenAI and Docker configuration
   - HTTPS enforced

4. Create parameters file with environment defaults

5. Test: `az bicep build --file infrastructure/main.bicep`

6. Commit infrastructure code

---

## Task 3: GitHub Actions CI/CD Pipeline

**Files to create:**
- `.github/workflows/pr-validation.yml` - PR checks
- `.github/workflows/main-deploy.yml` - Production deployment

**PR Validation Workflow triggers:**
- Pull requests to main
- Paths: backend/**, .github/workflows/**, infrastructure/**

**PR Validation steps:**
1. Build container image (no push)
2. Security scan with Trivy
3. Container startup test
4. Bicep template validation

**Main Deploy Workflow triggers:**
- Push to main branch
- Paths: backend/**, infrastructure/**, workflow file

**Main Deploy steps:**
1. Build and push image to ACR (tags: latest, branch-sha)
2. Deploy infrastructure with Bicep
3. Deploy container to App Service
4. Health check verification (10 retries, 30s intervals)

**Required secrets:**
- `AZURE_CREDENTIALS` - Service principal JSON
- `AZURE_SUBSCRIPTION_ID` - Subscription ID

---

## Task 4: GitHub Secrets Configuration

**Manual steps (not automatable):**

1. Create Azure Service Principal with Contributor role on resource group

2. Configure GitHub repository secrets:
   - `AZURE_CREDENTIALS`: Service principal output
   - `AZURE_SUBSCRIPTION_ID`: Your subscription ID

3. Update `infrastructure/parameters.json` with actual Azure OpenAI values

4. Create resource group: `az group create --name rg-dev-vibe-app --location eastus`

5. Trigger deployment by pushing to main

---

## Task 5: Testing & Validation

**Local testing:**
1. Build and run with Docker Compose
2. Verify health endpoint responds
3. Test chat functionality

**Azure deployment testing:**
1. Verify GitHub Actions complete successfully
2. Test health endpoint on Azure URL
3. Test chat functionality on public URL

**CI/CD testing:**
1. Create PR with small change
2. Verify PR validation passes
3. Merge and verify deployment
4. Confirm app functionality post-deploy

**Final commit with Phase 1.5 completion summary**

---

## Success Criteria

- [ ] Chainlit app accessible via public Azure URL
- [ ] MSI authentication working with Azure OpenAI
- [ ] CI/CD pipeline functional (PR + auto-deploy)
- [ ] Local development with Docker Compose
- [ ] Container optimized for cold starts
- [ ] Security scanning in CI pipeline
- [ ] Health checks working
- [ ] Infrastructure as Code with Bicep
