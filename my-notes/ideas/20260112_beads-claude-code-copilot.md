---
status: in-progress
priority: high
tags: [beads, claude, copilot, ai]
created: 2026-01-12
source_path:
source_feature: "usar Beads (bd) como memoria de tareas para agentes"
used_in: []
published_to: []
---

# Beads (bd) para Claude Code y Copilot (VS Code)

## Qué quiero escribir

- Qué es Beads (bd) y por qué ayuda a los agentes (memoria persistente y tareas con dependencias)
- Setup mínimo en un repo (bd init + AGENTS.md)
- Integración recomendada en Claude Code: CLI + hooks (`bd setup claude` y `bd prime`)
- Uso opcional del plugin de Claude Code (slash commands /beads:…)
- Alternativa MCP (beads-mcp) para entornos sin shell
- Cómo trasladar el flujo a VS Code + Copilot (misma disciplina, distintas interfaces)
- Deep-dive: trade-offs CLI/hooks vs MCP (overhead de contexto)

## Público objetivo

- Devs que usan Claude Code o VS Code Copilot
- Nivel: intermedio (saben usar terminal y git; no necesitan saber Go)

## Referencias

- Repo oficial: https://github.com/steveyegge/beads
- Instalación (bd): https://github.com/steveyegge/beads/blob/main/docs/INSTALLING.md
- Integración Claude Code (diseño + hooks): https://github.com/steveyegge/beads/blob/main/docs/CLAUDE_INTEGRATION.md
- Plugin Claude Code: https://github.com/steveyegge/beads/blob/main/docs/PLUGIN.md
- beads-mcp (PyPI): https://pypi.org/project/beads-mcp/
- Notas locales (curación de links): docs/notes/links.md

## Diseño del artículo

### Lector
- Conocimientos previos: git básico, terminal, usar un asistente (Copilot/Claude)
- Necesidad de explicar conceptos: sí, definir “memoria del agente”, “JSONL”, “hooks”, “MCP” en 1–2 líneas

### Tipo de introducción
- Desde un problema: planes en Markdown se rompen / el agente olvida el hilo / multitarea

### Estilo
- Tutorial paso a paso + secciones de deep-dive para trade-offs
- Evitar: marketing exagerado; promesas tipo “magia”

### Visualización
- Diagrama simple (Mermaid) del flujo CLI/hooks y de la opción MCP
