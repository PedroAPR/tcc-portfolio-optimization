import json
import os
import subprocess
import sys
from pathlib import Path
import pandas as pd
import numpy as np

src_dir = Path(__file__).resolve().parent
project_root = src_dir.parent
data_dir = project_root / "data"

stages = {
    "03_Filtro_Liquidez": src_dir / "03_Filtro_Liquidez",
    "04_Taxas_Livres_Risco": src_dir / "04_Taxas_Livres_Risco",
    "05_Alinhamento_Winsorizacao": src_dir / "05_Alinhamento_Winsorizacao",
    "06_Estimacao_Covariancia": src_dir / "06_Estimacao_Covariancia",
    "07_Otimizacao_Carteiras": src_dir / "07_Otimizacao_Carteiras",
    "08_Fronteira_Eficiente": src_dir / "08_Fronteira_Eficiente",
    "09_Inferencia_Econometrica": src_dir / "09_Inferencia_Econometrica",
}


print("="*60)
# RE-CONVERÇÃO DE ENCODING PARA SAÍDA WINDOWS SEGURO
sys.stdout.reconfigure(encoding='utf-8')
print("INICIANDO SUÍTE DE TESTES DO PIPELINE TRATAMENTO DE DADOS")
print("="*60)

# --- CASO DE TESTE 1: Validação Estática de Importações nos Notebooks ---
def test_static_imports():
    print("\n[TEST 1] Validando estaticamente importações de utils nos notebooks...")
    mismatch = False
    
    for stage_name, stage_path in stages.items():
        notebooks = list(stage_path.glob("*.ipynb"))
        for nb_path in notebooks:
            with open(nb_path, "r", encoding="utf-8") as f:
                nb = json.load(f)
            
            for cell in nb.get("cells", []):
                if cell.get("cell_type") != "code":
                    continue
                source = "".join(cell.get("source", []))
                
                # Procura por linhas que importam de utils
                for line in source.split("\n"):
                    line = line.strip()
                    if ("from utils." in line or "import utils." in line) and not line.startswith("#"):
                        # Verifica se o arquivo utils importado realmente existe na pasta local daquela etapa
                        parts = line.split()
                        try:
                            # ex: "from utils.config_loader import carregar_parametros"
                            idx = parts.index("from") if "from" in parts else -1
                            if idx != -1:
                                import_source = parts[idx + 1] # "utils.config_loader"
                                if import_source.startswith("utils."):
                                    module_name = import_source.split(".")[1] # "config_loader"
                                    # Verifica se module_name.py existe em <etapa>/utils/
                                    target_file = stage_path / "utils" / f"{module_name}.py"
                                    if not target_file.exists():
                                        print(f"  [-] Erro: Notebook '{nb_path.name}' tenta importar '{import_source}', mas '{target_file.name}' não existe.")
                                        mismatch = True
                        except ValueError:
                            pass
                            
    if mismatch:
        raise AssertionError("Falha no Teste 1: Notebooks contêm importações inválidas para a estrutura física local.")
    else:
        print("[OK] Teste 1: Todas as importações de utils nos notebooks são válidas e locais.")

# --- CASO DE TESTE 2: Resolução do Config Centralizado ---
def test_config_resolution():
    print("\n[TEST 2] Validando resolução dinâmica de src/config.json a partir de cada subpasta...")
    
    # 1. Modifica temporariamente uma chave de teste no config.json central
    config_path = src_dir / "config.json"
    with open(config_path, "r", encoding="utf-8") as f:
        config_data = json.load(f)
        
    original_val = config_data.get("K_MAD", 3.5)
    test_val = 999.0
    config_data["K_MAD"] = test_val
    
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config_data, f, indent=1)
        
    try:
        # 2. Chama subprocessos em cada etapa funcional para ver se o config carregado é o correto
        for stage_name, stage_path in stages.items():
            cmd = ["python", "-c", "from utils.config_loader import carregar_parametros; print(carregar_parametros()['K_MAD'])"]
            res = subprocess.run(cmd, cwd=str(stage_path), capture_output=True, text=True)
            if res.returncode != 0:
                raise AssertionError(f"Erro ao executar config_loader em {stage_name}: {res.stderr}")
            val = float(res.stdout.strip())
            if val != test_val:
                raise AssertionError(f"config_loader em {stage_name} não leu o config.json central! Valor lido: {val}")
            print(f"  [OK] Etapa '{stage_name}' resolveu o config central com sucesso.")
    finally:
        # Restaura o config.json
        config_data["K_MAD"] = original_val
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config_data, f, indent=1)
            
    print("[OK] Teste 2: Resolução dinâmica de src/config.json funciona perfeitamente.")

# --- CASO DE TESTE 3: Consistência de Dados e Validação de Contratos ---
def test_data_consistency():
    print("\n[TEST 3] Validando contratos e consistência dimensional dos arquivos de dados...")
    
    # 1. Tickers de ações
    tickers_path = data_dir / "Tickers" / "tickers_finais.csv"
    if not tickers_path.exists():
        raise FileNotFoundError("tickers_finais.csv não gerado.")
    tickers = pd.read_csv(tickers_path)["ticker"].tolist()
    
    # 2. Matriz de preços sanitizada
    precos_path = data_dir / "Matriz_Precos" / "Matriz_precos_sanitizada.csv"
    if not precos_path.exists():
        raise FileNotFoundError("Matriz_precos_sanitizada.csv não gerada.")
    df_precos = pd.read_csv(precos_path, index_col=0)
    
    # Asserção: todos os tickers finais devem estar nas colunas de preços sanitizados
    for t in tickers:
        if t not in df_precos.columns:
            raise AssertionError(f"Ticker '{t}' está na lista final mas ausente de Matriz_precos_sanitizada.csv!")
            
    # 3. Painel alinhado
    painel_path = data_dir / "Painel_Dados" / "painel_alinhado.csv"
    if not painel_path.exists():
        raise FileNotFoundError("painel_alinhado.csv não gerado.")
    df_painel = pd.read_csv(painel_path, index_col=0)
    
    # Asserção: colunas mínimas do painel
    cols_minimas = ["IBOV_close", "CDI_diario", "SELIC_diario"]
    for c in cols_minimas:
        if c not in df_painel.columns:
            raise AssertionError(f"Coluna obrigatória '{c}' ausente de painel_alinhado.csv!")
            
    # Asserção: tickers no painel alinhado com prefixo ACAO_
    for t in tickers:
        col_acao = f"ACAO_{t}"
        if col_acao not in df_painel.columns:
            raise AssertionError(f"Ação '{col_acao}' ausente de painel_alinhado.csv!")
            
    print(f"  [OK] Contrato de dados validado: {len(tickers)} ativos investíveis alinhados em {len(df_painel)} datas.")
    print("[OK] Teste 3: Dimensões e estruturas de arquivos validadas.")

# --- CASO DE TESTE 4: Teste de Finitude e Relações Geométricas ---
def test_math_assertions():
    print("\n[TEST 4] Validando identidades matemáticas e ausência de NaNs/Infs nos retornos...")
    
    ret_simples_path = data_dir / "Retornos" / "retornos_simples_saneado.parquet"
    ret_log_path = data_dir / "Retornos" / "retornos_log_saneado.parquet"
    
    if not ret_simples_path.exists() or not ret_log_path.exists():
        raise FileNotFoundError("Matrizes de retorno saneadas ausentes.")
        
    df_simples = pd.read_parquet(ret_simples_path)
    df_log = pd.read_parquet(ret_log_path)
    
    # Asserção 1: Preservação de forma
    if df_simples.shape != df_log.shape:
        raise AssertionError("Matrizes de retorno simples e log possuem dimensões distintas!")
        
    # Asserção 2: Ausência de NaNs e Infinitos
    if df_simples.isna().sum().sum() > 0 or df_log.isna().sum().sum() > 0:
        raise AssertionError("Matrizes de retornos contêm valores NaNs remanescentes!")
    if not np.isfinite(df_simples.values).all() or not np.isfinite(df_log.values).all():
        raise AssertionError("Matrizes de retornos contêm valores infinitos (divisão por zero)!")
        
    # Asserção 3: Identidade geométrica: log == ln(1 + simples)
    if not np.allclose(df_log.values, np.log1p(df_simples.values), atol=1e-10):
        raise AssertionError("Identidade geométrica r_log = ln(1+R_simples) rompida nos retornos saneados!")
        
    # Asserção 4: Consistência do log de winsorização
    log_win_path = data_dir / "Retornos" / "log_winsorizacao.csv"
    if not log_win_path.exists():
        raise FileNotFoundError("log_winsorizacao.csv não gerado.")
    df_log_win = pd.read_csv(log_win_path, index_col=0)
    if df_log_win["n_winsor_v2"].sum() <= 0:
        raise AssertionError("Log de winsorização não registrou nenhum truncamento efetuado!")
        
    print(f"  [OK] Finitude e geometria validadas. Log-retornos com erro flutuante < 10^-10.")
    print("[OK] Teste 4: Asserções financeiras e geométricas validadas com sucesso.")

# --- CASO DE TESTE 5: Validação de Matrizes de Covariância (Ledoit-Wolf) ---
def test_covariance_regularization():
    print("\n[TEST 5] Validando estimadores de covariância e regularização (Ledoit-Wolf)...")
    
    # 1. Tickers de ações para validação dimensional
    tickers_path = data_dir / "Tickers" / "tickers_finais.csv"
    if not tickers_path.exists():
        raise FileNotFoundError("tickers_finais.csv não encontrado.")
    tickers = pd.read_csv(tickers_path)["ticker"].tolist()
    N = len(tickers)
    
    # 2. Insumos da Etapa 6
    momentos_path = data_dir / "Momentos" / "momentos_anuais.parquet"
    mu_path = data_dir / "Momentos" / "mu_anual.parquet"
    sigma_amostral_path = data_dir / "Momentos" / "sigma_amostral_anual.parquet"
    sigma_lw_path = data_dir / "Momentos" / "sigma_ledoitwolf_anual.parquet"
    correlacao_path = data_dir / "Momentos" / "correlacao.parquet"
    
    for p in [momentos_path, mu_path, sigma_amostral_path, sigma_lw_path, correlacao_path]:
        if not p.exists():
            raise FileNotFoundError(f"Arquivo obrigatório ausente da Etapa 6: {p.name}")
            
    df_momentos = pd.read_parquet(momentos_path)
    df_mu = pd.read_parquet(mu_path)
    df_sigma_amostral = pd.read_parquet(sigma_amostral_path)
    df_sigma_lw = pd.read_parquet(sigma_lw_path)
    df_corr = pd.read_parquet(correlacao_path)
    
    # Validação Dimensional (T3)
    if len(df_momentos) != N or len(df_mu) != N:
        raise AssertionError(f"Vetor mu ou momentos possui dimensão divergente do número de ativos ({N})!")
    if df_sigma_amostral.shape != (N, N) or df_sigma_lw.shape != (N, N) or df_corr.shape != (N, N):
        raise AssertionError(f"Matrizes de covariância/correlação possuem dimensões inválidas (deveria ser {N}x{N})!")
        
    # Validação de Simetria (T2)
    if not np.allclose(df_sigma_amostral.values, df_sigma_amostral.values.T, atol=1e-10):
        raise AssertionError("Matriz de covariância amostral não é perfeitamente simétrica!")
    if not np.allclose(df_sigma_lw.values, df_sigma_lw.values.T, atol=1e-10):
        raise AssertionError("Matriz de covariância regularizada (Ledoit-Wolf) não é perfeitamente simétrica!")
        
    # Validação de Posto, Invertibilidade e Autovalores Positivos (T1)
    ev_amostral = np.linalg.eigvalsh(df_sigma_amostral.values)
    ev_lw = np.linalg.eigvalsh(df_sigma_lw.values)
    
    if ev_lw.min() <= 1e-8:
        raise AssertionError(f"Erro T1: Menor autovalor de Σ_LW é {ev_lw.min():.2e} (limiar min: 10^-8). Possível singularidade!")
        
    # Validação de Conservação de Traço e Variância Total (T4)
    # Como o Ledoit-Wolf utiliza ddof=0 internamente para a covariância amostral base (S),
    # enquanto a covariância amostral clássica exportada (Sigma_amostral) utiliza ddof=1,
    # ajustamos o traço amostral pelo fator (T-1)/T para verificar a igualdade matemática exata.
    ret_simples_path = data_dir / "Retornos" / "retornos_simples_saneado.parquet"
    T = len(pd.read_parquet(ret_simples_path))
    
    trace_amostral_ddof0 = np.trace(df_sigma_amostral.values) * (T - 1) / T
    trace_lw = np.trace(df_sigma_lw.values)
    if not np.allclose(trace_amostral_ddof0, trace_lw, atol=1e-8):
        raise AssertionError(f"Erro T4: Conservação do traço violada! Amostral (ddof=0): {trace_amostral_ddof0:.6f} | LW: {trace_lw:.6f}")
        
    print(f"  [OK] Testes T1 (Estabilidade λ_min={ev_lw.min():.2e} > 1e-8) aprovado.")
    print(f"  [OK] Teste T2 (Simetria Perfeita) aprovado.")
    print(f"  [OK] Teste T3 (Geometria N={N} ativos) aprovado.")
    print(f"  [OK] Teste T4 (Conservação de Traço Tr(Σ)={trace_lw:.4f}) aprovado.")
    print("[OK] Teste 5: Todos os critérios estatísticos e dimensionais da covariância foram atendidos.")



# --- CASO DE TESTE 6: Validação do Backtest e Retornos out-of-sample ---
def test_backtest_outputs():
    print("\n[TEST 6] Validando arquivos de saída e consistência do backtest (Etapa 7)...")
    
    ret_path = data_dir / "Estrategias" / "strategy_returns.parquet"
    perf_path = data_dir / "Estrategias" / "desempenho_estrategias.parquet"
    pesos_path = data_dir / "Estrategias" / "pesos_historico.csv"
    
    for p in [ret_path, perf_path, pesos_path]:
        if not p.exists():
            raise FileNotFoundError(f"Arquivo obrigatório de saída ausente: {p.name}")
            
    df_ret = pd.read_parquet(ret_path)
    df_perf = pd.read_parquet(perf_path)
    df_pesos = pd.read_csv(pesos_path)
    
    # Validações estruturais e dimensionais
    if len(df_ret) == 0:
        raise AssertionError("strategy_returns.parquet está vazio!")
    if len(df_perf) == 0:
        raise AssertionError("desempenho_estrategias.parquet está vazio!")
    if len(df_pesos) == 0:
        raise AssertionError("pesos_historico.csv está vazio!")
        
    # Verifica que strategy_returns contém a coluna IBOV
    if "IBOV" not in df_ret.columns:
        raise AssertionError("A coluna 'IBOV' está ausente de strategy_returns.parquet!")
        
    print(f"  [OK] Arquivos de saída existem e não estão vazios.")
    print(f"  [OK] strategy_returns: {df_ret.shape[0]} datas x {df_ret.shape[1]} estratégias/IBOV.")
    print(f"  [OK] desempenho_estrategias: {df_perf.shape[0]} estratégias x {df_perf.shape[1]} métricas.")
    print(f"  [OK] pesos_historico: {df_pesos.shape[0]} alocações de ativos gravadas.")
    print("[OK] Teste 6: Estrutura física das saídas do backtest validada.")

# --- CASO DE TESTE 7: Validação de Restrições Metodológicas (MPT/PMPT CVM 175) ---
def test_portfolio_constraints():
    print("\n[TEST 7] Validando restrições de orçamento, long-only e teto CVM 175 nos pesos...")
    
    pesos_path = data_dir / "Estrategias" / "pesos_historico.csv"
    df_pesos = pd.read_csv(pesos_path)
    
    # 1. Validação de Orçamento e Long-Only
    # Agrupa por estratégia e data para verificar a soma dos pesos
    # Tolerância de 1e-4 para lidar com arredondamentos no CSV
    grouped = df_pesos.groupby(["estrategia", "data"])["peso"].sum()
    for (est, dt), soma in grouped.items():
        if abs(soma - 1.0) > 1e-4:
            raise AssertionError(f"Erro de orçamento! Estratégia '{est}' em {dt} soma {soma:.6f} (deveria somar 1.0)!")
            
    # Verifica se há algum peso negativo
    if (df_pesos["peso"] < -1e-6).any():
        negativos = df_pesos[df_pesos["peso"] < -1e-6]
        raise AssertionError(f"Erro Long-Only! Encontrados {len(negativos)} pesos negativos no histórico de pesos.")
        
    # 2. Validação do Teto CVM 175 (Limite máximo de 10% por emissor)
    # Aplica-se exclusivamente para estratégias que terminam com _c10
    c10_pesos = df_pesos[df_pesos["estrategia"].str.endswith("_c10")]
    violacoes_teto = c10_pesos[c10_pesos["peso"] > 0.10001]
    if len(violacoes_teto) > 0:
        print(violacoes_teto.head(5))
        raise AssertionError(f"Erro CVM 175! Encontradas {len(violacoes_teto)} alocações excedendo o teto de 10% nas estratégias limitadas.")
        
    print(f"  [OK] Validação de Orçamento Pleno (soma dos pesos = 100%) aprovada.")
    print(f"  [OK] Validação de Posicionamento Estrito (long-only, w >= 0) aprovada.")
    print(f"  [OK] Validação de Limites de Concentração (CVM 175, w <= 10%) aprovada.")
    print("[OK] Teste 7: Todas as restrições financeiras e metodológicas foram rigorosamente respeitadas.")


# --- CASO DE TESTE 8: Validação dos Outputs de Fronteira Eficiente ---
def test_efficient_frontier():
    print("\n[TEST 8] Validando outputs da fronteira eficiente (Etapa 8)...")
    
    mv_path = data_dir / "Estrategias" / "fronteira_mv_pontos.csv"
    canon_path = data_dir / "Estrategias" / "carteiras_canonicas.csv"
    img_path = data_dir / "Estrategias" / "fronteira_eficiente.png"
    
    for p in [mv_path, canon_path, img_path]:
        if not p.exists():
            raise FileNotFoundError(f"Arquivo obrigatório ausente da Etapa 8: {p.name}")
            
    df_mv = pd.read_csv(mv_path)
    df_canon = pd.read_csv(canon_path)
    
    if len(df_mv) < 10:
        raise AssertionError("fronteira_mv_pontos.csv contem poucos pontos (< 10)!")
    if len(df_canon) == 0:
        raise AssertionError("carteiras_canonicas.csv está vazio!")
        
    print(f"  [OK] MV pontos: {len(df_mv)} linhas. Carteiras canônicas: {len(df_canon)} linhas.")
    print("[OK] Teste 8: Validação física da fronteira eficiente aprovada.")


# --- CASO DE TESTE 9: Validação dos Apêndices de Inferência Econométrica ---
def test_econometric_inference():
    print("\n[TEST 9] Validando outputs da inferência econométrica (Etapa 9)...")
    
    ap_g_path = data_dir / "Estrategias" / "apendice_G_diagnostico_ibov.csv"
    ap_h_path = data_dir / "Estrategias" / "apendice_H_testes_estrategia.csv"
    ap_h_m_path = data_dir / "Estrategias" / "apendice_H_painel_metricas.csv"
    ap_h_c_path = data_dir / "Estrategias" / "apendice_H_comparativo_rf.csv"
    
    for p in [ap_g_path, ap_h_path, ap_h_m_path, ap_h_c_path]:
        if not p.exists():
            raise FileNotFoundError(f"Arquivo obrigatório ausente da Etapa 9: {p.name}")
            
    df_g = pd.read_csv(ap_g_path)
    df_h = pd.read_csv(ap_h_path)
    
    if len(df_g) < 5:
        raise AssertionError("apendice_G_diagnostico_ibov.csv contem poucas linhas (< 5)!")
    if len(df_h) < 10:
        raise AssertionError("apendice_H_testes_estrategia.csv contem poucas linhas (< 10)!")
        
    for col in ["CAPM p_alfa", "JK/Memmel p", "Spanning p"]:
        if col in df_h.columns:
            if not ((df_h[col] >= 0.0) & (df_h[col] <= 1.0001)).all():
                raise AssertionError(f"p-valores da coluna '{col}' fora do intervalo [0, 1]!")
                
    print(f"  [OK] Apêndice G: {len(df_g)} linhas. Apêndice H: {len(df_h)} linhas.")
    print("[OK] Teste 9: Contratos de dados da inferência econométrica validados.")


# Execução sucessiva
try:
    test_static_imports()
    test_config_resolution()
    test_data_consistency()
    test_math_assertions()
    test_covariance_regularization()
    test_backtest_outputs()
    test_portfolio_constraints()
    test_efficient_frontier()
    test_econometric_inference()
    print("\n" + "="*60)
    print("SUCESSO: TODOS OS CASOS DE TESTE DO PIPELINE FORAM APROVADOS")
    print("="*60)
except Exception as e:
    print(f"\n[-] ERRO NA SUÍTE DE TESTES: {e}")
    sys.exit(1)


