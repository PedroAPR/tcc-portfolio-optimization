# tests/conftest.py
"""
Configuração compartilhada do pytest para a suíte de auditoria do TCC.
Adiciona src/ ao PYTHONPATH para importar os módulos utils centrais.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(1, str(ROOT / "src" / "07_Otimizacao_Carteiras"))
sys.path.insert(2, str(ROOT / "src" / "09_Inferencia_Econometrica"))
