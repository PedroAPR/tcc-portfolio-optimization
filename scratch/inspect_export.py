import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
nb_path = Path("src/arquivo/Etapa1_Tratamento_Dados/07_Inferencia_Econometrica_Desempenho_Final_corrigido.ipynb")

with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

for idx in [29, 30]:
    if idx < len(nb['cells']):
        cell = nb['cells'][idx]
        print(f"=== Cell {idx} ({cell['cell_type']}) ===")
        print("".join(cell['source']))
        print("="*60)
