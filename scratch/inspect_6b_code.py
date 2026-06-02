import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
nb_path = Path("src/arquivo/Etapa1_Tratamento_Dados/06b_Fronteira_Eficiente_Final_corrigido.ipynb")

with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

out_path = Path("scratch/code_6b.txt")
with open(out_path, "w", encoding="utf-8") as out:
    out.write("=== CODE CELLS OF NOTEBOOK 6b ===\n\n")
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            out.write(f"=== CELL {i} ===\n")
            out.write("".join(cell['source']))
            out.write("\n\n")

print(f"✓ All code cells dumped to {out_path}")
