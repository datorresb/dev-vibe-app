---
name: blog-manager
description: Use for all blog writing tasks including creating articles (Zenn, dev.to/Medium English), managing ideas, and setting up blog projects. This is the unified entry point for technical blog writing workflow. Supports idea tracking with status management (backlog/in-progress/done).
---

# Blog Manager Skill

Esta skill proporciona un flujo de trabajo unificado para escribir blogs técnicos.

## Purpose

- Configurar proyectos de escritura de blog
- Gestionar el estado de ideas de artículos (backlog → in-progress → done)
- Generar artículos aplicando una perspectiva (perspective)
- Generar artículos (Zenn en español / dev.to y Medium en inglés)
- Actualizar el estado tras publicar y ayudar con la promoción

---

## Three-Layer Structure

La escritura del blog se gestiona en 3 capas: “material”, “perspectiva” y “entregable”.

```
my-blog/
├── ideas/                  # Material (ideas reutilizables)
│   ├── YYYYMMDD_langchain-tips.md
│   └── YYYYMMDD_rag-patterns.md
├── perspectives/           # Perspectiva (estilos reutilizables)
│   ├── showcase.md         # Para presentar producto
│   ├── personal.md         # Opinión personal
│   └── tutorial.md         # Tutorial práctico (hands-on)
├── .draft/                 # Artículos generados (resultado de una ejecución)
│   └── YYYYMMDD_article-zenn.md
└── articles/               # Para publicar
```

| Capa | Rol | Reutilización |
|---------|------|--------|
| `ideas/` | Material / ideas (qué escribir) | ○ Reutilizable |
| `perspectives/` | Perspectiva / estilo (cómo escribir) | ○ Reutilizable |
| `.draft/` | Artículo generado | × Resultado de una ejecución |

**La relación entre una idea y un artículo no es 1:1:**
- 1 idea → varios artículos (con distintas perspectivas)
- Varias ideas → 1 artículo (combinadas)
- Reutilizar la misma idea para otro artículo

## When to Use

- Cuando te digan “escribe un artículo” o “escribe un blog”
- Cuando vayas a crear artículos para Zenn, dev.to o Medium
- Cuando quieras configurar un nuevo proyecto de blog
- Cuando quieras revisar la lista/estado de ideas de artículos
- Cuando necesites actualizar el estado tras publicar

---

## Input Sources

El material de origen para un artículo se puede obtener de dos formas:

### Patrón A: desde `ideas/`

Generar un artículo a partir de una idea ya anotada en `ideas/`:

```
> Escribe un artículo para Zenn basado en ideas/20241215_langchain-tips.md
```

### Patrón B: desde un directorio de desarrollo (especificación directa)

Generar un artículo especificando directamente una función concreta de un proyecto en desarrollo:

```
> Escribe un artículo para Zenn sobre la función de autenticación de /path/to/project
> Convierte la implementación de LangGraph de @myproject/ en un artículo para dev.to
> Escribe un artículo sobre la funcionalidad de servidor MCP de este repositorio
```

**Flujo de trabajo del patrón B:**

```
┌─────────────────────────────────────────────────────────────┐
│  1. El usuario especifica directorio + función                │
│     “Escribe un artículo sobre autenticación en /path/to/project”│
└─────────────────┬───────────────────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────────────────┐
│  2. Explorar y leer el código relevante                        │
│     - Leer README.md si existe                                │
│     - Identificar archivos relacionados con la función         │
│     - Entender los puntos clave de la implementación           │
└─────────────────┬───────────────────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────────────────┐
│  3. Generar el artículo (salida en .draft/)                    │
└─────────────────┬───────────────────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────────────────┐
│  4. Crear un registro en ideas/ automáticamente (evitar duplicados)│
│     ideas/YYYYMMDD_project-name-feature.md                   │
│     status: in-progress                                      │
│     source_path: /path/to/project                            │
└─────────────────────────────────────────────────────────────┘
```

**Ejemplo de archivo de registro creado en `ideas/`:**

```yaml
---
status: in-progress
priority: high
tags: [authentication, nextjs, security]
created: 2024-01-20
source_path: /path/to/project      # Ruta del proyecto original
source_feature: autenticación       # Función objetivo
published_to: []
---

# Explicación de la implementación de autenticación en Next.js

## Fuente

Artículo generado a partir de la función de autenticación de /path/to/project

## Puntos clave para el artículo

- Implementación de tokens JWT
- Gestión de sesión
- Verificación de autenticación en middleware
```

Con esto:
- Puedes detectar si intentas escribir otra vez sobre la misma función
- Puedes hacer seguimiento tras publicar con `published_to`
- Puedes volver al código fuente con `source_path`

---

## Perspective (perspectiva)

La “perspectiva” se especifica al generar el artículo y se gestiona de forma independiente del material (`ideas/`).

### Cómo especificar la perspectiva

```
# Referenciar una plantilla
> Escribe un artículo para Zenn basado en ideas/20241215_mcp-server.md con la perspectiva showcase

# Especificación directa
> Convierte ideas/20241215_new-feature.md en un artículo
> Perspectiva: con un tono moderado y como opinión personal

# Múltiples materiales + una perspectiva
> Escribe un artículo para Zenn con perspectiva tutorial usando ideas/20241210_langchain-tips.md y ideas/20241212_rag-patterns.md
```

### Plantillas de perspectiva estándar

| perspective | Uso | Tono |
|-------------|------|--------|
| `showcase` | Presentación de producto/herramienta | Entusiasta, orientado a que lo prueben |
| `personal` | Opinión personal / diario de desarrollo | Moderado, basado en propuestas |
| `tutorial` | Tutorial práctico (hands-on) | Cuidadoso, paso a paso |
| `deep-dive` | Profundización técnica | Detallado, especializado |

Para más detalles, consulta [perspectives.md](references/perspectives.md).

### Metadatos del artículo generado

En `.draft/YYYYMMDD_article-zenn.md` se registran la perspectiva y las fuentes usadas:

```yaml
---
title: "Guía práctica para implementar RAG con LangChain"
emoji: "📚"
type: "tech"
topics: ["langchain", "rag", "python", "ai"]
published: false
_meta:
  perspective: tutorial
  perspective_notes: "De forma cuidadosa, paso a paso"
  sources:
    - ideas/20241210_langchain-tips.md
    - ideas/20241212_rag-patterns.md
  generated_at: 2024-01-20
---
```

---

## Workflow Overview

```
┌─────────────────────────────────────────────────────────────┐
│  1. Añadir una idea en ideas/                                  │
│     Crear frontmatter con status: backlog                      │
│     → Ver references/idea-management.md                        │
└─────────────────┬───────────────────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────────────────┐
│  2. Revisar el diseño del artículo (antes de escribir)         │
│     - Conocimientos previos del lector; si hace falta explicar conceptos│
│     - Tipo de intro (directa / problema / experiencia / pregunta)│
│     - Estilo y tono a evitar (p. ej., demasiado marketing)      │
│     - Preferencias de visualización (Mermaid/árbol/tabla/ninguna)│
│     - Detalles de comportamiento real (si es una herramienta, el flujo de interacción, etc.)│
│     - Información adicional (margen de personalización, alternativas)│
│     → Ver “Diseño del artículo” en references/idea-management.md│
└─────────────────┬───────────────────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────────────────┐
│  3. Empezar a escribir                                         │
│     Actualizar status: in-progress                              │
│     Elegir la plataforma:                                      │
│     - Zenn (español) → references/zenn-guide.md                │
│     - dev.to/Medium (inglés) → references/devto-guide.md       │
└─────────────────┬───────────────────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────────────────┐
│  4. El artículo se genera en .draft/                            │
│     - .draft/YYYYMMDD_article-zenn.md (para Zenn)              │
│     - .draft/YYYYMMDD_article-devto.md (para dev.to)           │
│     - .draft/YYYYMMDD_article-medium.md (para Medium, opcional)│
└─────────────────┬───────────────────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────────────────┐
│  5. Revisión y edición                                         │
│     - Revisar el contenido y ajustar                            │
│     - Añadir imágenes/GIF                                       │
│     - Zenn: comprobar con npx zenn preview                       │
└─────────────────┬───────────────────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────────────────┐
│  6. Mover al directorio definitivo                              │
│     .draft/YYYYMMDD_article-zenn.md → articles/slug.md      │
│     .draft/YYYYMMDD_article-devto.md → external/devto/published/│
└─────────────────┬───────────────────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────────────────┐
│  7. Actualizar el status de la idea a done                      │
│     Registrar la URL de publicación en published_to             │
└─────────────────┬───────────────────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────────────────┐
│  8. Publicar y promocionar                                      │
│     → Ver references/promotion-tips.md                          │
└─────────────────────────────────────────────────────────────┘
```

---

## Platform Selection

Elegir la plataforma según lo que pida el usuario:

| Palabras clave | Plataforma | Guía |
|-----------|-----------------|--------|
| “Zenn”, “español”, “artículo técnico” | Zenn | [zenn-guide.md](references/zenn-guide.md) |
| “dev.to”, “inglés”, “lanzamiento” | dev.to | [devto-guide.md](references/devto-guide.md) |
| “Medium”, “historia” | Medium | [devto-guide.md](references/devto-guide.md) (modo Medium) |
| “ambos”, “multi” | Zenn + dev.to | Generar ambos |

**Si la plataforma no está clara:**
Preguntar al usuario:
- Para lectores en español → Zenn
- Para lectores globales → dev.to/Medium
- Ambas → generar para ambas plataformas

---

## References

| Archivo | Contenido |
|---------|------|
| [directory-structure.md](references/directory-structure.md) | Estructura de directorios del proyecto |
| [idea-management.md](references/idea-management.md) | Gestión de frontmatter de ideas (material) |
| [perspectives.md](references/perspectives.md) | Definición y uso de plantillas de perspectiva |
| [zenn-guide.md](references/zenn-guide.md) | Guía para generar artículos para Zenn (español) |
| [devto-guide.md](references/devto-guide.md) | Guía para generar artículos para dev.to/Medium (inglés) |
| [promotion-tips.md](references/promotion-tips.md) | Estrategia y timing de promoción |

---

## Usage Examples

### 1. Configurar proyecto
```
> Configura un proyecto para escribir el blog
```
→ Crear directorios siguiendo [directory-structure.md](references/directory-structure.md)

### 2. Gestión de ideas
```
> Lista el backlog dentro de ideas/
> Cambia el status de ideas/20241215_xxx.md a in-progress
```
→ Editar el frontmatter según [idea-management.md](references/idea-management.md)

### 3. Generar artículo para Zenn (desde ideas/)
```
> Escribe un artículo para Zenn basado en ideas/20241215_langchain-tips.md
```
→ Generar `.draft/YYYYMMDD_article-zenn.md` siguiendo [zenn-guide.md](references/zenn-guide.md)

### 4. Generar artículo especificando perspectiva
```
> Escribe un artículo para Zenn basado en ideas/20241215_mcp-server.md con perspectiva showcase
> Convierte ideas/20241215_new-lib.md en un artículo con perspectiva personal
```
→ Aplicar la plantilla en perspectives/ y generar el artículo

### 5. Generar artículo combinando varios materiales
```
> Escribe un artículo para Zenn con perspectiva tutorial usando ideas/20241210_langchain-tips.md y ideas/20241212_rag-patterns.md
```
→ Integrar varios materiales y generar el artículo con la perspectiva indicada

### 6. Generar artículo desde un directorio de desarrollo
```
> Escribe un artículo para Zenn sobre la función de autenticación de /path/to/myproject
> Convierte el patrón de procesamiento en paralelo de @langgraph-plugin/ en un artículo con perspectiva showcase
```
→ Leer código → generar artículo → crear registro automáticamente en `ideas/`

### 7. Generar artículo para dev.to
```
> Escribe un artículo para dev.to basado en este README
> Escribe un artículo para dev.to sobre @my-cli-tool/ con perspectiva showcase
```
→ Generar `.draft/YYYYMMDD_article-devto.md` siguiendo [devto-guide.md](references/devto-guide.md)

### 8. Generar ambos
```
> Escribe artículos para Zenn y dev.to basados en ideas/20241215_mcp-intro.md con perspectiva showcase
```
→ Generar ambas versiones con la misma perspectiva

### 9. Actualización tras publicar
```
> Cambia el status de ideas/20241215_langchain-tips.md a done
> Añade https://zenn.dev/xxx/articles/yyy a published_to
```
→ Actualizar el frontmatter

### 10. Consulta de promoción
```
> Dime una estrategia de promoción para este artículo
```
→ Dar consejos basados en [promotion-tips.md](references/promotion-tips.md)

---

## Output Files

| Archivo | Descripción |
|---------|------|
| `.draft/YYYYMMDD_article-zenn.md` | Artículo para Zenn (español) |
| `.draft/YYYYMMDD_article-devto.md` | Artículo para dev.to (inglés) |
| `.draft/YYYYMMDD_article-medium.md` | Artículo para Medium (inglés, opcional) |

**Formato del nombre de archivo:** `YYYYMMDD_` es la fecha de generación (8 dígitos) (ej.: `20241215_article-zenn.md`)

---

## Checklist para generar artículos

Cuando el usuario pida “escribe un artículo”, si falta información, confirmar lo siguiente:

| Ítem | Cuándo hace falta confirmar | Ejemplo de pregunta |
|------|-----------------|--------|
| Conocimientos previos del lector | El público objetivo no está claro | “¿Podemos asumir que el lector conoce ◯◯?” |
| Si hace falta explicar conceptos | Presentación de herramienta/tecnología | “¿Necesitas que explique qué es ◯◯?” |
| Tipo de introducción | No hay indicación | “¿Prefieres una intro directa, problema, experiencia, pregunta…?” |
| Tono a evitar | No hay indicación | “¿Hay expresiones o tonos que quieras evitar?” |
| Preferencia de visualización | Cuando se explica estructura | “¿Usamos diagramas (Mermaid, etc.) o basta texto?” |
| Comportamiento real | Presentación de herramienta/función | “¿Qué ocurre cuando el usuario hace ◯◯?” |
| Información adicional | Herramienta personalizable | “¿Mencionamos ajustes posibles o alternativas?” |

**Punto clave**: Confirmar esto al inicio reduce mucho las idas y vueltas durante la redacción.

---

## Notes

- Toda generación de artículos se escribe en `.draft/` (ubicación temporal)
- Cuando esté listo, mover a `articles/` (Zenn) o `external/` (otros)
- La gestión de estados de ideas ayuda a evitar artículos duplicados
- Puedes publicar la misma idea en varias plataformas (seguimiento con `published_to`)
- Los ajustes finos tras generar se pueden hacer a mano o pidiéndoselos a Claude Code
