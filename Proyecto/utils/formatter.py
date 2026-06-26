"""Utilidades de formato para salidas Markdown en la UI."""

from __future__ import annotations

import re
from textwrap import dedent


def clean_text(text: str) -> str:
    """Limpia espacios redundantes sin alterar la semántica del contenido."""
    normalized = dedent(text).replace("\r\n", "\n").strip()
    # Reduce múltiples líneas en blanco consecutivas a un máximo de una.
    return re.sub(r"\n{3,}", "\n\n", normalized)


def ensure_markdown(text: str, fallback: str = "_Sin contenido generado._") -> str:
    """Asegura que siempre exista contenido Markdown válido para renderizar."""
    if not text or not text.strip():
        return fallback
    return clean_text(text)


def extract_code_blocks(markdown_text: str, language: str | None = None) -> list[str]:
    """Extrae bloques de código de un Markdown, filtrando opcionalmente por lenguaje."""
    pattern = r"```(?P<lang>[a-zA-Z0-9_-]*)\n(?P<code>.*?)```"
    matches = re.finditer(pattern, markdown_text, flags=re.DOTALL)
    blocks: list[str] = []
    for match in matches:
        block_lang = match.group("lang").strip().lower()
        if language and block_lang != language.lower():
            continue
        blocks.append(match.group("code").strip())
    return blocks
