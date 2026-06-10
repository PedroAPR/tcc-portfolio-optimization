# Relatório do Estado Atual do Pipeline de Otimização de Carteiras B3

## A. Sumário do estado atual
O pipeline executa o processo completo de processamento quantitativo para o TCC: da conversão de planilhas Excel da B3 até o backtest de 16 estratégias de otimização (MPT vs. PMPT) e inferência estatística out-of-sample (2015–2025). O universo atual de ativos é de **102 ativos** (e não 113 como indicado no roteiro do prompt). Isso ocorre porque a Etapa VII (Classificador de Integridade v2) excluiu **16 ativos** a partir da lista inicial de 118 ativos pós-liquidez, e não 9 ativos. O pipeline foi re-executado por completo e todos os notebooks e saídas em disco estão sincronizados. A suíte de testes finais (`test_pipeline.py`) obteve aprovação em todos os 9 testes de consistência dimensional e financeira.

---

## B. Mapa do pipeline
A tabela a seguir apresenta o mapeamento de execução sequencial real do pipeline:

| Ordem | Arquivo | Propósito | Inputs | Outputs | Parâmetros-chave (valores) | Nº ativos | Re-executado? |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: |
| 1 | `01_01_convertendo_em_parquet_v3.ipynb` | Conversão Parquet | Planilhas `.xlsx` da B3 | `dados_brutos_economatica.parquet` | `max_workers = os.cpu_count()` | - | Sim (114.1s) |
| 2 | `02_01_consolidando_dados.ipynb` | Consolidação Dados | `dados_brutos_economatica.parquet` | `dados_brutos_economatica.parquet` | Consolidação temporal MultiIndex | - | Sim (25.7s) |
| 3 | `run_etapa03.py` (Etapa 3 unificada) | Orquestração local da liquidez e integridade | `dados_brutos_economatica.parquet` | `universo_pos_liquidez.csv`, `tickers_excluidos_integridade.csv`, `tickers_finais.csv`, `Matriz_precos_sanitizada.csv` | `PERCENTIL_LIQUIDEZ`: 0.1 (p10), `ANO_FORMACAO_ADTV`: 2010 | 118 (ADTV) $\rightarrow$ 102 (final) | Sim (42.8s) |
| 4 | `04_01_Taxas_Livres_Risco_SGS_Final.ipynb` | Taxas Livres Risco | BCB SGS API | `rf_diario.csv` | CDI e SELIC diários do Banco Central | - | Sim (73.1s) |
| 5 | `05_01_Alinhamento_e_Retornos.ipynb` | Alinhamento Retornos | `Matriz_precos_sanitizada.csv`, `rf_diario.csv` | `painel_alinhado.csv`, `retornos_simples.parquet`, `retornos_log.parquet` | `DATA_INICIO`: "2010-01-01", `DATA_FIM`: "2025-12-31" | 102 | Sim (14.4s) |
| 6 | `05_02_Saneamento_e_Winsorizacao.ipynb` | Saneamento e Winsorização | `retornos_simples.parquet` | `retornos_simples_saneado.parquet`, `retornos_log_saneado.parquet` | `K_MAD`: 3.5, `C_MAD`: 0.6745 | 102 | Sim (12.4s) |
| 7 | `06_01_Estimacao_LedoitWolf.ipynb` | Estimação Covariância | `retornos_simples_saneado.parquet` | `sigma_amostral_anual.parquet`, `sigma_ledoitwolf_anual.parquet` | `TRADING_DAYS`: 252 | 102 | Sim (10.8s) |
| 8 | `07_01_Otimizacao_Carteiras.ipynb` | Otimização Carteiras (Backtest) | `retornos_simples_saneado.parquet`, `sigma_ledoitwolf_anual.parquet` | `strategy_returns.parquet`, `desempenho_estrategias.parquet`, `pesos_historico.csv` | `WARMUP_MESES`: 60, `CUSTO_BPS`: 50.0, `ALPHA_PMPT`: 0.95, `TETO_PESO`: 0.1 | 102 | Sim (4221.5s) |
| 9 | `08_01_Fronteira_Eficiente.ipynb` | Fronteira Eficiente | `retornos_simples_saneado.parquet` | `fronteira_mv_pontos.csv`, `carteiras_canonicas.csv`, `fronteira_eficiente.png` | `N_MONTECARLO`: 50000 | 102 | Sim (148.6s) |
| 10 | `09_01_Inferencia_Econometrica.ipynb` | Inferência Econométrica | `strategy_returns.parquet` | `apendice_G_diagnostico_ibov.csv`, `apendice_H_testes_estrategia.csv` | `BOOTSTRAP_REPS`: 2000, `BOOTSTRAP_BLOCK_MEAN`: 10 | 102 | Sim (2862.0s) |

---

## C. Funil do universo
A filtragem do universo transcorre na Etapa 3 em 3 passagens orquestradas pelo `run_etapa03.py`:
1. **Universo Bruto Inicial:** 496 ativos (provenientes do consolidado Economática).
2. **Presença ≥ 95%:** Reduz de 496 para 135 ativos (361 reprovados).
3. **IPO Tardio / Integridade:** Reduz de 135 para 131 ativos (4 excluídos por histórico posterior a 2010).
4. **ADTV (Liquidez p10 em 2010):** Reduz de 131 para 118 ativos (13 reprovados por iliquidez).
5. **Classificador de Integridade (COTAHIST):** Reduz de 118 para **102 ativos** (16 excluídos devido a reorganizações societárias ou penny stocks ilíquidas recentes).

### Propagação do Universo nos Estágios a Jusante

| Estágio a jusante | Nº de ativos | Os 9 ausentes? (S/N) | Evidência |
| :--- | :---: | :---: | :--- |
| Matriz de preços sanitizada | 102 | S | `03_01c_Pos_Integridade.ipynb` (célula 10, linha 341) |
| Matriz de retornos simples/log saneados | 102 | S | `05_02_Saneamento_e_Winsorizacao.ipynb` (célula 8, linha 371) |
| Matriz de covariância (Ledoit-Wolf) | 102 | S | `06_01_Estimacao_LedoitWolf.ipynb` (célula 3, linha 295) |
| Vetor/Série de pesos históricos | 102 | S | `test_pipeline.py` (caso de teste 6, pesos de 102 ativos) |
| Resultados do backtest | 102 | S | `07_01_Otimizacao_Carteiras.ipynb` (célula 10, linha 722) |
| Testes econométricos | 102 | S | `09_01_Inferencia_Econometrica.ipynb` (células 11 e 12) |

Os 9 ativos mencionados no prompt (`FICT3, GOLL54, VSTE3, PDTC3, LIGT3, PMAM3, RPMG3, RSID3, ETER3`) estão **ausentes** de todos os estágios. Eles foram excluídos no Passo 3b pelo Classificador v2 (que exclui estes 9 mais 7 ativos adicionais: `AMER3, LUPA3, NEXP3, OIBR3, OIBR4, PDGR3, VIVR3`, totalizando 16 exclusões).

---

## D. Artefatos de dados em disco

| Arquivo | Tipo | Shape | Período (min→max) | Observação |
| :--- | :---: | :---: | :---: | :--- |
| `dados_brutos_economatica.parquet` | Parquet | (6507, 496) | 2010-01-04 $\rightarrow$ 2025-12-30 | Base consolidada crua (preço/volume) |
| `Matriz_precos_sanitizada.csv` | CSV/Parquet | (3967, 102) | 2010-01-04 $\rightarrow$ 2025-12-30 | Preços pós-filtro de liquidez e integridade |
| `rf_diario.csv` | CSV | (3967, 2) | 2010-01-04 $\rightarrow$ 2025-12-30 | CDI e SELIC diários do Banco Central |
| `retornos_simples_saneado.parquet` | Parquet | (3966, 102) | 2010-01-05 $\rightarrow$ 2025-12-30 | Retornos simples após winsorização |
| `retornos_log_saneado.parquet` | Parquet | (3966, 102) | 2010-01-05 $\rightarrow$ 2025-12-30 | Log-retornos após winsorização |
| `sigma_amostral_anual.parquet` | Parquet | (102, 102) | - | Matriz de covariância anualizada amostral |
| `sigma_ledoitwolf_anual.parquet` | Parquet | (102, 102) | - | Matriz de covariância regularizada |
| `strategy_returns.parquet` | Parquet | (2690, 17) | 2015-03-02 $\rightarrow$ 2025-12-30 | Retornos OOS de 16 estratégias + IBOV |
| `desempenho_estrategias.parquet` | Parquet | (17, 5) | - | Métricas de risco/retorno consolidadas |
| `pesos_historico.csv` | CSV | (55159, 4) | 2015-03-02 $\rightarrow$ 2025-12-30 | Histórico de pesos não-nulos por rebalanceamento |
| `fronteira_mv_pontos.csv` | CSV | (60, 2) | - | Curva de fronteira eficiente MPT |

---

## E. Parâmetros metodológicos realizados

1. **Janela de Estudo:** 2010-01-01 a 2025-12-31 (Evidência: `src/config.json`).
2. **Filtro de Presença:** Mínimo de 95% de pregões válidos (Evidência: `03_01a_Pre_Integridade.ipynb` : célula 2).
3. **Corte de Liquidez (ADTV):** P10 (10%) dos volumes negociados em 2010 (Evidência: `03_01a_Pre_Integridade.ipynb` : célula 2).
4. **Winsorização:** `K_MAD = 3.5` e `C_MAD = 0.6745` (Evidência: `05_02_Saneamento_e_Winsorizacao.ipynb` : célula 2).
5. **Período de Warmup do Backtest:** 60 meses (5 anos) para estimação da primeira carteira (Evidência: `07_01_Otimizacao_Carteiras.ipynb` : célula 9).
6. **Custo de Transação:** 50.0 bps (0,5%) descontado no dia de rebalanceamento (Evidência: `07_01_Otimizacao_Carteiras.ipynb` : célula 9).
7. **Limite de Concentração (CVM 175):** Máximo de 10% por emissor nas carteiras com sufixo `_c10` (Evidência: `07_01_Otimizacao_Carteiras.ipynb` : célula 8).
8. **Anualização:** Assumido 252 dias úteis por ano (Evidência: `utils.config_loader` / `CLAUDE.md`).
9. **Parâmetros do Bootstrap:** 2000 reamostragens com tamanho médio de bloco de 10 dias úteis (Evidência: `09_01_Inferencia_Econometrica.ipynb` : célula 2).

---

## F. Resultados-título atuais
Desempenho out-of-sample (líquido de custos) no período 2015-03-02 a 2025-12-30 (2.690 pregões, 130 rebalanceamentos):

| Estratégia | CAGR (ret_anual) | Volatilidade | Sharpe | Sortino | Max Drawdown | Turnover Anual |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **EqualWeight** | 13.91% | 19.56% | 0.2902 | 0.4027 | -35.54% | 0.8293 |
| **InvVol** | 14.65% | 18.90% | 0.3276 | 0.4554 | -34.28% | 0.7881 |
| **MinVar** | 13.00% | 12.95% | 0.2931 | 0.4003 | -25.05% | 0.8009 |
| **MinVar_c10** | 13.17% | 12.98% | 0.3044 | 0.4154 | -25.00% | 0.7856 |
| **MaxSharpe** | 13.96% | 17.54% | 0.3046 | 0.4302 | -22.76% | 1.2187 |
| **MaxSharpe_c10** | 12.99% | 16.54% | 0.2606 | 0.3649 | -23.89% | 1.5076 |
| **MaxOmega** | 10.71% | 21.23% | 0.1487 | 0.2103 | -30.67% | 2.2408 |
| **MaxSortino** | 13.53% | 17.79% | 0.2812 | 0.3973 | -23.26% | 1.3100 |
| **MaxKappa3** | 13.64% | 18.26% | 0.2843 | 0.4029 | -22.55% | 1.3375 |
| **MinCVaR** | 12.57% | 12.88% | 0.2644 | 0.3626 | -26.44% | 1.1056 |
| **MinCDaR** | 5.36% | 19.82% | -0.1050 | -0.1454 | -62.46% | 1.4735 |
| **BL_classico** | 24.31% | 25.97% | 0.6110 | 0.8902 | -38.93% | 7.9819 |
| **BL_classico_c10** | 20.44% | 20.20% | 0.5632 | 0.7916 | -33.60% | 6.2942 |
| **BL_downside** | 22.91% | 32.17% | 0.5138 | 0.7532 | -57.41% | 9.4819 |
| **BL_downside_c10** | 16.87% | 22.30% | 0.3951 | 0.5543 | -38.01% | 7.3287 |
| **IBOV** | 11.26% | 23.32% | 0.1777 | 0.2445 | -46.82% | - |
| **EqualWeight_BuyHold** | 17.28% | 19.28% | 0.4429 | 0.6206 | -33.00% | 0.0000 |

### Achado Central do TCC:
- **Black-Litterman clássico (BL_classico)** e sua versão restrita (**BL_classico_c10**) alcançaram o melhor Sharpe (+0.6110 e +0.5632, respectivamente) e retornos (24.31% e 20.44% a.a.) no período out-of-sample, com p-valores significativos a 5% em relação ao IBOVESPA ($p = 0.0417$ e $p = 0.0400$ no teste CAPM HAC, Newey-West). 
- O **EqualWeight_BuyHold** (sem rebalanceamento) superou o benchmark rebalanceado **EqualWeight** (Sharpe 0.4429 vs. 0.2902), impulsionado pela alta concentração em ativos de forte crescimento como `UNIP6` (que cresceu 79.5x e terminou com peso de 14.2% na carteira Buy & Hold).
- Estratégias puras de cauda como **MinCDaR** falharam no mercado brasileiro, obtendo Sharpe negativo (-0.1050) e alto drawdown (-62.46%).

---

## G. Discrepâncias, obsolescências e avisos

1. **Divergência Crítica de Escopo (Severidade: ALTA):** Mismatch entre o premissa do prompt (113 ativos, 9 exclusões) e a realidade executada dos arquivos (102 ativos, 16 exclusões). A realidade reflete o classificador refinado (v2). Os 9 ativos citados pelo usuário estão todos excluídos (bateram 100% de exclusão), porém 7 outros ativos de distress foram somados à lista por critérios objetivos.
2. **Aviso de Timeout (Severidade: MÉDIA):** O notebook de otimização de carteiras (`07_01_Otimizacao_Carteiras.ipynb`) levava ~79 minutos para rodar devido ao solver de LP de CDaR em janelas expansivas longas. Isso estourava o timeout do `nbconvert` padrão (1 hora). Foi corrigido aumentando os núcleos de paralelização para 6 e estendendo o timeout global no script para 2 horas.
3. **Aviso de Permissão do Windows (Severidade: MÉDIA):** Erros ocasionais de permissão de arquivo (`PermissionError: [WinError 32]`) ao tentar deletar notebooks temporários no Windows foram contornados na etapa 3 adicionando um laço de tentativas com delay no script `run_etapa03.py`.
4. **Sem Avisos/Erros de Execução (Severidade: BAIXA):** A suíte de testes finais rodou sem apresentar falhas, e não há outros avisos ou células com exceção.

---

## H. Log de evidências

- **Universo bruto de 496 ativos:** `src/03_Filtro_Liquidez/03_01a_Pre_Integridade.ipynb` (Célula 3)
- **Filtro de presença (135 ativos):** `src/03_Filtro_Liquidez/03_01a_Pre_Integridade.ipynb` (Célula 6)
- **Filtro de IPO (131 ativos):** `src/03_Filtro_Liquidez/03_01a_Pre_Integridade.ipynb` (Célula 7)
- **Filtro de ADTV (118 ativos):** `src/03_Filtro_Liquidez/03_01a_Pre_Integridade.ipynb` (Célula 8)
- **Exclusão de 16 ativos (universo final de 102 ativos):** `src/03_Filtro_Liquidez/03_01c_Pos_Integridade.ipynb` (Célula 10) e `src/11_Classificador_Integridade/Apendice_Classificador_Integridade_Universo_v2.ipynb` (Célula 9)
- **Matriz de preços sanitizada (102 ativos x 3967 pregões):** `src/03_Filtro_Liquidez/03_01c_Pos_Integridade.ipynb` (Célula 10)
- **Matriz de retornos simples/log (102 ativos x 3966 pregões):** `src/05_Alinhamento_Winsorizacao/05_02_Saneamento_e_Winsorizacao.ipynb` (Célula 10)
- **Espectro de autovalores de Ledoit-Wolf:** `src/06_Estimacao_Covariancia/06_01_Estimacao_LedoitWolf.ipynb` (Célula 3)
- **Rendimento das estratégias out-of-sample (2690 pregões):** `src/07_Otimizacao_Carteiras/07_01_Otimizacao_Carteiras.ipynb` (Células 10 e 11)
- **Bootstrap estatístico (B=2000):** `src/09_Inferencia_Econometrica/09_01_Inferencia_Econometrica.ipynb` (Célula 8)
- **CAPM HAC / Newey-West p-valores:** `src/09_Inferencia_Econometrica/09_01_Inferencia_Econometrica.ipynb` (Célula 10)

---

## I. NÃO VERIFICADO / Requer execução
Não há etapas de execução pendentes ou não verificadas no atual estado do repositório. Toda a cadeia do pipeline foi executada do início ao fim com cache atualizado, e os arquivos em disco correspondem fielmente às saídas salvas nas células dos notebooks. Qualquer modificação futura em parâmetros do `config.json` exigirá a invalidação do cache e nova re-execução.

---

## J. Sugestões

1. **Ajuste de Terminologia no TCC:** Recomenda-se atualizar a introdução do Capítulo 4 e 5 para explicitar o número de **102 ativos finais** (e **16 exclusões** de integridade) para alinhar a tese teórica com os resultados quantitativos reais em disco.
2. **Uso de Janela CDaR:** Para melhorar o desempenho computacional e mitigar drawdowns severos da estratégia CDaR, sugere-se a adoção opcional de um limite histórico recente no otimizador (ex: `janela_max = 756` dias úteis) em trabalhos futuros.
3. **Persistência de Paralelismo:** Manter o número de núcleos de processamento em 6 e o timeout de 2 horas para garantir que o pipeline possa ser executado sob demanda sem quebras no Windows.
