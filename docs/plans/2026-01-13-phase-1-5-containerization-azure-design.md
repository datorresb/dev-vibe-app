# Phase 1.5: Containerization & Azure Deployment Design

**Date:** 2026-01-13
**Status:** Ready for Implementation
**Scope:** POC - Containerize and deploy existing Chainlit app to Azure App Service

## Overview

Phase 1.5 adds containerization and cloud deployment to the existing LangGraph + Chainlit application. This is a minimal, POC-focused approach using Docker, GitHub Actions CI/CD, and Azure App Service.

## Architecture

### Current State (Phase 1)
- LangGraph agent with Azure OpenAI integration
- Chainlit web interface
- Local development in Dev Container
- MSI authentication for Azure OpenAI

### Target State (Phase 1.5)
- Same application containerized with Docker
- Automated CI/CD with GitHub Actions
- Running on Azure App Service for Containers
- Public URL accessible

## Components

### 1. Containerization

**Dockerfile:**
- Multi-stage build for optimization
- Base: Python 3.13-slim
- Stage 1: Build with `uv` for fast dependency installation
- Stage 2: Lean runtime image
- Health check endpoint
- Port 8000 exposed

**Docker Compose (Local Development):**
- Single service for the Chainlit app
- Volume mounts for development hot reload
- `.env.local` for environment variables
- Ready for future multi-service expansion

### 2. CI/CD Pipeline

**GitHub Actions Strategy:**
- PR Workflow: Build + test + security scan
- Main Workflow: Build + push + deploy

**PR Pipeline:**
1. Build Docker image (pr-{number} tag)
2. Security scan with Trivy
3. Container startup test
4. Status comment on PR

**Main Pipeline:**
1. Build and tag (latest + {sha})
2. Push to Azure Container Registry
3. Deploy to App Service
4. Health check verification
5. Auto-rollback on failure

### 3. Azure Infrastructure (Bicep)

**Resources:**
- Resource Group: rg-dev-vibe-app
- Azure Container Registry: crdevvibeapp
- App Service Plan: B1 tier (Linux)
- App Service: Container-based, MSI enabled

**Configuration:**
- No Key Vault (POC simplicity)
- Direct App Service Application Settings
- HTTPS enforced
- Health check: /health
- Auto-scaling on CPU > 70%

### 4. Environment Configuration

**Local Development:**
- Environment variables in .env.local
- Azure OpenAI endpoint, deployment, API version

**Azure App Service Settings:**
- Same variables configured in App Service
- MSI authentication automatic
- No manual az login required

## Deployment Flow

1. **Development:** Code locally with Docker Compose
2. **PR Creation:** GitHub Actions builds and validates
3. **Merge to Main:** Auto-deployment to Azure
4. **Access:** Public URL provided by Azure App Service

## Success Criteria

- [ ] Chainlit app accessible via public Azure URL
- [ ] MSI authentication working with Azure OpenAI
- [ ] CI/CD pipeline functional
- [ ] Local development with Docker Compose
- [ ] Container optimized for cold starts

## Implementation Phases

1. **Dockerfile & Docker Compose** - Local containerization
2. **GitHub Actions** - CI/CD pipeline setup
3. **Bicep Templates** - Infrastructure as Code
4. **Azure Deployment** - First production deployment
5. **Testing & Validation** - End-to-end verification

## Notes

- POC approach: minimal complexity, maximum functionality
- No staging environment (direct to production)
- No complex secrets management
- Foundation for future React frontend (Phase 2)
