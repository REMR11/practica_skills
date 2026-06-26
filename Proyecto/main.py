"""Aplicación Streamlit para generar documentación ágil asistida por IA."""

from __future__ import annotations

import streamlit as st

try:
    from config import load_settings
    from skills.architect import ArchitectSkill
    from skills.product_owner import ProductOwnerSkill
    from skills.qa import QASkill
    from utils.formatter import ensure_markdown
except ModuleNotFoundError:
    from Proyecto.config import load_settings
    from Proyecto.skills.architect import ArchitectSkill
    from Proyecto.skills.product_owner import ProductOwnerSkill
    from Proyecto.skills.qa import QASkill
    from Proyecto.utils.formatter import ensure_markdown


def inject_styles() -> None:
    st.markdown(
        """
        <style>
            .stApp {
                background: radial-gradient(circle at top, #1a1e2d 0%, #0f1118 55%, #0a0b10 100%);
                color: #e8eefc;
            }
            .main-title {
                font-size: 2rem;
                font-weight: 700;
                letter-spacing: 0.3px;
                margin-bottom: 0.35rem;
            }
            .subtitle {
                color: #a9b3d0;
                margin-bottom: 1.2rem;
            }
            .card {
                border: 1px solid #2f3854;
                background: linear-gradient(145deg, #131726 0%, #0f1320 100%);
                border-radius: 14px;
                padding: 1rem;
                margin-top: 0.75rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def init_session_state() -> None:
    st.session_state.setdefault("results", None)


@st.cache_resource
def build_skills() -> tuple[ProductOwnerSkill, QASkill, ArchitectSkill]:
    return ProductOwnerSkill(), QASkill(), ArchitectSkill()


def run_pipeline(requirement: str) -> dict[str, str]:
    po_skill, qa_skill, architect_skill = build_skills()

    with st.status("Procesando requerimiento...", expanded=True) as status:
        status.write("1/3 - Product Owner: generando historia de usuario...")
        historia = po_skill.run(requirement)

        status.write("2/3 - QA: generando casos de prueba críticos...")
        qa_cases = qa_skill.run(historia)

        status.write("3/3 - Arquitectura: generando recomendaciones técnicas...")
        architecture = architect_skill.run(requirement)

        status.update(label="Documentación generada correctamente", state="complete")

    return {
        "product_owner": historia,
        "qa": qa_cases,
        "arquitectura": architecture,
    }


def main() -> None:
    st.set_page_config(
        page_title="AI Product Docs Dashboard",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    inject_styles()
    init_session_state()

    settings = load_settings()

    st.markdown('<div class="main-title">🧠 Generador de Documentación IA</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Convierte una necesidad informal en artefactos de Product Owner, QA y Arquitectura.</div>',
        unsafe_allow_html=True,
    )

    if settings.use_mock_by_default:
        st.info("Modo actual: fallback mock activo. Define ANTIGRAVITY_API_KEY para habilitar la integración real.")
    else:
        st.success("Modo actual: integración IA habilitada.")

    with st.expander("Cómo usar esta app", expanded=False):
        st.write("1. Describe la necesidad del cliente.")
        st.write("2. Ejecuta el pipeline para generar Historia, QA y Arquitectura.")
        st.write("3. Revisa los resultados en las pestañas de la interfaz.")

    requirement = st.text_area(
        "Necesidad del cliente",
        height=220,
        placeholder="Ejemplo: Necesitamos una plataforma para reservar turnos médicos, con recordatorios y panel de administración.",
    )

    if st.button("Generar Documentación", type="primary", use_container_width=True):
        if not requirement.strip():
            st.warning("Por favor, ingresa una necesidad antes de ejecutar el pipeline.")
        else:
            try:
                st.session_state["results"] = run_pipeline(requirement)
            except Exception as exc:  # pragma: no cover - UI safety net
                st.error(f"No se pudo generar la documentación: {exc}")

    results = st.session_state.get("results")
    if not results:
        st.info("Carga un requerimiento y presiona **Generar Documentación** para ver resultados.")
        return

    tabs = st.tabs(["📌 Product Owner", "✅ QA", "🏗️ Arquitectura"])

    with tabs[0]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(ensure_markdown(results.get("product_owner", "")))
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[1]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(ensure_markdown(results.get("qa", "")))
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[2]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(ensure_markdown(results.get("arquitectura", "")))
        st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
