# Relatório de Cobertura de Testes — Qualidade e Reprodutibilidade (Fase P2)

**Objetivo:** Descrever a arquitetura de testes automatizados implementada no diretório `tests/` para assegurar o rigor matemático dos estimadores, otimizadores e métricas estatísticas utilizados no TCC.

---

## 1. Resumo Executivo da Execução de Testes

A suíte de testes completa foi executada com sucesso utilizando o framework `pytest`, abrangendo tanto as verificações unitárias rápidas quanto as simulações pesadas de calibração estatística Monte Carlo. 

*   **Total de Testes Executados:** 97
*   **Status Geral:** **PASS (100% de Aprovação)**
*   **Tempo de Execução:** 333,43 segundos (5 minutos e 33 segundos)

---

## 2. Estrutura de Testes e Cobertura por Arquivo

Os testes estão divididos de forma modular em seis arquivos principais:

### 2.1. Métricas de Desempenho Financeiro (`test_metricas.py` — 22 testes)
Verifica o cálculo analítico exato de todas as fórmulas de desempenho e risco relatadas no TCC:
*   **Sharpe Ratio:** Teste com CDI variável, fallback de taxa fixa, tratamento de volatilidade nula (retorno zero = Sharpe zero) e anualização por $\sqrt{252}$.
*   **Sortino Ratio:** Teste de cálculo manual sob cauda downside e verificação de retorno infinito quando não há retornos negativos.
*   **CAGR:** Testes de cálculo de juros compostos em série vazia, retornos constantes e variações históricas.
*   **Max Drawdown:** Verificação da fórmula clássica de rebaixamento a partir da riqueza acumulada multiplicativa, assegurando que o drawdown máximo seja sempre $\le 0$.
*   **Jobson-Korkie/Memmel:** Validação da comparação estatística de Sharpe com a correção de Memmel (2003), incluindo proteção contra erros de divisão por zero.

### 2.2. Estimadores de Risco (`test_estimadores.py` — 18 testes)
Garante as propriedades algébricas fundamentais dos estimadores de covariância clássica e downside:
*   **Ledoit-Wolf Shrinkage:** Confirmação de simetria matricial, teste de semidefinição positiva (PSD), restrição do parâmetro de encolhimento $\delta \in [0, 1]$, conservação de traço, convergência assintótica para a covariância amostral, e paridade numérica exata com o módulo `sklearn.covariance.ledoit_wolf`.
*   **Semicovariância de Estrada:** Validação do estimador downside de Estrada (2008), confirmando simetria, propriedade PSD da matriz resultante, menor ou igualdade termo a termo contra a covariância total na diagonal, e suporte a MAR nulo ou literal.

### 2.3. Otimizadores Convexos e Não-Convexos (`test_otimizadores.py` — 32 testes)
Testa a corretude matemática das alocações ótimas sob restrições estruturais:
*   **EqualWeight (1/N) & InvVol:** Confirmação de fórmula fechada e consistência sob ativos degenerados.
*   **Mínima Variância Global (MinVar):** Teste de restrição de soma de pesos $=1$, restrição *long-only* (pesos $\ge 0$), teto regulatório de 10% (CVM 175) e propriedade de que a variância otimizada seja menor ou igual à da carteira 1/N.
*   **Máximo Sharpe (MaxSharpe):** Teste de invariantes e validação de Sharpe ótimo ex-ante superior ao de referência.
*   **Mínimo CVaR e CDaR:** Teste das propriedades convexas solucionadas via LP (CVXPY) com tolerâncias numéricas estritas, e validação de que o rebaixamento acumulado utiliza a riqueza multiplicativa correta.
*   **Resolvedor Kappa (Omega/Sortino/Kappa3):** Validação das três ordens do momento parcial inferior, confirmando a estabilidade paramétrica do SLSQP.

### 2.4. Propriedades e Escalas de Black-Litterman (`test_black_litterman.py` — 7 testes)
Garante a integridade do framework Bayesiano:
*   **Invariantes Matemáticos:** Confirmação de que quando a incerteza da visão é infinita ($\Omega \to \infty$), o posterior colapsa de volta no prior (equilíbrio); e quando a incerteza é zero ($\Omega = 0$), o posterior é puxado exatamente para as visões $Q$.
*   **Consistência de Escala [FIX D1]:** Teste de verificação para garantir que a covariância anualizada do prior e do momentum operem na mesma base de escala temporal, evitando o colapso artificial do posterior clássico.

### 2.5. Testes Econométricos e Bootstrap (`test_inferencia_calibracao.py` — 10 testes)
Valida a reprodutibilidade dos testes sob reamostragem:
*   **Stationary Bootstrap:** Teste determinístico de reprodutibilidade de p-valores fixando a semente randômica central (`SEED=42`), garantindo que o DSR (Deflated Sharpe Ratio) seja idêntico em execuções repetidas.
*   **Tamanho de Bloco:** Teste de robustez paramétrica sob diferentes tamanhos de bloco de reamostragem (5, 10 e 21 dias).

### 2.6. Integração do Backtest (`test_backtest_integracao.py` — 3 testes)
Verifica o cálculo final da riqueza da simulação histórica de 2015 a 2025:
*   **Drift de Preços:** Confirmação de que os retornos compostos acumulam de forma compatível com a variação diária.
*   **Custo de Transação:** Validação da dedução de $50\text{ bps}$ sobre o giro absoluto (turnover) no rebalanceamento mensal.

---

## 3. Lacunas de Cobertura Identificadas

*   **Testes de Solver sob Inviabilidade:** Embora os otimizadores convexos (CVaR/CDaR) contenham cláusulas de exceção que acionam o fallback `EqualWeight`, a suíte de testes não simula um cenário artificialmente forçado onde o solver falha por completo por inviabilidade de restrições (ex.: retornos impossíveis), o que seria útil para garantir 100% de cobertura do bloco de exceção.
*   **Property-Based Testing (Hypothesis):** A biblioteca `hypothesis` não está listada em `requirements.txt`. Portanto, os testes de propriedades usam matrizes geradas aleatoriamente via `numpy.random.default_rng(seed)` em vez de buscas de borda de forma totalmente automatizada.
