# Instrucciones para este proyecto

## Propósito general
Este repositorio contiene una aplicación Streamlit que transforma un requerimiento informal en artefactos de negocio y técnica:
1. Historia de usuario (Product Owner)
2. Casos de prueba críticos (QA)
3. Recomendaciones de arquitectura

## Estructura importante
- La app principal está en Proyecto/main.py.
- Las skills están en Proyecto/skills/.
- Los prompts están en Proyecto/prompts/ como archivos Markdown.
- Las utilidades de formato están en Proyecto/utils/formatter.py.

## Reglas de trabajo
- Mantener el flujo principal consistente: recibir un requerimiento, procesarlo por las skills y mostrar resultados en Markdown.
- Si se modifica una skill, conservar la interfaz esperada: clase responsable, método run() y fallback a respuesta mock cuando no haya API disponible.
- Si se editan prompts, mantenerlos claros, breves y orientados a un rol específico (Product Owner, QA o Arquitectura).
- Preferir cambios pequeños y localizados; no introducir dependencias nuevas si no son necesarias.
- Mantener compatibilidad con la ejecución desde la raíz del proyecto y desde la carpeta Proyecto.

## Convenciones de código
- Usar Python moderno con tipado simple cuando sea útil.
- Mantener el output en Markdown para que se pueda renderizar bien en la interfaz.
- Respetar la separación entre lógica de negocio, prompts y presentación.
- Cuando se agregue una nueva skill, seguir el patrón existente: cargar prompt desde archivo, soportar modo mock y exponer run().

## Comportamiento esperado
- La app debe seguir funcionando aunque la integración con IA real no esté disponible.
- Si falta una API key o un paquete externo, el sistema debe caer de forma segura a una respuesta mock.
- Los mensajes de error deben ser claros y no romper la interfaz.
