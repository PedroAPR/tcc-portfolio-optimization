import os
import sys
import json
import argparse
import pandas as pd
from pathlib import Path

# Configura UTF-8 para evitar problemas de encoding no Windows console
sys.stdout.reconfigure(encoding='utf-8')

# Adiciona o raiz ao path para poder importar src.run_pipeline
auditoria_dir = Path(__file__).resolve().parent
project_root = auditoria_dir.parent.parent
sys.path.insert(0, str(project_root))

try:
    from src.run_pipeline import pipeline_stages, run_notebook
except ImportError as e:
    print(f"[-] Erro ao importar run_pipeline: {e}")
    sys.exit(1)

# Definições do grafo de dependência
DEPENDENCY_GRAPH = {
    "01_Conversao_Parquet": [
        "01_Conversao_Parquet", "02_Consolidacao_Dados", "03_Filtro_Liquidez",
        "05_01_Alinhamento_Retornos", "05_02_Saneamento_Winsorizacao",
        "06_Estimacao_Covariancia", "07_Otimizacao_Carteiras", "08_Fronteira_Eficiente", "09_Inferencia_Econometrica"
    ],
    "02_Consolidacao_Dados": [
        "02_Consolidacao_Dados", "03_Filtro_Liquidez",
        "05_01_Alinhamento_Retornos", "05_02_Saneamento_Winsorizacao",
        "06_Estimacao_Covariancia", "07_Otimizacao_Carteiras", "08_Fronteira_Eficiente", "09_Inferencia_Econometrica"
    ],
    "03_Filtro_Liquidez": [
        "03_Filtro_Liquidez", "05_01_Alinhamento_Retornos", "05_02_Saneamento_Winsorizacao",
        "06_Estimacao_Covariancia", "07_Otimizacao_Carteiras", "08_Fronteira_Eficiente", "09_Inferencia_Econometrica"
    ],
    "04_Taxas_Livres_Risco": [
        "04_Taxas_Livres_Risco", "05_01_Alinhamento_Retornos", "05_02_Saneamento_Winsorizacao",
        "06_Estimacao_Covariancia", "07_Otimizacao_Carteiras", "08_Fronteira_Eficiente", "09_Inferencia_Econometrica"
    ],
    "05_01_Alinhamento_Retornos": [
        "05_01_Alinhamento_Retornos", "05_02_Saneamento_Winsorizacao",
        "06_Estimacao_Covariancia", "07_Otimizacao_Carteiras", "08_Fronteira_Eficiente", "09_Inferencia_Econometrica"
    ],
    "05_02_Saneamento_Winsorizacao": [
        "05_02_Saneamento_Winsorizacao", "06_Estimacao_Covariancia",
        "07_Otimizacao_Carteiras", "08_Fronteira_Eficiente", "09_Inferencia_Econometrica"
    ],
    "06_Estimacao_Covariancia": [
        "06_Estimacao_Covariancia", "07_Otimizacao_Carteiras", "09_Inferencia_Econometrica"
    ],
    "07_Otimizacao_Carteiras": [
        "07_Otimizacao_Carteiras", "09_Inferencia_Econometrica"
    ],
    "08_Fronteira_Eficiente": [
        "08_Fronteira_Eficiente"
    ],
    "09_Inferencia_Econometrica": [
        "09_Inferencia_Econometrica"
    ]
}

FILE_TO_STAGE_MAP = {
    # Notebooks
    "01_01_convertendo_em_parquet_v3.ipynb": "01_Conversao_Parquet",
    "02_01_consolidando_dados.ipynb": "02_Consolidacao_Dados",
    "03_01_Ingestao_Filtro_Liquidez_v3.ipynb": "03_Filtro_Liquidez",
    "04_01_Taxas_Livres_Risco_SGS_Final.ipynb": "04_Taxas_Livres_Risco",
    "05_01_Alinhamento_e_Retornos.ipynb": "05_01_Alinhamento_Retornos",
    "05_02_Saneamento_e_Winsorizacao.ipynb": "05_02_Saneamento_Winsorizacao",
    "06_01_Estimacao_LedoitWolf.ipynb": "06_Estimacao_Covariancia",
    "07_01_Otimizacao_Carteiras.ipynb": "07_Otimizacao_Carteiras",
    "08_01_Fronteira_Eficiente.ipynb": "08_Fronteira_Eficiente",
    "09_01_Inferencia_Econometrica.ipynb": "09_Inferencia_Econometrica",
    # Utils
    "worker.py": "01_Conversao_Parquet",
    "run_etapa03.py": "03_Filtro_Liquidez",
    "alinhamento.py": "05_01_Alinhamento_Retornos",
    "conversoes.py": "05_01_Alinhamento_Retornos",
    "config_loader.py": "05_01_Alinhamento_Retornos",  # assume baseline
    "winsorizacao.py": "05_02_Saneamento_Winsorizacao",
    "covariancia.py": "06_Estimacao_Covariancia",
    "otimizacao.py": "07_Otimizacao_Carteiras",
    "fronteira.py": "08_Fronteira_Eficiente",
    "inferencia.py": "09_Inferencia_Econometrica"
}

def detect_changed_stages():
    """Detecta quais arquivos foram alterados usando git status e retorna as etapas afetadas."""
    import subprocess
    cmd = ["git", "status", "--porcelain"]
    res = subprocess.run(cmd, cwd=str(project_root), capture_output=True, text=True)
    if res.returncode != 0:
        return []
    
    changed_stages = set()
    for line in res.stdout.splitlines():
        # ex: " M src/07_Otimizacao_Carteiras/utils/otimizacao.py"
        file_path = line[3:].strip()
        filename = Path(file_path).name
        if filename in FILE_TO_STAGE_MAP:
            changed_stages.add(FILE_TO_STAGE_MAP[filename])
            
    return list(changed_stages)

def is_close(val1, val2, rtol=1e-5, atol=1e-8):
    if val1 is None and val2 is None:
        return True
    if val1 is None or val2 is None:
        return False
    diff = abs(val1 - val2)
    if diff <= atol:
        return True
    denom = max(abs(val1), abs(val2))
    return (diff / denom) <= rtol

def validate_golden_master():
    """Compara saídas atuais com o golden_master.json."""
    golden_path = auditoria_dir / "golden_master.json"
    if not golden_path.exists():
        print(f"[-] Erro: golden_master.json não encontrado em {golden_path}")
        return False
        
    with open(golden_path, "r", encoding="utf-8") as f:
        gold = json.load(f)
        
    data_dir = project_root / "data"
    estrategias_dir = data_dir / "Estrategias"
    perf_csv_path = estrategias_dir / "desempenho_estrategias.csv"
    
    if not perf_csv_path.exists():
        print(f"[-] Erro: desempenho_estrategias.csv não encontrado!")
        return False
        
    df_perf = pd.read_csv(perf_csv_path, index_col=0)
    
    passed = True
    print("\n" + "="*60)
    print("           RESULTADO DA VALIDAÇÃO (VS GOLDEN MASTER)           ")
    print("="*60)
    
    # 1. Comparar estratégias e métricas
    print("\n[Métricas Financeiras]")
    for strategy, metrics in gold["strategies"].items():
        if strategy not in df_perf.index:
            print(f"  [-] Estratégia '{strategy}' ausente no novo output! [FAIL]")
            passed = False
            continue
            
        row = df_perf.loc[strategy]
        metrics_mapping = {
            "CAGR": "ret_anual",
            "Vol": "vol_anual",
            "Sharpe": "sharpe",
            "Sortino": "sortino",
            "MaxDD": "max_drawdown",
            "Turnover": "turnover_aa"
        }
        
        failed_metrics = []
        for gold_name, csv_name in metrics_mapping.items():
            gold_val = metrics[gold_name]
            new_val = row.get(csv_name)
            if pd.isna(new_val):
                new_val = None
            else:
                new_val = float(new_val)
                
            if not is_close(gold_val, new_val):
                failed_metrics.append((gold_name, gold_val, new_val))
                
        if failed_metrics:
            passed = False
            print(f"  [-] {strategy:20}: FALHOU nas seguintes métricas:")
            for m, g_v, n_v in failed_metrics:
                print(f"      * {m}: Golden={g_v:.6f} vs Novo={n_v:.6f} (diff={abs(g_v - n_v if g_v is not None and n_v is not None else 999):.2e})")
        else:
            print(f"  [+] {strategy:20}: PASS [OK]")
            
    # 2. Comparar shapes
    print("\n[Dimensões de Arquivos (Shapes)]")
    files_to_shape = {
        "Matriz_precos_sanitizada": data_dir / "Matriz_Precos" / "Matriz_precos_sanitizada.csv",
        "painel_alinhado": data_dir / "Painel_Dados" / "painel_alinhado.csv",
        "retornos_simples_saneado": data_dir / "Retornos" / "retornos_simples_saneado.parquet",
        "retornos_log_saneado": data_dir / "Retornos" / "retornos_log_saneado.parquet",
        "sigma_amostral_anual": data_dir / "Momentos" / "sigma_amostral_anual.parquet",
        "sigma_ledoitwolf_anual": data_dir / "Momentos" / "sigma_ledoitwolf_anual.parquet",
        "strategy_returns": estrategias_dir / "strategy_returns.parquet",
        "pesos_historico": estrategias_dir / "pesos_historico.csv"
    }
    
    for name, expected_shape in gold["shapes"].items():
        path = files_to_shape[name]
        if not path.exists():
            print(f"  [-] Arquivo '{name}' não existe! [FAIL]")
            passed = False
            continue
            
        if str(path).endswith(".parquet"):
            df = pd.read_parquet(path)
        else:
            df = pd.read_csv(path)
            
        new_shape = list(df.shape)
        if new_shape != expected_shape:
            print(f"  [-] Shape de '{name}': Esperado {expected_shape} vs Novo {new_shape} [FAIL]")
            passed = False
        else:
            print(f"  [+] Shape de '{name}': {new_shape} [OK]")
            
    print("="*60)
    if passed:
        print("RESULTADO GERAL: PASS (Tudo em conformidade com o Golden Master!)")
        print("="*60)
        return True
    else:
        print("RESULTADO GERAL: FAIL (Divergências numéricas detectadas!)")
        print("="*60)
        return False

def main():
    parser = argparse.ArgumentParser(description="Script de Re-validação Numérica de Regressões do TCC.")
    parser.add_argument("file", nargs="?", help="Nome do arquivo modificado (ex: otimizacao.py)")
    parser.add_argument("--all", action="store_true", help="Força a re-execução de todo o pipeline")
    parser.add_argument("--check-only", action="store_true", help="Apenas compara os outputs atuais contra o Golden Master sem rodar nada")
    
    args = parser.parse_args()
    
    if args.check_only:
        success = validate_golden_master()
        sys.exit(0 if success else 1)
        
    stages_to_run = set()
    
    if args.all:
        print("[*] Forçando re-execução de todas as etapas do pipeline...")
        stages_to_run = set(DEPENDENCY_GRAPH.keys())
    elif args.file:
        filename = Path(args.file).name
        if filename in FILE_TO_STAGE_MAP:
            start_stage = FILE_TO_STAGE_MAP[filename]
            stages_to_run = set(DEPENDENCY_GRAPH[start_stage])
            print(f"[*] Arquivo '{filename}' mapeado para a etapa inicial '{start_stage}'.")
            print(f"[*] Etapas afetadas a jusante: {sorted(list(stages_to_run))}")
        else:
            print(f"[-] Erro: Arquivo '{filename}' não mapeado em FILE_TO_STAGE_MAP.")
            print("Opções de arquivos válidos:")
            for k in sorted(FILE_TO_STAGE_MAP.keys()):
                print(f"  * {k}")
            sys.exit(1)
    else:
        # Tenta detectar via git
        detected = detect_changed_stages()
        if detected:
            print(f"[*] Arquivos modificados detectados via Git:")
            stages_to_run = set()
            for s in detected:
                print(f"  * Etapa afetada: {s}")
                stages_to_run.update(DEPENDENCY_GRAPH[s])
            print(f"[*] Grafo unificado de etapas a jusante a rodar: {sorted(list(stages_to_run))}")
        else:
            print("[*] Nenhum arquivo alterado detectado via git e nenhum argumento passado.")
            print("[*] Apenas validando os outputs atuais contra o Golden Master...")
            success = validate_golden_master()
            sys.exit(0 if success else 1)
            
    # Orquestrar execução ordenada das etapas selecionadas
    # Importante: precisamos executar na ordem cronológica do pipeline
    stages_run_count = 0
    for stage in pipeline_stages:
        stage_name = stage["name"]
        if stage_name in stages_to_run:
            nb_path = stage["notebook"]
            print(f"\n[EXEC] Executando Etapa: {stage_name} ({nb_path.name})...")
            success = run_notebook(nb_path)
            if not success:
                print(f"[-] Erro ao executar a etapa {stage_name}. Abortando.")
                sys.exit(1)
            stages_run_count += 1
            
    print(f"\n[*] {stages_run_count} etapas do pipeline foram re-executadas.")
    
    # Compara saídas com o Golden Master
    success = validate_golden_master()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
