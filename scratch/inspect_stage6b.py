import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
nb_path = Path("src/arquivo/Etapa1_Tratamento_Dados/06b_Fronteira_Eficiente_Final_corrigido.ipynb")

with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

print(f"Total cells: {len(nb['cells'])}")
print("="*60)
for i, cell in enumerate(nb['cells']):
    ctype = cell.get("cell_type")
    source = "".join(cell.get("source", []))
    
    if ctype == "markdown":
        print(f"Cell {i} (MD):\n{source.strip()[:400]}")
        print("-"*40)
    elif ctype == "code":
        code_str = source.lower()
        if any(x in code_str for x in ["read_csv", "read_parquet", "to_csv", "to_parquet", "minimize", "solve", "plot", "savefig"]):
            print(f"Cell {i} (Code):\n{source[:400]}")
            print("-"*40)
