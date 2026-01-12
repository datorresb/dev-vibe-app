# Zenn Article Guide

Guía para crear artículos técnicos (en español) para publicar en Zenn.

## Output

Archivo generado: `.draft/YYYYMMDD_article-zenn.md`

**Formato de nombre de archivo:** `YYYYMMDD_` es la fecha de generación (8 dígitos) (ej.: `20241215_article-zenn.md`)

---

## Workflow

### Step 1: Confirmar la información de base

Leer el README.md y la información del proyecto aportada por el usuario, y entender:

- El objetivo del proyecto y su propuesta de valor
- Las funciones y características principales
- Cómo instalar
- Ejemplos de uso
- Público objetivo

### Step 2: Elegir el tipo de artículo

En Zenn hay dos tipos de artículos:

- **tech**: Artículo técnico (código, librerías, herramientas, etc.) → normalmente este
- **idea**: Artículo de ideas (reflexiones, carrera, ensayo, etc.)

### Step 3: Generar el artículo

Crear el artículo en `.draft/YYYYMMDD_article-zenn.md` siguiendo esta estructura.

---

## Article Structure

### Frontmatter (obligatorio)

```yaml
---
title: "Título del artículo (recomendado: ≤ 40 caracteres)"
emoji: "🚀"
type: "tech"
topics: ["topic1", "topic2", "topic3", "topic4"]
published: false
_meta:
  perspective: showcase
  perspective_notes: ""
  sources:
    - ideas/20240120_example.md
  generated_at: 2024-01-20
---
```

| Campo | Requerido | Descripción |
|-----------|------|------|
| title | ○ | Título del artículo |
| emoji | ○ | Un emoji que represente el artículo |
| type | ○ | `tech` o `idea` |
| topics | ○ | Tags (máx 4, minúsculas alfanuméricas) |
| published | ○ | `true` para publicar, `false` para borrador |
| _meta | - | Metadatos de generación (para gestión; se puede borrar antes de publicar) |

### Campo _meta (metadatos de generación)

Campos de gestión añadidos automáticamente al generar:

```yaml
_meta:
  perspective: tutorial              # Perspectiva usada
  perspective_notes: "Explicar con cuidado"  # Instrucciones adicionales
  sources:                           # Fuentes usadas
    - ideas/20240110_langchain-tips.md
    - ideas/20240115_rag-patterns.md
  generated_at: 2024-01-20           # Fecha de generación
```

| Campo | Descripción |
|-----------|------|
| perspective | Nombre de la plantilla de perspectiva usada |
| perspective_notes | Nota adicional indicada por el usuario |
| sources | Material usado (rutas en ideas/) |
| generated_at | Fecha de generación |

**Nota:** `_meta` es para gestión del artículo; puedes eliminarlo antes de publicar en Zenn.

### Section Structure

```markdown
---
title: "Cómo [lograr algo] con [tecnología]"
emoji: "🚀"
type: "tech"
topics: ["python", "ai", "llm", "tutorial"]
published: false
---

En este artículo explico cómo lograr [qué conseguir] usando [tecnología].
Es un tutorial práctico con el que puedes alcanzar [meta] en [tiempo estimado].

## Prerrequisitos

### Entorno necesario

- Python 3.10 o superior
- pip

### Público objetivo

- Personas que ya conocen lo básico de Python

## Objetivo del artículo

- [Lo que lograrás 1]
- [Lo que lograrás 2]

## Setup

\`\`\`bash
pip install package-name
\`\`\`

## Uso básico

\`\`\`python
from package import Main

result = Main.run()
print(result)
# => Salida
\`\`\`

## Pasos de implementación

### Paso 1: [Título]

[Explicación]

\`\`\`python
# Código
\`\`\`

### Paso 2: [Título]

[Explicación]

\`\`\`python
# Código
\`\`\`

## Resumen

En este artículo cubrimos:

- [Punto 1]
- [Punto 2]

### Enlaces de referencia

- [Documentación oficial](link)
```

---

## Writing Guidelines

### Cómo poner el título

**Ejemplos de buenos títulos:**
- "[Edición 2024] Introducción al desarrollo de apps LLM con Python"
- "Reconstruí mi blog usando las novedades de Next.js 14"
- "Cómo reduje el coste de la API de ChatGPT en un 80%"

**Reglas:**
- Recomendado: ≤ 40 caracteres (no se corta en resultados de búsqueda)
- Incluir tecnologías y versiones concretas
- Usar números ayuda a destacar
- Dejar claro el beneficio para el lector

### Lead (primeras 2-3 líneas)

**Patrones efectivos:**

Planteamiento de problema:
```
"¿En el desarrollo de apps LLM, no terminas escribiendo siempre el mismo código?"
```

Presentación de resultado:
```
"Con esta librería puedes crear un agente de IA con solo 10 líneas de código."
```

Empatía:
```
"Sinceramente, al principio yo tampoco entendía Docker en absoluto."
```

### Estilo

- Mantener un tono educado y accesible
- Explicar términos técnicos la primera vez que aparecen
- Escribir como si hablaras con el lector

### Bloques de código

- Indicar siempre el lenguaje (```python, ```typescript, etc.)
- Escribir comentarios en español (si el artículo es para Zenn en español)
- Proveer código completo y ejecutable
- Incluir ejemplos de salida (formato `# =>`)

### Imágenes y diagramas

- Usar `![descripción](image-placeholder.png)` como placeholder
- Explicar las figuras dentro del texto

### Longitud

- Tiempo de lectura objetivo: 5–15 min (aprox. 2000–6000 caracteres)
- Si se hace largo, proponer dividirlo en varios artículos

---

## Zenn Markdown Extensions

**Caja de mensaje:**

```markdown
:::message
Esto es información adicional.
:::

:::message alert
Esto es un mensaje de advertencia.
:::
```

**Acordeón (plegable):**

```markdown
:::details Haz clic para ver los detalles
Escribe aquí la explicación detallada
:::
```

**Fórmulas (KaTeX):**

```markdown
$$
E = mc^2
$$
```

---

## Topic (Tag) Selection

Se pueden configurar hasta 4.

**Relacionado con AI/ML:**
- `ai`, `llm`, `chatgpt`, `openai`, `claude`, `langchain`
- `machinelearning`, `deeplearning`, `python`

**Desarrollo Web:**
- `nextjs`, `react`, `typescript`, `javascript`
- `nodejs`, `deno`, `bun`

**Infra / herramientas:**
- `docker`, `kubernetes`, `aws`, `gcp`, `azure`
- `github`, `vscode`, `cli`

**Combinaciones populares:**
- AI: `python`, `ai`, `llm`, `chatgpt`
- Web: `typescript`, `react`, `nextjs`, `frontend`
- Infra: `docker`, `kubernetes`, `aws`, `devops`

---

## Emoji Selection

| Categoría | Emojis recomendados |
|---------|-----------|
| AI/ML | 🤖 🧠 🔮 ✨ |
| Desarrollo Web | 🌐 💻 🚀 ⚡ |
| Infra | 🐳 ☁️ 🔧 🛠️ |
| Seguridad | 🔐 🛡️ 🔑 |
| Tutorial | 📝 📚 🎓 |
| Tips | 💡 ✅ 📌 |

---

## Pre-Publish Checklist

- [ ] ¿El frontmatter está correctamente configurado?
- [ ] ¿El título es específico y ≤ 40 caracteres?
- [ ] ¿El emoji encaja con el contenido?
- [ ] ¿Hay ≤ 4 topics y son adecuados?
- [ ] ¿Los prerrequisitos están claros?
- [ ] ¿El código funciona de verdad?
- [ ] ¿Las imágenes y enlaces se ven bien?
- [ ] ¿No hay typos?
- [ ] ¿Hay resumen y enlaces de referencia?

---

## Article Types

### Artículo de introducción / tutorial
- Mostrar el objetivo al principio
- Numerar los pasos
- Explicar qué ocurre en cada paso
- Anticipar puntos donde el lector se atasca

### Artículo de presentación de librería/herramienta
- Mostrar primero “qué puede hacer”
- Tabla comparativa con herramientas similares
- Casos de uso reales
- Ser honesto con pros y contras

### Artículo de troubleshooting
- Incluir el error tal cual (para que sea buscable)
- Explicar la causa
- Proponer varias soluciones
- Incluir prevención

### Artículo de buenas prácticas
- Explicar por qué es buena práctica
- Comparación Before/After
- Ejemplo aplicado a un proyecto real
- Mencionar casos excepcionales
