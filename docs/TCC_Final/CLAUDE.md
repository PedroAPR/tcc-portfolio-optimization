# CLAUDE.md — TCC: Otimização de Portfólios no Mercado Brasileiro
**Autor:** Pedro Augusto Pinheiro Reis | UFG — Ciências Contábeis  
**Título oficial:** Moderna Teoria das Carteiras no Mercado de Ações Brasileiro: Comparação entre Otimizadores e Inputs  
**Última atualização:** Maio de 2026 (Sessão 2)

---

## Estado Atual do Projeto

| Componente | Status |
|---|---|
| Documento TCC (Entrega_10) | ✅ Estrutura ABNT corrigida — usar como base |
| Capítulo 1 — Introdução | ✅ Completo (Entrega_9/10) |
| Capítulo 2 — Referencial Teórico | ✅ Completo (seções 2.1–2.22) |
| Capítulo 3 — Metodologia | ✅ Reescrito nesta sessão — colar no Word |
| Capítulo 4 — Resultados e Discussão | ✅ Escrito — faltam métricas de risco das estratégias L1 |
| Capítulo 5 — Conclusão | ✅ Escrito nesta sessão |
| Referências Bibliográficas | ✅ Lista completa (38 referências) |
| Apêndice — Testes Econométricos | ✅ Notebook `.ipynb` gerado |
| Pipeline flowchart com correções | ✅ `.jsx` interativo gerado |

**Pendências críticas antes da defesa:**
1. Executar `14_2_4_KPI_Min_Var.ipynb` → preencher Vol, Sharpe, MDD nas Tabelas 4.5 e 5.1
2. Executar `14_1_4_KPI_Max_Sharpe.ipynb` → preencher Vol, Sharpe, MDD nas Tabelas 4.6 e 5.1
3. Corrigir `4_Calculo_Premio_Risco.ipynb` (parquet → csv) e reexecutar pipeline base
4. Padronizar período de backtest para jan/2015 em todas as estratégias

---

## Arquivos Gerados neste Projeto

| Arquivo | Descrição |
|---|---|
| `Entrega_10_Pedro_Reis_Estrutura_Corrigida.docx` | TCC com estrutura ABNT corrigida — base de trabalho |
| `Apendice_Testes_Econometricos.ipynb` | Notebook completo com todos os testes econométricos |
| `pipeline_correcoes.jsx` | Fluxograma interativo com bugs e correções por notebook |
| `tcc_workflow.jsx` | Fluxograma de progresso das tarefas por dia |
| `diagnostico_econometrico_130_ativos.csv` | Resultados dos testes para os 130 ativos |
| `Parecer_Testes_Econometricos_TCC.md` | Parecer sobre suficiência dos testes propostos |
| `Relatorio_Final_Sintese_TCC.md` | Síntese completa de todos os notebooks auditados |

---

## Estrutura do Documento (Entrega_10 — corrigida)

```
Capa (título: "Moderna Teoria das Carteiras...")
Resumo
Sumário  ← atualizar no Word: clicar → "Atualizar Tabela" → "Índice inteiro"
1. INTRODUÇÃO
2. REFERENCIAL TEÓRICO (2.1–2.22)
3. METODOLOGIA DA PESQUISA
   3.1 Natureza e Classificação da Pesquisa
   3.2 Universo, Amostra e Fonte dos Dados
   3.3 Tratamento e Preparação dos Dados
   3.4 Estimação dos Parâmetros de Otimização
   3.5 Modelos de Otimização Implementados
       3.5.1 Mínima Variância Global com L1
       3.5.2 Máximo Índice de Sharpe com L1
       3.5.3 Black-Litterman com Visões LSTM
   3.6 Protocolo de Backtesting (Janelas Expansivas)
   3.7 Métricas de Avaliação de Desempenho
4. RESULTADOS E DISCUSSÃO
   4.1 Estatísticas Descritivas e Diagnóstico Econométrico
   4.2 Resultados do Backtest Out-of-Sample (2015–2025)
       4.2.1 Mínima Variância L1 (+460%)
       4.2.2 Máximo Sharpe L1 (+240%)
       4.2.3 Black-Litterman + LSTM (+56%, MDD -93%)
   4.3 Análise Comparativa entre Estratégias  ← placeholder a preencher
5. CONCLUSÃO
CRONOGRAMA (sem número de capítulo)
REFERÊNCIAS (38 referências — lista completa gerada)
APÊNDICES A–J  ← K–P foram deletados (duplicatas)
```

---

## Estrutura de Diretórios

```
C:\VSCodeWorkspace\TCC_Escrito\
├── data\
│   ├── lista_economatica_dados_Jan_2010_Dezembro_2025.csv  ← preços brutos (sep=';' decimal=',')
│   ├── precos_sanitizada_v3.csv      ← após sanitização
│   ├── CDI_2010_2026.xlsx            ← taxa DI diária (~0.00037/dia = 9.3% a.a.)
│   ├── IBOV_2010_2026.xlsx           ← nível do índice
│   ├── SELIC_2010_2026.xlsx          ← taxa Selic diária
│   └── nefin_factors.csv             ← Rm_minus_Rf, SMB, HML, WML, IML
└── notebooks\
    ├── [1–9]    Pipeline base
    ├── [12–13]  Backtests HMM+EWMA
    ├── [14]     Backtests L1 Expansivo  ← resultados principais
    ├── [15]     CAPM e prior BL
    ├── [16–18]  Black-Litterman híbrido
    └── [19–20]  Métricas finais
```

---

## Pipeline Canônico — Ordem de Execução

### Fase 1 — Base (obrigatória para todas as estratégias)

| Notebook | Entrada | Saída | Status |
|---|---|---|---|
| `1_Sanitizacao_Dados.ipynb` | `lista_economatica...csv` | `precos_limpos_finais.csv` | ⚠️ IQR sobre preços (limitação documentada) |
| `2_1_Matriz_de_Retornos.ipynb` | `precos_limpos_finais.csv` | `matriz_retornos_simples_v2.csv`, `_logaritmicos_v2.csv` | ⚠️ Corrigir WEGE3_ → WEGE3 |
| `3_1_Merge_B3_CDI_SELIC.ipynb` | acima + excels | `base_mestre_consolidada_IBOV_CDI_SELIC.csv` | ✅ OK |
| `4_Calculo_Premio_Risco.ipynb` | `base_mestre...csv` | `matriz_premio_risco.csv` | 🔴 **Corrigir parquet→csv** |
| `5_Matriz_Covariancia_KPIs.ipynb` | `matriz_premio_risco.csv` | `matriz_covariancia_anualizada.csv`, `kpis_ativos_markowitz.csv` | ✅ OK (após n04 corrigido) |

### Fase 2 — Estratégia A: Mínima Variância L1 (resultado principal +460%)

| Notebook | Saída | Status |
|---|---|---|
| `14_2_1_Janelas_Expansivas_Min_Var.ipynb` | `historico_pesos_l1_5anos_M_min_var.parquet` | ⚠️ Verificar sep/decimal e data jan/2015 |
| `14_2_2_Backteste_Min_Var.ipynb` | `equity_curve_l1_min_var.png` (+460%) | ⚠️ Verificar shift(1) nos pesos |
| `14_2_3_Turnover_Min_Var.ipynb` | turnover 0.32%/mês | ✅ OK |
| `14_2_4_KPI_Min_Var.ipynb` | Vol, Sharpe, MDD | 🔴 **NÃO EXECUTADO — rodar agora** |

### Fase 3 — Estratégia B: Máximo Sharpe L1 (+240%)

| Notebook | Saída | Status |
|---|---|---|
| `14_1_1_Janelas_Expansivas_Max_Sharpe.ipynb` | `historico_pesos_l1_5anos_M_max_sharpe.parquet` | ⚠️ Verificar sep/decimal e data jan/2015 |
| `14_1_2_Backteste_Max_Sharpe.ipynb` | `equity_curve_l1_max_sharpe.png` (+240%) | ⚠️ Verificar shift(1) nos pesos |
| `14_1_3_Turnover_Max_Sharpe.ipynb` | turnover 4.29%/mês | ✅ OK |
| `14_1_4_KPI_Max_Sharpe.ipynb` | Vol, Sharpe, MDD | 🔴 **NÃO EXECUTADO — rodar agora** |

### Fase 4 — Estratégia C: Black-Litterman + LSTM (Sharpe -0.14, MDD -93%)

| Notebook | Saída | Status |
|---|---|---|
| `17_Extracao_Fatores_NEFIN.ipynb` | `fatores_nefin_limpos.csv` | ✅ OK |
| `2_Pesos_Mercado.ipynb` | `pesos_mercado_black_litterman.csv` | 🔴 Look-ahead bias (2026) + WEGE3_ |
| `15_CAPM_.ipynb` | — | 🔴 Crash: drop('Data') antes de set_index |
| `15_2_CAPM_Reverso_BL.ipynb` | delta = -0.0884 | 🔴 Inválido — usar delta=2.5 hardcoded |
| `4_Teste2_Janelas_Expansivas.ipynb` | `visoes_lstm_black_litterman_overnight.csv` | ⚠️ Scaler com look-ahead + WEGE3_ |
| `17_3_Black_Litterman_Hibrido_ff5.ipynb` | `historico_alocacao_lstm_ff5_overnight.csv` | 🔴 **sigma ×21 → ×252; delta=2.5** |
| `18_Calculo_Curva_Capital.ipynb` | curva de capital | ⚠️ Sem output confirmado |
| `19_Tabela_Metricas_Risco.ipynb` | `tabela_metricas_finais_tcc.csv` | ✅ Resultados válidos |

---

## ☠️ Notebooks Envenenados — Nunca Executar

```
4_1_Calculo_Premio_Risco_original.ipynb  → CDI implícito de ~160%/ano
5_Matriz_Covariância_KPIs_CAPM_original.ipynb  → KPIs inválidos
6_Fronteira_Eficiente.ipynb  → Sharpe da fronteira = -2.93 (CDI errado)
```

---

## Bugs Conhecidos e Correções Exatas

### Bug 1 — CRÍTICO: `4_Calculo_Premio_Risco.ipynb` lê parquet inexistente
```python
# REMOVER:
df_mestre = pd.read_parquet("...base_mestre_consolidada_IBOV_CDI_SELIC.parquet")
# SUBSTITUIR POR:
df_mestre = pd.read_csv("...base_mestre_consolidada_IBOV_CDI_SELIC.csv",
                        sep=';', decimal=',', index_col='Data', parse_dates=True)
```

### Bug 2 — CRÍTICO: sigma mensalizado no Black-Litterman (`17_3_...ipynb`)
```python
# REMOVER:
sigma_mensal = dados_janela.cov().values * 21
# SUBSTITUIR POR:
sigma_anual = dados_janela.cov().values * 252
```

### Bug 3 — CRÍTICO: delta negativo no CAPM reverso (`15_2_...ipynb`)
```python
# NÃO USAR o delta calculado (-0.0884). SUBSTITUIR por:
delta = 2.5  # He & Litterman (1999) — documentar como Limitação 2 no Cap. 5
```

### Bug 4 — Ticker WEGE3 com underscore (todos os notebooks)
```python
# Em qualquer notebook que use lista de ativos:
df.rename(columns={'WEGE3_': 'WEGE3'}, inplace=True)
# Em 2_Pesos_Mercado.ipynb:
ativos_yf = [f"{a.rstrip('_')}.SA" for a in lista_ativos]
```

### Bug 5 — `15_CAPM_.ipynb` crash no drop('Data')
```python
# REMOVER esta linha:
ibov = ibov.drop(columns=['Data'])
# O set_index('Data') logo abaixo já resolve
```

### Bug 6 — Look-ahead bias no scaler do LSTM (`4_Teste2...ipynb`)
```python
# ERRADO (ajusta com série completa):
scaler = MinMaxScaler().fit(serie_completa.reshape(-1,1))
# CORRETO (ajusta só com dados de treino):
scaler = MinMaxScaler().fit(dados_treino.reshape(-1,1))
dados_escalados = scaler.transform(serie_completa.reshape(-1,1))
```

### Bug 7 — Separador CSV nos notebooks de backtest
Verificar antes de executar `13`, `14_1_2`, `14_2_2`:
```bash
head -2 base_mestre_consolidada_IBOV_CDI_SELIC.csv
# Se colunas separadas por ';' → sep=';', decimal=','
# Se separadas por ',' → sep=',' (pandas padrão)
```

---

## Convenções Críticas do Projeto

### Retornos: qual usar onde
| Contexto | Tipo | Código |
|---|---|---|
| Otimização Markowitz | Simples | `df.pct_change()` |
| Backtesting (curva de capital) | Simples | `df.pct_change()` |
| Testes econométricos (ADF, ARCH) | Logarítmico | `np.log(df/df.shift(1))` |
| Estimação de média para BL prior | Simples | `df.pct_change().mean() * 252` |

### Look-ahead bias — regra inviolável
```python
# TODO cruzamento pesos × retornos DEVE ter shift(1):
pesos_diarios = df_pesos.reindex(df_ret.index).ffill().shift(1)
retorno_carteira = (pesos_diarios * df_ret).sum(axis=1)
```

### Anualização — sempre 252 dias úteis
```python
vol_anual  = ret_diario.std() * np.sqrt(252)
ret_anual  = ret_diario.mean() * 252
cov_anual  = ret_diario.cov() * 252   # nunca * 21
```

### Sanity checks rápidos
```python
# CDI diário correto: ~0.00037 (9.3% a.a.)
# Se CDI > 0.001 → bug do arquivo original

# Sharpe < -1 ou MDD < -50% → verificar arquivo de pesos lido

# Turnover > 20%/mês → penalidade L1 insuficiente
```

---

## Resultados Consolidados

> ⚠️ Períodos de início diferentes — comparação direta inválida até padronização para jan/2015

| Estratégia | Retorno | IBOV (mesmo período) | Sharpe | MDD | Turnover |
|---|---|---|---|---|---|
| **Min Variância L1** | **+460.20%** | +215.00% | a preencher | a preencher | 0.32% |
| Max Sharpe L1 | +240.09% | +215.00% | a preencher | a preencher | 4.29% |
| HMM+EWMA | +381.44% | +243.49% | n/d | n/d | 0.51% |
| BL+LSTM+FF5 | +56.48% | +243.49% | **-0.14** | **-92.99%** | ~55% |
| CDI (ref.) | +166–171% | — | — | — | — |

**Métricas "a preencher"**: executar `14_2_4` e `14_1_4` e atualizar Tabelas 4.5, 4.6 e 5.1 do TCC.

---

## Decisões Metodológicas Confirmadas

| Decisão | Escolha | Justificativa |
|---|---|---|
| Universo de ativos | 130 ativos com ≥95% de cobertura | Garante suficiência estatística |
| Tratamento de NaN | ffill + bfill | Pregões sem negociação mantêm último preço |
| Período out-of-sample | jan/2015 – dez/2025 | 5 anos de treino (2010–2014) |
| Janelas | Expansivas (não rolling) | Toda informação histórica disponível em cada ponto |
| Retornos p/ otimização | Simples (`pct_change`) | Aditividade transversal (propriedade de Markowitz) |
| Retornos p/ testes | Logarítmicos | Aditividade temporal, estacionaridade |
| Delta BL | 2.5 hardcoded | Delta calculado = -0.0884 (inválido); convenção He & Litterman |
| Sigma BL | Anualizado (×252) | Escala correta para o framework BL |
| Custo transacional | 0.5% sobre turnover | Penalidade L1 nos otimizadores |

---

## Execuções Longas

| Notebook | Tempo estimado | Observação |
|---|---|---|
| `4_Teste2_Janelas_Expansivas.ipynb` | 2–8h | LSTM 130 ativos — reiniciável (checkpoint em disco) |
| `5_LSTM_Treinamento_Janelas_expansivas.ipynb` | 4–12h | LSTM+FF5 — reiniciável |
| `14_1_1` e `14_2_1` | 10–20min | L1 expansivo, 132 períodos |
| `14_1_4` e `14_2_4` | 2–5min | Apenas cálculo de métricas — rodar hoje |

---

## Dependências e Ambiente

**Python recomendado:** 3.11.9 (TensorFlow/Keras não suporta 3.14 completamente)

```bash
pip install pandas numpy scipy matplotlib seaborn plotly
pip install scikit-learn tensorflow keras
pip install cvxpy hmmlearn statsmodels
pip install yfinance openpyxl pyarrow tabulate tqdm
```

**Solvers CVXPY:**
- Série 14 (L1): `cp.OSQP` com fallback `cp.ECOS`
- Série 17 (BL): `cp.CLARABEL`
- Série 12 (HMM): `cp.ECOS`

---

## Preferências de Trabalho com Claude

- **Sempre perguntar** antes de executar código: "Executar agora ou gerar como notebook `.ipynb`?"
- **Preferência padrão:** gerar como notebook `.ipynb` para editar e incluir nos apêndices
- Capítulos 3, 4, 5 e Referências já foram escritos — não reescrever, apenas ajustar trechos

---

## Referências Essenciais

- Black & Litterman (1992) — *Financial Analysts Journal* 48(5) — modelo central
- He & Litterman (1999) — Goldman Sachs WP — calibração delta/tau
- DeMiguel, Garlappi & Uppal (2009) — *RFS* 22(5) — por que Min Variância vence
- Markowitz (1952) — *Journal of Finance* 7(1) — fundação da MPT
- Ledoit & Wolf (2004) — *J. Multivariate Analysis* 88(2) — covariância robusta
- Rockafellar & Uryasev (2002) — *J. Banking & Finance* 26(7) — CVaR
- Santos & Tessari (2012) — *RBFin* 10(3) — otimização na B3
- Welch & Goyal (2008) — *RFS* 21(4) — por que LSTM não prevê retornos
- Campbell, Lo & MacKinlay (1997) — livro — econometria de mercados financeiros
