import unittest

from Proyecto.skills.product_owner import ProductOwnerSkill
from Proyecto.skills.qa import QASkill
from Proyecto.skills.architect import ArchitectSkill
from Proyecto.utils.formatter import ensure_markdown


class SkillTests(unittest.TestCase):
    def test_product_owner_mock_response_is_markdown(self) -> None:
        skill = ProductOwnerSkill(use_mock=True)
        output = skill.run("Necesito un sistema para agendar turnos médicos")
        self.assertIn("## Historia de Usuario", output)
        self.assertIn("**Como... Quiero... Para...**", output)

    def test_qa_mock_response_is_markdown(self) -> None:
        skill = QASkill(use_mock=True)
        output = skill.run("Como usuario quiero agendar turnos")
        self.assertIn("## Casos de Prueba Críticos", output)
        self.assertIn("QA-001", output)

    def test_architect_mock_response_is_markdown(self) -> None:
        skill = ArchitectSkill(use_mock=True)
        output = skill.run("Necesito una API para reservas")
        self.assertIn("## Recomendaciones Técnicas", output)
        self.assertIn("Streamlit", output)

    def test_ensure_markdown_returns_fallback_for_empty_input(self) -> None:
        self.assertEqual(ensure_markdown(""), "_Sin contenido generado._")


if __name__ == "__main__":
    unittest.main()
