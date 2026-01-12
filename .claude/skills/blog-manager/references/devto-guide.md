# Dev.to / Medium Article Guide

Guía para crear artículos técnicos en inglés para publicar en dev.to y Medium.

## Output

- Archivo generado: `.draft/YYYYMMDD_article-devto.md`
- Versión Medium (opcional): `.draft/YYYYMMDD_article-medium.md`

**Formato de nombre de archivo:** `YYYYMMDD_` es la fecha de generación en 8 dígitos (ej.: `20241215_article-devto.md`)

---

## Workflow

### Step 1: Read and Analyze the Source

Lee el README.md y la información del proyecto provistos por el usuario, y entiende lo siguiente:

- Project purpose and core value proposition
- Key features and capabilities
- Installation process
- Usage examples
- Target audience

### Step 2: Generate the Article

Crea el artículo en `.draft/YYYYMMDD_article-devto.md` siguiendo la estructura de abajo.

### Step 3: Generate Medium Version (Optional)

Si se solicita, crea una versión más orientada a historia en `.draft/YYYYMMDD_article-medium.md`.

---

## Article Structure

### Frontmatter

```yaml
---
title: Your Title Here
published: false
description: One-line description for SEO (max 150 chars)
tags: ai, python, opensource, devtools
cover_image: https://your-image-url.com/cover.png
_meta:
  perspective: showcase
  perspective_notes: ""
  sources:
    - ideas/20240120_example.md
  generated_at: 2024-01-20
---
```

### Campo _meta (metadatos de generación)

Campo de administración agregado automáticamente al generar el artículo:

```yaml
_meta:
  perspective: showcase              # Perspectiva utilizada
  perspective_notes: "con entusiasmo"   # Instrucciones adicionales de perspectiva
  sources:                           # Material usado
    - ideas/20240120_mcp-server.md
  generated_at: 2024-01-20           # Fecha de generación
```

| Campo | Descripción |
|-----------|------|
| perspective | Nombre de la plantilla de perspectiva utilizada |
| perspective_notes | Nota adicional de perspectiva indicada por el usuario |
| sources | Material usado (rutas dentro de ideas/) |
| generated_at | Fecha de generación del artículo |

**Nota:** `_meta` es para gestión del artículo; puedes eliminarlo antes de publicar en dev.to/Medium.

### Required Sections (In Order)

#### 1. Title

Format: **"[Action Verb] + [Benefit/Problem Solved]"**

Examples:
- "Stop writing agents by hand: a new way to build AI systems"
- "Introducing an AI tool that designs, evaluates, and improves itself"
- "A new workflow for building AI apps—faster and smarter"

Rules:
- Maximum 60 characters for optimal display
- Use strong verbs: Stop, Introducing, Build, Create, Automate
- Promise a clear benefit
- Avoid generic titles like "My New Project"

#### 2. Hook (First 1-2 Lines)

**This is the most critical part.**

Patterns that work:

**Provocation:**
```
Stop building AI agents manually. Seriously—stop.
```

**Magic moment:**
```
I typed one line, and the entire workflow emerged automatically.
```

**Future shock:**
```
AI can now do in minutes what used to take teams days.
```

Rules:
- Short (1-2 sentences max)
- Surprising or controversial
- Opinionated
- Stand alone visually (separate paragraph)

#### 3. GIF Placeholder

Immediately after the hook:

```
[GIF: Brief description of what the demo should show - e.g., "Terminal showing automated workflow generation in 5 seconds"]
```

Guidelines:
- 5-12 seconds duration
- Show the "aha moment" only
- No audio required
- Visually demonstrate automation or results

#### 4. Problem Statement

Keep this SHORT. 3-5 sentences max.

```markdown
## The Problem

Building [X] manually means:
- [Pain point 1]
- [Pain point 2]
- [Pain point 3]

Sound familiar?
```

The reader should think: "Yes, this is exactly what I struggle with."

#### 5. Solution Overview

Do NOT dive into technical details yet.

```markdown
## What [Project Name] Does

[One sentence summary]

- **Automates** [what]
- **Generates** [what]
- **Evaluates** [what]
- **Optimizes** [what]
```

Use strong verbs:
- Automates, Generates, Evaluates, Optimizes, Integrates
- Eliminates, Simplifies, Accelerates, Transforms

#### 6. Installation

As short as possible. Readers decide in 10 seconds.

```markdown
## Quick Start

\`\`\`bash
pip install your-package
\`\`\`

That's it. You're ready.
```

Rules:
- 1-3 commands maximum
- No configuration steps in this section
- Link to docs for advanced setup

#### 7. How It Works

Show the main value in the simplest possible example.

```markdown
## How It Works

[Screenshot or GIF placeholder]

\`\`\`python
# Minimal code example (5-10 lines max)
from your_package import magic

result = magic("input")
print(result)  # Amazing output
\`\`\`

[Brief explanation - 2-3 sentences]
```

Rules:
- Single screenshot OR second GIF OR short code snippet
- Avoid long code blocks
- No internal architecture explanations
- Deliver the "oh, that's cool" moment

#### 8. Feature Deep Dive (Optional)

Maximum 2-4 subsections.

```markdown
## Key Features

### Feature 1: [Name]
[2-3 sentences + optional small diagram]

### Feature 2: [Name]
[2-3 sentences + optional small diagram]
```

Use diagrams over text where possible.

#### 9. Real Output Example

Make it visually engaging.

```markdown
## See It In Action

**Before:**
| Step | Manual Effort |
|------|---------------|
| Step 1 | 30 minutes |
| Step 2 | 2 hours |

**After:**
| Step | With [Project] |
|------|----------------|
| All | 30 seconds |
```

Rules:
- Use tables for before/after comparisons
- Highlighted terminal output if needed
- Annotated screenshots
- NO large monochrome terminal dumps

#### 10. Closing + CTA

```markdown
## Get Started Today

[Project Name] is open source and ready to use.

- **[Star on GitHub](link)** to support the project
- **[Try the quickstart](link)** in 5 minutes
- **[Open an issue](link)** with your ideas
- **Share** if you found this useful!

---

Thanks for reading! Questions? Drop a comment below.
```

---

## Visual Guidelines

### Recommended Image Flow

1. **Hook → GIF (mandatory)**
2. Screenshot of "initial magic moment"
3. Diagram or annotated terminal
4. Final output or result

### GIF Guidelines

- Should show transformation or automation
- Keep under 15 seconds
- Highlight UI cues (mouse, cursor)

### Screenshots

- Use annotations when possible (arrows, highlights)
- Avoid raw terminal dumps

---

## Reusable Hooks

### Provocative
- "Stop building AI agents manually."
- "Forget prompt engineering—this changes everything."

### Future-oriented
- "AI workflows are about to look very different."
- "A new way to build AI systems—faster and smarter."

### Magic moment
- "I typed one line and the agent built itself."

---

## Hashtags (for X.com posting)

Use 3-6:
- #AI
- #Python
- #MachineLearning
- #LLM
- #AIagents
- #AIengineering
- #OpenSource
- #DevTools

---

## Pre-Publish Checklist

- [ ] Hook is provocative and stands alone
- [ ] GIF placeholder clearly describes the demo
- [ ] Installation is 1-3 commands
- [ ] No long code blocks in first half
- [ ] Visuals are described/planned
- [ ] Clear CTA at the end
- [ ] Total reading time: 4-7 minutes

---

## Medium Differences

Si creas una versión para Medium:

- Un enfoque más **story-driven**
- Incluir experiencias personales y contexto
- Artículo más largo con SEO en mente
- Priorizar el “por qué” sobre los detalles técnicos
- Los títulos en forma de pregunta suelen funcionar

Medium es adecuado para buscar tráfico orgánico a largo plazo.

---

## Project Type Adaptations

### Libraries
Focus on:
- Installation simplicity
- One killer code snippet
- Clear before/after improvement

### Tools / Plugins
Focus on:
- Animated demo
- UI interactions
- Productivity gain

### Frameworks
Focus on:
- Architecture diagram
- Conceptual clarity
- Extensibility

### Benchmarks / Evaluators
Focus on:
- Reproducibility
- Clear metrics
- Example outputs
