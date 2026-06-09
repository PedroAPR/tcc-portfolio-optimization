# Relatório de Recomendações e Checklist Acadêmico — Padrão A1 (Fase P6)

**Objetivo:** Propor melhorias visuais, estruturais e de robustez estatística para elevar o TCC ao nível de excelência científica exigido para publicação em periódicos de alto impacto (Qualis A1 / Classificação Internacional).

---

## 1. Tabelas e Figuras Recomendadas para Padrão de Periódico

Para enriquecer a análise empírica e aproximar o documento das publicações internacionais em finanças quantitativas, recomenda-se a inclusão dos seguintes elementos visuais:

1.  **Curvas de Riqueza Acumulada (Log Scale):**
    *   *Descrição:* Gráfico de linha que demonstra o crescimento de $1,00 investido em março de 2015 até dezembro de 2025 para as 16 estratégias, plotado em escala logarítmica para evitar distorções visuais de crescimento composto extremo nas estratégias vencedoras (como a família Black-Litterman).
2.  **Gráfico "Underwater" de Drawdown:**
    *   *Descrição:* Visualização de área preenchida invertida (abaixo de 0%) demonstrando os rebaixamentos acumulados das estratégias principais (EqualWeight, MinVar, BL e MinCDaR). Facilita a identificação visual da profundidade e tempo de recuperação das perdas de capital da carteira CDaR que sofreu forte queda.
3.  **Heatmap de Evolução de Pesos:**
    *   *Descrição:* Heatmap bidimensional (Eixo X: Tempo; Eixo Y: Ativos) demonstrando a dinâmica de pesos das estratégias principais ao longo dos 130 rebalanceamentos. É indispensável para ilustrar o efeito do teto de 10% (CVM 175) e a esparsidade gerada pela penalidade Lasso de custo de transação.
4.  **Sharpe Ratio Móvel (Rolling Sharpe):**
    *   *Descrição:* Sharpe ratio calculado em janelas móveis de 24 ou 36 meses para as estratégias concorrentes principais, ilustrando a estabilidade temporal da performance sob diferentes regimes de mercado (crise de 2015-2016, COVID-2020 e ciclo de juros de 2022).
5.  **Matriz Estratégia × Métrica Consolidada:**
    *   *Descrição:* Tabela unificada contendo CAGR, Volatilidade, Sharpe, Sortino, Max Drawdown, Calmar, Turnover médio anual e Retorno Líquido para todas as 16 estratégias concorrentes, facilitando a comparação transversal imediata.
6.  **Matriz de Significância Par a Par (p-valores):**
    *   *Descrição:* Matrizes triangulares exibindo os p-valores dos testes estatísticos de comparação de Sharpe (Jobson-Korkie/Memmel e Ledoit-Wolf Bootstrap) para todos os pares de carteiras, destacando com asteriscos (*, **, ***) a rejeição de H0 de igualdade de performance.
7.  **Heatmap de Correlação Estatística entre Estratégias:**
    *   *Descrição:* Mostra a correlação dos retornos diários fora da amostra entre as 16 estratégias, confirmando se variantes como `BL_downside` e `BL_classico` operam de forma redundante ou se possuem dinâmicas distintas.
8.  **Tabela de Turnover × Fricção Transacional:**
    *   *Descrição:* Exibição do impacto dos custos transacionais no CAGR das estratégias sensíveis ao giro (família BL e MinCDaR), simulando cenários alternativos de 0 bps, 25 bps, 50 bps (padrão) e 100 bps de custo transacional.

---

## 2. Lista de Abreviaturas e Siglas

Recomenda-se a inclusão de uma seção formal contendo as seguintes siglas compiladas do texto, verificando-se a necessidade de definição na sua primeira ocorrência:

*   **MPT:** *Modern Portfolio Theory* (Teoria Moderna do Portfólio) — introduzida por Harry Markowitz em 1952.
*   **PMPT:** *Post-Modern Portfolio Theory* (Teoria Pós-Moderna do Portfólio) — focada em medidas assimétricas de risco.
*   **BL:** *Black-Litterman* — modelo Bayesiano de alocação de ativos.
*   **CAPM:** *Capital Asset Pricing Model* (Modelo de Precificação de Ativos de Capital) — âncora de equilíbrio do prior.
*   **VaR:** *Value-at-Risk* (Valor em Risco) — medida de perda máxima esperada sob um nível de confiança.
*   **CVaR:** *Conditional Value-at-Risk* (Valor em Risco Condicional) — perda esperada na cauda além do VaR.
*   **CDaR:** *Conditional Drawdown-at-Risk* (Rebaixamento Condicional em Risco) — média dos piores rebaixamentos da riqueza.
*   **MAD:** *Median Absolute Deviation* (Mediana dos Desvios Absolutos) — estatística robusta de dispersão.
*   **SLSQP:** *Sequential Least Squares Programming* (Programação Quadrática Sequencial) — otimizador de restrições lineares.
*   **LP:** *Linear Programming* (Programação Linear) — formulação matemática usada para resolver CVaR e CDaR.
*   **PSD:** *Positive Semi-Definite* (Semi-definida Positiva) — propriedade matemática exigida para matrizes de covariância.
*   **CAGR:** *Compound Annual Growth Rate* (Taxa de Crescimento Anual Composta).
*   **CVM:** Comissão de Valores Mobiliários (regulador brasileiro).
*   **CVM 175:** Resolução CVM nº 175/2022 (limite de 10% de alocação por emissor para varejo).
*   **B3:** Brasil, Bolsa, Balcão (bolsa de valores brasileira).
*   **CDI:** Certificado de Depósito Interbancário (proxy da taxa livre de risco Rf no Brasil).
*   **SELIC:** Sistema Especial de Liquidação e de Custódia.
*   **IBOV / IBOVESPA:** Índice da Bolsa de Valores de São Paulo (proxy do portfólio de mercado).
*   **FF3 / FF5:** Modelos de 3 e 5 Fatores de Fama e French (1993, 2015).
*   **WML:** *Winners Minus Losers* (Fator Momentum de Jegadeesh e Titman, 1993).
*   **SMB:** *Small Minus Big* (Fator Tamanho de Fama e French).
*   **HML:** *High Minus Low* (Fator Valor de Fama e French).
*   **RMW:** *Robust Minus Weak* (Fator Lucratividade de Fama e French).
*   **CMA:** *Conservative Minus Aggressive* (Fator Investimento de Fama e French).
*   **LPM:** *Lower Partial Moment* (Momento Parcial Inferior).
*   **MAR:** *Minimum Acceptable Return* (Retorno Mínimo Aceitável).
*   **OOS / IS:** *Out-of-Sample* (Fora da Amostra) / *In-Sample* (Na Amostra).
*   **HAC:** *Heteroskedasticity and Autocorrelation Consistent* (Erros robustos de Newey-West).
*   **OLS:** *Ordinary Least Squares* (Mínimos Quadrados Ordinários).
*   **ADF:** *Augmented Dickey-Fuller* (Teste de raiz unitária Dickey-Fuller Aumentado).
*   **ARCH / GARCH:** Modelos de Heterocedasticidade Condicional Autorregressiva.

---

## 3. Checklist de Excelência A1 / Periódico

Esta seção consolida as exigências de qualidade metodológica comuns a periódicos de alto impacto:

### 3.1. Reprodutibilidade
*   **Sementes Psico-Aleatórias (Seeds):** A semente randômica central (`SEED=42`) deve ser propagada universalmente em todo código de simulação bootstrap para garantir que os p-valores sejam 100% idênticos a cada execução.
*   **Requirements Fixados:** O arquivo `requirements.txt` foi limpo com sucesso de dependências legadas e pacotes não utilizados (TensorFlow, Keras, hmmlearn). Versões mínimas das bibliotecas científicas foram declaradas.
*   **Script de Pipeline Único:** O pipeline é executado via script CLI centralizado, mitigando inconsistências comuns de notebooks rodados fora de ordem.
*   **Disponibilidade de Dados:** O TCC deve incluir uma declaração explícita informando que o código é de livre acesso, mas que os dados brutos são protegidos por licença proprietária comercial (Economática), fornecendo os caminhos necessários para que um terceiro com acesso à mesma base possa reproduzir os retornos estruturados.

### 3.2. Robustez
*   **Sensibilidade a Custos de Transação:** O pipeline deve testar e documentar o Sharpe ex-post sob custos de transação alternativos ($0, 25, 50, 100\text{ bps}$). Isso protege o trabalho de revisores que aleguem que o desempenho da carteira Black-Litterman decorre exclusivamente de giro excessivo sob custos irrealisticamente baixos.
*   **Estabilidade por Subperíodos (Sub-sample Analysis):** Apresentar a performance das estratégias subdividida em regimes:
    1.  *Regime Recessivo / Volátil (2015-2018):* Crise político-econômica nacional.
    2.  *Regime de Transição / Choque (2019-2022):* Ciclo COVID-19 e deflação/inflação extrema.
    3.  *Regime Recente (2023-2025):* Recuperação de juros.
*   **Taxa Livre de Risco Alternativa:** A adoção do CDI como livre de risco é a praxe brasileira, mas revisores internacionais frequentemente exigem taxas indexadas à inflação real (como NTN-B curtas) para descontar o Sharpe de excesso.
*   **Correção de Múltiplos Testes:** O pipeline implementa a correção de Holm-Bonferroni sobre as matrizes de significância, o que é excelente e responde à principal crítica de *data-snooping* (viés de seleção).
*   **Data-Snooping Avançado:** Recomenda-se a menção conceitual ao *Deflated Sharpe Ratio* (Bailey & López de Prado) ou ao *Stepwise SPA* (Hansen) para consolidar a robustez matemática.

### 3.3. Transparência e Limitações
*   **Viés de Sobrevivência (Survivorship Bias):** O fato de o painel de 102 ativos reter apenas empresas sobreviventes ativas em 2025 deve ser transparentemente reportado como limitação no resumo.
*   **Liquidez Mínima:** Declarar que manter ativos de baixa liquidez (que passaram raspando nos 95% de pregões mas possuem spreads elevados em certos meses) introduz ruído que a taxa fixa de 50 bps pode não cobrir integralmente.
*   **Divergências Teóricas:** Admitir na dissertação os dois pontos identificados na auditoria de rastreabilidade:
    1.  Que o `MaxSharpe` foi otimizado diretamente na sua forma de razão não-linear, em vez de utilidade quadrática.
    2.  Que a covariância posterior $\Sigma_{BL}$ foi omitida no otimizador para estabilizar as matrizes e evitar soluções degeneradas derivadas de ruídos nos retornos de momentum.

---

## 4. Matriz de Priorização (Impacto × Esforço)

Para guiar o aprimoramento final do TCC com prazo crítico até **29 de junho**, as recomendações foram estruturadas em ordem decrescente de prioridade:

| Recomendação Recomendada | Tipo | Impacto na Avaliação | Esforço para Implementar | Nota de Prioridade | Ação Sugerida |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Correção de Sharpe vs. Utilidade** | Texto | **Crítico (Erro Teórico)** | Baixo | **10 / 10** | Ajustar parágrafo `P1107-1108` para descrever a otimização direta via SLSQP. |
| **Correção do Cálculo de $\Sigma_{BL}$**| Texto/Código| **Crítico (Incoerência)** | Baixo (se ajuste no texto) | **9,5 / 10** | Adicionar ressalva na metodologia declarando o uso de prior $S$ na otimização. |
| **Heatmap de Evolução de Pesos** | Visual | **Alto (A1 Standard)** | Baixo (código já gera pesos) | **9,0 / 10** | Plotar o heatmap a partir de `pesos_historico.csv`. |
| **Underwater Drawdown Plot** | Visual | **Alto (A1 Standard)** | Baixo | **8,5 / 10** | Plotar a partir do acumulado de retornos diários. |
| **Análise de Custos Alternativos** | Robustez | **Alto (Robustez)** | Médio | **7,5 / 10** | Roda de pipeline para $0$ e $100\text{ bps}$ e inclusão de tabela sintética. |
| **Lista de Abreviaturas Completa** | Estrutura | **Médio (ABNT)** | Baixo | **7,0 / 10** | Incluir a compilação do item 2 nas páginas preliminares do Word. |
| **Estabilidade por Subperíodos** | Robustez | **Alto (Estatístico)** | Médio | **6,5 / 10** | Gerar tabela de Sharpe/CAGR dividida em 2015-18, 2019-22 e 2023-25. |
| **DSR / Testes SPA** | Robustez | **Baixo (Teórico)** | Alto | **3,0 / 10** | Apenas citar como extensão nas limitações metodológicas. |
