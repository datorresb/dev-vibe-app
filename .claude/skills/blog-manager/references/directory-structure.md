# Directory Structure

Estructura de directorios recomendada para un proyecto de escritura de blog (basada en Zenn CLI, ampliada + estructura de 3 capas).

## Three-Layer Concept

La escritura del blog se gestiona en 3 capas: “material”, “perspectiva” y “entregable”.

| Capa | Directorio | Rol | Reutilización |
|---------|-------------|------|--------|
| Material | `ideas/` | Qué escribir (ideas) | ○ |
| Perspectiva | `perspectives/` | Cómo escribir (estilo) | ○ |
| Entregable | `.draft/` → `articles/` | Artículo generado | × |

## Standard Structure

```
my-blog/
├── .claude/                    # Configuración de Claude Code
│   └── settings.local.json
├── .draft/                     # Generación de borradores (ubicación temporal)
│   ├── YYYYMMDD_article-zenn.md    # Borrador para Zenn (ej.: 20241215_article-zenn.md)
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
├── articles/                   # Publicación en Zenn (compatible con Zenn CLI)
│   └── my-published-article.md
├── books/                      # Libros de Zenn (opcional)
│   └── my-book/
│       ├── config.yaml
│       └── chapters/
├── images/                     # Imágenes/GIF compartidos (compatible con Zenn CLI)
│   └── screenshots/
├── external/                   # Versiones finales para otras plataformas
│   ├── devto/
│   │   ├── drafts/
│   │   └── published/
│   └── medium/
│       ├── drafts/
│       └── published/
├── .gitignore
└── README.md
```

## Directory Roles

| Directorio | Rol | Nota |
|-------------|------|------|
| `.draft/` | Destino de generación automática (por la skill) | Mover tras revisar |
| `ideas/` | Stock de ideas/material | Reutilizable; estado via frontmatter |
| `perspectives/` | Plantillas de perspectiva | Reutilizable; define tono/estilo |
| `articles/` | Publicación en Zenn | Compatible con Zenn CLI; `npx zenn preview` |
| `books/` | Libros de Zenn | Opcional |
| `images/` | Archivos de imagen | Compatible con Zenn CLI |
| `external/` | dev.to, Medium | Separado en drafts/published |

## Zenn CLI Compatibility

Esta estructura de directorios es totalmente compatible con Zenn CLI:

```bash
# Vista previa con Zenn CLI
npx zenn preview

# Crear un artículo nuevo
npx zenn new:article

# Crear un libro nuevo
npx zenn new:book
```

## Setup Commands

Si vas a crear un proyecto nuevo:

```bash
# Crear directorios
mkdir -p my-blog/{.draft,ideas,perspectives,articles,books,images/screenshots}
mkdir -p my-blog/external/{devto,medium}/{drafts,published}

# Entrar al proyecto
cd my-blog

# Inicializar Git
git init

# Configurar Zenn CLI (opcional)
npm init -y
npm install zenn-cli
npx zenn init
```

### Plantillas iniciales en perspectives/

En perspectives/ coloca estas plantillas:

```bash
# Crear plantillas estándar
touch perspectives/{showcase,personal,tutorial,deep-dive}.md
```

Consulta [perspectives.md](perspectives.md) para el contenido de cada plantilla.

## Recommended .gitignore

```gitignore
# OS
.DS_Store
Thumbs.db

# Editor
.vscode/
.idea/
*.swp
*~

# Node
node_modules/
package-lock.json

# Optional: si no quieres versionar borradores en Git
# .draft/

# Secrets
.env
.env.local
```

## File Naming Conventions

### .draft/
- `YYYYMMDD_article-{platform}.md` - con prefijo de fecha de generación
- Ej.: `20241215_article-zenn.md`, `20241215_article-devto.md`
- platform: `zenn`, `devto`, `medium`

### ideas/
- `YYYYMMDD_topic-name.md` - prefijo de fecha de creación + kebab-case
- Ej.: `20241215_langchain-tips.md`, `20241210_claude-code-intro.md`

### articles/ (Zenn)
- `slug-name.md` - se convierte en el slug de URL
- Ej.: `how-to-use-langchain.md`
- En Zenn: 14 a 50 caracteres; alfanumérico ASCII (a-z0-9) y guiones

### external/
- `YYYY-MM-DD-title.md` - prefijo de fecha recomendado
- Ej.: `2024-01-15-langchain-tips.md`

## Project Initialization Checklist

Checklist al crear un proyecto nuevo:

- [ ] Crear estructura de directorios (ideas/, perspectives/, .draft/, etc.)
- [ ] Configurar `.gitignore`
- [ ] Inicializar el repositorio Git
- [ ] Configurar Zenn CLI (si usarás Zenn)
- [ ] Añadir plantillas estándar en perspectives/
- [ ] Escribir la explicación del proyecto en README.md
- [ ] Añadir la primera idea a `ideas/`
