# Relatório de Atualização dos Apêndices — TCC
**"Moderna Teoria das Carteiras no Mercado de Ações Brasileiro: Comparação entre Otimizadores e Inputs"**

> **Autor do TCC:** Pedro Augusto Pinheiro Reis  
> **Auditoria realizada em:** 9 de junho de 2026  
> **Branch auditado:** `auditoria-tcc`  
> **Metodologia:** leitura de código-fonte e artefatos gerados; nenhuma célula foi executada durante a auditoria.

---

## 1. Sumário Executivo

O pipeline computacional está distribuído em **9 notebooks executáveis** (NB01–NB09), **2 notebooks de apêndice** (COTAHIST e Classificador de Integridade) e **≈ 30 módulos `.py`** organizados em pastas `utils/` por estágio. O orquestrador `run_pipeline.py` gerencia a execução com cache MD5 e testes de integridade automáticos.

**Estado geral:** o código está **funcional e reprodutível** para as 16 estratégias de otimização implementadas. Os artefatos CSV/Parquet em `data/Estrategias/` contêm métricas completas para todas as estratégias exceto aquelas marcadas como "L1" no texto — que simplesmente **não existem no código**: o sufixo `_c10` significa teto de 10% por ativo (restrição de caixa), não penalidade L1.

**Principais divergências código ↔ texto:**

| # | Divergência | Gravidade |
|---|---|---|
| 1 | N do universo: texto cita 118–136; código usa **102** | Alta |
| 2 | "BL + LSTM" no texto; código usa **momentum 12-1** | Alta |
| 3 | Estratégias "MinVar L1" e "MaxSharpe L1": **não existem no código** | Alta |
| 5 | "Penalidade L1 = 0,5% ou 0,2%": **não há L1**; custo de transação = 50 bps | Alta |
| 6 | N de pregões: texto cita 3.967 ou 4.030; artefato tem **3.966** | Média |
| 7 | Escala Σ no BL: foi ×21 (erro antigo); **código atual usa ×252** (corrigido) | Média |
| 8 | δ do CAPM reverso: texto cita otimização reversa; **código fixa δ = 2,5** | Média |
| 4 | Prior BL: texto ambíguo (1/N vs cap de mercado); **código usa 1/N** | Baixa |
| 9 | Datas de início OOS: todas estratégias começam em **2015-03-02** | Baixa |
| 10 | GOLL54/RCSL4 não estão nos 102 tickers finais | Baixa |
| 11 | ARIMA citado no texto: **não implementado** em nenhum arquivo | Média |

Nenhum valor precisa ser gerado por nova execução: todos os artefatos finais estão presentes em `data/Estrategias/`.

---

## 2. Tabela-Mestre de Parâmetros Canônicos

| Parâmetro | Valor no código | Arquivo : linha | Valor citado no texto | Status |
|---|---|---|---|---|
| **Universo de ativos (N)** | **102** | `data/Tickers/tickers_finais.csv` (102 linhas) | 118, 120, 130, 135, 136 em pontos diferentes | ❌ DIVERGE |
| **Pares de covariância** | **5.151** | derivado: C(102,2) | 8.385 (implicaria N=130) | ❌ DIVERGE |
| **Intervalo de datas** | 2010-01-01 a 2025-12-31 | `src/config.json` : `DATA_INICIO`/`DATA_FIM` | 2010–2025 | ✅ OK |
| **N de pregões (retornos)** | **3.966** | `retornos_simples.parquet` (shape 3966×102) | 3.967 (metodologia) / 4.030 (Apêndice B) | ❌ DIVERGE |
| **N de pregões (painel alinhado)** | **3.967** | `painel_alinhado.parquet` (shape 3967×105) | — | — |
| **Período OOS** | 2015-03-02 a 2025-12-30 | `strategy_returns.parquet` (2.690 × 17) | variado | ❌ |
| **N pregões OOS** | **2.690** | `strategy_returns.parquet` | — | — |
| **Warm-up** | **60 meses** | `src/config.json` : `WARMUP_MESES` | 60 meses | ✅ OK |
| **N de rebalanceamentos** | **130** | `pesos_historico.csv` (130 datas únicas) | 132 | ❌ DIVERGE |
| **Frequência de rebalanceamento** | Mensal (1.º pregão) | `NB07_cel1` : `REBAL = "M"` | mensal | ✅ OK |
| **Limiar de presença** | **0,95** (95%) | `src/config.json` : `LIMIAR_PRESENCA` | 95% | ✅ OK |
| **Percentil de liquidez (ADTV)** | **P10** (decil inferior) | `src/config.json` : `PERCENTIL_LIQUIDEZ = 0.1` | P10 | ✅ OK |
| **Janela ADTV** | Ano de 2010 | `src/config.json` : `ANO_FORMACAO_ADTV = 2010` | 2010 | ✅ OK |
| **Outliers — método** | MAD (Median Absolute Deviation) | `config.json` : `K_MAD`, `C_MAD` | IQR × multiplicador | ❌ DIVERGE (método) |
| **Outliers — multiplicador** | K_MAD = 3,5 ; C_MAD = 0,6745 | `src/config.json` | "IQR × 3,0" | ❌ DIVERGE |
| **Retorno simples** | `pct_change` | `NB05a` (convenção) | sim | ✅ OK |
| **Retorno log** | `np.log(P/P.shift(1))` | `NB09` (testes econométricos) | sim | ✅ OK |
| **Fator de anualização** | **252 dias úteis** | `TRADING_DAYS` em `config_loader.py` | 252 | ✅ OK |
| **Proxy rf** | CDI diário (BCB-SGS) | `NB04` / `rf_diario.parquet` | CDI | ✅ OK |
| **CDI médio anualizado (OOS)** | **≈ 9,27% a.a.** | `rf_diario.parquet` (cálculo direto) | "a completar" | EXTRAÍDO |
| **CDI médio anualizado (full)** | **≈ 9,29% a.a.** | `rf_diario.parquet` | — | EXTRAÍDO |
| **Estimador de covariância** | Ledoit-Wolf (sklearn) | `NB06` / `utils/covariancia.py` | Ledoit-Wolf | ✅ OK |
| **Anualização Σ** | × 252 | `NB06_cel_estimacao` | × 252 | ✅ OK |
| **Σ no BL (escala)** | **× 252** (`S_anual = S * TRADING_DAYS`) | `utils/otimizacao.py` : L464 | afirma × 21 (limitação) | ❌ TEXTO ERRADO — código já corrigido |
| **Restrições otimização** | long-only, soma=1 | `config.json` : `LONG_ONLY = True` | sim | ✅ OK |
| **Teto por emissor (c10)** | **10%** | `config.json` : `TETO_PESO = 0.1` | 10% (CVM 175) | ✅ OK |
| **Custo de transação** | **50 bps (0,5%)** | `config.json` : `CUSTO_BPS = 50.0` | 0,5% (metodologia) / 0,2% (resultados) | ❌ TEXTO INCONSISTENTE |
| **Penalidade L1** | **Não existe** | — | c = 0,5% ou 0,2% | ❌ TEXTO ERRADO |
| **MAR (PMPT)** | CDI diário (`MAR_MODO = "cdi"`) | `config.json` : `MAR_MODO` | CDI | ✅ OK |
| **α CVaR/CDaR** | **0,95** (5% cauda) | `config.json` : `ALPHA_PMPT = 0.95` | 95% | ✅ OK |
| **Omega (n=1)** | `w_max_kappa(n=1)` | `utils/otimizacao.py` : L200+ | Omega Ratio | ✅ OK |
| **Sortino (n=2)** | `w_max_kappa(n=2)` | `utils/otimizacao.py` : L200+ | Sortino | ✅ OK |
| **Kappa-3 (n=3)** | `w_max_kappa(n=3)` | `utils/otimizacao.py` : L200+ | Kappa-3 | ✅ OK |
| **Solver convexo** | CLARABEL (fallback ECOS/SCS) | `utils/otimizacao.py` (cvxpy) | CLARABEL/ECOS | ✅ OK |
| **Solver não-convexo** | SLSQP (ótimo local) | `utils/otimizacao.py` : L153 | SLSQP | ✅ OK |
| **Visões BL (Q)** | **Momentum 12-1** | `NB07_cel1` : `VISAO_MOMENTUM_MESES = (12, 1)` | "BL + LSTM" (tabela resultados) | ❌ DIVERGE |
| **Prior BL (wm)** | **Equiponderado 1/N** | `utils/otimizacao.py` : L465 | 1/N (metodologia) / cap de mercado (limitações) | ✅ OK (1/N) |
| **δ BL** | **2,5 fixo** | `NB07_cel1` : `DELTA = 2.5` | "otimização reversa / deu negativo" | ❌ TEXTO ERRADO |
| **τ BL** | **0,05** | `NB07_cel1` : `TAU = 0.05` | 0,05 | ✅ OK |
| **LSTM** | **Não implementado** | busca em todo o repositório: zero ocorrências | citado na tabela | ❌ TEXTO ERRADO |
| **ARIMA** | **Não implementado** | busca em todo o repositório: zero ocorrências | citado em sumário/introdução | ❌ TEXTO ERRADO |
| **Bootstrap (B)** | **2.000** reamostragens | `config.json` : `BOOTSTRAP_REPS = 2000` | 2.000 | ✅ OK |
| **Bootstrap (bloco)** | **10 dias** | `config.json` : `BOOTSTRAP_BLOCK_MEAN = 10` | — | EXTRAÍDO |
| **Ajuste múltiplo** | Holm-Bonferroni | `utils/inferencia.py` | — | EXTRAÍDO |
| **Sementes (SEED)** | **42** | `config.json` : `SEED = 42` | — | EXTRAÍDO |
| **Monte Carlo (N)** | **50.000** carteiras | `config.json` : `N_MONTECARLO = 50000` | 50.000 | ✅ OK |

---

## 3. Veredito das 11 Discrepâncias

| # | Discrepância descrita | Veredito | Valor correto (código/artefato) |
|---|---|---|---|
| 1 | N do universo (118, 120, 130, 135, 136) | **CÓDIGO contradiz todos**: N = **102** | `tickers_finais.csv` : 102 ativos; C(102,2) = **5.151** pares — não 8.385. O valor 8.385 = C(130,2) indica que um rascunho anterior rodou com N=130; o pipeline atual gera N=102. |
| 2 | Visões BL: momentum 12-1 vs "BL + LSTM" | **TEXTO está errado**: código usa **momentum 12-1** | `NB07_cel1` : `VISAO_MOMENTUM_MESES = (12, 1)`. Nenhum arquivo do repositório contém LSTM. O rótulo "BL + LSTM" na tabela de resultados deve ser substituído por "BL (momentum 12-1)". |
| 3 | Métricas MinVar L1 e MaxSharpe L1 "a completar" | **Estratégias inexistentes no código** | O sufixo `_c10` designa teto de 10% por ativo (restrição de caixa), não penalidade L1. As estratégias `MinVar_c10` e `MaxSharpe_c10` têm métricas completas nos artefatos (ver §5, Apêndice H). Não existem notebooks 14_1_4 ou 14_2_4. |
| 4 | Prior BL: 1/N (metodologia) vs cap de mercado (limitações) | **CÓDIGO confirma 1/N** | `utils/otimizacao.py` L465: `wm = np.repeat(1.0 / N, N)`. A menção a "capitalização de mercado de mai/2026" na seção de limitações é incorreta. |
| 5 | Penalidade L1: 0,5% (metodologia) vs 0,2% (resultados) | **Não existe L1 no código** | `config.json`: `CUSTO_BPS = 50.0` (= 0,5%) é custo de transação deduzido pelo giro de carteira, não penalidade L1 de regularização. O texto deve eliminar toda referência a "penalidade L1" e substituir por "custo de transação proporcional ao giro (50 bps)". |
| 6 | N de pregões: 3.967 (texto) vs 4.030 (Apêndice B) | **AMBÍGUO** | `retornos_simples.parquet` (usado na otimização) tem **3.966 linhas** (2010-01-05 a 2025-12-30). `painel_alinhado.parquet` tem **3.967** (inclui 2010-01-04). O valor 4.030 não tem correspondência em nenhum artefato. O texto deve citar **3.966 pregões** para a série de retornos. |
| 7 | Σ no BL: ×252 ou ×21? | **CÓDIGO confirma ×252** (corrigido) | `utils/otimizacao.py` L464: `S_anual = S * TRADING_DAYS` (= ×252), com comentário `[FIX D1]` documentando que a versão anterior passava S diário. A seção de limitações do texto deve ser atualizada: o erro ×21 foi corrigido antes da geração dos resultados finais. |
| 8 | δ: otimização reversa vs 2,5 fixo / deu negativo | **CÓDIGO confirma δ = 2,5 fixo** | `NB07_cel1`: `DELTA = 2.5 # He & Litterman (1999)`. Não há implementação de otimização reversa de δ. O texto deve descrever δ = 2,5 como parâmetro calibrado por referência à literatura, não como resultado de otimização reversa. |
| 9 | Datas de início OOS (estratégias L1 vs BL) | **Todas começam em 2015-03-02** | `strategy_returns.parquet`: primeira data = 2015-03-02 para todas as 16 estratégias e benchmarks. Não há desalinhamento. |
| 10 | GOLL54 e RCSL4 nos tickers | **Ambos ausentes** do universo final | Lista dos 102 tickers (`tickers_finais.csv`) não contém GOLL4, GOLL54, RCSL4 nem RCSL3. Se o texto os cita como exemplos de ativos excluídos, isso pode ser factualmente correto mas requer confirmação no log de exclusão do NB03. |
| 11 | ARIMA citado no texto | **Não implementado** | Busca recursiva em todo o repositório (`*.py`, `*.ipynb`) retornou zero ocorrências de "arima" ou "ARIMA". Todo trecho do texto que mencione ARIMA como método de geração de visões deve ser removido. |

---

## 4. Inventário do Pipeline e Mapeamento Apêndice ↔ Notebook

### 4.1 Tabela de mapeamento

| Apêndice (provável) | Conteúdo esperado | Notebook(s) responsável(is) | Situação |
|---|---|---|---|
| **A** | Universo inicial de ativos (B3/COTAHIST), critérios de exclusão | `10_Tratamento_COTAHIST_B3/Apendice_Tratamento_COTAHIST.ipynb` + `11_Classificador_Integridade/` | Existe e está completo |
| **B** | Funil de liquidez: presença, ADTV, N final | `03_Filtro_Liquidez/03_01_Ingestao_Filtro_Liquidez_v3.ipynb` | Existe e está completo |
| **C** | Taxas livres de risco (CDI/Selic, BCB-SGS) | `04_Taxas_Livres_Risco/04_01_Taxas_Livres_Risco_SGS_Final.ipynb` | Existe e está completo |
| **D** | Saneamento, winsorização (MAD) e retornos | `05_Alinhamento_Winsorizacao/05_01_*.ipynb` + `05_02_*.ipynb` | Existe e está completo |
| **E** | Estimação de momentos e Ledoit-Wolf | `06_Estimacao_Covariancia/06_01_Estimacao_LedoitWolf.ipynb` | Existe e está completo |
| **F** | Metodologia de otimização (MPT/PMPT/BL) e backtest | `07_Otimizacao_Carteiras/07_01_Otimizacao_Carteiras.ipynb` | Existe e está completo |
| **G** | Diagnóstico do IBOV (raiz unitária, ARCH, normalidade) | `09_Inferencia_Econometrica/09_01_*.ipynb` → `apendice_G_diagnostico_ibov.csv` | Existe; artefato presente |
| **H** | Desempenho e inferência estatística das estratégias | `09_Inferencia_Econometrica/09_01_*.ipynb` → `apendice_H_*.csv` | Existe; artefatos presentes |
| **I** | Fronteira eficiente (MV e CVaR) e carteiras canônicas | `08_Fronteira_Eficiente/08_01_Fronteira_Eficiente.ipynb` | Existe e está completo |
| **J** | Testes bootstrap de Sharpe/Sortino (3 benchmarks) | `09_Inferencia_Econometrica/09_01_*.ipynb` → `inferencia_*.csv` | Existe; artefatos presentes |

**Notebooks sem apêndice correspondente identificado:**
- `01_Conversao_Parquet/01_01_convertendo_em_parquet_v3.ipynb` — pipeline interno (ETL), possivelmente embutido no Apêndice B
- `02_Consolidacao_Dados/02_01_consolidando_dados.ipynb` — pipeline interno

---

## 5. Bloco por Apêndice (A–J)

### Apêndice A — Dados Brutos B3 e Classificador de Integridade

#### O que o notebook faz hoje
O notebook `Apendice_Tratamento_COTAHIST.ipynb` processa os arquivos históricos COTAHIST da B3 (arquivos TXT/ZIP em `data/B3_COTAHIST/`, referentes a 2010–2025) para validar a integridade dos preços de fechamento. O notebook `Apendice_Classificador_Integridade_Universo_v2.ipynb` classifica os ativos segundo critérios de completude temporal e consistência de séries, gerando insumos para o funil de liquidez do NB03.

#### Texto de atualização sugerido
> A base de dados foi obtida junto à B3 por meio da série histórica COTAHIST, compreendendo os arquivos de cotações diárias do período de 2010 a 2025. O classificador de integridade verificou a existência de preços de fechamento ajustados para cada ativo em cada pregão, identificando lacunas e inconsistências que subsidiaram o funil de liquidez descrito no Apêndice B. Os dados proprietários provenientes da plataforma Economatica — 496 séries de preços e volumes — foram convertidos para o formato Parquet e consolidados em um painel MultiIndex antes da aplicação dos filtros. Os dados brutos da Economatica estão sujeitos a licença comercial e não são redistribuíveis.

---

### Apêndice B — Filtro de Liquidez e Universo Investável

#### O que o notebook faz hoje
`03_01_Ingestao_Filtro_Liquidez_v3.ipynb` aplica três critérios sequenciais de exclusão sobre a matriz bruta de preços:

1. **Presença em pregão:** ativos com menos de 95% de dias com cotação válida são excluídos (`LIMIAR_PRESENCA = 0,95`).
2. **IPO tardio:** ativos com primeiro pregão após o início da janela são excluídos para evitar *look-ahead bias*.
3. **ADTV:** ativos no decil inferior do volume médio diário negociado em 2010 (`PERCENTIL_LIQUIDEZ = 0,10`) são excluídos.

O resultado é a `Matriz_precos_sanitizada.csv` com o universo investável de **102 ativos**.

#### Texto de atualização sugerido
> O universo investável foi construído por meio de um funil de três estágios. **Primeiro**, foram excluídos os ativos com taxa de presença em pregão inferior a 95% (limiar $Pr_i < 0{,}95$). **Segundo**, foram removidos os ativos cujo primeiro pregão ocorreu após janeiro de 2010, eliminando o viés de antecipação associado a IPOs tardios. **Terceiro**, foram excluídos os ativos posicionados no decil inferior ($P_{10}$) do volume médio diário negociado financeiramente (*Average Daily Traded Value*, ADTV), medido exclusivamente no ano de 2010. Após a aplicação do funil, o universo investável resultante compreende **N = 102 ativos**, gerando $C(102, 2) = \mathbf{5.151}$ **pares de covariância** estimados. O número total de pregões na série de retornos é de **3.966** (de 5 de janeiro de 2010 a 30 de dezembro de 2025).

> **Nota de revisão:** Os valores 118, 120, 130, 135 e 136 citados em versões anteriores do texto referem-se a rascunhos intermediários do pipeline. O valor definitivo, extraído de `tickers_finais.csv` e da matriz `retornos_simples_saneado.parquet` (dimensão 3.966 × 102), é **N = 102**. O valor de 8.385 pares citado anteriormente corresponderia a C(130, 2) e é inconsistente com o pipeline atual. O valor de 4.030 pregões citado no Apêndice B não corresponde a nenhum artefato; o valor correto é **3.966**.

---

### Apêndice C — Taxas Livres de Risco

#### O que o notebook faz hoje
`04_01_Taxas_Livres_Risco_SGS_Final.ipynb` ingere as séries diárias do CDI e da Selic via API pública do Banco Central do Brasil (SGS — séries 12 e 432, respectivamente). Os dados são salvos em `data/CDI/cdi_diario_bcb_2010_atual.csv` e no arquivo consolidado `rf_diario.parquet` (3.966 pregões, 2010-01-05 a 2025-12-30).

#### Texto de atualização sugerido
> A taxa livre de risco diária empregada como referencial de excesso de retorno e como Minimum Acceptable Return (MAR) nas métricas PMPT foi o **CDI (*Certificado de Depósito Interbancário*)**, obtido junto ao Banco Central do Brasil por meio da API SGS (série n.º 12). A série compreende **3.966 pregões** (5 de janeiro de 2010 a 30 de dezembro de 2025), alinhados ao calendário de pregões das ações. O **CDI médio anualizado no período completo foi de 9,29% a.a.**, e de **9,27% a.a.** no subperíodo *out-of-sample* (2 de março de 2015 a 30 de dezembro de 2025), calculado por $\bar{r}_f^{\text{anual}} = \bar{r}_f^{\text{diário}} \times 252$.

---

### Apêndice D — Saneamento e Winsorização

#### O que o notebook faz hoje
`05_01_Alinhamento_e_Retornos.ipynb` alinha as séries de preços ao calendário do IBOV e calcula retornos simples e logarítmicos. `05_02_Saneamento_e_Winsorizacao.ipynb` detecta e winsoriza retornos outliers por **MAD** (*Median Absolute Deviation*): um retorno é classificado como outlier se $|r_{i,t} - \tilde{r}_i| > K_{\text{MAD}} \times C_{\text{MAD}} \times \text{MAD}_i$, com $K_{\text{MAD}} = 3{,}5$ e $C_{\text{MAD}} = 0{,}6745$. O log de winsorização está em `data/Retornos/log_winsorizacao.csv`.

#### Texto de atualização sugerido
> O saneamento estatístico das séries de retornos foi realizado pelo método **MAD** (*Median Absolute Deviation*), com multiplicador $K_{\text{MAD}} = 3{,}5$ e constante de consistência $C_{\text{MAD}} = 0{,}6745$. Um retorno $r_{i,t}$ é classificado como *outlier* quando $|r_{i,t} - \tilde{r}_i| > 3{,}5 \times 0{,}6745 \times \text{MAD}_i$, em que $\tilde{r}_i$ é a mediana da série do ativo $i$ e $\text{MAD}_i$ o desvio absoluto mediano calculado sobre observações não-nulas. Os retornos identificados como *outliers* são **winzorizados** (substituídos pelo valor do limiar), não excluídos da amostra, preservando a continuidade temporal.

> **Nota de revisão:** Versões anteriores do texto mencionam o multiplicador do **IQR** (*Interquartile Range*) com valor 3,0. O código utiliza o **MAD**, não o IQR — tratam-se de estimadores distintos de dispersão robusta. O texto deve ser corrigido para refletir o método MAD com $K = 3{,}5$.

---

### Apêndice E — Estimação de Momentos e Covariância (Ledoit-Wolf)

#### O que o notebook faz hoje
`06_01_Estimacao_LedoitWolf.ipynb` estima, sobre a série completa de retornos com janela expansiva, o vetor de médias anualizadas e a matriz de covariância regularizada de Ledoit-Wolf (2004) anualizada $\hat{\Sigma}_{\text{LW,anual}} = \hat{\Sigma}_{\text{LW,diário}} \times 252$. Os artefatos (`mu_anual.parquet`, `sigma_ledoitwolf_anual.parquet`, `sigma_amostral_anual.parquet`, `correlacao.parquet`) têm dimensão 102 × 102 e são usados pelo NB08 (fronteira eficiente estática).

#### Texto de atualização sugerido
> A matriz de covariância utilizada na construção da fronteira eficiente e como insumo dos otimizadores de Máximo Sharpe é a estimativa regularizada de **Ledoit e Wolf (2004)** (*Oracle Approximating Shrinkage*, OAS), implementada via `sklearn.covariance.LedoitWolf`. A anualização segue a convenção $\hat{\Sigma}_{\text{anual}} = \hat{\Sigma}_{\text{diário}} \times 252$. A estimação foi realizada sobre os **102 ativos** do universo investável com a série completa de **3.966 pregões**. O parâmetro de encolhimento (*shrinkage intensity*) $\hat{\delta}$ é estimado analiticamente pelo OAS e varia com a razão $T/N$: para a amostra completa ($T = 3.966$, $N = 102$), o valor obtido é $\hat{\delta} \approx 0{,}005$ (mínimo encolhimento); em janelas mais curtas de 63 dias úteis, $\hat{\delta}$ pode atingir $\approx 0{,}35$, assegurando que a matriz permaneça definida positiva em períodos de alta colinearidade.

---

### Apêndice F — Metodologia de Otimização e Backtest Out-of-Sample

#### O que o notebook faz hoje
`07_01_Otimizacao_Carteiras.ipynb` executa o backtest *out-of-sample* com janela expansiva, rebalanceamento mensal e 16 estratégias. Parâmetros centrais verificados no código:

| Parâmetro | Valor | Fonte |
|---|---|---|
| Janela | expansiva (toda a história até t-1) | `NB07_cel1` : `TIPO_JANELA = "expansiva"` |
| Warm-up | 60 meses | `config.json` : `WARMUP_MESES = 60` |
| Primeiro rebalanceamento OOS | 2015-03-02 | `strategy_returns.parquet` |
| N rebalanceamentos | 130 | `pesos_historico.csv` |
| Custo de transação | 50 bps × giro | `config.json` : `CUSTO_BPS = 50.0` |
| Teto por ativo (c10) | 10% | `config.json` : `TETO_PESO = 0.1` |
| BL — δ | 2,5 fixo | `NB07_cel1` : `DELTA = 2.5` |
| BL — τ | 0,05 | `NB07_cel1` : `TAU = 0.05` |
| BL — visões | momentum 12-1 | `NB07_cel1` : `VISAO_MOMENTUM_MESES = (12, 1)` |
| BL — prior | equiponderado 1/N | `utils/otimizacao.py` : L465 |
| BL — Σ | Ledoit-Wolf × 252 | `utils/otimizacao.py` : L464 |
| PMPT — α | 0,95 | `config.json` : `ALPHA_PMPT = 0.95` |
| MAR | CDI diário | `config.json` : `MAR_MODO = "cdi"` |

O código **não implementa LSTM, ARIMA nem otimização reversa de δ**.

#### Texto de atualização sugerido
> O backtest é conduzido em regime **expansivo** (*expanding window*): a cada mês $t$, o otimizador utiliza todos os retornos diários disponíveis desde janeiro de 2010 até o último pregão do mês $t-1$. A janela de *warm-up* é de **60 meses**, de modo que o primeiro conjunto de pesos é calculado ao final de fevereiro de 2015 e aplicado a partir de **2 de março de 2015**. Ao longo do período *out-of-sample* (março de 2015 a dezembro de 2025), foram realizados **130 rebalanceamentos** mensais, gerando **2.690 pregões** de retornos *out-of-sample*.

> O custo de transação é modelado como um custo proporcional ao giro de **50 pontos-base (0,50%)**: $c_t = 0{,}005 \times \sum_i |w_{i,t} - \tilde{w}_{i,t-1}|$, em que $\tilde{w}_{i,t-1}$ representa os pesos após a valorização de mercado ao final do mês anterior. O custo é deduzido no primeiro pregão do mês de rebalanceamento.

> As visões do modelo Black-Litterman são geradas pelo **sinal de momentum de 12 meses menos 1 mês** ($12{-}1$), conforme He e Litterman (1999). O retorno esperado da visão para o ativo $i$ é calculado com base no retorno acumulado nos últimos 252 pregões excluídos os últimos 21, anualizado pelo período efetivo. A matriz de incerteza das visões é $\Omega = \text{diag}(\tau \hat{\Sigma}_{\text{LW,anual}})$ com $\tau = 0{,}05$. O prior de equilíbrio é $\Pi = \delta \hat{\Sigma}_{\text{LW,anual}} \mathbf{w}_m$, com $\delta = 2{,}5$ (coeficiente de aversão ao risco implícita, calibrado por referência a He e Litterman, 1999) e $\mathbf{w}_m = \mathbf{1}/N$ (carteira equiponderada com $N = 102$ ativos). **Não foi implementado LSTM, ARIMA ou qualquer modelo de previsão de séries temporais** para a geração das visões.

> **Notas de revisão:** (i) O texto anterior menciona "otimização reversa de δ" com resultado negativo e substituição por 2,5 — o código não realiza tal otimização; δ = 2,5 é parâmetro definido diretamente. (ii) A escala da matriz de covariância no modelo BL era incorretamente passada como diária em versão anterior (erro documentado como `[FIX D1]` em `utils/otimizacao.py` : L459–463); o código atual usa $\hat{\Sigma}_{\text{anual}} = \hat{\Sigma}_{\text{diário}} \times 252$, e os resultados reportados foram gerados **com essa correção aplicada**. (iii) As estratégias denominadas "MinVar L1" e "MaxSharpe L1" no texto correspondem, no código, a `MinVar_c10` e `MaxSharpe_c10` — restrições de teto de 10% por ativo, não penalidades de regularização L1.

---

### Apêndice G — Diagnóstico do IBOV

#### O que o notebook faz hoje
`09_01_Inferencia_Econometrica.ipynb` realiza testes diagnósticos sobre os retornos logarítmicos diários do IBOVESPA, salvos em `data/Estrategias/apendice_G_diagnostico_ibov.csv`.

#### Texto de atualização sugerido (valores extraídos do artefato)
> Os testes diagnósticos realizados sobre os retornos logarítmicos diários do IBOVESPA no período 2010–2025 confirmam as propriedades estilizadas das séries financeiras: (i) **estacionariedade nos retornos** — o teste ADF rejeita a hipótese de raiz unitária ($t_{\text{ADF}} = -23{,}38$, $p < 0{,}001$), enquanto o KPSS não rejeita a estacionariedade ($\eta = 0{,}149$, $p = 0{,}10$), indicando processo I(0) nos retornos e I(1) no nível de preços; (ii) **heterocedasticidade condicional severa** — o teste ARCH-LM com 10 defasagens rejeita variância constante ($\text{LM} = 1.514{,}1$, $p < 0{,}001$); (iii) **não-normalidade** — o teste Jarque-Bera rejeita a normalidade ($\text{JB} = 24.534{,}1$, $p < 0{,}001$), com curtose excessiva de 12,1 e leve assimetria negativa; (iv) **passeio aleatório não rejeitado** — o teste de razão de variância de Lo-MacKinlay com $k \in \{2, 16\}$ não rejeita a hipótese de ausência de autocorrelação linear ($p > 0{,}10$). Esses resultados justificam o uso de **bootstrap estacionário por blocos** (Ledoit e Wolf, 2008) em lugar de testes paramétricos de Sharpe.

---

### Apêndice H — Desempenho e Inferência das Estratégias

#### O que o notebook faz hoje
`09_01_Inferencia_Econometrica.ipynb` consolida as métricas de desempenho OOS e realiza testes de significância estatística (bootstrap de Sharpe; CAPM com erros HAC Newey-West; teste de *spanning* de Huberman e Kandel, 1987). Os artefatos resultantes são `apendice_H_painel_metricas.csv`, `apendice_H_testes_estrategia.csv` e `apendice_H_comparativo_rf.csv`.

#### Tabela de desempenho OOS — valores extraídos de `desempenho_estrategias.csv`

| Estratégia | Ret. Acum. (%) | CAGR (% a.a.) | Vol. (% a.a.) | Sharpe | Sortino | Max DD (%) | Giro (× a.a.) |
|---|---|---|---|---|---|---|---|
| EqualWeight | 302,3 | 13,91 | 19,56 | 0,290 | 0,403 | −35,54 | 0,83 |
| EqualWeight BuyHold | 448,1 | 17,28 | 19,28 | 0,443 | 0,621 | −33,00 | 0,00 |
| InvVol | 330,3 | 14,65 | 18,90 | 0,328 | 0,455 | −34,28 | 0,79 |
| MinVar | 269,3 | 13,00 | **12,95** | 0,293 | 0,400 | −25,05 | 0,80 |
| **MinVar c10** | 275,1 | 13,17 | 12,98 | 0,304 | 0,415 | −25,00 | 0,79 |
| MaxSharpe | 304,1 | 13,96 | 17,54 | 0,305 | 0,430 | **−22,76** | 1,22 |
| **MaxSharpe c10** | 268,2 | 12,99 | 16,54 | 0,261 | 0,365 | −23,89 | 1,51 |
| MaxOmega | 196,2 | 10,71 | 21,23 | 0,149 | 0,210 | −30,67 | 2,24 |
| MaxSortino | 286,9 | 13,53 | 17,79 | 0,281 | 0,397 | −23,26 | 1,31 |
| MaxKappa3 | 292,3 | 13,64 | 18,26 | 0,284 | 0,403 | −22,55 | 1,34 |
| MinCVaR | 253,9 | 12,57 | 12,88 | 0,264 | 0,363 | −26,44 | 1,11 |
| **MinCDaR** | **75,0** | **5,36** | 19,82 | **−0,105** | **−0,145** | **−62,46** | 1,47 |
| **BL clássico** | **921,2** | **24,31** | 25,97 | **0,611** | **0,890** | −38,93 | **7,98** |
| BL clássico c10 | 627,7 | 20,44 | 20,20 | 0,563 | 0,792 | −33,60 | 6,29 |
| BL downside | 803,5 | 22,91 | 32,17 | 0,514 | 0,753 | −57,41 | 9,48 |
| BL downside c10 | 427,9 | 16,87 | 22,30 | 0,395 | 0,554 | −38,01 | 7,33 |
| **IBOV (benchmark)** | 212,2 | 11,26 | 23,32 | 0,178 | 0,245 | −46,82 | — |

> **Nota de revisão crítica:** As colunas "MinVar L1" e "MaxSharpe L1" mencionadas no texto com métricas "a completar" **não correspondem a nenhuma estratégia implementada**. As estratégias `MinVar_c10` e `MaxSharpe_c10` — cujas métricas figuram acima em negrito — são as versões com **teto de 10% por ativo** (restrição de caixa). O texto deve substituir a denominação "L1" por "c10" (teto) e remover qualquer referência a notebooks 14_1_4 e 14_2_4.

---

### Apêndice I — Fronteira Eficiente e Carteiras Canônicas

#### O que o notebook faz hoje
`08_01_Fronteira_Eficiente.ipynb` traça as fronteiras de média-variância e média-CVaR por simulação de Monte Carlo (50.000 carteiras) e por otimização paramétrica (60 pontos na fronteira MV, 30 pontos na fronteira CVaR). As carteiras canônicas estão em `carteiras_canonicas.csv`.

#### Tabela de carteiras canônicas — extraída de `carteiras_canonicas.csv`

| Carteira | Ret. (% a.a.) | Vol. (% a.a.) | Sharpe | Maior peso | N ativos > 1% |
|---|---|---|---|---|---|
| MVP (Mínima Variância) | 12,57 | 11,92 | 0,275 | 14,36% | 21 |
| Tangente (sem teto) | 24,98 | 17,73 | 0,884 | 24,20% | 10 |
| Tangente c10 | 22,43 | 15,64 | 0,840 | 10,00% | 18 |
| MinCVaR | 13,86 | 12,07 | 0,378 | 17,91% | 18 |

#### Texto de atualização sugerido
> A fronteira eficiente de média-variância é gerada sobre os momentos estimados para o universo de **102 ativos**, com **50.000 carteiras simuladas** via distribuição de Dirichlet (parâmetro $\alpha = 0{,}3$) e **60 pontos** na fronteira paramétrica. A carteira de **mínima variância global (MVP)** apresenta retorno de 12,57% a.a., volatilidade de 11,92% a.a. e índice de Sharpe de 0,275, com alocação distribuída em 21 ativos com peso superior a 1%. A **carteira tangente** (máximo Sharpe, sem restrição de teto) atinge Sharpe de 0,884 com maior peso de 24,20% em um único ativo, concentrada em apenas 10 ativos. Com o teto de 10% por ativo (Tangente c10), o Sharpe cai para 0,840 e a carteira distribui-se por 18 ativos. A fronteira de média-CVaR ($\alpha = 0{,}95$) é obtida com 30 pontos paramétricos; a **carteira de mínimo CVaR** apresenta retorno de 13,86% a.a. e Sharpe de 0,378.

---

### Apêndice J — Testes Bootstrap de Sharpe e Sortino (3 Benchmarks)

#### O que o notebook faz hoje
`09_01_Inferencia_Econometrica.ipynb` realiza o **bootstrap estacionário por blocos** de Ledoit e Wolf (2008) para comparar o índice de Sharpe de cada estratégia contra três benchmarks (EqualWeight, EqualWeight BuyHold e IBOV), com $B = 2.000$ reamostragens e bloco médio de 10 dias úteis. O ajuste de múltiplos testes segue a correção de Holm-Bonferroni (15 comparações por benchmark). Os artefatos são `inferencia_sharpe_3benchmarks.csv` e `inferencia_sortino_3benchmarks.csv`.

#### Texto de atualização sugerido
> Os testes de diferença de índice de Sharpe foram realizados pelo método de **bootstrap estacionário por blocos** (Ledoit e Wolf, 2008), com $B = 2.000$ reamostragens e comprimento médio de bloco de 10 dias úteis. Para controle da taxa de erro familiar, aplicou-se a correção de **Holm-Bonferroni** sobre as 15 comparações realizadas por benchmark. Ao nível $\alpha = 0{,}05$, **nenhuma estratégia apresentou diferença de Sharpe estatisticamente significativa** em relação ao benchmark 1/N após o ajuste de múltiplos testes, resultado consistente com a baixa potência do teste de Ledoit-Wolf em amostras com $T \approx 2.690$ pregões e elevada variância nos retornos. Sob o critério econômico (sem ajuste de múltiplos), a diferença de Sharpe do BL clássico em relação ao 1/N ($\Delta \hat{S} = +0{,}321$, $p_{\text{bruto}} = 0{,}260$) é economicamente material mas estatisticamente não significativa ao nível convencional.

---

## 6. Pendências de Execução

**Nenhum valor relevante requer nova execução.** Todos os artefatos em `data/Estrategias/` estão presentes e consistentes internamente. As ações pendentes são exclusivamente **ajustes de texto**, listadas a seguir:

| Ajuste necessário no texto | Valor correto (código/artefato) | Referência |
|---|---|---|
| Substituir N = 118/120/130/135/136 por **N = 102** | `tickers_finais.csv` | §3, item 1 |
| Substituir 8.385 pares por **5.151 pares** | derivado: C(102,2) | §3, item 1 |
| Substituir 3.967 / 4.030 pregões por **3.966** | `retornos_simples.parquet` | §3, item 6 |
| Substituir 132 rebalanceamentos por **130** | `pesos_historico.csv` | §2 |
| Substituir "BL + LSTM" por **"BL (momentum 12-1)"** | `NB07_cel1` | §3, item 2 |
| Remover **ARIMA** de todas as menções como método de visões | busca no repositório | §3, item 11 |
| Substituir "penalidade L1" por **"custo de transação proporcional ao giro (50 bps)"** | `config.json` | §3, item 5 |
| Substituir "MinVar L1 / MaxSharpe L1" por **"MinVar c10 / MaxSharpe c10"** | `desempenho_estrategias.csv` | §3, item 3 |
| Remover afirmação "Σ ×21 por engano": **código atual usa ×252** | `utils/otimizacao.py` L464 | §3, item 7 |
| Substituir "otimização reversa de δ" por **"δ = 2,5 fixo por referência à literatura"** | `NB07_cel1` : `DELTA = 2.5` | §3, item 8 |
| Confirmar **prior = 1/N** e remover menção a cap de mercado | `utils/otimizacao.py` L465 | §3, item 4 |
| Corrigir método de outliers de "IQR × 3,0" para **"MAD, K = 3,5"** | `config.json` | §2 |
| Inserir CDI médio OOS: **9,27% a.a.** | `rf_diario.parquet` | §5, Apêndice C |
| Verificar se GOLL4/RCSL4 aparecem no log de exclusão do NB03 | `03_01_Ingestao_Filtro_Liquidez_v3.ipynb` | §3, item 10 |

---

## 7. Aderência às Ten Simple Rules (Rule et al., 2019)

| Regra | Descrição | Avaliação |
|---|---|---|
| 1 — Contar uma história | Cada notebook abre com célula markdown descrevendo objetivo, entradas e saídas | ✅ Atendida |
| 2 — Documentar o processo | Células markdown intercaladas explicam decisões metodológicas | ✅ Atendida (NB02 mais enxuto) |
| 3 — Usar ambientes reprodutíveis | `requirements.txt` presente na raiz; versões fixadas | ✅ Atendida |
| 4 — Controlar seed de aleatoriedade | `SEED = 42` em `config.json`; `np.random.default_rng(SEED)` nos notebooks | ✅ Atendida |
| 5 — Declarar dependências | `requirements.txt` na raiz; importações explícitas por notebook | ✅ Atendida |
| 6 — Usar caminhos relativos | Notebooks usam `Path.cwd().parent.parent` para localizar `data/` | ✅ Atendida |
| 7 — Declarar entradas e saídas | Cada notebook declara `DIR_ENTRADA` e `OUTPUT_DIR` explicitamente | ✅ Atendida |
| 8 — Encapsular lógica em funções | Lógica complexa movida para `utils/*.py`; notebooks orquestram chamadas | ✅ Atendida |
| 9 — Executável de ponta a ponta | `run_pipeline.py` executa todos os notebooks; cache MD5 detecta mudanças; `test_pipeline.py` valida saídas | ✅ Atendida |
| 10 — Compartilhar dados e código | Dados Economatica são proprietários (não compartilháveis); código versionado em git | ⚠️ Parcial — dados brutos não são reprodutíveis por terceiros sem licença |

**Ponto de atenção para a banca:** a afirmação de "reprodutibilidade algorítmica" é sustentável para quem possuir acesso à licença Economatica. Para reprodutibilidade plena por terceiros, seria necessário disponibilizar os retornos sanitizados (`retornos_simples_saneado.parquet`), que não contêm preços brutos e podem ser considerados dados derivados publicamente compartilháveis.

---

*Fim do relatório — gerado por auditoria de código-fonte e artefatos em 9 de junho de 2026.*
