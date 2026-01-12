# Perspectives (plantillas de perspectiva)

Conjunto de plantillas para definir la “perspectiva” de un artículo.

## Purpose

- Unificar el tono y el estilo del artículo
- Reutilizar perspectivas usadas con frecuencia
- Gestionarlas de forma independiente del material (ideas/)

---

## Standard Templates

Coloca las siguientes plantillas en el directorio `perspectives/` del proyecto del blog:

### showcase.md - Presentación de producto/herramienta

```yaml
---
name: showcase
description: "Presentar un producto/herramienta de forma clara para que la gente lo pruebe"
---

# Estilo Showcase

## Tono
- Con entusiasmo, pero sin imponer
- Compartir el “¡esto es útil!”
- Hacer que el lector piense “quiero probarlo”

## Puntos de estructura
- Mostrar primero “qué puede hacer” (GIF/captura)
- Instalación lo más corta posible (1-3 comandos)
- Más ejemplos de uso real
- CTA claro (poner star, probar)

## Expresiones a usar
- “Puedes…” / “Es posible…”
- “Pruébalo” / “Te invito a probarlo”
- “Espero tu feedback”

## Evitar
- No entrar demasiado en detalles de implementación
- Introducciones demasiado largas
- Sonar presumido
```

### personal.md - Ideas personales / registro de desarrollo

```yaml
---
name: personal
description: "Compartir de forma moderada ideas personales y registros de desarrollo"
---

# Estilo Personal

## Tono
- Moderado y humilde
- En clave de propuesta (“yo lo veo así”)
- Dejar espacio para que el lector piense

## Puntos de estructura
- Empezar empatizando con el problema/duda del lector (planteo del problema)
- Empezar por el contexto o la motivación
- Incluir el proceso de prueba y error
- Contar el ejemplo como un episodio concreto (no solo descripción abstracta)
- Hacerlo visual con diagramas o snippets
- No imponer una conclusión
- Mantener la postura de “por si te sirve”

## Expresiones a usar
- “Personalmente, creo que…”
- “Como un enfoque posible…”
- “Me encantaría conocer tu opinión”
- “Todavía estoy iterando, pero…”
- “Lo que hago es este método…”
- “Lo importante es…” (enfatizar, pero con moderación)
- “Te invito a probarlo” (como propuesta al lector)

## Evitar
- Expresiones tajantes
- Afirmar “esta es la respuesta correcta”
- Descalificar otros enfoques
- Quedarse solo en lo abstracto (sin ejemplos concretos cuesta transmitirlo)
- Explicaciones redundantes (la historia importa, pero sé conciso)
- Solo listar puntos (se necesita ritmo para enganchar)
```

### tutorial.md - Tutorial paso a paso

```yaml
---
name: tutorial
description: "Enseñar con detalle paso a paso"
---

# Estilo Tutorial

## Tono
- Cuidadoso y amable
- Fácil de seguir para principiantes
- Incluir ánimo

## Puntos de estructura
- Declarar el objetivo al inicio
- Aclarar prerequisitos
- Numerar cada paso
- Explicar “qué ocurre” en cada paso
- Anticipar los puntos donde la gente se atasca
- Mostrar el código final al final

## Expresiones a usar
- “Primero, vamos a…”
- “Aquí haremos…”
- “Si no funciona, revisa…”
- “¡Felicitaciones!”

## Evitar
- Volcar código sin explicación
- Decir “es fácil” (puede intimidar al lector)
- Omitir conocimientos previos necesarios
```

### deep-dive.md - Profundización técnica

```yaml
---
name: deep-dive
description: "Profundizar en los detalles técnicos"
---

# Estilo Deep-Dive

## Tono
- Especializado y detallado
- Mostrar fundamentos
- Priorizar precisión

## Puntos de estructura
- Explicar con detalle el contexto del problema
- Comparar múltiples enfoques
- Explicitar trade-offs
- Incluir benchmarks o cifras
- Aportar buenas referencias

## Expresiones a usar
- “La razón de … es …”
- “Comparado con …”
- “Internamente ocurre …”
- “Según la documentación…”

## Evitar
- Afirmaciones sin base
- Simplificar en exceso
- Explicaciones redundantes para principiantes
```

---

## Custom Perspective

Si no encaja con las plantillas estándar, también puedes especificarla directamente:

```
> Convierte ideas/20241215_new-feature.md en un artículo
> Perspectiva: moderada, como reflexión personal. Prioriza el “por qué lo diseñé así” sobre los detalles técnicos
```

En ese caso, se registrará en `_meta.perspective_notes` del artículo generado:

```yaml
_meta:
  perspective: custom
  perspective_notes: |
    Moderado, como reflexión personal.
    Prioriza el “por qué lo diseñé así” sobre los detalles técnicos
```

---

## Creating New Templates

Para añadir una nueva plantilla de perspectiva:

1. Crea un nuevo archivo `.md` en `perspectives/`
2. En el frontmatter añade `name` y `description`
3. Define tono, puntos de estructura, expresiones a usar y qué evitar

**Ej.: announcement.md (anuncio de release)**

```yaml
---
name: announcement
description: "Anunciar nuevas funcionalidades o releases"
---

# Estilo Announcement

## Tono
- Priorizar lo noticioso
- Ser breve y al grano
- Transmitir entusiasmo

## Puntos de estructura
- Empezar diciendo “qué hay de nuevo” de forma concisa
- Listar los cambios principales
- Indicar cómo actualizar
- Mencionar brevemente lo que viene después

...
```

---

## Combining Perspectives

También es posible combinar varias perspectivas:

```
> Escribe un artículo de Zenn a partir de ideas/20241215_new-lib.md con showcase + tutorial
```

En ese caso:
- La primera mitad es showcase (presentación, qué puede hacer)
- La segunda mitad es tutorial (paso a paso de uso)

---

## Perspective Selection Guide

| Lo que quieres escribir | Perspective recomendada |
|-------------|------------------|
| Quiero presentar una herramienta nueva | showcase |
| Compartir pensamientos durante el desarrollo | personal |
| Enseñar cómo se usa | tutorial |
| Explicar el funcionamiento en detalle | deep-dive |
| Anunciar un release | announcement |
| Comparar varias herramientas | deep-dive |
| Compartir una historia de fallo | personal |
