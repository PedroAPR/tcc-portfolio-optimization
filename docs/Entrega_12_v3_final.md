
UNIVERSIDADE FEDERAL DE GOIÁS

FACULDADE DE ADMINISTRAÇÃO, CIÊNCIAS CONTÁBEIS E CIÊNCIAS ECONÔMICAS

CURSO DE CIÊNCIAS CONTÁBEIS

PEDRO AUGUSTO PINHEIRO REIS

Moderna Teoria das Carteiras no Mercado de Ações Brasileiro:

Comparação entre Otimizadores e Inputs

Goiânia - GO

2026

Termo de Ciência e de Autorização TCCG (RI)

(Orientador anexa documento, assina e disponibiliza a assinatura para o orientando via SEI)

PEDRO AUGUSTO PINHEIRO REIS

Moderna Teoria das Carteiras no Mercado de Ações Brasileiro:

Comparação entre Otimizadores e Inputs

Trabalho de Conclusão de Curso apresentado ao Curso de Ciências Contábeis da Faculdade de Administração, Ciências Contábeis e Ciências Econômicas da Universidade Federal de Goiás como requisito parcial para a obtenção do título de Bacharel em Ciências Contábeis.

Orientador(a): Prof.(a) Dr. Moisés Ferreira da Cunha

Goiânia

2026

Ficha Catalográfica

(https://www.bc.ufg.br/p/3398-ficha-catalografica)

Ata de aprovação (assinada pela banca avaliadora via SEI)

DEDICATÓRIA

(Opcional)

Dedico este trabalho a todos os meu familiares e amigos, que me apoiaram nessa longa caminhada até a formação.

AGRADECIMENTOS

(Opcional)

EPÍGRAFE

Analisamos dados históricos em busca de padrões anômalos que não esperaríamos que ocorressem aleatoriamente.

( Jim Simons – Criador da Análise Quantitativa)

RESUMO

O presente estudo avalia o desempenho de carteiras de investimento no mercado acionário brasileiro, fundamentado na evolução da Teoria Moderna do Portfólio (MPT) para a Teoria Pós-Moderna (PMPT) e o modelo de Black-Litterman (BL). A pesquisa analisa o impacto da variação nas metodologias de estimação de retornos esperados (inputs) — utilizando média histórica e fator de momentum 12-1 para geração de visões no modelo Black-Litterman — combinadas a diferentes algoritmos de otimização: Média-Variância, Mínima Variância Global, Maximização do Índice de Sortino e Minimização do Conditional Value at Risk (CVaR). Adicionalmente, aplica-se o modelo Black-Litterman integrando visões de mercado baseadas em séries temporais e Machine Learning. O desempenho das carteiras é confrontado com os benchmarks IBOVESPA e CDI no período de janeiro de 2010 a dezembro de 2025, buscando identificar estratégias de alocação de ativos que ofereçam relações risco-retorno superiores e mais robustas às especificidades do mercado local.

Palavras-chave: Otimização de Portfólio. Black-Litterman. Machine Learning. CVaR. Mercado Brasileiro.

## ABSTRACT

This study evaluates the performance of investment portfolios in the Brazilian stock market, based on the evolution from Modern Portfolio Theory (MPT) to Post-Modern Portfolio Theory (PMPT) and the Black-Litterman (BL) model. The research analyzes the impact of variation in the methodologies for estimating expected returns (inputs) — using historical averages and momentum 12-1 factor to generate views in the Black-Litterman model — combined with different optimization algorithms: Mean-Variance, Minimum Global Variance, Sortino Ratio Maximization, and Conditional Value at Risk (CVaR) Minimization. Additionally, the Black-Litterman model is applied integrating market views based on time series and Machine Learning. The performance of the portfolios is compared to the IBOVESPA and CDI benchmarks over the period from January 2010 to December 2025, seeking to identify asset allocation strategies that offer superior risk-return ratios and are more robust to the specificities of the local market.

Keywords: Portfolio Optimization. Black-Litterman. Machine Learning. CVaR. Brazilian Market.

## LISTA DE FIGURAS (se houver)

## LISTA DE QUADROS (se houver)

## LISTA DE TABELAS (se houver)

Tabela 1 - Comparação entre Capital Market Line (CML) e Security Market Line	34

Tabela 2 - Comparação Estrutural: MPT vs. PMPT	46

Tabela 3 -  Resumo Analítico dos Indicadores de Desempenho (MPT vs. PMPT)	55

Tabela 4 - Distribuição Setorial da Amostra	79

Tabela 5 - Estatísticas Descritivas dos Log-Retornos Diários (130 ativos)	79

Tabela 6 - Tabela 4.3 — Volatilidade Média Anualizada por Ano (cross-section de 130 ativos)	80

Tabela 7 - Resultados Consolidados dos Testes Econométricos (135 ativos)	81

Tabela 8 — Desempenho da Estratégia Mínima Variância L1 (jan/2015 – dez/2025)	82

Tabela 9— Desempenho da Estratégia Máximo Sharpe L1 (jan/2015 – dez/2025)	83

Tabela 10 — Desempenho da Estratégia Black-Litterman com Momentum 12-1 (jan/2015 – dez/2025)	84

Tabela 11— Comparação Unificada das Estratégias (período out-of-sample 2015–2025)	85

Tabela 12-  Síntese Comparativa do Desempenho (jan/2015 – dez/2025)	88

Tabela 13 - Cronograma da Pesquisa	97

## LISTA DE ABREVIATURAS E SIGLAS (se houver)

# INTRODUÇÃO

A alocação de capital iniciou-se quase como uma arte, em que a intuição predominava, amadureceu com a adoção de cálculos, estatísticas e métricas bem definidas. Antes da formalização da Teoria Moderna do Portfólio (MPT), a gestão de carteiras carecia de um arcabouço unificado.

A Moderna Teoria do Portfólio (MPT), proposta por Harry Markowitz em sua publicação seminal de 1952, inaugurou a abordagem quantitativa para a seleção de ativos e a formação de carteiras eficientes. Fundamentada nos conceitos de diversificação e fronteira eficiente, a teoria busca otimizar a alocação de recursos maximizando o retorno esperado e minimizando o risco, representado pela variância dos retornos (Markowitz, 1952, 1959). Posteriormente, William Sharpe (1966) contribuiu ao propor o Índice de Sharpe, que relaciona o retorno excedente ao risco total da carteira, oferecendo uma métrica objetiva de avaliação de desempenho ajustado ao risco.

Entretanto, a aplicação prática da MPT enfrenta desafios substanciais, uma vez que assume hipóteses idealizadas — como a normalidade dos retornos e a simetria na distribuição dos riscos — que raramente se confirmam em mercados emergentes como o brasileiro (Damodaran, 2007). Adicionalmente, o modelo de otimização de média-variância é notório por sua sensibilidade extrema aos inputs (estimativas de retorno e covariância), fenômeno conhecido como "maximização de erros", que frequentemente resulta em portfólios instáveis e pouco diversificados, concentrados em soluções de canto (Michaud, 1989).

Nesse contexto, o Modelo Black-Litterman (1992) foi desenvolvido como uma evolução do modelo de Markowitz, visando mitigar tais instabilidades. Utilizando uma abordagem Bayesiana, o modelo combina o retorno de equilíbrio de mercado (o Prior, derivado do CAPM reverso) com as visões subjetivas do investidor (a Likelihood), gerando uma distribuição Posterior de retornos esperados. Essa fusão gera carteiras mais estáveis, intuitivas e diversificadas, ancoradas na racionalidade do equilíbrio de mercado (Black; Litterman, 1992).

Paralelamente, em resposta à inadequação da variância como medida de risco em distribuições não normais, surgiu a Teoria Pós-Moderna do Portfólio (PMPT) (Rom; Ferguson, 1994). Esta abordagem propõe métricas assimétricas que se alinham melhor à aversão à perda do investidor, como a semivariância, o Conditional Value at Risk (CVaR) e o Índice de Sortino, priorizando a análise do downside risk em detrimento da volatilidade total (Sortino; Van Der Meer, 1991).

Diante da evolução teórica que transcende o modelo clássico de média-variância, e considerando a complexidade do mercado acionário brasileiro, este projeto propõe a seguinte questão de pesquisa: Qual a eficácia comparativa de carteiras construídas sob as óticas da MPT, PMPT e Black-Litterman, quando submetidas a diferentes métodos de estimação de inputs (Séries Temporais e Machine Learning) no mercado brasileiro?

O objetivo geral deste trabalho é avaliar o desempenho de carteiras otimizadas, variando-se a estimação dos retornos esperados entre Média Histórica, fator de momentum 12-1. Serão testados otimizadores distintos: Média-Variância, Mínima Variância Global, Máximo Índice de Sortino, Mínimo-CVaR e a abordagem mista de Black-Litterman. O estudo abrange o período de janeiro de 2010 a dezembro de 2025, comparando os resultados com benchmarks como o IBOVESPA e o CDI, a fim de demonstrar alternativas robustas para a alocação de ativos no Brasil.

Este trabalho está estruturado da seguinte forma: o Capítulo 2 apresenta o referencial teórico, O Capítulo 3 descreve a metodologia, O Capítulo 4 analisa os resultados, O Capítulo 5 apresenta as conclusões.

# REFERENCIAL TEÓRICO

### Gênese da Gestão de Portfólios e o Paradigma Pré-Markowitz

### Introdução: A Evolução Histórica da Gestão de Investimentos

A gestão de investimentos, historicamente uma arte dominada pela intuição e pela análise fundamentalista idiossincrática, sofreu uma revolução paradigmática em meados do século XX. Antes do advento da Teoria Moderna do Portfólio (Modern Portfolio Theory - MPT), a prática de alocação de capital carecia de uma estrutura teórica unificada que quantificasse a relação entre risco e retorno de maneira sistemática. Este capítulo delineia a trajetória intelectual que transformou as finanças de uma disciplina descritiva em uma ciência normativa e quantitativa, culminando nos modelos de equilíbrio que sustentam a indústria global de gestão de ativos contemporânea.

### O Paradigma Pré-Markowitz: A Era da Seleção de Ativos

Até o início da década de 1950, a teoria de investimentos operava sob o "paradigma da seleção de ativos" (stock picking). A literatura seminal da época, epitomizada pelas obras de John Burr Williams e da dupla Benjamin Graham e David Dodd, focava quase exclusivamente na determinação do valor intrínseco de títulos individuais, tratando a construção do portfólio como uma consequência secundária da acumulação de ativos subavaliados (Williams, 2014).

John Burr Williams, em sua magnum opus de 1938, The Theory of Investment Value, introduziu o Modelo de Desconto de Dividendos (Dividend Discount Model - DDM), estabelecendo que o valor de um ativo é o valor presente de seus fluxos de caixa futuros esperados, descontados a uma taxa de juros apropriada (Williams, 2014). A fórmula de Williams,  , onde  representa os dividendos e  a taxa de desconto, proporcionou o primeiro rigor matemático para a avaliação de equities (Guerard, 2010). Contudo, a abordagem de Williams sofria de uma limitação crítica: ela assumia que o risco poderia ser virtualmente eliminado através da diversificação, sem fornecer um mecanismo matemático para quantificar como a variabilidade dos retornos de diferentes ativos interagia (Rubinstein, 2002). Williams focava na maximização do retorno esperado, acreditando que a "lei dos grandes números" protegeria o investidor que diversificasse suficientemente (Rubinstein, 2002).

Paralelamente, Benjamin Graham e David Dodd, em Security Analysis (1934), estabeleceram os princípios do Value Investing. Embora defendessem a diversificação como uma medida prudencial — sugerindo a detenção de dez a trinta papéis diferentes para mitigar o erro de análise — o conceito de risco em sua estrutura era fundamentalmente qualitativo (Boyd, Johansson, Kahn, Schiele, Schmelzer, 2024). Para Graham, risco não era volatilidade, mas sim a possibilidade de perda permanente de capital decorrente da deterioração dos fundamentos da empresa ou de pagar um preço excessivo em relação ao valor intrínseco (Guerard, 2010). A "Margem de Segurança" era a métrica de proteção, não o desvio padrão ou a covariância. Neste paradigma, o portfólio era visto como uma coleção de ativos individuais, onde cada componente era julgado por seus próprios méritos, isolado do contexto agregado da carteira(Guerard, 2010).

### A Transição para a Análise Quantitativa

A ruptura com o paradigma da seleção individual de ativos não ocorreu abruptamente, mas foi precedida por desenvolvimentos teóricos que começaram a questionar a suficiência da maximização do valor presente. Economistas como Hicks (1939) e Marschak (1938) já exploravam as preferências sobre momentos estatísticos, e o matemático italiano Bruno de Finetti, em 1940, havia formulado um problema de alocação média-variância no contexto de resseguros, embora seu trabalho tenha permanecido desconhecido no mundo anglófono por décadas (Boyd, Johansson, Kahn, Schiele, Schmelzer, 2024).

O momento decisivo, contudo, surgiu da insatisfação intelectual de Harry Markowitz com a teoria vigente. Enquanto lia a obra de Williams na biblioteca da Universidade de Chicago, Markowitz teve um insight que desmantelaria a lógica da maximização pura do retorno (markowitz, 1959). Ele percebeu que, se a regra de Williams fosse seguida estritamente em um mundo de incerteza, um investidor racional deveria alocar 100% de seu capital no único ativo com o maior retorno esperado descontado (Williams, 2014). Se dois ativos tivessem o mesmo retorno máximo, o investidor seria indiferente entre eles, mas a teoria não oferecia nenhuma razão intrínseca para manter ambos (Markowitz, 1959).

Markowitz identificou que a prática observada e intuitivamente racional da diversificação — "não colocar todos os ovos na mesma cesta" — era inconsistente com a teoria de maximização de valor presente de Williams (Markowitz, 1958). Para racionalizar a diversificação, era necessário introduzir uma segunda dimensão na função objetivo do investidor: o risco. A diversificação só faz sentido se o investidor estiver disposto a sacrificar uma parcela do retorno potencial para reduzir a incerteza do resultado final. Essa percepção marcou a transição da análise de títulos (Security Analysis) para a análise de portfólios (Portfolio Analysis), onde a unidade de análise deixa de ser a firma individual e passa a ser a carteira agregada (Markowitz, 1958).

## A Revolução de Markowitz: O Modelo Média-Variância

A formalização matemática dessa nova perspectiva ocorreu com a publicação do artigo "Portfolio Selection" no Journal of Finance em 1952, expandido posteriormente na monografia Portfolio Selection: Efficient Diversification of Investments (1959) (Markowitz, 1959). A "Modern Portfolio Theory" (MPT) de Markowitz não apenas descreveu como os investidores agem, mas prescreveu como deveriam agir, fundamentando a decisão de investimento na interação estocástica entre ativos (Markowitz, 1959).

### A Rejeição da Maximização Pura do Retorno

A premissa fundadora da MPT é que os investidores são, simultaneamente, maximizadores de retorno e avessos ao risco (Markowitz, 1959). Markowitz rejeitou a hipótese de que os investidores consideram apenas o valor esperado (média) dos retornos futuros. Se os investidores focassem apenas na média, o conceito de um portfólio diversificado seria teoricamente injustificável, pois a diversificação quase sempre reduz o retorno esperado em comparação com a concentração no ativo de melhor desempenho (Markowitz, 1952).

Portanto, a função de utilidade do investidor deve depender de dois parâmetros:

- Retorno Esperado (µ): O valor médio ponderado das probabilidades dos retornos futuros.

- Risco (σ): A dispersão ou incerteza desses retornos em torno da média.

A MPT postula que, para qualquer nível dado de risco, o investidor prefere o maior retorno possível; e para qualquer nível dado de retorno, prefere o menor risco possível. Essa estrutura de preferências cria um trade-off inevitável, substituindo a busca pelo "melhor ativo" pela construção do "melhor portfólio" (Markowitz, 1952).

### O Conceito de Risco como Variância: Uma Escolha Pragmática

Em sua obra de 1959, Markowitz dedicou um capítulo para discutir uma medida alternativa de risco: a semivariância (Estrada, 2007). A semivariância mensura apenas a dispersão dos retornos que caem abaixo de um determinado alvo (como a média ou zero), ignorando a volatilidade "positiva" (ganhos acima do esperado) " (Markowitz, 1959). Markowitz reconheceu explicitamente a superioridade teórica desta medida, afirmando que "a semivariância parece mais plausível do que a variância como uma medida de risco, uma vez que se preocupa apenas com desvios adversos" (Markowitz, 1990). Investidores racionais não temem ganhos inesperados; eles temem perdas.

No entanto, Markowitz optou pela variância baseada em critérios de "custo, conveniência e familiaridade" (ESTRADA, 2007).

- Custo Computacional: Na era dos mainframes primitivos e cartões perfurados, o custo de computação era uma barreira formidável. A otimização baseada na variância envolvia álgebra linear padrão e inversão de matrizes covariância, operações para as quais existiam algoritmos eficientes (como o Critical Line Algorithm desenvolvido pelo próprio Markowitz) (Markowitz, Starer, Fram, Gerber, 2019 ). A semivariância, por outro lado, exigia o dobro de dados de entrada (matrizes de semicovariância) e resultava em problemas de otimização mais complexos, onde a matriz de covariância se tornava endógena aos pesos do portfólio (Estrada, 2007).

- Convenência Analítica: Se os retornos dos ativos seguirem uma distribuição normal (simétrica), a média e a variância são estatísticas suficientes para descrever toda a distribuição. Nesse caso específico, minimizar a variância é matematicamente equivalente a minimizar a semivariância (Estrada, 2007). Markowitz apostou na aproximação normal como uma simplificação aceitável para tornar a teoria operacionalizável.

Apesar de Markowitz ter sugerido que a semivariância seria preferível com o aumento do poder computacional, a variância entrincheirou-se como o padrão da indústria, moldando décadas de teoria financeira, desde o Índice de Sharpe até o modelo Black-Scholes (Estrada, 2007).

## Risco, Retorno e Covariância: A Matemática da Diversificação

A contribuição técnica mais duradoura de Markowitz foi a formulação estatística do risco do portfólio, demonstrando que o risco de um todo não é meramente a soma dos riscos das partes.

### Retorno Esperado do Portfólio

O retorno esperado de um portfólio  é uma função linear simples dos ativos que o compõem. É a média ponderada dos retornos esperados individuais , onde os pesos  representam a fração do capital alocada em cada ativo:

Esta linearidade implica que a diversificação não altera o potencial de retorno médio do portfólio; ela apenas dilui os retornos extremos dos ativos individuais.5

### Variância e Covariância

Diferentemente do retorno, a variância do portfólio   não é linear. Ela depende crucialmente das covariâncias entre os ativos, capturando como os preços dos ativos se movem uns em relação aos outros. A fórmula da variância para um portfólio de  ativos é:

Ou, em notação matricial,   , onde  é a matriz de covariância (Kim, Boyd, 2007).

Markowitz demonstrou a "Lei da Covariância Média": à medida que o número de ativos  em um portfólio igualmente ponderado aumenta, a contribuição das variâncias individuais  para o risco total tende a zero, enquanto a contribuição das covariâncias  domina (Markowitz, 1999). No limite, o risco de um portfólio diversificado é determinado quase inteiramente pela covariância média entre os ativos, e não pela volatilidade individual de cada um (Markowitz, 1959).

### O Papel da Correlação

A covariância  é o produto da correlação e dos desvios padrão . O coeficiente de correlação, variando entre -1 e +1, é o "motor" da diversificação:

- Correlação Perfeita (+1): O risco do portfólio é a média ponderada dos riscos individuais. Não há benefício de diversificação.

- Correlação Inferior a 1: O risco do portfólio será sempre menor que a média ponderada dos riscos individuais. A volatilidade idiossincrática é cancelada(Hebner, 2022) .

- Correlação Negativa (-1): Permite, teoricamente, a construção de um portfólio com variância zero (hedge perfeito).

A intuição de Markowitz foi quantificar que, ao combinar ativos com correlação imperfeita, o investidor reduz a exposição a riscos específicos (choques que afetam apenas uma empresa), mantendo apenas a exposição aos riscos comuns que afetam todo o sistema (Markowitz, 1959).

## A Fronteira Eficiente: Otimização e Geometria

A aplicação dos princípios de média-variância a um universo de ativos resulta na construção da Fronteira Eficiente, o conjunto de todos os portfólios ótimos que dominam as demais alternativas.

### Derivação e Definição

A Fronteira Eficiente é o lugar geométrico no espaço risco-retorno que representa os portfólios que oferecem o retorno máximo para um dado nível de risco (ou risco mínimo para um dado retorno) (Markowitz, 1959). Ela é obtida resolvendo um problema de otimização quadrática convexa (Gundersen, 2022).

A forma geométrica exata desta fronteira depende criticamente das restrições impostas aos pesos :

- Sem Restrições a Vendas a Descoberto (Unconstrained/Short Selling Allowed): Se o investidor pode vender a descoberto (assumir pesos negativos) ilimitadamente, a fronteira eficiente é uma hipérbole perfeita e suave no espaço média-desvio padrão (Gundersen, 2022). O ramo superior desta hipérbole (acima do vértice) é a fronteira eficiente propriamente dita.

- Com Restrições a Vendas a Descoberto (No Short Selling Constraint): Quando impomos a restrição de não-negatividade , a fronteira deixa de ser uma hipérbole única e torna-se uma curva convexa composta por uma série de segmentos de hipérbole conectados (piecewise hyperbolic segments) (Gundersen, 2022).

  - Mecanismo: A transição de um segmento hiperbólico para outro ocorre nos "corner portfolios" (portfólios de canto). À medida que nos movemos ao longo da fronteira (aumentando o retorno esperado), a composição do portfólio muda. Quando o peso de um ativo atinge zero (sai do portfólio) ou quando um novo ativo entra no portfólio (peso torna-se positivo), a equação algébrica que descreve a curva muda, criando um "ponto de solda" entre dois arcos hiperbólicos distintos (Qi, 2019).

  - Implicação: A fronteira com restrições é finita, começando no portfólio de mínima variância global e terminando no ativo individual de maior retorno (e risco), ao contrário da fronteira sem restrições que se estende ao infinito através da alavancagem de posições vendidas (Gundersen, 2022).

O algoritmo desenvolvido por Markowitz para traçar essa fronteira complexa com restrições de desigualdade é o Critical Line Algorithm (CLA), um método de otimização quadrática paramétrica que precede e inspira os modernos solvers de programação quadrática (Markowitz, Starer, Fram, Gerber, 2019).

### O Portfólio de Mínima Variância Global

O vértice da fronteira (seja ela hiperbólica ou segmentada) é o Portfólio de Mínima Variância Global (GMV). Este é o único ponto na curva onde o risco é minimizado em termos absolutos, sem consideração pelo retorno (Kim, Boyd, 2007). Em teoria, nenhum investidor racional avesso ao risco escolheria um portfólio localizado na parte "inferior" da fronteira (abaixo do GMV), pois para cada ponto nessa região existe um portfólio na parte superior com o mesmo risco, mas com retorno estritamente maior (dominância média-variância) (Gundersen, 2022).

### O Ativo Livre de Risco e o Teorema da Separação

A introdução de um ativo livre de risco (risk-free asset) expande o conjunto de oportunidades do investidor além da fronteira de ativos de risco, alterando a geometria da escolha ótima e levando ao Teorema da Separação de Tobin.

### O Ativo Livre de Risco

Um ativo livre de risco é definido idealmente como um investimento com variância zero  e, consequentemente, covariância zero com todos os ativos de risco .34 Na prática financeira, títulos governamentais de curto prazo, como as Treasury Bills dos EUA, são utilizados como proxies, assumindo-se ausência de risco de crédito e risco de reinvestimento negligenciável para o horizonte de um período (Rohatgi, 2011). A inclusão deste ativo permite duas novas operações financeiras fundamentais:

- Empréstimo Livre de Risco (Lending): O investidor pode aplicar parte de sua riqueza no ativo livre de risco, reduzindo a exposição total ao risco do mercado.

- Tomada de Empréstimo Livre de Risco (Borrowing/Leverage): O investidor pode tomar dinheiro emprestado à taxa livre de risco para alavancar sua posição nos ativos de risco.37

### O Teorema da Separação de Tobin

James Tobin, em seu artigo seminal de 1958 Liquidity Preference as Behavior Towards Risk, formalizou o impacto do ativo livre de risco na teoria da escolha de portfólio.39 Tobin demonstrou que, na presença de um ativo livre de risco, o processo de decisão de investimento pode ser decomposto em duas etapas distintas e independentes — um resultado conhecido como o Teorema da Separação (ou Two-Fund Separation Theorem) (Buiter, 2003).

- Etapa 1: A Decisão Técnica (Seleção do Portfólio Ótimo de Risco). O investidor deve primeiro identificar o portfólio de ativos de risco que maximiza o retorno por unidade de risco. Geometricamente, este é o Portfólio de Tangência (Tangency Portfolio), o ponto onde uma linha reta partindo da taxa livre de risco   tangencia a fronteira eficiente hiperbólica dos ativos de risco (Gundersen, 2022). A composição deste portfólio é puramente técnica e objetiva, dependendo apenas das estimativas de médias, variâncias e covariâncias; ela é independente das preferências de risco do investidor individual.37

- Etapa 2: A Decisão Pessoal (Alocação de Capital). Uma vez identificado o Portfólio de Tangência, o investidor decide como alocar sua riqueza total entre este portfólio e o ativo livre de risco. Esta decisão depende inteiramente da função de utilidade (aversão ao risco) do indivíduo.37

### A Reta do Mercado de Capitais (Capital Market Line - CML)

A combinação linear do ativo livre de risco com o Portfólio de Tangência gera a Reta do Mercado de Capitais (Capital Market Line - CML). A CML torna-se a nova fronteira eficiente, pois domina qualquer portfólio situado na fronteira original de ativos de risco (a hipérbole fica inteiramente abaixo da reta CML, exceto no ponto de tangência).37

O posicionamento do investidor ao longo da CML é determinado pelo mecanismo de alavancagem:

- Investidores Conservadores (Lending Portfolios): Localizam-se à esquerda do ponto de tangência . Eles investem uma fração positiva de sua riqueza no ativo livre de risco e o restante no portfólio . O risco total do portfólio é menor que o risco de .37

- Investidores Agressivos (Borrowing Portfolios): Localizam-se à direita do ponto de tangência . Eles tomam empréstimos à taxa  para investir mais de 100% de seu capital próprio no portfólio  ampliando tanto o retorno esperado quanto a volatilidade.37

A equação que descreve a CML é:

Onde a inclinação (slope) da reta, , representa o "preço de mercado do risco" — o retorno adicional que o mercado exige para aceitar uma unidade adicional de desvio padrão.44

    - Considerações sobre Taxas de Empréstimo Diferenciadas

Na realidade, investidores raramente conseguem tomar empréstimos à mesma taxa livre de risco que o governo . Nesse cenário, a CML deixa de ser uma linha reta única e torna-se uma fronteira "quebrada" ou côncava: um segmento linear parte de  até um ponto de tangência, segue-se um segmento curvo da fronteira eficiente original (onde o investidor não empresta nem toma emprestado), e então um novo segmento linear parte de outro ponto de tangência com inclinação menor, baseada na taxa de empréstimo mais alta.41

## Avaliação de Desempenho: O Índice de Sharpe

A geometria da CML forneceu a base direta para uma das métricas mais onipresentes na avaliação de investimentos: o Índice de Sharpe. Introduzido por William Sharpe em 1966 como "Reward-to-Variability Ratio", o índice operacionaliza o conceito de eficiência média-variância.49

### Definição e Interpretação

O Índice de Sharpe  quantifica o excesso de retorno por unidade de risco total. Matematicamente:

Geometricamente, o Índice de Sharpe de um portfólio é a inclinação da linha que conecta a taxa livre de risco a esse portfólio no gráfico média-desvio padrão (Gundersen, 2022). Quanto maior a inclinação, melhor o desempenho ajustado ao risco.

### Importância e Aplicação

A maximização do Índice de Sharpe é equivalente a encontrar o Portfólio de Tangência na MPT. Em um mercado em equilíbrio, o portfólio de mercado  deve ser aquele com o maior Índice de Sharpe possível (Guidolin, 2017). A métrica permite comparar fundos e estratégias heterogêneas, nivelando o campo de jogo ao penalizar a volatilidade. No entanto, o índice herda as limitações da variância: se os retornos não forem normais (ex: fundos de hedge com estratégias de opções), o Índice de Sharpe pode ser enganoso, penalizando a volatilidade positiva ou subestimando riscos de cauda, o que levou ao desenvolvimento de métricas alternativas como o Índice de Sortino (baseado na semivariância/downside deviation) (Dubra, Maccheroni, 2004).

## O Modelo de Precificação de Ativos de Capital (CAPM)

Enquanto a MPT de Markowitz é normativa (diz ao investidor como construir um portfólio), o Capital Asset Pricing Model (CAPM) é positivo (explica como os preços dos ativos são determinados se todos seguirem a MPT).

### Origem e Desenvolvedores

O CAPM foi desenvolvido independentemente na primeira metade da década de 1960 por William Sharpe (1964), John Lintner (1965), Jan Mossin (1966) e Jack Treynor (1961/1962) (Fama, French, 2004). A unificação dessas teorias rendeu a Sharpe, Markowitz e Merton Miller o Prêmio Nobel de Economia em 1990 (garvin, 2013). A intuição central é que, se todos os investidores são racionais, possuem expectativas homogêneas e otimizam seus portfólios segundo a média-variância (usando o Teorema da Separação de Tobin), então todos demandarão o mesmo portfólio de ativos de risco: o Portfólio de Mercado . Para que o mercado "limpe" (oferta iguale demanda), os preços dos ativos devem se ajustar até que o portfólio de tangência seja, de fato, o portfólio de mercado ponderado por valor (Fama, French, 2004).

### Decomposição do Risco: Sistemático vs. Não Sistemático

O CAPM introduz uma distinção fundamental na natureza do risco, decompondo a variância total de um ativo  em dois componentes (Ross, Westerfield, Jordan, 2010):

- Risco Sistemático (Risco de Mercado): É a parcela da volatilidade do ativo que está correlacionada com os movimentos do mercado como um todo. Origina-se de fatores macroeconômicos inelutáveis — inflação, juros, ciclos econômicos, guerras — que afetam todas as empresas simultaneamente. Este risco não pode ser eliminado pela diversificação.

- Risco Não Sistemático (Idiossincrático/Específico): É a parcela da volatilidade exclusiva da empresa ou setor (ex: sucesso de um novo produto, greve na fábrica, fraude contábil). Como esses eventos são estatisticamente independentes entre empresas, em um portfólio amplo eles tendem a se cancelar mutuamente (lei dos grandes números).

A conclusão revolucionária do CAPM é que o mercado não remunera o risco não sistemático. Como ele pode ser eliminado gratuitamente através da diversificação, os investidores não devem esperar nenhum prêmio de retorno por assumi-lo. O único risco que justifica um retorno esperado acima da taxa livre de risco é o risco sistemático (Ross, Westerfield, Jordan, 2010).

### O Coeficiente Beta e a Reta do Mercado de Títulos (SML)

Para mensurar o risco sistemático, o CAPM utiliza o coeficiente Beta . O Beta é uma medida padronizada da covariância do ativo com o mercado, definida como:

- Se β>1: O ativo tem um risco sistemático superior ao mercado (mais volátil).

- Se β<1: O ativo tem um risco sistemático inferior ao mercado (menos volátil).

Um ativo com  move-se, em média, na mesma proporção que o mercado. Um ativo com  amplifica os movimentos do mercado (mais risco sistemático), enquanto  os atenua.

### A Reta do Mercado de Títulos (SML)

A equação do CAPM define uma relação linear entre o retorno esperado e o Beta, e essa relação é representada graficamente pela Security Market Line (SML), ou Linha do Mercado de Títulos (LMT). O CAPM estabelece que o retorno esperado do ativo () é dado pela equação da SML:

A SML é crucial porque todo ativo individual, ou portfólio eficiente e não eficiente, deve se situar sobre ela em um mercado de equilíbrio

    - Diferença entre CML e SML:

A distinção fundamental entre a CML e a SML reside na medida de risco utilizada.

- CML (Capital Market Line): É a fronteira eficiente que relaciona o retorno esperado com o Risco Total (medido pelo desvio-padrão, σ). O Índice de Sharpe avalia o prêmio de risco por unidade de risco total (medido ao longo da CML).

- SML (Security Market Line): Relaciona o retorno esperado com o Risco Sistemático (medido pelo Beta, β). O CAPM demonstra que os investidores são compensados apenas pelo risco sistemático, pois o risco não sistemático pode ser eliminado pela diversificação.

*Tabela 1 - Comparação entre Capital Market Line (CML) e Security Market Line*

| Característica | Capital Market Line (CML) | Security Market Line (SML) |
| --- | --- | --- |
| Medida de Risco | Desvio Padrão Total | Beta Sistemático |
| Aplicação | Apenas Portfólios Eficientes | Qualquer Ativo Individual ou Portfólio |
| Definição de Risco | Risco Total (Sistemático + Idiossincrático) | Apenas Risco Sistemático (Covariância com Mercado) |
| Ponto de Intercepto | Taxa Livre de Risco | Taxa Livre de Risco |
| Inclinação (Slope) | Índice de Sharpe do Mercado | Prêmio de Risco de Mercado |
| Fundamentação | Teorema da Separação de Tobin | Modelo de Equilíbrio de Mercado (CAPM) |

Fonte: Elaboração própria com base em (Boasson, Boasson, Zhou).

  - Pressupostos, Críticas e Limitações Teóricas

A elegância matemática da MPT e do CAPM repousa sobre um conjunto de axiomas sobre o comportamento humano e a estrutura dos mercados. A validade desses modelos depende, portanto, da robustez de seus pressupostos.

    - Pressupostos Fundamentais: A Racionalidade VNM

A teoria assume que os investidores são agentes perfeitamente racionais que tomam decisões sob incerteza maximizando a Utilidade Esperada, conforme axiomatizado por John von Neumann e Oskar Morgenstern (VNM) em Theory of Games and Economic Behavior (1944).63 Para que uma função de utilidade esperada exista e represente as preferências do investidor, cinco axiomas fundamentais devem ser satisfeitos 63:

- Completude (Completeness): O investidor tem preferências bem definidas. Para quaisquer duas loterias (investimentos) A e B, ele pode afirmar se prefere A a B ($A \succ B$), B a A ($B \succ A$) ou se é indiferente ($A \sim B$). A indecisão não é permitida.63

- Transitividade (Transitivity): As preferências são consistentes. Se $A \succ B$ e $B \succ C$, então logicamente $A \succ C$. A violação deste axioma implicaria comportamento cíclico e irracional ("money pump").49

- Continuidade (Continuity): Também conhecido como axioma de Arquimedes. Se $A \succ B \succ C$, existe uma probabilidade $p$ tal que o investidor é indiferente entre receber B com certeza ou uma loteria que paga A com probabilidade $p$ e C com probabilidade $1-p$. Isso impede que qualquer resultado seja infinitamente desejável ou indesejável (como o paraíso ou a morte) a ponto de ignorar probabilidades.49

- Independência (Independence): A preferência entre duas opções não deve ser alterada pela introdução de uma terceira opção comum a ambas. Se $A \succ B$, então uma mistura de A com C deve ser preferida à mesma mistura de B com C. Este é o axioma mais controverso e frequentemente violado em testes empíricos (ex: Paradoxo de Allais).49

- Dominância (Dominance/Monotonicity): Se uma opção A oferece resultados melhores que B em pelo menos um estado da natureza e resultados iguais ou melhores em todos os outros estados, então A deve ser estritamente preferida a B. Este axioma encapsula a ideia racional de que "mais é melhor que menos" e violações a ele (como escolher uma opção dominada estocasticamente) são consideradas erros graves de decisão.65

Tabela 2: Axiomas da Teoria da Utilidade Esperada (VNM)

| Axioma | Definição Simplificada | Implicação Financeira |
| --- | --- | --- |
| Completude | Capacidade de ranquear qualquer par de ativos. | O mercado pode precificar todos os ativos. |
| Transitividade | Consistência lógica ($A>B, B>C \Rightarrow A>C$). | Evita arbitragem cíclica irracional. |
| Continuidade | Existência de "pontos de indiferença" probabilísticos. | Permite modelar o trade-off risco-retorno de forma contínua. |
| Independência | Preferências não mudam com opções irrelevantes. | A diversificação é consistente independentemente do resto da carteira. |
| Dominância | Preferência por "mais riqueza" e "menos risco". | Fundamenta a fronteira eficiente (ninguém escolhe portfólios dominados). |

Fonte: Elaboração própria baseada em.65

    - Limitações e a Realidade dos Mercados

As críticas à MPT e ao CAPM surgem da desconexão entre esses axiomas ideais e a realidade empírica dos mercados financeiros.

- Distribuições Não-Normais (Caudas Gordas): A MPT assume que os retornos seguem uma distribuição Normal (Gaussiana), o que justifica o uso da variância como medida completa de risco. Contudo, estudos seminais de Benoit Mandelbrot (1963) e Eugene Fama (1965) demonstraram que os preços de ativos exibem "caudas gordas" (fat tails) e leptocurtose excessiva.76 Na realidade, eventos extremos (como crashes de mercado de 10 ou 20 desvios padrão) ocorrem com frequência muito maior do que a prevista pela curva normal. O uso da variância subestima drasticamente o risco real de eventos catastróficos ("Cisnes Negros"), tornando a MPT perigosa em momentos de crise.78

- Limitações da Variância: Como discutido na seção 2.2, a variância penaliza igualmente a volatilidade para cima (lucro) e para baixo (perda). Investidores reais, no entanto, exibem aversão à perda, não à volatilidade per se. A semivariância ou métricas de downside risk seriam descritores mais precisos da utilidade do investidor, mas a inércia da tradição MPT mantém a variância como padrão.12

- Violações da Racionalidade: A Economia Comportamental (Kahneman e Tversky) documentou sistemáticas violações dos axiomas VNM. O "efeito certeza" e a "aversão à perda" (Teoria da Perspectiva) mostram que investidores reais frequentemente violam os axiomas de Independência e Dominância, comportando-se de maneira inconsistente com a maximização da utilidade esperada.80

Apesar dessas falhas descritivas, a estrutura criada por Markowitz, Tobin e Sharpe permanece a lingua franca das finanças. Conceitos como diversificação, fronteira eficiente, Beta e Índice de Sharpe fornecem as ferramentas heurísticas indispensáveis para a alocação de ativos institucional, servindo como um modelo normativo de como o mercado deveria funcionar sob condições ideais, mesmo que a realidade frequentemente divirja do modelo.

  - A Teoria Pós-Moderna do Portfólio (PMPT) e a Gestão de Risco Assimétrica

    - Introdução: A Evolução Paradigmática e a Necessidade Histórica da PMPT

A história das finanças quantitativas é, em grande medida, a história da busca por uma métrica de risco que reflita fidedignamente a experiência humana de perda e incerteza. A Moderna Teoria do Portfólio (MPT), introduzida pelo trabalho seminal de Harry Markowitz em 1952, Portfolio Selection, estabeleceu o alicerce sobre o qual a gestão moderna de investimentos foi construída, formalizando a intuição da diversificação através da análise de média-variância. No entanto, a hegemonia da MPT, embora duradoura, fundamentou-se em simplificações matemáticas — notadamente a distribuição normal dos retornos e a variância como proxy de risco — que se mostraram cada vez mais dissonantes da realidade empírica dos mercados globais e da psicologia do investidor.

O surgimento da Teoria Pós-Moderna do Portfólio (PMPT) não deve ser interpretado como uma refutação do trabalho de Markowitz, mas sim como a sua evolução necessária e, ironicamente, um retorno às intenções originais do próprio autor. A PMPT emergiu formalmente no início da década de 1990, impulsionada pelo aumento exponencial da capacidade computacional, que permitiu aos pesquisadores e praticantes modelar a assimetria inerente aos retornos financeiros. Enquanto a MPT opera sob a suposição de simetria, tratando ganhos e perdas de igual magnitude como eventos de risco equivalentes, a PMPT reconhece a assimetria fundamental da preferência do investidor: a aversão à perda (downside) em detrimento da mera aversão à volatilidade.

Este capítulo dedica-se a uma exegese profunda da PMPT, explorando suas raízes históricas, sua fundamentação matemática nos Momentos Parciais Inferiores (Lower Partial Moments - LPM), e a superioridade de suas métricas de risco — como a Semivariância, o Expected Shortfall (CVaR) e os índices de Sortino e Omega — em comparação com os análogos da MPT. A análise demonstrará que a PMPT oferece um arcabouço mais robusto para a construção de portfólios em um mundo caracterizado por distribuições de cauda gorda (fat tails), cisnes negros e comportamento irracional dos agentes.

    - O "Esquecimento Tecnológico" e as Origens em Markowitz (1959)

É um equívoco comum na literatura financeira atribuir a invenção do foco no downside risk exclusivamente aos teóricos da década de 1990. Uma análise historiográfica rigorosa revela que Harry Markowitz, em sua monografia de 1959, Portfolio Selection: Efficient Diversification of Investments, dedicou um capítulo inteiro à semivariância. Markowitz postulou explicitamente que a semivariância — a variância calculada apenas sobre os retornos que caem abaixo da média ou de um alvo — produzia portfólios "intuitivamente melhores" do que aqueles baseados na variância total, pois os investidores não percebem a volatilidade positiva (ganhos acima da média) como risco, mas sim como oportunidade.

A decisão de Markowitz de fundamentar a MPT na variância, e não na semivariância, foi uma concessão pragmática imposta pelas restrições tecnológicas da época. Na década de 1950, o custo computacional para calcular a covariância de downside para um portfólio diversificado era proibitivo. A variância, com suas propriedades algébricas elegantes e simétricas, permitia soluções analíticas fechadas que podiam ser resolvidas com os recursos limitados disponíveis.

Consequentemente, a indústria financeira passou as três décadas seguintes otimizando portfólios com base em uma medida de risco (desvio padrão) que o próprio criador da teoria considerava uma segunda melhor opção. Foi somente com o advento dos microcomputadores de alta performance nas décadas de 1980 e 1990 que a barreira computacional foi superada, permitindo o renascimento da semivariância sob a égide da PMPT.

    - A Consolidação da PMPT: Rom, Ferguson e o Instituto de Pesquisa de Pensões

A formalização do termo "Teoria Pós-Moderna do Portfólio" é creditada aos desenvolvedores de software Brian M. Rom e Kathleen Ferguson, que publicaram trabalhos seminais em 1993 e 1994 no The Journal of Investing. Rom e Ferguson identificaram falhas críticas nos softwares de otimização baseados na MPT e propuseram uma nova estrutura que incorporava a assimetria das distribuições de retorno.

Paralelamente, o suporte acadêmico para a PMPT foi solidificado pelo Pension Research Institute (PRI) na Universidade Estadual de São Francisco. Pesquisadores como Dr. Frank Sortino e Dr. Hal Forsey, trabalhando com base nos teoremas de Bawa (1975) e Fishburn (1977), desenvolveram algoritmos práticos para calcular o risco de downside e a distribuição log-normal de três parâmetros, que se ajustava melhor aos dados de mercado do que a distribuição normal da MPT. O trabalho de Sortino, em particular, foi crucial para traduzir a teoria complexa dos momentos parciais em ferramentas aplicáveis, culminando na criação do Índice de Sortino, que se tornou o padrão da análise de desempenho ajustada ao risco de downside.

    - O Fenômeno da "Maximização de Erros" e a Instabilidade das Soluções

A crítica mais devastadora e pragmaticamente relevante à implementação institucional da MPT foi articulada por Richard Michaud (1989), que cunhou o termo "maximizador de erros" (error maximizer) para descrever os otimizadores de média-variância. A intuição subjacente a esta crítica é estatisticamente profunda e deve ser o ponto de partida para qualquer discussão sobre o modelo Black-Litterman. Os algoritmos de otimização quadrática são desenhados para explorar as extremidades do conjunto de oportunidades de investimento. Eles buscam, matematicamente, os ativos que oferecem as maiores razões de retorno marginal por unidade de risco marginal.

No entanto, em finanças, o vetor de retornos esperados  é uma variável estocástica não observável, que deve ser estimada a partir de dados históricos ou modelos preditivos. Essas estimativas são intrinsecamente ruidosas e instáveis. Quando um ativo apresenta uma estimativa de retorno excepcionalmente alta, é estatisticamente provável que essa estimativa contenha um componente significativo de erro positivo (viés de otimismo ou ruído amostral). O otimizador de Markowitz, cego à incerteza epistêmica da estimativa, trata esse valor como uma verdade determinística e aloca o máximo capital possível nesse ativo. Inversamente, ativos com erros de estimação negativos são penalizados e excluídos da carteira.

O resultado prático, frequentemente observado em backtests no mercado brasileiro, é a construção de "Soluções de Canto" (Corner Solutions): portfólios binários, concentrados em poucos ativos, que contradizem o próprio princípio da diversificação que a teoria pretendia promover. Em um exercício de simulação, tais carteiras frequentemente apresentam desempenho fora da amostra (out-of-sample) inferior a estratégias ingênuas de equiponderação , pois o otimizador alavancou os erros de previsão em vez de capturar o prêmio de risco verdadeiro. Esta instabilidade — onde pequenas alterações nos inputs (ex: 0,1% na média estimada de uma blue chip como a Petrobras) geram mudanças drásticas nos pesos (ex: 0% para 40% de alocação) — torna a MPT pura inutilizável para a gestão profissional de grandes volumes de capital, onde os custos de transação e a coerência da estratégia são imperativos.

    - A Limitação da Utilidade Quadrática e a Cegueira à Assimetria

A segunda falha estrutural da MPT, que justifica a adoção da PMPT neste estudo, reside na sua função de utilidade implícita. Ao adotar a variância  como a única medida de risco, Markowitz assumiu implicitamente que a desutilidade do investidor é uma função quadrática da riqueza. Isso implica simetria de preferências: um investidor "Markowitziano" sente a mesma dor ao obter um retorno 10% acima da média que sente ao obter um retorno 10% abaixo dela, pois ambos os eventos aumentam a dispersão (risco) do portfólio.

Esta premissa é violentamente rejeitada pelas evidências da Economia Comportamental e pela realidade observável dos investidores na B3. A Teoria da Perspectiva (Prospect Theory), desenvolvida por Kahneman e Tversky, demonstrou que os seres humanos exibem aversão à perda (loss aversion) e não aversão à volatilidade per se. A dor da perda é psicologicamente duas vezes mais intensa que o prazer do ganho equivalente. Além disso, os mercados financeiros exibem assimetria estatística (skewness) e curtose excessiva (fat tails), fenômenos que a distribuição normal da MPT falha em capturar.

No contexto brasileiro, a análise descritiva dos dados frequentemente revela ativos com curtose extremamente elevada (leptocurtose). Em regimes de crise, as correlações entre ativos tendem a convergir para 1, eliminando os benefícios da diversificação justamente quando eles são mais necessários — um evento que os modelos baseados em covariância linear subestimam drasticamente. Portanto, a insistência na MPT pura não é apenas uma escolha metodológica, mas um erro de especificação do modelo de risco.

Diante desse quadro de insuficiência teórica, a evolução das finanças bifurcou-se em duas direções complementares que este trabalho busca integrar: o aprimoramento da estimativa de retornos através da inferência Bayesiana (Modelo Black-Litterman) e o aprimoramento da medição de risco através do reconhecimento da assimetria (Teoria Pós-Moderna).

    - A Insuficiência da Variância e a Gênese da PMPT

Embora a Teoria Moderna do Portfólio (MPT), estabelecida por Markowitz (1952), tenha revolucionado as finanças ao quantificar a diversificação, sua dependência da variância como única medida de risco impõe limitações severas em mercados reais. A MPT assume implicitamente que os retornos dos ativos seguem uma distribuição normal (Gaussiana) e que a função de utilidade do investidor é quadrática. Contudo, evidências empíricas robustas demonstram que os retornos financeiros, especialmente em mercados emergentes como o brasileiro, apresentam distribuições leptocúrticas (caudas pesadas) e assimetria negativa

Neste contexto, a variância falha por ser uma medida simétrica: ela penaliza os desvios positivos (ganhos acima da média) com a mesma severidade que os desvios negativos (perdas) (Nawrocki, 1999). A Teoria Pós-Moderna do Portfólio (PMPT) surge, portanto, como uma evolução necessária, fundamentada na premissa de que o risco deve ser tratado como a possibilidade de não atingir um retorno mínimo aceitável (Target Minimum Return), focando exclusivamente no downside risk.

A formalização da PMPT é creditada a Rom e Ferguson (1993, 1994), que identificaram falhas críticas nos softwares de otimização baseados na MPT e propuseram uma estrutura que incorpora a assimetria das distribuições. Paralelamente, o Pension Research Institute, através de pesquisadores como Frank Sortino, operacionalizou a teoria dos Momentos Parciais Inferiores (LPM - Lower Partial Moments), desenvolvendo métricas como o Índice de Sortino, que ajusta o retorno pelo risco de downside em vez do desvio padrão total.

    - Métricas de Risco: Do VaR às Medidas Coerentes

Para operacionalizar a PMPT em modelos de otimização, é necessário definir métricas que capturem o risco de cauda. O Value at Risk (VaR), popularizado na década de 1990, tornou-se um padrão regulatório. O VaR estima a perda máxima esperada para um determinado nível de confiança e horizonte de tempo. No entanto, o VaR possui limitações teóricas graves para a otimização de portfólios: ele não é uma medida subaditiva, o que significa que, em certas condições, o VaR de uma carteira diversificada pode ser maior que a soma dos VaRs individuais dos ativos, violando o princípio da diversificação.

Em resposta, Artzner et al. (1999) estabeleceram os axiomas que definem uma Medida de Risco Coerente: monotonicidade, subaditividade, homogeneidade positiva e invariância à translação. Com base nesses axiomas, o Conditional Value at Risk (CVaR), também conhecido como Expected Shortfall (ES), emergiu como a métrica superior.

O CVaR mede a perda esperada dado que a perda excedeu o limite do VaR, capturando a severidade dos eventos extremos na cauda esquerda da distribuição. Diferentemente do VaR, o CVaR é uma medida coerente e convexa, o que permite sua minimização eficiente através de técnicas de programação linear, conforme demonstrado por Rockafellar e Uryasev (2000, 2002).

    - Transição da MPT para a PMPT

A transição da MPT para a PMPT no contexto deste trabalho implica a substituição da função objetivo do otimizador. Enquanto o modelo clássico de Markowitz minimiza a variância , o modelo Pós-Moderno aqui proposto busca minimizar o CVaR para um dado nível de retorno.

A formulação do problema de otimização de Média-CVaR pode ser descrita como a busca pelos pesos (w) que minimizam as perdas extremas ponderadas pela distribuição de probabilidade dos retornos, sujeitos às restrições de alocação. Estudos empíricos no mercado brasileiro indicam que carteiras otimizadas por Média-CVaR tendem a apresentar melhor desempenho ajustado ao risco e maior proteção contra drawdowns em períodos de crise, comparativamente às carteiras de Média-Variância, devido à sua sensibilidade aos momentos de ordem superior (assimetria e curtose).

Portanto, ao comparar carteiras geradas por diferentes otimizadores, espera-se que o otimizador PMPT (Mínimo-CVaR) gere alocações mais defensivas e robustas a eventos de cauda, refletindo de forma mais fidedigna a aversão à perda descrita pelas Finanças Comportamentais

  - Desconstrução Crítica da MPT: As Falácias da Normalidade e da Utilidade Quadrática

A resiliência da MPT no meio acadêmico e profissional, apesar de suas limitações conhecidas, deve-se à sua simplicidade pedagógica. No entanto, a aplicação da MPT em mercados reais exige a aceitação de pressupostos que, quando violados, podem levar a alocações de ativos subótimas e a uma subestimação perigosa dos riscos extremos. A PMPT surge como uma resposta direta a duas críticas estruturais à MPT: a suposição de distribuição normal dos retornos e a função de utilidade quadrática do investidor.

    - Limitações da Distribuição Normal: Caudas Pesadas e Assimetria

A MPT assume que os retornos dos ativos financeiros são variáveis aleatórias independentes e identicamente distribuídas (i.i.d.) que seguem uma distribuição normal (Gaussiana). Esta suposição é conveniente porque uma distribuição normal é perfeitamente descrita por apenas dois parâmetros: média e desvio padrão . Sob esta ótica, a probabilidade de eventos extremos diminui exponencialmente à medida que nos afastamos da média.

No entanto, evidências empíricas exaustivas demonstram que as séries temporais financeiras exibem características que violam sistematicamente a normalidade:

- Leptocurtose (Caudas Gordas): Os mercados financeiros apresentam uma frequência de eventos extremos (tanto positivos quanto negativos) significativamente maior do que a prevista pela distribuição normal. Eventos de "seis sigmas" , que teoricamente deveriam ocorrer uma vez a cada milhões de anos, ocorrem com uma regularidade alarmante em crises financeiras.

- Assimetria (Skewness): Os retornos não são simétricos. Em mercados de ações, por exemplo, observa-se frequentemente uma assimetria negativa, onde as quedas são mais abruptas e profundas do que as altas.

      - Implicação para a Gestão de Portfólio

Ao utilizar o desvio padrão como medida de risco, a MPT falha em distinguir entre a volatilidade gerada por "saltos" positivos e a volatilidade gerada por "crashes". Mais grave ainda, a MPT subestima o risco de cauda. Um fundo de hedge que opera estratégias de venda de opções fora do dinheiro pode apresentar um desvio padrão baixo e um Índice de Sharpe alto durante longos períodos de calmaria, ocultando um risco latente de ruína que só é capturado por métricas que consideram a curtose e a assimetria, como preconizado pela PMPT. Esta, ao não assumir normalidade, permite o uso de distribuições mais flexíveis ou métodos não paramétricos que capturam a verdadeira natureza do risco de cauda.

    - A Função de Utilidade e a Teoria da Perspectiva

A MPT baseia-se na Teoria da Utilidade Esperada, assumindo implicitamente que a função de utilidade do investidor é quadrática. Matematicamente, isso implica que o investidor penaliza desvios positivos e negativos da média com a mesma intensidade. Em termos práticos, sob a MPT, um retorno excepcionalmente alto é tão indesejável quanto um retorno excepcionalmente baixo, pois ambos aumentam a variância do portfólio.4

Esta premissa entra em conflito direto com as descobertas das Finanças Comportamentais, especificamente a Teoria da Perspectiva (Prospect Theory) desenvolvida por Daniel Kahneman e Amos Tversky. A Teoria da Perspectiva demonstra que os investidores exibem aversão à perda (loss aversion) em vez de aversão ao risco (risk aversion).

- Aversão à Perda: A dor psicológica de perder $100 é aproximadamente duas vezes mais intensa do que o prazer de ganhar $100.

- Ponto de Referência: Os investidores avaliam o desempenho não em relação à média do portfólio, mas em relação a um ponto de referência ou alvo (target return). Retornos acima do alvo são vistos como "ganhos" e retornos abaixo como "perdas".

A PMPT operacionaliza a Teoria da Perspectiva ao substituir a média pelo Retorno Mínimo Aceitável (MAR) e a variância pelo risco de downside. Dessa forma, a PMPT alinha a matemática da otimização de portfólio com a psicologia real do investidor: minimizando a probabilidade e a magnitude de falhar em atingir os objetivos financeiros, enquanto deixa o upside livre para capturar retornos excessivos.

*Tabela 2 - Comparação Estrutural: MPT vs. PMPT*

| Dimensão Analítica | Moderna Teoria do Portfólio (MPT) | Teoria Pós-Moderna do Portfólio (PMPT) |
| --- | --- | --- |
| Medida de Risco Central | Variância / Desvio Padrão | Downside Deviation / LPM / CVaR |
| Distribuição de Retornos | Normal (Simétrica, Paramétrica) | Qualquer (Não-Normal, Assimétrica, Empírica) |
| Definição de Risco | Dispersão em torno da média (Incerteza Total) | Fracasso em atingir o Retorno Mínimo (MAR) |
| Visão do Investidor | Avesso à variância (Quadrática) | Avesso à perda (Loss Aversion - Prospect Theory) |
| Tratamento do Upside | Penalizado como risco (aumenta ) | Ignorado ou valorizado (Upside Potential) |
| Objetivo da Otimização | Maximizar Retorno para dado | Maximizar Retorno para dado Downside Risk |

Fonte: Elaboração Propria

  - Conceitos Fundamentais de 'Downside Risk': A Estrutura dos Momentos Parciais Inferiores (LPM)

Para superar as limitações da variância, a PMPT adota a estrutura matemática dos Momentos Parciais Inferiores (Lower Partial Moments - LPM). Desenvolvida teoricamente por Bawa (1975) e expandida por Fishburn (1977), a família de métricas LPM oferece uma generalização flexível para mensurar o risco abaixo de um limiar específico. A elegância dos LPMs reside na sua capacidade de incorporar diferentes graus de aversão ao risco através de um único parâmetro,  (a ordem do momento).

    - Definição Matemática dos LPMs

Seja a variável aleatória que representa os retornos do ativo e  (tau) o Retorno Mínimo Aceitável (MAR) ou target return. O LPM de ordem  é definido pela integral:

No caso discreto, onde temos uma série temporal de  observações de retorno , a fórmula torna-se:

$

Nesta formulação, apenas os retornos que ficam abaixo do alvo  contribuem para a medida de risco. A função  atua como um filtro, zerando qualquer contribuição de retornos positivos (acima do alvo), o que reflete matematicamente a premissa de que o upside não é risco.

    - A Hierarquia dos Graus de LPM e suas Interpretações

A escolha do grau ( permite ajustar a métrica à psicologia do investidor, ponderando a severidade das perdas de maneira distinta:

- LPM de Ordem 0  – Probabilidade de Perda (Safety First):

- Mede a frequência com que o retorno cai abaixo do alvo.

- Matematicamente, equivale a .

- Interpretação: Responde à pergunta "Qual a chance de eu perder dinheiro?". No entanto, falha em distinguir entre uma perda pequena e uma perda catastrófica (uma perda de 1% conta o mesmo que uma de 50%).15

- LPM de Ordem 1  – Déficit Esperado (Target Shortfall):

- Mede a magnitude média das perdas. Os desvios abaixo do alvo são ponderados linearmente.

- Interpretação: Responde à pergunta "Se eu perder dinheiro, quanto espero perder em média?". É a medida de risco fundamental para o cálculo do Índice Omega (discutido na Seção 2.5) e reflete um investidor neutro ao risco em relação à severidade da perda, desde que a média seja controlada.

- LPM de Ordem 2  – Semivariância (Target Semivariance):

- Mede a dispersão quadrática dos retornos abaixo do alvo. Semelhante à variância, mas unilateral.

- Interpretação: Penaliza desproporcionalmente as grandes perdas. Uma perda duas vezes maior pesa quatro vezes mais no cálculo do risco. Esta é a medida preferida por Markowitz (1959) e a base para o Desvio Padrão de Downside , que é o denominador do Índice de Sortino.

- LPM de Ordens Superiores :

- Refletem uma aversão extrema a perdas catastróficas. À medida que  aumenta, o foco da métrica desloca-se quase exclusivamente para a cauda esquerda extrema da distribuição, ignorando pequenas flutuações negativas.

    - Semivariância vs. Variância: O Impacto na Alocação

A substituição da variância pela semivariância tem implicações profundas na construção de portfólios. Em distribuições simétricas (normais), a semivariância é proporcional à variância, e a fronteira eficiente da PMPT converge para a da MPT. No entanto, na presença de assimetria (skewness), as fronteiras divergem.

Um ativo com alta assimetria positiva (como uma opção de compra longa ou uma startup de venture capital) terá uma variância alta (devido ao potencial de ganho ilimitado) mas uma semivariância baixa (perda limitada ao capital investido). A MPT penalizaria este ativo, reduzindo sua alocação para diminuir o risco total. A PMPT, utilizando a semivariância, reconheceria o perfil favorável de risco/retorno e aumentaria a alocação, capturando o "upside potential". Estudos empíricos mostram que, em mercados emergentes ou durante crises, portfólios otimizados via semivariância tendem a preservar capital de forma mais eficiente do que aqueles baseados em média-variância.45

  - Métricas Avançadas de Risco e Propriedades de Coerência

A evolução da gestão de riscos não parou nos LPMs. A necessidade de quantificar o capital regulatório bancário e o risco sistêmico levou ao desenvolvimento de métricas baseadas em quantis, como o Value at Risk (VaR) e o Expected Shortfall (ES/CVaR). A análise dessas métricas sob a perspectiva da teoria axiomática de riscos revela distinções cruciais sobre sua confiabilidade.

    - Value at Risk (VaR): A Revolução Incoerente

Popularizado em 1994 pelo J.P. Morgan através do sistema RiskMetrics, o VaR tornou-se o padrão da indústria para a gestão de riscos de mercado e regulação bancária (Acordos de Basileia I e II). O VaR é definido como a perda máxima esperada em um determinado horizonte de tempo, com um certo nível de confiança .

Por exemplo, um VaR de 99% de $10 milhões em 1 dia implica que há apenas 1% de chance de a perda exceder $10 milhões.

Apesar de sua ubiquidade, o VaR apresenta falhas estruturais graves sob a ótica da PMPT e da teoria estatística:

- Cegueira da Cauda (Tail Blindness): O VaR indica o limiar da perda, mas nada diz sobre a severidade da perda caso esse limiar seja ultrapassado. Em distribuições de cauda gorda, a perda média além do VaR pode ser muitas vezes superior ao próprio VaR, ocultando riscos catastróficos.

- Violação da Subaditividade: Artzner et al. (1999), em seu artigo fundamental sobre medidas de risco coerentes, demonstraram que o VaR não é subaditivo. Isso significa que o VaR de um portfólio diversificado pode ser maior do que a soma dos VaRs dos ativos individuais . Essa propriedade perversa desencoraja a diversificação e viola um dos princípios basilares da gestão de portfólio. Exemplos teóricos e práticos mostram que, em distribuições muito assimétricas ou com caudas pesadas, a fusão de riscos pode parecer aumentar o risco medido pelo VaR, uma anomalia teórica inaceitável.

    - Medidas de Risco Coerentes e os Axiomas de Artzner

Para remediar as falhas do VaR, Artzner, Delbaen, Eber e Heath (1999) estabeleceram quatro axiomas que uma medida de risco  deve satisfazer para ser considerada "coerente" e segura para alocação de capital 50:

- Monotonicidade: Se o portfólio ( tem retornos sempre melhores que (, o risco de  deve ser menor .

- Subaditividade: O risco do todo não pode exceder a soma dos riscos das partes . Garante que a diversificação reduz o risco.

- Homogeneidade Positiva: O risco escala linearmente com o tamanho da posição .

- Invariância de Translação: Adicionar um montante garantido de caixa $k$ reduz o risco nesse mesmo montante .

    - Conditional Value at Risk (CVaR) / Expected Shortfall (ES)

Como resposta direta à incoerência do VaR, Rockafellar e Uryasev (2000, 2002) propuseram e operacionalizaram o Conditional Value at Risk (CVaR), também conhecido como Expected Shortfall (ES). O CVaR é definido como a média das perdas que ocorrem na cauda da distribuição, estritamente além do ponto de corte do VaR.56

    - Superioridade do CVaR na PMPT

- Coerência: O CVaR satisfaz todos os axiomas de Artzner, incluindo a subaditividade. Ele reconhece corretamente os benefícios da diversificação mesmo em cenários de estresse extremo.

- Convexidade e Otimização: Diferentemente do VaR, que é uma função não-convexa e difícil de otimizar (com múltiplos mínimos locais), o CVaR é convexo. Isso permitiu a Rockafellar e Uryasev desenvolver algoritmos de programação linear que podem otimizar portfólios com milhares de ativos e cenários de forma extremamente eficiente, minimizando diretamente o risco de cauda.

- Sensibilidade à Cauda: O CVaR captura a forma da distribuição na região de perdas extremas. Se um ativo possui "cisnes negros" latentes, o CVaR será significativamente maior que o VaR, alertando o gestor sobre a verdadeira dimensão do risco.

A transição regulatória global, exemplificada pela Fundamental Review of the Trading Book (FRTB) do Comitê de Basileia, que substituiu o VaR pelo Expected Shortfall para o cálculo de capital de risco de mercado, constitui a validação institucional definitiva dos princípios defendidos pela PMPT: o risco real reside na cauda, e métricas incoerentes são inadequadas para a segurança sistêmica.

  - Indicadores de Desempenho Ajustados: Sortino, Omega e a Generalização Kappa

A PMPT não se limita a medir o risco; ela redefine a avaliação de desempenho. O onipresente Índice de Sharpe, ao penalizar a volatilidade de alta, falha em capturar o valor gerado por gestores que produzem assimetria positiva. A PMPT propõe alternativas que integram os conceitos de downside risk e momentos superiores.

    - Índice de Sortino: Refinando Sharpe

Desenvolvido por Frank Sortino no início dos anos 1980 e popularizado nos anos 1990, o Índice de Sortino é a modificação mais direta e amplamente adotada do Índice de Sharpe. Ele substitui o desvio padrão total pelo Desvio de Downside  no denominador.

Onde:

- é o retorno médio do portfólio.

- (Minimum Acceptable Return) é o retorno alvo definido pelo investidor.

- (Target Downside Deviation) é a raiz quadrada da semivariância em relação ao MAR.

Análise Comparativa

O Índice de Sortino e o Sharpe convergem quando a distribuição dos retornos é normal e o MAR é igual à média. Contudo, para estratégias com alta assimetria positiva (e.g., trend following, opções longas), o Sortino será consistentemente superior ao Sharpe, pois não penaliza os ganhos voláteis. Inversamente, para estratégias com assimetria negativa (e.g., venda de volatilidade), o Sortino revelará um desempenho ajustado ao risco inferior, expondo os riscos ocultos que o Sharpe mascara.

    - O Índice Omega: Capturando Todos os Momentos

Introduzido por Keating e Shadwick em 2002, o Índice Omega  representa um salto conceitual ao dispensar completamente a necessidade de estimar momentos estatísticos (média, variância) e operar diretamente sobre a distribuição de probabilidade cumulativa dos retornos.

O Omega é definido como a razão entre a probabilidade ponderada de ganhos e a probabilidade ponderada de perdas em relação a um limiar :

Vantagem Crítica

O Omega captura implicitamente todos os momentos da distribuição (média, variância, assimetria, curtose e momentos superiores) em uma única métrica. Ao variar o limiar , o Omega fornece um perfil completo de risco-retorno, em vez de uma estimativa pontual. Isso o torna a ferramenta predileta para analisar ativos complexos e não lineares, como fundos de hedge e criptoativos, onde a suposição de normalidade é fatalmente falha.64

Adicionalmente, existe uma relação direta entre o conceito de Upside Potential Ratio e o Omega. O numerador do Omega corresponde ao potencial de alta (Upside Potential), enquanto o denominador corresponde ao potencial de baixa (Downside Potential), alinhando a métrica com a intuição econômica de ganho versus dor.

    - O Índice Kappa: A Generalização Unificadora

Kaplan e Knowles (2004) propuseram o Índice Kappa  como uma medida generalizada que unifica o Sortino e o Omega sob uma única estrutura matemática baseada em LPMs.

A elegância do Kappa reside na sua capacidade de recuperar as outras métricas através do ajuste do parâmetro :

- Quando , o Kappa é funcionalmente equivalente ao Índice Omega (ranking idêntico).

- Quando , o Kappa torna-se o Índice de Sortino.

- Para  ou superior, o Kappa penaliza severamente a curtose e riscos extremos de cauda.

Essa generalização permite que gestores de portfólio calibrem a métrica de desempenho especificamente para a função de utilidade de seus clientes. Para um investidor avesso a perdas catastróficas, um  ou seria mais apropriado; para um investidor focado na probabilidade geral de ganho, um  (Omega) seria ideal.

  - Fronteiras Eficientes: A Geometria da Assimetria

A aplicação das métricas de PMPT altera a geometria da fronteira eficiente. Enquanto a fronteira eficiente da MPT (média-variância) é sempre uma hipérbole suave e convexa, a fronteira eficiente da PMPT (retorno-LPM ou retorno-CVaR) pode assumir formas irregulares e não-suaves, especialmente quando composta por ativos com distribuições heterogêneas (mistura de ativos normais e não-normais).43

Em particular, a fronteira da PMPT tende a sugerir alocações mais concentradas em ativos com assimetria positiva e a evitar ativos com caudas esquerdas pesadas, mesmo que estes possuam alta média de retorno. Estudos recentes sobre criptoativos mostram que a otimização via PMPT resulta em portfólios com melhor proteção contra drawdowns severos do que a otimização via MPT, dado o perfil extremamente leptocúrtico desses ativos.

  - Avanços Recentes e Integração com Machine Learning (2024-2025)

A fronteira atual da pesquisa em PMPT reside na sua integração com a Inteligência Artificial. Publicações e estudos de 2024 e 2025 indicam uma tendência crescente no uso de algoritmos de Machine Learning, como fatores de momentum, para estimar dinamicamente os Momentos Parciais Inferiores e otimizar portfólios.

Ao contrário dos modelos estáticos tradicionais que dependem de dados históricos passados, modelos híbridos (PMPT + ML) conseguem prever mudanças nos regimes de volatilidade e na forma das caudas (tail risk forecasting), ajustando as alocações em tempo real para minimizar o CVaR futuro. Essa abordagem, denominada "Otimização Robusta Dinâmica", supera as limitações da MPT e da PMPT clássica, oferecendo resultados superiores em backtests e aplicações reais, especialmente em mercados voláteis e durante transições de regime econômico.

Além disso, a PMPT tem sido fundamental na integração de critérios ESG (Environmental, Social, and Governance) na gestão de portfólios. Estudos recentes sugerem que o uso de métricas de downside risk como o Índice de Sortino revela melhor o perfil de risco ajustado de empresas com altas pontuações ESG, que tendem a ter menor risco de cauda (menor risco reputacional e regulatório) do que empresas convencionais, algo que o Índice de Sharpe muitas vezes falha em capturar.

  - Conclusão

A Teoria Pós-Moderna do Portfólio representa a maturidade da gestão de investimentos quantitativa. Ao rejeitar a simplificação excessiva da normalidade e abraçar a complexidade assimétrica dos mercados e da psicologia humana, a PMPT oferece ferramentas — LPM, CVaR, Sortino, Omega — que são não apenas teoricamente superiores, mas pragmaticamente indispensáveis. Em um ambiente financeiro caracterizado por crises recorrentes e incerteza radical, a capacidade de distinguir entre o risco de ruína e a volatilidade de oportunidade é o que separa a sobrevivência da extinção. A PMPT é a linguagem matemática dessa distinção.

*Tabela 3 -  Resumo Analítico dos Indicadores de Desempenho (MPT vs. PMPT)*

| Indicador | Base Teórica | Fórmula Conceitual | Sensibilidade à Cauda | Principal Aplicação |
| --- | --- | --- | --- | --- |
| Sharpe | MPT (Variância) |  | Baixa (Assume Normalidade) | Ativos tradicionais, Benchmark relativo |
| Sortino | PMPT (LPM 2) |  | Média (Foca no Downside) | Fundos Assimétricos, Hedge Funds |
| Omega | PMPT (Todos Momentos) |  | Alta (Captura toda distribuição) | Derivativos, Cripto, Private Equity |
| Kappa | PMPT (LPM 3) |  | Muito Alta (Penaliza extremos) | Gestão de Risco de Cauda, Seguros |

Fonte: Elaboração propria.

  - O Modelo de Black-Litterman: Uma Reconstrução Bayesiana da Alocação de Ativos

    - Introdução: A Gênese Histórica e a Motivação Teórica

A evolução da gestão de portfólios institucionais sofreu uma inflexão paradigmática no início da década de 1990, impulsionada pelas limitações práticas da Teoria Moderna do Portfólio (MPT) de Harry Markowitz. Embora a MPT tenha fornecido a fundação matemática para a diversificação, estabelecendo a média-variância como o framework dominante para a análise de risco e retorno, a sua aplicação direta através da Otimização de Média-Variância (MVO) revelou-se profundamente problemática para gestores profissionais. Foi neste contexto de dissonância entre a elegância teórica acadêmica e a frustração prática operacional que Fischer Black e Robert Litterman, atuando na divisão de Gestão de Ativos da Goldman Sachs (GSAM), desenvolveram o Modelo Black-Litterman (BL).

    - O Contexto da Goldman Sachs e a Colaboração Black-Litterman

A transição de Fischer Black da academia para a prática financeira em 1984, ao juntar-se à Goldman Sachs, marcou o início de uma era de ouro na engenharia financeira aplicada. Black, já reverenciado por sua contribuição seminal ao modelo de precificação de opções Black-Scholes (1973), assumiu a liderança do Grupo de Estratégias Quantitativas da firma. Neste ambiente, ele colaborou estreitamente com Robert Litterman, um econometrista renomado e então vice-presidente da divisão de pesquisa de Renda Fixa.

A motivação primordial para o desenvolvimento do modelo não foi puramente acadêmica, mas sim uma necessidade comercial urgente. A Goldman Sachs buscava oferecer aos seus clientes institucionais uma abordagem quantitativa e disciplinada para estruturar portfólios de títulos internacionais (global bonds) e moedas. No entanto, Black e Litterman observaram que os modelos de otimização quantitativa existentes, baseados na MPT clássica, eram raramente utilizados na sua forma pura. Para tornar os resultados da otimização "palatáveis", os gestores eram forçados a impor restrições artificiais severas — como limites rígidos de posição por ativo ou proibição de vendas a descoberto — que, na prática, anulavam a inteligência matemática do otimizador.

Em 1990, a dupla apresentou internamente uma abordagem inovadora que permitia aos gestores incorporar suas visões de mercado sem destruir a estrutura de diversificação do portfólio. Inicialmente focado em renda fixa, o modelo foi expandido para ações em 1991 e formalizado academicamente com a publicação de dois artigos fundamentais: "Asset Allocation: Combining Investor Views with Market Equilibrium" no The Journal of Fixed Income (1991) e "Global Portfolio Optimization" no Financial Analysts Journal (1992). Estes trabalhos estabeleceram o modelo Black-Litterman (BL) não apenas como uma ferramenta proprietária da GSAM, mas como o novo padrão da indústria para a alocação de ativos, resolvendo o dilema da sensibilidade aos inputs.

    - As Limitações da Média-Variância e a Gênese do Black-Litterman

Embora a Teoria Moderna do Portfólio (MPT) tenha estabelecido os fundamentos da diversificação, sua implementação prática via otimização de Média-Variância (MV) enfrenta desafios críticos. Conforme apontam Michaud (1989) e Best e Grauer (1991), o otimizador MV tende a funcionar como um "maximizador de erros", sendo extremamente sensível aos inputs de retorno esperado. Pequenas variações nas estimativas podem resultar em carteiras extremas, pouco diversificadas e instáveis (soluções de canto), que não refletem a intuição do investidor.

Em resposta a essas limitações, Black e Litterman (1990, 1992) propuseram um modelo que mitiga a sensibilidade aos erros de estimação e produz alocações mais estáveis e robustas. O Modelo Black-Litterman (BL) não substitui a otimização MV, mas aprimora a estimativa dos retornos esperados — o input mais volátil do processo — utilizando uma abordagem Bayesiana para combinar informações de mercado com expectativas específicas do investidor.

    - A Estrutura Bayesiana: Prior, Visões e Posterior

O rigor matemático e a elegância prática do Modelo Black-Litterman residem na sua formulação como um problema de inferência Bayesiana. Ao contrário da estatística frequentista clássica, que trata os parâmetros (como o retorno esperado) como constantes fixas e desconhecidas, a abordagem Bayesiana trata os parâmetros como variáveis aleatórias que possuem uma distribuição de probabilidade própria. Isso permite incorporar explicitamente a incerteza sobre a estimativa e atualizar essa crença à medida que novas informações (visões) se tornam disponíveis. A estrutura conceitual do BL segue o silogismo Bayesiano clássico: sendo que a inovação central do modelo BL reside na combinação de duas fontes distintas de informação para gerar um novo vetor de retornos esperados (distribuição Posterior), o Prior (Equilibrio de Mercado), as Visões (Views - Q) e a Incerteza (Ω):

- O Prior (Equilíbrio de Mercado): Diferentemente de Markowitz, que muitas vezes utiliza médias históricas, o BL assume como ponto de partida neutro que o mercado está em equilíbrio. Utilizando um processo de "Otimização Reversa" (Baseada no CAPM), o modelo deriva os Retornos de Equilíbrio Implícitos (Π) a partir das capitalizações de mercado atuais. Esse vetor atua como um "centro de gravidade", garantindo que, na ausência de novas informações, a alocação ótima seja a carteira de mercado, evitando posições extremas.

- Likelihood, as Visões (Views - Q) e a Incerteza (Ω): O modelo permite que o investidor incorpore suas expectativas subjetivas ou quantitativas sobre o desempenho dos ativos. Essas visões são expressas no vetor Q e associadas a uma matriz de incerteza diagonal Ω, que reflete o grau de confiança em cada previsão (baseado, por exemplo, no erro quadrático médio dos modelos preditivos).

- Posterior, a Nova Estimativa Combinada: O resultado final é a distribuição a posteriori, calculada aplicando a Regra de Bayes. O vetor de retornos esperados BL  é uma média ponderada complexa entre o Prior (Equilíbrio) e a Likelihood (Visões).Se o gestor tem baixa confiança nas suas visões, o Posterior converge para o Prior (o portfólio tende ao índice de mercado).Se o gestor tem alta confiança, o Posterior afasta-se do equilíbrio na direção das visões, alterando os pesos do portfólio.Essa mecânica atua como um filtro de estabilidade (shrinkage estimator), mitigando a "maximização de erros" ao ancorar as estimativas em valores economicamente plausíveis.19

    - Derivação Matemática Detalhada: A "Fórmula Mestra"

A combinação do equilíbrio de mercado (Π) com as previsões dos modelos (Q), ponderada pela incerteza (Ω) e pelo escalar de confiança no prior (τ), resulta no vetor de Retornos Esperados de Black-Litterman (E[R]), calculado pela equação canônica do modelo:

Onde Σ representa a matriz de covariância dos retornos dos ativos.

O vetor resultante E[R] é então utilizado como input no otimizador de média-variância. A vantagem desta abordagem para o presente estudo é dupla: (i) permite testar se o fator de momentum 12-1 agrega valor estatístico ao portfólio (via vetor Q); e (ii) utiliza a estrutura Bayesiana para "suavizar" os erros de previsão desses modelos, ancorando as decisões no equilíbrio de mercado quando as previsões são incertas. Dessa forma, espera-se que as carteiras geradas via Black-Litterman apresentem desempenho ajustado ao risco superior e menor turnover do que aquelas baseadas puramente em otimização histórica.

    - A Crítica à MPT: O Dilema da "Maximização de Erros" e as Soluções de Canto

A inovação de Black e Litterman foi uma resposta direta e técnica às falhas patológicas da otimização de Markowitz quando alimentada com estimativas ruidosas. A literatura acadêmica da época, com destaque para os trabalhos de Richard Michaud (1989), já havia diagnosticado que a MVO atua, na prática, como um "maximizador de erros" (error maximizer). O algoritmo de otimização, ao buscar matematicamente a fronteira eficiente, tende a sobrealocar capital em ativos com retornos esperados marginalmente superiores e subestimar aqueles com retornos inferiores, ignorando que essas diferenças podem ser meramente fruto de erros de estimação ou ruído estatístico.

Black e Litterman (1992) articularam que o problema central não residia na matemática da otimização em si, mas na dificuldade intrínseca de estimar o vetor de retornos esperados . Enquanto a matriz de covariância  é relativamente estável e previsível ao longo do tempo, os retornos esperados são notoriamente voláteis e difíceis de prever. Na abordagem tradicional da MPT, um gestor é forçado a fornecer uma estimativa de retorno pontual para cada ativo no universo de investimento. Para um fundo global, isso poderia significar estimar retornos para centenas de ativos, muitos dos quais o gestor não possui uma opinião formada (visão neutra). A inserção de estimativas "neutras" ou baseadas apenas em médias históricas introduzia vieses que resultavam em portfólios extremos, instáveis e pouco diversificados, conhecidos como "soluções de canto" (corner solutions).

A solução proposta pelo modelo BL foi inverter o processo de engenharia do portfólio. Em vez de exigir que o investidor construísse as estimativas de retorno "do zero" (from scratch), o modelo parte de uma premissa de neutralidade baseada no equilíbrio de mercado. A filosofia subjacente é que, se o investidor não possui informações privilegiadas ou visões específicas que contradigam o mercado, a melhor estimativa de retorno é aquela que justifica a atual capitalização de mercado dos ativos. Apenas quando o investidor possui uma convicção forte (uma "visão") é que o portfólio deve desviar-se deste equilíbrio

  - Fundamentos Matemáticos: A Arquitetura Bayesiana

O rigor matemático e a elegância prática do Modelo Black-Litterman residem na sua formulação como um problema de inferência Bayesiana. Ao contrário da estatística frequentista clássica, que trata os parâmetros (como o retorno esperado) como constantes fixas e desconhecidas, a abordagem Bayesiana trata os parâmetros como variáveis aleatórias que possuem uma distribuição de probabilidade própria. Isso permite incorporar explicitamente a incerteza sobre a estimativa e atualizar essa crença à medida que novas informações (visões) se tornam disponíveis.2

A estrutura conceitual do BL segue o silogismo Bayesiano clássico:

- Prior: O Equilíbrio de Mercado

O ponto de partida do modelo, ou distribuição a priori, é a premissa de neutralidade. Na ausência de qualquer informação específica ou visão profética por parte do gestor, qual é a melhor estimativa racional para os retornos futuros? A resposta de Black e Litterman baseia-se na Hipótese de Mercados Eficientes e no CAPM (Capital Asset Pricing Model).

Assume-se que, no agregado, o mercado está em equilíbrio. Portanto, o portfólio de mercado (ponderado pela capitalização de todos os ativos) deve ser o portfólio ótimo para o investidor médio avesso ao risco. A partir dessa observação observável (os pesos de mercado), o modelo "engenharia reversa" os retornos que justificam esses pesos. Este vetor, denominado Retornos de Equilíbrio Implícitos , serve como a âncora gravitacional do modelo. Ele garante que, se o gestor não tiver visões ("eu não sei nada"), o modelo recomendará manter o portfólio de mercado passivo, evitando as alocações extremas da MPT.13

- Likelihood: As Visões do Investidor (Views)

A "verossimilhança" ou informação nova entra no modelo através das Visões. Diferente da MPT, que exige um vetor completo de retornos para todos os ativos, o BL permite que o gestor expresse opiniões apenas sobre um subconjunto de ativos (Visões Parciais). Estas visões podem ser absolutas ("Petrobras vai subir 10%") ou relativas ("Bancos vão superar Varejo em 2%"). Crucialmente, cada visão é acompanhada por um grau de incerteza (variância do erro), permitindo que o modelo pondere matematicamente a convicção do gestor.17

- Posterior: A Nova Estimativa Combinada

O resultado final é a distribuição a posteriori, calculada aplicando a Regra de Bayes. O vetor de retornos esperados BL  é uma média ponderada complexa entre o Prior (Equilíbrio) e a Likelihood (Visões).

- Se o gestor tem baixa confiança nas suas visões, o Posterior converge para o Prior (o portfólio tende ao índice de mercado).

- Se o gestor tem alta confiança, o Posterior afasta-se do equilíbrio na direção das visões, alterando os pesos do portfólio.

Essa mecânica atua como um filtro de estabilidade (shrinkage estimator), mitigando a "maximização de erros" ao ancorar as estimativas em valores economicamente plausíveis.19

    - Derivação Matemática Detalhada: A "Fórmula Mestra"

A implementação do modelo exige a manipulação precisa de álgebra matricial para combinar as distribuições normais assumidas para o Prior e as Visões. A seguir, detalha-se a derivação dos componentes críticos e a estrutura das matrizes envolvidas.

    - O Vetor de Retornos Implícitos  e a Otimização Reversa

O cálculo do Prior baseia-se na inversão da equação de otimização de Markowitz. O problema de maximização da utilidade quadrática do investidor representativo é dado por:

=

Onde:

- : Vetor de pesos dos ativos no portfólio de mercado.

- : Vetor desconhecido de retornos em excesso de equilíbrio.

- Matriz de covariância dos retornos dos ativos (estimada historicamente ou via modelos GARCH).

- : Coeficiente de aversão ao risco do mercado.

A condição de primeira ordem para a otimização . Reorganizando para isolar  , obtemos a fórmula da Otimização Reversa:

Este vetor  representa os retornos que o mercado precisa esperar para que os atuais pesos de capitalização  sejam ótimos. O parâmetro de aversão ao risco global  é frequentemente calibrado como , situando-se tipicamente entre 2 e 4 em estudos empíricos.16

A incerteza associada a esta estimativa do Prior é modelada como , onde  é um escalar de proporcionalidade. Portanto, a distribuição do Prior é:

    - A Estrutura das Visões: Matrizes

As visões subjetivas são modeladas como um sistema linear estocástico:

Com termo de erro  .

A Matriz de Projeção / Identificação

É uma matriz de dimensão , onde  é o número de visões e  o número de ativos. Cada linha  mapeia uma visão sobre os ativos.

- Visão Absoluta: Para uma visão sobre o Ativo A (índice ), o elemento  e os demais são .

- Visão Relativa: Para uma visão "Ativo A supera Ativo B", a linha contém valores positivos para  e negativos para. A soma da linha é tipicamente zero. A ponderação pode ser igualitária  ou ponderada por capitalização (value-weighted), o que reduz o ruído em visões sobre setores inteiros.15

O Vetor de Expectativas das Visões

É um vetor coluna . Cada elemento representa o retorno esperado da visão . Para visões relativas,  é o spread ou diferencial de retorno esperado, não o retorno total absoluto.22

A Matriz de Incerteza das Visões

É uma matriz de covariância  dos termos de erro . Assume-se geralmente que as visões são independentes, tornando  uma matriz diagonal:

A magnitude de  representa a incerteza da visão . Se 0, o investidor tem certeza absoluta (confiança infinita), e o modelo forçará o portfólio a satisfazer a visão exatamente. Se , a visão é ignorada.17

    - A Fórmula Mestra de Black-Litterman

Combinando o Prior  e a Likelihood  via Teorema de Bayes, obtemos a distribuição Posterior . O vetor de retornos esperados combinados é dado pela "Fórmula Mestra":

Esta equação, embora intimidante, é intuitivamente uma média ponderada pela precisão (inverso da variância).

- O termo  é a precisão do Prior (Equilíbrio).

- O termo  é a precisão das Visões projetada no espaço dos ativos.

- O modelo pondera  com base nessas precisões relativas.

Para fins computacionais, utiliza-se frequentemente a Identidade de Matrizes de Woodbury para reescrever a fórmula de modo a evitar a inversão da matriz  (que pode ser singular ou mal condicionada em grandes dimensões), resultando na forma alternativa mais estável numericamente:

Nesta forma, o retorno BL é explicitamente o Retorno de Equilíbrio  mais um termo de ajuste (tilt). O ajuste depende da discrepância entre a visão e o equilíbrio , escalado pela razão entre incerteza do Prior e incerteza da Visão.23

A nova matriz de covariância a posteriori, que deve alimentar o otimizador, é:

Note que  é maior que a covariância histórica  . O modelo adiciona uma camada extra de risco, refletindo a incerteza epistêmica sobre a verdadeira média dos retornos.22

  - A Controvérsia Teórica sobre o Escalar Tau

O parâmetro  permanece como um dos componentes mais esotéricos e debatidos na literatura do BL, gerando interpretações conflitantes sobre sua calibração e impacto.

- A Visão Original (Black & Litterman, 1992): Os autores sugeriram que  deveria ser um valor pequeno (próximo de zero), argumentando que a incerteza sobre a média de longo prazo é muito menor que a volatilidade dos retornos. Valores entre 0,025 e 0,05 são comuns nesta abordagem.24

- A Abordagem Estatística (Walters, 2014; Meucci, 2005): Argumentam que, se o Prior é derivado de uma série histórica,  deve ser calibrado como o erro padrão da média, ou seja, , onde  é o número de observações da amostra. Para 5 anos de dados mensais, .  Esta visão fornece uma base empírica objetiva para o parâmetro.24

- A Abordagem de Satchell e Scowcroft (2000): Propuseram fixar . Embora simplifique a álgebra, essa escolha altera drasticamente o peso relativo do Prior, exigindo que a matriz  seja recalibrada proporcionalmente para evitar que as visões dominem completamente o portfólio. Eles tratam a incerteza do prior e das visões como magnitudes comparáveis a priori.24

Em última análise, como demonstrado por Thomas Idzorek (2005), a escolha do valor escalar de  torna-se irrelevante para o cálculo do vetor de retornos  se a matriz  for calibrada endogenamente proporcional a . Contudo,  continua a afetar a matriz de covariância posterior , influenciando a magnitude absoluta do risco estimado.17

  - Inovações Práticas: O Método de Idzorek e a Matriz

A maior barreira para a adoção generalizada do BL não foi teórica, mas operacional: a especificação da matriz . Solicitar a um gestor que quantifique a "variância do erro da sua previsão" (ex: "Minha visão tem variância de 0.0045") é contra-intuitivo e propenso a erros de calibragem.

    - O Algoritmo de Confiança Percentual (Idzorek, 2005)

Thomas Idzorek propôs uma solução pragmática que traduz a intuição humana para a álgebra matricial. Seu método permite que o usuário especifique apenas um nível de confiança percentual (0% a 100%) para cada visão. O algoritmo então "implica" matematicamente o valor de  necessário.21

O processo, detalhado no trabalho seminal "A Step-by-Step Guide to the Black-Litterman Model" (2005), segue os seguintes passos lógicos:

- Cálculo do Portfólio de Certeza Total: O modelo calcula qual seria o vetor de retornos se o investidor tivesse 100% de confiança na visão (o que equivaleria a . Isso gera um vetor de pesos de alocação de "certeza total".

- Determinação do Desvio Máximo: Calcula-se a diferença de alocação (vetor de tilts) entre o portfólio de equilíbrio (sem visões) e o portfólio de certeza total.

- Interpolação Linear pela Confiança: Se o investidor declara 50% de confiança, o algoritmo define que o tilt alvo deve ser 50% do desvio máximo calculado no passo anterior.

- Engenharia Reversa de : O algoritmo resolve iterativamente ou analiticamente para encontrar os valores da diagonal de  que, quando inseridos na fórmula mestra do BL, resultam exatamente nesses pesos-alvo interpolados.

A fórmula implícita derivada por Idzorek assume que a variância da visão é proporcional à variância do portfólio da visão  ajustada por um fator de escala  derivado da confiança :

Essa inovação democratizou o modelo, permitindo que gestores fundamentais utilizassem a ferramenta quantitativa sem necessidade de doutorado em estatística, expressando visões como "Tenho 80% de confiança que Tech superará Energy".21

  - Comparação Crítica: BL, MPT e PMPT

A análise da evolução dos modelos de alocação exige distinguir claramente o papel de cada teoria. Uma confusão comum é tratar BL e PMPT como concorrentes diretos, quando na verdade atuam em dimensões distintas do problema de portfólio.

    - MPT vs. BL: A Correção da Estabilidade

A MPT (Markowitz) falha primariamente na sensibilidade aos inputs. Como discutido (Seção 3.1.2), a MPT maximiza erros de estimação, levando a soluções de canto. O BL corrige isso não alterando o otimizador, mas "limpando" os inputs. Ao ancorar o retorno esperado  no equilíbrio, o BL atua como um filtro Bayesiano que remove o ruído estatístico. O resultado são portfólios que, mesmo sem restrições, tendem a ser diversificados e intuitivos, ao contrário das alocações binárias da MPT pura.4

    - BL vs. PMPT: Complementaridade Estrutural

A Teoria Pós-Moderna do Portfólio (PMPT) critica a MPT por um motivo diferente: a medida de risco. A PMPT argumenta que a variância (utilizada tanto na MPT quanto no BL clássico) é uma medida falha porque penaliza a volatilidade positiva (upside) tanto quanto a negativa. A PMPT propõe métricas assimétricas como Semivariância, Downside Deviation e CVaR (Conditional Value at Risk).26

A relação entre BL e PMPT é de complementaridade, não substituição:

- Black-Litterman foca na melhoria da Estimativa de Retorno (Primeiro Momento, ).

- PMPT foca na melhoria da Medição de Risco (Segundos Momentos e Caudas).

Consequentemente, a fronteira da pesquisa atual em finanças quantitativas propõe modelos híbridos "BL-Mean-CVaR". Nesta abordagem, utiliza-se a estrutura Bayesiana do BL para derivar o vetor de retornos esperados robustos  e, subsequentemente, alimenta-se este vetor em um otimizador que minimiza o CVaR ou maximiza o Índice de Sortino (PMPT), em vez de minimizar a variância. Estudos empíricos indicam que essa combinação "Inputs BL + Otimizador PMPT" gera os portfólios mais robustos out-of-sample, protegendo contra riscos de cauda enquanto evita a instabilidade de alocação.28

Tabela 3.1: Síntese Comparativa dos Modelos

| Dimensão Analítica | MPT (Markowitz) | Black-Litterman (BL) | PMPT (Pós-Moderna) |
| --- | --- | --- | --- |
| Foco Principal | Diversificação Matemática | Estabilidade da Estimativa | Assimetria do Risco (Downside) |
| Input de Retorno | Histórico (Instável) | Equilíbrio + Visões (Bayesiano) | Histórico ou Subjetivo |
| Tratamento de Erros | Maximiza Erros (Michaud) | Mitiga via Shrinkage (Prior) | Neutro (Depende do Input) |
| Medida de Risco | Variância (Simétrica) | Variância (Canônico) | Semivariância, CVaR, LPM |
| Resultado Típico | Soluções de Canto (Instáveis) | Portfólio Diversificado (Estável) | Proteção de Cauda e Assimetria |

  - Limitações e Extensões Modernas

Apesar de sua elegância, o modelo BL clássico de 1992 não é isento de falhas, muitas das quais derivam de suas premissas simplificadoras herdadas da MPT.

    - Dependência da Normalidade e do CAPM

O modelo assume que os retornos dos ativos seguem uma distribuição Normal Multivariada. Esta suposição é empiricamente rejeitada pela presença observada de "caudas gordas" (leptocurtose) e assimetria (skewness) nos mercados financeiros, especialmente em períodos de crise.30 O uso da distribuição normal subestima a probabilidade de eventos extremos, tornando o BL clássico vulnerável a "Cisnes Negros". Adicionalmente, o Prior depende da validade do CAPM. Se o mercado for ineficiente ou se o proxy do portfólio de mercado for inadequado, o ponto de ancoragem  estará enviesado ("Garbage In"), contaminando toda a alocação subsequente.11

    - Entropy Pooling e Fully Flexible Views (Meucci)

Para superar a restrição da normalidade, Attilio Meucci (2008, 2010) introduziu a generalização conhecida como Entropy Pooling (Agrupamento de Entropia). Diferente do BL que usa fórmulas fechadas para conjugados gaussianos, o Entropy Pooling utiliza otimização numérica para minimizar a Divergência de Kullback-Leibler (Entropia Relativa) entre a distribuição Prior e a Posterior.30

As vantagens desta extensão são profundas:

- Prior Genérico: O Prior não precisa ser normal ou de equilíbrio. Pode ser uma distribuição empírica histórica, uma distribuição de Monte Carlo com caudas pesadas, ou derivada de Cópulas para modelar dependência não-linear nas caudas.

- Visões Flexíveis: O gestor não se limita a visões sobre médias . É possível inserir visões sobre volatilidade ("A vol vai aumentar"), correlação, ou medidas de cauda como o VaR ("O risco de perda máxima será de 15%").

- Consistência: O método garante que a distribuição Posterior seja a mais próxima possível do Prior (preservando a estrutura de mercado) enquanto satisfaz as restrições impostas pelas visões complexas.

Essa abordagem representa o estado da arte na alocação de ativos, permitindo a fusão da estabilidade Bayesiana do BL com a consciência de risco de cauda da PMPT em um framework matemático unificado e agnóstico quanto à distribuição subjacente.33

  - Conclusão do Capítulo

O Modelo de Black-Litterman transcendeu sua origem como uma ferramenta proprietária da Goldman Sachs para se tornar um pilar fundamental das Finanças Quantitativas modernas. Sua contribuição não foi refutar Markowitz, mas sim "salvar" a MPT de si mesma, introduzindo uma camada Bayesiana de bom senso econômico que estabiliza as alocações. Ao permitir a fusão elegante entre a disciplina passiva do equilíbrio de mercado e a inteligência ativa das visões do gestor, o BL resolveu o dilema da "maximização de erros". As suas extensões modernas, como o método de confiança de Idzorek e a Entropy Pooling de Meucci, asseguram que o modelo permaneça adaptável a um mundo financeiro cada vez mais complexo e não-normal, servindo como a ponte ideal entre a teoria de eficiência de mercado e a gestão ativa prática.

# CAPÍTULO 3 — METODOLOGIA DA PESQUISA

## Natureza e Classificação da Pesquisa

A presente pesquisa classifica-se, quanto à sua natureza, como aplicada, pois tem por finalidade gerar conhecimento prático sobre estratégias de alocação de ativos no mercado acionário brasileiro, com vistas à resolução de um problema concreto de gestão de portfólios. Quanto à abordagem, é quantitativa, utilizando modelos matemáticos, otimização convexa e técnicas de aprendizado de máquina para o processamento e a análise dos dados. Quanto aos objetivos, é descritiva e comparativa, na medida em que descreve o comportamento das séries financeiras e compara o desempenho de diferentes estratégias de alocação em um mesmo horizonte temporal.

O método adotado é o experimental por simulação histórica (backtesting), que consiste em aplicar, retroativamente sobre dados passados, as decisões de investimento que teriam sido tomadas por cada estratégia, respeitando rigorosamente a restrição de que apenas informações disponíveis até o momento da decisão são utilizadas, conforme o princípio de vedação ao viés de antecipação (look-ahead bias).

## Universo, Amostra e Fonte dos Dados

O universo da pesquisa compreende o conjunto de ações ordinárias e preferenciais negociadas na B3 (Brasil, Bolsa, Balcão) no período de janeiro de 2010 a dezembro de 2025, totalizando 3.967 pregões válidos.

Os dados de preços de fechamento ajustados por proventos — incluindo dividendos, desdobramentos e bonificações — foram obtidos por meio da base de dados Economática, que assegura a continuidade e a comparabilidade intertemporal das séries de preços ajustados.

### Critério de Inclusão na Amostra

Dada a heterogeneidade de liquidez do mercado acionário brasileiro, a amostra foi submetida a um critério restritivo de liquidez: foram retidos apenas os ativos presentes em 95% ou mais dos pregões do período completo (2010–2025). Esse limiar garante séries com continuidade estatística suficiente para a estimação confiável de matrizes de covariância e retornos esperados.

A aplicação desse crivo resultou em uma amostra final de 118 ativos, distribuídos nos principais setores da B3: Financeiro, Utilidade Pública, Consumo Cíclico, Materiais Básicos, Consumo Não Cíclico, Petróleo e Gás, Bens Industriais, Saúde, Imobiliário, Comunicações e Tecnologia. A lista completa dos ativos consta do Apêndice A.

Como variáveis macroeconômicas de referência, foram utilizados:

- **CDI** (*Certificado de Depósito Interbancário*): taxa de referência diária, utilizada como *proxy* da taxa livre de risco (RfR_f Rf​), obtida junto ao Banco Central do Brasil;

- SELIC: taxa básica de juros, utilizada como referência adicional de comparação;

- IBOVESPA: índice de mercado, utilizado como benchmark primário de desempenho e como proxy do portfólio de mercado para o modelo Black-Litterman.

## Tratamento e Preparação dos Dados

### Filtragem de Liquidez e Remoção de Anomalias

A matriz bruta de cotações foi processada em quatro etapas sequenciais, todas implementadas em Python com reprodutibilidade algorítmica completa:

- Etapa 1 — Estruturação Temporal: as séries foram indexadas pelo eixo de datas de pregão em formato datetime, com ordenação cronológica estrita e eliminação de eventuais duplicatas.

- Etapa 2 — Crivo de Liquidez: ativos com percentual de dados ausentes superior a 5% do total de pregões foram excluídos da amostra, conforme critério descrito na seção anterior.

- **Etapa 3 — Detecção de Anomalias via IQR:** para identificar erros de dados ou eventos corporativos não ajustados (desdobramentos sem reflexo no preço), aplicou-se o método da Amplitude Interquartil com multiplicador conservador de 3,0 (*outliers* severos). Observações que extrapolaram os limites   foram substituídas por valores ausentes para tratamento na etapa seguinte.

- Etapa 4 — Imputação Controlada: as lacunas remanescentes foram preenchidas por interpolação linear temporal entre os pontos válidos adjacentes. Lacunas nas bordas da série — quando o primeiro ou último pregão do ativo estava ausente — foram tratadas pelo método de propagação da última observação válida (forward-fill e backward-fill). O resultado final foi uma matriz de preços sem valores ausentes.

### Transformação dos Preços em Retornos

Os preços ajustados foram convertidos em duas modalidades de retornos diários, cada qual com finalidade metodológica distinta:

Retornos Simples (Discretos): calculados como variação percentual diária:

Os retornos simples foram utilizados como base da otimização de portfólio, pois satisfazem a propriedade de aditividade transversal: o retorno de uma carteira é a soma ponderada dos retornos individuais de seus ativos , condição indispensável para a correta aplicação do modelo de Markowitz.

Retornos Logarítmicos (Contínuos): calculados como logaritmo natural da razão de preços:

Os log-retornos foram utilizados exclusivamente para os testes econométricos, pois apresentam propriedades estatísticas superiores: aditividade temporal, maior proximidade com a distribuição normal e estacionariedade após a diferenciação.

### Diagnóstico Econométrico das Séries

Antes da estimação dos modelos de otimização, as séries de log-retornos foram submetidas a uma bateria de testes econométricos sobre os 118 ativos da amostra, cujos resultados estão consolidados no Apêndice K:

- Teste de Estacionariedade: a hipótese de raiz unitária (não-estacionariedade) foi avaliada por meio do Teste Dickey-Fuller Aumentado (ADF) via Variance Ratio e autocorrelação de lag-1. Os log-retornos mostraram-se estacionários em todos os 130 ativos, enquanto os preços brutos exibiram comportamento consistente com passeio aleatório — resultado esperado pela teoria e confirmado empiricamente.

- **Teste de Autocorrelação (Ljung-Box):** o teste foi aplicado tanto aos log-retornos quanto aos retornos ao quadrado (ri,t2r_{i,t}^2 ri,t2​), com defasagens de 5, 10 e 20 períodos. Os resultados revelaram autocorrelação linear significativa nos retornos em 115 de 130 ativos, e efeito ARCH — evidenciado pela autocorrelação nos quadrados — em **130 de 130 ativos**, indicando presença universal de agrupamento de volatilidade (*volatility clustering*).

- **Teste de Normalidade (Jarque-Bera):** a hipótese nula de distribuição normal foi rejeitada em **130 de 130 ativos** (p≈0p \approx 0 p≈0 em todos), com curtose excedente média de 19,0 e mediana de 8,69. Esse resultado fundamenta empiricamente a inadequação da variância simétrica como única medida de risco e justifica o uso de métricas de *downside risk* apresentadas no referencial teórico.

- Teste ARCH LM (Engle): a estatística LM foi calculada com 10 defasagens para cada ativo, com valor médio de 504,0 frente ao crítico de 18,31 (χ2\chi^2 χ2 com 10 graus de liberdade, α=5%\alpha = 5\% α=5%). O efeito ARCH foi confirmado em 130 de 130 ativos, o que implica que modelos de estimação de risco baseados em variância constante produzem inferências inválidas para a totalidade da amostra.

- Teste de Quebra Estrutural (Chow + CUSUM): a estabilidade paramétrica foi avaliada em quatro datas candidatas: início da recessão brasileira (2015), período do impeachment (2016), crash da COVID-19 (2020) e ciclo de juros extremo (2022). O teste de Chow sobre a média dos retornos não detectou quebras expressivas (menos de 8% de rejeições em qualquer data), confirmando que a média é estável. Contudo, a análise de volatilidade por subperíodo revelou elevação de 25% na variância após 2015, e o CUSUM detectou quebra formal em PETR4 centrada em janeiro de 2016. Esses resultados indicam que a quebra estrutural é na variância, não na média, fundamentando a necessidade de modelos de covariância dinâmica.

## Estimação dos Parâmetros de Otimização

### Prêmio de Risco (Excesso de Retorno)

Para cada ativo ii i e instante tt t, o prêmio de risco diário (excesso de retorno) foi calculado subtraindo-se a taxa livre de risco do retorno simples:

Onde  corresponde ao CDI diário no instante tt t. Analogamente, o prêmio de risco do mercado foi calculado como .

O CDI médio diário no período foi de 0,0369% ao dia, equivalente a aproximadamente 9,3% ao ano — valor consistente com a trajetória histórica da taxa DI entre 2010 e 2025.

### Retornos Esperados e Matriz de Covariância

Em cada ponto de rebalanceamento do backtest, os parâmetros de otimização foram estimados exclusivamente com dados disponíveis até a data de corte (expanding window), respeitando a vedação ao viés de antecipação:

- Vetor de Retornos Esperados : calculado como a média histórica simples dos retornos em excesso diários acumulados desde o início da amostra até a data de corte, anualizada por um fator de 252 dias úteis:

- Matriz de Covariância: estimada como a covariância amostral das séries de retornos em excesso, igualmente anualizada:

A dimensão da matriz no ponto de maturidade da amostra foi de .

## Modelos de Otimização Implementados

Esta seção formaliza os quinze modelos de alocação avaliados no estudo, organizados nas três famílias teóricas discutidas no Capítulo 2: (i) os modelos de média-variância da Teoria Moderna do Portfólio (MPT); (ii) os modelos de risco de queda (downside risk) da Teoria Pós-Moderna do Portfólio (PMPT); e (iii) as variantes do modelo Bayesiano de Black-Litterman (BL). Todos compartilham o mesmo arcabouço de restrições e a mesma penalidade de fricção transacional, descritos a seguir, sendo a função objetivo o elemento que os distingue.

### Otimização de Máximo Índice de Sharpe com Penalidade

Seja  o número de ativos investíveis em um dado ponto de rebalanceamento e  o vetor de pesos a ser determinado. Em cada um dos  pontos mensais do backtest, a janela expansiva de retornos — composta por todas as observações disponíveis desde o início da amostra até a data de corte, após um período mínimo de formação (treinamento inicial) de 60 meses (cinco anos) — é utilizada para estimar o vetor de retornos esperados em excesso anualizados  e a matriz de covariância anualizada , esta última obtida pelo estimador de encolhimento de Ledoit-Wolf descrito na Seção 3.4.2.

Todos os modelos estão sujeitos ao mesmo conjunto de restrições estruturais, que garantem a admissibilidade financeira das carteiras para um investidor institucional:

A primeira condição impõe o orçamento pleno (a totalidade do capital é alocada); a segunda impõe a vedação a vendas a descoberto (long-only), em conformidade com a regulação aplicável a fundos de investimento de varejo no Brasil; e a terceira é um teto de concentração por emissor, com  (sem teto) nas variantes irrestritas e  nas variantes identificadas pelo sufixo c10, que refletem o limite de 10% por emissor estabelecido pela Resolução CVM nº 175/2022.

Penalidade de fricção transacional (norma )

Para evitar que o otimizador realize realocações economicamente injustificadas a cada mês, incorpora-se à função objetivo uma penalidade proporcional ao giro (turnover) da carteira, medida pela norma  do vetor de variação de pesos:

onde  é o vetor de pesos vigente no período anterior (após a deriva natural dos preços) e  é o custo transacional proporcional, calibrado conservadoramente para corretagem, emolumentos e impacto de mercado na B3. Essa penalidade é isomórfica a uma regularização do tipo Lasso: ela induz esparsidade nas realocações e cria uma zona de não-negociação (no-trade zone), na qual o otimizador mantém os pesos inalterados sempre que o ganho marginal da realocação for inferior ao seu custo.

Solvers

Os problemas convexos diferenciáveis (média-variância e suas variantes) são resolvidos pelo algoritmo de Programação Quadrática Sequencial (SLSQP) da biblioteca scipy.optimize, eficiente para problemas de pequena dimensão () com restrições lineares e de caixa. Os problemas reformuláveis como programação linear ou cônica de segunda ordem (CVaR, CDaR) são resolvidos pela biblioteca cvxpy, com a cadeia de solvers CLARABEL → ECOS → SCS acionada por fallback automático em caso de não-convergência.

### Família I — Modelos de Média-Variância (MPT)

Os seis modelos desta família operacionalizam o paradigma de Markowitz (1952), no qual o risco é mensurado pela variância da carteira, .

- Ponderação Igualitária — EqualWeight (1/N)

A estratégia ingênua de referência atribui peso idêntico a todos os ativos, sem qualquer otimização:

Constitui o benchmark central de DeMiguel, Garlappi e Uppal (2009), contra o qual a vantagem informacional dos demais otimizadores é aferida.

- Inverso da Volatilidade — InvVol

Aloca capital de forma inversamente proporcional à volatilidade individual de cada ativo , ignorando as covariâncias cruzadas:

- Mínima Variância Global — MinVar

Minimiza a variância da carteira sem qualquer referência ao vetor de retornos esperados, o que a torna teoricamente robusta ao componente de estimação mais ruidoso do processo (DeMiguel; Garlappi; Uppal, 2009):

- Mínima Variância com Teto de 10% — MinVar_c10

Idêntica à anterior, com o teto de concentração  ativo, em conformidade com a Resolução CVM nº 175/2022.

- Máxima Utilidade Média-Variância — MaxSharpe ()

Maximiza uma função de utilidade quadrática que pondera retorno esperado e variância pelo coeficiente de aversão ao risco . Equivalentemente, minimiza o negativo dessa utilidade acrescido da penalidade transacional:

com . Cabe a ressalva metodológica de que esta formulação não maximiza diretamente o Índice de Sharpe — problema não-convexo —, mas sim a utilidade média-variância, que produz o portfólio de tangência apenas sob condições específicas. O rótulo histórico “Máximo Sharpe” é, portanto, mantido apenas por continuidade nominal com a literatura, devendo a função objetivo ser interpretada como de máxima utilidade.

- Máxima Utilidade Média-Variância com Teto de 10% — MaxSharpe_c10

Idêntica à anterior, com .

### Família II — Modelos de Risco de Queda (PMPT)

Esta família substitui a variância simétrica por medidas de risco assimétricas, sensíveis apenas às realizações desfavoráveis. O arcabouço unificador é o dos Momentos Parciais Inferiores (Lower Partial Moments, LPM), apresentado na Seção 2.10. Dada uma série de  retornos  da carteira e um retorno mínimo aceitável (Minimum Acceptable Return, MAR) , o LPM de ordem  é estimado por:

- Máximo Índice Ômega — MaxOmega

O Índice Ômega (Keating; Shadwick, 2002) é a razão entre o potencial de ganho acima do alvo e o risco de perda abaixo dele, correspondendo à razão entre os momentos parciais superior e inferior de primeira ordem ():

A estratégia busca os pesos que maximizam , com  fixado na taxa livre de risco (CDI).

- Máximo Índice de Sortino — MaxSortino

O Índice de Sortino (Sortino; Van der Meer, 1991) refina o Índice de Sharpe ao substituir o desvio-padrão total pelo desvio de queda (downside deviation), que é a raiz do LPM de segunda ordem ():

A estratégia maximiza  sujeita às restrições estruturais comuns.

- Máximo Índice Kappa de Ordem 3 — MaxKappa3

O Índice Kappa (Kaplan; Knowles, 2004) generaliza Sortino e Ômega para uma ordem  arbitrária do momento parcial inferior. A variante de ordem  incorpora a assimetria (skewness) da distribuição de perdas, penalizando mais intensamente as perdas extremas:

- Mínimo CVaR — MinCVaR

O Conditional Value-at-Risk (CVaR), ou Expected Shortfall, é a perda esperada condicional a que a perda exceda o quantil do Value-at-Risk ao nível de confiança  (adotado em ). Diferentemente do VaR, o CVaR é uma medida de risco coerente (Artzner et al., 1999) e convexa, podendo ser minimizada por programação linear através da formulação de Rockafellar e Uryasev (2000). Introduzindo a variável auxiliar  (o VaR) e as variáveis de folga , o problema é:

sujeito a:

onde  é o vetor de retornos dos ativos no período  da janela de estimação. A restrição sobre  captura apenas as perdas que excedem o limiar , de modo que a função objetivo minimiza a severidade média da cauda esquerda da distribuição.

- Mínimo CDaR — MinCDaR

O Conditional Drawdown-at-Risk (CDaR) transpõe a lógica do CVaR do domínio dos retornos para o domínio dos rebaixamentos acumulados (drawdowns), minimizando a média dos  piores rebaixamentos da curva de capital. Seja  o rebaixamento no instante , definido a partir do valor acumulado  como:

Analogamente ao CVaR, com variável auxiliar  e folgas , o problema linear é:

mantidas as restrições estruturais comuns. O CDaR é particularmente relevante para o investidor avesso a perdas prolongadas, por penalizar diretamente a magnitude e a persistência dos rebaixamentos.

### Família III — Modelo de Black-Litterman (BL)

Os quatro modelos desta família implementam o arcabouço Bayesiano de Black e Litterman (1992), que combina um prior de equilíbrio de mercado com visões quantitativas do investidor, gerando um vetor de retornos esperados posteriores mais estável que a média histórica.

Vetor de retornos implícitos de equilíbrio ()

O prior é obtido por otimização reversa do CAPM. Para garantir a viabilidade empírica e eliminar qualquer viés de antecipação (look-ahead bias) no vetor de pesos, adota-se um portfólio de referência estritamente equiponderado. O vetor de retornos que tornaria ótima a carteira neutra é extraído por:

onde  é o vetor de pesos onde cada ativo recebe a alocação de 1/N  , sendo N=118 , e   é o coeficiente de aversão ao risco agregado. Conforme documentado nas limitações (Seção 3.5.5), o  estimado por otimização reversa sobre a amostra resultou em valor negativo, economicamente inválido; adotou-se, portanto, o valor convencional , calibrado por He e Litterman (1999).

Visões quantitativas por momentum (, , )

As visões são absolutas e geradas pelo fator de momentum 12-1, definido como o retorno acumulado de cada ativo nos últimos doze meses, excluído o mês mais recente para mitigar o efeito de reversão de curto prazo. Como há uma visão por ativo, a matriz de incidência é a identidade, , e o vetor de visões  contém os retornos previstos por momentum. A matriz de incerteza das visões  é diagonal e proporcional à variância do prior, seguindo He e Litterman (1999):

Retorno esperado posterior (fórmula mestra)

A combinação Bayesiana do prior com as visões produz o vetor de retornos esperados posteriores pela fórmula mestra de Black-Litterman:

O vetor  resultante substitui então a média histórica  na função objetivo de máxima utilidade média-variância da Seção 3.5.2, sujeito às mesmas restrições e penalidade .

Variante downside (semicovariância de Estrada)

Nas variantes BL_downside, a matriz de covariância  — tanto no prior quanto na otimização — é substituída pela matriz de semicovariância de queda de Estrada (2008), que considera apenas as realizações conjuntas abaixo de um alvo de referência :

As quatro variantes implementadas

A combinação dos dois priors (clássico e downside) com a presença ou ausência do teto de concentração gera os quatro modelos da família:

- BL_classico — prior de equilíbrio com  de Ledoit-Wolf; sem teto;

- BL_classico_c10 — idem, com teto ;

- BL_downside — prior com a semicovariância de Estrada (2008); sem teto;

- BL_downside_c10 — idem, com teto .

### Síntese e Limitações Declaradas da Implementação

O Quadro a seguir consolida os quinze modelos, sua função objetivo e a medida de risco subjacente.

*Table 1 - Quadro de Consolidação dos 15 modelos*

| Modelo | Família | Função objetivo | Medida de risco | Teto |
| --- | --- | --- | --- | --- |
| EqualWeight | MPT | — (regra fixa ) | — | — |
| InvVol | MPT | — (regra ) | Volatilidade individual | — |
| MinVar | MPT | Min variância |  | Não |
| MinVar_c10 | MPT | Min variância |  | 10% |
| MaxSharpe | MPT | Máx utilidade MV () | Variância | Não |
| MaxSharpe_c10 | MPT | Máx utilidade MV () | Variância | 10% |
| MaxOmega | PMPT | Máx |  | Não |
| MaxSortino | PMPT | Máx Sortino |  | Não |
| MaxKappa3 | PMPT | Máx |  | Não |
| MinCVaR | PMPT | Min CVaR (95%) | Cauda de retornos | Não |
| MinCDaR | PMPT | Min CDaR (95%) | Cauda de drawdowns | Não |
| BL_classico | BL | Máx utilidade MV sobre | Variância | Não |
| BL_classico_c10 | BL | Máx utilidade MV sobre | Variância | 10% |
| BL_downside | BL | Máx utilidade MV sobre | Semicovariância | Não |
| BL_downside_c10 | BL | Máx utilidade MV sobre | Semicovariância | 10% |

Fonte: elaboração própria.

Três limitações de implementação são declaradas para preservar a integridade metodológica do estudo. Primeiro, o coeficiente de aversão ao risco  do modelo Black-Litterman, quando estimado por otimização reversa sobre a amostra completa, resultou em valor negativo — economicamente inválido por implicar propensão ao risco —, em razão de subperíodos com prêmio de risco do IBOVESPA negativo; adotou-se o valor convencional  de He e Litterman (1999), cuja adequação ao mercado brasileiro permanece uma hipótese a ser testada. Segundo, na ausência de dados de capitalização de mercado para a totalidade do painel, adotou-se a carteira equiponderada (1/N) como portfólio de referência do prior, em lugar da carteira de mercado por capitalização preconizada pela formulação canônica do CAPM reverso; embora essa escolha atenue a interpretação estrita de retornos de equilíbrio, ela tem a vantagem metodológica de eliminar o viés de antecipação que o uso de capitalizações de mercado correntes introduziria no prior. Terceiro, o custo transacional é modelado como uma taxa proporcional fixa de  sobre o giro, não capturando spreads de compra e venda específicos por ativo, por indisponibilidade de dados de microestrutura.

# CAPÍTULO 4 — RESULTADOS E DISCUSSÃO

## Estatísticas Descritivas e Diagnóstico Econométrico

### Modelo Black-Litterman com Visões de Momentum 12-1

A amostra final é composta por 118 ativos da B3 com presença mínima de 95% dos pregões entre janeiro de 2010 e dezembro de 2025, resultando em 3.967 observações diárias válidas por ativo. A distribuição setorial está apresentada na Tabela 4.1.

*Tabela 4 - Distribuição Setorial da Amostra*

| Setor econômico (B3) | Nº de ativos | % do universo |
| --- | --- | --- |
| Consumo Cíclico | 27 | 22,9% |
| Materiais Básicos | 18 | 15,3% |
| Utilidade Pública | 17 | 14,4% |
| Financeiro | 14 | 11,9% |
| Bens Industriais | 11 | 9,3% |
| Consumo Não Cíclico | 10 | 8,5% |
| Comunicações | 7 | 5,9% |
| Petróleo, Gás e Biocombustíveis | 5 | 4,2% |
| Saúde | 5 | 4,2% |
| Tecnologia da Informação | 4 | 3,4% |
| Total | 118 | 100,0% |

Fonte: elaboração própria com base nos dados da Economática (2026).

### Distribuição dos Retornos — Evidência de Não-Normalidade

*Tabela 5 - Estatísticas Descritivas dos Log-Retornos Diários (130 ativos)*

| Estatística | Média transversal | Mediana transversal | Mínimo | Máximo |
| --- | --- | --- | --- | --- |
| Retorno médio diário | 0,049% | 0,038% | -0,021% | 0,241% |
| Volatilidade anualizada | 38,40% | 35,10% | 14,20% | 94,70% |
| Assimetria | + 0,12 | + 0,08 | -3,21 | + 4,47 |
| Curtose excedente | 19,0 | 8,69 | 1,42 | 640 |
| Ativos com curtose > 3 | 125/130 (96,2%) | — | - | - |

Fonte: elaboração própria.

Os resultados confirmam, de forma conclusiva, a inadequação da hipótese de normalidade para a totalidade da amostra. A curtose excedente mediana de 8,69 indica que a distribuição empírica dos retornos brasileiros é aproximadamente 4,5 vezes mais leptocúrtica do que a distribuição normal, o que implica frequência significativamente maior de eventos extremos — tanto ganhos quanto perdas — em relação ao previsto pelo modelo gaussiano. Esse fenômeno é documentado para mercados emergentes por Damodaran (2007) e constitui uma das principais motivações para o emprego de métricas de risco assimétricas, como o CVaR e o índice de Sortino, abordadas no referencial teórico.

A assimetria média ligeiramente positiva (+0,12) mascara heterogeneidade relevante: 78 dos 130 ativos (60,0%) apresentaram assimetria negativa, indicando que perdas extremas são mais frequentes do que ganhos de mesma magnitude — comportamento consistente com a aversão à perda descrita pela Teoria da Perspectiva de Kahneman e Tversky (1979).

### Comportamento da Volatilidade por Subperíodo

A Tabela 4.3 apresenta a volatilidade média anualizada da amostra por ano calendário, revelando a presença de múltiplos regimes de volatilidade no período.

*Tabela 6 - Tabela 4.3 — Volatilidade Média Anualizada por Ano (cross-section de 130 ativos)*

| Ano | Vol. Média | Evento Relevante |
| --- | --- | --- |
| 2010–2013 | 28,30% | Período de expansão econômica |
| 2014–2016 | 38,70% | Recessão + crise política + Lava-Jato |
| 2017–2019 | 29,10% | Recuperação gradual |
| 2020 | 55,20% | Crash COVID-19 (março: pico de 93,7% em PETR4) |
| 2021–2022 | 34,60% | Ciclo de juros extremo (Selic > 13%) |
| 2023–2025 | 30,80% | Normalização relativa |

Fonte: elaboração própria.

A variabilidade da volatilidade entre subperíodos — com a volatilidade média do crash COVID representando 1,95 vezes a volatilidade do período pré-crise — constitui evidência empírica direta de que a hipótese de variância constante, implícita no modelo de Markowitz clássico, é violada sistematicamente. A quebra estrutural está na variância e não na média dos retornos, o que fundamenta a superioridade metodológica de abordagens que modelam dinamicamente a covariância ou que penalizam o risco de cauda.

### Estrutura de Correlação

A correlação média de Pearson entre os pares de ativos da amostra, calculada sobre os retornos em excesso diários do período completo, foi de 0,2058. Esse valor é inferior à correlação média documentada para o S&P 500 no mesmo período (aproximadamente 0,30–0,40), sugerindo maiores oportunidades de diversificação no mercado brasileiro em condições normais.

Contudo, a análise da covariância revelou que apenas 1 par dentre os 8.385 cruzamentos possíveis — RCSL4 e GOLL54 — apresentou covariância estritamente negativa (-0,0159). A quase totalidade das correlações é positiva, reflexo do elevado risco sistemático do mercado brasileiro, no qual choques macroeconômicos (variações da Selic, câmbio e ciclos políticos) afetam simultaneamente todos os ativos. Em períodos de crise, as correlações convergem para valores próximos de 1, eliminando os benefícios de diversificação precisamente quando são mais necessários.

### Síntese do Diagnóstico Econométrico

*Tabela 7 - Resultados Consolidados dos Testes Econométricos (135 ativos)*

| Teste | H₀ | Resultado |
| --- | --- | --- |
| ADF (log-retornos) | Raiz unitária | Estacionário em 130/130 ✓ |
| Ljung-Box Q(10) nos retornos | Sem autocorrelação | Rejeitada em 115/130 |
| Ljung-Box Q(10) nos retornos² | Sem efeito ARCH | Rejeitada em 130/130 ✗ |
| ARCH LM (10 defasagens) | Variância constante | Rejeitada em 130/130 ✗ |
| Jarque-Bera | Normalidade | Rejeitada em 130/130 ✗ |
| Chow (média, 4 datas) | Sem quebra na média | Não rejeitada em >92% ✓ |
| CUSUM (volatilidade) | Sem quebra na variância | Quebra detectada pós-2015 ✗ |

Fonte: elaboração própria. ✓ = favorável à modelagem; ✗ = requer atenção metodológica.

A convergência dos testes aponta três implicações diretas para a modelagem: (i) a transformação para log-retornos é suficiente para garantir estacionariedade; (ii) modelos de variância constante são inadequados para todos os ativos da amostra; e (iii) a distribuição gaussiana subestima sistematicamente o risco de eventos extremos. Esses achados corroboram empiricamente as premissas que motivaram o uso de penalidade L1 nos otimizadores e justificam a escolha do Índice de Sortino como métrica complementar ao Índice de Sharpe na avaliação de desempenho.

## Resultados do Backtest Out-of-Sample (2015–2025)Caracterização da Amostra Final

O período de avaliação out-of-sample compreende janeiro de 2015 a dezembro de 2025, com 132 pontos mensais de rebalanceamento para as estratégias L1. O portfólio inicia com valor normalizado em R$ 1,00 (ou equivalentemente, índice 100) e evolui segundo a curva de capital descrita na Metodologia (Seção 3.6).

### Estratégia 1 — Mínima Variância Global com L1

*Tabela 8 — Desempenho da Estratégia Mínima Variância (MinVar) (jan/2015 – dez/2025)*

| Métrica | MinVar | IBOVESPA | CDI |
| --- | --- | --- | --- |
| Retorno Acumulado | +231,80% | +215,00% | +166,14% |
| Vol. a.a. | 11,89% a.a. | 11,6% | 10,2% |
| Volatilidade Anualizada | 12,96% | - | - |
| Índice de Sharpe | 0,217 | - | - |
| Maximum Drawdown | -25,62% | - | - |
| Turnover médio mensal | -41,97% | - | - |

Fonte: elaboração própria. Nota: métricas de risco a serem completadas com os outputs do notebook 14_2_4.

A estratégia de Mínima Variância com penalidade L1 produziu o melhor resultado dentre as três estratégias implementadas, com retorno acumulado de 460,20% no período out-of-sample, superando em 245,20 pontos percentuais o IBOVESPA (+215,00%) e em 294,06 pontos percentuais o CDI (+166,14%).

O turnover médio de apenas 0,32% ao mês demonstra que a penalidade L1 cumpriu seu papel de estabilização: em 131 dos 132 rebalanceamentos mensais, as realocações foram marginais. O único episódio de turnover expressivo ocorreu em março de 2020 (14,57%), coincidindo com o crash pandêmico — período em que a mudança abrupta na estrutura de covariância tornou o portfólio anterior subótimo, forçando uma realocação defensiva relevante. Esse comportamento é teoricamente esperado: o otimizador de mínima variância, ao detectar o aumento da covariância sistêmica, redistribuiu o capital para os ativos com menor exposição ao risco de mercado no novo regime.

A superioridade da Mínima Variância sobre as demais estratégias é consistente com os resultados de DeMiguel, Garlappi e Uppal (2009), que demonstraram, para o mercado americano, que portfólios de mínima variância superam estratégias de otimização mais sofisticadas out-of-sample, uma vez que eliminam o componente de erro de estimação do vetor de retornos esperados — o input mais ruidoso e instável do processo de otimização de Markowitz.

A composição da carteira ao longo do período concentrou-se consistentemente em ativos de setores defensivos com baixa covariância com o mercado: energia elétrica (CGAS5, EQTL3, CLSC4), saneamento (SAPR4, CSMG3), alimentos processados (ABEV3, MDIA3) e farmacêutico (RADL3, HYPE3). Essa concentração setorial é endógena ao critério de mínima variância: ações de utilidade pública e consumo não cíclico apresentam menor exposição ao ciclo econômico, resultando naturalmente em menor covariância com o índice de mercado.

### Estratégia 2 — Máximo Índice de Sharpe com L1

*Tabela 9— Desempenho da Estratégia Máximo Sharpe (MaxSharpe) (jan/2015 – dez/2025)*

| Métrica | MaxSharpe | IBOVESPA | CDI |
| --- | --- | --- | --- |
| Retorno Acumulado | +290,18% | +215,00% | +166,14% |
| Vol. a.a. | 13,60% a.a. | 11,6% | 10,2% |
| Volatilidade Anualizada | 17,53% | - | - |
| Índice de Sharpe | 0,287 | - | - |
| Maximum Drawdown | -22,76% | - | - |
| Turnover médio mensal | -37,35% | - | - |

Fonte: elaboração própria. Nota: métricas de risco a serem completadas com os outputs do notebook 14_1_4.

A estratégia de Máximo Índice de Sharpe com penalidade L1 produziu retorno acumulado de 240,09%, superando marginalmente o IBOVESPA (+25,09 pp) e o CDI (+73,95 pp) no mesmo período.

O turnover médio de 4,29% ao mês é substancialmente maior do que o da Mínima Variância (0,32%), refletindo a instabilidade inerente ao vetor de retornos esperados estimado por média histórica. Os maiores choques de realocação ocorreram em março e abril de 2015 (respectivamente 15,14% e 13,08%) e dezembro de 2019 (11,99%), períodos de mudanças abruptas no desempenho relativo entre setores. Esse nível de turnover implica custo transacional anual estimado em aproximadamente 0,26% — valor reduzido, porém não negligenciável para horizontes longos.

A função objetivo do otimizador de Máximo Sharpe implementado neste trabalho corresponde, na prática, a uma maximização de utilidade média-variância com parâmetro de aversão ao risco , e não a uma maximização direta do índice de Sharpe, que seria um problema não-convexo. Essa distinção tem implicações para a interpretação dos resultados: o otimizador equilibra retorno esperado e risco, mas sem garantia de que o portfólio resultante seja o de máximo Sharpe ex-post.

### Estratégia 2 — Máximo Índice de Sharpe com L1

*Tabela 10 — Desempenho da Estratégia Black-Litterman com Momentum 12-1 (jan/2015 – dez/2025)*

| Métrica | BL Clássico (momentum 12-1) | IBOVESPA | CDI |
| --- | --- | --- | --- |
| Retorno Acumulado | +673,52% | +243,49% | +171,10% |
| CAGR | 21,12% a.a. | +12,17% | +10,51% |
| Volatilidade Anualizada | 25,99% | +23,31% | - |
| Índice de Sharpe | 0,511 | +0,10% | - |
| Índice de Sortino | 0,740 | +0,10% | - |
| Maximum Drawdown | -43,78% | -46,82% | - |
| Turnover médio mensal | 824,88% a.a. | - | - |

Fonte: elaboração própria com base nos outputs do notebook 19_Tabela_Metricas_Risco.ipynb.

A estratégia Black-Litterman com Momentum 12-1 produziu o pior resultado dentre as três estratégias, com retorno acumulado de apenas 56,48% — aproximadamente um quinto do retorno do IBOVESPA (+243,49%) no mesmo período. Todos os indicadores de risco apontam na mesma direção: o Índice de Sharpe negativo (-0,14) indica que a estratégia gerou retorno inferior à taxa livre de risco; o Índice de Sortino igualmente negativo (-0,15) confirma que a performance ajustada ao risco de downside também foi inferior; e o Maximum Drawdown de -92,99% revela que em algum momento do período o portfólio chegou a valer apenas 7% de seu valor inicial.

Esse resultado adverso demanda análise detalhada de suas causas, apresentada na Seção 4.4.

## Análise Comparativa entre Estratégias

### Tabela Unificada de Desempenho

*Tabela 11— Comparação Unificada das Estratégias (período out-of-sample 2015–2025)*

| Estratégia | CAGR | CAGR | Sharpe | Sortino | MaxDD |
| --- | --- | --- | --- | --- | --- |
| EqualWeight (1/N) | 5,97% | 19,84% | -0,075 | -0,102 | -41,97% |
| EqualWeight BuyHold | 15,71% | 19,30% | 0,372 | 0,520 | -34,50% |
| InvVol | 9,16% | 19,11% | 0,070 | 0,095 | -37,35% |
| MinVar | 11,89% | 12,96% | 0,217 | 0,295 | -25,62% |
| MinVar (c10) | 11,93% | 12,99% | 0,219 | 0,298 | -25,63% |
| MaxSharpe | 13,60% | 17,53% | 0,287 | 0,404 | -22,76% |
| MaxSharpe (c10) | 12,66% | 16,55% | 0,243 | 0,340 | -23,90% |
| MaxOmega | 9,82% | 21,21% | 0,111 | 0,157 | -30,61% |
| MaxSortino | 13,16% | 17,78% | 0,263 | 0,371 | -23,26% |
| MaxKappa3 | 13,32% | 18,26% | 0,269 | 0,381 | -22,55% |
| MinCVaR | 11,85% | 12,96% | 0,214 | 0,293 | -26,26% |
| MinCDaR | -1,75% | 21,09% | -0,417 | -0,565 | -81,81% |
| BL Clássico | 21,12% | 25,99% | 0,511 | 0,740 | -43,78% |
| BL Clássico (c10) | 17,99% | 20,30% | 0,460 | 0,643 | -34,33% |
| BL Downside | 20,66% | 32,36% | 0,456 | 0,666 | -59,82% |
| BL Downside (c10) | 14,45% | 22,32% | 0,301 | 0,421 | -37,13% |
| IBOVESPA | 11,26% | 23,32% | 0,178 | 0,245 | -46,82% |
| CDI (referência) | ~10,5% a.a. | — | — | — | — |

Fonte: elaboração própria.

Nota: a diferença nos valores do IBOVESPA e CDI entre as estratégias reflete leve diferença no ponto inicial do período (set/2015 para L1 vs jan/2015 para BL com momentum 12-1).

### Hierarquia de Desempenho e o Paradoxo da Complexidade

O resultado mais relevante deste estudo é o ordenamento inverso entre complexidade do modelo e desempenho out-of-sample:

- MinVar (mais simples) → melhor resultado absoluto e ajustado ao risco

- BL Clássico (complexidade intermediária) → resultado marginal sobre o benchmark

- Black-Litterman com Momentum 12-1 (mais complexo) → pior resultado, com destruição expressiva de capital

Esse padrão é teoricamente previsto por DeMiguel, Garlappi e Uppal (2009), que demonstraram que a adição de complexidade na estimação de retornos esperados tende a introduzir mais erro de estimação do que informação, resultando em portfólios out-of-sample inferiores às estratégias simples. No contexto brasileiro, a elevada volatilidade e a presença de regimes macroeconômicos distintos amplificam esse efeito, dificultando a extração de sinal preditivo consistente por modelos de machine learning.

### Análise do Desempenho do Black-Litterman com Momentum 12-1

O desempenho observado na estratégia BL com momentum decorre da combinação de três fatores identificados na análise do código:

- Caracterização das Visões de Momentum. As previsões de retorno (QQ Q) geradas pelo fator de momentum 12-1 variaram substancialmente de um mês para o outro, refletindo a baixa persistência dos padrões aprendidos pelos modelos em séries com relação sinal-ruído muito baixa. O Ljung-Box sobre os retornos ao quadrado confirmou que a estrutura de volatilidade é captável, mas a direção dos retornos — o que o LSTM tenta prever — não apresenta padrão exploravelmente consistente na escala mensal.

- Turnover Excessivo (55% ao mês). O custo transacional de 0,5% sobre o giro foi insuficiente para estabilizar as realocações frente à volatilidade das visões LSTM. Com 55% de giro mensal, a estratégia substitui a maior parte da carteira a cada dois meses, gerando custos de transação anualizados de aproximadamente 1,3% e impedindo a acumulação de retorno composto por qualquer posição individual.

- Escala Incorreta da Covariância no Prior. A covariância utilizada no modelo BL foi mensalizada (multiplicada por 21 dias) em vez de anualizada (multiplicada por 252), o que alterou a escala relativa entre o prior de equilíbrio (Π\Pi Π) e as visões de momentum 12-1 (QQ Q), conferindo peso excessivo às visões em detrimento do ancoras de equilíbrio de mercado — justamente o mecanismo de estabilidade que torna o BL superior à MPT pura.

A combinação desses três fatores BL com momentum apresentou elevada rotatividade decorrente da instabilidade das visões de momentum de curto prazo, sem o efeito estabilizador que caracteriza o modelo original de Black e Litterman (1992).

### Interpretação à Luz do Referencial Teórico

O resultado da Mínima Variância corrobora empiricamente no mercado brasileiro a tese central de Markowitz (1959) — posteriormente formalizada por DeMiguel et al. (2009) — de que a estimação confiável da covariância é mais factível do que a estimação confiável do vetor de retornos esperados. Ao eliminar completamente a dependência de μ^\hat{\mu} μ^​, a Mínima Variância evita que erros de estimação de retorno se propaguem para a alocação, produzindo portfólios mais estáveis e com menor turnover.

O resultado do BL com momentum, por sua vez, confirma o diagnóstico de Welch e Goyal (2008), que demonstraram que praticamente nenhum preditor econométrico melhora significativamente a previsão out-of-sample de retornos de ações em relação à média histórica simples. Modelos de séries temporais mais sofisticados, como modelos de machine learning, não são imunes a essa limitação fundamental: a baixíssima relação sinal-ruído dos retornos acionários impede a extração de informação preditiva estrutural, mesmo com arquiteturas de aprendizado profundo.

Por fim, a superação do IBOVESPA pela Mínima Variância (+245 pp) e, em menor grau, pelo Máximo Sharpe (+25 pp), é consistente com os achados de Santos e Tessari (2012) para o mercado brasileiro, que documentaram superioridade de estratégias quantitativas de otimização sobre o índice passivo, especialmente em cenários de alta volatilidade.

## l

A carteira igualmente ponderada (1/N) com rebalanceamento mensal produziu retorno acumulado de 267,7% (CAGR 12,8%, Sharpe 0,13), superando o IBOVESPA em 35,6 pontos percentuais no mesmo período. Esse resultado confirma empiricamente no mercado brasileiro os achados de DeMiguel, Garlappi e Uppal (2009): a diversificação ingênua supera o índice ponderado por capitalização out-of-sample. Mais relevante para os objetivos desta pesquisa, a Mínima Variância L1 (+460%) supera a 1/N (+268%) em 192 pontos percentuais, evidenciando que o ganho do otimizador é genuíno e não se explica pela seleção do universo de ativos.

# CAPÍTULO 5 — CONCLUSÃO

## Retomada da Questão de Pesquisa

Este trabalho partiu da seguinte questão central: qual a eficácia comparativa de carteiras construídas sob as óticas da MPT, PMPT e Black-Litterman, quando submetidas a diferentes métodos de estimação de inputs no mercado acionário brasileiro?

Para respondê-la, foram implementadas e avaliadas três estratégias de complexidade crescente sobre um universo de 135 ações da B3 com série histórica completa entre 2010 e 2025, em protocolo rigoroso de backtesting out-of-sample com 132 rebalanceamentos mensais entre janeiro de 2015 e dezembro de 2025.

## Síntese dos Resultados

A Tabela 5.1 sintetiza os achados centrais do estudo.

*Tabela 12-  Síntese Comparativa do Desempenho (jan/2015 – dez/2025)*

| Estratégia | CAGR | CAGR | Sharpe | Sortino | MaxDD |
| --- | --- | --- | --- | --- | --- |
| Mínima Variância L1 | 11,89% | 12,96% | 0,217 | 0,295 | -25,62% |
| MaxSharpe | 13,60% | 17,53% | 0,287 | 0,404 | -22,76% |
| Máximo Sharpe L1 | 21,12% | 25,99% | 0,511 | 0,740 | -43,78% |
| IBOVESPA | 11,26% | 23,32% | 0,178 | 0,245 | -46,82% |
| CDI (referência) | ~10,5% a.a. | — | — | — | - |

Fonte: elaboração própria.

O resultado mais importante do estudo é a inversão completa entre complexidade do modelo e desempenho: a estratégia mais simples — a carteira de Mínima Variância Global com penalidade L1 — produziu o maior retorno absoluto do período, superando o IBOVESPA em 245 pontos percentuais e o CDI em 294 pontos percentuais, com turnover médio de apenas 0,32% ao mês. A estratégia de complexidade intermediária — Máximo Índice de Sharpe com penalidade L1 — gerou ganho marginal sobre o benchmark de mercado. E a estratégia mais sofisticada — Black-Litterman

Diante desses resultados, a resposta à questão de pesquisa é direta: no mercado brasileiro entre 2015 e 2025, a adição de complexidade na estimação de inputs não produziu ganho de desempenho out-of-sample, mas sim destruição de valor. A estratégia que obteve o melhor resultado é precisamente aquela que elimina completamente o componente de retorno esperado da função objetivo, dependendo exclusivamente da estimação da matriz de covariância.

## Contribuições do Estudo

### Confirmação Empírica no Mercado Brasileiro

O principal achado deste trabalho confirma, no contexto do mercado acionário brasileiro, a tese central de DeMiguel, Garlappi e Uppal (2009) para o mercado americano: estratégias baseadas em modelos sofisticados de estimação de retornos esperados não superam consistentemente estratégias mais simples out-of-sample, porque o erro de estimação introduzido pelo modelo supera o ganho de informação gerado. A contribuição deste estudo é demonstrar que esse fenômeno — documentado para mercados maduros e eficientes — manifesta-se de forma ainda mais pronunciada no mercado brasileiro, em que a volatilidade elevada, a baixa relação sinal-ruído das séries de retornos e a presença de múltiplos regimes macroeconômicos amplificam os erros de estimação de qualquer modelo preditivo.

### Implicação Prática para Gestão de Portfólios

A superioridade da Mínima Variância com penalidade L1 tem implicação prática imediata para investidores institucionais no Brasil: a adoção de uma estratégia quantitativa simples, baseada exclusivamente na minimização da variância do portfólio com custo transacional explicitamente penalizado, teria gerado retorno acumulado superior ao IBOVESPA e ao CDI no período analisado, com baixíssimo giro da carteira (0,32% ao mês) e, consequentemente, custos operacionais negligenciáveis.

Esse resultado é relevante porque o IBOVESPA é o benchmark utilizado pela maioria dos fundos de ações brasileiros para avaliação de desempenho. Uma estratégia puramente quantitativa, sem qualquer análise fundamentalista ou visão macroeconômica discricionária, teria superado consistentemente esse benchmark durante uma janela de 11 anos que inclui crise política, recessão, pandemia e ciclos extremos de juros — demonstrando que a diversificação eficiente baseada na estrutura de covariância captura oportunidades de risco-retorno que o índice ponderado por capitalização não aproveita.

### Evidência sobre os Limites do Aprendizado de Máquina em Finanças

O desempenho adverso do Black-Litterman integrado a visões de momentum contribui para o debate em aberto sobre a aplicabilidade de modelos de aprendizado profundo à previsão de retornos acionários. Os resultados deste estudo são consistentes com Welch e Goyal (2008), que demonstraram que praticamente nenhum preditor econométrico melhora a previsão out-of-sample de retornos em relação à média histórica simples — conclusão que se estende aos modelos de aprendizado de máquina quando aplicados diretamente às séries de preços ou retornos.

A constatação não implica que redes neurais sejam inúteis em finanças; implica que o problema de prever a direção dos retornos acionários de curto prazo permanece fundamentalmente difícil, independentemente da arquitetura do modelo. Os modelos implementados neste trabalho mostraram-se mais informativos para a estrutura de covariância do que como preditores de retorno — dado observado no turnover elevado gerado pelas visões instáveis — o que sugere que a aplicação mais promissora para esse tipo de rede no contexto do Black-Litterman seria a estimação dinâmica da matriz de incerteza Ω\Omega Ω, e não do vetor de visões QQ Q.

## Limitações do Estudo

A interpretação dos resultados deve ser feita à luz das seguintes limitações metodológicas, reconhecidas explicitamente no espírito da transparência científica:

- Viés de antecipação parcial no Black-Litterman. Os pesos de mercado () utilizados no cálculo do prior de equilíbrio   foram obtidos com as capitalizações de mercado vigentes em maio de 2026, não com as capitalizações históricas de cada ponto de rebalanceamento. Esse procedimento introduz um viés de antecipação no prior do modelo BL que, embora provavelmente não determinante dado o peso reduzido do prior na presença de visões de alta incerteza, deve ser corrigido em estudos futuros mediante a coleta de séries históricas de capitalização.

- Delta negativo no CAPM reverso. O coeficiente de aversão ao risco  calculado por otimização reversa (δ=E[Rm−Rf]/σm2\delta = E[R_m - R_f] / \sigma_m^2 δ=E[Rm​−Rf​]/σm2​) resultou em valor negativo (-0,0884) para o período completo, em razão de subperíodos com prêmio de risco do IBOVESPA negativo. O valor convencional δ=2,5\delta = 2{,}5 δ=2,5 foi adotado em substituição, conforme He e Litterman (1999), porém essa substituição implica que o prior de equilíbrio não é derivado endogenamente dos dados da amostra, mas sim fixado por premissa externa.

- Escala da covariância no modelo BL. A matriz de covariância utilizada na fórmula mestra do BL foi mensalizada (×21 dias úteis) em vez de anualizada (×252), alterando a escala relativa entre prior e visões e conferindo peso excessivo às visões de momentum 12-1. Essa inconsistência de escala contribui para o turnover elevado observado e explica parcialmente a degradação do desempenho.

- Não padronização dos períodos de backtest. As estratégias L1 (Min Variância e Máximo Sharpe) iniciam o período out-of-sample em setembro de 2015, enquanto a estratégia BL com momentum 12-1 inicia em janeiro de 2015, resultando em valores distintos para o IBOVESPA como referência (+215% vs +243,49%). A comparação direta entre estratégias está, portanto, prejudicada, e deve ser tomada com cautela até que todos os backtests sejam recalculados com data de início padronizada.

- Benchmark 1/N O benchmark 1/N na versão buy-and-hold (sem rebalanceamento) apresenta concentração crescente ao longo do tempo — ao final de 2025, um único ativo representava aproximadamente 25% do portfólio, comprometendo a propriedade de diversificação que caracteriza a estratégia 1/N. Por essa razão, a versão com rebalanceamento mensal foi adotada como referência comparativa primária.

- Ausência de testes de significância estatística. As diferenças de desempenho entre estratégias são expressas em termos de retornos acumulados e índices de Sharpe, mas não são acompanhadas de testes formais de significância estatística — como o teste de Jobson-Korkie (1981) para igualdade de Índices de Sharpe ou o teste de Ledoit-Wolf (2008) para diferenças de retorno ajustado ao risco. A interpretação dos resultados deve considerar que o período de 132 meses, embora substantivo, pode ser insuficiente para distinguir habilidade de sorte em estratégias de alto risco.

## Sugestões para Pesquisas Futuras

Com base nos resultados e limitações deste trabalho, identificam-se cinco direções prioritárias para pesquisas futuras:

- Covariância dinâmica (DCC-GARCH). A quebra estrutural na variância detectada nos testes econométricos, com volatilidade do período COVID representando quase o dobro da volatilidade do período normal, sugere que a estimação estática da matriz de covariância é o principal ponto de fragilidade das estratégias L1 implementadas. A substituição por um modelo DCC-GARCH (Dynamic Conditional Correlation) permitiria que a covariância se adaptasse em tempo real às mudanças de regime, potencialmente melhorando o desempenho especialmente nos períodos de crise.

- Extensão do Black-Litterman com delta e pesos históricos. A reconstrução do modelo BL com capitalizações de mercado históricas e delta derivado de subperíodos de prêmio de risco positivo permitiria avaliar se a falha observada decorre das limitações das visões de momentum ou das inconsistências de implementação do prior identificadas neste trabalho.

- Modelos de machine learning como estimadores de volatilidade. Uma extensão direta e metodologicamente mais defensável seria utilizar modelos de machine learning para estimar dinamicamente a diagonal da matriz Ω\Omega Ω do modelo BL — ou seja, a incerteza das visões — em vez de gerar as próprias visões de retorno. Nessa configuração, o modelo de machine learning atuaria como um calibrador de confiança, deixando a estimação da direção dos retornos para o prior de equilíbrio.

- Inclusão do benchmark 1/N e teste de Jobson-Korkie. A adição da carteira igualmente ponderada como referência e a aplicação de testes formais de significância são extensões metodológicas imediatas que elevariam o rigor científico do estudo e permitiriam afirmações mais robustas sobre a geração de alfa pelas estratégias implementadas.

- Análise de subperíodos. A avaliação do desempenho das estratégias separadamente nos regimes de alta volatilidade (2015–2016 e 2020) e nos períodos de normalidade (2017–2019 e 2021–2025) permitiria identificar em quais condições de mercado cada estratégia apresenta vantagem relativa — informação de alto valor prático para investidores que precisam selecionar estratégias em função das condições macroeconômicas vigentes.

## Considerações Finais

Este trabalho demonstrou que, no mercado acionário brasileiro no período de 2015 a 2025, a complexidade dos modelos de estimação não foi aliada do desempenho out-of-sample. A carteira de Mínima Variância, ao ignorar deliberadamente o componente de retorno esperado, eliminou a principal fonte de erro de estimação do processo de otimização e produziu resultados superiores a todos os demais modelos testados, incluindo o índice de mercado e a taxa livre de risco.

Esse achado não é uma crítica à teoria de Black-Litterman ou ao uso de aprendizado de máquina em finanças — é uma evidência sobre as condições necessárias para que esses modelos funcionem. O Black-Litterman exige um prior bem calibrado, visões com poder preditivo genuíno e mecanismos de controle de turnover adequados ao sinal gerado pelas visões. O uso de fatores de momentum exige que tais fatores possuam poder preditivo persistente nas séries de retorno. Em um mercado com a volatilidade e a complexidade macroeconômica do Brasil, nenhuma dessas condições foi plenamente satisfeita na implementação realizada.

O resultado, portanto, não é uma falha dos modelos — é um resultado científico. A constatação de que estratégias simples superam estratégias sofisticadas em um mercado emergente específico, durante um período específico, é uma contribuição empírica legítima para a literatura de finanças quantitativas brasileiras, alinhada com os resultados de Santos e Tessari (2012) e com a tradição inaugurada por DeMiguel et al. (2009).

Ao pesquisador que se debruçar sobre esses dados com modelos mais robustos — prior historicamente calibrado, covariância dinâmica, visões com validação preditiva formal e período padronizado — o desafio permanece em aberto: superar consistentemente a Mínima Variância, a mais simples das estratégias, no mercado acionário brasileiro.

# REFERÊNCIAS

BLACK, Fischer. Capital market equilibrium with restricted borrowing. The Journal of Business, Chicago, v. 45, n. 3, p. 444–455, jul. 1972.

BLACK, Fischer; LITTERMAN, Robert. Global portfolio optimization. Financial Analysts Journal, Charlottesville, v. 48, n. 5, p. 28–43, set./out. 1992.

BOYD, Stephen; VANDENBERGHE, Lieven. Convex optimization. Cambridge: Cambridge University Press, 2004.

CAMPBELL, John Y.; LO, Andrew W.; MACKINLAY, A. Craig. The econometrics of financial markets. Princeton: Princeton University Press, 1997.

CHOW, Gregory C. Tests of equality between sets of coefficients in two linear regressions. Econometrica, New Haven, v. 28, n. 3, p. 591–605, jul. 1960.

DAMODARAN, Aswath. Investment valuation: tools and techniques for determining the value of any asset. 3. ed. Hoboken: John Wiley & Sons, 2012.

DEMIGUEL, Victor; GARLAPPI, Lorenzo; UPPAL, Raman. Optimal versus naive diversification: how inefficient is the 1/N portfolio strategy? The Review of Financial Studies, Oxford, v. 22, n. 5, p. 1915–1953, maio 2009.

DICKEY, David A.; FULLER, Wayne A. Distribution of the estimators for autoregressive time series with a unit root. Journal of the American Statistical Association, Alexandria, v. 74, n. 366, p. 427–431, jun. 1979.

ENGLE, Robert F. Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation. Econometrica, New Haven, v. 50, n. 4, p. 987–1007, jul. 1982.

FAMA, Eugene F. Efficient capital markets: a review of theory and empirical work. The Journal of Finance, Hoboken, v. 25, n. 2, p. 383–417, maio 1970.

FAMA, Eugene F.; FRENCH, Kenneth R. Common risk factors in the returns on stocks and bonds. Journal of Financial Economics, Amsterdam, v. 33, n. 1, p. 3–56, fev. 1993.

FAMA, Eugene F.; FRENCH, Kenneth R. A five-factor asset pricing model. Journal of Financial Economics, Amsterdam, v. 116, n. 1, p. 1–22, abr. 2015.

HE, Guangliang; LITTERMAN, Robert. The intuition behind Black-Litterman model portfolios. New York: Goldman Sachs Investment Management Division, 1999. (Investment Management Research).

HOCHREITER, Sepp; SCHMIDHUBER, Jürgen. Long short-term memory. Neural Computation, Cambridge, v. 9, n. 8, p. 1735–1780, nov. 1997.

JARQUE, Carlos M.; BERA, Anil K. A test for normality of observations and regression residuals. International Statistical Review, Hague, v. 55, n. 2, p. 163–172, ago. 1987.

JOBSON, J. D.; KORKIE, Bob M. Performance hypothesis testing with the Sharpe and Treynor measures. The Journal of Finance, Hoboken, v. 36, n. 4, p. 889–908, set. 1981.

KAHNEMAN, Daniel; TVERSKY, Amos. Prospect theory: an analysis of decision under risk. Econometrica, New Haven, v. 47, n. 2, p. 263–291, mar. 1979.

KWIATKOWSKI, Denis; PHILLIPS, Peter C. B.; SCHMIDT, Peter; SHIN, Yongcheol. Testing the null hypothesis of stationarity against the alternative of a unit root. Journal of Econometrics, Amsterdam, v. 54, n. 1–3, p. 159–178, out./dez. 1992.

LEDOIT, Olivier; WOLF, Michael. A well-conditioned estimator for large-dimensional covariance matrices. Journal of Multivariate Analysis, Amsterdam, v. 88, n. 2, p. 365–411, fev. 2004.

LINTNER, John. The valuation of risk assets and the selection of risky investments in stock portfolios and capital budgets. The Review of Economics and Statistics, Cambridge, v. 47, n. 1, p. 13–37, fev. 1965.

LJUNG, Greta M.; BOX, George E. P. On a measure of lack of fit in time series models. Biometrika, Oxford, v. 65, n. 2, p. 297–303, ago. 1978.

LO, Andrew W.; MACKINLAY, A. Craig. Stock market prices do not follow random walks: evidence from a simple specification test. The Review of Financial Studies, Oxford, v. 1, n. 1, p. 41–66, jan. 1988.

MARKOWITZ, Harry M. Portfolio selection. The Journal of Finance, Hoboken, v. 7, n. 1, p. 77–91, mar. 1952.

MARKOWITZ, Harry M. Portfolio selection: efficient diversification of investments. New York: John Wiley & Sons, 1959.

MERTON, Robert C. An analytic derivation of the efficient portfolio frontier. The Journal of Financial and Quantitative Analysis, Cambridge, v. 7, n. 4, p. 1851–1872, set. 1972.

NÚCLEO DE ECONOMIA FINANCEIRA E APLICADA (NEFIN). Fatores de risco do mercado acionário brasileiro. São Paulo: FEA-USP, 2024. Disponível em: http://nefin.com.br/risk_factors.html. Acesso em: jan. 2025.

ROCKAFELLAR, R. Tyrrell; URYASEV, Stanislav. Conditional value-at-risk for general loss distributions. Journal of Banking & Finance, Amsterdam, v. 26, n. 7, p. 1443–1471, jul. 2002.

ROM, Brian M.; FERGUSON, Kathleen W. Post-modern portfolio theory comes of age. The Journal of Investing, New York, v. 3, n. 3, p. 11–17, out. 1994.

ROLL, Richard. A critique of the asset pricing theory's tests. Part I: on past and potential testability of the theory. Journal of Financial Economics, Amsterdam, v. 4, n. 2, p. 129–176, mar. 1977.

ROSS, Stephen A. The arbitrage theory of capital asset pricing. Journal of Economic Theory, Amsterdam, v. 13, n. 3, p. 341–360, dez. 1976.

SANTOS, André Alves Portela; TESSARI, Cristina. Técnicas quantitativas de otimização de carteiras aplicadas ao mercado de ações brasileiro. Revista Brasileira de Finanças, Rio de Janeiro, v. 10, n. 3, p. 369–393, set. 2012.

SHARPE, William F. Capital asset prices: a theory of market equilibrium under conditions of risk. The Journal of Finance, Hoboken, v. 19, n. 3, p. 425–442, set. 1964.

SHARPE, William F. Mutual fund performance. The Journal of Business, Chicago, v. 39, n. 1, p. 119–138, jan. 1966.

SORTINO, Frank A.; PRICE, Lee N. Performance measurement in a downside risk framework. The Journal of Investing, New York, v. 3, n. 3, p. 59–64, out. 1994.

WELCH, Ivo; GOYAL, Amit. A comprehensive look at the empirical performance of equity premium prediction. The Review of Financial Studies, Oxford, v. 21, n. 4, p. 1455–1508, jul. 2008.

# CRONOGRAMA

*Tabela 13 - Cronograma da Pesquisa*

| ATIVIDADES | Março | Abril | Maio | Junho | Julho |
| --- | --- | --- | --- | --- | --- |
| 1 | Entrega da carta de aceite | X |  |  |  |  |
| 2 | Realização da matricula pela secretaria acadêmica | X |  |  |  |  |
| 3 | Definição do tema do projeto | X |  |  |  |  |
| 4 | Definição da estrutura | X |  |  |  |  |
| 5 | Realização do Tópico 1 do referencial teórico |  | X |  |  |  |
| 6 | Realização do Tópico 2 do referencial teórico |  | X |  |  |  |
| 7 | Introdução |  | X |  |  |  |
| 8 | Introdução Ajustes finais da introdução |  |  | X |  |  |
| 9 | Metodologia Definição do modelo e operacionalização da pesquisa |  |  | X |  |  |
| 10 | Metodologia Ajuste final da metodologia |  |  | X |  |  |
| 10 | Entrega - Formatação ABNT |  |  |  | X |  |

APENDICES

  - APÊNDICE A — Universo Investável Habilitado (N = 118)

Relação dos 118 ativos que satisfizeram simultaneamente os critérios de elegibilidade descritos no Capítulo 3 (presença em pregão ≥ 95%, primeiro pregão anterior ou igual a 04/01/2010 e ADTV fora do decil inferior aferido na janela de formação de 2010). A classificação setorial segue o setor econômico da B3.

*Tabela 14 - A1 - Composição Setorial*

| Setor econômico (B3) | Nº de ativos | % do universo |
| --- | --- | --- |
| Consumo Cíclico | 27 | 22,9% |
| Materiais Básicos | 18 | 15,3% |
| Utilidade Pública | 17 | 14,4% |
| Financeiro | 14 | 11,9% |
| Bens Industriais | 11 | 9,3% |
| Consumo Não Cíclico | 10 | 8,5% |
| Comunicações | 7 | 5,9% |
| Petróleo, Gás e Biocombustíveis | 5 | 4,2% |
| Saúde | 5 | 4,2% |
| Tecnologia da Informação | 4 | 3,4% |
| Total | 118 | 100,0% |

Fonte: elaboração própria, a partir de dados da Economatica e da classificação setorial da B3.

*Tabela 15 -Relação Completa dos Ativos*

| Posição | Ticker | Nome da Empresa | Setor (B3) |
| --- | --- | --- | --- |
| 1 | ABCB4 | Banco ABC Brasil S.A. | Financeiro |
| 2 | ABEV3 | Ambev S.A. | Consumo Não Cíclico |
| 3 | AGRO3 | BrasilAgro – Cia Brasileira de Propriedades Agrícolas | Consumo Não Cíclico |
| 4 | ALPA4 | Alpargatas S.A. | Consumo Cíclico |
| 5 | AMAR3 | Marisa Lojas S.A. | Consumo Cíclico |
| 6 | AMER3 | Americanas S.A. | Consumo Cíclico |
| 7 | AXIA3 | Companhia de Participações Aliança da Bahia* | Utilidade Pública |
| 8 | AXIA6 | Companhia de Participações Aliança da Bahia* | Utilidade Pública |
| 9 | B3SA3 | B3 S.A. – Brasil, Bolsa, Balcão | Financeiro |
| 10 | BBAS3 | Banco do Brasil S.A. | Financeiro |
| 11 | BBDC3 | Banco Bradesco S.A. | Financeiro |
| 12 | BBDC4 | Banco Bradesco S.A. | Financeiro |
| 13 | BEEF3 | Minerva S.A. | Consumo Não Cíclico |
| 14 | BRAP4 | Bradespar S.A. | Materiais Básicos |
| 15 | BRKM5 | Braskem S.A. | Materiais Básicos |
| 16 | BRSR6 | Banco do Estado do Rio Grande do Sul S.A. – Banrisul | Financeiro |
| 17 | CGAS5 | Companhia de Gás de São Paulo – COMGÁS | Utilidade Pública |
| 18 | CLSC4 | Centrais Elétricas de Santa Catarina S.A. – CELESC | Utilidade Pública |
| 19 | CMIG3 | Companhia Energética de Minas Gerais – CEMIG | Utilidade Pública |
| 20 | CMIG4 | Companhia Energética de Minas Gerais – CEMIG | Utilidade Pública |
| 21 | COCE5 | Companhia Energética do Ceará – COELCE | Utilidade Pública |
| 22 | CPFE3 | CPFL Energia S.A. | Utilidade Pública |
| 23 | CPLE3 | Companhia Paranaense de Energia – COPEL | Utilidade Pública |
| 24 | CSAN3 | Cosan S.A. | Petróleo, Gás e Biocombustíveis |
| 25 | CSMG3 | Companhia de Saneamento de Minas Gerais – COPASA | Utilidade Pública |
| 26 | CSNA3 | Companhia Siderúrgica Nacional – CSN | Materiais Básicos |
| 27 | CSUD3 | Companhia Siderúrgica Nacional – CSN Mineração* | Materiais Básicos |
| 28 | CYRE3 | Cyrela Brazil Realty S.A. Empreendimentos e Participações | Consumo Cíclico |
| 29 | DXCO3 | Dexco S.A. | Materiais Básicos |
| 30 | EGIE3 | Engie Brasil Energia S.A. | Utilidade Pública |
| 31 | EMBJ3 | Empresa Elétrica Bragantina S.A.* | Utilidade Pública |
| 32 | ENEV3 | Eneva S.A. | Utilidade Pública |
| 33 | EQTL3 | Equatorial Energia S.A. | Utilidade Pública |
| 34 | ETER3 | Eternit S.A. | Materiais Básicos |
| 35 | EUCA4 | Eucatex S.A. Indústria e Comércio | Materiais Básicos |
| 36 | EVEN3 | Even Construtora e Incorporadora S.A. | Consumo Cíclico |
| 37 | EZTC3 | EZTEC Empreendimentos e Participações S.A. | Consumo Cíclico |
| 38 | FESA4 | Cia de Ferro Ligas da Bahia – FERBASA | Materiais Básicos |
| 39 | FHER3 | Fertilizantes Heringer S.A. | Consumo Não Cíclico |
| 40 | FICT3 | Companhia de Telecomunicações do Brasil Central* | Comunicações |
| 41 | FLRY3 | Fleury S.A. | Saúde |
| 42 | GFSA3 | Gafisa S.A. | Consumo Cíclico |
| 43 | GGBR3 | Gerdau S.A. | Materiais Básicos |
| 44 | GGBR4 | Gerdau S.A. | Materiais Básicos |
| 45 | GOAU4 | Metalúrgica Gerdau S.A. | Materiais Básicos |
| 46 | GOLL54 | Gol Linhas Aéreas Inteligentes S.A. | Consumo Cíclico |
| 47 | GRND3 | Grendene S.A. | Consumo Cíclico |
| 48 | HAGA4 | Companhia Haga S.A.* | Bens Industriais |
| 49 | HBOR3 | Helbor Empreendimentos S.A. | Consumo Cíclico |
| 50 | HYPE3 | Hypera S.A. | Saúde |
| 51 | INEP4 | Inepar Indústria e Construções S.A. | Bens Industriais |
| 52 | ISAE4 | ISA Cteep – Cia de Transmissão de Energia Elétrica Paulista | Utilidade Pública |
| 53 | ITSA3 | Itaúsa S.A. | Financeiro |
| 54 | ITSA4 | Itaúsa S.A. | Financeiro |
| 55 | ITUB3 | Itaú Unibanco Holding S.A. | Financeiro |
| 56 | ITUB4 | Itaú Unibanco Holding S.A. | Financeiro |
| 57 | JHSF3 | JHSF Participações S.A. | Consumo Cíclico |
| 58 | KEPL3 | Kepler Weber S.A. | Bens Industriais |
| 59 | KLBN4 | Klabin S.A. | Materiais Básicos |
| 60 | LAND3 | Terra Santa Propriedades Agrícolas S.A. | Consumo Não Cíclico |
| 61 | LIGT3 | Light S.A. | Utilidade Pública |
| 62 | LOGN3 | Log-In Logística Intermodal S.A. | Bens Industriais |
| 63 | LPSB3 | LPS Brasil – Consultoria de Imóveis S.A. | Consumo Cíclico |
| 64 | LREN3 | Lojas Renner S.A. | Consumo Cíclico |
| 65 | LUPA3 | Lupatech S.A. | Petróleo, Gás e Biocombustíveis |
| 66 | MBRF3 | MBRF Global Foods Company S.A. | Consumo Não Cíclico |
| 67 | MDIA3 | M. Dias Branco S.A. Ind. e Com. de Alimentos | Consumo Não Cíclico |
| 68 | MOTV3 | Telequality Participações S.A.* | Comunicações |
| 69 | MRVE3 | MRV Engenharia e Participações S.A. | Consumo Cíclico |
| 70 | MULT3 | Multiplan Empreendimentos Imobiliários S.A. | Consumo Cíclico |
| 71 | MYPK3 | Iochpe-Maxion S.A. | Bens Industriais |
| 72 | NATU3 | Natura Cosméticos S.A. | Consumo Não Cíclico |
| 73 | NEXP3 | Nexen Pneus do Brasil S.A.* | Consumo Cíclico |
| 74 | ODPV3 | Odontoprev S.A. | Saúde |
| 75 | OIBR3 | Oi S.A. | Comunicações |
| 76 | OIBR4 | Oi S.A. | Comunicações |
| 77 | PDGR3 | PDG Realty S.A. Empreendimentos e Participações | Consumo Cíclico |
| 78 | PDTC3 | Padtec Holding S.A. | Tecnologia da Informação |
| 79 | PETR3 | Petróleo Brasileiro S.A. – Petrobras | Petróleo, Gás e Biocombustíveis |
| 80 | PETR4 | Petróleo Brasileiro S.A. – Petrobras | Petróleo, Gás e Biocombustíveis |
| 81 | PFRM3 | Profarma Distribuidora de Produtos Farmacêuticos S.A. | Saúde |
| 82 | PINE4 | Banco Pine S.A. | Financeiro |
| 83 | PMAM3 | Paranapanema S.A. | Materiais Básicos |
| 84 | POMO4 | Marcopolo S.A. | Bens Industriais |
| 85 | POSI3 | Positivo Tecnologia S.A. | Tecnologia da Informação |
| 86 | PSSA3 | Porto Seguro S.A. | Financeiro |
| 87 | RADL3 | Raia Drogasil S.A. | Saúde |
| 88 | RAPT4 | Randon S.A. Implementos e Participações | Bens Industriais |
| 89 | RDNI3 | RDI Negócios Imobiliários S.A.* | Consumo Cíclico |
| 90 | RENT3 | Localiza Rent a Car S.A. | Consumo Cíclico |
| 91 | RIAA3 | Guararapes Confecções S.A. | Consumo Cíclico |
| 92 | ROMI3 | Indústrias Romi S.A. | Bens Industriais |
| 93 | RPMG3 | Refinaria de Petróleos de Manguinhos S.A. | Petróleo, Gás e Biocombustíveis |
| 94 | RSID3 | Rossi Residencial S.A. | Consumo Cíclico |
| 95 | SANB11 | Banco Santander (Brasil) S.A. | Financeiro |
| 96 | SANB4 | Banco Santander (Brasil) S.A. | Financeiro |
| 97 | SBSP3 | Cia de Saneamento Básico do Estado de São Paulo – SABESP | Utilidade Pública |
| 98 | SCAR3 | São Carlos Empreendimentos e Participações S.A. | Consumo Cíclico |
| 99 | SLCE3 | SLC Agrícola S.A. | Consumo Não Cíclico |
| 100 | SMTO3 | São Martinho S.A. | Consumo Não Cíclico |
| 101 | TASA4 | Tensacalho S.A.* | Materiais Básicos |
| 102 | TCSA3 | Tecnisa S.A. | Consumo Cíclico |
| 103 | TELB4 | Telecomunicações Brasileiras S.A. – Telebras | Comunicações |
| 104 | TGMA3 | Tegma Gestão Logística S.A. | Bens Industriais |
| 105 | TIMS3 | TIM S.A. | Comunicações |
| 106 | TOTS3 | Totvs S.A. | Tecnologia da Informação |
| 107 | TPIS3 | Triunfo Participações e Investimentos S.A. | Bens Industriais |
| 108 | TRIS3 | Trisul S.A. | Consumo Cíclico |
| 109 | UNIP6 | Unipar Carbocloro S.A. | Materiais Básicos |
| 110 | USIM3 | Usinas Siderúrgicas de Minas Gerais S.A. – USIMINAS | Materiais Básicos |
| 111 | USIM5 | Usinas Siderúrgicas de Minas Gerais S.A. – USIMINAS | Materiais Básicos |
| 112 | VALE3 | Vale S.A. | Materiais Básicos |
| 113 | VIVR3 | Viver Incorporadora e Construtora S.A. | Consumo Cíclico |
| 114 | VIVT3 | Telefônica Brasil S.A. (VIVO) | Comunicações |
| 115 | VLID3 | Valid Soluções S.A. | Tecnologia da Informação |
| 116 | VSTE3 | Veste S.A. | Consumo Cíclico |
| 117 | WEGE3 | WEG S.A. | Bens Industriais |
| 118 | YDUQ3 | Yduqs Participações S.A. | Consumo Cíclico |

Fonte: elaboração própria. Ativos ordenados alfabeticamente pelo código de negociação.

Filtro de liquidez financeira (ADTV no decil inferior): exclusão dos ativos pertencentes ao decil inferior (P₁₀) da distribuição do Volume Diário Médio Negociado (Average Daily Traded Value), com o ADTV mensurado ex-ante exclusivamente na janela de formação de 2010 (dias sem negociação computados como volume nulo). Por ser um critério transversal ancorado no ano de ingresso, ativos que vieram a sofrer descontinuidade, recuperação judicial ou fechamento de capital nos anos seguintes permanecem elegíveis até o último pregão disponível, o que neutraliza o viés de sobrevivência.

  - Apêndice B – Diretrizes Metodológicas de Higienização e Filtragem de Liquidez da Base de Cotações

- Estruturação Relacional e Governança Dimensional: De modo a assegurar os preceitos de padronização estrutural (Tidy Data Structure), a base primária de cotações financeiras foi submetida a um algoritmo de alinhamento temporal. O eixo de tempo (datas de pregão) foi indexado sob a tipologia de dados datetime, garantindo a ordenação cronológica estrita dos vetores de preços e a eliminação de redundâncias transversais. O processo resultou num esqueleto vetorial constituído por 3.967 pregões contínuos.

- Crivo Estatístico de Omissões e Liquidez: Para mitigar os vieses decorrentes de ativos com baixa liquidez ou descontinuidade de negociação severa, implementou-se uma regra restritiva de tolerância para valores ausentes (Missing Values). O escrutínio metodológico estipulou uma tolerância máxima de 5% de dados omissos por ativo em relação à totalidade do período analisado. Ativos que ultrapassaram este limiar de iliquidez foram sumariamente excluídos da base empírica, salvaguardando a robustez dos estimadores inferenciais posteriores. O referencial metodológico adotado reteve 118 ativos que atenderam a este critério de alta liquidez.

- Diagnóstico e Escrutínio de Anomalias (Outliers): Considerando a suscetibilidade das séries financeiras a ruídos de infraestrutura ou não-ajustamento de proventos (como desdobramentos não refletidos), procedeu-se à detecção endógena de anomalias estatísticas severas. Empregou-se o Z-score modificado de Iglewicz e Hoaglin (1993), baseado na Mediana das Desvios Absolutos (MAD), com limiar K = 3,5 e constante de normalização c = 0,6745, calculado exclusivamente sobre variações não-nulas de cada série. Retornos com valor absoluto superior a 100% foram sinalizados como impossíveis. Adicionalmente, implementou-se uma barreira lógica de integridade, suprimindo quaisquer ocorrências irreais de preços negativos.

- Imputação Heurística Controlada:

- Na presença das omissões remanescentes e das lacunas geradas deliberadamente pela supressão das anomalias prévias, absteve-se taxativamente de substituições enviesadas que corrompessem a variância natural. O preenchimento operou-se exclusivamente por interpolação matemática temporal linear (time interpolation), resguardando a continuidade da série de tempo. Lacunas localizadas nas extremidades periféricas das séries foram corrigidas pelos métodos de propagação da última observação válida (Forward-Fill e Backward-Fill).

- Reprodutibilidade Algorítmica:Todo o fluxo de higienização de dados foi modelado num ambiente isolado (computação em linguagem Python acoplada à plataforma Jupyter), documentado de forma que as premissas matemáticas supramencionadas operassem de forma exógena e isenta de interferência manual arbitrária.

  - Apêndice C – Transformação Vetorial da Matriz de Cotações em Séries de Retornos Financeiros

- Estacionariedade e Retornos Financeiros: Os dados de apreçamento em formato bruto apresentam comumente um comportamento não estacionário. Para viabilizar a modelação estocástica, os dados foram submetidos a transformações matriciais com vistas a capturar as rentabilidades diárias.

- Derivação de Retornos Simples (Discretos): O vetor de retornos simples foi computado por intermédio da variação percentual discreta Rt = (Pt - Pt-1) / Pt-1. Este tratamento matemático foi executado para garantir o pilar analítico da agregação de ativos na construção teórica de Markowitz.

- Derivação de Retornos Logarítmicos (Contínuos): Concomitantemente, elaborou-se o processamento dos retornos compostos de forma contínua através do logaritmo natural das razões de preços: rt = ln(Pt / Pt-1). Esta estratégia fundamenta-se nas prerrogativas estatísticas para séries financeiras intertemporais independentes.

- Reprodutibilidade: Ambas as transformações operaram na supressão endógena da observação t0. O processo está consolidado integralmente na arquitetura computacional Python reproduzível.

  - Apêndice D – Consolidação da Base Mestre e Tratamento do Viés de Antecipação

- Integração de Variáveis Macroeconómicas e Benchmarks: Com o intuito de viabilizar o cálculo de indicadores de desempenho ajustados ao risco, a matriz de preços higienizada foi integrada aos vetores das taxas livres de risco (CDI e SELIC) e ao principal indicador do mercado acionário brasileiro (IBOVESPA). O processo de fusão operou via interseção cronológica estrita (Inner Join).

- Mitigação do Viés de Antecipação (Look-ahead Bias): Para assegurar a validade científica dos testes de backtesting a serem realizados a partir do ano de 2026, a base de dados de treinamento e parametrização foi deliberadamente truncada na data de 31 de dezembro de 2025. Esta separação rígida entre os períodos de estudo e validação impede que informações futuras influenciem a calibração dos modelos.

  - Apêndice E – Derivação do Prêmio de Risco e Estabelecimento dos Retornos em Excesso

- Transformação Paramétrica Preliminar: A partir da base de dados mestra consolidada, operou-se a segregação das variáveis. Os vetores de cotações e o IBOVESPA foram convertidos para retornos simples diários. O CDI foi isolado na forma de taxa de variação diária.

- Isolamento do Prémio de Risco (Excess Return): Alinhados os referenciais, executou-se a derivação vetorial do prémio de risco para cada ativo i no instante t mediante a subtração direta da taxa livre de risco: ERi,t = Ri,t - Rf,t, onde Rf,t compreende o CDI no instante homólogo.

- Prémio de Risco de Mercado: Calculou-se o retorno em excesso do mercado (ERm,t = RIBOV,t - Rf,t). A inclusão desta variável constitui um requisito endógeno para o cálculo subsequente da covariância e indicadores de risco sistemático.

  - Apêndice F – Parâmetros Inferenciais Globais: Covariância, Risco Sistemático e Desempenho Ajustado

- Matriz de Covariância Empírica Anualizada: Como alicerce incondicional para a otimização de Markowitz, processou-se a matriz de variância-covariância transversal anualizada (Σ_anual = Σ_diaria × 252). A volatilidade (desvio-padrão) individual de cada ativo é anualizada pela relação σ_anual = σ_diaria × √252. Esses construtos capturam a dinâmica de interdependência e magnitude dos co-movimentos latentes. Nota de auditoria: a notação anterior “sigma_anual = sigma_diaria * 252” estava incorreta para o desvio-padrão; a multiplicação direta por 252 (sem raiz quadrada) aplica-se exclusivamente à matriz de covariância Σ.

- Derivação do Risco Sistemático (Coeficiente Beta): Tendo o IBOVESPA como proxy de mercado, derivou-se o coeficiente Beta (beta = Cov(ERi, ERm) / Var(ERm)), refletindo a sensibilidade ao risco sistemático.

- Índice de Sharpe Analítico: Para o escalonamento do prémio de risco face à dispersão estocástica, calculou-se o Índice de Sharpe (IS = E[ERi] / sigma_i), refletindo o desempenho ajustado ao risco.

  - Apêndice G – Construção Estocástica e Otimização Numérica da Fronteira Eficiente de Markowitz

- Simulação Estocástica do Conjunto de Oportunidades Viáveis: Empregou-se uma simulação de Monte Carlo para gerar 50.000 portfólios com vetores de pesos aleatórios e normalizados. Este construto visou desenhar o Espaço Paramétrico de Viabilidade de Risco/Retorno.

- Otimização Numérica pelo Algoritmo SLSQP: Recorreu-se ao algoritmo SLSQP para identificar os vértices exatos da Fronteira Eficiente, sujeito às restrições de restrição orçamental e não-negatividade posicional (Long-Only).

- Derivação dos Portfólios Canónicos: Foram maximizadas as funções objetivo para isolar o Portfólio de Mínima Variância Global (MVP) e o Portfólio de Máximo Índice de Sharpe (Tangente).

  - Apêndice H – Isolamento Matricial De Covariâncias Negativas E Mapeamento De Hedge Estrutural

- Inspeção de Covariância Reversa: Procedeu-se a um escrutínio matricial para isolar estritamente os coeficientes onde sigma_i,j < 0, mapeando as oportunidades reais de hedge endógeno na amostra.

- Visualização Categórica via Mapa de Calor: Aplicou-se um algoritmo de mascaramento dinâmico para suprimir covariâncias positivas e redundâncias, gerando um Heatmap que evidencia apenas os pares de ativos com descorrelação negativa.

  - Apêndice I – Análise de Correlação de Pearson e Clusterização Hierárquica Estrutural

- Matriz de Correlação Univariada: Computou-se a Matriz de Correlação de Pearson (rho) sobre os retornos em excesso, isolando a dispersão volatilidade-dependente numa escala de [-1, 1].

- Agrupamento por Clusterização Hierárquica: A matriz foi submetida a um modelo de aprendizado de máquina não-supervisionado (Hierarchical Clustering) via método de Ward e distância Euclidiana, reorganizando o vetor espacial em blocos setoriais.

- Mapeamento da Fronteira de Máxima Diversificação Local: O algoritmo extraiu os pares ordenados com os coeficientes de correlação mais ínfimos, configurando a base referencial para a elaboração de portfólios descorrelacionados.

  - Apêndice J – Engenharia Reversa De Black-Litterman: Extração Do Vetor De Retornos Implícitos De Equilíbrio (Π)

- Premissa do Modelo: Para contornar a sensibilidade extremada do modelo Média-Variância a inputs históricos ruidosos, adotou-se o modelo bayesiano de Black-Litterman (1992).

- Extração do Vetor de Retornos Implícitos: A fase primordial consistiu na derivação do vetor Pi (Π = δ · Σ_LW · w_m), utilizando o coeficiente de aversão ao risco δ = 2,5 (fixo; He & Litterman, 1999) e o vetor de referência equiponderado w_m = 1/N. A matriz de covariância Σ_LW é estimada por Ledoit-Wolf e anualizada (×252). As visões de retorno são geradas pelo fator momentum 12-1 (sem LSTM nem ARIMA). A incerteza das visões Ω segue He & Litterman (1999), com τ = 0,05. Nota de auditoria (2026-06-04): a rotulagem “BL + LSTM” constante em versões anteriores do texto constitui erro descritivo. Não há implementação de redes neurais (LSTM) nem de ARIMA no repositório. A metodologia empregada é Black-Litterman com visões de momentum puro (12-1). Este processo estabiliza as expectativas de retorno e purga o efeito de anomalias pretéritas.

