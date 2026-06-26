# Guía de comentarios para las skills

Esta guía está pensada para pegarse justo encima de las clases y funciones, de forma que el editor pueda inferir mejor la intención.

## ProductOwnerSkill

```python
# Clase encargada de transformar un requerimiento en una historia de usuario en formato Scrum.
# Debe cargar un prompt, limpiar la entrada y generar una respuesta Markdown.
class ProductOwnerSkill:
    pass
```

```python
# Método utilizado para inicializar la skill con la ruta del prompt y el modo de ejecución.
# Debe configurar el prompt base y decidir si se usa mock o integración real.
def __init__(self, prompt_path=None, use_mock=None):
    pass
```

```python
# Método utilizado para cargar el prompt desde un archivo Markdown.
# Debe validar que el archivo exista y devolver su contenido como texto.
def _load_prompt(self):
    pass
```

```python
# Método utilizado para ejecutar la lógica principal de la skill.
# Debe recibir el requerimiento, limpiarlo y devolver una historia de usuario en Markdown.
def run(self, user_requirement):
    pass
```

```python
# Método utilizado para integrar la lógica con un servicio de IA real.
# Si la integración no está disponible, debe devolver la respuesta mock.
def _invoke_antigravity(self, requirement):
    pass
```

```python
# Método utilizado para generar una respuesta de respaldo en formato Markdown.
# Debe devolver una historia de usuario estructurada cuando no haya API disponible.
def _mock_response(self, requirement):
    pass
```

## QASkill

```python
# Clase encargada de generar casos de prueba críticos a partir de una historia de usuario.
# Debe cargar un prompt y producir resultados en formato Markdown.
class QASkill:
    pass
```

```python
# Método utilizado para inicializar la skill de QA con el prompt correspondiente.
# Debe configurar el prompt base y definir el modo de ejecución.
def __init__(self, prompt_path=None, use_mock=None):
    pass
```

```python
# Método utilizado para cargar el prompt de QA desde un archivo Markdown.
# Debe leer el contenido del archivo y devolverlo como texto.
def _load_prompt(self):
    pass
```

```python
# Método utilizado para ejecutar la generación de casos de prueba críticos.
# Debe recibir la historia de usuario y devolver casos de prueba en Markdown.
def run(self, user_story_markdown):
    pass
```

```python
# Método utilizado para integrar la skill con un servicio de IA real.
# Si no hay SDK o conexión, debe caer al modo mock.
def _invoke_antigravity(self, story):
    pass
```

```python
# Método utilizado para generar una respuesta de respaldo para QA.
# Debe devolver casos de prueba estructurados aunque no haya integración real.
def _mock_response(self, story):
    pass
```

## ArchitectSkill

```python
# Clase encargada de generar recomendaciones técnicas de arquitectura.
# Debe cargar un prompt y producir un resultado en Markdown orientado a decisiones técnicas.
class ArchitectSkill:
    pass
```

```python
# Método utilizado para inicializar la skill de arquitectura con el prompt adecuado.
# Debe definir si se ejecuta con mock o con integración real.
def __init__(self, prompt_path=None, use_mock=None):
    pass
```

```python
# Método utilizado para cargar el prompt de arquitectura desde un archivo Markdown.
# Debe leer el contenido del archivo y devolverlo como texto.
def _load_prompt(self):
    pass
```

```python
# Método utilizado para ejecutar la generación de recomendaciones técnicas.
# Debe recibir el requerimiento y devolver recomendaciones de arquitectura en Markdown.
def run(self, user_requirement):
    pass
```

```python
# Método utilizado para integrar la skill con un servicio de IA real.
# Si no hay disponibilidad, debe usar la respuesta mock.
def _invoke_antigravity(self, requirement):
    pass
```

```python
# Método utilizado para crear una salida de respaldo de arquitectura.
# Debe entregar buenas prácticas, riesgos y tecnologías sugeridas en formato Markdown.
def _mock_response(self, requirement):
    pass
```
