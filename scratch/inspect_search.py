import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

nb_path = Path("src/arquivo/Etapa1_Tratamento_Dados/07_Inferencia_Econometrica_Desempenho_Final_corrigido.ipynb")

with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

search_terms = ["bootstrap", "garch", "spanning", "memmel", "jobson", "hac", "newey", "wald", "opt_block", "arch_model"]

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        source = "".join(cell['source'])
        lines = source.split("\n")
        printed = False
        for j, line in enumerate(lines):
            if any(term in line.lower() for term in search_terms):
                if not printed:
                    print(f"\n--- Cell {i} ---")
                    printed = True
                # Print 3 lines before and after
                start = max(0, j - 2)
                end = min(len(lines), j + 3)
                print(f"Line {j}:")
                for k in range(start, end):
                    marker = ">> " if k == j else "   "
                    print(f"{marker}{k}: {lines[k]}")
                print("...")
