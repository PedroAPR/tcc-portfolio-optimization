import json
from pathlib import Path

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Notebook 9 — Inferência Econométrica de Desempenho e Caracterização do Benchmark\n",
                "\n",
                "**TCC — Pedro Augusto Pinheiro Reis · Ciências Contábeis · UFG**\n",
                "\n",
                "Este notebook operacionaliza a caracterização econométrica do benchmark (IBOVESPA) e executa os testes de hipóteses estatísticas comparando as carteiras ótimas contra o mercado."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 1. Importações e Configurações"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import sys\n",
                "import warnings\n",
                "from pathlib import Path\n",
                "import numpy as np\n",
                "import pandas as pd\n",
                "from scipy import stats\n",
                "import statsmodels.api as sm\n",
                "from statsmodels.tsa.stattools import adfuller, kpss\n",
                "from statsmodels.stats.diagnostic import het_arch\n",
                "from arch import arch_model\n",
                "from arch.unitroot import VarianceRatio\n",
                "\n",
                "from utils.config_loader import carregar_parametros\n",
                "from utils.inferencia import (\n",
                "    fmt_pvalor,\n",
                "    sharpe,\n",
                "    sortino,\n",
                "    sharpe_de_excesso,\n",
                "    sortino_de_excesso,\n",
                "    cagr,\n",
                "    max_drawdown,\n",
                "    _wald_spanning,\n",
                "    _jk_memmel,\n",
                "    bootstrap_ic,\n",
                "    diagnostico_residuos,\n",
                "    TRADING_DAYS\n",
                ")\n",
                "\n",
                "warnings.filterwarnings(\"ignore\")\n",
                "\n",
                "cfg = carregar_parametros()\n",
                "SEED = cfg.get(\"SEED\", 42)\n",
                "BOOTSTRAP_REPS = cfg.get(\"BOOTSTRAP_REPS\", 1000)\n",
                "BOOTSTRAP_BLOCK_MEAN = cfg.get(\"BOOTSTRAP_BLOCK_MEAN\", 21)\n",
                "SPANNING_MAX_LAGS = cfg.get(\"SPANNING_MAX_LAGS\", 5)\n",
                "\n",
                "project_root = Path.cwd().parent.parent\n",
                "INPUT_DIR_IBOV = project_root / \"data\" / \"Ibov\" / \"Ibov_Diario\"\n",
                "INPUT_DIR_CDI = project_root / \"data\" / \"CDI\"\n",
                "INPUT_DIR_STRATEGY = project_root / \"data\" / \"Estrategias\"\n",
                "OUTPUT_DIR = project_root / \"data\" / \"Estrategias\"\n",
                "OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n",
                "\n",
                "ESTRATEGIAS = [\n",
                "    \"EqualWeight\", \"InvVol\", \"MinVar\", \"MinVar_c10\", \"MaxSharpe\", \"MaxSharpe_c10\",\n",
                "    \"MaxOmega\", \"MaxSortino\", \"MaxKappa3\", \"MinCVaR\", \"MinCDaR\"\n",
                "]\n",
                "\n",
                "print(f\"✓ Configurações carregadas. Total de estratégias: {len(ESTRATEGIAS)}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Ingestão de Dados e Alinhamento do Benchmark"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "ibov_path = INPUT_DIR_IBOV / \"ibov_diario_2010_2026.csv\"\n",
                "if not ibov_path.exists():\n",
                "    raise FileNotFoundError(\"ibov_diario_2010_2026.csv não encontrado.\")\n",
                "ibov = pd.read_csv(ibov_path, parse_dates=[\"data\"])\n",
                "ibov = ibov.dropna(subset=[\"ibov_ret_simples\"]).reset_index(drop=True)\n",
                "\n",
                "cdi_path = INPUT_DIR_CDI / \"cdi_diario_bcb_2010_atual.csv\"\n",
                "if not cdi_path.exists():\n",
                "    raise FileNotFoundError(\"cdi_diario_bcb_2010_atual.csv não encontrado.\")\n",
                "cdi_df = pd.read_csv(cdi_path, sep=\";\", parse_dates=[\"data\"])\n",
                "\n",
                "cdi_serie = cdi_df.set_index(\"data\")[\"cdi_diario\"].reindex(ibov[\"data\"]).ffill().bfill()\n",
                "ibov[\"cdi_diario\"] = cdi_serie.values\n",
                "ibov[\"ibov_ret_log\"] = np.log(1 + ibov[\"ibov_ret_simples\"])\n",
                "\n",
                "print(f\"✓ Benchmark carregado e alinhado: {len(ibov):,} observações.\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Testes de Raiz Unitária e Ordem de Integração do IBOV"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "r = ibov[\"ibov_ret_log\"].dropna()\n",
                "p = ibov[\"ibov_close\"]\n",
                "\n",
                "adf_r = adfuller(r, autolag=\"AIC\")\n",
                "adf_p = adfuller(p, autolag=\"AIC\")\n",
                "kpss_r = kpss(r, regression=\"c\", nlags=\"auto\")\n",
                "kpss_p = kpss(p, regression=\"c\", nlags=\"auto\")\n",
                "\n",
                "print(\"========================================================================\")\n",
                "print(\"TESTES DE ESTACIONARIEDADE DO BENCHMARK (IBOV)\")\n",
                "print(\"========================================================================\\n\")\n",
                "print(f\"ADF em log-retornos:   estat={adf_r[0]:.4f} | p-valor={fmt_pvalor(adf_r[1])}\")\n",
                "print(f\"KPSS em log-retornos:  estat={kpss_r[0]:.4f} | p-valor={fmt_pvalor(kpss_r[1])}\")\n",
                "print(f\"ADF em nível (close):  estat={adf_p[0]:.4f} | p-valor={fmt_pvalor(adf_p[1])}\")\n",
                "print(f\"KPSS em nível (close): estat={kpss_p[0]:.4f} | p-valor={fmt_pvalor(kpss_p[1])}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. Diagnóstico de Momentos Superiores e Dependência Temporal"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "arch_stat, arch_p, _, _ = het_arch(r, nlags=10)\n",
                "jb_stat, jb_p = stats.jarque_bera(r)\n",
                "\n",
                "print(\"========================================================================\")\n",
                "print(\"DIAGNÓSTICO ESTATÍSTICO DE COMPORTAMENTO DISTRIBUTIVO (IBOV)\")\n",
                "print(\"========================================================================\\n\")\n",
                "print(f\"ARCH-LM (10 lags):  estat = {arch_stat:.2f}  p-valor = {fmt_pvalor(arch_p)}\")\n",
                "print(f'Jarque-Bera:        estat = {jb_stat:.2f}  p-valor = {fmt_pvalor(jb_p)}')\n",
                "print(f\"Assimetria:         {r.skew():+.4f}\")\n",
                "print(f\"Curtose excedente:  {r.kurt():+.4f}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 5. Teste de Razão de Variâncias de Lo-MacKinlay"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "log_price = np.log(p).values\n",
                "vr_2 = VarianceRatio(log_price, 2, overlap=True)\n",
                "vr_16 = VarianceRatio(log_price, 16, overlap=True)\n",
                "\n",
                "print(\"========================================================================\")\n",
                "print(\"TESTE DE RAZÃO DE VARIÂNCIAS DE LO-MACKINLAY (1988) DO IBOV\")\n",
                "print(\"========================================================================\\n\")\n",
                "print(f\"Razão de Variâncias (k=2):   estat={vr_2.stat:.4f} | p-valor={fmt_pvalor(vr_2.pvalue)}\")\n",
                "print(f\"Razão de Variâncias (k=16):  estat={vr_16.stat:.4f} | p-valor={fmt_pvalor(vr_16.pvalue)}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 6. Modelagem de Volatilidade Condicional e Parâmetro Delta"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "r_pct = r * 100\n",
                "res_garch = arch_model(r_pct, mean=\"Constant\", vol=\"Garch\", p=1, q=1, dist=\"normal\").fit(disp=\"off\")\n",
                "res_gjr = arch_model(r_pct, mean=\"Constant\", vol=\"Garch\", p=1, o=1, q=1, dist=\"t\").fit(disp=\"off\")\n",
                "res_eg = arch_model(r_pct, mean=\"Constant\", vol=\"EGARCH\", p=1, o=1, q=1, dist=\"t\").fit(disp=\"off\")\n",
                "\n",
                "comp = pd.DataFrame([\n",
                "    diagnostico_residuos(res_garch, \"GARCH(1,1) Normal\"),\n",
                "    diagnostico_residuos(res_gjr,   \"GJR-GARCH(1,1,1) t\"),\n",
                "    diagnostico_residuos(res_eg,    \"EGARCH(1,1,1) t\"),\n",
                "])\n",
                "\n",
                "melhor = comp.loc[comp[\"BIC\"].idxmin(), \"Modelo\"]\n",
                "res_melhor = {\"GARCH(1,1) Normal\": res_garch, \"GJR-GARCH(1,1,1) t\": res_gjr, \"EGARCH(1,1,1) t\": res_eg}[melhor]\n",
                "\n",
                "print(\"========================================================================\")\n",
                "print(\"COMPARAÇÃO DE MODELOS DE VOLATILIDADE CONDICIONAL E CRITÉRIOS\")\n",
                "print(\"========================================================================\\n\")\n",
                "print(comp.round(4).to_string(index=False))\n",
                "print(f\"\\n>>> Modelo selecionado pelo BIC: {melhor}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 7. Consolidação de Estratégias e Análise de Sensibilidade"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "strat_pq = INPUT_DIR_STRATEGY / \"strategy_returns.parquet\"\n",
                "strat_csv = INPUT_DIR_STRATEGY / \"strategy_returns.csv\"\n",
                "if strat_pq.exists():\n",
                "    strat = pd.read_parquet(strat_pq)\n",
                "else:\n",
                "    strat = pd.read_csv(strat_csv, index_col=0, parse_dates=True)\n",
                "\n",
                "df = pd.DataFrame(index=strat.index)\n",
                "df[\"ret_ibov\"] = ibov.set_index(\"data\")[\"ibov_ret_simples\"].reindex(df.index).ffill().bfill()\n",
                "df[\"rf\"] = ibov.set_index(\"data\")[\"cdi_diario\"].reindex(df.index).ffill().bfill()\n",
                "\n",
                "for est in ESTRATEGIAS:\n",
                "    df[est] = strat[est]\n",
                "    df[f\"excess_{est}\"] = df[est] - df[\"rf\"]\n",
                "df[\"excess_ibov\"] = df[\"ret_ibov\"] - df[\"rf\"]\n",
                "\n",
                "colunas_teste = ESTRATEGIAS + [\"ret_ibov\"]\n",
                "linhas_perf = []\n",
                "for c in colunas_teste:\n",
                "    nm = \"IBOVESPA\" if c == \"ret_ibov\" else c\n",
                "    r_serie = df[c]\n",
                "    sh = sharpe(r_serie, df[\"rf\"])\n",
                "    so = sortino(r_serie, df[\"rf\"])\n",
                "    linhas_perf.append({\n",
                "        \"Estratégia\": nm,\n",
                "        \"Retorno Acumulado (%)\": float((1 + r_serie).prod() - 1) * 100,\n",
                "        \"CAGR (% a.a.)\": cagr(r_serie) * 100,\n",
                "        \"Volatilidade (% a.a.)\": float(r_serie.std() * np.sqrt(TRADING_DAYS)) * 100,\n",
                "        \"Sharpe\": sh,\n",
                "        \"Sortino\": so,\n",
                "        \"Max Drawdown (%)\": max_drawdown(r_serie) * 100\n",
                "    })\n",
                "painel = pd.DataFrame(linhas_perf)\n",
                "\n",
                "print(\"========================================================================\")\n",
                "print(\"PAINEL COMPARATIVO GERAL DE PERFORMANCE E RISCO\")\n",
                "print(\"========================================================================\\n\")\n",
                "print(painel.round(4).to_string(index=False))"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 8. Validação Não-Paramétrica via Stationary Bootstrap"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "print(f\"Stationary bootstrap (B={BOOTSTRAP_REPS}, block_mean={BOOTSTRAP_BLOCK_MEAN}d)\\n\")\n",
                "print(f\"{'Métrica Estatística':<22} | {'Estratégia (IC 95%)':<36} | {'IBOVESPA (IC 95%)'}\")\n",
                "print(\"-\" * 100)\n",
                "\n",
                "for est in ESTRATEGIAS:\n",
                "    print(f\"\\n========================================================================\")\n",
                "    print(f\"INTERVALOS DE CONFIANÇA POR REAMOSTRAGEM: {est} VS IBOVESPA\")\n",
                "    print(\"========================================================================\")\n",
                "    for nome_fn, fn, serie_a, serie_b in [\n",
                "        (\"Sharpe (excesso)\",  sharpe_de_excesso,  df[f\"excess_{est}\"], df[\"excess_ibov\"]),\n",
                "        (\"Sortino (excesso)\", sortino_de_excesso, df[f\"excess_{est}\"], df[\"excess_ibov\"]),\n",
                "        (\"CAGR (bruto)\",      cagr,               df[est],             df[\"ret_ibov\"]),\n",
                "    ]:\n",
                "        s_lo, s_md, s_hi = bootstrap_ic(serie_a, fn, B=BOOTSTRAP_REPS, block_mean=BOOTSTRAP_BLOCK_MEAN, seed=SEED)\n",
                "        i_lo, i_md, i_hi = bootstrap_ic(serie_b, fn, B=BOOTSTRAP_REPS, block_mean=BOOTSTRAP_BLOCK_MEAN, seed=SEED)\n",
                "        print(f\"{nome_fn:<22} | [{s_lo:+.4f},  {s_md:+.4f},  {s_hi:+.4f}]  | \"\n",
                "              f\"[{i_lo:+.4f},  {i_md:+.4f},  {i_hi:+.4f}]\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 9. CAPM HAC, Jobson-Korkie/Memmel e Wald Spanning"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "X_capm = sm.add_constant((df[\"ret_ibov\"] - df[\"rf\"]).values)\n",
                "X_span = sm.add_constant(df[\"ret_ibov\"].values)\n",
                "exc_ibov = df[\"ret_ibov\"] - df[\"rf\"]\n",
                "\n",
                "linhas_testes = []\n",
                "for est in ESTRATEGIAS:\n",
                "    exc = df[est] - df[\"rf\"]\n",
                "    capm = sm.OLS(exc.values, X_capm).fit(cov_type=\"HAC\", cov_kwds={\"maxlags\": SPANNING_MAX_LAGS})\n",
                "    z_jk, p_jk = _jk_memmel(exc, exc_ibov)\n",
                "    _, f_sp, p_sp = _wald_spanning(df[est].values, X_span, maxlags=SPANNING_MAX_LAGS)\n",
                "    linhas_testes.append({\n",
                "        \"Estrategia\":         est,\n",
                "        \"CAPM alfa (% a.a.)\": capm.params[0] * TRADING_DAYS * 100,\n",
                "        \"CAPM beta\":          capm.params[1],\n",
                "        \"CAPM t_alfa (NW)\":   capm.tvalues[0],\n",
                "        \"CAPM p_alfa\":        capm.pvalues[0],\n",
                "        \"JK/Memmel z\":        z_jk,\n",
                "        \"JK/Memmel p\":        p_jk,\n",
                "        \"Spanning F\":         f_sp,\n",
                "        \"Spanning p\":         p_sp,\n",
                "        \"Sharpe (rf var)\":    sharpe(df[est], df[\"rf\"]),\n",
                "        \"Sortino (rf var)\":   sortino(df[est], df[\"rf\"]),\n",
                "    })\n",
                "\n",
                "apendice_H = pd.DataFrame(linhas_testes).set_index(\"Estrategia\")\n",
                "\n",
                "print(\"========================================================================\")\n",
                "print(\"APÊNDICE L — INFERÊNCIA COMPARATIVA TRANSVERSAL (HAC Newey-West)\")\n",
                "print(\"========================================================================\\n\")\n",
                "for est, row in apendice_H.iterrows():\n",
                "    print(f\"\\n> {est}\")\n",
                "    print(f\"   CAPM:     alfa = {row['CAPM alfa (% a.a.)']:+.2f}% a.a. | beta = {row['CAPM beta']:.3f} \"\n",
                "          f\"| t(NW) = {row['CAPM t_alfa (NW)']:+.3f} | p = {fmt_pvalor(row['CAPM p_alfa'])}\")\n",
                "    print(f\"   JK/Memmel vs IBOV: z = {row['JK/Memmel z']:+.3f} | p = {fmt_pvalor(row['JK/Memmel p'])}\")\n",
                "    print(f\"   Spanning (a=0,b=1): F = {row['Spanning F']:.2f} | p = {fmt_pvalor(row['Spanning p'])}\")\n",
                "    print(f\"   Sharpe = {row['Sharpe (rf var)']:+.4f} | Sortino = {row['Sortino (rf var)']:+.4f}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 10. Exportação dos Resultados e Apêndices"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "apendice_G = pd.DataFrame([\n",
                "    {\"Teste\": \"ADF (log-retornos)\",     \"H₀\": \"raiz unitária\",    \"Estat.\": adf_r[0],  \"p-valor\": adf_r[1]},\n",
                "    {\"Teste\": \"KPSS (log-retornos)\",    \"H₀\": \"estacionariedade\", \"Estat.\": kpss_r[0], \"p-valor\": kpss_r[1]},\n",
                "    {\"Teste\": \"ADF (nível)\",            \"H₀\": \"raiz unitária\",    \"Estat.\": adf_p[0],  \"p-valor\": adf_p[1]},\n",
                "    {\"Teste\": \"KPSS (nível)\",           \"H₀\": \"estacionariedade\", \"Estat.\": kpss_p[0], \"p-valor\": kpss_p[1]},\n",
                "    {\"Teste\": \"ARCH-LM (10 lags)\",      \"H₀\": \"variância constante\", \"Estat.\": arch_stat, \"p-valor\": arch_p},\n",
                "    {\"Teste\": \"Jarque-Bera\",            \"H₀\": \"normalidade\",      \"Estat.\": jb_stat,        \"p-valor\": jb_p},\n",
                "    {\"Teste\": \"VR k=2 (Lo-MacKinlay)\",  \"H₀\": \"passeio aleatório\", \"Estat.\": vr_2.stat,  \"p-valor\": vr_2.pvalue},\n",
                "    {\"Teste\": \"VR k=16 (Lo-MacKinlay)\", \"H₀\": \"passeio aleatório\", \"Estat.\": vr_16.stat, \"p-valor\": vr_16.pvalue},\n",
                "])\n",
                "apendice_G[\"Decisão\"] = np.where(apendice_G[\"p-valor\"] < 0.05, \"Rejeita H₀ ✗\", \"Não rejeita H₀ ✓\")\n",
                "apendice_G.to_csv(OUTPUT_DIR / \"apendice_G_diagnostico_ibov.csv\", index=False)\n",
                "\n",
                "apendice_H.to_csv(OUTPUT_DIR / \"apendice_H_testes_estrategia.csv\", float_format=\"%.6f\")\n",
                "painel.to_csv(OUTPUT_DIR / \"apendice_H_painel_metricas.csv\", index=False)\n",
                "\n",
                "comp_rf_linhas = []\n",
                "for c in colunas_teste:\n",
                "    nm = \"IBOVESPA\" if c == \"ret_ibov\" else c\n",
                "    comp_rf_linhas.append({\n",
                "        \"Estratégia\": nm,\n",
                "        \"Sharpe (CDI)\": sharpe(df[c], df[\"rf\"]),\n",
                "        \"Sharpe (Zero)\": sharpe(df[c], 0.0),\n",
                "        \"Sortino (CDI)\": sortino(df[c], df[\"rf\"]),\n",
                "        \"Sortino (Zero)\": sortino(df[c], 0.0),\n",
                "    })\n",
                "comp_rf = pd.DataFrame(comp_rf_linhas)\n",
                "comp_rf.to_csv(OUTPUT_DIR / \"apendice_H_comparativo_rf.csv\", index=False)\n",
                "\n",
                "print(\"✓ CSVs de apêndice exportados com sucesso em:\", OUTPUT_DIR)"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.11.9"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
}

nb_folder = Path("src/09_Inferencia_Econometrica")
nb_folder.mkdir(parents=True, exist_ok=True)
with open(nb_folder / "09_01_Inferencia_Econometrica.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=1)

print("✓ Stage 9 notebook generated successfully!")
