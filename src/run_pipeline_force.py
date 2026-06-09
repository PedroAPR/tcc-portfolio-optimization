import os
import sys
import time
import subprocess
from pathlib import Path

# Configura a saída padrão para UTF-8 para evitar problemas de codificação no Windows
sys.stdout.reconfigure(encoding="utf-8")

# Caminhos do projeto
src_dir = Path(__file__).resolve().parent
project_root = src_dir.parent

# ─────────────────────────────────────────────────────────────────────────────
# ETAPA 3 — Tratamento especial
# ─────────────────────────────────────────────────────────────────────────────
# O NB03 (Filtro de Liquidez) precisava rodar em duas passagens com o
# Classificador de Integridade no meio. O orquestrador anterior tratava os três
# como blocos independentes e sofria de path mismatch (Classificador gravava em
# data/, NB03 lia de data/Tickers/), fazendo a exclusão de integridade ser pulada.
#
# Solução: a Etapa 3 agora é delegada ao script `run_etapa03.py`, que:
#   (1) roda 03_01a_Pre_Integridade.ipynb  → exporta universo_pos_liquidez.csv
#   (2) roda o Classificador v2 com PASTA_SAIDA corrigido para data/Tickers/
#   (3) roda 03_01c_Pos_Integridade.ipynb  → grava a matriz final
#
# As entradas antigas (NB03 + Classificador + NB03) foram REMOVIDAS da lista
# abaixo e substituídas por uma entrada do tipo "script" que chama run_etapa03.py.
# ─────────────────────────────────────────────────────────────────────────────

# Ordem cronológica dos estágios do pipeline
# Cada entrada pode ser do tipo "notebook" (usa nbconvert) ou "script" (chama python direto)
pipeline_stages = [
    {
        "name": "01_Conversao_Parquet",
        "type": "notebook",
        "notebook": src_dir / "01_Conversao_Parquet" / "01_01_convertendo_em_parquet_v3.ipynb",
        "desc": "Conversão e sanitização individual de planilhas B3 (.xlsx -> .parquet & .csv)",
    },
    {
        "name": "02_Consolidacao_Dados",
        "type": "notebook",
        "notebook": src_dir / "02_Consolidacao_Dados" / "02_01_consolidando_dados.ipynb",
        "desc": "Consolidação dos dados em painel unificado MultiIndex",
    },
    {
        # ── Etapa 3 unificada: 03a → Classificador (com path corrigido) → 03c ──
        "name": "03_Filtro_Liquidez_e_Integridade",
        "type": "script",
        "script": src_dir / "run_etapa03.py",
        "args": ["--skip-cache"],  # força re-execução em modo "force"
        "desc": (
            "Sequência em 3 passagens: "
            "(1) filtros presença/IPO/ADTV → universo_pos_liquidez.csv; "
            "(2) Classificador de Integridade COTAHIST → tickers_excluidos_integridade.csv; "
            "(3) aplicação das exclusões → Matriz_precos_sanitizada.csv"
        ),
    },
    {
        "name": "04_Taxas_Livres_Risco",
        "type": "notebook",
        "notebook": src_dir / "04_Taxas_Livres_Risco" / "04_01_Taxas_Livres_Risco_SGS_Final.ipynb",
        "desc": "Ingestão e alinhamento de taxas livres de risco (CDI e SELIC via SGS/BCB)",
    },
    {
        "name": "05_01_Alinhamento_Retornos",
        "type": "notebook",
        "notebook": src_dir / "05_Alinhamento_Winsorizacao" / "05_01_Alinhamento_e_Retornos.ipynb",
        "desc": "Alinhamento de datas das ações com IBOV/CDI/Selic e cálculo de retornos",
    },
    {
        "name": "05_02_Saneamento_Winsorizacao",
        "type": "notebook",
        "notebook": src_dir / "05_Alinhamento_Winsorizacao" / "05_02_Saneamento_e_Winsorizacao.ipynb",
        "desc": "Saneamento estatístico de retornos e winsorização robusta de outliers",
    },
    {
        "name": "06_Estimacao_Covariancia",
        "type": "notebook",
        "notebook": src_dir / "06_Estimacao_Covariancia" / "06_01_Estimacao_LedoitWolf.ipynb",
        "desc": "Estimação de momentos estatísticos e covariância regularizada por Ledoit-Wolf",
    },
    {
        "name": "07_Otimizacao_Carteiras",
        "type": "notebook",
        "notebook": src_dir / "07_Otimizacao_Carteiras" / "07_01_Otimizacao_Carteiras.ipynb",
        "desc": "Backtest das carteiras MPT/PMPT (janela expansiva, rebalanceamento mensal)",
    },
    {
        "name": "08_Fronteira_Eficiente",
        "type": "notebook",
        "notebook": src_dir / "08_Fronteira_Eficiente" / "08_01_Fronteira_Eficiente.ipynb",
        "desc": "Simulação Monte Carlo e traçado das fronteiras eficientes MPT e PMPT",
    },
    {
        "name": "09_Inferencia_Econometrica",
        "type": "notebook",
        "notebook": src_dir / "09_Inferencia_Econometrica" / "09_01_Inferencia_Econometrica.ipynb",
        "desc": "Testes de Sharpe/CAPM/Spanning via Bootstrap e erros HAC",
    },
]


def run_notebook(nb_path: Path) -> bool:
    """Executa um notebook Jupyter in-place via nbconvert."""
    cmd = [
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute",
        "--inplace",
        "--ExecutePreprocessor.timeout=7200",
        str(nb_path),
    ]
    try:
        result = subprocess.run(
            cmd,
            cwd=str(nb_path.parent),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        if result.returncode != 0:
            print(f"\n[-] Erro ao executar {nb_path.name}:")
            print(result.stderr[-3000:])  # últimas 3000 chars
            return False
        return True
    except Exception as e:
        print(f"\n[-] Falha crítica de execução: {e}")
        return False


def run_script(script_path: Path, extra_args: list) -> bool:
    """Executa um script Python diretamente."""
    cmd = [sys.executable, str(script_path)] + extra_args
    try:
        result = subprocess.run(
            cmd,
            cwd=str(script_path.parent),
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        return result.returncode == 0
    except Exception as e:
        print(f"\n[-] Falha crítica ao executar {script_path.name}: {e}")
        return False


def main():
    print("=" * 75)
    print("        INICIANDO ORQUESTRADOR DO PIPELINE (EXECUÇÃO FORÇADA)          ")
    print("=" * 75)
    print(f"Diretório raiz do projeto: {project_root.resolve()}")
    print(f"Total de etapas configuradas: {len(pipeline_stages)}")
    print("[!] Modo: FORÇA TOTAL — todos os estágios serão executados.\n")

    start_pipeline = time.perf_counter()

    for idx, stage in enumerate(pipeline_stages, 1):
        stage_name = stage["name"]
        stage_type = stage.get("type", "notebook")

        print(f"[{idx}/{len(pipeline_stages)}] Etapa: {stage_name}")
        print(f"    Descrição: {stage['desc']}")

        # ── Verifica existência do artefato ───────────────────────────────────
        if stage_type == "notebook":
            artifact = stage["notebook"]
            label = artifact.relative_to(project_root)
        else:
            artifact = stage["script"]
            label = artifact.relative_to(project_root)

        print(f"    Arquivo:   {label}")

        if not artifact.exists():
            print(f"    [-] ERRO: Arquivo não encontrado: {artifact}")
            print("Execução interrompida.")
            sys.exit(1)

        print("    [RUN] Iniciando execução forçada...")
        start_stage = time.perf_counter()

        # ── Executa ───────────────────────────────────────────────────────────
        if stage_type == "notebook":
            success = run_notebook(stage["notebook"])
        else:
            success = run_script(stage["script"], stage.get("args", []))

        elapsed = time.perf_counter() - start_stage

        if success:
            print(f"    [OK] Concluído com sucesso em {elapsed:.1f}s.\n")
        else:
            print("=" * 75)
            print(f"[-] FALHA NA ETAPA: {stage_name}. O pipeline foi interrompido.")
            print("=" * 75)
            sys.exit(1)

    total_time = time.perf_counter() - start_pipeline

    print("=" * 75)
    print("                 PIPELINE EXECUTADO COM SUCESSO!                 ")
    print(f"                 Tempo total gasto: {total_time:.1f}s")
    print("=" * 75)

    # Suíte de testes ao final
    test_script = src_dir / "test_pipeline.py"
    if test_script.exists():
        print("\nIniciando suíte de testes de integridade (test_pipeline.py)...")
        res = subprocess.run([sys.executable, str(test_script)], cwd=str(src_dir))
        if res.returncode == 0:
            print("\n[OK] Todos os testes de integridade foram aprovados!")
        else:
            print("\n[-] A suíte de testes de integridade falhou.")
            sys.exit(1)
    else:
        print("\n[!] Aviso: test_pipeline.py não encontrado na pasta src.")


if __name__ == "__main__":
    main()
