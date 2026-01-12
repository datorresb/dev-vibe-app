# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

Development playground for exploring AI-assisted workflows and writing technical blog content. Focus areas:

- **Beads** (`bd`): Task memory system for agents - tracks plans with dependencies in JSONL
- **Superpowers Marketplace**: Claude Code plugins (`/brainstorm`, `/write-plan`, `/execute-plan`)
- Building conversational apps with LangGraph + Azure OpenAI
- UI options: Chainlit (Phase 0 POC), React + AG-UI + CopilotKit (target)

## Development Environment

- **Container**: Dev Container with Python 3.13 (Bookworm) + Node LTS
- **Python Package Manager**: `uv` (modern, fast)
- **PYTHONPATH**: Includes `src/` and project root
- **Azure OpenAI**: Managed Identity (MSI) auth - run `az login` for local dev

## Tools

```bash
# Beads - task memory for agents (install: go install github.com/steveyegge/beads/cmd/bd@latest)
bd init              # Initialize beads in repo
bd prime             # Load context for agent
bd setup claude      # Configure Claude Code hooks

# Superpowers - Claude Code plugins (install via Superpowers Marketplace)
/brainstorm          # Generate ideas
/write-plan          # Create structured plan
/execute-plan        # Execute plan step by step
```

## Blog Writing

Use `/blog-manager` skill for all blog tasks. Three-layer model:

1. **Material** (`ideas/`): Reusable ideas with status tracking
2. **Perspective** (`perspectives/`): Writing styles
3. **Output** (`.draft/`): Generated articles

Platforms: EsPersonal (Spanish), dev.to/Medium (English)

## Principles

- **Single Responsibility**: Each component does one thing
- **Latest Versions**: No version pinning - install with latest
- **Plan First**: In planning mode, focus on design, avoid writing code
