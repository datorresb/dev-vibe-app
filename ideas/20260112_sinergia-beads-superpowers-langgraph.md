---
status: in-progress
priority: high
tags: [beads, superpowers, langgraph, chainlit, azure, tutorial]
created: 2026-01-12
source_path: /workspaces/dev-vibe-app
source_feature: "sinergia de Beads + Superpowers para crear app conversacional"
published_to: []
---

# Sinergia Beads + Superpowers: Crea un Chatbot con LangGraph

## Qué quiero escribir

Artículo práctico que muestra cómo combinar:
- **Beads** para gestionar el plan de desarrollo (memoria de tareas)
- **Superpowers** para planificar con /brainstorm, /write-plan, /execute-plan
- **LangGraph** para el backend conversacional con estado
- **Chainlit** para la UI web
- **UV** como gestor de paquetes moderno
- **Azure OpenAI GPT 5.1** como modelo (con Managed Identity)

## Flujo del artículo

1. Intro: por qué combinar estas herramientas
2. Setup del proyecto con UV
3. Usar Superpowers para planificar (/brainstorm → /write-plan)
4. Usar Beads para trackear las tareas del plan
5. Implementar el chatbot paso a paso (/execute-plan)
6. Deploy con Chainlit
7. Resumen y próximos pasos

## Stack técnico

- uv (gestor de paquetes)
- langgraph
- chainlit
- azure-identity (MSI)
- openai (Azure endpoint)

## Público objetivo

- Devs que ya conocen Claude Code
- Nivel: intermedio
- Quieren ver un caso real de desarrollo con AI-assisted workflow

## Perspectiva

- Tutorial práctico con showcase del flujo
