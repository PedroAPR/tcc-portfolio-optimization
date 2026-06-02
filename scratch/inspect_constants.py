import json
from pathlib import Path

nb_path = Path("src/arquivo/Etapa1_Tratamento_Dados/07_Inferencia_Econometrica_Desempenho_Final_corrigido.ipynb")

with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

print("=== CODE CELLS IN DETAIL ===")
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        source = "".join(cell['source'])
        # Look for assignments of uppercase variables or paths
        lines = source.split("\n")
        printed_cell = False
        for line in lines:
            line_s = line.strip()
            if not line_s or line_s.startswith("#"):
                continue
            # simple heuristic for constants: uppercase variable name = value
            if "=" in line_s and not line_s.startswith("self."):
                left = line_s.split("=")[0].strip()
                if left.isupper() and len(left) > 1:
                    if not printed_cell:
                        print(f"\n--- Cell {i} ---")
                        printed_cell = True
                    print(f"  {line_s}")
