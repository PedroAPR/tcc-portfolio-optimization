# CLAUDE.md — TCC: Otimização de Portfólios no Mercado Brasileiro
**Autor:** Pedro Augusto Pinheiro Reis | UFG — Ciências Contábeis  
**Tema:** Moderna Teoria das Carteiras, PMPT e Black-Litterman com implementação em Python

---

## Visão Geral do Projeto

TCC de graduação que implementa e compara estratégias de otimização de portfólio no mercado de ações brasileiro (B3), período 2010–2025. O pipeline vai de dados brutos de preços até backtests out-of-sample com cinco estratégias distintas.

O **resultado mais sólido** é a Mínima Variância L1 com janelas expansivas: +460% vs IBOV +215% (2015–2025). O resultado mais fraco é o Black-Litterman+LSTM+FF5: +56%, MDD -93%, Sharpe -0.14.

---

## Estrutura de Diretórios

```
C:\VSCodeWorkspace\TCC_Escrito\
├── data\                          ← TODOS os CSVs, Parquets e Excels vivem aqui
│   ├── precos_sanitizada_v3.csv   ← Input bruto (Economática), nunca modificar
│   ├── CDI_2010_2026.xlsx         ← Taxa DI diária (coluna: Date, CDI)
│   ├── IBOV_2010_2026.xlsx        ← Índice Bovespa (coluna: Date, IBOV)
│   ├── SELIC_2010_2026.xlsx       ← Taxa Selic (coluna: Date, SELIC)
│   └── nefin_factors.csv          ← Fatores NEFIN (Rm_minus_Rf,SMB,HML,WML,IML)
│
└── notebooks\                     ← Jupyter notebooks numerados (pipeline = ordem)
    ├── [1–9]   Pipeline base
    ├── [12–13] Backtests HMM+EWMA
    ├── [14]    Backtests L1 Expansivo (os resultados bons)
    ├── [15]    CAPM e prior BL
    ├── [16–18] Black-Litterman híbrido
    └── [19–20] Métricas finais e LSTM end-to-end
```

---

## Pipeline Canônico (ordem de execução)

Execute nesta ordem. **Nunca pule etapas** — cada notebook depende dos arquivos gerados pelo anterior.

### Fase 1 — Preparação de Dados

| Nº | Notebook | Entrada | Saída |
|----|----------|---------|-------|
| 1 | `1_Sanitizacao_Dados.ipynb` | `precos_sanitizada_v3.csv` | `precos_limpos_finais.csv` |
| 2 | `2_1_Matriz_de_Retornos_Simples_Logaritmica.ipynb` | `precos_limpos_finais.csv` + `IBOV_2010_2026.xlsx` | `matriz_retornos_simples_v2.csv`, `matriz_retornos_logaritmicos_v2.csv` |
| 3 | `3_1_Merge_B3_CDI_SELIC_Acoes.ipynb` | `precos_limpos_finais.csv` + excels | `base_mestre_consolidada_IBOV_CDI_SELIC.csv` |
| 4 | `4_Calculo_Premio_Risco.ipynb` | `base_mestre_consolidada_IBOV_CDI_SELIC.csv` | `matriz_premio_risco.csv` |
| 5 | `5_Matriz_Covariância_KPIs_CAPM.ipynb` | `matriz_premio_risco.csv` | `matriz_covariancia_anualizada.csv`, `kpis_ativos_markowitz.csv` |

### Fase 2 — Análise Descritiva (opcional, apenas visualizações)

| Nº | Notebook | Saída |
|----|----------|-------|
| 7 | `7_Fronteira_Eficiente.ipynb` | `fronteira_eficiente.png` (in-sample, não usar para backtesting) |
| 8 | `8_Grafico_Matriz_Covariancia.ipynb` | `heatmap_covariancia_negativa.png` |
| 9 | `9_Grafico_Matriz_Correlacao.ipynb` | `heatmap_correlacao_clusterizada.png` |

### Fase 3A — Backtest HMM+EWMA

| Nº | Notebook | Saída |
|----|----------|-------|
| 12.1.1 | `12_1_1_Janelas_Moveis_HMM_EWMA_Mensal_atualizado_maximo_sharpe.ipynb` | `historico_alocacao_HMM_EWMA_maximo_sharpe.csv` |
| 13 | `13_Grafico_Rentabilidade_HMM_EWMA.ipynb` | `equity_curve_hmm_final.png` |

### Fase 3B — Backtest L1 Expansivo ← Resultados principais do TCC

| Nº | Notebook | Saída | Resultado |
|----|----------|-------|-----------|
| 14.1.1 | `14_1_1_Janelas_Expansivas_Max_Sharpe.ipynb` | `historico_pesos_l1_5anos_M_max_sharpe.parquet` | — |
| 14.1.2 | `14_1_2_Backteste_Janelas_Expansivas_Max_Sharpe.ipynb` | `equity_curve_l1_max_sharpe.png` | **+240% vs IBOV +215%** |
| 14.1.3 | `14_1_3_Turnover_Janela_Expansiva_Max_Sharpe.ipynb` | `analise_turnover_mensal_max_sharpe.png` | giro médio 4.29% |
| 14.2.1 | `14_2_1_Janelas_Expansivas_Min_Var.ipynb` | `historico_pesos_l1_5anos_M_min_var.parquet` | — |
| 14.2.2 | `14_2_2_Backteste_Janelas_Expansivas_Min_Var.ipynb` | `equity_curve_l1_min_var.png` | **+460% vs IBOV +215%** |
| 14.2.3 | `14_2_3_Turnover_Janela_Expansiva_Min_Var.ipynb` | `analise_turnover_mensal_min_var.png` | giro médio 0.32% |

### Fase 3C — Backtest Black-Litterman + LSTM + Fama-French 5

| Nº | Notebook | Saída |
|----|----------|-------|
| 17_ext | `17_Extracao_Fatores_NEFIN.ipynb` | `fatores_nefin_limpos.csv` |
| 2_mkt | `2_Pesos_Mercado.ipynb` | `pesos_mercado_black_litterman.csv` |
| 5_lstm | `5_LSTM_Treinamento_Janelas_expansivas.ipynb` | `visoes_lstm_ff5_overnight_completo.csv` ← longa execução |
| 17.3 | `17_3_Black_Litterman_Hibrido_ff5.ipynb` | `historico_alocacao_lstm_ff5_overnight.csv` |
| 18 | `18_Calculo_Curva_Capital_Quantamental.ipynb` | `curva_capital_quantamental_final.png` |
| 19 | `19_Tabela_Metricas_Risco.ipynb` | `tabela_metricas_finais_tcc.csv` |

---

## ⚠️ Arquivos e Notebooks ENVENENADOS — Nunca usar

Estes arquivos foram gerados com um bug crítico (CDI calculado erroneamente como ~160%/ano). Qualquer saída deles é inválida.

```
4_1_Calculo_Premio_Risco_original.ipynb   ← BUG: lê master file como CDI
5_Matriz_Covariância_KPIs_CAPM_original.ipynb  ← Gerado com CDI errado
6_Fronteira_Eficiente.ipynb               ← Gerado com CDI errado (Sharpe = -2.93)
```

Se esses arquivos CSV correspondentes estiverem em `data/`, excluir e regenerar:
- `kpis_ativos_markowitz.csv` gerado antes de mar/2025 → regenerar com `5_Matriz_Covariância_KPIs_CAPM.ipynb`
- `pesos_carteiras_otimizadas.csv` gerado pelo notebook `6` → regenerar com `7_Fronteira_Eficiente.ipynb`

---

## Bugs Conhecidos e Correções

### Bug 1 — `4_Calculo_Premio_Risco.ipynb` tenta ler `.parquet` que não existe

```python
# ATUAL (quebrado):
caminho_mestre = os.path.join(diretorio_dados, "base_mestre_consolidada_IBOV_CDI_SELIC.parquet")
df_mestre = pd.read_parquet(caminho_mestre)

# CORRETO:
caminho_mestre = os.path.join(diretorio_dados, "base_mestre_consolidada_IBOV_CDI_SELIC.csv")
df_mestre = pd.read_csv(caminho_mestre, index_col='Data', parse_dates=True)
```

### Bug 2 — Ticker WEGE3 com underscore espúrio

O arquivo `precos_sanitizada_v3.csv` e o pipeline têm a coluna `WEGE3_` (com underscore). Isso causa erro 404 no yfinance e aparece errado nos gráficos. Renomear a coluna para `WEGE3` na sanitização ou na geração da `matriz_retornos_simples_v2.csv`.

### Bug 3 — `15_CAPM_.ipynb` elimina coluna Date antes de indexar

```python
# LINHA PROBLEMÁTICA (remover esta):
ibov = ibov.drop(columns=['Data'])
# Em seguida falha em:
retornos_ibov = ibov.set_index('Data')  # KeyError: 'Data'
```

### Bug 4 — Delta do CAPM reverso é negativo

`15_2_CAPM_Reverso_BL.ipynb` produz `delta = -0.0884`. Isso é matematicamente inválido para o prior do BL. **Não usar este valor**. Os notebooks de BL usam `delta=2.5` hardcoded, que é a convenção correta da literatura (He & Litterman, 1999). Documentar esta limitação no TCC.

### Bug 5 — Leitura de CSV com separador errado nos notebooks de backtest

Os notebooks `13`, `14_1_2`, `14_2_2` leem `base_mestre_consolidada_IBOV_CDI_SELIC.csv` com:
```python
pd.read_csv(caminho, sep=';', decimal=',', encoding='latin1')
```
Verificar **antes de executar** qual é o separador real do arquivo. Se foi gerado pelo `3_1_Merge_B3_CDI_SELIC_Acoes.ipynb` (pandas padrão), o correto é `sep=','`. Se foi exportado pelo Excel brasileiro, `sep=';'` está certo. Rodar `head -2 base_mestre_consolidada_IBOV_CDI_SELIC.csv` para confirmar.

---

## Convenções do Projeto

### Nomenclatura de arquivos de dados

| Sufixo/Padrão | Significado |
|---|---|
| `_v2` | Versão corrigida e final (ex: `matriz_retornos_simples_v2.csv`) |
| `_original` | Versão antiga com bug — não usar |
| `_maximo_sharpe` | Arquivo de pesos da estratégia Max Sharpe |
| `_min_var` | Arquivo de pesos da estratégia Mínima Variância |
| `_overnight` | Gerado em execução longa (LSTM para todos os ativos) |
| `.parquet` | Gerado pelos notebooks da série 14 (mais rápido que CSV) |

### Variáveis recorrentes no código

```python
pasta_dados = r"C:\VSCodeWorkspace\TCC_Escrito\data"  # diretório único de dados

colunas_macro = ['IBOV', 'CDI', 'SELIC']              # separar de ativos
colunas_ativos = [col for col in df.columns if col not in colunas_macro]

# CDI diário correto ≈ 0.00036885 (aprox 9.3% a.a.)
# Se aparecer CDI diário > 0.001, há bug — parar e investigar
```

### Look-ahead bias — regra crítica

Todo cruzamento de pesos com retornos **deve** usar `shift(1)`:
```python
# CORRETO:
pesos_diarios = df_pesos.reindex(df_retornos.index).ffill().shift(1)
retorno = (pesos_diarios * df_retornos).sum(axis=1)

# ERRADO (contamina resultados):
retorno = (df_pesos * df_retornos).sum(axis=1)
```

### Anualização

```python
retornos_anualizados = df_retornos_diarios.mean() * 252
volatilidade_anualizada = df_retornos_diarios.std() * np.sqrt(252)
cov_anualizada = df_retornos_diarios.cov() * 252
# NÃO usar * 21 para mensalizar — o BL usa covariância anualizada
```

---

## Dependências e Ambiente

**Python**: 3.11.9 (usar para todos os backtests; alguns notebooks foram testados com 3.14 mas não é recomendado para TF/Keras)

```bash
pip install pandas numpy scipy matplotlib seaborn plotly
pip install scikit-learn tensorflow keras
pip install cvxpy hmmlearn
pip install yfinance openpyxl pyarrow
pip install statsmodels tabulate tqdm
```

**Solvers CVXPY** (em ordem de preferência por notebook):
- Notebooks série 14: `cp.OSQP` com fallback `cp.ECOS`
- Notebooks série 16/17 (BL): `cp.CLARABEL`
- Notebooks série 12 (HMM): `cp.ECOS`

---

## Resultados Consolidados (referência rápida)

Todos os backtests usam período out-of-sample iniciando em **~jan/2015** (após 60 meses de treino com dados desde 2010).

> ⚠️ Os notebooks 14_x_2 iniciam em ~set/2015 (IBOV=215%), enquanto os notebooks 13 e 19 iniciam em ~jan/2015 (IBOV=243%). **Não comparar resultados entre esses grupos diretamente** sem padronizar o período.

| Estratégia | Retorno | IBOV mesmo período | Sharpe | MDD | Turnover/mês |
|---|---|---|---|---|---|
| L1 Mínima Variância Expansiva | **+460.20%** | +215.00% | n/calculado | n/calculado | 0.32% |
| L1 Max Sharpe Expansiva | **+240.09%** | +215.00% | n/calculado | n/calculado | 4.29% |
| HMM+EWMA (notebook 13) | +381.44% | +243.49% | n/calculado | n/calculado | 0.51% |
| BL+LSTM+FF5 | +56.48% | +243.49% | **-0.14** | **-92.99%** | ~55% |

**Sanity check rápido**: se qualquer estratégia mostrar Sharpe abaixo de -1 ou MDD pior que -50%, verificar o arquivo de pesos que está sendo lido — pode estar usando o arquivo errado.

---

## Estrutura dos Dados Externos Obrigatórios

```
CDI_2010_2026.xlsx
  Colunas: Date (datetime), CDI (float, taxa diária ~0.00037)

IBOV_2010_2026.xlsx
  Colunas: Date (datetime), IBOV (float, nível do índice)

SELIC_2010_2026.xlsx
  Colunas: Date (datetime), SELIC (float, taxa diária)

nefin_factors.csv
  Colunas: Date, Rm_minus_Rf, SMB, HML, WML, IML
  Fonte: http://nefin.com.br/risk_factors.html
  Período disponível: 2001–presente
```

---

## Execuções Longas — Planejar com Antecedência

| Notebook | Tempo estimado | Observação |
|---|---|---|
| `4_Teste2_Janelas_Expansivas.ipynb` | 2–8h | LSTM para ~136 ativos, reiniciável (checkpoint) |
| `5_LSTM_Treinamento_Janelas_expansivas.ipynb` | 4–12h | LSTM+FF5 para ~136 ativos, reiniciável |
| `14_1_1` e `14_2_1` | 10–20min | L1 expansivo, 132 períodos |
| `12_1_1` e `12_2_1` | 5–10min | HMM+EWMA, 132 períodos |
| `16_Black_Litterman_Hibrido_2.ipynb` | <1min | BL é rápido (sem ML no loop) |

---

## Perguntas Frequentes para Contexto de Código

**"Qual arquivo de retornos devo usar?"**  
→ `matriz_retornos_simples_v2.csv` para otimização e backtesting. `matriz_retornos_logaritmicos_v2.csv` para análise estatística (assimetria, curtose).

**"Qual arquivo de covariância devo usar?"**  
→ `matriz_covariancia_anualizada.csv` (gerado pelo `5_Matriz_Covariância_KPIs_CAPM.ipynb`). Nunca o gerado pelo notebook `5_original`.

**"Preciso do IBOVESPA como série?"**  
→ Está em `matriz_retornos_simples_v2.csv` como coluna `IBOV`. Separar com: `retorno_ibov = df['IBOV']`, `df_ativos = df.drop(columns=['IBOV'])`.

**"O CDI já está subtraído nos retornos?"**  
→ Depende do arquivo. `matriz_premio_risco.csv` = retornos JÁ com CDI subtraído (excess return). `matriz_retornos_simples_v2.csv` = retornos brutos, CDI ainda não subtraído.

**"Como saber qual versão do arquivo usar quando há v1 e v2?"**  
→ Sempre `v2`. A v1 foi gerada antes da correção do bug do CDI ou sem o IBOV alinhado.

---

## Referências Bibliográficas Essenciais

- Black & Litterman (1992) — *Financial Analysts Journal*, 48(5)
- He & Litterman (1999) — Goldman Sachs working paper (calibração delta/tau)
- DeMiguel, Garlappi & Uppal (2009) — *Review of Financial Studies*, 22(5) — por que Min Variância vence
- Ledoit & Wolf (2004) — *J. Multivariate Analysis*, 88(2) — covariância robusta
- Rockafellar & Uryasev (2002) — *J. Banking & Finance*, 26(7) — CVaR
- Santos & Tessari (2012) — *Revista Brasileira de Finanças*, 10(3) — otimização na B3
- Welch & Goyal (2008) — *Review of Financial Studies*, 21(4) — por que LSTM não prevê retornos

---

*Última atualização: Maio de 2026*
