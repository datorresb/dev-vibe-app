# Idea Management

Es un esquema de gestión de frontmatter para ideas de artículos (material/fuente).

## Purpose

- Seguimiento del estado de la idea (backlog → in-progress → done)
- **Reutilizable como material** (una idea puede usarse en varios artículos)
- Seguimiento de publicaciones en múltiples plataformas
- Seguimiento de en qué artículos se usó este material

**Importante:** una idea es “material” y no tiene “perspectiva (perspective)” del artículo.
La perspectiva se especifica por separado al generar el artículo. → Consulta [perspectives.md](perspectives.md)

## Idea File Template

En el directorio `ideas/`, crea un archivo con el siguiente formato:

**Formato del nombre de archivo:** `YYYYMMDD_topic-name.md` (ej.: `20241215_langchain-tips.md`)

```yaml
---
status: backlog              # backlog | in-progress | done
priority: medium             # high | medium | low
tags: [langchain, ai, python]
created: 2024-01-10
source_path:                 # (opcional) Ruta del proyecto original
source_feature:              # (opcional) Nombre de la funcionalidad objetivo
used_in: []                  # Artículos donde se usó este material
published_to: []             # Registrar tras publicar
---

# Propuestas de título

## Qué quiero escribir

- Punto 1
- Punto 2
- Punto 3

## Público objetivo

- Descripción del público objetivo

## Referencias

- [Enlace 1](url)
- [Enlace 2](url)

## Diseño del artículo

Rellenar esta sección antes de escribir reduce el retrabajo en las iteraciones.

### Lector
- Conocimientos previos: (principiante / intermedio / alguien familiarizado con el tema)
- Necesidad de explicar conceptos: (¿hace falta incluir “qué es ◯◯” o no?)

### Relación entre tema y material
- Tema (lo más importante a transmitir):
- Rol del ejemplo/material: (un ejemplo que apoya el tema / el tema en sí)

### Flujo de trabajo del ejemplo (si usas un ejemplo real)
- Anota qué pasos seguiste realmente, con episodios concretos
- **Si es una presentación de herramienta/función**: documenta el flujo de interacción (qué dice el usuario y qué ocurre)

### Tipo de introducción
- Directa: empezar simple con “En este artículo presento…”
- Desde un problema: empezar con “¿Te pasa esto?”
- Basada en experiencia: empezar con una historia tipo “El otro día, cuando…”
- Pregunta al lector: empezar con “¿No crees que…?”

### Estilo
- Estilo: (centrado en listas / más narrativo / más técnico)
- Términos que quiero usar:
- Términos a evitar:
- Tono a evitar: (demasiado marketing, provocación barata, frases que suenan “en masa”, etc.)

### Visualización
- ¿Se necesita diagrama?: (con texto basta / quiero diagramas)
- Formato: (diagrama de flujo Mermaid / árbol de directorios / tabla / ninguno)

### Información adicional
- Posibles personalizaciones: (partes ajustables por el lector)
- Alternativas / patrones de aplicación: (si hay otras formas)
```

### Rol de used_in

`used_in` registra en qué artículos se usó este material:

```yaml
used_in:
  - path: articles/langchain-rag-guide.md
    perspective: tutorial
    date: 2024-01-20
  - path: external/devto/published/20240125_langchain-intro.md
    perspective: showcase
    date: 2024-01-25
```

Con esto:
- Se ve claramente que el mismo material se reutilizó con distintas perspectivas
- Se puede medir cuánto se está aprovechando el material
- Junto con `published_to`, se puede rastrear el historial completo

### Cuando se genera automáticamente desde un directorio de desarrollo

Si el usuario indica: `"Escribe un artículo sobre la funcionalidad de autenticación de /path/to/project"`,
se generará automáticamente un archivo como el siguiente en `ideas/`:

```yaml
---
status: in-progress
priority: high
tags: [authentication, nextjs, security]
created: 2024-01-20
source_path: /path/to/project
source_feature: autenticación
published_to: []
---

# Guía de implementación de autenticación en Next.js

## Origen

Artículo generado a partir de la funcionalidad de autenticación de /path/to/project

## Puntos clave para convertirlo en artículo

- Implementación de tokens JWT
- Gestión de sesión
- Verificación de autenticación con middleware
```

Tener `source_path` permite:
- Detectar cuando se intenta volver a escribir sobre la misma funcionalidad
- Volver al código original para verificar detalles

## Status Definitions

| status | Significado | Siguiente acción |
|--------|------|---------------|
| `backlog` | Solo idea. Sin empezar | Cambiar a `in-progress` al comenzar a escribir |
| `in-progress` | En redacción | Cambiar a `done` tras publicar |
| `done` | Artículo completado | Expandir a otras plataformas si aplica |

## Priority Levels

| priority | Significado | Guía |
|----------|------|------|
| `high` | Quiero escribirlo pronto | Esta semana ~ la próxima |
| `medium` | Quiero escribirlo algún día | Dentro de este mes |
| `low` | Guardado como idea | Si hay tiempo |

## Published To Format

Cuando publiques un artículo, actualiza `published_to`:

```yaml
published_to:
  - platform: zenn
    url: https://zenn.dev/username/articles/article-slug
    date: 2024-01-15
  - platform: devto
    url: https://dev.to/username/article-title-xxx
    date: 2024-01-16
  - platform: medium
    url: https://medium.com/@username/article-title-xxx
    date: 2024-01-17
```

## Workflow Examples

### 1. Añadir una idea nueva

```bash
# Crear ideas/20240120_mcp-server-intro.md
```

```yaml
---
status: backlog
priority: high
tags: [mcp, claude, ai]
created: 2024-01-20
published_to: []
---

# Introducción: cómo crear un servidor MCP

## Qué quiero escribir

- Qué es MCP
- Implementación de un servidor simple
- Integración con Claude Code

## Público objetivo

- Usuarios de Claude Code
- Desarrolladores de herramientas de IA
```

### 2. Actualizar status al empezar a escribir

```yaml
---
status: in-progress    # ← cambiado desde backlog
priority: high
tags: [mcp, claude, ai]
created: 2024-01-20
published_to: []
---
```

### 3. Después de publicar en Zenn

```yaml
---
status: done           # ← cambiado desde in-progress
priority: high
tags: [mcp, claude, ai]
created: 2024-01-20
published_to:
  - platform: zenn
    url: https://zenn.dev/ayu/articles/mcp-server-intro
    date: 2024-01-25
---
```

### 4. Después de publicar también en dev.to

```yaml
---
status: done
priority: high
tags: [mcp, claude, ai]
created: 2024-01-20
published_to:
  - platform: zenn
    url: https://zenn.dev/ayu/articles/mcp-server-intro
    date: 2024-01-25
  - platform: devto
    url: https://dev.to/ayu/how-to-build-mcp-server-xxx
    date: 2024-01-26
---
```

## Querying Ideas

### Lista de ideas en backlog
```
Lista los archivos en ideas/ con status: backlog
```

### Ideas con prioridad high
```
Lista los archivos en ideas/ con priority: high
```

### Ideas con un tag específico
```
Lista los archivos en ideas/ cuyo tags incluya "langchain"
```

### Ideas aún no publicadas en dev.to
```
Lista los archivos en ideas/ con status: done y sin devto en published_to
```

## Best Practices

1. **Que la idea sea concreta**
  - No “escribir sobre IA”, sino “3 patrones de implementación RAG en LangChain”

2. **Define claramente el público objetivo**
  - La forma de escribir cambia según quién lo lea

3. **Anota las referencias en el momento**
  - Buscarlo después es difícil

4. **Revisa periódicamente el backlog**
  - Elimina o actualiza ideas que se hayan quedado obsoletas

5. **Actualiza siempre published_to al publicar**
  - Para evitar publicaciones duplicadas

6. **Rellena el “Diseño del artículo” antes de escribir**
  - Define de antemano los conocimientos previos del lector, la relación entre tema y ejemplo, y el estilo
  - Esto reduce mucho el retrabajo durante la redacción
  - Si usas un ejemplo real, anota el flujo de trabajo de forma concreta
