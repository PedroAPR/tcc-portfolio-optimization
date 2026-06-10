# Plano de Testes Econométricos e Quantitativos Ampliado
**Abordagem de Revisão Científica Rigorosa e Independente (Peer-Review Standard)**

**TCC:** Moderna Teoria das Carteiras no Mercado de Ações Brasileiro  
**Autor:** Pedro Augusto Pinheiro Reis | UFG — Ciências Contábeis  
**Data:** 10 de junho de 2026  
**Auditor/Revisor:** Gemini (Antigravity)  
**Escopo do Plano:** Validação estatística, econométrica e de robustez contra múltiplos testes (Data-Snooping) para a suite de 16 estratégias de otimização de portfólios no mercado brasileiro (B3).

---

## Introdução: Parecer Editorial do Revisor Independente

Sob a ótica de uma revisão acadêmica cega por pares (*double-blind peer review*) para periódicos internacionais de alto impacto (ex: *Journal of Financial Economics*, *Journal of Banking & Finance* ou *Revista Brasileira de Finanças*), o principal risco metodológico de um trabalho que testa 16 estratégias de investimento sobre um universo de 102 ativos é o **viés de mineração de dados (*data-snooping bias*)**. 

Se um pesquisador rodar otimizações suficientes com parâmetros distintos, ele inevitavelmente encontrará uma estratégia que supera o benchmark (como a carteira igualmente ponderada 1/N ou o Ibovespa) meramente por acaso estatístico (*lucky draw*). Sem testes de significância robustos e controles de múltiplos testes, as conclusões empíricas do trabalho tornam-se frágeis.

Este **Plano de Testes Ampliado** estabelece um protocolo econométrico rigoroso dividido em três camadas defensivas:
1.  **Testes Clínicos Básicos (Paramétricos):** Modelagem clássica de fatores de risco e testes de Sharpe sob premissa de distribuição normal.
2.  **Testes de Robustez Não-Paramétricos (Bootstrap):** Reamostragem livre de distribuição para capturar a real estrutura de cauda e dependência temporal do mercado brasileiro.
3.  **Testes de Blindagem Avançada (Anti-Data-Snooping):** Penalização matemática sistemática pelo número de estratégias testadas para provar a existência de "alfa real".

---

## 1. Primeira Camada: Testes Clínicos Básicos (Paramétricos)

Esta camada valida a presença de prêmios de risco excedentes e realiza comparações par a par sob as premissas econométricas clássicas.

### 1.1. CAPM com Erros Padrão HAC de Newey-West (1987)
*   **Objetivo:** Estimar o retorno excedente ajustado ao risco (Alfa de Jensen, $\alpha$) e a sensibilidade sistemática (Beta, $\beta$) de cada uma das 16 estratégias em relação ao Ibovespa.
*   **Formula Geral:**
    $$R_{i,t} - R_{f,t} = \alpha_i + \beta_i (R_{m,t} - R_{f,t}) + \varepsilon_{i,t}$$
    Onde $R_{i,t}$ é o retorno diário da estratégia $i$, $R_{f,t}$ é a taxa livre de risco (CDI diário) e $R_{m,t}$ é o retorno do Ibovespa.
*   **Hipóteses do Teste:**
    $$\begin{cases} H_0: \alpha_i = 0 & \text{(Estratégia não gera retorno excedente após ajustar pelo mercado)} \\ H_1: \alpha_i \neq 0 & \text{(Estratégia gera retorno excedente significativo)} \end{cases}$$
*   **Protocolo de Rigor (HAC):** Os resíduos financeiros $\varepsilon_{i,t}$ tipicamente exibem autocorrelação e heterocedasticidade condicional. O plano de testes exige que a matriz de variância-covariância dos parâmetros seja estimada pelo método heterocedasticamente e autocorrelacionadamente consistente (**HAC de Newey-West**) com seleção automática de defasagem (lags) baseada no critério de informação de Akaike (AIC) ou regra de Bartlett:
    $$m = \lfloor 4 \times (T/100)^{2/9} \rfloor$$

### 1.2. Teste de Jobson-Korkie (1981) com Correção de Memmel (2003)
*   **Objetivo:** Comparar de forma pareada se a diferença entre o Índice de Sharpe da carteira candidata $i$ e o Índice de Sharpe da carteira de referência $j$ (ex: EqualWeight) é estatisticamente diferente de zero.
*   **Estatística de Teste ($Z$):**
    $$Z = \frac{\widehat{SR}_i - \widehat{SR}_j}{\sqrt{\widehat{\theta}}}$$
    Onde a variância assintótica da diferença $\widehat{\theta}$ é dada por:
    $$\widehat{\theta} = \frac{1}{T} \left[ 2(1 - \rho_{i,j}) + \frac{1}{2}(\widehat{SR}_i^2 + \widehat{SR}_j^2 - 2\widehat{SR}_i\widehat{SR}_j\rho_{i,j}^2) \right]$$
    E $\rho_{i,j}$ representa a correlação linear simples entre os retornos das duas estratégias.
*   **Premissas e Limitações:** Assume que os retornos são i.i.d. e seguem uma distribuição Normal conjunta.
*   **Guarda de Estabilidade:** Conforme auditado e implementado na suite, o teste deve conter guarda para séries de retornos idênticas ou constantes (volatilidade residual nula) para evitar divisão por zero:
    $$\text{Se } \sigma_i \le 10^{-14} \text{ ou } \sigma_j \le 10^{-14} \implies Z = 0.0, \, p\text{-value} = 1.0$$

---

## 2. Segunda Camada: Testes de Robustez Não-Paramétricos (Bootstrap)

O mercado brasileiro apresenta forte assimetria, caudas pesadas (curtose excessiva) e agrupamento de volatilidade, o que invalida os testes paramétricos clássicos em amostras finitas. Esta camada aplica reamostragem estatística livre de distribuição.

### 2.1. Teste de Sharpe Ratio Bootstrap de Ledoit-Wolf (2008)
*   **Objetivo:** Testar a diferença de Sharpe Ratio entre duas carteiras utilizando o método de *Stationary Bootstrap* (Politis & Romano, 1994) para gerar intervalos de confiança e p-valores robustos à dependência temporal.
*   **Mecanismo de Reamostragem (Stationary Bootstrap):**
    Em vez de reamostrar observações diárias isoladas (o que destrói a dependência temporal e a autocorrelação da volatilidade), o algoritmo sorteia blocos de dados de tamanho aleatório. O comprimento do bloco segue uma distribuição geométrica com média pré-definida ($L = 10$ dias úteis).
*   **Estatística de Teste Pivotada:**
    1.  Calcula-se o estimador pontual da diferença: $\widehat{\Delta} = \widehat{SR}_i - \widehat{SR}_j$.
    2.  Gera-se $B = 2000$ réplicas bootstrap dos retornos conjuntos das duas carteiras.
    3.  Para cada réplica $b$, calcula-se a diferença $\widehat{\Delta}^{*,b}$.
    4.  Estima-se o erro padrão bootstrap $\widehat{SE}^* = \text{std}(\widehat{\Delta}^{*,1:B})$.
    5.  O p-valor bicaudal é computado a partir do escore Z studentizado:
        $$Z = \frac{\widehat{\Delta}}{\widehat{SE}^*} \implies p = 2 \times (1 - \Phi(|Z|))$$

### 2.2. Teste de Sortino Ratio Bootstrap
*   **Objetivo:** Comparar estatisticamente a diferença entre os Índices de Sortino de duas carteiras de investimento, capturando a assimetria específica de retornos abaixo da taxa mínima de atratividade (MAR = CDI).
*   **Estatística de Teste:**
    Similar ao algoritmo de Ledoit-Wolf, contudo a métrica alvo reamostrada é o Sortino Ratio:
    $$Sortino_i = \frac{E[R_i - R_f]}{\sqrt{E[\min(R_i - R_f, 0)^2]}} \times \sqrt{252}$$
    O denominador é estimado exclusivamente sobre os desvios negativos, tornando o bootstrap crucial por lidar com estatísticas de cauda muito sensíveis ao tamanho amostral.

---

## 3. Terceira Camada: Blindagem Avançada contra Data-Snooping

Esta camada aplica filtros matemáticos severos que penalizam o desempenho das estratégias proporcionalmente ao tamanho do esforço de busca do pesquisador.

### 3.1. Deflated Sharpe Ratio — DSR (Bailey & López de Prado, 2012)
*   **Objetivo:** Ajustar e "deflacionar" o Índice de Sharpe observado da melhor estratégia para refletir o número de testes realizados, a assimetria, a curtose e a correlação mútua.
*   **Racional Científico:** Se testarmos 16 estratégias que são altamente correlacionadas entre si, o risco de falso positivo é menor do que se testarmos 16 estratégias totalmente independentes. O DSR modela formalmente essa dinâmica.
*   **Fórmula Matemática:**
    O Índice de Sharpe Mínimo Exigido ($SR^*$) para que o modelo seja considerado estatisticamente significativo com nível de confiança $\alpha$ é dado por:
    $$SR^* = \sqrt{V(\{SR_n\})} \left( (1-\gamma)\Phi^{-1}\left(1-\frac{1}{N}\right) + \gamma\Phi^{-1}\left(1-\frac{1}{N}e^{-1}\right) \right)$$
    Onde:
    *   $N$: Número de estratégias testadas ($N = 16$).
    *   $V(\{SR_n\})$: Variância dos Índices de Sharpe das $N$ estratégias.
    *   $\gamma$: Constante de Euler-Mascheroni ($\approx 0.5772$).
    *   $\Phi$: Função de distribuição acumulada da normal padrão.
    
    A partir disso, o **Deflated Sharpe Ratio (DSR)** é calculado como a probabilidade do Sharpe observado ($SR_{obs}$) superar o Sharpe mínimo sob a hipótese nula de mineração de dados:
    $$DSR = \Phi \left[ \frac{(SR_{obs} - SR_0) \sqrt{T-1}}{\sqrt{1 - \widehat{\lambda}_3 SR_{obs} + \frac{\widehat{\lambda}_4 - 1}{4} SR_{obs}^2}} \right]$$
    Onde $\widehat{\lambda}_3$ e $\widehat{\lambda}_4$ representam a assimetria e a curtose estimada dos retornos, e $SR_0$ é o Sharpe ajustado pelo viés de seleção multi-estratégia.
*   **Critério de Aprovação:** Um DSR $> 0.95$ indica que a estratégia gera retorno excedente genuíno mesmo descontando o efeito de termos testado 16 combinações diferentes de carteiras.

### 3.2. Superior Predictive Ability — SPA de Hansen (2005)
*   **Objetivo:** Avaliar de forma conjunta se o melhor modelo de alocação de carteiras (por exemplo, `MaxSharpe_c10` ou `BL_downside_c10`) supera estatisticamente o benchmark de referência (`EqualWeight`), penalizando de forma consistente pelo número total de modelos alternativos.
*   **Hipótese Nula ($H_0$):**
    $$H_0: \max_{k=1,\dots,M} E[d_{k,t}] \le 0$$
    Onde $d_{k,t} = L(R_{benchmark,t}) - L(R_{k,t})$ representa a diferença de performance (perda ou utilidade) entre o benchmark e a estratégia alternativa $k$. Se a hipótese nula não for rejeitada, conclui-se que nenhuma das estratégias alternativas é superior ao benchmark após controlar pelo viés de múltiplos testes.
*   **Vantagem sobre o Reality Check de White (2000):** O teste SPA de Hansen (2005) é assintoticamente mais poderoso porque exclui do cálculo da variância de penalização os modelos que são severamente ruins, evitando que estratégias ineficientes mascarem a performance das estratégias vencedoras.

---

## 4. Testes de Higiene e Diagnósticos de Resíduos

Antes de reportar a significância dos testes de comparação, o plano de testes exige que sejam rodados diagnósticos individuais em cada uma das séries de retornos históricos das carteiras:

| Teste Diagnóstico | Finalidade Metodológica | Racional para a Banca Examinadora |
| :--- | :--- | :--- |
| **Jarque-Bera (1980)** | Testar se os retornos seguem uma distribuição Gaussiana. | Justifica por que testes estatísticos paramétricos clássicos de finanças não são confiáveis e valida o uso de Bootstrap. |
| **Ljung-Box (1978)** | Testar se os retornos apresentam autocorrelação linear em até 10 lags. | Revela a presença de inércia ou atrito de negociação nos retornos diários das carteiras de rebalanceamento mensal. |
| **ARCH-LM de Engle (1982)** | Testar a presença de heterocedasticidade condicional autoregressiva. | Comprova cientificamente que a volatilidade ocorre em agrupamentos (*volatility clustering*), exigindo o Stationary Bootstrap. |

---

## 5. Protocolo de Execução e Orquestração no Repositório

Para garantir a reprodutibilidade científica total por revisores externos, o plano estabelece a seguinte árvore de automação no repositório:

1.  **Isolamento Estocástico:** Todas as rotinas econométricas de bootstrap e simulações Monte Carlo devem herdar deterministicamente o parâmetro de semente global extraído de `config.json` (`SEED = 42`).
2.  **Suite de Testes Rápidos (`pytest -v -m "not slow"`):** Valida a física das métricas (cálculos de Sharpe, Sortino, limites e guarda anti-divisão por zero) em menos de 10 segundos.
3.  **Suite de Testes Lentos de Monte Carlo (GARCH Size/Power):** Executa o teste de calibragem de tamanho e poder estatístico com 500 réplicas sob processos artificiais de GARCH(1,1) para provar a consistência dos p-valores gerados pelo bootstrap Ledoit-Wolf.
4.  **Interface de Validação Numérica (`revalidar.py`):** Script gatekeeper que garante que qualquer alteração de código que afete o cálculo de regressão ou pesos seja instantaneamente comparada com o `golden_master.json`.

---

## Conclusão: Contribuição Metodológica para o TCC

Ao incorporar este **Plano de Testes Ampliado** no texto dissertativo (Capítulo 3 - Metodologia, e Capítulo 4 - Análise de Resultados), o trabalho eleva-se do padrão comum de monografias e alinha-se às exigências metodológicas de periódicos científicos internacionais de primeira linha. A presença conjunta de correções robustas a autocorrelação (HAC Newey-West), reamostragem temporal (Bootstrap Ledoit-Wolf) e controle de mineração de dados (Deflated Sharpe Ratio de López de Prado) fornece blindagem absoluta contra questionamentos de bancas examinadoras rigorosas.
