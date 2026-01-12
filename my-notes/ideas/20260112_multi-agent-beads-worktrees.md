---
status: in-progress
priority: high
tags: [beads, claude-code, multi-agent, git-worktrees, parallel]
created: 2026-01-12
source_path: null
source_feature: "Orquestar múltiples agentes Claude con Beads y git worktrees"
published_to: []
---

# Múltiples Agentes Claude en Paralelo con Beads

## Qué quiero escribir

Tutorial práctico que muestra cómo orquestar múltiples sesiones de Claude Code trabajando en paralelo, usando:
- **Git worktrees** para aislar cada agente en su directorio
- **Beads** como backlog compartido (sincronizado via git)
- El flujo de "reclamar tarea → trabajar → sync → push"

## Público objetivo

- Devs que ya usan Claude Code
- Nivel: intermedio (saben git, han usado Claude Code)
- Quieren maximizar productividad con múltiples agentes

## Puntos clave

1. El humano orquesta, Claude ejecuta
2. Cada agente en su worktree (sin conflictos de archivos)
3. Beads sincroniza el backlog via `.beads/issues.jsonl`
4. IDs hash (`bd-a1b2`) previenen colisiones de merge
5. `bd sync` + `git push` al terminar cada sesión

## Referencias

- Anthropic best practices: https://www.anthropic.com/engineering/claude-code-best-practices
- Beads AGENTS.md: https://github.com/steveyegge/beads/blob/main/AGENTS.md
- Git worktrees: https://git-scm.com/docs/git-worktree

## Diseño del artículo

### Lector
- Conoce Claude Code básico
- Sabe usar git
- No necesita explicación de qué es un worktree (pero sí cómo usarlo)

### Tipo de introducción
- Desde un problema: "tienes 5 tareas independientes y un solo Claude"

### Estilo
- Tutorial paso a paso con ejemplo real
- Diagrama de arquitectura

### Visualización
- Diagrama ASCII/Mermaid del flujo
- Comandos con output esperado
