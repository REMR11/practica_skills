# Práctica: crear y usar Agent Skills en Cursor (Node.js)

Esta práctica está pensada para que **tú** diseñes y completes skills; el material incluye teoría, criterios de calidad, **seis enunciados** y **skills deliberadamente incompletas** que pueden fallar o no activarse si las usas tal cual.

## Objetivos de aprendizaje

Al terminar deberías poder:

1. Explicar qué es una skill, dónde vive en el proyecto y cómo la descubre el agente.
2. Redactar un frontmatter (`name`, `description`) que **dispare** la skill en el momento correcto.
3. Estructurar el cuerpo de `SKILL.md` (pasos, referencias, límites) sin duplicar documentación que ya está en el repo.
4. Detectar skills rotas o ambiguas y corregirlas siguiendo criterios explícitos.
5. (Opcional) Instalar skills de terceros con Node/`npx` y compararlas con las tuyas.

## Contexto: qué es una Agent Skill

Una **skill** es un archivo (normalmente `SKILL.md`) con instrucciones que el agente lee **cuando el contexto de la conversación encaja** con la `description` del frontmatter. No es un script que se ejecuta solo: es **contexto operativo** para el modelo.

Cursor descubre skills en rutas como:

| Ubicación | Alcance |
| --- | --- |
| `.cursor/skills/` | Proyecto (ideal para equipos; se versiona en Git) |
| `.agents/skills/` | Proyecto (convención alternativa compatible) |
| `~/.cursor/skills/` | Usuario (global en tu máquina) |

En **Cloud Agents** y entornos remotos, las skills globales de tu laptop **no** se copian automáticamente: prioriza skills **dentro del repositorio**.

Documentación oficial: [Agent Skills](https://cursor.com/docs/context/skills).

## Anatomía de `SKILL.md`

### Frontmatter (YAML)

Campos habituales:

```yaml
---
name: mi-skill-en-kebab-case
description: Qué hace la skill y cuándo debe usarse. Tercera persona. Incluye palabras clave que el usuario diría en chat.
---
```

| Campo | Criterio |
| --- | --- |
| `name` | Minúsculas, guiones, sin espacios; estable y único en el proyecto. |
| `description` | **Qué** + **cuándo**; frases que un estudiante o dev diría (“correr tests”, “publicar en npm”, “revisar PR”). Evita descripciones genéricas (“ayuda con código”). |
| Otros (opcional) | `allowed-tools`, `environments`, etc., según necesidad del flujo. |

Si falta o está mal la `description`, la skill **no se activará** o se activará en momentos incorrectos.

### Cuerpo (Markdown)

Buenas prácticas:

- **Conciso y accionable**: pasos numerados, comandos copy-paste, criterios de “hecho”.
- **Una responsabilidad**: una skill por flujo (p. ej. “release patch de npm”, no “todo el backend”).
- **Referencias**: archivos largos en `references/` y enlaces desde `SKILL.md`.
- **Límites explícitos**: cuándo **no** usar la skill, qué no tocar, prerequisitos (`node >= 20`, variables de entorno).
- **Convenciones del repo**: enlazar a `package.json`, scripts existentes, no inventar comandos.

Tamaño orientativo: preferible **&lt; 500 líneas** en `SKILL.md`; lo demás en referencias.

## Checklist antes de dar por buena una skill

- [ ] `name` en kebab-case y coherente con la carpeta.
- [ ] `description` con disparadores claros (3–5 frases útiles).
- [ ] Prerrequisitos listados (Node, `.env`, servicios).
- [ ] Pasos verificables y comandos probados en este repo.
- [ ] Sección “Cuándo no usar” o límites.
- [ ] Sin secretos ni tokens en el markdown.
- [ ] Probada: abrir un chat nuevo y pedir algo que **debería** activar la skill.

## Material incluido en este repositorio

```
recursos/
  plantillas/plantilla-SKILL.md     # punto de partida vacío
  skills-incompletas/               # ⚠️ NO usar en producción; solo para la práctica
    ejercicio-01-estructura-minima/
    ejercicio-02-scripts-npm/
    ejercicio-03-referencias/
    ejercicio-04-testing/
    ejercicio-05-seguridad-env/
    ejercicio-06-publicar-skill/
```

Cada carpeta bajo `skills-incompletas/` contiene un `SKILL.md` **incompleto** y un `PISTAS.md` con orientación (no solución literal).

---

## Actividad 0 (opcional, recomendada): instalar y auditar una skill con Node

Objetivo: ver una skill “real” de la comunidad y contrastarla con la plantilla de esta práctica.

**Requisitos:** Node.js y red (para `npx`).

1. En un **proyecto de prueba** (no hace falta que sea este repo), ejecuta:

   ```bash
   npx skills add owner/repo --agent cursor
   ```

   Sustituye `owner/repo` por un repositorio público que anuncie skills compatibles (por ejemplo entradas en [skills.sh](https://skills.sh/) orientadas a Cursor). Si el instalador es interactivo, elige **alcance de proyecto** (`.cursor/skills/` o `.agents/skills/`).

2. Abre **Customize → Skills** en Cursor y localiza la skill instalada.

3. Entrega un informe breve (máx. 1 página):

   - Ruta donde quedó instalada.
   - Copia del frontmatter (`name`, `description`) y tu opinión: ¿disparadores suficientes?
   - Una mejora concreta que harías (una sola, justificada).
   - Cómo la desinstalarías (`rm -rf` de la carpeta o reinstalar según documentación del CLI).

4. **No** commits de skills de terceros en este repo de práctica salvo que el enunciado de tu docente lo pida.

Alternativa sin CLI: clonar manualmente una carpeta con `SKILL.md` en `.cursor/skills/nombre-skill/`.

---

## Enunciado 1 — Estructura mínima viable

**Contexto:** El agente ignora skills mal formadas o con metadatos vacíos.

**Material:** `recursos/skills-incompletas/ejercicio-01-estructura-minima/SKILL.md` (⚠️ incompleta).

**Tarea:**

1. Copia la carpeta a `.cursor/skills/estructura-minima-node/` en un proyecto Node de práctica (puede ser un `npm init -y` vacío).
2. Completa frontmatter y secciones faltantes para que la skill enseñe al agente a **inicializar un paquete Node con estándares del curso** (ESM o CJS, según indique tu docente).
3. Escribe en el README del proyecto una tabla: campo → valor final → por qué importa.
4. Valida en un chat nuevo: “Ayúdame a preparar este repo Node desde cero siguiendo la skill del curso”.

**Criterios de evaluación:** frontmatter válido; al menos 4 pasos accionables; criterio de “listo” explícito.

---

## Enunciado 2 — Skill atada a `package.json`

**Contexto:** En proyectos Node, la skill debe **leer scripts reales**, no inventarlos.

**Material:** `recursos/skills-incompletas/ejercicio-02-scripts-npm/SKILL.md` (⚠️ incompleta).

**Tarea:**

1. Crea un mini-proyecto con scripts: `dev`, `lint`, `test`, `build` (pueden ser placeholders con `echo` al inicio).
2. Completa la skill para que el agente:
   - Consulte siempre `package.json` antes de proponer comandos.
   - Use `npm run` / `npx` de forma consistente.
   - Documente orden recomendado: lint → test → build antes de un commit.
3. Añade una sección **“Errores frecuentes”** con al menos 2 casos (script inexistente, Node version mismatch).

**Criterios:** la skill menciona nombres de scripts concretos de *tu* `package.json`; incluye “cuándo no usar” (p. ej. no ejecutar `build` en CI sin tests).

---

## Enunciado 3 — Skill con carpeta `references/`

**Contexto:** Skills largas son difíciles de mantener; el patrón **SKILL.md + references/** separa “cuándo actuar” del detalle.

**Material:** `recursos/skills-incompletas/ejercicio-03-referencias/SKILL.md` (⚠️ incompleta; enlaces rotos a referencias).

**Tarea:**

1. Completa `SKILL.md` con un flujo corto (máx. 80 líneas) para **añadir una dependencia de producción** con criterios del curso (lockfile, auditoría, semver).
2. Crea `references/auditoria-npm.md` y `references/semver-equipo.md` con el detalle.
3. En `SKILL.md`, tabla de “Workflow → Reference” como en skills oficiales de Cursor.
4. Demuestra que el agente puede seguir el flujo sin pegar todo el contenido en el chat.

**Criterios:** referencias existen y están enlazadas; SKILL.md no duplica párrafos enteros de las referencias.

---

## Enunciado 4 — Skill de testing (Jest o Vitest)

**Contexto:** El agente suele crear tests genéricos; la skill debe fijar **estructura de carpetas, convención de nombres y comando único de CI**.

**Material:** `recursos/skills-incompletas/ejercicio-04-testing/SKILL.md` (⚠️ incompleta).

**Tarea:**

1. Elige **Jest** o **Vitest** e instálalo en tu proyecto de práctica.
2. Completa la skill con:
   - Ubicación de tests (`__tests__/` o `*.test.ts`).
   - Cómo ejecutar tests en watch vs CI (`CI=true`, `--run`, etc.).
   - Qué hacer si falla un snapshot (cuándo actualizar vs corregir).
3. Añade un **ejemplo mínimo** de test (5–10 líneas) en el repo, no solo en la skill.

**Criterios:** un solo comando documentado para CI; la skill dice explícitamente “no desactivar tests para pasar el pipeline”.

---

## Enunciado 5 — Skill de secretos y variables de entorno

**Contexto:** Skills mal redactadas pueden empujar al agente a **commitear `.env`** o hardcodear API keys.

**Material:** `recursos/skills-incompletas/ejercicio-05-seguridad-env/SKILL.md` (⚠️ incompleta y peligrosa si no se corrige).

**Tarea:**

1. Añade `.env.example` a tu proyecto y asegura `.env` en `.gitignore`.
2. Reescribe la skill para un flujo seguro: cargar config con `dotenv` / `process.env`, validar variables requeridas al arranque, nunca imprimir secretos en logs.
3. Incluye checklist pre-commit (¿aparece `.env` en `git status`?).
4. Redacta `description` con disparadores: “variables de entorno”, “API key”, “config local”, “dotenv”.

**Criterios:** sección “Prohibido” clara; ejemplo de validación (pseudocódigo o código real); prueba conversacional pidiendo “guarda mi API key en el repo” — la skill debe orientar a **rechazar** esa petición.

---

## Enunciado 6 — Publicar y compartir una skill en el equipo

**Contexto:** Las skills de proyecto viven en Git; el objetivo es **empaquetar conocimiento** para todo el equipo Node.

**Material:** `recursos/skills-incompletas/ejercicio-06-publicar-skill/SKILL.md` (⚠️ incompleta).

**Tarea:**

1. Parte de la skill que **tú** completaste en los enunciados 1–5 (elige la mejor) y muévela a `.cursor/skills/<nombre-final>/`.
2. Completa la skill “publicar-skill” para documentar:
   - Convención de nombres de carpeta = `name` del frontmatter.
   - README del repo: sección “Skills del equipo” con tabla nombre / propósito / owner.
   - Proceso de revisión (PR checklist: description, secretos, comandos probados).
   - (Opcional) Cómo otros repos instalarían una copia vía `npx skills add ... --agent cursor`.
3. Abre un PR simulado (o real) en tu fork con solo la carpeta de skills y el README.

**Criterios:** skill instalable clonando el repo; otro compañero puede activarla sin instrucciones verbales extra.

---

## Entregables sugeridos (para el docente)

| Entregable | Enunciados |
| --- | --- |
| Repo Node con `.cursor/skills/` | 1–6 |
| Informe de auditoría de skill instalada | 0 |
| Captura o transcript de chat donde la skill se activa correctamente | 1, 2, 4, 5 |
| PR con skill de equipo | 6 |

## Errores típicos (para autoevaluación)

- Description demasiado corta: “Ayuda con Node”.
- Skill de 800 líneas sin `references/`.
- Comandos que no existen en `package.json`.
- Disparadores que compiten con otra skill del mismo repo (solapamiento).
- Usar skills incompletas de `recursos/skills-incompletas/` en `.cursor/skills/` **sin completarlas** → comportamiento impredecible del agente.

---

## Recursos adicionales

- [Cursor — Agent Skills](https://cursor.com/docs/context/skills)
- Plantilla local: `recursos/plantillas/plantilla-SKILL.md`
- Comando slash integrado en Cursor (si está disponible en tu versión): `/create-skill` para contrastar tu trabajo con la guía oficial.
