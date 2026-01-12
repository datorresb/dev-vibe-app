# Directory Structure

Estructura de directorios recomendada para un proyecto de escritura de blog (estructura de 3 capas).

## Three-Layer Concept

La escritura del blog se gestiona en 3 capas: “material”, “perspectiva” y “entregable”.

| Capa | Directorio | Rol | Reutilización |
|---------|-------------|------|--------|
| Material | `ideas/` | Qué escribir (ideas) | ○ |
| Perspectiva | `perspectives/` | Cómo escribir (estilo) | ○ |
| Entregable | `.draft/` → `articles/` | Artículo generado | × |

## Standard Structure

```
my-notes/
├── .draft/                     # Generación de borradores (ubicación temporal)
│   ├── YYYYMMDD_article-EsPersonal.md    # Borrador principal (ej.: 20241215_article-EsPersonal.md)
│   ├── YYYYMMDD_article-devto.md   # Borrador para dev.to
│   └── YYYYMMDD_article-medium.md  # Borrador para Medium
├── ideas/                      # Ideas/material para artículos (reutilizable)
│   ├── YYYYMMDD_langchain-tips.md    # Ej.: 20241215_langchain-tips.md
│   ├── YYYYMMDD_claude-code-intro.md
│   └── ...
├── perspectives/               # Plantillas de perspectiva (reutilizable)
│   ├── showcase.md             # Presentación de producto
│   ├── personal.md             # Opinión personal
│   ├── tutorial.md             # Tutorial práctico (hands-on)
│   └── deep-dive.md            # Profundización técnica
├── articles/                   # Artículos listos para publicar
│   └── my-published-article.md
├── books/                      # Libros (opcional)
│   └── my-book/
│       ├── config.yaml
│       └── chapters/
├── images/                     # Imágenes/GIF compartidos
│   └── screenshots/
├── external/                   # Versiones finales para otras plataformas
│   ├── devto/
│   │   ├── drafts/
│   │   └── published/
│   └── medium/
│       ├── drafts/
│       └── published/
└── notes/
    └── general-notes.md         # Notas generales
```

## Directory Roles

| Directorio | Rol | Nota |
|-------------|------|------|
| `.draft/` | Destino de generación automática (por la skill) | Mover tras revisar |
| `ideas/` | Stock de ideas/material | Reutilizable; estado via frontmatter |
| `perspectives/` | Plantillas de perspectiva | Reutilizable; define tono/estilo |
| `articles/` | Publicación | Puedes publicar desde aquí (Markdown) |
| `books/` | Libros | Opcional |
| `images/` | Archivos de imagen | Puedes referenciarlos desde tus artículos |
| `external/` | dev.to, Medium | Separado en drafts/published |

## Vista previa

Estas opciones suelen ser suficientes:

- **VS Code Markdown Preview** (Ctrl/Cmd+Shift+V)
- **GitHub rendering**: sube el markdown a un repo y revisa el render

Si más adelante quieres un preview “tipo plataforma”, puedes agregar una herramienta específica, pero es opcional.

## Setup Commands

Si vas a crear un proyecto nuevo:

```bash
# Crear directorios
mkdir -p my-notes/{.draft,ideas,perspectives,articles,books,images/screenshots}
mkdir -p my-notes/external/{devto,medium}/{drafts,published}

# Entrar al proyecto
cd my-notes
```

### Plantillas iniciales en perspectives/

En perspectives/ coloca estas plantillas:

```bash
# Crear plantillas estándar
touch perspectives/{showcase,personal,tutorial,deep-dive}.md
```

Consulta [perspectives.md](perspectives.md) para el contenido de cada plantilla.

## File Naming Conventions

### .draft/
- `YYYYMMDD_article-{platform}.md` - con prefijo de fecha de generación
- Ej.: `20241215_article-EsPersonal.md`, `20241215_article-devto.md`
- platform: `EsPersonal`, `devto`, `medium`

### ideas/
- `YYYYMMDD_topic-name.md` - prefijo de fecha de creación + kebab-case
- Ej.: `20241215_langchain-tips.md`, `20241210_claude-code-intro.md`

### articles/
- `slug-name.md` - se convierte en el slug de URL
- Ej.: `how-to-use-langchain.md`
- En EsPersonal, recomendado ≤ 50 caracteres; alfanumérico ASCII (a-z0-9) y guiones

### external/
- `YYYY-MM-DD-title.md` - prefijo de fecha recomendado
- Ej.: `2024-01-15-langchain-tips.md`

## Project Initialization Checklist

Checklist al crear un proyecto nuevo:

- [ ] Crear estructura de directorios (ideas/, perspectives/, .draft/, etc.)
- [ ] Configurar `.gitignore`
- [ ] Inicializar el repositorio Git
- [ ] Añadir plantillas estándar en perspectives/
- [ ] Escribir la explicación del proyecto en README.md
- [ ] Añadir la primera idea a `ideas/`
