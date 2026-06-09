# Relatório de Análise e Orientação Metodológica para o TCC "Moderna Teoria das Carteiras no Mercado de Ações Brasileiro"


## Introdução

Este documento apresenta uma análise técnica e um plano de ação estruturado com base no Trabalho de Conclusão de Curso (TCC) submetido, intitulado "Moderna Teoria das Carteiras no Mercado de Ações Brasileiro: Uma Opção para Diversificação e Gerenciamento do Risco".1 O objetivo deste relatório é fornecer um diagnóstico das inconsistências críticas presentes no documento atual e oferecer um roteiro metodológico detalhado para sua correção, aprimoramento e conclusão. O foco é elevar o rigor acadêmico, a coesão interna e a contribuição quantitativa da pesquisa.
O relatório está dividido em quatro partes:
**Diagnóstico Crítico e Direcionamento Metodológico:** Identifica e resolve as inconsistências fundamentais de escopo, estrutura e período de análise.
**Fluxo de Trabalho Estratégico:** Define um plano de ação sequencial com atividades granulares.
**Revisão Gramatical e Semântica:** Apresenta correções e melhorias para o texto existente.
**Guia de Redação por Capítulo:** Fornece um conjunto exaustivo de prompts e questões-guia para preencher todas as seções do TCC, incluindo as ausentes.

## PARTE 1: DIAGNÓSTICO CRÍTICO E DIRECIONAMENTO METODOLÓGICO

A análise do documento 1 revela três inconsistências centrais que impedem o desenvolvimento coeso do trabalho. Estas devem ser resolvidas antes de qualquer nova redação.1

### 1.1 A Inconsistência de Escopo (A Tese Central)

O documento apresenta duas teses de pesquisa conflitantes 1:
**Tese do Resumo:** O objetivo é "avaliar o desempenho de carteiras desenvolvidas de acordo com a Moderna Teoria das Carteiras (MPT) com a Pós-Moderna Teoria do Portifolio (PMPT)".1 Isso sugere uma *comparação de frameworks de otimização* (ex: Média-Variância vs. Média-Semivariância).
**Tese da Introdução:** A questão de pesquisa é "qual é o impacto da substituição da média histórica ($\mu$) por modelos de previsão estatísticos (ARIMA) e de *machine learning* (LSTM) na performance de portfólios otimizados pelo método de Markowitz".1 Isso sugere uma *melhoria de inputs* ($\mu$) dentro de um único *framework* (MPT).
Estas são duas pesquisas distintas. A Tese 2 (ARIMA/LSTM) é tecnicamente mais sofisticada, mais original no contexto de um TCC de graduação e aborda uma das críticas mais relevantes à MPT: o *erro de estimação* (estimation risk) dos retornos esperados.
Direcionamento Metodológico:
O TCC deve adotar a Tese 2 (ARIMA/LSTM) como seu foco exclusivo. O Resumo atual 1 deve ser descartado e reescrito ao final. Os conceitos da PMPT (mencionados na Tese 1) não serão o foco da otimização, mas serão reintegrados de forma elegante: serão usados como métricas de avaliação de desempenho (ex: Índice de Sortino, CVaR) para comparar as carteiras geradas pela Tese 2. Isso unifica todas as ideias presentes no documento.

### 1.2 A Inconsistência Estrutural (Sumário vs. Texto)

A estrutura do documento está desalinhada 1:
O **Sumário** lista: 2. METODOLOGIA, 3. REFERENCIAL TEÓRICO.1
A **Introdução** descreve: Capítulo 2 (Revisão da Literatura), Capítulo 3 (Metodologia).1
Capítulos essenciais (4. Análise de Resultados, 5. Conclusão), mencionados na Introdução, estão ausentes do Sumário.1
Direcionamento Estrutural:
A estrutura acadêmica padrão deve ser aplicada. O Sumário e o documento devem seguir esta ordem:
Introdução
Referencial Teórico
Metodologia da Pesquisa
Análise e Discussão dos Resultados
Conclusão

### 1.3 A Inconsistência Temporal (Período de Análise)

Os períodos de análise divergem dentro do próprio documento 1:
**Introdução (Problema de Pesquisa):** Período de 2010 a 2024.1
**Metodologia (Universo e Amostra):** Período de janeiro de 2015 a dezembro de 2023.1
Direcionamento Temporal:
Para uma pesquisa que envolve backtesting de modelos preditivos (ARIMA/LSTM), um período de análise mais longo é preferível, pois captura múltiplos regimes de mercado (ex: crise de 2014, crash da COVID-19, recuperação). O período de 2010-2024 (ou o mais longo possível) é o mais indicado.
Mais importante, a metodologia 1 falha em definir o conceito de **janelas de treino e teste** (ex: janelas deslizantes ou expansíveis), que é a forma correta de aplicar modelos preditivos em *backtesting*. O período de análise não será monolítico, mas sim dividido em sucessivas janelas de estimação e previsão.

## PARTE 2: FLUXO DE TRABALHO ESTRATÉGICO (PLANO DE AÇÃO)

Para a conclusão bem-sucedida do TCC, recomenda-se a seguinte ordem de atividades ("atividades menores"):
**Fase 1: Definição e Estruturação (Atividades Imediatas)**
**Atividade:** Corrigir a estrutura do arquivo .docx.
**Detalhe:** Renomear e reordenar os capítulos no Sumário para refletir a estrutura correta (Intro, Ref. Teórico, Metodologia, Resultados, Conclusão).
**Atividade:** Reescrever o Capítulo 1 (Introdução).
**Detalhe:** Utilizar os prompts da Parte 4 deste relatório para redefinir o problema de pesquisa, objetivos (geral e específicos) e justificativa, focando *exclusivamente* no tema ARIMA/LSTM e no erro de estimação de $\mu$.1
**Fase 2: Fundamentação Teórica (Redação)**
**Atividade:** Completar o Capítulo 2 (Referencial Teórico).
**Detalhe:** O material existente sobre MPT, VaR e CVaR é um bom começo.1 Utilizar os prompts da Parte 4 para *adicionar* as seções críticas que estão faltando 1:
2.X Pós-Moderna Teoria de Carteiras (foco em Semivariância e Índice de Sortino).
2.X Modelos de Previsão de Séries Temporais (ARIMA).
2.X Modelos de *Machine Learning* (Redes Neurais LSTM).
**Fase 3: Execução Metodológica (Coleta e Modelagem)**
**Atividade:** Redefinir a Amostra e Coletar os Dados.
**Detalhe:** Substituir o critério de amostra vago ("volume de negócios superior a zero" 1) por um critério rigoroso de liquidez (ex: presença no IBOVESPA, volume médio diário). Coletar as séries temporais de preços.
**Atividade:** Escrever o roteiro (script) de *backtest*.
**Detalhe:** Definir em código (Python ou R) a lógica de *backtesting* (ex: janela deslizante *walk-forward*), o período de treino (ex: 60 meses) e o período de teste/rebalanceamento (ex: 1 mês).
**Atividade:** Executar os modelos preditivos.
**Detalhe:** Em cada janela de treino, treinar os modelos (ARIMA, LSTM) para prever o $\mu$ do próximo período de teste para cada ativo.
**Atividade:** Otimizar as carteiras.
**Detalhe:** Em cada período de teste, utilizar os $\mu$ previstos (Histórico, ARIMA, LSTM) e a matriz de covariância ($\Sigma$) histórica para calcular os pesos da carteira otimizada (ex: Max Sharpe).
**Fase 4: Análise e Redação Final**
**Atividade:** Gerar os resultados consolidados.
**Detalhe:** Calcular as métricas de performance (Sharpe, Sortino, Drawdown, Retorno Anualizado) para a série temporal de retornos de cada uma das carteiras simuladas e dos *benchmarks* (IBOV, CDI).
**Atividade:** Escrever o Capítulo 4 (Análise e Discussão dos Resultados).
**Detalhe:** Preencher as tabelas de resultados e interpretar graficamente a evolução do patrimônio.
**Atividade:** Escrever o Capítulo 5 (Conclusão).
**Detalhe:** Responder objetivamente à nova pergunta de pesquisa, discutir limitações e propor trabalhos futuros.
**Fase 5: Revisão e Fechamento**
**Atividade:** Escrever o Resumo (Abstract).
**Detalhe:** *Somente agora*, escrever o Resumo, garantindo que ele reflita o trabalho que foi *realmente* executado (ARIMA/LSTM).
**Atividade:** Revisão final de formatação e referências.

## PARTE 3: REVISÃO GRAMATICAL E SEMÂNTICA DO TEXTO EXISTENTE

Com base na análise do texto existente 1, foram identificados padrões que necessitam de correção para atingir um rigor acadêmico superior. A tabela abaixo apresenta exemplos de correções necessárias.
**Tabela 1: Correções de Gramática e Estilo Acadêmico**


| Texto Original (do ) | Problema Identificado | Sugestão de Revisão e Justificativa |
| --- | --- | --- |
| "Apesar do avanço, observou-se também uma queda no saldo mediano em custódia — de R$ 7 mil para R$ 3 mil... — sugerindo a entrada de pequenos investidores..." | Coesão / Pontuação | "Apesar do avanço, observou-se também uma queda no saldo mediano em custódia (de R$ 7 mil para R$ 3 mil...), o que sugere a entrada de pequenos investidores..." Justificativa: O uso de travessões (—) é menos formal que parênteses () para intercalar dados em texto corrido. O gerúndio "sugerindo" é substituído por "o que sugere", uma oração adjetiva explicativa que oferece melhor coesão. |
| "...muitos dos quais sem conhecimento técnico profundo sobre gestão de portfólios." | Vocabulário / Preposição | "...muitos dos quais sem conhecimento técnico aprofundado em gestão de portfólios." Justificativa: "Aprofundado" é um termo mais formal. A regência de "conhecimento" é mais precisa com a preposição "em" ou "de" do que "sobre" neste contexto. |
| "Diante desse panorama, este trabalho busca responder à seguinte questão de pesquisa: q ual é o impacto..." | Formatação / Gramática | "Diante desse panorama, este trabalho busca responder à seguinte questão de pesquisa: Qual é o impacto..." Justificativa: Erro de formatação ("q ual") e uso de minúscula após dois-pontos que introduzem uma citação direta (a pergunta). A primeira letra da pergunta deve ser maiúscula.1 |
| "Um ativo livre de risco é aquele que oferece ao investidor a certeza do retorno esperado, resultando em um risco-variância igual a zero..." | Terminologia (Semântica) | "Um ativo livre de risco é aquele que oferece ao investidor a certeza do retorno esperado, resultando em uma variância (risco) dos retornos igual a zero..." Justificativa: Conforme 1, "risco-variância" é uma terminologia redundante no contexto da MPT, onde a variância é a métrica de risco. A correção clarifica o conceito. (Nota: O sobrenome "Reily" está grafado incorretamente no original, devendo ser "Reilly" 1). |
| "A metodologia Média-Variância possui duas premissas básicas: a normalidade das distribuições dos retornos dos ativos e que as funções de utilidade... são quadráticas." | Gramática (Paralelismo) | "A metodologia Média-Variância possui duas premissas básicas: (1) a normalidade das distribuições dos retornos dos ativos e (2) a suposição de que as funções de utilidade... são quadráticas." Justificativa: Quebra de paralelismo estrutural.1 O primeiro item da lista é um substantivo ("a normalidade"), enquanto o segundo é uma oração ("que as funções..."). A correção padroniza a lista (substantivo + substantivo). |


## PARTE 4: GUIA DE REDAÇÃO POR CAPÍTULO (PROMPTS DETALHADOS)

Esta seção fornece questões-guia detalhadas para a redação ou reescrita de cada capítulo do TCC, com base nas lacunas identificadas em 1 e no escopo redefinido na Parte 1.

### Capítulo 1: INTRODUÇÃO (A SER REESCRITO)

**Contextualização (O Cenário):**
(Manter os parágrafos 1 e 2 sobre a democratização da B3 e a entrada de pessoas físicas 1).
Como a MPT de Markowitz (1952) se propõe como a solução *tradicional* para o problema desses novos investidores? (Descrever brevemente o dilema risco vs. retorno).
Qual é a principal *crítica* ou *limitação* da MPT na prática, especificamente em relação aos seus *inputs* (parâmetros de entrada)? (Aponte para a dificuldade de estimar $\mu$, o retorno esperado).
**Problematização (A Lacuna):**
Por que usar a média histórica simples dos retornos passados como uma estimativa para o retorno futuro ($\mu$) é problematicamente ingênuo? (Citar DeMiguel e Nogales (2009), já presente em 1).
Como a instabilidade dos mercados emergentes, como o Brasil (volatilidade, assimetria, caudas longas), torna essa estimativa histórica ainda menos confiável?
Se os *inputs* (estimativas de retorno) são ruins, a otimização de Markowitz, mesmo sendo matematicamente elegante, produzirá carteiras "ótimas" que são, na verdade, subótimas (o chamado *erro de estimação* ou *estimation risk*).
Como modelos estatísticos (ARIMA) e de *machine learning* (LSTM) surgem como alternativas potenciais para *melhorar* a estimação desse $\mu$? Qual a promessa teórica deles (capturar dinâmicas temporais e não-linearidades que a média histórica ignora)?
**Questão de Pesquisa (O Foco Central - Corrigido):**
(Substituir a pergunta existente em 1 por esta): "Qual é o impacto no desempenho, ajustado ao risco, de carteiras Média-Variância otimizadas no mercado brasileiro, quando o *input* de retorno esperado ($\mu$) é estimado por modelos preditivos (ARIMA e LSTM) em comparação com a tradicional média histórica?"
**Objetivos:**
**Geral:** Avaliar o ganho de performance (se houver) ao aplicar modelos de previsão de séries temporais (ARIMA) e *machine learning* (LSTM) na estimação de retornos esperados para a otimização de portfólios de Markowitz no Brasil.
**Específicos:**
Revisar a literatura sobre MPT, suas limitações (especialmente o erro de estimação) e os fundamentos dos modelos ARIMA e LSTM.
Coletar e tratar dados de séries temporais de ativos listados na B3 (definir o período e critérios de liquidez).
Implementar e treinar os modelos ARIMA e LSTM para prever os retornos dos ativos em um esquema de *backtesting* robusto.
Construir (via simulação) carteiras otimizadas (ex: Max Sharpe) usando três fontes de $\mu$: (a) Média Histórica, (b) Previsão ARIMA, (c) Previsão LSTM.
Comparar o desempenho das carteiras (e *benchmarks* como IBOV e CDI) usando métricas de risco-retorno (ex: Sharpe, Sortino, Max Drawdown).
**Justificativa:**
Por que esta pesquisa é relevante para o investidor pessoa física no Brasil? (Ajuda a navegar a volatilidade com ferramentas mais robustas).
Qual a contribuição acadêmica? (Testa a eficácia de modelos de ML, um tema atual, em um *framework* clássico (MPT) no contexto específico do mercado brasileiro).
**Estrutura do Trabalho:**
(Corrigir este parágrafo, que está errado em 1, para refletir a nova estrutura): "Este trabalho está estruturado da seguinte forma: o Capítulo 2 apresenta o referencial teórico... O Capítulo 3 descreve a metodologia... O Capítulo 4 analisa os resultados... O Capítulo 5 apresenta as conclusões."

### Capítulo 2: REFERENCIAL TEÓRICO (A SER COMPLETADO)

Status (Baseado em 1): As seções sobre MPT, VaR e CVaR 1 são um bom começo. Agora, as seções que faltam devem ser adicionadas para dar suporte à nova questão de pesquisa.
**2.1. A Moderna Teoria de Carteiras (MPT)**
(Manter o conteúdo sobre Diversificação, Risco Sistemático/Não Sistemático e Análise Média-Variância 1).
*Adicionar:* Detalhar matematicamente como o retorno esperado e a variância de uma carteira com N ativos são calculados (as fórmulas). Destacar a importância da matriz de covariância.
*Adicionar:* Explicar o "Erro de Estimação" (*Estimation Risk*). Por que a MPT é tão sensível aos *inputs*? (Citar Elton e Gruber (1997) e DeMiguel e Nogales (2009), já presentes em 1).
**2.2. Pós-Moderna Teoria de Carteiras (PMPT) e Métricas de Risco *****Downside***
Insight (1): Esta seção está faltando, mas é crucial para justificar *como* as carteiras serão avaliadas.
Por que a variância (usada pela MPT) é uma métrica de risco "cega"? (Ela penaliza tanto a volatilidade "boa" (para cima) quanto a "ruim" (para baixo)).
O que são Finanças Comportamentais (mencionadas na intro de 1) e como elas justificam que investidores se preocupam mais com perdas do que com variabilidade?
Definir **Semivariância**: O que é? Como ela difere da variância? (Ela só mede a dispersão dos retornos *abaixo* de um alvo).
Definir o **Índice de Sortino**: Qual a fórmula? Por que ele é um "Sharpe Ratio melhorado" no contexto da PMPT? (Usa semivariância no denominador).
**2.3. Modelos de Previsão de Séries Temporais (ARIMA)**
Insight (1): Esta seção é *nova* e *vital*.
O que é uma série temporal financeira? Quais suas características (não estacionariedade, clusterização de volatilidade)?
O que é **estacionariedade**? Por que a maioria das séries de preços não é estacionária, mas os retornos são? Como testar (ex: Teste Dickey-Fuller)?
Definir o modelo **ARIMA (p, d, q)**:
O que significa a parte **AR (p)** (Autoregressiva)?
O que significa a parte **I (d)** (Integrada)?
O que significa a parte **MA (q)** (Média Móvel)?
Como o ARIMA será usado no trabalho? (Ele tentará prever o $\mu$ do próximo período com base na estrutura temporal dos retornos passados).
**2.4. Modelos de *****Machine Learning***** (LSTM)**
Insight (1): Esta seção também é *nova* e *vital*.
O que são Redes Neurais Artificiais (RNAs)? (Breve explicação de neurônios, camadas, pesos).
O que são Redes Neurais Recorrentes (RNNs)? Por que elas são boas para dados sequenciais?
Qual é o problema das RNNs simples (o "desvanecimento do gradiente" ou *vanishing gradient*)?
Como a arquitetura **LSTM (Long Short-Term Memory)** resolve esse problema? (Explicar os "portões": *input*, *forget* e *output gate*). O que é a "célula de memória"?
Por que, teoricamente, um LSTM pode ser superior a um ARIMA para prever retornos? (Capacidade de capturar padrões não lineares e dependências de longo prazo).

### Capítulo 3: METODOLOGIA DA PESQUISA (A SER REESCRITA)

Status (1): A metodologia atual é vaga, desalinhada (fala em TMPT) e o critério de amostragem é fraco. É necessário detalhar o *processo quantitativo* de forma replicável.
**3.1. Tipo de Pesquisa**
(Reescrever): Esta pesquisa é classificada como **quantitativa**, **descritiva** e **aplicada**. Utiliza-se da **modelagem e simulação** (*backtesting*) como principal técnica de análise de dados.
**3.2. Definição da Amostra e Coleta de Dados**
Qual será o **Universo**? (Ações do IBOVESPA? IBrA-100?).
Qual será o **Período de Análise**? (Justificar o período 2010-2024).
Quais os **Critérios de Inclusão/Filtro**? (Substituir o critério "volume > 0" 1 por critérios rigorosos. Sugestão: "Ações que compuseram o IBrA-100 em pelo menos 80% dos meses do período de análise" ou "Ações com volume médio diário de negociação acima de R$ X").
Qual a **Fonte dos Dados**? (Economática 1, Profit? Yahoo Finance?).
Qual a **Frequência dos Dados**? (Diários? Semanais? Mensais?). (Sugestão: Diários).
Como os dados serão **Tratados**? (Cálculo dos retornos logarítmicos? Ajuste de dividendos e *splits*?).
**3.3. Desenho Experimental (A Estratégia de *****Backtest*****)**
Esta é a seção mais importante que falta.1
Será utilizada uma **Janela Deslizante (*****Rolling Window*****)** ou **Janela Expansível (*****Expanding Window*****)**? (Justificar a escolha).
Qual o **Tamanho da Janela de Treino**? (Ex: 60 meses / 1250 dias de pregão).
Qual o **Período de Teste/Previsão**? (Ex: prever o $\mu$ para o próximo 1 mês / 21 dias).
Qual a **Frequência de Rebalanceamento** da carteira? (Mensal? Trimestral?). (Justificar. Ex: Mensal, para capturar as novas previsões dos modelos sem gerar custos de transação excessivos).
**3.4. Modelagem dos *****Inputs***** (As Três Carteiras)**
Para cada período de rebalanceamento no *backtest*, como os *inputs* (Retorno $\mu$ e Matriz de Covariância $\Sigma$) serão calculados?
**Cálculo da Matriz de Covariância ($\Sigma$)**: Será a mesma para todas as carteiras? (Sugestão: Sim, usar a covariância histórica da Janela de Treino. O foco do TCC é no $\mu$).
**Cálculo do Vetor de Retorno Esperado ($\mu$)**:
**Carteira 1 (Baseline - Média Histórica):** O $\mu$ de cada ativo será a média aritmética simples dos retornos na Janela de Treino.
**Carteira 2 (ARIMA):** Para cada ativo, um modelo ARIMA(p,d,q) será ajustado aos dados da Janela de Treino (Como p,d,q serão escolhidos? Auto-ARIMA?). O modelo fará uma previsão *out-of-sample* para o Período de Teste. O $\mu$ será essa previsão.
**Carteira 3 (LSTM):** Para cada ativo, um modelo LSTM será treinado na Janela de Treino (Definir a arquitetura: quantas camadas? neurônios? *lookback period*?). O modelo fará uma previsão *out-of-sample* para o Período de Teste. O $\mu$ será essa previsão.
**3.5. Processo de Otimização (O Método de Markowitz)**
Qual portfólio de Markowitz será montado? (Carteira de **Máximo Índice de Sharpe**? É a mais recomendada, pois usa o $\mu$ e o $\Sigma$).
Qual será a *proxy* para a Taxa Livre de Risco (R_f)? (O CDI, como citado em 1).
Haverá **restrições**? (Ex: Pesos 100% comprados ($w_i \ge 0$, $\Sigma w_i = 1$)? Peso máximo por ativo?).
**3.6. Métricas de Avaliação de Desempenho**
Como as carteiras serão comparadas? (Usar todas estas):
**Retorno:** Retorno Total Acumulado e Retorno Médio Anualizado.
**Risco (MPT):** Volatilidade (Desvio Padrão) Anualizada.
**Risco (PMPT):** Semivariância Anualizada e Máximo *Drawdown*.
**Retorno/Risco (MPT):** Índice de Sharpe.
**Retorno/Risco (PMPT):** Índice de Sortino.
**Benchmarks:** Comparar contra IBOVESPA e CDI.1

### Capítulo 4: ANÁLISE E DISCUSSÃO DOS RESULTADOS (CAPÍTULO NOVO)

Este capítulo ainda não existe.1 Ele é o "coração" do TCC.
**4.1. Estatísticas Descritivas dos Dados**
Descrever a amostra final (Quantos ativos? De quais setores?).
Apresentar uma tabela com as estatísticas descritivas dos retornos dos ativos (Média, Volatilidade, Assimetria, Curtose).
*Análise:* Os dados são normalmente distribuídos? (Provavelmente não. Curtose alta e assimetria justificam o uso de PMPT e LSTM).
**4.2. Resultados do *****Backtest***** (Comparação de Desempenho)**
Apresentar o gráfico da evolução do patrimônio (R$ 100,00 iniciais) ao longo do tempo (Período de Teste) para as 3 carteiras + 2 benchmarks (IBOV, CDI). Este é o gráfico principal.
Apresentar a tabela-resumo que responde à pergunta de pesquisa.
**Tabela 2: Métricas de Performance Consolidadas (Período de Teste Total)**

| Métrica | Carteira Média Histórica | Carteira ARIMA | Carteira LSTM | IBOVESPA | CDI |
| --- | --- | --- | --- | --- | --- |
| Retorno Anualizado | X.X% | Y.Y% | Z.Z% | B.B% | C.C% |
| Volatilidade Anualizada | X.X% | Y.Y% | Z.Z% | B.B% | C.C% |
| Índice de Sharpe | X.X | Y.Y | Z.Z | B.B | C.C |
| Índice de Sortino | X.X | Y.Y | Z.Z | B.B | - |
| Máximo Drawdown | -X.X% | -Y.Y% | -Z.Z% | -B.B% | -C.C% |

**4.3. Discussão e Interpretação dos Resultados**
*Não apenas apresentar os números, mas interpretá-los.*
Qual carteira venceu no critério de Sharpe? E no de Sortino?
Os modelos preditivos (ARIMA, LSTM) conseguiram superar o *baseline* (Média Histórica)?
O LSTM (não linear) foi melhor que o ARIMA (linear)? Por que isso pode ter acontecido?
Como as carteiras se comportaram em períodos de crise (ex: COVID-19)? O Máximo *Drawdown* foi menor para os modelos preditivos?
Discutir o *Turnover* (giro da carteira). As carteiras preditivas sugerem muitas mudanças (alto custo transacional)? (Pode ser uma limitação).

### Capítulo 5: CONCLUSÃO (CAPÍTULO NOVO)

Este capítulo também não existe.1
**5.1. Síntese dos Achados**
Começar retomando a pergunta de pesquisa (Cap. 1): "Este trabalho se propôs a avaliar o impacto...".
Responder objetivamente: Qual foi o impacto? (Ex: "Os resultados do *backtest* demonstram que a substituição da média histórica por modelos LSTM resultou em um aumento de XX% no Índice de Sharpe...").
Resumir os achados da Tabela 2.
**5.2. Contribuições do Trabalho**
Qual a contribuição prática (para o investidor) e acadêmica (para a literatura em finanças no Brasil)?
**5.3. Limitações da Pesquisa**
O que o modelo *não* considerou?
Custos de transação (corretagem, impostos) e liquidez (impacto no preço).
Otimização apenas do $\mu$ (o $\Sigma$ também poderia ser previsto).
*Overfitting* (O LSTM pode ter se ajustado demais aos dados de treino?).
**5.4. Sugestões para Trabalhos Futuros**
O que pode ser feito a seguir?
(Usar as limitações): "Incluir custos de transação..."
"Testar outras arquiteturas de *machine learning* (ex: Transformers)..."
"Aplicar modelos para prever a matriz de covariância ($\Sigma$), não apenas o $\mu$..."

### Seções Pré-Textuais (A SEREM FEITAS POR ÚLTIMO)

**RESUMO (A SER TOTALMENTE REESCRITO)**
Ignorar o Resumo de.1 Escrever um novo (máx. 250 palavras) que siga esta estrutura:
(Contexto): "A otimização de carteiras Média-Variância de Markowitz (MPT) é fundamental na gestão de investimentos, mas sofre com erros de estimação do retorno esperado ($\mu$)."
(Objetivo): "Este trabalho avalia o impacto da substituição da média histórica por modelos de previsão (ARIMA) e *machine learning* (LSTM) na estimação de $\mu$ para otimização de portfólios no mercado brasileiro."
(Metodologia): "Utilizando um *backtest* em janela deslizante de AAAA a BBBB com ativos da B3, comparou-se o desempenho ajustado ao risco (Sharpe, Sortino) de carteiras otimizadas (Max Sharpe) usando os três métodos de estimação de $\mu$."
(Resultados): "Os resultados indicam que a carteira baseada em LSTM obteve [desempenho superior/inferior/similar] ao *baseline* da média histórica, apresentando [maior/menor] Índice de Sharpe (X.X contra Y.Y) e [menor/maior] *drawdown*."
(Conclusão): "Conclui-se que o uso de modelos [não] parece ser uma alternativa viável para [mitigar o erro de estimação/melhorar a performance] no contexto da MPT no Brasil."
**Palavras-Chave:**
(Ajustar). Sugestões: Moderna Teoria das Carteiras; Markowitz; Otimização de Portfólio; Erro de Estimação; ARIMA; LSTM; *Machine Learning*.
#### Referências citadas
Entrega_08_11_25_Pedro_Reis_TMP.docx
