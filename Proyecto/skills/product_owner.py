"""Skill para generar historia de usuario estilo Product Owner."""

from __future__ import annotations

from pathlib import Path

try:
    from config import is_mock_mode
    from utils.formatter import clean_text, ensure_markdown
except ModuleNotFoundError:
    from Proyecto.config import is_mock_mode
    from Proyecto.utils.formatter import clean_text, ensure_markdown


class ProductOwnerSkill:
    """Transforma requerimientos en historia de usuario con criterios de aceptación."""

    def __init__(self, prompt_path: str | Path | None = None, use_mock: bool | None = None) -> None:
        base_dir = Path(__file__).resolve().parents[1]
        self.prompt_path = Path(prompt_path) if prompt_path else base_dir / "prompts" / "historia.md"
        self.system_prompt = self._load_prompt()
        self.use_mock = is_mock_mode() if use_mock is None else use_mock

    def _load_prompt(self) -> str:
        if not self.prompt_path.exists():
            raise FileNotFoundError(f"No se encontró el prompt: {self.prompt_path}")
        return self.prompt_path.read_text(encoding="utf-8").strip()

    def run(self, user_requirement: str) -> str:
        requirement = clean_text(user_requirement)
        if not requirement:
            raise ValueError("El requerimiento del usuario no puede estar vacío.")
        if self.use_mock:
            return ensure_markdown(self._mock_response(requirement))
        return ensure_markdown(self._invoke_antigravity(requirement))

    def _invoke_antigravity(self, requirement: str) -> str:
        """
        Punto de integración para SDK real.
        Si el SDK no está disponible, cae de forma segura al mock.
        """
        try:
            import antigravity  # noqa: F401
        except Exception:
            return self._mock_response(requirement)

        # Placeholder para implementación real del cliente IA.
        return self._mock_response(requirement)

    def _mock_response(self, requirement: str) -> str:
        short_req = requirement.split("\n")[0][:180]
        return f"""
## Historia de Usuario
Como usuario del producto,
Quiero {short_req.lower().rstrip('.')},
Para obtener valor de negocio de manera rápida y consistente.

## Criterios de Aceptación
- El sistema transforma el requerimiento en el formato **Como... Quiero... Para...**.
- La historia de usuario es clara, verificable y orientada a valor.
- El resultado se entrega en Markdown listo para documentación.
"""
