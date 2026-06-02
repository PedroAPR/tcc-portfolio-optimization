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
        if any(x in source for x in ["apendice_K", "apendice_L", "apendice_G", "apendice_H"]):
            print(f"Cell {i} contains matching variables:")
            for line in source.split("\n"):
                if any(x in line for x in ["apendice_K", "apendice_L", "apendice_G", "apendice_H", "apendice"]):
                    print("  ", line.strip())
