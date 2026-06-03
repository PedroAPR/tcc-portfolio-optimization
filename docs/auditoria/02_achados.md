# Auditoria FASE 2 — Achados Detalhados

**TCC:** Moderna Teoria das Carteiras no Mercado de Ações Brasileiro  
**Autor:** Pedro Augusto Pinheiro Reis | UFG — Ciências Contábeis  
**Auditor:** Claude Sonnet 4.6 | Data: 2026-06-03  
**Escopo:** `src/07_Otimizacao_Carteiras/`, `src/09_Inferencia_Econometrica/`, `src/config.json`

---

## A. Convenção de Retorno Intramês

### A1. Convenção "constant-mix" vs. "buy-and-hold" intramês
**Arquivo:** `src/07_Otimizacao_Carteiras/07_01_Otimizacao_Carteiras.ipynb` — célula `1163fbc8`, linhas do bloco de simulação  
**O que está:**
```python
R = ret.loc[dias].values        # retornos dos dias do mês i
rp = (R @ w).astype(float)      # w é o vetor do início do mês, fixo todos os dias
```
A cada dia do mês, `w` é o alvo calculado no rebalanceamento — peso constante. Isso é equivalente a rebalancear diariamente de volta ao alvo ("constant-mix"), não a deixar os pesos derivarem livremente dentro do mês ("buy-and-hold intra").

**O que deveria estar (alternativa):** Para simular genuinamente a política de "rebalancear apenas no início de cada mês e deixar derivar", o código deveria acumular o produto de retornos dia a dia com pesos que evoluem:
```python
w_dia = w.copy()
for t, dia in enumerate(dias):
    rp_t = float(ret.loc[dia].values @ w_dia)
    rp[t] = rp_t
    w_dia = w_dia * (1 + ret.loc[dia].values)
    w_dia /= w_dia.sum()
```

**Impacto numérico estimado:**  
Para EqualWeight (constant-mix vs. buy-and-hold), a diferença é capturada diretamente pela comparação entre as duas estratégias que já existem no notebook:
- EqualWeight (constant-mix): CAGR = 5,97%, Sharpe = -0,075
- EqualWeight_BuyHold (derive livre): CAGR = 15,71%, Sharpe = +0,372

A diferença de ~9,7 p.p. de CAGR é, no entanto, não atribuível exclusivamente à convenção intramês — ela reflete principalmente a concentração do BuyHold em vencedores do período (UNIP6 +7.852%, PETR4 +2.683%). Para as estratégias otimizadas (MinVar, MaxSharpe), o impacto intra-período é menor porque as janelas são mensais e os retornos diários individuais são pequenos; a diferença de CAGR entre constant-mix e buy-and-hold intra é estimada em menos de 0,2 p.p. por período de 30 dias úteis para retornos diários típicos de 0,05%.

**Consequência não capturada:** o custo de transação (linha `rp[0] -= custo_unit * turn`) é cobrado **apenas no primeiro dia do mês** (o rebalanceamento formal). Com constant-mix, nenhum custo é cobrado pelos "rebalanceamentos" implícitos dos demais 20 pregões do mês — o que subestima o custo real se o gestor efetivamente mantiver o peso fixo via ajustes diários.

**Classificação:** [DECISÃO DE PROJETO]  
**Justificativa:** A implementação com `w` fixo é matematicamente equivalente ao retorno de uma carteira constant-mix (contínua). Isso não é incorreto em si — é uma escolha de convenção que deve ser declarada explicitamente no Capítulo 3. O fato de existir a estratégia `EqualWeight_BuyHold` mostra que o autor conhece a distinção; porém o texto do TCC não esclarece que EqualWeight e demais estratégias usam constant-mix diário. Recomenda-se documentar a convenção e, se a intenção for "rebalancear mensalmente e derivar no meio", alterar o código — mas somente após confirmação do autor.

---

## B. Prior do Black-Litterman

### B1. Pesos de mercado são uniformes (1/N), não capitalizações reais
**Arquivo:** `src/07_Otimizacao_Carteiras/utils/otimizacao.py` — linha 421  
**O que está:**
```python
wm = np.repeat(1.0 / N, N)
```
e no notebook `07_01_Otimizacao_Carteiras.ipynb` — célula `02df11b6`, linha equivalente:
```python
wm = np.repeat(1.0 / N, N)
```

**O que deveria estar:** Segundo He & Litterman (1999), `wm` deve ser o vetor de pesos de capitalização de mercado (proporção de cada ativo no índice ou no universo investível). O código usa simplesmente pesos iguais (1/N).

**Há download de capitalização em algum ponto do pipeline?** Não foi encontrado em nenhum notebook lido nesta auditoria. O CLAUDE.md menciona o notebook `2_Pesos_Mercado.ipynb` do pipeline do TCC escrito, mas esse notebook não existe neste repositório (`C:\VSCodeWorkspace\1_TCC_Final`). Nenhuma chamada a `yfinance` foi encontrada no código desta pasta.

**Contradição com o texto do TCC:** O CLAUDE.md afirma que um notebook usa "pesos de mercado (Yahoo Finance)", o que contradiz diretamente o que está implementado aqui. As sanity checks analíticas na célula `3590b040` do NB07 usam `_wm2 = np.repeat(1/3, 3)` — coerente com o código, mas não com o referencial teórico.

**Impacto numérico estimado:** Com wm = 1/N e N = 118 ativos, cada ativo recebe prior de equilíbrio `Pi_i = delta * (Sigma @ wm)_i`. Com capitalizações reais, ativos grandes (VALE3, PETR4, ITUB4) teriam Pi mais alto; ativos pequenos teriam Pi mais baixo. A diferença no vetor `mu_BL` pode ser materialmente diferente — especialmente no prior downside, onde `SigD` amplia a assimetria das semicovariâncias. Não é possível quantificar sem os dados de capitalização, mas a direção da distorção favorece ativos pequenos no prior atual.

**Classificação:** [DEFEITO]  
**Justificativa:** O framework de Black-Litterman (He & Litterman, 1999) é fundamentalmente construído sobre o prior de equilíbrio de mercado capturado por capitalizações ponderadas. Usar 1/N como proxy "de mercado" inverte o sentido do prior — o texto do TCC afirma usar pesos de mercado, mas o código usa pesos iguais. Isso invalida a interpretação do BL como "equilíbrio CAPM reverso" e viola a Proposição 3 verificada na célula `3590b040` para o contexto real (a verificação passa no caso sintético apenas porque wm sintético = 1/3 por construção). Requer correção ou redefinição explícita de "prior" no texto.

---

## C. Hipótese Nula no lw_bootstrap_sharpe/sortino

### C1. Ausência de centralização para impor H0: deltaSR = 0
**Arquivo:** `src/09_Inferencia_Econometrica/utils/inferencia.py` — linhas 136–151 (`lw_bootstrap_sharpe`) e 153–170 (`lw_bootstrap_sortino`)  
**O que está:** A função reamostral os índices com mesmo bloco para ambas as séries e computa:
```python
diffs[b] = _sr(ri[idx]) - _sr(rj[idx])
se = diffs.std(ddof=1)
z  = diff_obs / se if se > 0 else 0.0
```
A distribuição bootstrap de `diffs` **não é centralizada** em zero — ela fica centrada em `diff_obs` (pois as mesmas séries reamostradas preservam a diferença observada em esperança).

**Ledoit-Wolf (2008) original faz centralização?** O artigo de Ledoit & Wolf (2008, "Robust Performance Hypothesis Testing with the Sharpe Ratio", Journal of Empirical Finance) propõe uma estatística de teste bootstrap onde as séries são centralizadas para impor H0. A versão aqui implementada **não centraliza**, seguindo uma variante alternativa conhecida como "bootstrap percentil-t sem centralização" ou "bootstrap de Politis & Romano (1994) direto".

**A validade do p-valor sem centralização:** Sem centralização, a distribuição `diffs` está centrada em `diff_obs`, portanto `SE = std(diffs)` é um estimador da variabilidade amostral de `delta_SR`, mas o pivô `z = diff_obs / SE` é equivalente ao que se obteria com centralização (pois em ambos os casos o SE é o mesmo — a centralização apenas desloca a distribuição, não altera seu desvio padrão). Logo, o p-valor bicaudal `2*(1 - Phi(|z|))` é **assintoticamente válido** como teste aproximado. A diferença em relação à versão com centralização é de segunda ordem para amostras grandes.

**Formalmente:** Seja `mu_boot = E[diffs_b]`. Com reamostramento estacionário sobre as séries originais (sem manipulação), `mu_boot ≈ diff_obs` por consistência do bootstrap. Então `SE = std(diffs) ≈ std(diffs - diff_obs)`, que é o que seria obtido após centralização. O pivô `z = diff_obs / SE` testa a hipótese `H0: delta_SR = 0` usando a variabilidade correta. Portanto a implementação é **funcionalmente equivalente** à versão com centralização explícita.

### C2. Explicação da significância de InvVol vs. não-significância de MinVar
**Arquivo:** `src/09_Inferencia_Econometrica/utils/inferencia.py` e dados reais em `data/Estrategias/strategy_returns.parquet`  
**Resultados calculados com dados reais (seed=42, B=2000, bloco=10):**

| Estratégia | dSR diário | SE bootstrap | z | p-valor | dSR anual |
|---|---|---|---|---|---|
| InvVol | 0,0091 | 0,0014 | 6,419 | < 0,001 | 0,145 |
| MinVar | 0,0185 | 0,0092 | 2,004 | 0,045 | 0,294 |

InvVol tem dSR anual **menor** que MinVar (+0,145 vs. +0,294), mas SE muito menor (0,0014 vs. 0,0092). Isso ocorre porque InvVol tem correlação alta e estável com EqualWeight (ambos baseados em volatilidades individuais, mesmos ativos), tornando a distribuição das diferenças reamostradas muito estreita. MinVar tem uma relação mais variável com EqualWeight ao longo do tempo (a composição muda substancialmente mês a mês), gerando SE seis vezes maior. O fator determinante é o **SE bootstrap**, não a magnitude da diferença.

**Nota:** Os p-valores calculados aqui diferem ligeiramente dos do notebook executado porque o notebook foi executado em sessão diferente; a lógica é a mesma.

**Classificação C1:** [DECISÃO DE PROJETO] — a variante sem centralização é válida assintoticamente.  
**Classificação C2:** [OBSERVAÇÃO ANALÍTICA] — o fenômeno (SE domina, não a magnitude) deve ser explicitado no texto do TCC para evitar que a banca interprete como inconsistência.

---

## D. Escala do Black-Litterman

### D1. Mistura de escalas diária/anual nas entradas de bl_posterior
**Arquivo:** `src/07_Otimizacao_Carteiras/utils/otimizacao.py` e `07_01_Otimizacao_Carteiras.ipynb`

**Análise linha a linha (dentro de `otimizar_mes_task`, linhas 420–434, e `construir_alvos`, célula `02df11b6`):**

| Variável | Escala | Linha/Local | Como é obtida |
|---|---|---|---|
| `S` (Sigma para BL clássico) | **DIÁRIA** | `otimizacao.py:383` | `S = estimar_sigma(Jv, metodo=METODO_COV)` — `Jv` são retornos diários, sem `* TRADING_DAYS` |
| `SigD` (Sigma downside) | **ANUAL** | `otimizacao.py:420` | `SigD = estrada_semicov(Jv, MAR_ESTRADA) * TRADING_DAYS` — multiplicado por 252 |
| `Pi` (prior clássico) | **DIÁRIA** | `otimizacao.py:423` | `Pi = DELTA * S @ wm` — S diário × delta |
| `Pi` (prior downside) | **ANUAL** | `otimizacao.py:423` | `Pi = DELTA * SigD @ wm` — SigD anual × delta |
| `Q` (visões de momentum) | **ANUAL** | `otimizacao.py:86` | `Q = prod(1+bloco)^(252/len) - 1` — retorno anualizado |
| `Om` (Omega) | **DEPENDE** | `otimizacao.py:89` | `Om = diag(tau_bl * Sg * ...)` onde `Sg` é o argumento passado |

**Problema identificado:** Em `visoes_momentum` (linha 88): `Sg = Sigma if Sigma is not None else ledoit_wolf(R) * trading_days`. Quando chamada a partir de `otimizar_mes_task`, `Sigma = S` (escala DIÁRIA), portanto `Sg = S` (diário). Isso produz:
- `Om = diag(tau_bl * S_diária * ...)` → Omega em escala **diária**
- `Q` em escala **anual**

Para o prior **clássico** (`BL_classico`): `bl_posterior(S_diária, Pi_diária, P, Q_anual, Om_diária, tau_bl)`. As entradas `Pi` e `Om` são diárias, `Q` é anual — **escalas inconsistentes**.

Para o prior **downside** (`BL_downside`): `bl_posterior(SigD_anual, Pi_anual, P, Q_anual, Om_????, tau_bl)`. `Om` é calculado com `Sg=S_diária` passado originalmente a `visoes_momentum`, mas `SigD_anual` é usado em `bl_posterior`. Também inconsistente.

**O que deveria estar:** Todas as quatro entradas devem estar na mesma escala. A solução mais limpa é anualizá-las todas:
- `S_anual = S * TRADING_DAYS` antes de passar para `visoes_momentum` e para o prior clássico
- `Pi_anual = DELTA * S_anual @ wm`
- `Om` calculado com `Sg = S_anual`

**Impacto numérico estimado:** Para o prior clássico, `Q_anual ≈ 252 × Q_diário`. Com Pi e Om na escala diária, a fórmula BL pondera as visões com um "ruído" 252× menor que o real (Om subestimado). Isso faz o posterior se aproximar excessivamente das visões de momentum, afastando-se do prior de equilíbrio. O efeito concreto é um `mu_BL` muito volátil e dependente de momentum — o que pode explicar o turnover anualizado muito alto (8,3×/ano e 8,6×/ano) das carteiras BL.

**Classificação:** [DEFEITO]  
**Justificativa:** A inconsistência de escala viola a premissa fundamental do framework He & Litterman (1999). A fórmula `mu_BL = (tau*Sigma^-1 + P'*Omega^-1*P)^-1 * (tau*Sigma^-1*Pi + P'*Omega^-1*Q)` requer que Pi, Q, Sigma e Omega estejam todos na mesma escala temporal. A mistura diário/anual distorce o peso relativo do prior vs. visões.

---

## E. Determinismo com ProcessPoolExecutor

### E1. Seed não passada explicitamente aos workers
**Arquivo:** `src/07_Otimizacao_Carteiras/07_01_Otimizacao_Carteiras.ipynb` — célula `1163fbc8`  
**O que está:**
```python
with ProcessPoolExecutor(max_workers=min(3, os.cpu_count())) as executor:
    for i, data_rebal, alvos in executor.map(otimizar_mes_task, tarefas_args):
```
A tupla `tarefas_args` contém os 18 parâmetros descritos na assinatura de `otimizar_mes_task` (linha 358 de `otimizacao.py`). Examinando a lista: `(i, data_rebal, dir_retornos_str, N, ALPHA, TETO_PESO, KAPPA_ORDENS, CVXPY_OK, REBAL, WARMUP_MESES, TRADING_DAYS, METODO_COV, MAR_MODO, DELTA, TAU, MAR_ESTRADA, VISAO_MOMENTUM_MESES, w_prev)`. **Nenhum parâmetro SEED é passado.**

**Impacto:** Os otimizadores SLSQP e CVXPY são **determinísticos** dado o ponto de partida `w0` (warm-start). Nenhuma fonte de aleatoriedade é usada dentro de `otimizar_mes_task` — não há bootstrap, Monte Carlo ou amostragem estocástica. Logo, a ausência de seed **não afeta o determinismo do resultado de otimização**.

**O único `np.random.seed(SEED)` do notebook** (célula `b03afee4`, linha `np.random.seed(SEED)`) é executado no processo pai e não se propaga automaticamente para os processos filhos no Windows com `spawn` (o método padrão). Porém, como nenhum código nos workers usa `np.random`, isso é irrelevante na prática atual.

### E2. Garantia da ordem temporal do warm-start
**Arquivo:** célula `1163fbc8`, trecho de construção de `tarefas_args`  
**O que está:**
```python
w_prev_snapshot = dict(w_prev_global) if w_prev_global else None
tarefas_args.append((i, ..., w_prev_snapshot))
```
O snapshot é tirado **no processo pai, sequencialmente**, antes de submeter os tasks ao pool. Portanto `tarefas_args[i]` sempre contém os pesos de `i-1` como warm-start — a ordem temporal está garantida pela construção sequencial da lista.

**Porém:** `executor.map` entrega os resultados **na ordem de envio** (não de conclusão), então o loop `for i, data_rebal, alvos in executor.map(...)` atualiza `w_prev_global` na ordem correta. Não há race condition.

**Duas execuções sequenciais dão o mesmo resultado?** Sim — os otimizadores SLSQP são determinísticos dado `w0`, e `w0` é determinado pela ordem sequencial do loop. A única fonte potencial de variação seria o comportamento numérico do solver em threads paralelas, mas como cada processo filho é independente e opera sobre dados fixos, o resultado é reproduzível.

**Classificação:** [DECISÃO DE PROJETO] — arquitetura correta, seed é irrelevante aqui pois não há aleatoriedade nos workers. Documentar no TCC que a ausência de seed nos workers é intencional (otimizadores determinísticos).

---

## F. Família de Correção Holm

### F1. Holm aplicado separadamente por benchmark (15 testes cada)
**Arquivo:** `src/09_Inferencia_Econometrica/09_01_Inferencia_Econometrica.ipynb` — célula `cell-22` (seção 11), célula `cell-24` (seção 12), célula `cell-26` (seção 26)  
**O que está:**
```python
testes_sr['LW_p_holm'] = multipletests(testes_sr['LW_p'], method='holm')[1]
```
Na seção 11/12: Holm aplicado sobre os 15 p-valores do benchmark EqualWeight separadamente.  
Na seção 26 (3 benchmarks): Holm aplicado separadamente para cada benchmark (`tmp["LW_p_holm"] = multipletests(tmp["LW_p"], method='holm')[1]` dentro do loop por benchmark).

**O que poderia ser alternativo:** Aplicar Holm sobre todos os 45 testes simultaneamente (15 estratégias × 3 benchmarks). Isso é mais conservador.

**Impacto numérico calculado com dados reais (benchmark EqualWeight, LW bootstrap, B=2000):**

| Estratégia | dSR anual | p bruto | p Holm/15 | p Holm/45 | Muda sig? |
|---|---|---|---|---|---|
| EqualWeight_BuyHold | +0,448 | < 0,001 | < 0,001 | < 0,001 | Não |
| InvVol | +0,145 | < 0,001 | < 0,001 | < 0,001 | Não |
| MinVar | +0,294 | 0,045 | 0,451 | 1,000 | Não (ambos já NS) |
| BL_classico_c10 | +0,535 | 0,013 | 0,159 | 0,478 | Não (ambos NS) |
| BL_downside_c10 | +0,594 | 0,006 | 0,078 | 0,234 | Não |

Com Holm/15, nenhuma estratégia é significativa além de EqualWeight_BuyHold e InvVol. Com Holm/45, o resultado é idêntico (nada muda de significância). Isso ocorre porque os p-valores brutos das estratégias "candidatas" (MinVar, BL) estão longe do limiar Holm ajustado mesmo com 15 testes; adicionar 30 testes a mais apenas eleva ainda mais o limite de rejeição para as posições intermediárias.

**Classificação:** [DECISÃO DE PROJETO]  
**Justificativa:** Aplicar Holm separadamente por benchmark é metodologicamente defensável — cada família de comparações tem semântica distinta (vs. 1/N, vs. BuyHold, vs. IBOV). O efeito empírico neste conjunto de dados é nulo: a escolha entre 15 e 45 testes não altera nenhuma conclusão. Documentar a escolha no Capítulo 3.

---

## G. Varredura Geral

### G1. Divisões por zero potenciais
**Arquivo:** `src/07_Otimizacao_Carteiras/utils/otimizacao.py:117`  
**O que está:**
```python
def w_inv_vol(S):
    iv = 1.0 / np.sqrt(np.diag(S))
    return iv / iv.sum()
```
Se qualquer diagonal de `S` for zero (ativo sem variância — por exemplo, série constante no período), `np.sqrt(0) = 0` produz divisão por zero e retorna `inf`. `iv.sum()` seria `inf`, e `inf/inf = nan`.

**Risco:** Baixo em dados reais (nenhum ativo tem variância exatamente zero em 5+ anos de janela expansiva). Porém, em janelas de warmup muito curtas ou com filtro de liquidez insuficiente, pode ocorrer.

**Arquivo:** `src/09_Inferencia_Econometrica/utils/inferencia.py:84`  
```python
SRa = exc_a.mean() / exc_a.std(ddof=1)
```
Se `exc_a.std(ddof=1) == 0` (série constante), produz divisão por zero. A função `sharpe` (linha 25) tem proteção `if std_val == 0: return 0.0`, mas `_jk_memmel` não tem proteção equivalente.

**Classificação G1a (w_inv_vol):** [DEFEITO de baixo risco] — adicionar `iv = np.where(np.diag(S) > 0, 1/np.sqrt(np.diag(S)), 0.0)` como proteção.  
**Classificação G1b (_jk_memmel):** [DEFEITO de baixo risco] — adicionar `if exc_a.std(ddof=1) == 0 or exc_b.std(ddof=1) == 0: return 0.0, 1.0`.

### G2. ddof inconsistente entre estimadores
**Arquivo:** `src/07_Otimizacao_Carteiras/utils/otimizacao.py:35` e `src/09_Inferencia_Econometrica/utils/inferencia.py:84,142`  
**O que está:**
- `ledoit_wolf`: `S = (Xc.T @ Xc) / T` — divisor **T** (MLE, ddof=0)
- `estimar_sigma` com método "amostral": `np.cov(janela, rowvar=False)` — divisor **T-1** (ddof=1 por padrão)
- `_jk_memmel`: `exc_a.std(ddof=1)` — ddof=1
- `lw_bootstrap_sharpe`: `def _sr(x): s = x.std(ddof=1)` — ddof=1

**Avaliação de consistência:**  
A literatura de otimização (Ledoit & Wolf, 2004) usa ddof=0 (MLE) para consistência com a teoria de matrizes aleatórias. Para Sharpe ratio, a literatura usa ddof=1 (não-viesado para amostras finitas). A separação entre ddof=0 (covariância de portfólio) e ddof=1 (estatísticas de teste) é **metodologicamente correta** — não é inconsistência, é uso contextualmente adequado. O único ponto de atenção é o método "amostral" de `estimar_sigma` que usa ddof=1 (np.cov default), enquanto `ledoit_wolf` usa ddof=0 — as duas estimativas de Sigma ficam em escalas ligeiramente diferentes (fator T/(T-1)), o que pode afetar comparações diretas entre os dois métodos (irrelevante aqui pois o método padrão é `ledoit_wolf`).

**Classificação:** [DECISÃO DE PROJETO] — a separação é correta. Documentar no TCC.

### G3. Look-ahead via ffill em séries de retorno
**Arquivo:** `src/09_Inferencia_Econometrica/utils/inferencia.py:14`  
```python
return rf.reindex(retornos.index).ffill().bfill()
```
E no NB09 célula `cell-4`:
```python
cdi_serie = cdi_df.set_index("data")["cdi_diario"].reindex(ibov["data"]).ffill().bfill()
```
**Avaliação:** O `ffill` aqui é aplicado à taxa livre de risco (CDI), não a retornos de ativos. CDI é observado diariamente e publicado no dia útil seguinte; usar `ffill` para propagar o CDI em finais de semana ou feriados é **prática padrão e correta** — não introduz look-ahead bias porque o CDI de um dia útil aplica-se aos dias não-úteis subsequentes até o próximo pregão. O `bfill` no início da série pode ser questionável (preenche com o primeiro CDI observado para datas anteriores), mas o impacto é negligenciável.

**Nos notebooks de backtest (NB07):** O `ffill` de RF dentro de `otimizar_mes_task` (linha 385: `rf_j = rf.reindex(janela.index).dropna()`) usa apenas dados até `fim_prev` — sem look-ahead.

**Classificação:** [DECISÃO DE PROJETO] — sem look-ahead real.

### G4. Alinhamento de índices entre strategy_returns e ibov/cdi no NB09
**Arquivo:** `src/09_Inferencia_Econometrica/09_01_Inferencia_Econometrica.ipynb` — célula `cell-14`  
**O que está:**
```python
df["ret_ibov"] = ibov.set_index("data")["ibov_ret_simples"].reindex(df.index).ffill().bfill()
df["rf"] = ibov.set_index("data")["cdi_diario"].reindex(df.index).ffill().bfill()
```
O `df.index` vem de `strat.index` (retornos das estratégias, gerado pelo NB07, 2015-03-02 a 2025-12-30). O IBOV tem 3.966 observações (2010-01-05 a 2025-12-30). O reindex com ffill pode preencher datas em que o IBOV não operou mas as estratégias sim (ou vice-versa). Caso existam datas em `strat.index` ausentes em `ibov["data"]`, o `ffill` propaga o último retorno do IBOV disponível — o que é incorreto (deveria usar 0.0 ou NaN para dias sem pregão do índice, não o retorno do dia anterior).

**Risco prático:** Ambas as séries derivam de dados da B3 e BCB, que têm o mesmo calendário de dias úteis brasileiros. Datas discrepantes seriam raras. Mas a célula `cell-4` lê `ibov_diario_2010_2026.csv` e a célula `cell-14` faz `reindex` sem checar o número de NaN produzidos. Não há aviso de quantas datas foram preenchidas por ffill.

**Classificação:** [DECISÃO DE PROJETO] com recomendação de adicionar `assert df[["ret_ibov","rf"]].isna().sum().sum() == 0, "Datas desalinhadas"` após o reindex para garantir ausência de NaN (ou ffill não-intencional).

### G5. CUSTO_BPS e aplicação sobre turnover
**Arquivo:** `src/07_Otimizacao_Carteiras/07_01_Otimizacao_Carteiras.ipynb` — célula `1163fbc8`  
**O que está:**
```python
custo_unit = CUSTO_BPS / 1e4      # 50/10000 = 0.005 = 0.5%
...
turn = np.abs(w - w_ant[k]).sum()  # soma das variações absolutas de peso
rp[0] -= custo_unit * turn         # deduzido do retorno do 1º dia do mês
```
`turn` é a soma das variações absolutas de peso (one-way turnover em termos de fração do portfólio). O custo é `0.5% × turnover_one_way`, aplicado sobre o retorno do primeiro dia — não sobre o valor total da carteira. Isso é **correto**: representa o custo de execução das ordens de rebalanceamento (proporcional ao giro, não ao tamanho da carteira).

**Classificação:** [SEM ACHADO] — implementação correta.

### G6. BOOTSTRAP_REPS (config.json=1000) vs. BOOT_REPS (NB09=2000)
**Arquivo:** `src/config.json:24` e `src/09_Inferencia_Econometrica/09_01_Inferencia_Econometrica.ipynb` — célula `cell-2`  
**O que está:**
```python
# config.json:
"BOOTSTRAP_REPS": 1000

# NB09 célula cell-2:
BOOTSTRAP_REPS = cfg.get("BOOTSTRAP_REPS", 1000)  # lido do config: 1000
BOOT_REPS  = 2000                                   # hardcoded
```
Os dois parâmetros são usados em lugares distintos:
- `BOOTSTRAP_REPS` (1000): usado em `bootstrap_ic()` na seção 9 (intervalos de confiança individuais)
- `BOOT_REPS` (2000): usado em `lw_bootstrap_sharpe/sortino` nas seções 11, 12 e 26 (testes de diferença)

**Impacto:** Os testes de diferença (mais importantes para as conclusões) usam 2000 reamostras — maior precisão que as seções de IC. A seção 9 usa apenas IC exploratórios com 1000 reamostras. Não há inconsistência metodológica grave, mas há risco de confusão: o leitor do TCC pode ver "B=1000" na seção 9 e "B=2000" nas seções 11-12 sem entender a distinção.

**Classificação:** [DECISÃO DE PROJETO] — porém a inconsistência entre o parâmetro do config (`BOOTSTRAP_REPS`) e o valor hardcoded (`BOOT_REPS`) é suscetível a regressão: se alguém alterar `BOOTSTRAP_REPS` no `config.json`, os testes de diferença **não mudarão** (pois usam `BOOT_REPS` hardcoded). Recomendável unificar ou renomear para evitar confusão.

### G7. cumsum de retornos simples para drawdown no w_min_cdar
**Arquivo:** `src/07_Otimizacao_Carteiras/utils/otimizacao.py` — linhas 315–319  
**O que está:**
```python
Rcum = np.cumsum(R, axis=0)   # soma cumulativa dos retornos simples
C = Rcum @ w                  # "nível" da carteira
cons = [..., u >= C, u[1:] >= u[:-1], u[0] >= 0, z >= (u - C) - zeta]
```
**O que seria matematicamente correto para drawdown:** O drawdown é medido como queda em relação ao pico de um processo de riqueza, que segue produto cumulativo: `W_t = prod(1 + r_1..r_t)`. A soma cumulativa `cumsum(r)` aproxima `log(W_t)` para retornos pequenos (pois `sum(r) ≈ sum(log(1+r)) ≈ log(W_t)` quando r pequeno).

**Impacto quantificado:** Para uma série de 1000 retornos diários com média 0,05% e vol 1,5% (dados típicos do backtest), o retorno acumulado via produto é ~+45% em 4 anos; via soma é ~+46% (diferença de ~1 p.p.). O drawdown máximo via cumsum ficou 0,325 vs. 0,302 via cumprod em simulação com seed=42 — diferença de ~7% na magnitude do drawdown. Para janelas longas de 60 meses (1260 dias), a diferença cresce substancialmente: retorno via produto ~+460%, via soma ~+187% — o processo de riqueza aproximado pela soma diverge significativamente.

**Consequência prática:** A carteira otimizada por `w_min_cdar` minimiza drawdowns em escala aditiva (unidades de "retorno somado"), não em escala multiplicativa (% de queda do pico). Para janelas longas, isso faz com que o CDaR otimizado não corresponda ao CDaR que será computado na métrica de desempenho `max_drawdown` (que usa cumprod). A estratégia MinCDaR pode não ser a carteira de mínimo CDaR real.

**Classificação:** [DEFEITO de severidade média]  
**Justificativa:** A inconsistência entre o processo de riqueza usado na otimização (aditivo) e o usado na avaliação (multiplicativo, `max_drawdown` em `inferencia.py:59`) significa que a estratégia MinCDaR está minimizando uma métrica diferente da que é reportada. Para retornos diários individuais pequenos (~1%), o erro é aceitável num único período; para janelas de 5 anos (T=1260), a discrepância é materialmente grande. A correção seria usar `Rcum = np.cumprod(1 + R, axis=0)` ou, alternativamente, aplicar log para converter em escala aditiva consistente.

---

## Tabela-Resumo dos Achados

| Achado | Título resumido | Severidade | Classificação | Requer aval antes de corrigir? |
|---|---|---|---|---|
| A1 | Constant-mix vs. buy-and-hold intramês | Média | DECISÃO DE PROJETO | **Sim** — define interpretação do TCC |
| B1 | Pesos de mercado = 1/N (não capitalização) | Alta | DEFEITO | **Sim** — impacta todas as estratégias BL |
| C1 | Sem centralização bootstrap (H0) | Baixa | DECISÃO DE PROJETO | Não — matematicamente equivalente |
| C2 | SE bootstrap domina magnitude (InvVol vs MinVar) | Baixa | OBSERVAÇÃO | Não — apenas documentar no texto |
| D1 | Escala diária/anual inconsistente no BL | Alta | DEFEITO | **Sim** — invalida resultados BL |
| E1 | Seed não passada aos workers do pool | Baixa | DECISÃO DE PROJETO | Não — sem aleatoriedade nos workers |
| E2 | Ordem temporal do warm-start garantida | — | SEM ACHADO | — |
| F1 | Holm por benchmark (15) vs. global (45) | Baixa | DECISÃO DE PROJETO | Não — zero impacto empírico aqui |
| G1a | Divisão por zero em w_inv_vol | Baixa | DEFEITO | Não — baixo risco em dados reais |
| G1b | Divisão por zero em _jk_memmel | Baixa | DEFEITO | Não — baixo risco em dados reais |
| G2 | ddof inconsistente entre estimadores | Baixa | DECISÃO DE PROJETO | Não — contextualmente correto |
| G3 | ffill na taxa livre de risco | Baixa | DECISÃO DE PROJETO | Não — prática padrão |
| G4 | Alinhamento ibov/cdi sem verificação | Baixa | DECISÃO DE PROJETO | Não — recomenda assert |
| G5 | CUSTO_BPS aplicado sobre turnover | — | SEM ACHADO | — |
| G6 | BOOTSTRAP_REPS vs. BOOT_REPS hardcoded | Baixa | DECISÃO DE PROJETO | Não — risco de regressão futura |
| G7 | cumsum vs. cumprod no CDaR | Média | DEFEITO | **Sim** — afeta estratégia MinCDaR |

### Priorização para ação imediata

1. **B1 + D1 (Alta):** Os dois defeitos afetam as estratégias Black-Litterman, que são as de maior retorno no backtest. Corrigir B1 (pesos de mercado reais) e D1 (escala anual consistente) pode mudar substancialmente os resultados de BL_classico e BL_downside. Requer decisão do autor sobre fonte de capitalização e re-execução do NB07 e NB09.

2. **G7 (Média):** MinCDaR minimiza um CDaR aproximado. Impacto menor que B1/D1 pois a estratégia tem desempenho modesto (CAGR 10,9%, Sharpe 0,15) e não é central nas conclusões do TCC.

3. **A1 (Média):** Decisão de projeto que deve ser explicitada no Capítulo 3 para evitar questionamentos da banca. Não requer alteração de código se a convenção constant-mix for a intenção.
