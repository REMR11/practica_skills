"""Skill para generar casos de prueba críticos a partir de una historia."""

from __future__ import annotations

from pathlib import Path

try:
    from config import is_mock_mode
    from utils.formatter import clean_text, ensure_markdown
except ModuleNotFoundError:
    from Proyecto.config import is_mock_mode
    from Proyecto.utils.formatter import clean_text, ensure_markdown


class QASkill:
    """Genera casos de prueba funcionales en formato Markdown estructurado."""

    def __init__(self, prompt_path: str | Path | None = None, use_mock: bool | None = None) -> None:
        base_dir = Path(__file__).resolve().parents[1]
        self.prompt_path = Path(prompt_path) if prompt_path else base_dir / "prompts" / "qa.md"
        self.system_prompt = self._load_prompt()
        self.use_mock = is_mock_mode() if use_mock is None else use_mock

    def _load_prompt(self) -> str:
        if not self.prompt_path.exists():
            raise FileNotFoundError(f"No se encontró el prompt: {self.prompt_path}")
        return self.prompt_path.read_text(encoding="utf-8").strip()

    def run(self, user_story_markdown: str) -> str:
        story = clean_text(user_story_markdown)
        if not story:
            raise ValueError("La historia de usuario no puede estar vacía.")
        if self.use_mock:
            return ensure_markdown(self._mock_response(story))
        return ensure_markdown(self._invoke_antigravity(story))

    def _invoke_antigravity(self, story: str) -> str:
        try:
            import antigravity  # noqa: F401
        except Exception:
            return self._mock_response(story)

        # Placeholder de integración real; fallback al mock para entorno sin SDK.
        return self._mock_response(story)

    def _mock_response(self, story: str) -> str:
        summary = story.splitlines()[0][:120]
        return f"""
## Casos de Prueba Críticos

### Caso ID: QA-001
- **Precondición:** El usuario está autenticado y puede acceder al módulo principal.
- **Pasos:**
  1. Ingresar un requerimiento válido.
  2. Ejecutar la generación de documentación.
  3. Revisar la historia de usuario obtenida.
- **Resultado Esperado:** Se genera una historia alineada al formato Scrum sin errores.

### Caso ID: QA-002
- **Precondición:** Existe conectividad a la capa de IA o mock activo.
- **Pasos:**
  1. Ejecutar el pipeline con el input: "{summary}".
  2. Verificar sección de QA en la interfaz.
- **Resultado Esperado:** Se muestran entre 1 y 3 casos de prueba con estructura completa.

### Caso ID: QA-003
- **Precondición:** El sistema está inicializado.
- **Pasos:**
  1. Intentar ejecutar con input vacío.
  2. Revisar la respuesta del sistema.
- **Resultado Esperado:** Se informa validación de entrada y no se rompe el flujo de la aplicación.
"""
