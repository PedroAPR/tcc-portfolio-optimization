# tests/conftest.py
"""
Configuração compartilhada do pytest para a suíte de auditoria do TCC.
Adiciona src/07 e src/09 ao PYTHONPATH para importar os módulos utils.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src" / "07_Otimizacao_Carteiras"))
sys.path.insert(0, str(ROOT / "src" / "09_Inferencia_Econometrica"))
