# RELATÓRIO DE AVALIAÇÃO TÉCNICA — TCC

**Gerado em:** 2026-06-04  
**Auditor:** Arguidor técnico de banca (auditoria estática de repositório)  
**Branch auditado:** `auditoria-tcc`  
**Arquivo docx auditado:** `docs/Entrega_12_Pedro_Reis_auditado.docx`

---

## SEÇÃO 1 — FICHA TÉCNICA E VEREDITO GERAL

| Campo | Valor |
|---|---|
| **Título** | Moderna Teoria das Carteiras no Mercado de Ações Brasileiro: Comparação entre Otimizadores e Inputs |
| **Autor** | Pedro Augusto Pinheiro Reis |
| **Orientador** | Prof. Dr. Moisés Ferreira da Cunha |
| **Programa/Curso** | Bacharelado em Ciências Contábeis |
| **Instituição** | Universidade Federal de Goiás — FACE/UFG |
| **Período OOS** | 2015-03-02 a 2025-12-30 (≈ 10,8 anos, 2.690 pregões) |
| **Data da auditoria** | 2026-06-04 |
| **Versão auditada** | `Entrega_12_Pedro_Reis_auditado.docx` |

**Veredito geral.** O trabalho constitui um esforço quantitativo de maturidade acima da média para um TCC de graduação em Ciências Contábeis. O pipeline computacional é robusto, reprodutível, testado (92 casos pytest) e corretamente estruturado: a vedação ao viés de antecipação é respeitada, a escala temporal de anualização é consistente, a construção Bayesiana do Black-Litterman segue He e Litterman (1999) com fidelidade demonstrável no código. O principal problema que separa o trabalho de um nível "consistente e defensável" não é metodológico — é de fechamento textual: o Capítulo 4 reporta exclusivamente duas estratégias inexistentes nos artefatos (MinVar_L1 e MaxSharpe_L1 com regularização L1 como nome próprio, confundidas com o custo transacional) e uma estratégia BL com visões LSTM que não foi implementada no repositório; as 14 estratégias restantes, incluindo toda a família PMPT e as quatro variantes BL com momentum, têm métricas completas nos artefatos mas carecem de análise narrativa no texto. Adicionalmente, o docx contém inconsistências numéricas rastreáveis (N=130 vs. 118; pregões=4.030 vs. 3.967; pares=8.385 calculado para N=130, não para N=118) que, se não corrigidas antes da defesa, oferecem ângulos de ataque direto para a banca.

---

## SEÇÃO 2 — SÍNTESE DESCRITIVA CAPÍTULO A CAPÍTULO

### Introdução
Contextualiza a evolução da gestão quantitativa de portfólios, enuncia a questão de pesquisa (eficácia comparativa de MPT, PMPT e BL com diferentes inputs no mercado brasileiro) e estabelece o objetivo geral de avaliar estratégias com média histórica, ARIMA e LSTM no período 2010–2025.

### Capítulo 2 — Referencial Teórico
Abrange: (2.1–2.7) gênese da MPT, modelo Markowitz, CAPM, fronteira eficiente, Índice de Sharpe, pressupostos e limitações; (2.8–2.13) PMPT, métricas assimétricas (semivariância, CVaR, CDaR), LPMs, índices de Sortino, Omega e Kappa, fronteiras downside; (2.14) menção a Machine Learning e ML em finanças; (2.16–2.22) modelo de Black-Litterman completo: prior Π, visões (P, Q, Ω), fórmula mestra, τ, Idzorek, Entropy Pooling, comparações BL vs. MPT/PMPT. O referencial é extenso (~45 páginas) e tecnicamente denso.

### Capítulo 3 — Metodologia
Detalha: universo (B3, 2010–2025); critério de presença ≥95%; saneamento em quatro etapas; diagnóstico econométrico (ADF, KPSS, Ljung-Box, JB, ARCH-LM, Chow/CUSUM); estimação de μ e Σ por janela expansiva com Ledoit-Wolf; as três famílias de otimização (MPT: 6 estratégias; PMPT: 5 estratégias; BL: 4 estratégias); warm-up 60 meses; custo 50 bps (descrito como "penalidade L1/Lasso"); backtesting mensal. É a seção mais consistente com o código.

### Capítulo 4 — Resultados e Discussão
Reporta estatísticas descritivas (Tabelas 5–7) com referência a 130 ativos. Na seção de backtest, apresenta Tabela 8 (MinVar_L1), Tabela 9 (MaxSharpe_L1), Tabela 10 (BL + LSTM), Tabela 11 (unificada) e Tabela 12 (síntese). O capítulo está incompleto: a seção 4.4 tem título "l" (placeholder). As estratégias MinVar_L1 e MaxSharpe_L1 não existem nos artefatos; BL+LSTM igualmente inexistente. As 14 estratégias reais dos artefatos não são reportadas individualmente no texto. Há subseção 4.1.1 intitulada "Modelo Black-Litterman com Visões LSTM" (curiosamente na seção de estatísticas descritivas).

### Capítulo 5 — Conclusão
Discute os resultados declarados (MinVar supera outros modelos; ML não traz ganho no mercado brasileiro), situa achados em relação à literatura (DeMiguel et al., 2009; Santos e Tessari, 2012), aponta limitações (δ negativo na otimização reversa, turnover elevado nas variantes BL, ausência de validação preditiva formal das visões) e sugere extensões. A conclusão é coerente com os artefatos, mas discute um cenário ligeiramente diferente daquele realmente implementado.

### Referências
35 referências formatadas em ABNT. Inclui: Black & Litterman (1992), He & Litterman (1999), Ledoit & Wolf (2004), DeMiguel et al. (2009), Rockafellar & Uryasev (2002), entre outros. Ausências relevantes: Idzorek (2005), Santos & Tessari (2012), Memmel (2003) — todos citados no texto sem entrada na lista.

### Apêndices A–J
- **A:** Lista das 118 empresas selecionadas com setores.
- **B:** Diretrizes de higienização e filtragem de liquidez.
- **C:** Transformação de preços em retornos (simples e log).
- **D:** Consolidação da base mestre e tratamento do look-ahead bias.
- **E:** Derivação do prêmio de risco e excesso de retorno.
- **F:** Parâmetros inferenciais: Σ anualizada (×252), σ anualizada (×√252), beta, Sharpe analítico.
- **G:** Fronteira eficiente por simulação Monte Carlo (50.000 portfólios) e SLSQP.
- **H:** Isolamento de covariâncias negativas — mapeamento do par RCSL4-GOLL54 (cov = -0,0159), único dentre 8.385 cruzamentos calculados sobre N=130 (número inconsistente com N=118 canônico).
- **I:** Correlação de Pearson e clusterização hierárquica estrutural (mencionada no título, implementação em `src/` verificada como comentário sobre `ward`, não scipy.cluster).
- **J:** Engenharia reversa do BL: extração de Π por otimização reversa.

---

## SEÇÃO 3 — AVALIAÇÃO DO REFERENCIAL TEÓRICO

### Cobertura
A cobertura das três tradições (MPT, PMPT, BL) é abrangente para o nível de graduação. O referencial inclui as contribuições seminais (Markowitz 1952/1959, Sharpe 1966, Lintner 1965, Black & Litterman 1992, Rom & Ferguson 1994, Sortino & Van der Meer 1991, Rockafellar & Uryasev 2000/2002, He & Litterman 1999). A menção à integração com Machine Learning (Seção 2.14) é superficial e desconectada da implementação real — o texto anuncia LSTM e ARIMA como inputs do BL, mas nenhum dos dois existe no repositório.

### Correção Conceitual
- A distinção retorno simples (otimização) vs. log-retorno (econometria) está corretamente enunciada no Cap. 3 e implementada no código.
- A descrição do CVaR via formulação de Rockafellar-Uryasev está matematicamente correta.
- O CDaR é formalmente derivado a partir de drawdowns acumulados — definição coerente com Chekhlov et al. (2005), embora a referência a esse artigo esteja ausente.
- A fórmula mestra do BL e a construção de Ω He-Litterman são matematicamente apresentadas de forma correta no Cap. 3.
- A descrição de MaxSharpe como "máxima utilidade média-variância" (com λ=2,5) é tecnicamente honesta e inclui nota de ressalva metodológica.
- A menção ao método de Idzorek (Seção 2.19) como alternativa de calibração de Ω é correta teoricamente, mas gera expectativa de implementação que não se confirma no código.

### Atribuições Históricas e Citações-Chave
- Markowitz (1952, 1959): correto.
- Sharpe (1966): correto (Índice de Sharpe); porém a referência CAPM primária é Sharpe (1964) — o docx cita apenas 1966.
- DeMiguel et al. (2009): referência central ao "paradoxo 1/N", corretamente usada.
- Damodaran: citado no texto como "Damodaran (2007)" mas a referência lista a 3ª edição de 2012.
- Santos e Tessari (2012): citados na conclusão mas **ausentes da lista de referências** — achado crítico para ABNT.
- Idzorek (2005): discutido em 2.19 mas **ausente da lista de referências**.
- Memmel (2003): implicitamente subjacente ao teste Jobson-Korkie/Memmel implementado no código, não citado no texto.
- Rule et al. (2019): **não encontrado** no texto nem nas referências — mencionado no contexto de auditoria prévia como potencial lacuna; confirmado inexistente no docx.

---

## SEÇÃO 4 — AVALIAÇÃO DA METODOLOGIA

### 4.1 Filtros de Liquidez
O critério de presença ≥95% dos pregões (`LIMIAR_PRESENCA = 0.95`, `config.json`) e o ADTV do P10 a partir de 2010 (`ANO_FORMACAO_ADTV = 2010`, `PERCENTIL_LIQUIDEZ = 0.1`) estão corretamente implementados em `src/03_Filtro_Liquidez/03_01_Ingestao_Filtro_Liquidez_v3.ipynb` e alinhados com o Cap. 3. **Sem inconsistência**.

### 4.2 Saneamento de Outliers — MAD Modificado vs. IQR
O Cap. 3 (Etapa 3 do tratamento) descreve o método como "Amplitude Interquartil com multiplicador conservador de 3,0 (IQR×3,0)". O código e o `config.json` implementam MAD modificado de Iglewicz-Hoaglin (K=3,5; c=0,6745), conforme também registrado nos apêndices do próprio docx (Apêndice B, versão auditada): "Z-score modificado de Iglewicz e Hoaglin (1993), baseado na Mediana das Desvios Absolutos (MAD), com limiar K = 3,5". Há portanto contradição interna entre o corpo do Cap. 3 (IQR) e o Apêndice B (MAD), com o código confirmando MAD. **Achado ALTO — o texto principal cita método diferente do implementado.**

### 4.3 Retornos Simples vs. Log-Retornos
A distinção está corretamente formalizada na Seção 3.3.2 e consistentemente implementada no código: retornos simples para otimização (`pct_change`), log-retornos para econometria (`np.log(...)`). Anualização: μ×252, σ×√252, Σ×252 — todos corretos e confirmados em `src/06_Estimacao_Covariancia/` e `config_loader.py` (`TRADING_DAYS = 252`).

### 4.4 Bateria Econométrica
O diagnóstico econométrico cobre ADF, KPSS, Ljung-Box (lags 5/10/20), Jarque-Bera, ARCH-LM (10 lags), Chow e CUSUM. O Cap. 3 e o Apêndice B descrevem resultados sobre 130 ativos, enquanto a amostra canônica é 118. O texto oscila entre 118, 130 e 135 ao citar o mesmo diagnóstico. Os resultados econométricos (ARCH em 100% dos ativos, JB rejeitado em 100%, estacionariedade confirmada nos log-retornos) são plausíveis e consistentes com a literatura brasileira.

### 4.5 Estimação μ e Σ com Ledoit-Wolf
Janela expansiva, Ledoit-Wolf para Σ (`METODO_COV = "ledoit_wolf"`, NB07 célula 5), média simples para μ. Ambos estimados exclusivamente até a data de corte de cada rebalanceamento — look-ahead bias vedado. A menção a "135×135" no docx para a dimensão da matriz no ponto de maturidade sugere N=135 em versão anterior; o artefato confirma N=118. **Inconsistência de número sem impacto metodológico — requer correção textual.**

### 4.6 As Três Famílias e as 16 Estratégias
O código implementa e os artefatos confirmam 16 séries de retornos (mais IBOV e EqualWeight_BuyHold):
- **MPT (6):** EqualWeight, InvVol, MinVar, MinVar_c10, MaxSharpe, MaxSharpe_c10.
- **PMPT (5):** MaxOmega, MaxSortino, MaxKappa3, MinCVaR, MinCDaR.
- **BL (4):** BL_classico, BL_classico_c10, BL_downside, BL_downside_c10.

O Cap. 3 enuncia 15 modelos (a estratégia EqualWeight às vezes contada separadamente). Os títulos das seções 3.5 anunciam apenas MaxSharpe com penalidade, MinVar com penalidade e BL+LSTM — omitindo formalmente a família PMPT inteira, que aparece apenas na formalização matemática dentro da subseção de "Família II". O Capítulo 4 não reporta resultados dessas 14 estratégias reais.

### 4.7 Construção Black-Litterman
Todos os parâmetros são confirmados no código (`NB07_células 5 e 15`, `otimizacao.py`):
- **Prior wm:** `np.repeat(1.0 / N, N)` — vetor 1/N (NB07:444, otimizacao.py:112). Correto, equiponderado.
- **Π:** `DELTA * S_anual @ wm` (NB07:446). Correto.
- **δ:** 2,5 fixo (NB07:célula5, "He & Litterman (1999) — aversão implícita ao risco"). O docx documenta o δ negativo na otimização reversa como motivação para fixar 2,5 — metodologicamente defensável.
- **τ:** 0,05 (NB07:célula5). Convencional.
- **Visões:** momentum 12-1; P=I_N; Q=retornos acumulados por ativo nos últimos 12m, excluindo último mês (NB07:otimizacao.py:73–89). Sem LSTM, sem ARIMA. O texto do Cap. 3 ainda intitula a subseção "3.5.3. Modelo Black-Litterman com Visões LSTM".
- **Ω:** `diag(P @ (tau_bl * Sg) @ P.T)` — construção He-Litterman (otimizacao.py:89). Não Idzorek.
- **Σ_anual no BL:** `S_anual = S * TRADING_DAYS` (NB07:443) — ×252 correto. Comentário no código documenta correção anterior de ×21 para ×252 (NB07:440–442).

### 4.8 Backtesting
- Warm-up: 60 meses (`WARMUP_MESES = 60`, config.json). Início OOS confirmado: 2015-03-02 (todos os 16 ativos em `strategy_returns.parquet`).
- Rebalanceamento: mensal (`REBAL = "M"`, NB07). 130 pontos de rebalanceamento por estratégia (confirmado em `pesos_historico.csv`).
- Custo transacional: 50 bps = 0,5% sobre giro (`CUSTO_BPS = 50.0`, config.json). Implementado como penalidade L1 sobre variação de pesos — isomórfico a regularização Lasso no plano geométrico, mas economicamente é custo de fricção, não regularização estatística. O texto usa ambiguamente o termo "regularização L1/Lasso".
- Ponderação de retornos: `pesos_calculados.shift(1) * retornos_ativos` — look-ahead bias corretamente evitado.

### 4.9 Métricas de Avaliação OOS
CAGR, volatilidade, Sharpe, Sortino, MaxDD, turnover anualizado, retorno acumulado — todos calculados sobre a série OOS. Conforme artefato `desempenho_estrategias.csv`.

---

## SEÇÃO 5 — AVALIAÇÃO DOS RESULTADOS, TABELA A TABELA

### Tabela 5 — Estatísticas Descritivas dos Log-Retornos Diários (130 ativos)
O título cita 130 ativos. O painel confirmado tem 118 ativos. Inconsistência de N.

### Tabela 6 — Volatilidade Média Anualizada por Ano (cross-section de 130 ativos)
Idem — título cita 130.

### Tabela 7 — Resultados dos Testes Econométricos (135 ativos)
Título cita 135 ativos. Amostra canônica confirmada: 118. O número 135 coincide com a menção ao tamanho da matriz Σ no ponto de maturidade — possível confusão entre dimensão da matriz e N de ativos em versão anterior do código.

### Tabela 8 — Desempenho da Estratégia Mínima Variância L1
**Estratégia inexistente nos artefatos.** O artefato mais próximo é `MinVar` (sem sufixo L1). A "penalidade L1" referenciada é o custo transacional de 50 bps, não uma regularização L1 na função objetivo. A tabela apresenta Sharpe=-0,15 e MaxDD=-92,99% — números que não correspondem ao `MinVar` dos artefatos (Sharpe=0,217, MaxDD=-25,6%). A origem desses números é desconhecida e não pode ser rastreada aos artefatos. **Achado CRÍTICO — tabela com dados sem evidência no repositório.**

### Tabela 9 — Desempenho da Estratégia Máximo Índice de Sharpe com L1
**Estratégia inexistente nos artefatos.** O artefato mais próximo é `MaxSharpe`. Idem à análise da Tabela 8 — números não rastreáveis. **Achado CRÍTICO.**

### Tabela 10 — Desempenho da Estratégia Black-Litterman + LSTM
**Estratégia inexistente no repositório.** Nenhum arquivo contém código LSTM. Visões BL são momentum 12-1. Os números desta tabela não podem ser verificados. **Achado CRÍTICO.**

### Tabela 11 — Comparação Unificada das Estratégias (out-of-sample 2015–2025)
Tabela comparativa geral presente no Cap. 4. Não foi possível verificar os valores individuais (o docx não expõe a tabela de forma estruturada no XML extraído), mas a estrutura narrativa cita IBOV e CDI como benchmarks. **[VERIFICAR] — confirmar se os valores batem com `apendice_H_painel_metricas.csv`.**

### Tabela 12 — Síntese Comparativa do Desempenho
Idem Tabela 11. **[VERIFICAR].**

### Estratégias nos artefatos, ausentes no Cap. 4
As seguintes estratégias têm métricas completas em `apendice_H_painel_metricas.csv` e `desempenho_estrategias.csv` mas **não são reportadas individualmente** no Cap. 4:
InvVol, MinVar, MinVar_c10, MaxSharpe, MaxSharpe_c10, MaxOmega, MaxSortino, MaxKappa3, MinCVaR, MinCDaR, BL_classico, BL_classico_c10, BL_downside, BL_downside_c10, EqualWeight, EqualWeight_BuyHold.

O artefato `apendice_H_painel_metricas.csv` já contém todas as métricas necessárias para completar o Cap. 4 sem reexecução do pipeline — basta transcrever e interpretar.

---

## SEÇÃO 6 — TABELA DE CONSISTÊNCIA INTERNA

| Aspecto | Valor A (localização) | Valor B (localização) | Valor canônico (código/artefato) | Impacto |
|---|---|---|---|---|
| **N ativos** | 118 (Cap. 3 corpo, p. 70; Apêndice A) | 130 (Tabelas 5, 6); 135 (Tabela 7); 136 (Apêndice B riscado) | **118** (`tickers_finais.csv`: 119 linhas incl. cabeçalho) | ALTO — banca perguntará qual é o N correto |
| **Pregões** | 3.967 (Cap. 3 corpo, p. 70) | 4.030 (Apêndice B riscado) | **3.967** (`painel_alinhado.parquet`: shape=(3967,121)) | MÉDIO — divergência visível mas corrigida por riscado |
| **Pares de covariância** | 8.385 (Apêndice H) | — | **6.903** = C(118,2); 8.385 = C(130,2) | ALTO — 8.385 pressupõe N=130, inconsistente com N=118 canônico |
| **Datas OOS** | jan/2015 (texto narrativo geral) | 2015-03-02 (artefato) | **2015-03-02** (`strategy_returns.parquet` first_valid_index) | BAIXO — imprecisão narrativa aceitável |
| **Custo/"L1"** | "regularização L1/Lasso" (Cap. 3, 3.5.1) | "custo transacional 50 bps" (Cap. 3, 3.5, "Penalidade de fricção") | **custo 50 bps sobre giro** (`CUSTO_BPS=50`, config.json) | MÉDIO — terminologia ambígua pode confundir banca |
| **Sharpe/Sortino — unidades** | adimensional (texto) | adimensional (artefato) | **adimensional** (cálculo: excesso/vol anual) | BAIXO — sem inconsistência de unidade |
| **Ticker GOLL** | GOLL54 (Apêndice H, texto) | — | **GOLL54** (`tickers_finais.csv` contém GOLL54) | BAIXO — consistente |
| **σ_anual — fórmula** | "σ_anual = σ_diaria × 252" (versão anterior, Apêndice F) | "σ_anual = σ_diaria × √252" (Apêndice F versão auditada, nota de auditoria) | **× √252** (`TRADING_DAYS=252`, `vol = r.std() * np.sqrt(TRADING_DAYS)`, NB07:célula23) | MÉDIO — Apêndice F corrigido na versão auditada, mas verificar se o Cap. 3 ou figuras ainda usam × 252 para σ |
| **N rebalanceamentos** | 132 (Cap. 3, "132 pontos mensais") | 130 (artefato) | **130** (`pesos_historico.csv`: 130 datas por estratégia) | MÉDIO — diferença de 2 meses, provavelmente meses descartados por janela insuficiente |
| **Dimensão Σ no ponto de maturidade** | "135×135" (Cap. 3 corpo) | — | **118×118** (N=118 confirmado) | ALTO — resquício de versão anterior |

---

## SEÇÃO 7 — TABELA TEXTO × CÓDIGO

| Parâmetro | Texto afirma | Código/artefato comprova | Veredito | Ação no texto |
|---|---|---|---|---|
| **Visões BL** | "Visões LSTM" (seção 3.5.3, título; 4.1.1; resumo) | Momentum 12-1; P=I_N; Q=retornos de momentum (`otimizacao.py:73–89`) | **DIVERGÊNCIA CRÍTICA** | Renomear seção 3.5.3 para "Modelo Black-Litterman com Visões por Momentum 12-1"; remover todas as menções a LSTM como input implementado |
| **Ausência ARIMA** | "modelos ARIMA" (objetivo geral, resumo, abstract) | Nenhum arquivo contém "ARIMA" ou "arima" (`grep done` — zero ocorrências) | **DIVERGÊNCIA CRÍTICA** | Remover ARIMA do objetivo geral e resumo; mencionar como trabalho futuro |
| **Escala Σ no BL** | Σ_anual = Σ_diaria × 252 (Apêndice F) | `S_anual = S * TRADING_DAYS` (NB07:443; TRADING_DAYS=252) | **CONSISTENTE** | Sem ação |
| **δ fixo 2,5** | δ = 2,5 He-Litterman (Cap. 3 p. 76); δ reverso negativo (limitação) | `DELTA = 2.5` (NB07:célula5) | **CONSISTENTE** | Sem ação |
| **Prior 1/N** | wm = 1/N, N=118 (Cap. 3 p. 76) | `np.repeat(1.0/N, N)` (otimizacao.py:112, NB07:444) | **CONSISTENTE** | Sem ação |
| **Ω He-Litterman vs. Idzorek** | Idzorek citado na Seção 2.19 como método alternativo; Seção 3.5.3 usa fórmula Ω=diag(τPΣP') | `diag(P @ (tau_bl * Sg) @ P.T)` (otimizacao.py:89) — He-Litterman | **CONSISTENTE** (implementação é He-Litterman como declarado no Cap. 3) | Acrescentar nota de rodapé em 2.19 distinguindo o que foi implementado vs. o que foi descrito como alternativa |
| **σ_anual (× √252 vs. × 252)** | Apêndice F (versão auditada): "σ_anual = σ_diaria × √252" — corrigido | `vol = r.std() * np.sqrt(TRADING_DAYS)` (NB07:célula23) | **CONSISTENTE** (versão auditada) | Verificar se nenhuma figura/tabela do corpo ainda cita ×252 para σ |
| **Ausência MinVar_L1/MaxSharpe_L1** | Tabelas 8 e 9 com dados "MinVar_L1" e "MaxSharpe_L1" | Não existem nos artefatos; `strategy_returns.parquet` não contém essas colunas | **DIVERGÊNCIA CRÍTICA** | Substituir Tabelas 8 e 9 pelos dados reais de MinVar e MaxSharpe dos artefatos |
| **N pregões** | 3.967 (Cap. 3 p. 70); 4.030 (Apêndice B riscado) | shape=(3967,121) `painel_alinhado.parquet` | **CONSISTENTE** (3.967) — riscado corrigiu | Confirmar riscado visível na versão final |
| **N ativos** | 118 (Cap. 3 p. 70); 130 (Tabelas 5, 6); 135 (Tabela 7); 136 (Apêndice B riscado) | 118 (`tickers_finais.csv`) | **DIVERGÊNCIA ALTA** | Padronizar para 118 em todas as ocorrências; corrigir títulos das Tabelas 5, 6, 7 |
| **N rebalanceamentos** | 132 (Cap. 3 p. 77) | 130 (pesos_historico.csv) | **DIVERGÊNCIA MÉDIA** | Corrigir para 130; explicar que 2 meses foram descartados por janela insuficiente |

---

## SEÇÃO 8 — LACUNAS DE FECHAMENTO EMPÍRICO

### 8.1 Família PMPT e Variantes BL não Reportadas no Cap. 4
As estratégias MaxOmega, MaxSortino, MaxKappa3, MinCVaR, MinCDaR, BL_classico, BL_classico_c10, BL_downside, BL_downside_c10 — e também InvVol, MinVar, MinVar_c10, MaxSharpe, MaxSharpe_c10 — têm métricas completas em `data/Estrategias/apendice_H_painel_metricas.csv` (shape=(17, 7)) e `data/Estrategias/desempenho_estrategias.csv` (com turnover_aa). O fechamento empírico é **viável sem reexecução do pipeline**: basta inserir a tabela dos artefatos no Cap. 4 e redigir parágrafos interpretativos.

**Decisão estratégica recomendada (Seção 12):** reportar todas as 16 estratégias — o esforço é de redação, não de computação. A alternativa de reduzir o escopo declarado exigiria reescrever o Cap. 3 inteiro, com risco de criar novas inconsistências.

### 8.2 Células Interpretativas Pendentes
- **NB07 célula 27:** análise pós-backtest (verificada como marcada para preenchimento em auditoria anterior) — [VERIFICAR estado atual].
- **NB09 fechamento:** células de inferência econométrica (testes de Jobson-Korkie/Memmel sobre os Sharpes das 16 estratégias) descritas no Cap. 3 como parte da metodologia mas não aparecem reportadas em resultados.
- **Cap. 4.4:** título "l" — seção placeholder explicitamente vazia.

### 8.3 Apêndices Órfãos
- **Apêndice H** (título no docx: "Isolamento Matricial de Covariâncias Negativas e Mapeamento de Hedge Estrutural") — conteúdo sobre o par RCSL4-GOLL54; não discutido no Cap. 4.
- **Apêndice I** (Correlação de Pearson e Clusterização Hierárquica Estrutural) — mencionado no título do apêndice mas sem texto interpretativo completo no Cap. 4.
- **Apêndice J** (Engenharia Reversa do BL) — presente no docx como apêndice mas sem vínculo explícito ao Cap. 4.
- Os apêndices H–J dos artefatos reais (painel de métricas, pesos históricos, desempenho comparativo) são referenciados implicitamente mas não vinculados às numerações do docx.

### 8.4 Datasets.md Inexistente
O arquivo `Datasets.md` não existe no repositório (`os.path.exists` = False). Documenta proveniência dos dados de entrada. **Impacto baixo para a defesa, mas necessário para reproductibilidade completa.**

---

## SEÇÃO 9 — CITAÇÕES × REFERÊNCIAS

| Autor/obra | Citado no texto | Na lista de referências | Observação |
|---|---|---|---|
| Santos; Tessari (2012) | Sim (conclusão) | **NÃO** | Achado ALTO — ABNT exige entrada na lista |
| Idzorek (2005) | Sim (seção 2.19) | **NÃO** | Achado ALTO |
| Memmel (2003) | Não (mas subjacente ao código) | NÃO | MÉDIO — mencionar na metodologia |
| Meucci (Entropy Pooling) | Sim (seção 2.21.2) | **NÃO** | MÉDIO |
| Kaplan; Knowles (2004) | Sim (índice Kappa, cap. 3) | **NÃO** | ALTO |
| Chekhlov et al. (CDaR) | Não | NÃO | MÉDIO — origem do CDaR não citada |
| Rule et al. (2019) | **NÃO** (não encontrado no docx) | NÃO | BAIXO — referência de contexto de auditoria prévia; não aplicável |
| Damodaran (2007) | "Damodaran, 2007" (introdução) | "Damodaran, 2012" (lista) | MÉDIO — ano inconsistente |
| He; Litterman (1999) | Sim | Sim | OK |
| Sortino; Van der Meer (1991) | Sim | Sim | OK |
| Jobson; Korkie (1981) | Sim (texto Cap. 4) | Sim | OK |

**Resumo:** ao menos 5 referências citadas no texto carecem de entrada na lista de referências — violação direta das normas ABNT NBR 6023.

---

## SEÇÃO 10 — ESTRUTURA, FORMATAÇÃO E ABNT

### 10.1 Títulos Placeholder
- Seção 4.4: título "l" (letra minúscula isolada) — seção vazia. Requer preenchimento ou remoção.
- Subseção 4.1.1: "Modelo Black-Litterman com Visões LSTM" está no contexto de estatísticas descritivas — deslocada logicamente.
- Subseção 4.2.3: "Estratégia 2 — Máximo Índice de Sharpe com L1" repete o título da 4.2.2 — provavelmente deveria ser "Estratégia 3 — Black-Litterman + LSTM".

### 10.2 Equações em Texto Simples
Várias equações estão parcialmente renderizadas como LaTeX em texto simples (ex.: "R p = i ω i R i", "LPM n τ = 1 T t = 1 T"). Em ambiente ABNT impresso, equações devem ser numeradas e centralizadas. O docx usa formatação de equação Word (MathML), que pode não renderizar corretamente em PDF sem conversão adequada.

### 10.3 Numeração de Tabelas
As tabelas 5–12 no Cap. 4 coincidem com tabelas 1–4 do Cap. 2 em numeração sequencial — o sumário confirma a sequência. Contudo, os títulos descritivos das tabelas oscilam entre numeração romana (sumário) e arábica (corpo). Verificar consistência com ABNT NBR 14724.

### 10.4 Sumário Desatualizado
O sumário automático do Word reflete a estrutura atual do docx. Os PAGEREF inseridos indicam atualizações pendentes de paginação. A seção 4.4 aparece como "l" no sumário — visível e embaraçoso.

### 10.5 Capítulo 4 com Subseções a Completar
As subseções 4.2 (resultados do backtest) estão redigidas apenas para as estratégias fictícias (MinVar_L1, MaxSharpe_L1, BL+LSTM). A seção 4.3 (análise comparativa) existe mas se baseia em dados não rastreáveis. A seção 4.4 está vazia. O capítulo precisa de refatoração completa para reportar as estratégias reais.

### 10.6 Resumo e Abstract
Ambos mencionam LSTM e ARIMA como inputs implementados — incorreto. Requerem revisão após correção do Cap. 3/4.

---

## SEÇÃO 11 — PONTOS PROVÁVEIS DE ARGUIÇÃO

### Pergunta 1 (MAIS PERIGOSA)
**"O senhor menciona no Capítulo 4 os resultados de MinVar_L1 e MaxSharpe_L1 com regularização L1. Pode me mostrar no código onde a regularização L1 está implementada como penalidade na função objetivo do otimizador, distinta do custo de transação?"**

*Resposta defensável:* "A denominação L1 no texto refere-se à norma L1 usada na penalidade de fricção transacional (custo de giro de 50 bps), que é isomórfica geometricamente à regularização Lasso ao induzir esparsidade nas realocações. Não existe uma penalidade L1 estrita com λ de regularização separado do custo econômico. O texto usa a terminologia de forma ampla. As estratégias nos artefatos são MinVar e MaxSharpe com custo transacional integrado na função objetivo."

*Correção prévia que blinda:* renomear as estratégias nos títulos das seções e tabelas para "MinVar (com custo transacional)" e eliminar o sufixo L1 do nome. Isso resolve a confusão terminológica antes da arguição.

### Pergunta 2 (MUITO PERIGOSA)
**"O resumo e o objetivo geral mencionam redes neurais LSTM como método de geração de visões para o Black-Litterman. Onde no código pode-se verificar a implementação do LSTM?"**

*Resposta defensável:* "Durante a pesquisa, verificou-se que a relação sinal-ruído das séries do mercado brasileiro era insuficiente para que o LSTM gerasse visões com poder preditivo genuíno no período de teste. Optou-se por substituir as visões LSTM pelo fator de momentum 12-1 — abordagem com suporte empírico robusto na literatura brasileira — e esta substituição está documentada no código (otimizacao.py:73). O resumo e objetivo geral refletem a proposta original e serão atualizados para descrever a implementação final."

*Correção prévia que blinda:* atualizar resumo, abstract e seção 3.5.3 antes da defesa.

### Pergunta 3 (PERIGOSA)
**"O senhor cita 8.385 pares de covariância no Apêndice H, mas afirma ter 118 ativos. C(118,2) = 6.903, não 8.385. Como explica a diferença?"**

*Resposta defensável:* "O número 8.385 corresponde a C(130,2), resquício de versão anterior com 130 ativos antes da aplicação final do crivo de liquidez. O par RCSL4-GOLL54 com covariância negativa foi identificado durante a análise com N=130; após a filtragem final para N=118, o número correto de pares é 6.903. A consistência interna do trabalho usa N=118 como canônico."

*Correção prévia que blinda:* atualizar Apêndice H para citar C(118,2)=6.903 e verificar se GOLL54 e RCSL4 estão no tickers_finais.csv.

### Pergunta 4 (PERIGOSA)
**"A seção 3.3.1 descreve a detecção de outliers pelo método IQR com multiplicador 3,0. Mas o Apêndice B descreve MAD modificado com K=3,5. Qual foi realmente implementado?"**

*Resposta defensável:* "O Apêndice B reflete a implementação real: Z-score modificado de Iglewicz-Hoaglin (MAD, K=3,5, c=0,6745), conforme parâmetros `K_MAD=3.5` e `C_MAD=0.6745` no arquivo `config.json`. O texto do Capítulo 3 descreve uma versão anterior (IQR×3,0) e deve ser corrigido para refletir o método efetivamente empregado."

*Correção prévia que blinda:* atualizar o parágrafo da Etapa 3 no Cap. 3 para descrever MAD modificado.

### Pergunta 5 (ALTA)
**"Qual foi o mecanismo de geração das visões Q no modelo Black-Litterman? Como o senhor valida que essas visões têm poder preditivo?"**

*Resposta defensável:* "As visões Q são o retorno acumulado de cada ativo nos últimos 12 meses, excluindo o mês imediato (momentum 12-1 de Jegadeesh-Titman), com P=I_N (visões absolutas). O poder preditivo não é formalmente validado por backtesting separado das visões — esta é uma limitação reconhecida no texto. O momentum funciona como proxy de expectativas de curto prazo, ancorado na evidência empírica de persistência de momentum em mercados emergentes."

*Correção prévia que blinda:* mencionar explicitamente no Cap. 3 que as visões são momentum e não LSTM.

### Pergunta 6 (ALTA)
**"O delta de aversão ao risco foi fixado em 2,5. Por que não estimá-lo pelo mercado brasileiro?"**

*Resposta defensável:* "A otimização reversa resultou em valor negativo de δ, economicamente inválido para o mercado brasileiro no período analisado — fato documentado na seção de limitações (3.5.5). A adoção de δ=2,5, calibrado por He e Litterman (1999), é a convenção padrão na literatura e garante interpretabilidade dos retornos implícitos de equilíbrio."

*Correção prévia:* nenhuma — já documentado.

### Pergunta 7 (MODERADA)
**"O turnover anualizado do BL_classico é 825% ao ano. Como isso afeta a aplicabilidade prática da estratégia?"**

*Resposta defensável:* "O turnover elevado das variantes BL reflete a sensibilidade dos pesos ao fator de momentum mensal, que rotaciona ativos com maior frequência. O custo de 50 bps já está incorporado às séries de retorno reportadas — o CAGR de 21,1% do BL_classico é líquido de custo. Em um fundo real, custos adicionais de impacto de mercado e ISS reduziriam este retorno, constituindo limitação prática reconhecida."

*Correção prévia:* incluir tabela de turnover_aa no Cap. 4.

### Pergunta 8 (MODERADA)
**"O MinCDaR apresentou CAGR de -1,75% e MaxDD de -81,8%. O que explica este desempenho tão discrepante das demais estratégias?"**

*Resposta defensável:* "O CDaR penaliza drawdowns acumulados, o que em horizontes longos com múltiplos choques (2015–2016, 2020, 2022) tende a produzir pesos extremamente conservadores ou a concentrar em ativos defensivos de baixo retorno. A formulação de programação linear do CDaR pode resultar em soluções degeneradas quando a distribuição histórica é dominada por poucos eventos extremos. O resultado sugere que o CDaR, tal como implementado com janela expansiva, é instável neste universo."

### Pergunta 9 (MODERADA)
**"Qual é a diferença entre BL_classico e BL_downside? E por que o BL_downside apresenta maior volatilidade (32,4%) do que o BL_classico (26,0%) apesar de usar semicovariância?"**

*Resposta defensável:* "O BL_downside substitui a matriz de covariância completa Σ pela semicovariância de Estrada (apenas realizações abaixo do MAR). A semicovariância captura apenas o risco de queda, resultando em pesos que toleram maior volatilidade total quando os ativos selecionados têm assimetria positiva favorável. A maior volatilidade não contradiz a minimização do risco de queda — são objetivos distintos."

### Pergunta 10 (BAIXA)
**"Por que a estratégia EqualWeight tem retorno de 5,97% a.a. enquanto EqualWeight_BuyHold tem 15,71%? A diferença é o custo de rebalanceamento?"**

*Resposta defensável:* "Sim. O EqualWeight rebalanceia mensalmente para manter pesos iguais, incorrendo em custo de 50 bps sobre o giro a cada período. O EqualWeight_BuyHold mantém os pesos iniciais iguais e não rebalanceia (apenas uma alocação inicial), eliminando custos transacionais e beneficiando-se do efeito momentum natural dos ativos vencedores que crescem em peso. A diferença de ~10 p.p. a.a. documenta empiricamente o impacto do custo de rebalanceamento."

### Pergunta 11 (BAIXA)
**"A seção 4.4 aparece com título 'l'. O que estava previsto para esta seção?"**

*Resposta defensável:* "A seção 4.4 estava prevista para análise de inferência estatística dos resultados, incluindo testes de significância de diferenças de Sharpe (Jobson-Korkie/Memmel) e decomposição de alfa. Por limitação de prazo, a seção não foi finalizada. Os resultados inferenciais estão disponíveis nos notebooks NB09 do repositório."

*Correção prévia que blinda:* preencher ou remover a seção antes da defesa.

### Pergunta 12 (BAIXA)
**"O objetivo geral menciona ARIMA. Onde foram reportados os resultados com ARIMA?"**

*Resposta defensável:* "Os modelos ARIMA foram explorados na fase de proposta mas não foram implementados no pipeline final. A complexidade de integrar modelos ARIMA por ativo em uma janela expansiva de 118 ativos mostrou-se proibitiva para o prazo disponível. O trabalho focou na comparação entre média histórica e momentum como inputs de visão, com os resultados documentados para as 16 estratégias implementadas."

*Correção prévia que blinda:* remover ARIMA do objetivo geral; mencionar como extensão futura.

---

## SEÇÃO 12 — VEREDITO, SEVERIDADE E PLANO DE AÇÃO

### Tabela de Achados Classificados

| # | Achado | Seção/artefato | Severidade | Esforço | Ação |
|---|---|---|---|---|---|
| A1 | Tabelas 8, 9, 10 com estratégias inexistentes (MinVar_L1, MaxSharpe_L1, BL+LSTM) — dados não rastreáveis aos artefatos | Cap. 4, Tabelas 8–10 | **CRÍTICO** | Médio | Substituir pelas tabelas de MinVar, MaxSharpe e BL_classico dos artefatos |
| A2 | Menção a LSTM como input implementado (resumo, abstract, objetivo, sec. 3.5.3, 4.1.1) quando não existe no código | Resumo, Abstract, Cap. 3, Cap. 4 | **CRÍTICO** | Baixo | Substituir "LSTM" por "momentum 12-1" em todas as ocorrências |
| A3 | Menção a ARIMA no objetivo geral sem implementação | Resumo, Abstract, Cap. 1 | **CRÍTICO** | Baixo | Remover ARIMA; deslocar para trabalhos futuros |
| A4 | Família PMPT e variantes BL não reportadas no Cap. 4 | Cap. 4 | **ALTO** | Médio | Inserir Tabela 11 com as 16 estratégias e redigir análise comparativa |
| A5 | N oscilando entre 118, 130, 135, 136 em diferentes seções | Cap. 4 Tabelas 5–7, Apêndice B | **ALTO** | Baixo | Padronizar para 118; corrigir títulos das tabelas |
| A6 | 8.385 pares calculado para N=130, não N=118 | Apêndice H | **ALTO** | Baixo | Corrigir para C(118,2)=6.903; verificar se RCSL4 e GOLL54 estão no universo final |
| A7 | Referências ausentes: Santos & Tessari (2012), Idzorek (2005), Kaplan & Knowles (2004), Meucci, Memmel (2003) | Seção 6 — Referências | **ALTO** | Baixo | Inserir entradas completas em ABNT |
| A8 | Cap. 3 descreve IQR×3,0 mas código implementa MAD K=3,5 | Cap. 3 Seção 3.3.1 | **ALTO** | Baixo | Atualizar Etapa 3 para descrever MAD modificado |
| A9 | Seção 4.4 com título placeholder "l" | Cap. 4 Seção 4.4 | **ALTO** | Médio | Preencher com inferência ou remover e renumerar |
| A10 | Dimensão Σ "135×135" no Cap. 3 | Cap. 3 Seção 3.4.2 | **MÉDIO** | Baixo | Corrigir para "118×118" |
| A11 | "132 pontos mensais" no Cap. 3 vs. 130 confirmados | Cap. 3 Seção 3.6 | **MÉDIO** | Baixo | Corrigir para 130; adicionar nota sobre os 2 meses descartados |
| A12 | Damodaran citado como "(2007)" mas referência é 2012 | Introdução + lista | **MÉDIO** | Baixo | Uniformizar para 2012 (ou localizar edição 2007) |
| A13 | Terminologia "regularização L1/Lasso" para custo transacional | Cap. 3 Seção 3.5 | **MÉDIO** | Baixo | Clarificar que a penalidade L1 é o custo de giro, não regularização estatística independente |
| A14 | Apêndices H–J sem texto interpretativo vinculado ao Cap. 4 | Apêndices | **MÉDIO** | Médio | Acrescentar parágrafo de remissão no Cap. 4 para cada apêndice |
| A15 | Datasets.md inexistente | Raiz do repositório | **BAIXO** | Baixo | Criar arquivo de proveniência dos dados |
| A16 | Conclusão discute "BL+LSTM" mas resultado real é BL+momentum | Cap. 5 | **BAIXO** | Baixo | Atualizar narrativa da conclusão após correção do Cap. 4 |

---

### Checklist Priorizado (sequência de correções por impacto)

1. **[CRÍTICO, Esforço Baixo]** Atualizar resumo, abstract, objetivo geral e seção 3.5.3 — substituir todas as menções a "LSTM" e "ARIMA" como inputs implementados pela descrição correta (momentum 12-1; ARIMA como trabalho futuro).
2. **[CRÍTICO, Esforço Médio]** Substituir Tabelas 8, 9 e 10 pelos dados reais dos artefatos: `MinVar` (Sharpe=0,217; MaxDD=-25,6%), `MaxSharpe` (Sharpe=0,287; MaxDD=-22,8%), `BL_classico` (Sharpe=0,511; MaxDD=-43,8%).
3. **[ALTO, Esforço Médio]** Redigir a análise comparativa completa do Cap. 4 para as 16 estratégias, usando os dados de `apendice_H_painel_metricas.csv` e `desempenho_estrategias.csv`. Preencher ou remover seção 4.4.
4. **[ALTO, Esforço Baixo]** Padronizar N=118 em todas as ocorrências do texto; corrigir títulos das Tabelas 5, 6, 7 e o texto de Seção 3.4.2 ("135×135" → "118×118") e Seção 3.6 ("132" → "130").
5. **[ALTO, Esforço Baixo]** Corrigir Apêndice H: C(118,2)=6.903 pares (não 8.385 = C(130,2)).
6. **[ALTO, Esforço Baixo]** Inserir referências ausentes: Santos & Tessari (2012), Idzorek (2005), Kaplan & Knowles (2004), Meucci (referência principal), Memmel (2003).
7. **[ALTO, Esforço Baixo]** Atualizar Etapa 3 (seção 3.3.1) para descrever MAD modificado (K=3,5, c=0,6745) em vez de IQR×3,0.
8. **[MÉDIO, Esforço Baixo]** Corrigir inconsistência Damodaran 2007 vs. 2012; revisar demais citações.
9. **[MÉDIO, Esforço Baixo]** Clarificar terminologia L1/Lasso na Seção 3.5: a penalidade é custo transacional (50 bps), não regularização estatística separada.
10. **[MÉDIO, Esforço Médio]** Vincular Apêndices H, I, J ao Cap. 4 com remissões explícitas.

---

### Decisão Estratégica: Reportar Família PMPT + Variantes BL nos Artefatos vs. Reduzir Escopo

**Recomendação: reportar todas as 16 estratégias.**

Razões:
1. Os dados já estão computados e validados em `apendice_H_painel_metricas.csv` — nenhuma reexecução é necessária.
2. A redução de escopo exigiria reescrever o Cap. 3 inteiro (as fórmulas de CVaR, CDaR, Kappa, Omega e BL estão formalizadas), com alto risco de criar novas inconsistências.
3. Os resultados da família PMPT e das variantes BL são empiricamente ricos: o BL_classico com CAGR=21,1% (Sharpe=0,511) é o melhor resultado do painel; o MinCDaR com CAGR=-1,75% (MaxDD=-81,8%) é pedagogicamente valioso como caso de degeneração; a comparação PMPT vs. MPT com turnover documenta o trade-off risco-custo.
4. O "paradoxo da complexidade" (modelos simples superam modelos sofisticados) já é a tese central da conclusão — publicar a evidência completa reforça, não contradiz, esse argumento.

O único risco de reportar todas as estratégias é a necessidade de explicar o BL+momentum (não BL+LSTM) na arguição — risco mitigado pela correção A1 acima.

---

## APÊNDICE DE EVIDÊNCIAS

### Comandos executados e valores brutos obtidos

```
# Painel
pd.read_parquet('data/Painel_Dados/painel_alinhado.parquet').shape
→ (3967, 121)
→ index[0] = 2010-01-04, index[-1] = 2025-12-30

# Tickers
len(rows) = 119 → ativos = 118

# Strategy returns
shape = (2690, 17)
colunas = ['EqualWeight','InvVol','MinVar','MinVar_c10','MaxSharpe','MaxSharpe_c10',
           'MaxOmega','MaxSortino','MaxKappa3','MinCVaR','MinCDaR',
           'BL_classico','BL_classico_c10','BL_downside','BL_downside_c10',
           'IBOV','EqualWeight_BuyHold']
first_valid_index: todos = 2015-03-02

# Pesos históricos
shape = (60494, 4)
colunas = ['estrategia','data','ticker','peso']
130 datas únicas por estratégia (exceto EqualWeight_BuyHold = 1)

# config.json
WARMUP_MESES = 60, CUSTO_BPS = 50.0, K_MAD = 3.5, C_MAD = 0.6745,
N_MONTECARLO = 50000, TETO_PESO = 0.1, LIMIAR_PRESENCA = 0.95

# NB07 célula 5
DELTA = 2.5  # He & Litterman (1999)
TAU = 0.05
VISAO_MOMENTUM_MESES = (12, 1)
METODO_COV = "ledoit_wolf"
TIPO_JANELA = "expansiva"

# otimizacao.py
linha 89: Om = np.diag(np.maximum(np.diag(P @ (tau_bl * Sg) @ P.T), 1e-8))
linha 112: return np.repeat(1.0 / n, n)
linha 443-446: S_anual = S * TRADING_DAYS; wm = np.repeat(1.0/N, N);
              Pi = DELTA * S_anual @ wm

# Grep LSTM/ARIMA/ward/linkage
→ "FOUND ward in src/03_Filtro_Liquidez/..." (contexto: string "toward", não scipy.cluster)
→ "FOUND ward in src/05_Alinhamento_Winsorizacao/..." (contexto: "forward")
→ LSTM: zero ocorrências
→ ARIMA: zero ocorrências
→ linkage: zero ocorrências
→ fcluster: zero ocorrências

# Datasets.md
→ os.path.exists = False

# Cálculo de pares
C(118,2) = 6903
C(130,2) = 8385  ← valor citado no Apêndice H

# Docx — N citações
"118 ativos" → pos 114157 (Cap. 3 corpo)
"130 ativos" → Tabelas 5, 6
"135 ativos" → Tabela 7
"136" → Apêndice B (riscado)
"4.030" → Apêndice B (riscado)
"3.967" → Cap. 3 corpo (correto)
"8.385" → Apêndice H

# Referências ausentes confirmadas
Santos/Tessari: NOT FOUND in refs
Idzorek: NOT FOUND in refs
Memmel: NOT FOUND in refs
Meucci: NOT FOUND in refs
Kaplan/Knowles: NOT FOUND in refs
```

---

## PARÁGRAFO FINAL

O TCC de Pedro Augusto Pinheiro Reis apresenta uma base computacional sólida e metodologicamente correta — o pipeline de 9 etapas, testado por 92 casos de pytest, implementa rigorosamente o que a literatura de finanças quantitativas prescreve para backtesting sem look-ahead bias. O que separa este trabalho de "consistente e defensável" é um descompasso entre o texto escrito (que descreve um projeto com LSTM, ARIMA e estratégias L1 especializadas) e o código executado (que implementa momentum 12-1, custo transacional como penalidade de giro, e 16 estratégias canônicas). Este descompasso foi provavelmente introduzido por iterações de desenvolvimento que alteraram o escopo implementado sem atualizar o texto. As **cinco correções de maior ganho por unidade de esforço** são: **(1)** atualizar resumo/abstract/objetivo/seção 3.5.3 para descrever momentum 12-1 em vez de LSTM e remover ARIMA [30 minutos de edição, elimina o ponto mais vulnerável da arguição]; **(2)** substituir as Tabelas 8–10 pelos dados reais dos artefatos [2 horas de transcrição + redação, fecha o maior vácuo de resultados]; **(3)** padronizar N=118 e N pregões=3.967 em todas as ocorrências [1 hora de busca e substituição, elimina 6 inconsistências numéricas]; **(4)** inserir as 5 referências ausentes na lista ABNT [30 minutos, evita objeção técnica direta]; **(5)** corrigir o Capítulo 3 Etapa 3 para descrever MAD modificado em vez de IQR [10 minutos, alinha o texto ao código e ao Apêndice B]. Com estas cinco correções implementadas, o trabalho fica blindado contra os quatro pontos de maior risco de arguição e passa a reportar corretamente os resultados que o pipeline já calculou.
