import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
nb_path = Path("src/arquivo/Etapa1_Tratamento_Dados/07_Inferencia_Econometrica_Desempenho_Final_corrigido.ipynb")

with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        source = "".join(cell['source'])
        if "def diagnostico_residuos" in source:
            print(f"=== Cell {i} ===")
            print(source)


