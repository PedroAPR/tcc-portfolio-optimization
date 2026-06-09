import json
import sys
from pathlib import Path

# Set console output encoding to utf-8
sys.stdout.reconfigure(encoding='utf-8')

project_root = Path(r"C:\VSCodeWorkspace\1_TCC_Final")
src_dir = project_root / "src"

def load_notebook(nb_path):
    with open(nb_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_notebook(nb_path, nb_data):
    with open(nb_path, "w", encoding="utf-8") as f:
        json.dump(nb_data, f, ensure_ascii=False, indent=1)
    print(f"  [OK] Notebook saved: {nb_path.name}")

# -----------------------------------------------------------------------------
# 1. UPDATE MENTIONS OF OLD COUNTS IN MARKDOWNS
# -----------------------------------------------------------------------------

# A. Update 06_01_Estimacao_LedoitWolf.ipynb (Cell 13)
print("Updating 06_01_Estimacao_LedoitWolf.ipynb...")
nb_path_6 = src_dir / "06_Estimacao_Covariancia" / "06_01_Estimacao_LedoitWolf.ipynb"
nb_data_6 = load_notebook(nb_path_6)

# Find Cell 13
cell_6_13 = nb_data_6["cells"][13]
if cell_6_13["cell_type"] == "markdown":
    text = "".join(cell_6_13["source"])
    
    # Apply replacements
    replacements = [
        ("retornos simples diários ($3.966 \\times 118$)", "retornos simples diários ($3.966 \\times 102$)"),
        ("formato $N \\times N$ ($118 \\times 118$)", "formato $N \\times N$ ($102 \\times 102$)"),
        ("para as 118 ações históricas", "para as 102 ações históricas"),
        ("($118 \\times 1$)", "($102 \\times 1$)"),
        ("N \times N$ ($118 \times 118$)", "N \times N$ ($102 \times 102$)"),
        ("N \times 1$ ($118 \times 1$)", "N \times 1$ ($102 \times 1$)"),
        ("para as 118 ações", "para as 102 ações"),
        ("33,61", "38,88"),
        ("4,27", "4,94"),
        ("2,14", "2,47"),
        ("1,07", "1,24"),
        ("0,53", "0,62")
    ]
    
    for old, new in replacements:
        text = text.replace(old, new)
        
    cell_6_13["source"] = [line + "\n" for line in text.split("\n")]
    # Remove trailing newline from last line if split added one
    if cell_6_13["source"] and cell_6_13["source"][-1] == "\n":
        cell_6_13["source"].pop()
    # strip trailing newlines on list items except the last line
    cell_6_13["source"] = [line if idx == len(cell_6_13["source"]) - 1 else line for idx, line in enumerate(cell_6_13["source"])]
    save_notebook(nb_path_6, nb_data_6)


# B. Update 07_01_Otimizacao_Carteiras.ipynb (Cell 5)
print("\nUpdating 07_01_Otimizacao_Carteiras.ipynb...")
nb_path_7 = src_dir / "07_Otimizacao_Carteiras" / "07_01_Otimizacao_Carteiras.ipynb"
nb_data_7 = load_notebook(nb_path_7)

cell_7_5 = nb_data_7["cells"][5]
if cell_7_5["cell_type"] == "markdown":
    text = "".join(cell_7_5["source"])
    text = text.replace("retornos simples saneados (118 ativos) provêm do NB04", "retornos simples saneados (102 ativos) provêm do NB05")
    cell_7_5["source"] = [line + "\n" for line in text.split("\n")]
    if cell_7_5["source"] and cell_7_5["source"][-1] == "\n":
        cell_7_5["source"].pop()
    save_notebook(nb_path_7, nb_data_7)


# -----------------------------------------------------------------------------
# 2. ADD "TEN SIMPLE RULES" TABLE TO THE THREE NOTEBOOKS MISSING IT
# -----------------------------------------------------------------------------

# Helper to build the cell dict
def build_rules_cell(notebook_name, evidence_rows):
    lines = [
        "# Autoavaliação — *Ten Simple Rules* (Rule et al., 2019)\n",
        "\n",
        "> Rule A, Birmingham A, Zuniga C, Altintas I, Huang S-C, Knight R, Moshiri N, Nguyen MH,\n",
        "> Rosenthal SB, Pérez F, Rose PW. *Ten simple rules for writing and sharing computational analyses\n",
        "> in Jupyter Notebooks.* PLOS Comput Biol. 2019;15(7):e1007007.\n",
        "\n",
        "| Regra | Tema | Status | Evidência / Aplicação no " + notebook_name + " |\n",
        "| :---: | :--- | :---: | :--- |\n"
    ]
    
    rules = [
        "Contar uma história",
        "Documentar o processo",
        "Divisão clara de células",
        "Modularizar código",
        "Registrar dependências",
        "Controle de versão",
        "Construir um pipeline",
        "Compartilhar/explicar dados",
        "Ler, rodar e explorar",
        "Pesquisa aberta"
    ]
    
    for idx, rule in enumerate(rules, 1):
        lines.append(f"| {idx} | {rule} | ✅ | {evidence_rows[idx-1]} |\n")
        
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": lines
    }

# A. Add to 03_01a_Pre_Integridade.ipynb
print("\nAdding Ten Simple Rules table to 03_01a_Pre_Integridade.ipynb...")
nb_path_3a = src_dir / "03_Filtro_Liquidez" / "03_01a_Pre_Integridade.ipynb"
nb_data_3a = load_notebook(nb_path_3a)

evidence_3a = [
    "Explica a ingestão, filtros de presença (95%), IPO tardio e cálculo de liquidez ADTV (p10).",
    "Racional das escolhas de corte e períodos de formação descritos em Markdown.",
    "Células curtas e modulares com explicações prévias das equações e critérios de corte.",
    "Importa funções utilitárias e parâmetros via config_loader.",
    "Dependências controladas em requirements.txt.",
    "Arquivo sob versionamento Git.",
    "Primeiro passo do estágio de liquidez, exportando universo_pos_liquidez.csv.",
    "Declara o uso de cotações Economática (proprietárias) e define o dicionário de variáveis.",
    "Executável de ponta a ponta sem erros.",
    "Código disponibilizado abertamente no repositório."
]

rules_cell_3a = build_rules_cell("NB 03_01a (Pré-Liquidez)", evidence_3a)
nb_data_3a["cells"].append(rules_cell_3a)
save_notebook(nb_path_3a, nb_data_3a)


# B. Add to 03_01c_Pos_Integridade.ipynb
print("\nAdding Ten Simple Rules table to 03_01c_Pos_Integridade.ipynb...")
nb_path_3c = src_dir / "03_Filtro_Liquidez" / "03_01c_Pos_Integridade.ipynb"
nb_data_3c = load_notebook(nb_path_3c)

evidence_3c = [
    "Explica a aplicação da lista de exclusão do classificador de integridade sobre a base de liquidez.",
    "Documenta a filtragem das 16 penny stocks/ativos sob distress severo na Etapa VII.",
    "Células modulares para filtragem e gravação final dos dados.",
    "Utiliza funções padrão e importador do config central.",
    "Dependências documentadas no repositório.",
    "Código sob controle de versão.",
    "Terceiro passo da Etapa 3 unificada, gerando a matriz final Matriz_precos_sanitizada.csv.",
    "Explica a aplicação das exclusões de integridade a partir do classificador.",
    "Executável sem estados ocultos.",
    "Código livre sob licença aberta."
]

rules_cell_3c = build_rules_cell("NB 03_01c (Pós-Integridade)", evidence_3c)
nb_data_3c["cells"].append(rules_cell_3c)
save_notebook(nb_path_3c, nb_data_3c)


# C. Add to Apendice_Classificador_Integridade_Universo_v2.ipynb
print("\nAdding Ten Simple Rules table to Apendice_Classificador_Integridade_Universo_v2.ipynb...")
nb_path_class = src_dir / "11_Classificador_Integridade" / "Apendice_Classificador_Integridade_Universo_v2.ipynb"
nb_data_class = load_notebook(nb_path_class)

evidence_class = [
    "Explica a lógica de auditoria point-in-time usando dados brutos do COTAHIST (B3).",
    "Define os três pilares objetivos de exclusão (reorganizações, CODBDI especial, penny stocks).",
    "Divisão em células de carga, análise por ativo, e consolidação de exportação.",
    "Modularizado em rotinas de leitura de lote de arquivos zip/csv da B3.",
    "Utiliza pandas e numpy definidos em requirements.",
    "Sob controle de versão Git.",
    "Integrado no fluxo de integridade da Etapa 3, exportando tickers_excluidos_integridade.csv.",
    "Indica o download dos dados públicos históricos do COTAHIST (B3).",
    "Executa de ponta a ponta gerando o mesmo resumo de 102 mantidos / 16 excluídos.",
    "Metodologia de auditoria publicada livremente."
]

rules_cell_class = build_rules_cell("Apêndice Classificador de Integridade", evidence_class)
nb_data_class["cells"].append(rules_cell_class)
save_notebook(nb_path_class, nb_data_class)

print("\nNotebook markdown updates completed successfully!")
