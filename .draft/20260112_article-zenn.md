---
title: "Beadsでエージェント作業を安定させる: Claude Code/Copilot"
emoji: "🧠"
type: "tech"
topics: ["ai", "claude", "copilot", "productivity"]
published: false
_meta:
  perspective: tutorial
  perspective_notes: "Tutorial paso a paso + secciones deep-dive; foco en CLI+hooks para Claude Code y adaptación a VS Code Copilot"
  sources:
    - ideas/20260112_beads-claude-code-copilot.md
  generated_at: 2026-01-12
---

¿Te pasa que empiezas una tarea con un agente (Claude Code o Copilot), el plan vive en un Markdown… y a la tercera iteración ya nadie sabe qué falta, qué bloquea qué, o qué se decidió?

En este artículo te explico cómo usar **Beads** (`bd`) como “memoria persistente” para agentes: un tracker de issues **git-backed** con dependencias, diseñado para flujos agentic.

- Repo oficial: https://github.com/steveyegge/beads

## Prerrequisitos

### Entorno necesario

- Linux/macOS/Windows
- `git`
- Acceso a terminal en tu editor (Claude Code / VS Code)

### Público objetivo

- Devs con nivel intermedio (usas git/terminal) que trabajan con Claude Code o GitHub Copilot

## Qué es Beads (en 60 segundos)

Beads (`bd`) es un issue tracker pensado para agentes:

- Guarda issues en `.beads/` y las exporta a `.beads/issues.jsonl` (versionable con git)
- Soporta dependencias (bloqueos) para saber qué está “ready”
- Está optimizado para agentes (salidas `--json`, IDs estables, workflow repetible)

:::message
En la práctica, Beads te da una forma de mantener el *estado del trabajo* fuera del prompt. Así el agente puede retomar sesiones sin “re-leer” un plan gigante.
:::

## Dos enfoques de integración (y cuál recomiendo)

- **Claude Code / editores con shell**: **CLI + hooks** (recomendado)
- **Entornos sin shell** (p. ej. Claude Desktop): **MCP** (`beads-mcp`)

:::details Deep-dive: por qué CLI+hooks suele ser mejor que MCP
Según el diseño de integración, el enfoque CLI+hooks es más eficiente en contexto:
- `bd prime` inyecta ~1–2k tokens de contexto de workflow.
- MCP puede añadir 10–50k tokens solo en schemas/herramientas.

Eso se traduce en menos latencia, menos coste y mejor “atención” del modelo.

Referencia: https://github.com/steveyegge/beads/blob/main/docs/CLAUDE_INTEGRATION.md
:::

## Paso 0 — Instalar `bd`

Elige una de estas opciones (la guía completa está en la doc oficial):

- Instalación rápida (script):

```bash
curl -fsSL https://raw.githubusercontent.com/steveyegge/beads/main/scripts/install.sh | bash
```

- npm:

```bash
npm install -g @beads/bd
```

Verifica:

```bash
bd version
bd help
```

Referencia: https://github.com/steveyegge/beads/blob/main/docs/INSTALLING.md

## Paso 1 — Inicializar Beads en tu repo

En la raíz de tu proyecto:

```bash
bd init --quiet
```

Esto crea (entre otras cosas) la carpeta `.beads/` y el archivo `.beads/issues.jsonl`.

:::message alert
Si tu repo es compartido y no quieres commitear metadata todavía, revisa el “modo sigiloso (stealth mode)” en la documentación de Beads.
:::

## Paso 2 — Darle instrucciones claras al agente (AGENTS.md)

Crea (o actualiza) `AGENTS.md` en la raíz del repo. Un mínimo útil:

```text
Use 'bd' for task tracking.
When you start, run: bd ready
Before finishing, run: bd sync
```

En el README del repo muestran el patrón:

- “Tell your agent: `echo "Use 'bd' for task tracking" >> AGENTS.md`”

Referencia: https://github.com/steveyegge/beads

## Paso 3 — Claude Code: activar integración recomendada (CLI + hooks)

Si usas Claude Code, lo más cómodo es que `bd prime` se ejecute automáticamente al iniciar sesión.

```bash
# Instala hooks globales para Claude Code
bd setup claude

# O solo para este proyecto
bd setup claude --project

# Verificar
bd setup claude --check
```

Qué hace:
- SessionStart hook: ejecuta `bd prime` al iniciar
- PreCompact hook: ejecuta `bd prime` antes de compactar contexto

Referencia: https://github.com/steveyegge/beads/blob/main/docs/CLAUDE_INTEGRATION.md

## Paso 4 — Flujo diario (humano + agente)

### 4.1 Crear tareas (issues)

```bash
bd create "Configurar Beads en el repo" -p 1
bd create "Agregar AGENTS.md" -p 1
bd create "Documentar flujo de trabajo" -p 2
```

### 4.2 Enlazar dependencias (cuando aplica)

Ejemplo: “documentar flujo” depende de “agregar AGENTS.md”.

```bash
bd dep add <child> <parent>
```

### 4.3 Trabajar siempre desde lo que está ready

```bash
bd ready
```

Idea mental: **si no está ready, está bloqueado por algo**.

### 4.4 Cerrar y sincronizar

```bash
bd close <id> --reason "Completed"
bd sync
```

## Paso 5 — (Opcional) Claude Code plugin: comandos tipo /beads:ready

Si quieres UX de slash commands en Claude Code, hay un plugin oficial.

Instalación (según la doc):

```text
/plugin marketplace add steveyegge/beads
/plugin install beads
```

Comandos típicos:
- `/beads:init`
- `/beads:create "..." feature 1`
- `/beads:ready`
- `/beads:workflow`

Referencia: https://github.com/steveyegge/beads/blob/main/docs/PLUGIN.md

## Paso 6 — VS Code + GitHub Copilot: cómo aplicar el mismo enfoque

Copilot en VS Code no “necesita” una integración especial para aprovechar Beads. El truco es:

1) Mantener el estado en `bd` (no en un plan suelto)
2) Pedirle a Copilot que tome decisiones a partir de `bd ready` / `bd show` / `bd list`

Flujo recomendado:

- En el terminal de VS Code:

```bash
bd ready
bd show <id>
```

- En Copilot Chat (modo Agent o Ask), pega la salida y pide:

- “Propón el plan para `bd-xxxx` y dime qué archivos tocarías.”
- “Implementa `bd-xxxx` y cuando termines, dime qué debería cerrar y por qué.”

:::details Deep-dive: cómo evitar que Copilot se pierda
Una regla práctica: cada vez que cambie el estado (empezar, descubrir trabajo, terminar), conviértelo en una operación explícita en Beads:
- descubrí algo → `bd create ...`
- bloquea algo → `bd dep add ...`
- terminé → `bd close ...`

Así el agente no tiene que reconstruir contexto desde el chat.
:::

### 6.1 Usar Beads con Copilot “al mismo tiempo” (y opcionalmente Claude Code)

Sí: puedes usar Beads como una **fuente de verdad compartida** mientras conversas con Copilot (VS Code) y, si quieres, también con Claude Code.

Reglas prácticas para que no se pisen:

1) **Un estado, una acción en bd**
- Si Copilot propone un plan, conviértelo en issues (`bd create`) y dependencias (`bd dep add`).
- Si Claude (o tú) descubre trabajo nuevo, también se registra igual.

2) **Sincroniza al final de cada “bloque” de trabajo**

```bash
bd sync
```

Eso fuerza la exportación/importación y evita que `.beads/issues.jsonl` se quede “atrás” respecto a la DB.

3) **Evita dos escritores a la vez sobre el mismo issue**
- Si estás trabajando `bd-123`, márcalo `in_progress` antes de tocar código.
- Si el otro agente quiere ayudar, que tome otro issue o cree sub-tareas (`bd-123.1`, `bd-123.2`).

4) **Copilot no necesita plugin**

En VS Code basta con:
- ejecutar `bd` en terminal
- pegar/adjuntar la salida en Copilot Chat (por ejemplo la salida de `bd ready` o `bd show <id>`) y pedir acciones concretas.

Si prefieres slash commands, eso existe como plugin para **Claude Code** (no para Copilot).

## Paso 7 — Si NO tienes shell: Beads vía MCP (Claude Desktop)

Para entornos MCP-only, existe `beads-mcp`.

Instalación:

```bash
uv tool install beads-mcp
# o
pip install beads-mcp
```

Ejemplo de configuración (Claude Desktop):

```json
{
  "mcpServers": {
    "beads": {
      "command": "beads-mcp"
    }
  }
}
```

Referencia: https://pypi.org/project/beads-mcp/

## Preguntas frecuentes

### “¿Esto es lo mismo que ‘skills’?”

No exactamente. Beads es una herramienta externa (`bd`) para **persistir** el estado del trabajo. En el diseño de integración de Beads se menciona explícitamente que **no requiere Claude Skills** y prefiere CLI+hooks.

Referencia: https://github.com/steveyegge/beads/blob/main/docs/CLAUDE_INTEGRATION.md

### “¿Qué commiteo en git?”

Normalmente, el archivo `.beads/issues.jsonl` es lo que viaja con git para compartir el estado del tracker.

## Resumen

- Beads (`bd`) te ayuda a mantener memoria y estado de trabajo fuera del prompt.
- En Claude Code, el camino recomendado es **CLI + hooks** (`bd setup claude`) para inyectar `bd prime` automáticamente.
- En VS Code + Copilot, el valor viene de usar `bd ready`/`bd show` como “fuente de verdad” del plan.
- MCP (`beads-mcp`) es útil cuando no hay shell, pero tiene más overhead.

## Enlaces de referencia

- Beads (repo): https://github.com/steveyegge/beads
- Installing: https://github.com/steveyegge/beads/blob/main/docs/INSTALLING.md
- Claude integration: https://github.com/steveyegge/beads/blob/main/docs/CLAUDE_INTEGRATION.md
- Plugin: https://github.com/steveyegge/beads/blob/main/docs/PLUGIN.md
- beads-mcp: https://pypi.org/project/beads-mcp/
