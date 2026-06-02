import os
import sys
import time
import json
import hashlib
import subprocess
from pathlib import Path

# Configura a saída padrão para UTF-8 para evitar problemas de codificação no Windows
sys.stdout.reconfigure(encoding='utf-8')

# Caminhos do projeto
src_dir = Path(__file__).resolve().parent
project_root = src_dir.parent

# Ordem cronológica dos scripts do pipeline com dependências e sentinelas
pipeline_stages = [
    {
        "name": "01_Conversao_Parquet",
        "notebook": src_dir / "01_Conversao_Parquet" / "01_01_convertendo_em_parquet_v3.ipynb",
        "desc": "Conversão e sanitização individual de planilhas B3 (.xlsx -> .parquet & .csv)",
        "dependencies": [src_dir / "01_Conversao_Parquet" / "worker.py"],
        "sentinels": [project_root / "data" / "dados_economatica_tratados"]
    },
    {
        "name": "02_Consolidacao_Dados",
        "notebook": src_dir / "02_Consolidacao_Dados" / "02_01_consolidando_dados.ipynb",
        "desc": "Consolidação dos dados em painel unificado MultiIndex",
        "dependencies": [],
        "sentinels": [project_root / "data" / "dados_economatica_consolidados" / "dados_brutos_economatica.parquet"]
    },
    {
        "name": "03_Filtro_Liquidez",
        "notebook": src_dir / "03_Filtro_Liquidez" / "03_01_Ingestao_Filtro_Liquidez_v3.ipynb",
        "desc": "Ingestão estruturada da matriz de preços e aplicação do funil de liquidez",
        "dependencies": [],
        "sentinels": [project_root / "data" / "Matriz_Precos" / "Matriz_precos_sanitizada.csv"]
    },
    {
        "name": "04_Taxas_Livres_Risco",
        "notebook": src_dir / "04_Taxas_Livres_Risco" / "04_01_Taxas_Livres_Risco_SGS_Final.ipynb",
        "desc": "Ingestão e alinhamento de taxas livres de risco (CDI e SELIC via SGS/BCB)",
        "dependencies": [],
        "sentinels": [
            project_root / "data" / "CDI" / "cdi_diario_bcb_2010_atual.csv",
            project_root / "data" / "Selic" / "selic_diario_bcb_2010_atual.csv"
        ]
    },

    {
        "name": "05_01_Alinhamento_Retornos",
        "notebook": src_dir / "05_Alinhamento_Winsorizacao" / "05_01_Alinhamento_e_Retornos.ipynb",
        "desc": "Alinhamento de datas das ações com IBOV/CDI/Selic e cálculo de retornos",
        "dependencies": [
            src_dir / "05_Alinhamento_Winsorizacao" / "utils" / "alinhamento.py",
            src_dir / "05_Alinhamento_Winsorizacao" / "utils" / "conversoes.py",
            src_dir / "05_Alinhamento_Winsorizacao" / "utils" / "config_loader.py"
        ],
        "sentinels": [
            project_root / "data" / "Retornos" / "retornos_simples.parquet",
            project_root / "data" / "Retornos" / "rf_diario.parquet"
        ]
    },
    {
        "name": "05_02_Saneamento_Winsorizacao",
        "notebook": src_dir / "05_Alinhamento_Winsorizacao" / "05_02_Saneamento_e_Winsorizacao.ipynb",
        "desc": "Saneamento estatístico de retornos e winsorização robusta de outliers",
        "dependencies": [
            src_dir / "05_Alinhamento_Winsorizacao" / "utils" / "winsorizacao.py",
            src_dir / "05_Alinhamento_Winsorizacao" / "utils" / "config_loader.py"
        ],
        "sentinels": [project_root / "data" / "Retornos" / "retornos_simples_saneado.parquet"]
    },
    {
        "name": "06_Estimacao_Covariancia",
        "notebook": src_dir / "06_Estimacao_Covariancia" / "06_01_Estimacao_LedoitWolf.ipynb",
        "desc": "Estimação de momentos estatísticos e covariância regularizada por Ledoit-Wolf",
        "dependencies": [
            src_dir / "06_Estimacao_Covariancia" / "utils" / "covariancia.py",
            src_dir / "06_Estimacao_Covariancia" / "utils" / "config_loader.py"
        ],
        "sentinels": [project_root / "data" / "Momentos" / "sigma_ledoitwolf_anual.parquet"]
    },
    {
        "name": "07_Otimizacao_Carteiras",
        "notebook": src_dir / "07_Otimizacao_Carteiras" / "07_01_Otimizacao_Carteiras.ipynb",
        "desc": "Estimação de momentos estatísticos e backtest das carteiras MPT/PMPT",
        "dependencies": [
            src_dir / "07_Otimizacao_Carteiras" / "utils" / "otimizacao.py",
            src_dir / "07_Otimizacao_Carteiras" / "utils" / "config_loader.py"
        ],
        "sentinels": [project_root / "data" / "Estrategias" / "strategy_returns.parquet"]
    },
    {
        "name": "08_Fronteira_Eficiente",
        "notebook": src_dir / "08_Fronteira_Eficiente" / "08_01_Fronteira_Eficiente.ipynb",
        "desc": "Simulação Monte Carlo e traçado das fronteiras eficientes MPT (média-variância) e PMPT (média-CVaR)",
        "dependencies": [
            src_dir / "08_Fronteira_Eficiente" / "utils" / "fronteira.py",
            src_dir / "08_Fronteira_Eficiente" / "utils" / "config_loader.py"
        ],
        "sentinels": [
            project_root / "data" / "Estrategias" / "fronteira_mv_pontos.csv",
            project_root / "data" / "Estrategias" / "carteiras_canonicas.csv",
            project_root / "data" / "Estrategias" / "fronteira_eficiente.png"
        ]
    },
    {
        "name": "09_Inferencia_Econometrica",
        "notebook": src_dir / "09_Inferencia_Econometrica" / "09_01_Inferencia_Econometrica.ipynb",
        "desc": "Caracterização econométrica do benchmark (IBOVESPA) e inferência comparada de Sharpe/CAPM/Spanning via Bootstrap e erros HAC",
        "dependencies": [
            src_dir / "09_Inferencia_Econometrica" / "utils" / "inferencia.py",
            src_dir / "09_Inferencia_Econometrica" / "utils" / "config_loader.py"
        ],
        "sentinels": [
            project_root / "data" / "Estrategias" / "apendice_G_diagnostico_ibov.csv",
            project_root / "data" / "Estrategias" / "apendice_H_testes_estrategia.csv",
            project_root / "data" / "Estrategias" / "apendice_H_painel_metricas.csv",
            project_root / "data" / "Estrategias" / "apendice_H_comparativo_rf.csv"
        ]
    }
]


def calculate_file_md5(file_path: Path) -> str:
    """Calcula o hash MD5 clássico de um arquivo físico."""
    hasher = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return ""

def calculate_nb_source_hash(nb_path: Path) -> str:
    """Calcula o hash MD5 do notebook ignorando metadados de execução, outputs e
    números de células, focando exclusivamente no conteúdo textual/código.
    """
    hasher = hashlib.md5()
    try:
        with open(nb_path, "r", encoding="utf-8") as f:
            nb = json.load(f)
        for cell in nb.get("cells", []):
            hasher.update(cell.get("cell_type", "").encode("utf-8"))
            source_content = "".join(cell.get("source", []))
            hasher.update(source_content.encode("utf-8"))
        return hasher.hexdigest()
    except Exception:
        # Fallback de segurança se o arquivo não estiver em formato JSON válido
        return calculate_file_md5(nb_path)

def get_stage_hash(nb_path: Path, dependencies: list[Path]) -> str:
    """Calcula um hash único combinando o notebook (somente código) e suas dependências."""
    hasher = hashlib.md5()
    hasher.update(calculate_nb_source_hash(nb_path).encode("utf-8"))
    for dep in sorted(dependencies):
        if dep.exists():
            hasher.update(calculate_file_md5(dep).encode("utf-8"))
    return hasher.hexdigest()

def check_sentinels(sentinels: list[Path]) -> bool:
    """Valida a presença física de todos os arquivos ou pastas sentinela de saída."""
    for s in sentinels:
        if not s.exists():
            return False
        if s.is_dir():
            try:
                # Se for diretório, precisa existir e não estar vazio
                if not any(s.iterdir()):
                    return False
            except Exception:
                return False
    return True

def run_notebook(nb_path: Path) -> bool:
    """Executa um notebook Jupyter in-place utilizando nbconvert."""
    cmd = [
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute",
        "--inplace",
        str(nb_path)
    ]
    try:
        # Executa no diretório onde o notebook reside para garantir caminhos relativos corretos
        result = subprocess.run(
            cmd,
            cwd=str(nb_path.parent),
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        if result.returncode != 0:
            print(f"\n[-] Erro ao executar o notebook {nb_path.name}:")
            print(result.stderr)
            return False
        return True
    except Exception as e:
        print(f"\n[-] Falha crítica de execução: {e}")
        return False

def main():
    print("=" * 75)
    print("      INICIANDO ORQUESTRADOR DO PIPELINE COM CACHE INTELIGENTE MD5      ")
    print("=" * 75)
    print(f"Diretório raiz do projeto: {project_root.resolve()}")
    print(f"Total de etapas configuradas: {len(pipeline_stages)}\n")

    # Carrega cache de execuções passadas
    cache_path = src_dir / ".pipeline_cache.json"
    cache = {}
    if cache_path.exists():
        try:
            with open(cache_path, "r", encoding="utf-8") as f:
                cache = json.load(f)
        except Exception as e:
            print(f"[!] Erro ao ler cache. Ignorando e forçando execução: {e}")

    start_pipeline = time.perf_counter()

    for idx, stage in enumerate(pipeline_stages, 1):
        nb_path = stage["notebook"]
        stage_name = stage["name"]
        print(f"[{idx}/{len(pipeline_stages)}] Etapa: {stage_name}")
        print(f"    Descrição: {stage['desc']}")
        print(f"    Arquivo:   {nb_path.relative_to(project_root)}")

        if not nb_path.exists():
            print(f"    [-] ERRO: Arquivo do notebook não encontrado!")
            print("Execução interrompida.")
            sys.exit(1)

        # Calcula o hash MD5 atualizado do código (excluindo outputs nbconvert)
        current_hash = get_stage_hash(nb_path, stage["dependencies"])
        
        # Verifica se o código não mudou E se os dados físicos de saída existem
        cached_hash = cache.get(stage_name)
        sentinels_ok = check_sentinels(stage["sentinels"])

        if cached_hash == current_hash and sentinels_ok:
            print(f"    [SKIP] Sem alterações no código e arquivos de saída existentes. Pulando etapa.\n")
            continue

        # Determina a causa da execução
        if not sentinels_ok:
            reason = "arquivos sentinela ausentes/incompletos"
        else:
            reason = "código fonte alterado"
            
        print(f"    [RUN] Iniciando execução ({reason})...")

        start_stage = time.perf_counter()
        success = run_notebook(nb_path)
        end_stage = time.perf_counter()

        elapsed = end_stage - start_stage

        if success:
            print(f"    [OK] Concluído com sucesso em {elapsed:.2f} segundos.")
            
            # Recalcula o hash pós-execução baseando-se apenas nas fontes
            # (garante consistência mesmo com o salvamento nbconvert in-place)
            post_run_hash = get_stage_hash(nb_path, stage["dependencies"])
            cache[stage_name] = post_run_hash
            try:
                with open(cache_path, "w", encoding="utf-8") as f:
                    json.dump(cache, f, indent=1)
                print(f"    [CACHE] Hash gravado com sucesso.\n")
            except Exception as e:
                print(f"    [!] Erro ao salvar cache: {e}\n")
        else:
            print("=" * 75)
            print(f"[-] FALHA NA ETAPA: {stage_name}. O pipeline foi interrompido.")
            print("=" * 75)
            sys.exit(1)

    end_pipeline = time.perf_counter()
    total_time = end_pipeline - start_pipeline

    print("=" * 75)
    print("                 PIPELINE EXECUTADO COM SUCESSO!                 ")
    print(f"                 Tempo total gasto: {total_time:.2f} segundos.")
    print("=" * 75)

    # Executa a suíte de testes automáticos ao final
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
