import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

nb_path = Path("src/arquivo/Etapa1_Tratamento_Dados/07_Inferencia_Econometrica_Desempenho_Final_corrigido.ipynb")

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
        # Print if there is any reading/writing or model fitting
        code_str = source.lower()
        if any(x in code_str for x in ["read_csv", "read_parquet", "to_csv", "to_parquet", "ols", "statsmodels", "regress", "t-test", "ttest", "jarque", "wilcoxon"]):
            print(f"Cell {i} (Code - Data/Model):\n{source[:400]}")
            print("-"*40)
