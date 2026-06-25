"""Skill para emitir recomendaciones técnicas de arquitectura."""

from __future__ import annotations

import os
from pathlib import Path

try:
    from utils.formatter import clean_text, ensure_markdown
except ModuleNotFoundError:
    from Proyecto.utils.formatter import clean_text, ensure_markdown


class ArchitectSkill:
    """Analiza requerimientos y sugiere lineamientos de arquitectura."""

    def __init__(self, prompt_path: str | Path | None = None, use_mock: bool | None = None) -> None:
        base_dir = Path(__file__).resolve().parents[1]
        self.prompt_path = Path(prompt_path) if prompt_path else base_dir / "prompts" / "arquitectura.md"
        self.system_prompt = self._load_prompt()
        self.use_mock = (not bool(os.getenv("ANTIGRAVITY_API_KEY"))) if use_mock is None else use_mock

    def _load_prompt(self) -> str:
        if not self.prompt_path.exists():
            raise FileNotFoundError(f"No se encontró el prompt: {self.prompt_path}")
        return self.prompt_path.read_text(encoding="utf-8").strip()

    def run(self, user_requirement: str) -> str:
        requirement = clean_text(user_requirement)
        if not requirement:
            raise ValueError("El requerimiento no puede estar vacío.")
        if self.use_mock:
            return ensure_markdown(self._mock_response(requirement))
        return ensure_markdown(self._invoke_antigravity(requirement))

    def _invoke_antigravity(self, requirement: str) -> str:
        try:
            import antigravity  # noqa: F401
        except Exception:
            return self._mock_response(requirement)

        # Placeholder de integración real con antigravity/SDK de cátedra.
        return self._mock_response(requirement)

    def _mock_response(self, requirement: str) -> str:
        topic = requirement.split("\n")[0][:160]
        return f"""
## Recomendaciones Técnicas

### Buenas prácticas
- Diseñar skills desacopladas con responsabilidades claras (PO, QA y Arquitectura).
- Mantener prompts versionados en archivos `.md` para facilitar auditoría y cambios.
- Aplicar validaciones de entrada y fallback a cliente mock cuando no haya API key.

### Riesgos potenciales
- Dependencia de salida generativa no determinística en entornos con IA real.
- Ambigüedad de requerimientos ({topic}) que podría afectar calidad de historias y pruebas.
- Falta de trazabilidad si no se registran inputs y outputs por ejecución.

### Tecnologías sugeridas
- **Streamlit** para interfaz full-stack rápida y mantenible.
- **Python 3.12+** y tipado estático básico para robustez.
- Cliente IA basado en `antigravity` (o wrapper compatible) con estrategia de retry/fallback.
"""
