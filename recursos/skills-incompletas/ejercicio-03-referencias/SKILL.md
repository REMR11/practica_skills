---
name: dependencias-produccion
description: Instalar paquetes npm en proyectos Node cuando el usuario pide añadir una librería o dependencia de producción.
---

# ⚠️ SKILL INCOMPLETA — NO USAR EN PRODUCCIÓN

> Enlaces a referencias **inexistentes** y flujo truncado. El agente puede alucinar políticas de semver. Ver **Enunciado 3**.

# Añadir dependencia de producción

Flujo rápido para el agente.

## Pasos

1. Confirmar nombre del paquete y si es `dependencies` vs `devDependencies`.
2. Ejecutar instalación con lockfile (¿`npm install pkg`? ¿ `--save-exact`? — **sin política de equipo**).
3. Detalle de auditoría y semver: ver `references/archivo-que-no-existe.md`.

## Workflow → Reference

| Paso | Referencia |
| --- | --- |
| Auditoría | `references/auditoria-npm.md` (**falta crear**) |
| Semver | `references/semver-equipo.md` (**falta crear**) |

## Criterio de hecho

- Paquete en `package.json`
- (falta: lockfile, audit, changelog si aplica)
