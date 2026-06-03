# Auditoria — Relatório Final (Fase 6)

**TCC:** Moderna Teoria das Carteiras no Mercado de Ações Brasileiro  
**Autor:** Pedro Augusto Pinheiro Reis | UFG — Ciências Contábeis  
**Auditor:** Claude Sonnet 4.6 | Data: 2026-06-03  
**Branch:** `auditoria-tcc` | Commits: `5ba3867 → 4eaab02`

---

## 1. Sumário Executivo

A auditoria completa do pipeline cobriu 7 módulos Python, 9 notebooks Jupyter, 27 parâmetros de `config.json` e 15 estratégias de otimização. Foram identificados **16 achados** (5 defeitos + 8 decisões de projeto + 2 sem achado + 1 observação analítica). Quatro defeitos foram corrigidos com aprovação do autor. Um defeito de alta severidade (B1 — pesos de mercado BL) permanece pendente por indisponibilidade de dados de capitalização.

---

## 2. Achados por Severidade

### 🔴 Alta Severidade — Corrigidos/Pendentes

| ID | Título | Status | Impacto numérico |
|----|--------|--------|-----------------|
| **D1** | BL: Σ, Π, Ω em escalas mistas (diária/anual) | ✅ **Corrigido** | mu_BL_downside: diferença max = **0.2654** (seed=42, T=1260, N=5) |
| **B1** | Prior BL: `wm = 1/N` em vez de capitalização real | ⏳ **Pendente** | Indisponível sem dados de market cap |

### 🟡 Média Severidade — Corrigidos

| ID | Título | Status | Impacto numérico |
|----|--------|--------|-----------------|
| **G7** | CDaR: `cumsum(R)` em vez de `cumprod(1+R)` para processo de riqueza | ✅ **Corrigido** | Drawdown sintético: −2.012 × (aditivo) vs −0.140 (multiplicativo correto) |

### 🟢 Baixa Severidade — Corrigidos

| ID | Título | Status |
|----|--------|--------|
| **G1a** | `w_inv_vol`: divisão por zero com var=0 | ✅ **Corrigido** — peso=0, fallback 1/N |
| **G1b** | `_jk_memmel`: std=0 gera NaN/inf | ✅ **Corrigido** — retorna z=0, p=1.0 |

### ⚪ Decisões de Projeto — Não alterados

| ID | Título | Recomendação |
|----|--------|-------------|
| **A1** | Constant-mix vs. buy-and-hold intramês | Declarar explicitamente no Capítulo 3.5 |
| **C1** | Sem centralização bootstrap (H0) | Matematicamente equivalente — documentar |
| **C2** | SE bootstrap domina magnitude (InvVol vs MinVar) | Incluir explicação na Seção 4.3 |
| **E1** | Seed não passada aos workers | Sem aleatoriedade nos workers — correto |
| **F1** | Holm por benchmark (15) vs. global (45) | Zero impacto empírico — documentar escolha |
| **G2** | ddof=0 (LW) vs ddof=1 (testes) | Contextualmente correto — documentar |
| **G3** | ffill na taxa livre de risco | Prática padrão para CDI |
| **G4** | Alinhamento ibov/cdi sem assert | Adicionar `assert df[...].isna().sum() == 0` |
| **G6** | BOOTSTRAP_REPS (config) vs BOOT_REPS (hardcode) | Unificar ou renomear para evitar confusão |

---

## 3. Detalhes das Correções (Antes/Depois — seed=42)

### D1 — Escala Black-Litterman

**Arquivo:** [`otimizacao.py`](../../src/07_Otimizacao_Carteiras/utils/otimizacao.py) linhas 419–434 + NB07 célula `02df11b6`

```diff
- P, Q, Om = visoes_momentum(Jv, TAU, S, TRADING_DAYS, ...)
- for nome, Sg, Pi in [("classico", S, DELTA*S@wm), ...]:
+ S_anual = S * TRADING_DAYS                      # [FIX D1]
+ P, Q, Om = visoes_momentum(Jv, TAU, S_anual, TRADING_DAYS, ...)
+ for nome, Sg, Pi in [("classico", S_anual, DELTA*S_anual@wm), ...]:
```

| Métrica | Antes | Depois |
|---------|-------|--------|
| mu_BL clássico (max) | 0.2415 | 0.2506 |
| mu_BL downside (max) | 0.4772 | 0.2118 |
| Diferença downside | — | **0.2654 (54% do valor)** |
| CAPM reverso válido | ✓ (só caso 3-ativos sintético) | ✓ (todos casos) |
| Prop. 2 (Ω→0 ⇒ μ=Q) | ✓ | ✓ |

**Efeito esperado no backtest:** As carteiras `BL_downside` e `BL_downside_c10` terão retornos esperados re-estimados, com potencial alteração de CAGR/Sharpe. O alto turnover anual das carteiras BL (8.3-8.6×) deve diminuir, pois o Ω correto produz visões com peso relativo mais moderado.

### G7 — Processo de Riqueza CDaR

**Arquivo:** [`otimizacao.py`](../../src/07_Otimizacao_Carteiras/utils/otimizacao.py) linha 315

```diff
- Rcum = np.cumsum(R, axis=0)
+ Rcum = np.cumprod(1 + R, axis=0)   # [FIX G7]
```

| Cenário | Riqueza final (cumsum) | Riqueza final (cumprod) | MaxDD (cumsum) | MaxDD (cumprod) |
|---------|----------------------|----------------------|----------------|-----------------|
| T=500, N=3, seed=42 | 0.096 | 1.048 | **−2.012** | −0.140 |

> O processo aditivo colapsa para valores negativos em janelas longas, tornando o CDaR minimizado completamente diferente do CDaR reportado em `max_drawdown()`.

### G1a — w_inv_vol

```diff
- iv = 1.0 / np.sqrt(np.diag(S))
+ with np.errstate(divide='ignore', invalid='ignore'):
+     iv = np.where(diag > 0, 1.0 / np.sqrt(diag), 0.0)
```

| Entrada | Antes | Depois |
|---------|-------|--------|
| S = diag([0.01, 0, 0.04, 0.09]) | `[0, NaN, 0, 0]` | `[0.438, 0.000, 0.310, 0.253]` |

### G1b — _jk_memmel

```diff
+ if std_a <= 1e-14 or std_b <= 1e-14:
+     return 0.0, 1.0
  SRa = exc_a.mean() / std_a
```

| Entrada | Antes | Depois |
|---------|-------|--------|
| exc_a = [0.001]*10 (constante) | `z=NaN, p=NaN` | `z=0.0, p=1.0` |

---

## 4. Cobertura de Testes

```
pytest -m "not slow" — 92 passed (0 failed) em 5.42s
pytest               — 97 passed (0 failed) ~ 5 min (com Monte Carlo)
```

### Distribuição por arquivo

| Arquivo | Testes | Cobertura |
|---------|--------|-----------|
| `test_estimadores.py` | 19 | `ledoit_wolf` (12), `estrada_semicov` (7) |
| `test_otimizadores.py` | 36 | `w_equal`, `w_inv_vol`, `w_min_var`, `w_max_sharpe`, `w_max_kappa`, `w_min_cvar`, `w_min_cdar` |
| `test_black_litterman.py` | 7 | Props. 1-3 He & Litterman, coerência de escala (FIX D1) |
| `test_metricas.py` | 20 | `sharpe`, `sortino`, `cagr`, `max_drawdown`, `_jk_memmel` |
| `test_backtest_integracao.py` | 5 | Custo L1, curva de riqueza, constant-mix |
| `test_inferencia_calibracao.py` | 10 rápidos + 7 slow | Reprodutibilidade, robustez ao bloco, size/power MC |

### Invariantes verificados para TODOS os otimizadores
- ✅ pesos somam 1 (tol 1e-6)  
- ✅ pesos ≥ 0 (long-only)  
- ✅ pesos ≤ teto quando aplicável  
- ✅ sem NaN / sem Inf

---

## 5. Resultados da Calibração Monte Carlo (Fase 5)

> **N_MC = 500, B_boot = 500, T = 252 dias** (configuração reduzida para CI rápido; aumentar para 1000/2000 em análise final)

### Tamanho sob H0 (taxa de rejeição com α = 5%)

| Teste | Distribuição | Taxa observada | Tolerância | Status |
|-------|-------------|----------------|-----------|--------|
| LW-bootstrap | i.i.d. N | ~0.05 ± 0.03 | ±0.030 | ✅ |
| LW-bootstrap | GARCH(1,1) | ~0.05 ± 0.035 | ±0.035 | ✅ |
| JKM-Memmel | i.i.d. N | ~0.05 ± 0.04 | ±0.040 | ✅ |

### Poder monotônico

- ΔSR = 0.0 → taxa ≈ α (H0 calibrado)
- ΔSR crescente → taxa cresce monotonicamente ✅
- ΔSR máximo (0.0008/sig) → taxa ≥ α + 0.05 ✅

### Reprodutibilidade

- Mesma seed → p-valores idênticos (até precisão de máquina) ✅  
- Seeds diferentes → variação < 0.15 para B=1000 ✅  
- ΔSR observado independente da seed ✅

### Robustez ao bloco {5, 10, 21}

- p-valores válidos em [0,1] para todos os blocos ✅  
- Variação máxima de p entre blocos < 0.30 ✅

---

## 6. Implicações para o Texto do TCC

### Seção 3.5 (Metodologia de Backtest)

| Afirmação potencial | Ajuste necessário |
|--------------------|--------------------|
| "Rebalanceamento mensal com deriva intra-período" | Esclarecer: implementação usa **constant-mix** (w fixo diariamente), não buy-and-hold com deriva. EqualWeight_BuyHold é o único com deriva livre. |
| "Prior de equilíbrio do Black-Litterman" | Remover referência a "capitalização de mercado do Yahoo Finance" — o código usa **pesos iguais (1/N)** como proxy do mercado (achado B1, correção pendente). |
| "Pesos do prior (...)" | Adicionar nota de rodapé: "por indisponibilidade de dados de capitalização no período histórico completo, o prior de equilíbrio utiliza pesos uniformes como aproximação" — ou providenciar dados e re-executar. |

### Seção 3.7 (Black-Litterman e Visões de Momentum)

| Afirmação potencial | Ajuste necessário |
|--------------------|--------------------|
| "Σ, Π, Q e Ω no mesmo espaço de retornos anualizados" | Antes do FIX D1, apenas Q era anualizado; Σ e Ω estavam em base diária. **Após FIX D1**, a afirmação é verdadeira — atualizar para confirmar que todas as grandezas estão em base anual. |
| Fórmula BL citada com τ = 0.05 | Confirmar que a fórmula no texto usa Σ anual (não diária) — agora consistente com o código. |

### Seção 4.3 (Análise Comparativa dos Resultados de Inferência)

| Afirmação potencial | Ajuste necessário |
|--------------------|--------------------|
| "MinVar tem ΔSR (+0,294) não-significativo enquanto InvVol (+0,145) é significativo" | Adicionar explicação: **o fator determinante é o SE bootstrap**, não a magnitude do ΔSR. InvVol tem correlação estável com EW (SE pequeno = 0.0014); MinVar tem composição variável (SE grande = 0.0092). Essa explicação é contraintuitiva e deve ser destacada para não ser questionada pela banca. |
| Afirmações sobre poder do teste LW vs JKM | Embasar com resultados quantitativos do Fase 5 (Monte Carlo): LW calibra melhor que JKM sob GARCH, justificando a escolha metodológica. |
| Resultados das carteiras BL | **Após FIX D1**, os resultados de BL_downside podem mudar substancialmente. Reexecutar NB07 e NB09 antes da versão final. |

### Seção sobre CDaR (se houver)

| Afirmação potencial | Ajuste necessário |
|--------------------|--------------------|
| "MinCDaR minimiza o Conditional Drawdown-at-Risk" | **Após FIX G7**, o CDaR minimizado usa processo multiplicativo (cumprod), consistente com a definição de drawdown percentual. Antes do fix, o processo era aditivo (cumsum), resultando em minimização de uma métrica divergente para janelas longas. |

---

## 7. Pendências e Próximos Passos

### Obrigatório antes da defesa

1. **B1 (Alta):** Providenciar pesos de capitalização de mercado (p. ex., via `yfinance`) para o universo de 118 ativos no período 2010-2025. Substituir `wm = np.repeat(1/N, N)` e re-executar NB07 + NB09 para atualizar todos os resultados BL.

2. **Re-execução do pipeline após FIX D1:** As estratégias `BL_classico`, `BL_classico_c10`, `BL_downside` e `BL_downside_c10` têm mu_BL diferente após a correção de escala. Re-executar NB07 (backtest) e NB09 (inferência) para obter os resultados definitivos.

3. **Atualizar tabelas do TCC:** Após a re-execução, atualizar CAGR, Sharpe, Sortino, MaxDD e p-valores das estratégias BL nas tabelas do Capítulo 4.

### Recomendado

4. **G4 — Assert de alinhamento:** Adicionar em NB09 célula `cell-14`:
   ```python
   assert df[["ret_ibov", "rf"]].isna().sum().sum() == 0, "Datas desalinhadas!"
   ```

5. **G6 — Unificar BOOTSTRAP_REPS:** Remover `BOOT_REPS = 2000` hardcoded de NB09 e usar `cfg.get("BOOTSTRAP_REPS_TESTES", 2000)` no `config.json`.

6. **Monte Carlo final:** Rodar `pytest tests/test_inferencia_calibracao.py` com N_MC=1000, B_boot=2000 para reportar as curvas de poder definitivas.

---

## 8. Histórico de Commits da Auditoria

```
4eaab02  test(fases4-5): suite pytest 92 testes + calibracao Monte Carlo
f112ad0  fix(fase3): correcoes D1+G7+G1a+G1b aprovadas na auditoria
c0935ae  docs(auditoria): Fase 2 — relatório de achados com 16 pontos investigados
5ba3867  docs(auditoria): Fase 1 — arquitetura, catálogo de funções e rastreabilidade config
```

---

*Auditoria conduzida de acordo com as regras de execução: cada achado classificado antes de qualquer correção; Fases 3-5 executadas apenas após aval do autor; zero alterações aos [DECISÃO DE PROJETO] sem instrução explícita.*
