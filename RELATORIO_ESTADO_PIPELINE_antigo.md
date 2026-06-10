# RELATORIO_ESTADO_PIPELINE.md

**Gerado em:** 2026-06-07  
**Projeto:** TCC — Comparação MPT × PMPT na B3 (2010–2025)  
**Autor:** Pedro Augusto Pinheiro Reis, UFG  
**Raiz:** `C:\VSCodeWorkspace\1_TCC_Final\`  
**Branch:** `auditoria-tcc`

---

## A. Sumário do Estado Atual

O pipeline de 9 estágios + 2 apêndices para otimização de carteiras na B3 (2010–2025) foi re-executado sequencialmente. O funil de liquidez resultou em **118 ativos** investíveis (Etapa VI). Uma etapa de exclusão de integridade (Etapa VII) pretendia remover 9 tickers de situação especial, resultando em 109 ativos finais (ou 113, se baseada em um universo antigo de 122). No entanto, o classificador v2 gravou [tickers_excluidos_integridade.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/tickers_excluidos_integridade.csv) na raiz de `data/`, enquanto a Etapa 3 buscou o arquivo em `data/Tickers/`. Devido a esse erro de caminhos, a etapa de exclusão não foi aplicada, gerando um aviso no log e propagando o universo completo de 118 ativos (incluindo ETER3, FICT3, GOLL54, etc.) para todas as etapas a jusante (retornos, covariância, otimização, testes econométricos). O maior risco identificado é a falha catastrófica da estratégia MinCDaR (CAGR de -1.75% e Max Drawdown de -81.81%), indicando provável não convergência do solver.

---

## B. Mapa do Pipeline

| Ordem | Arquivo | Propósito | Inputs principais | Outputs principais | Parâmetros-chave (valores reais) | Nº ativos (saída) | Re-executado? |
|-------|---------|-----------|-------------------|--------------------|----------------------------------|-------------------|---------------|
| 01 | [01_01_convertendo_em_parquet_v3.ipynb](file:///C:/VSCodeWorkspace/1_TCC_Final/src/01_Conversao_Parquet/01_01_convertendo_em_parquet_v3.ipynb) | Converter planilhas Excel da Economatica para Parquet e CSV | 496 planilhas `.xlsx` em `data/dados_economatica/` | 496 Parquet + 496 CSV em `data/dados_economatica_tratados/` | Paralelismo: 8 processos (`worker.py`) | 496 | SIM (06/06 22:13) |
| 02 | [02_01_consolidando_dados.ipynb](file:///C:/VSCodeWorkspace/1_TCC_Final/src/02_Consolidacao_Dados/02_01_consolidando_dados.ipynb) | Consolidar dados individuais em painel MultiIndex | 496 Parquet da etapa 1 | `dados_brutos_economatica.parquet` e `.csv` (6507 × 992) | Colunas: [Fechamento, Volume$] × 496 tickers | 496 | SIM (06/06 22:13) |
| 03 | [03_01_Ingestao_Filtro_Liquidez_v3.ipynb](file:///C:/VSCodeWorkspace/1_TCC_Final/src/03_Filtro_Liquidez/03_01_Ingestao_Filtro_Liquidez_v3.ipynb) | Ingestão e aplicação dos filtros de presença, IPO, liquidez (ADTV) e integridade | Painel MultiIndex (NB02), `tickers_excluidos_integridade.csv` (não localizado) | [Matriz_precos_sanitizada.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Matriz_Precos/Matriz_precos_sanitizada.csv) (3967 × 118), [tickers_finais.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Tickers/tickers_finais.csv) | `LIMIAR_PRESENCA=0.95`, `PERCENTIL_LIQUIDEZ=0.10`, `ANO_FORMACAO_ADTV=2010` | 118 (Pretendido: 109/113) | SIM (06/06 22:14, com Aviso de arquivo ausente) |
| 04 | [04_01_Taxas_Livres_Risco_SGS_Final.ipynb](file:///C:/VSCodeWorkspace/1_TCC_Final/src/04_Taxas_Livres_Risco/04_01_Taxas_Livres_Risco_SGS_Final.ipynb) | Ingerir taxas livres de risco (CDI e Selic) via API BCB-SGS | API BCB (séries 12 e 11) | `cdi_diario_bcb_2010_atual.csv`, `selic_diario_bcb_2010_atual.csv` (4020 obs) | Período: 2010-01-01 → 2025-12-31 | N/A (taxas) | SIM (06/06 22:15) |
| 05.01 | [05_01_Alinhamento_e_Retornos.ipynb](file:///C:/VSCodeWorkspace/1_TCC_Final/src/05_Alinhamento_Winsorizacao/05_01_Alinhamento_e_Retornos.ipynb) | Alinhar preços temporalmente ao calendário e calcular retornos simples/log | `Matriz_precos_sanitizada.parquet`, CDI/Selic (NB04) | [painel_alinhado.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Painel_Dados/painel_alinhado.csv) (3967 × 121), `retornos_simples.csv` (3966 × 118), `retornos_log.csv` | Anualização: 252 dias úteis/ano. `EXCLUIR_PRECO_CORROMPIDO=false`, `LIMIAR_PRECO_MAX=1000.0` (Filtro VI desligado) | 118 | SIM (06/06 22:15) |
| 05.02 | [05_02_Saneamento_e_Winsorizacao.ipynb](file:///C:/VSCodeWorkspace/1_TCC_Final/src/05_Alinhamento_Winsorizacao/05_02_Saneamento_e_Winsorizacao.ipynb) | Winsorização MAD robusta condicional a não-nulos | `retornos_simples.parquet`, `retornos_log.parquet` | [retornos_simples_saneado.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Retornos/retornos_simples_saneado.csv) (3966 × 118), `retornos_log_saneado.csv` | `K_MAD=3.5`, `C_MAD=0.6745`, `MAD_SOBRE_NAO_NULOS=true`, `LIMITE_IMPOSSIVEL=1.0` (100% a.d.) | 118 | SIM (06/06 22:15) |
| 06 | [06_01_Estimacao_LedoitWolf.ipynb](file:///C:/VSCodeWorkspace/1_TCC_Final/src/06_Estimacao_Covariancia/06_01_Estimacao_LedoitWolf.ipynb) | Estimar retornos esperados, volatilidade e covariância Ledoit-Wolf | `retornos_simples_saneado.parquet` | [momentos_anuais.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Momentos/momentos_anuais.csv) (118 × 5), `mu_anual.csv`, `sigma_ledoitwolf_anual.csv` (118 × 118) | Anualização: ×252 (μ), ×√252 (σ), ×252 (Σ). Encolhimento na amostra completa delta = 0.0065 | 118 | SIM (06/06 22:15) |
| 07 | [07_01_Otimizacao_Carteiras.ipynb](file:///C:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/07_01_Otimizacao_Carteiras.ipynb) | Otimizar carteiras (MPT/PMPT/BL) e rodar backtest mensal out-of-sample | Momentos e covariância (NB06), `retornos_simples_saneado.parquet`, CDI (NB04) | [strategy_returns.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Estrategias/strategy_returns.csv) (2690 × 17), `desempenho_estrategias.csv`, [pesos_historico.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Estrategias/pesos_historico.csv) (60494 reg) | `WARMUP_MESES=60`, `CUSTO_BPS=50.0`, `TETO_PESO=0.10`, `ALPHA_PMPT=0.95`, `MAR_MODO="cdi"`, 15 estratégias otimizadas | 118 | SIM (06/06 23:49, tempo: 5625.11s) |
| 08 | [08_01_Fronteira_Eficiente.ipynb](file:///C:/VSCodeWorkspace/1_TCC_Final/src/08_Fronteira_Eficiente/08_01_Fronteira_Eficiente.ipynb) | Simular nuvem Monte Carlo e traçar fronteiras eficientes MV e CVaR | Momentos (NB06), `retornos_simples_saneado.parquet` | `fronteira_mv_pontos.csv` (60×2), `fronteira_cvar_pontos.csv` (30×2), `fronteira_eficiente.png` | `N_MONTECARLO=50000`, `N_PONTOS_FRONT=60`, `ATIVOS_NUVEM=10`, `DIRICHLET_ALPHA=0.3`, `SEED=42` | 118 | SIM (06/06 23:52) |
| 09 | [09_01_Inferencia_Econometrica.ipynb](file:///C:/VSCodeWorkspace/1_TCC_Final/src/09_Inferencia_Econometrica/09_01_Inferencia_Econometrica.ipynb) | Testes de hipóteses de Sharpe/Sortino via bootstrap e regressões CAPM/HAC | `strategy_returns.parquet` (NB07), retornos saneados (NB05.02) | `apendice_G_diagnostico_ibov.csv`, `apendice_H_testes_estrategia.csv`, `apendice_H_painel_metricas.csv` | `BOOTSTRAP_REPS=2000`, `BOOTSTRAP_BLOCK_MEAN=10`, `SPANNING_MAX_LAGS=5`, `SEED=42` | 17 estratégias | SIM (07/06 00:32) |
| A10 | [Apendice_Tratamento_COTAHIST.ipynb](file:///C:/VSCodeWorkspace/1_TCC_Final/src/10_Tratamento_COTAHIST_B3/Apendice_Tratamento_COTAHIST.ipynb) | Processar arquivos brutos COTAHIST da B3 (desconectado do principal) | Arquivos txt COTAHIST brutos | Tabelas de referência tratadas | N/A | N/A | SIM (06/06 05:36) |
| A11b | [Apendice_Classificador_Integridade_Universo_v2.ipynb](file:///C:/VSCodeWorkspace/1_TCC_Final/src/11_Classificador_Integridade/Apendice_Classificador_Integridade_Universo_v2.ipynb) | Classificador atualizado de integridade (Penny/RJ/Linhagem) | [universo_pos_liquidez.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Tickers/universo_pos_liquidez.csv) (anterior com 122 ativos), base COTAHIST | `classificacao_universo_v2.csv`, `tickers_excluidos_integridade.csv` (9 ativos), `tickers_finais_v2.csv` | `PISO_PRECO=1.00`, `PERCENTIL_ADTV=20`, `ANOS_RECENTES=[2023, 2024, 2025]` | 122 -> 113 / 9 | SIM (06/06 14:56, salvo na raiz de data/) |

---

## C. Funil do Universo

### C.1 Sequência das Etapas de Filtragem (Última Execução)

O funil metodológico foi executado no notebook `03_01_Ingestao_Filtro_Liquidez_v3.ipynb` na seguinte ordem de restrição:

1. **Universo Bruto Ingerido:** **496 ativos** (Consolidação de 496 planilhas individuais contendo séries de preços e volumes na B3).
2. **Filtro de Presença (IV):** **135 aprovados** (361 reprovados por apresentarem preços válidos em menos de 95% dos pregões da janela temporal 2010–2025).
3. **Filtro de Integridade/IPO tardio (V):** **131 aprovados** (4 reprovados por listagem posterior a 04/01/2010).
4. **Filtro de ADTV (VI):** **118 aprovados** (13 reprovados por volume financeiro médio diário em 2010 abaixo do percentil 10, com limiar de R$ 374.412,21/dia).
5. **Filtro de Integridade/RJ (VII) — Etapa Central:**
   - **Intencionado:** **109 ativos** (aplicando a exclusão de 9 tickers identificados por Penny Stock recorrente ou Recuperação Judicial pelo Classificador v2: ETER3, FICT3, GOLL54, LIGT3, PDTC3, PMAM3, RPMG3, RSID3, VSTE3).
   - **Realizado na Execução:** **118 ativos** (0 excluídos. O arquivo `tickers_excluidos_integridade.csv` não foi localizado na subpasta `data/Tickers/` e a etapa foi pulada com aviso).

*Nota sobre a discrepância:* O usuário reportou o funil como "122 para 113 ativos". Isso ocorreu porque em uma execução antiga e não-saneada, o filtro ADTV aprovava 122 ativos, e a exclusão de 9 resultaria em 113. Na re-execução atual, a liquidez ADTV aprovou 118 ativos, o que deveria resultar em 109 ativos finais após exclusão. Como a exclusão falhou, o pipeline executou com 118 ativos.

### C.2 Tabela de Propagação do Universo

| Estágio a jusante | Nº de ativos | Os 9 ausentes? (S/N) | Evidência |
|-------------------|--------------|----------------------|-----------|
| [tickers_finais.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Tickers/tickers_finais.csv) | 118 | **N** | O arquivo lista todos os 118 tickers investíveis; ETER3 (linha 35), FICT3 (linha 41) e GOLL54 (linha 47) estão listados. |
| [Matriz_precos_sanitizada.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Matriz_Precos/Matriz_precos_sanitizada.csv) | 118 | **N** | Arquivo tem 119 colunas (índice + 118 ativos). Os 9 tickers estão presentes no cabeçalho. |
| [retornos_simples_saneado.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Retornos/retornos_simples_saneado.csv) | 118 | **N** | Matriz com 119 colunas (índice + 118 ativos). Todos os 9 tickers possuem séries de retornos winsorizados. |
| [momentos_anuais.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Momentos/momentos_anuais.csv) | 118 | **N** | O arquivo contém 119 linhas (header + 118 ativos), calculando momentos para todos os excluídos. |
| [sigma_ledoitwolf_anual.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Momentos/sigma_ledoitwolf_anual.csv) | 118 × 118 | **N** | Matriz de dimensão 119 × 119 (inclui índice). Contém correlações e covariâncias para os 9 ativos. |
| [strategy_returns.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Estrategias/strategy_returns.csv) | 17 estratégias | Sim (indireto) | Matriz 2690 × 18 (index + 17 estratégias). As séries de retorno foram otimizadas sobre o universo com 118 ativos. |
| [pesos_historico.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Estrategias/pesos_historico.csv) | 118 ativos | **N** | Contém alocações em tickers excluídos. Ex: ETER3 (peso 0.008475 no EqualWeight, linha 35), FICT3 (peso 0.008475, linha 41) no rebalanceamento de 2015-03-02. |
| [apendice_H_testes_estrategia.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Estrategias/apendice_H_testes_estrategia.csv) | 16 estratégias | Sim (indireto) | As regressões CAPM e testes de spanning utilizam retornos históricos baseados no universo inflado de 118 ativos. |

---

## D. Artefatos de Dados em Disco

A tabela abaixo inventaria todos os arquivos de dados físicos localizados na pasta `data/` do projeto, registrando suas dimensões e datas:

| Arquivo | Tipo | Shape | Período (min → max) | Observação |
|---------|------|-------|---------------------|------------|
| [universo_pos_liquidez.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Tickers/universo_pos_liquidez.csv) | CSV | 118 × 1 | — | Universo investível exportado após ADTV na Etapa 3. |
| [tickers_finais.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Tickers/tickers_finais.csv) | CSV | 118 × 1 | — | Lista final gerada na Etapa 3 (contém os 118 ativos). |
| [tickers_excluidos_integridade.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/tickers_excluidos_integridade.csv) | CSV | 9 × 5 | — | Lista de exclusão gerada na raiz de `data/` pelo Classificador v2. |
| [Matriz_precos_sanitizada.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Matriz_Precos/Matriz_precos_sanitizada.csv) | CSV | 3967 × 118 | 2010-01-04 → 2025-12-30 | Preços das ações; 982 NaNs preenchidos por forward fill. |
| [painel_alinhado.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Painel_Dados/painel_alinhado.csv) | CSV | 3967 × 121 | 2010-01-04 → 2025-12-30 | 118 ativos + IBOV + CDI + SELIC alinhados temporalmente. |
| [retornos_simples_saneado.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Retornos/retornos_simples_saneado.csv) | CSV | 3966 × 118 | 2010-01-05 → 2025-12-30 | Retornos saneados via winsorização robusta. |
| [momentos_anuais.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Momentos/momentos_anuais.csv) | CSV | 118 × 5 | — | Momentos anualizados (μ, σ, Sharpe, assimetria, curtose). |
| [sigma_ledoitwolf_anual.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Momentos/sigma_ledoitwolf_anual.csv) | CSV | 118 × 118 | — | Matriz de covariância regularizada Ledoit-Wolf anualizada. |
| [strategy_returns.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Estrategias/strategy_returns.csv) | CSV | 2690 × 17 | 2015-03-02 → 2025-12-30 | Séries temporais de retornos OOS das 17 estratégias, líquidas de custos. |
| [desempenho_estrategias.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Estrategias/desempenho_estrategias.csv) | CSV | 17 × 6 | — | Métricas consolidadas (CAGR, Vol, Sharpe, Sortino, MaxDD, Turnover). |
| [pesos_historico.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Estrategias/pesos_historico.csv) | CSV | 60494 × 4 | 2015-03-02 → 2025-12-30 | Histórico completo de pesos mensais por estratégia. |
| [fronteira_mv_pontos.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Estrategias/fronteira_mv_pontos.csv) | CSV | 60 × 2 | — | 60 pontos vol × ret para a fronteira Média-Variância. |
| [fronteira_cvar_pontos.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Estrategias/fronteira_cvar_pontos.csv) | CSV | 30 × 2 | — | 30 pontos CVaR × ret para a fronteira Média-CVaR. |
| [apendice_H_testes_estrategia.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Estrategias/apendice_H_testes_estrategia.csv) | CSV | 16 × 10 | — | Estatísticas econométricas HAC e CAPM de significância. |
| [apendice_H_painel_metricas.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Estrategias/apendice_H_painel_metricas.csv) | CSV | 17 × 6 | — | Métricas de performance líquidas incluindo IBOVESPA. |

---

## E. Parâmetros Metodológicos Realizados

- **Período de estudo:** 01/01/2010 a 31/12/2025 (Evidência: `config.json` : `DATA_INICIO`, `DATA_FIM` | Stage 3 Célula 2)
- **Pregões da janela:** 3.967 pregões válidos após remoção de fins de semana (Evidência: Stage 3 Célula 5)
- **Assunção de dias úteis/ano:** 252 (Evidência: Stage 5.01 Célula 6)
- **Filtro de presença mínima:** >=95% de observações não-nulas (Evidência: `config.json` : `LIMIAR_PRESENCA=0.95` | Stage 3 Célula 2)
- **Liquidez ADTV (formação):** volume mediano diário em 2010 acima do percentil 10 (p10). Limiar = R$ 374.412,21/dia (Evidência: `config.json` : `PERCENTIL_LIQUIDEZ`, `ANO_FORMACAO_ADTV` | Stage 3 Célula 8)
- **Filtro de IPO tardio:** exclusão de listados após 04/01/2010 (Evidência: Stage 3 Célula 7)
- **Multiplicador MAD winsorização (k):** 3,5 (Evidência: `config.json` : `K_MAD` | Stage 5.02 Célula 1)
- **Fator Gaussiano winsorização (c):** 0,6745 (Evidência: `config.json` : `C_MAD` | Stage 5.02 Célula 1)
- **Winsorização condicional a não-zero:** ativada para evitar sobre-winsorização (Evidência: `config.json` : `MAD_SOBRE_NAO_NULOS` | Stage 5.02 Célula 4)
- **Winsorização total realizada:** 9.207 observações clipadas (0,23% da amostra) (Evidência: Stage 5.02 Célula 4)
- **Warm-up para estimação:** 60 meses = 5 anos (Evidência: `config.json` : `WARMUP_MESES` | Stage 7 Célula 2)
- **Período out-of-sample (backtest):** 02/03/2015 a 30/12/2025 (2.690 dias úteis, 130 rebalanceamentos) (Evidência: Stage 7 Célula 10)
- **Frequência de rebalanceamento:** mensal (Evidência: Stage 7 Célula 10)
- **Custo de transação:** 50 bps por movimentação (Evidência: `config.json` : `CUSTO_BPS` | Stage 7 Célula 2)
- **Teto de peso individual (CVM 175):** 10% de alocação por emissor (Evidência: `config.json` : `TETO_PESO` | Stage 7 Célula 2)
- **Nível de confiança CVaR e CDaR:** 95% (Evidência: `config.json` : `ALPHA_PMPT` | Stage 7 Célula 2)
- **Taxa livre de risco diária (MAR):** CDI diário (Evidência: `config.json` : `MAR_MODO` | Stage 7 Célula 2)
- **Seed de reprodutibilidade:** 42 (Evidência: `config.json` : `SEED` | Stage 8 Célula 5, Stage 9 Célula 2)
- **Simulações de Monte Carlo (fronteira):** 50.000 carteiras simuladas sobre 10 ativos (Evidência: `config.json` : `N_MONTECARLO`, `ATIVOS_NUVEM` | Stage 8 Célula 4)
- **Concentração Dirichlet (Monte Carlo):** 0,3 (Evidência: `config.json` : `DIRICHLET_ALPHA` | Stage 8 Célula 1)
- **Replicações bootstrap (Sharpe/Sortino):** 2.000 (Evidência: `config.json` : `BOOTSTRAP_REPS` | Stage 9 Célula 2)
- **Bloco médio do bootstrap circular:** 10 dias (Evidência: `config.json` : `BOOTSTRAP_BLOCK_MEAN` | Stage 9 Célula 2)
- **Lags máximos HAC Newey-West:** 5 lags (Evidência: `config.json` : `SPANNING_MAX_LAGS` | Stage 9 Célula 2)

---

## F. Resultados-Título Atuais

### F.1 Métricas de Performance Out-of-Sample (Líquidas de Custos)

Período OOS: **02/03/2015 a 30/12/2025** (2.690 dias úteis, 130 rebalanceamentos). Parâmetros: Warm-up = 60m, Custo = 50 bps, Limite de peso = 10% (CVM 175). Benchmark livre de risco: CDI.

| Estratégia | Tipo | CAGR (% a.a.) | Vol (% a.a.) | Sharpe | Sortino | Max DD (%) | Turnover p.a. |
|------------|------|---------------|--------------|--------|---------|------------|---------------|
| EqualWeight | Benchmark | 5,97 | 19,84 | -0,0754 | -0,1025 | -41,97 | 0,91 |
| **EqualWeight_BuyHold** | Benchmark | **15,71** | 19,30 | **0,3724** | **0,5195** | -34,50 | 0,00 |
| InvVol | MPT | 9,16 | 19,11 | 0,0696 | 0,0953 | -37,35 | 0,84 |
| MinVar | MPT | 11,89 | 12,96 | 0,2169 | 0,2947 | -25,62 | 0,81 |
| MinVar_c10 | MPT (CVM175) | 11,93 | 12,99 | 0,2195 | 0,2979 | -25,63 | 0,80 |
| MaxSharpe | MPT | 13,60 | 17,53 | 0,2866 | 0,4044 | -22,76 | 1,22 |
| MaxSharpe_c10 | MPT (CVM175) | 12,66 | 16,55 | 0,2433 | 0,3404 | -23,90 | 1,51 |
| MaxOmega | PMPT | 9,82 | 21,21 | 0,1109 | 0,1566 | -30,61 | 2,29 |
| MaxSortino | PMPT | 13,16 | 17,78 | 0,2630 | 0,3713 | -23,26 | 1,32 |
| MaxKappa3 | PMPT | 13,32 | 18,26 | 0,2687 | 0,3806 | -22,55 | 1,35 |
| MinCVaR | PMPT | 11,85 | 12,96 | 0,2142 | 0,2929 | -26,26 | 1,24 |
| **MinCDaR** | PMPT | **-1,75** | 21,09 | **-0,4172** | **-0,5648** | **-81,81** | 1,53 |
| BL_classico | Black-Litterman | 21,12 | 25,99 | 0,5108 | 0,7395 | -43,78 | 8,25 |
| **BL_classico_c10** | BL (CVM175) | **17,99** | 20,30 | **0,4602** | **0,6434** | -34,33 | 6,46 |
| BL_downside | BL downside | 20,66 | 32,36 | 0,4556 | 0,6661 | -59,82 | 9,90 |
| BL_downside_c10 | BL downside (CVM175) | 14,45 | 22,32 | 0,3012 | 0,4210 | -37,13 | 7,81 |
| IBOVESPA | Benchmark mercado | 11,26 | 23,32 | 0,1777 | 0,2445 | -46,82 | N/A |

*Fonte dos dados:* [desempenho_estrategias.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Estrategias/desempenho_estrategias.csv) e [apendice_H_painel_metricas.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Estrategias/apendice_H_painel_metricas.csv).

### F.2 Significância e Diagnósticos Econométricos (HAC Newey-West)

Mapeamento de alfas, betas, testes de spanning e estatística Jobson-Korkie/Memmel comparada com o IBOVESPA:

| Estratégia | CAPM alfa (% a.a.) | CAPM beta | CAPM t-stat (NW) | CAPM p-valor | JK/Memmel z | JK/Memmel p | Spanning F | Spanning p |
|------------|---------------------|-----------|------------------|--------------|-------------|-------------|------------|------------|
| EqualWeight | -4,69 | 0,770 | -1,68 | 0,0933 | -1,90 | 0,0579 | 26,49 | < 0,001 |
| **EqualWeight_BuyHold** | **+4,06** | 0,755 | **+1,65** | 0,0980 | +1,52 | 0,1293 | 26,62 | < 0,001 |
| InvVol | -1,77 | 0,749 | -0,70 | 0,4838 | -0,85 | 0,3942 | 28,95 | < 0,001 |
| MinVar | +1,00 | 0,437 | +0,42 | 0,6773 | +0,20 | 0,8444 | 1013,65 | < 0,001 |
| MinVar_c10 | +1,01 | 0,445 | +0,43 | 0,6702 | +0,22 | 0,8294 | 942,10 | < 0,001 |
| MaxSharpe | +2,68 | 0,567 | +0,77 | 0,4388 | +0,51 | 0,6121 | 147,87 | < 0,001 |
| MaxSharpe_c10 | +1,72 | 0,558 | +0,55 | 0,5797 | +0,33 | 0,7432 | 216,22 | < 0,001 |
| MaxOmega | -0,53 | 0,696 | -0,13 | 0,8974 | -0,32 | 0,7504 | 48,61 | < 0,001 |
| MaxSortino | +2,32 | 0,569 | +0,65 | 0,5137 | +0,39 | 0,6958 | 135,45 | < 0,001 |
| MaxKappa3 | +2,54 | 0,570 | +0,68 | 0,4985 | +0,40 | 0,6867 | 117,21 | < 0,001 |
| MinCVaR | +1,04 | 0,418 | +0,43 | 0,6702 | +0,17 | 0,8652 | 988,39 | < 0,001 |
| **MinCDaR** | **-11,38** | 0,622 | **-2,28** | 0,0224 | -2,46 | 0,0140 | 96,01 | < 0,001 |
| **BL_classico** | **+10,53** | 0,663 | **+1,64** | 0,1007 | +1,21 | 0,2270 | 83,98 | < 0,001 |
| **BL_classico_c10** | **+6,67** | 0,646 | **+1,57** | 0,1163 | +1,28 | 0,1991 | 111,76 | < 0,001 |
| BL_downside | +11,66 | 0,745 | +1,39 | 0,1656 | +0,94 | 0,3453 | 31,68 | < 0,001 |
| BL_downside_c10 | +3,74 | 0,720 | +0,81 | 0,4207 | +0,57 | 0,5667 | 49,83 | < 0,001 |

*Fonte dos dados:* [apendice_H_testes_estrategia.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Estrategias/apendice_H_testes_estrategia.csv).

---

## G. Discrepâncias, Obsolescências e Avisos

| # | Severidade | Descrição | Evidência |
|---|-----------|-----------|-----------|
| G1 | **ALTA** | **Quebra de propagação de integridade:** O classificador v2 gravou o arquivo `tickers_excluidos_integridade.csv` na raiz de `data/`, mas a Etapa 3 de Ingestão de Liquidez procurou o arquivo sob `data/Tickers/`. Como o arquivo não existia naquele diretório, a etapa de exclusão foi pulada com aviso, gerando a matriz final com 118 ativos. Todos os arquivos a jusante herdaram esse universo inflado de 118 colunas. | [03_01_Ingestao_Filtro_Liquidez_v3.ipynb](file:///C:/VSCodeWorkspace/1_TCC_Final/src/03_Filtro_Liquidez/03_01_Ingestao_Filtro_Liquidez_v3.ipynb) : Célula 9 stdout ("tickers_excluidos_integridade.csv não encontrado") e código (linha 522). |
| G2 | **ALTA** | **Divergência de universo no TCC:** O prompt cita que o universo mudou de "122 para 113 ativos". No entanto, na execução física, o filtro ADTV resultou em 118 ativos (e não 122). Se a exclusão de 9 ativos por integridade tivesse funcionado, o universo real final seria de **109 ativos** (e não 113). Portanto, a carteira de 118 ativos atual contém 9 tickers reprovados a mais do que o esperado. | [Apendice_Classificador_Integridade_Universo_v2.ipynb](file:///C:/VSCodeWorkspace/1_TCC_Final/src/11_Classificador_Integridade/Apendice_Classificador_Integridade_Universo_v2.ipynb) Célula 2 stdout (`Universo: 122`) vs [03_01_Ingestao_Filtro_Liquidez_v3.ipynb](file:///C:/VSCodeWorkspace/1_TCC_Final/src/03_Filtro_Liquidez/03_01_Ingestao_Filtro_Liquidez_v3.ipynb) Célula 9 stdout (`ADTV: 118`). |
| G3 | **MÉDIA** | **Falha severa do otimizador MinCDaR:** O portfólio MinCDaR gerou retornos acumulados negativos com CAGR de -1.75%, Max Drawdown de -81.81% e Sharpe negativo de -0.4172. Essa performance discrepante (outlier absoluto negativo do backtest) aponta para não convergência do solver SCS/CLARABEL do CVXPY para restrições de drawdown acumulado em momentos de estresse na B3. | [desempenho_estrategias.csv](file:///C:/VSCodeWorkspace/1_TCC_Final/data/Estrategias/desempenho_estrategias.csv) linha 12. |
| G4 | **MÉDIA** | **Obsolescência do cache de orquestração:** O arquivo `.pipeline_cache.json` possui data de modificação antiga (03/06/2026) e não contém a chave para `09_Inferencia_Econometrica`. Adicionalmente, o script de execução forçada `run_pipeline_force.py` ignora o cache e não o atualiza, fazendo com que execuções subsequentes do orquestrador padrão sempre rodem a inferência econométrica do zero (overhead de ~40 minutos de bootstrap). | LastWriteTime de `src/.pipeline_cache.json` (03/06/2026 20:20:34) vs [run_pipeline_force.py](file:///C:/VSCodeWorkspace/1_TCC_Final/src/run_pipeline_force.py) código (sem gravação de cache). |
| G5 | **MÉDIA** | **Viés de sobrevivência passiva no EW_BuyHold:** O Sharpe de EqualWeight_BuyHold (0.3724) supera amplamente a carteira EqualWeight rebalanceada mensalmente (-0.0754) e todas as estratégias MPT ativas. Esse resultado não indica "habilidade", mas sim concentração passiva extrema no papel UNIP6 (que subiu 79.52x, terminando com peso de 14.20% no portfólio), distorcendo a comparação como um benchmark "passivo". | [07_01_Otimizacao_Carteiras.ipynb](file:///C:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/07_01_Otimizacao_Carteiras.ipynb) Célula 12 stdout. |
| G6 | **BAIXA** | **Filtro de Preço Corrompido desativado:** O notebook 5.01 indica que o toggle `EXCLUIR_PRECO_CORROMPIDO` está `False`, de forma que ativos com variações extremas causadas por grupamentos/splits desalinhados (ex: PDGR3, OIBR3, LUPA3) foram mantidos integralmente no painel de retornos, adicionando volatilidade artificial. | [05_01_Alinhamento_e_Retornos.ipynb](file:///C:/VSCodeWorkspace/1_TCC_Final/src/05_Alinhamento_Winsorizacao/05_01_Alinhamento_e_Retornos.ipynb) Célula 3 stdout. |
| G7 | **BAIXA** | **Notebooks apêndices desconectados:** Os notebooks 10 (Tratamento COTAHIST) e 11 (Classificador de Integridade) não estão mapeados nas dependências do orquestrador `run_pipeline.py`, exigindo execução manual paralela. | [run_pipeline.py](file:///C:/VSCodeWorkspace/1_TCC_Final/src/run_pipeline.py) (ausência de referências a NB10 e NB11). |

---

## H. Log de Evidências

- **Universo investível pré-integridade (118 ativos):** `src/03_Filtro_Liquidez/03_01_Ingestao_Filtro_Liquidez_v3.ipynb` : Célula 8 e Célula 9, stdout.
- **Aviso de ausência do arquivo de integridade:** `src/03_Filtro_Liquidez/03_01_Ingestao_Filtro_Liquidez_v3.ipynb` : Célula 9, stdout.
- **Caminho de gravação de saída no Classificador v2:** `src/11_Classificador_Integridade/Apendice_Classificador_Integridade_Universo_v2.ipynb` : Célula 5, código (linha 378: `PASTA_SAIDA / "tickers_excluidos_integridade.csv"`) e stdout (linha 365: `Gravado em C:\VSCodeWorkspace\1_TCC_Final\data`).
- **Caminho de leitura esperado pela Ingestão de Liquidez:** `src/03_Filtro_Liquidez/03_01_Ingestao_Filtro_Liquidez_v3.ipynb` : Célula 9, código (linha 522: `caminho_excl = DIR_TICKERS / "tickers_excluidos_integridade.csv"`, onde `DIR_TICKERS` é `data/Tickers`).
- **Dimensões do painel alinhado (3967 × 121):** `src/05_Alinhamento_Winsorizacao/05_01_Alinhamento_e_Retornos.ipynb` : Célula 5, stdout.
- **Dimensões e total de observações clipadas na winsorização (9207 obs):** `src/05_Alinhamento_Winsorizacao/05_02_Saneamento_e_Winsorizacao.ipynb` : Células 2 e 4, stdout.
- **T/N e condicionamento da covariância Ledoit-Wolf:** `src/06_Estimacao_Covariancia/06_01_Estimacao_LedoitWolf.ipynb` : Células 1, 3 e 5, stdout.
- **Parâmetros e tempo do backtest out-of-sample (5625.11s):** `src/07_Otimizacao_Carteiras/07_01_Otimizacao_Carteiras.ipynb` : Células 2 e 10, stdout.
- **CAGR, Max Drawdown e Sharpe das estratégias:** `data/Estrategias/desempenho_estrategias.csv` e `data/Estrategias/apendice_H_painel_metricas.csv`.
- **Top crescimento acumulado EW_BuyHold (UNIP6, 79.52x):** `src/07_Otimizacao_Carteiras/07_01_Otimizacao_Carteiras.ipynb` : Célula 12, stdout.
- **MVP e Tangente vol e ret da fronteira:** `src/08_Fronteira_Eficiente/08_01_Fronteira_Eficiente.ipynb` : Célula 5, stdout.
- **Parâmetros econométricos HAC e testes CAPM de estratégias:** `data/Estrategias/apendice_H_testes_estrategia.csv` e `src/09_Inferencia_Econometrica/09_01_Inferencia_Econometrica.ipynb` : Célula 10, stdout.
- **Diferenças de Sharpe e Sortino corrigidas por bootstrap Holm:** `src/09_Inferencia_Econometrica/09_01_Inferencia_Econometrica.ipynb` : Células 13 e 14, stdout.
- **Ausência de gravação de cache no orquestrador de força:** `src/run_pipeline_force.py` : Código da etapa loop (linhas 128-134).

---

## I. NÃO VERIFICADO / Requer Execução

| Item | Motivo |
|------|--------|
| **Visualização real das imagens de fronteiras eficientes** | Os arquivos `fronteira_eficiente.png` e `.svg` existem na pasta `data/Estrategias/`, mas por restrição de ambiente de leitura puramente textual, a validade visual e legenda das curvas plotadas não podem ser verificadas. |
| **Integridade matemática total do forward-fill** | A confirmação de que todos os 982 NaNs preenchidos na matriz de preços representam os últimos preços reais válidos de fechamento exigiria re-execução paralela de scripts de controle. |
| **Logs de iteração detalhados do solver para MinCDaR** | A causa exata da falha de convergência ou drawdown extremo da carteira MinCDaR exige re-executar a otimização com a flag `verbose=True` ativada no solver. |
| **Sucesso na suíte de testes de integração** | O sucesso das asserções e testes unitários localizados em `tests/` necessita da execução explícita de `python -m pytest tests/` no console (não permitido em modo somente leitura). |

---

## J. Sugestões

1. **Correção imediata de diretórios:** Alterar a definição de `PASTA_SAIDA` na linha 41 do notebook `Apendice_Classificador_Integridade_Universo_v2.ipynb` para apontar diretamente para a pasta de Tickers (`Path(r"C:\VSCodeWorkspace\1_TCC_Final\data\Tickers")`) de modo a gravar `tickers_excluidos_integridade.csv` no local correto, ou ajustar a variável `caminho_excl` na Etapa 3 para apontar para a raiz de `data/`.
2. **Re-execução de higienização do pipeline:** Após a correção dos caminhos, re-executar todo o pipeline para expurgar de ponta a ponta os 9 ativos excluídos e obter os resultados corretos baseados em **109 ativos**.
3. **Mapeamento de cache para Stage 9:** Adicionar a etapa `09_Inferencia_Econometrica` na escrita de cache do script de orquestração `run_pipeline.py`, e adicionar a escrita de cache no `run_pipeline_force.py` para evitar processamento bootstrap econométrico desnecessário de 40 minutos em execuções de checagem.
4. **Verificação do Solver MinCDaR:** Modificar a tolerância de convergência do solver CVXPY na etapa de CDaR ou restringir o solver para `CLARABEL` com parâmetros de barreira modificados para assegurar a corretude e convergência do problema.
5. **Correção textual do TCC:** Alinhar as referências ao funil de universo no texto do TCC para os números reais da B3 (118 antes da integridade, 109 final) a fim de refletir os dados reais da base Economatica e evitar inconsistências com a realidade do repositório.
