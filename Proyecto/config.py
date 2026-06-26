"""Configuración compartida para la aplicación y las skills."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AppSettings:
    """Valores de configuración cargados desde variables de entorno."""

    antigravity_api_key: str | None
    streamlit_port: int
    use_mock_by_default: bool


def load_settings() -> AppSettings:
    """Carga la configuración de entorno con valores por defecto seguros."""

    raw_api_key = os.getenv("ANTIGRAVITY_API_KEY", "").strip()
    return AppSettings(
        antigravity_api_key=raw_api_key or None,
        streamlit_port=int(os.getenv("STREAMLIT_SERVER_PORT", "8501")),
        use_mock_by_default=not bool(raw_api_key),
    )


def is_mock_mode(api_key: str | None = None) -> bool:
    """Devuelve si el pipeline debe usar el fallback mock."""

    if api_key is not None:
        return not bool(api_key.strip())
    return load_settings().use_mock_by_default
