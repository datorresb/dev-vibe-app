---
status: done
priority: high
tags: [claude-code, subagents, task-tool, parallel, tutorial]
created: 2026-01-12
source_path: null
source_feature: "Usar el Task tool para lanzar subagentes en paralelo dentro de Claude Code"
published_to: []
---

# Subagentes con el Task Tool en Claude Code

## Qué quiero escribir

Tutorial que muestra cómo usar el Task tool nativo de Claude Code para lanzar subagentes en paralelo, sin necesidad de worktrees ni herramientas externas.

## Diferencia con Beads + Worktrees

| Aspecto | Task Tool | Beads + Worktrees |
|---------|-----------|-------------------|
| Orquestación | Claude orquesta automático | Humano orquesta manualmente |
| Persistencia | Solo dentro de la sesión | Persiste entre sesiones |
| Conflictos | No pueden editar mismos archivos | Cada worktree aislado |
| Setup | Cero (built-in) | Requiere bd init + worktrees |

## Público objetivo

- Devs que usan Claude Code
- Nivel: principiante a intermedio
- Quieren paralelizar sin setup extra

## Puntos clave

1. Task tool es built-in, no requiere instalación
2. Subagentes tienen contexto aislado (200k tokens cada uno)
3. Solo el resultado final vuelve al orquestador
4. Límite: 10 tareas paralelas simultáneas
5. Ideal para investigación, no para editar mismos archivos

## Referencias

- Anthropic best practices: https://www.anthropic.com/engineering/claude-code-best-practices
- Subagent docs: https://code.claude.com/docs/en/sub-agents
- Zach Wills tutorial: https://zachwills.net/how-to-use-claude-code-subagents-to-parallelize-development/
