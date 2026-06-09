UNIVERSIDADE FEDERAL DE GOIÁS
FACULDADE DE ADMINISTRAÇÃO, CIÊNCIAS CONTÁBEIS E CIÊNCIAS ECONÔMICAS
CURSO DE CIÊNCIAS CONTÁBEIS


PEDRO AUGUSTO PINHEIRO REIS


Teoria das Carteiras no Mercado de Ações Brasileiro:
Comparação entre Otimizadores e Inputs


Goiânia 2026

UNIVERSIDADE FEDERAL DE GOIÁS
FACULDADE DE ADMINISTRAÇÃO, CIÊNCIAS CONTÁBEIS E CIÊNCIAS ECONÔMICAS
CURSO DE CIÊNCIAS CONTÁBEIS


PEDRO AUGUSTO PINHEIRO REIS


Moderna Teoria das Carteiras no Mercado de Ações Brasileiro:
Comparação entre Otimizadores e Inputs


Goiânia

2026


# RESUMO


O presente estudo analisa a eficiência da alocação de ativos no mercado acionário brasileiro, investigando o impacto da variação dos métodos de estimação de parâmetros (*inputs*) e das funções objetivo (*otimizadores*) na performance de portfólios. Fundamentada na evolução da Teoria Moderna do Portfólio (MPT) para a Teoria Pós-Moderna (PMPT) e o modelo de Black-Litterman, a pesquisa compara carteiras construídas sob diferentes premissas de risco e retorno. Metodologicamente, foram testados três modelos de estimação de retornos esperados: Média Histórica, modelos autorregressivos (ARIMA) e Inteligência Artificial via Redes Neurais Recorrentes (LSTM). Estes *inputs* alimentaram quatro algoritmos de otimização distintos: Média-Variância (MV), Mínima Variância Global, Maximização do Índice de Sortino e Minimização do *Conditional Value at Risk* (CVaR). O estudo abrange o período de janeiro de 2010 a dezembro de 2025, permitindo avaliar a robustez das estratégias em diferentes ciclos de mercado. O desempenho das carteiras foi confrontado com os *benchmarks* IBOVESPA e CDI. Os resultados visam identificar se a incorporação de métricas de risco assimétrico (PMPT) e técnicas preditivas avançadas (Machine Learning) oferece superioridade estatística sobre os modelos clássicos de alocação no contexto brasileiro.
Palavras Chave: Otimização de Portfólio. Black-Litterman. Machine Learning. CVaR. Mercado Brasileiro.


# INTRODUÇÃO

Nos últimos anos, o mercado de capitais brasileiro passou por um processo de democratização expressiva, impulsionado principalmente pelo crescimento da participação dos investidores pessoas físicas. Segundo relatório publicado pela B3 (Pessoas Físicas: uma análise da evolução dos investidores na B3, 2022), o número de CPFs ativos na bolsa passou de cerca de 1 milhão em 2017 para mais de 4,5 milhões em 2022. Apesar do avanço, observou-se também uma queda no saldo mediano em custódia — de R$ 7 mil para R$ 3 mil no mesmo intervalo — sugerindo a entrada de pequenos investidores, muitos dos quais sem conhecimento técnico profundo sobre gestão de portfólios. Nesse cenário, cresce a relevância de estratégias eficazes de alocação de ativos, capazes de equilibrar retorno e risco de maneira acessível e objetiva.
A Moderna Teoria do Portfólio (Modern Portfolio Theory – MPT), proposta por Harry Markowitz em sua publicação seminal de 1952, inaugurou uma abordagem quantitativa para a seleção de ativos e a formação de carteiras eficientes. Fundamentada nos conceitos de diversificação e fronteira eficiente, a teoria busca otimizar a alocação de recursos maximizando o retorno esperado e minimizando o risco, representado pela variância dos retornos (MARKOWITZ, 1952; 1959). Posteriormente, William Sharpe (1966) contribuiu ao propor o Índice de Sharpe, que relaciona o retorno excedente ao risco total da carteira, oferecendo uma métrica objetiva de avaliação de desempenho ajustado ao risco.
Entretanto, a MPT assume hipóteses idealizadas — como a normalidade dos retornos e a simetria na distribuição dos riscos — que raramente se confirmam em mercados emergentes como o brasileiro (Damoradan, 2007). 
O modelo de Black-Litterman (1992) foi desenvolvido para tentar resolver os problemas práticos e as falhas do modelo de Markowitz. O BL é considerado uma **evolução e aprimoramento** do modelo de Markowitz.
A otimização de portfólio de Markowitz sofre de "maximização de erro" na prática, devido a uma sequência de acumulação de erros na estimação dos parâmetros (retornos e covariâncias). O otimizador de Markowitz é muito sensível à qualidade dos *inputs*, muitas vezes resultando em portfólios pouco intuitivos, pouco diversificados e com **soluções extremas** (grande concentração em poucos ativos).
O modelo Black-Litterman resolve esses problemas utilizando uma **abordagem Bayesiana** para combinar o retorno de equilíbrio de mercado (que pode ser entendido como uma otimização adaptada de Markowitz/CAPM) com as **visões especulativas e subjetivas do investidor** sobre o comportamento dos ativos. Essa junção de expectativas individuais com o equilíbrio de mercado gera carteiras mais estáveis, intuitivas e diversificadas
Além de Black-Litterman, outros estudos foram desenvolvidos em busca de alternativas ao modelo de Markowitz, como, por exemplo, a Pós-Moderna Teoria do Portfólio (Post-Modern Portfolio Theory – PMPT) (Rockafellar e Uryasev 2000, 2002). Ela propõe medidas mais adequadas ao comportamento do investidor real, como a semivariância, o Conditional Value at Risk (CVaR) e o Índices de Sortino e Ômega, priorizando a análise do risco de perdas ao invés da simples dispersão dos retornos (SORTINO; VAN DER MEER, 1991; ROM; FERGUSON, 1994).
A PMPT oferece, assim, uma visão mais realista e abrangente da gestão de portfólios, sobretudo em contextos de elevada volatilidade, assimetria e ocorrência de eventos extremos — características típicas de mercados emergentes (BROMBERG; COSTA JUNIOR, 2014). Essa abordagem reconhece que os investidores não se preocupam apenas com a variabilidade, mas sim com o risco de perdas significativas, proporcionando métricas de avaliação mais sensíveis às preferências comportamentais dos agentes.
Diante desse panorama, este trabalho busca responder à seguinte questão de pesquisa: **"** **No mercado brasileiro (caracterizado por 'caudas pesadas'), ****no período de 2010 a 2024****, ****o desempenho do portfólio é mais sensível à melhoria dos inputs** **ou à melhoria do otimizador****?"**
Este trabalho está estruturado da seguinte forma: o Capítulo 2 apresenta o referencial teórico, O Capítulo 3 descreve a metodologia, O Capítulo 4 analisa os resultados, O Capítulo 5 apresenta as conclusões.

# REFERENCIAL TEÓRICO


# Capítulo 1: Fundamentação Teórica e Revisão Bibliográfica da Moderna Teoria do Portfólio


## Introdução: A Evolução Histórica da Gestão de Investimentos

A gestão de investimentos, historicamente uma arte dominada pela intuição e pela análise fundamentalista idiossincrática, sofreu uma revolução paradigmática em meados do século XX. Antes do advento da Teoria Moderna do Portfólio (Modern Portfolio Theory - MPT), a prática de alocação de capital carecia de uma estrutura teórica unificada que quantificasse a relação entre risco e retorno de maneira sistemática. Este capítulo delineia a trajetória intelectual que transformou as finanças de uma disciplina descritiva em uma ciência normativa e quantitativa, culminando nos modelos de equilíbrio que sustentam a indústria global de gestão de ativos contemporânea.

## O Paradigma Pré-Markowitz: A Era da Seleção de Ativos

Até o início da década de 1950, a teoria de investimentos operava sob o "paradigma da seleção de ativos" (*stock picking*). A literatura seminal da época, epitomizada pelas obras de John Burr Williams e da dupla Benjamin Graham e David Dodd, focava quase exclusivamente na determinação do valor intrínseco de títulos individuais, tratando a construção do portfólio como uma consequência secundária da acumulação de ativos subavaliados (WILLIAMS, 2014).
John Burr Williams, em sua *magnum opus* de 1938, *The Theory of Investment Value*, introduziu o Modelo de Desconto de Dividendos (Dividend Discount Model - DDM), estabelecendo que o valor de um ativo é o valor presente de seus fluxos de caixa futuros esperados, descontados a uma taxa de juros apropriada (WILLIAMS, 2014). A fórmula de Williams,  , onde  representa os dividendos e  a taxa de desconto, proporcionou o primeiro rigor matemático para a avaliação de equities (GUERARD, 2010). Contudo, a abordagem de Williams sofria de uma limitação crítica: ela assumia que o risco poderia ser virtualmente eliminado através da diversificação, sem fornecer um mecanismo matemático para quantificar como a variabilidade dos retornos de diferentes ativos interagia (RUBINSTEIN, 2002). Williams focava na maximização do retorno esperado, acreditando que a "lei dos grandes números" protegeria o investidor que diversificasse suficientemente (RUBINSTEIN, 2002).
Paralelamente, Benjamin Graham e David Dodd, em *Security Analysis* (1934), estabeleceram os princípios do *Value Investing*. Embora defendessem a diversificação como uma medida prudencial — sugerindo a detenção de dez a trinta papéis diferentes para mitigar o erro de análise — o conceito de risco em sua estrutura era fundamentalmente qualitativo (BOYD, JOHANSSON, KAHN, SCHIELE, SCHMELZER, 2024). Para Graham, risco não era volatilidade, mas sim a possibilidade de perda permanente de capital decorrente da deterioração dos fundamentos da empresa ou de pagar um preço excessivo em relação ao valor intrínseco (GUERARD, 2010). A "Margem de Segurança" era a métrica de proteção, não o desvio padrão ou a covariância. Neste paradigma, o portfólio era visto como uma coleção de ativos individuais, onde cada componente era julgado por seus próprios méritos, isolado do contexto agregado da carteira(GUERARD, 2010).

### A Transição para a Análise Quantitativa

A ruptura com o paradigma da seleção individual de ativos não ocorreu abruptamente, mas foi precedida por desenvolvimentos teóricos que começaram a questionar a suficiência da maximização do valor presente. Economistas como Hicks (1939) e Marschak (1938) já exploravam as preferências sobre momentos estatísticos, e o matemático italiano Bruno de Finetti, em 1940, havia formulado um problema de alocação média-variância no contexto de resseguros, embora seu trabalho tenha permanecido desconhecido no mundo anglófono por décadas (BOYD, JOHANSSON, KAHN, SCHIELE, SCHMELZER, 2024).
O momento decisivo, contudo, surgiu da insatisfação intelectual de Harry Markowitz com a teoria vigente. Enquanto lia a obra de Williams na biblioteca da Universidade de Chicago, Markowitz teve um *insight* que desmantelaria a lógica da maximização pura do retorno (MARKOWITZ, 1959). Ele percebeu que, se a regra de Williams fosse seguida estritamente em um mundo de incerteza, um investidor racional deveria alocar 100% de seu capital no único ativo com o maior retorno esperado descontado (WILLIAMS, 2014). Se dois ativos tivessem o mesmo retorno máximo, o investidor seria indiferente entre eles, mas a teoria não oferecia nenhuma razão intrínseca para manter ambos (MARKOWITZ, 1959).
Markowitz identificou que a prática observada e intuitivamente racional da diversificação — "não colocar todos os ovos na mesma cesta" — era inconsistente com a teoria de maximização de valor presente de Williams (MARKOWITZ, 1958). Para racionalizar a diversificação, era necessário introduzir uma segunda dimensão na função objetivo do investidor: o risco. A diversificação só faz sentido se o investidor estiver disposto a sacrificar uma parcela do retorno potencial para reduzir a incerteza do resultado final. Essa percepção marcou a transição da análise de títulos (*Security Analysis*) para a análise de portfólios (*Portfolio Analysis*), onde a unidade de análise deixa de ser a firma individual e passa a ser a carteira agregada (MARKOWITZ, 1958).

## A Revolução de Markowitz: O Modelo Média-Variância

A formalização matemática dessa nova perspectiva ocorreu com a publicação do artigo "Portfolio Selection" no *Journal of Finance* em 1952, expandido posteriormente na monografia *Portfolio Selection: Efficient Diversification of Investments* (1959) (MARKOWITZ, 1959). A "Modern Portfolio Theory" (MPT) de Markowitz não apenas descreveu como os investidores agem, mas prescreveu como deveriam agir, fundamentando a decisão de investimento na interação estocástica entre ativos (MARKOWITZ, 1959).

### A Rejeição da Maximização Pura do Retorno

A premissa fundadora da MPT é que os investidores são, simultaneamente, maximizadores de retorno e avessos ao risco (MARKOWITZ, 1959). Markowitz rejeitou a hipótese de que os investidores consideram apenas o valor esperado (média) dos retornos futuros. Se os investidores focassem apenas na média, o conceito de um portfólio diversificado seria teoricamente injustificável, pois a diversificação quase sempre reduz o retorno esperado em comparação com a concentração no ativo de melhor desempenho (MARKOWITZ, 1952).
Portanto, a função de utilidade do investidor deve depender de dois parâmetros:
**Retorno Esperado (****µ****):** O valor médio ponderado das probabilidades dos retornos futuros.
**Risco (****σ****):** A dispersão ou incerteza desses retornos em torno da média.
A MPT postula que, para qualquer nível dado de risco, o investidor prefere o maior retorno possível; e para qualquer nível dado de retorno, prefere o menor risco possível. Essa estrutura de preferências cria um *trade-off* inevitável, substituindo a busca pelo "melhor ativo" pela construção do "melhor portfólio" (MARKOWITZ, 1952).

### O Conceito de Risco como Variância: Uma Escolha Pragmática

Em sua obra de 1959, Markowitz dedicou um capítulo para discutir uma medida alternativa de risco: a **semivariância** (ESTRADA, 2007). A semivariância mensura apenas a dispersão dos retornos que caem abaixo de um determinado alvo (como a média ou zero), ignorando a volatilidade "positiva" (ganhos acima do esperado) " (MARKOWITZ, 1959). Markowitz reconheceu explicitamente a superioridade teórica desta medida, afirmando que "a semivariância parece mais plausível do que a variância como uma medida de risco, uma vez que se preocupa apenas com desvios adversos" (MARKOWITZ, 1990). Investidores racionais não temem ganhos inesperados; eles temem perdas.
No entanto, Markowitz optou pela variância baseada em critérios de "custo, conveniência e familiaridade" (ESTRADA, 2007).
**Custo Computacional:** Na era dos mainframes primitivos e cartões perfurados, o custo de computação era uma barreira formidável. A otimização baseada na variância envolvia álgebra linear padrão e inversão de matrizes covariância, operações para as quais existiam algoritmos eficientes (como o *Critical Line Algorithm* desenvolvido pelo próprio Markowitz) (MARKOWITZ, STARER, FRAM, GERBER, 2019 ). A semivariância, por outro lado, exigia o dobro de dados de entrada (matrizes de semicovariância) e resultava em problemas de otimização mais complexos, onde a matriz de covariância se tornava endógena aos pesos do portfólio (ESTRADA, 2007).
**Convenência Analítica:** Se os retornos dos ativos seguirem uma distribuição normal (simétrica), a média e a variância são estatísticas suficientes para descrever toda a distribuição. Nesse caso específico, minimizar a variância é matematicamente equivalente a minimizar a semivariância (ESTRADA, 2007). Markowitz apostou na aproximação normal como uma simplificação aceitável para tornar a teoria operacionalizável.
Apesar de Markowitz ter sugerido que a semivariância seria preferível com o aumento do poder computacional, a variância entrincheirou-se como o padrão da indústria, moldando décadas de teoria financeira, desde o Índice de Sharpe até o modelo Black-Scholes (ESTRADA, 2007).

## Risco, Retorno e Covariância: A Matemática da Diversificação

A contribuição técnica mais duradoura de Markowitz foi a formulação estatística do risco do portfólio, demonstrando que o risco de um todo não é meramente a soma dos riscos das partes.


## Retorno Esperado do Portfólio


O retorno esperado de um portfólio  é uma função linear simples dos ativos que o compõem. É a média ponderada dos retornos esperados individuais , onde os pesos  representam a fração do capital alocada em cada ativo:


Esta linearidade implica que a diversificação não altera o potencial de retorno médio do portfólio; ela apenas dilui os retornos extremos dos ativos individuais.5


## Variância e Covariância
Diferentemente do retorno, a variância do portfólio   não é linear. Ela depende crucialmente das **covariâncias** entre os ativos, capturando como os preços dos ativos se movem uns em relação aos outros. A fórmula da variância para um portfólio de  ativos é:


Ou, em notação matricial,   , onde  é a matriz de covariância (KIM, BOYD, 2007).
Markowitz demonstrou a "Lei da Covariância Média": à medida que o número de ativos  em um portfólio igualmente ponderado aumenta, a contribuição das variâncias individuais  para o risco total tende a zero, enquanto a contribuição das covariâncias  domina (MARKOWITZ, 1999). No limite, o risco de um portfólio diversificado é determinado quase inteiramente pela covariância média entre os ativos, e não pela volatilidade individual de cada um (MARKOWITZ, 1959).


## O Papel da Correlação
A covariância  é o produto da correlação e dos desvios padrão . O coeficiente de correlação, variando entre -1 e +1, é o "motor" da diversificação:
**Correlação Perfeita (+1):** O risco do portfólio é a média ponderada dos riscos individuais. Não há benefício de diversificação.
**Correlação Inferior a 1:** O risco do portfólio será sempre menor que a média ponderada dos riscos individuais. A volatilidade idiossincrática é cancelada(HEBNER, 2022) .
**Correlação Negativa (-1):** Permite, teoricamente, a construção de um portfólio com variância zero (hedge perfeito).
A intuição de Markowitz foi quantificar que, ao combinar ativos com correlação imperfeita, o investidor reduz a exposição a riscos específicos (choques que afetam apenas uma empresa), mantendo apenas a exposição aos riscos comuns que afetam todo o sistema (MARKOWITZ, 1959).

## . A Fronteira Eficiente: Otimização e Geometria
## 
A aplicação dos princípios de média-variância a um universo de ativos resulta na construção da Fronteira Eficiente, o conjunto de todos os portfólios ótimos que dominam as demais alternativas.

## Derivação e Definição

A Fronteira Eficiente é o lugar geométrico no espaço risco-retorno que representa os portfólios que oferecem o retorno máximo para um dado nível de risco (ou risco mínimo para um dado retorno) (MARKOWITZ, 1959). Ela é obtida resolvendo um problema de otimização quadrática convexa (GUNDERSEN, 2022).


A forma geométrica exata desta fronteira depende criticamente das restrições impostas aos pesos :
**Sem Restrições a Vendas a Descoberto (Unconstrained/Short Selling Allowed):** Se o investidor pode vender a descoberto (assumir pesos negativos) ilimitadamente, a fronteira eficiente é uma **hipérbole** perfeita e suave no espaço média-desvio padrão (GUNDERSEN, 2022). O ramo superior desta hipérbole (acima do vértice) é a fronteira eficiente propriamente dita.
**Com Restrições a Vendas a Descoberto (No Short Selling Constraint):** Quando impomos a restrição de não-negatividade , a fronteira deixa de ser uma hipérbole única e torna-se uma curva convexa composta por uma série de **segmentos de hipérbole conectados** (*piecewise hyperbolic segments*) (GUNDERSEN, 2022).
*Mecanismo:* A transição de um segmento hiperbólico para outro ocorre nos "corner portfolios" (portfólios de canto). À medida que nos movemos ao longo da fronteira (aumentando o retorno esperado), a composição do portfólio muda. Quando o peso de um ativo atinge zero (sai do portfólio) ou quando um novo ativo entra no portfólio (peso torna-se positivo), a equação algébrica que descreve a curva muda, criando um "ponto de solda" entre dois arcos hiperbólicos distintos (QI, 2019).
*Implicação:* A fronteira com restrições é finita, começando no portfólio de mínima variância global e terminando no ativo individual de maior retorno (e risco), ao contrário da fronteira sem restrições que se estende ao infinito através da alavancagem de posições vendidas (GUNDERSEN, 2022).27
O algoritmo desenvolvido por Markowitz para traçar essa fronteira complexa com restrições de desigualdade é o **Critical Line Algorithm (CLA)**, um método de otimização quadrática paramétrica que precede e inspira os modernos solvers de programação quadrática (MARKOWITZ, STARER, FRAM, GERBER, 2019).

## O Portfólio de Mínima Variância Global
## 

O vértice da fronteira (seja ela hiperbólica ou segmentada) é o Portfólio de Mínima Variância Global (GMV). Este é o único ponto na curva onde o risco é minimizado em termos absolutos, sem consideração pelo retorno (KIM, BOYD, 2007). Em teoria, nenhum investidor racional avesso ao risco escolheria um portfólio localizado na parte "inferior" da fronteira (abaixo do GMV), pois para cada ponto nessa região existe um portfólio na parte superior com o mesmo risco, mas com retorno estritamente maior (dominância média-variância) (GUNDERSEN, 2022).

### O Ativo Livre de Risco e o Teorema da Separação
## 
## 
A introdução de um ativo livre de risco (*risk-free asset*) expande o conjunto de oportunidades do investidor além da fronteira de ativos de risco, alterando a geometria da escolha ótima e levando ao Teorema da Separação de Tobin.

### O Ativo Livre de Risco

Um ativo livre de risco é definido idealmente como um investimento com variância zero  e, consequentemente, covariância zero com todos os ativos de risco .34 Na prática financeira, títulos governamentais de curto prazo, como as *Treasury Bills* dos EUA, são utilizados como *proxies*, assumindo-se ausência de risco de crédito e risco de reinvestimento negligenciável para o horizonte de um período (ROHATGI, 2011).
A inclusão deste ativo permite duas novas operações financeiras fundamentais:
**Empréstimo Livre de Risco (Lending):** O investidor pode aplicar parte de sua riqueza no ativo livre de risco, reduzindo a exposição total ao risco do mercado.
**Tomada de Empréstimo Livre de Risco (Borrowing/Leverage):** O investidor pode tomar dinheiro emprestado à taxa livre de risco para alavancar sua posição nos ativos de risco.37

## O Teorema da Separação de Tobin


James Tobin, em seu artigo seminal de 1958 *Liquidity Preference as Behavior Towards Risk*, formalizou o impacto do ativo livre de risco na teoria da escolha de portfólio.39 Tobin demonstrou que, na presença de um ativo livre de risco, o processo de decisão de investimento pode ser decomposto em duas etapas distintas e independentes — um resultado conhecido como o **Teorema da Separação** (ou *Two-Fund Separation Theorem*) (BUITER, 2003).
**Etapa 1: A Decisão Técnica (Seleção do Portfólio Ótimo de Risco).** O investidor deve primeiro identificar o portfólio de ativos de risco que maximiza o retorno por unidade de risco. Geometricamente, este é o **Portfólio de Tangência** (Tangency Portfolio), o ponto onde uma linha reta partindo da taxa livre de risco   tangencia a fronteira eficiente hiperbólica dos ativos de risco (GUNDERSEN, 2022). A composição deste portfólio é puramente técnica e objetiva, dependendo apenas das estimativas de médias, variâncias e covariâncias; ela é *independente* das preferências de risco do investidor individual.37
**Etapa 2: A Decisão Pessoal (Alocação de Capital).** Uma vez identificado o Portfólio de Tangência, o investidor decide como alocar sua riqueza total entre este portfólio e o ativo livre de risco. Esta decisão depende inteiramente da função de utilidade (aversão ao risco) do indivíduo.37

## A Reta do Mercado de Capitais (Capital Market Line - CML)

A combinação linear do ativo livre de risco com o Portfólio de Tangência gera a **Reta do Mercado de Capitais** (Capital Market Line - CML). A CML torna-se a *nova* fronteira eficiente, pois domina qualquer portfólio situado na fronteira original de ativos de risco (a hipérbole fica inteiramente abaixo da reta CML, exceto no ponto de tangência).37
O posicionamento do investidor ao longo da CML é determinado pelo mecanismo de alavancagem:
**Investidores Conservadores (Lending Portfolios):** Localizam-se à esquerda do ponto de tangência . Eles investem uma fração positiva de sua riqueza no ativo livre de risco e o restante no portfólio . O risco total do portfólio é menor que o risco de .37
**Investidores Agressivos (Borrowing Portfolios):** Localizam-se à direita do ponto de tangência . Eles tomam empréstimos à taxa  para investir mais de 100% de seu capital próprio no portfólio  ampliando tanto o retorno esperado quanto a volatilidade.37
A equação que descreve a CML é:


Onde a inclinação (slope) da reta, , representa o "preço de mercado do risco" — o retorno adicional que o mercado exige para aceitar uma unidade adicional de desvio padrão.44

**Considerações sobre Taxas de Empréstimo Diferenciadas:** Na realidade, investidores raramente conseguem tomar empréstimos à mesma taxa livre de risco que o governo . Nesse cenário, a CML deixa de ser uma linha reta única e torna-se uma fronteira "quebrada" ou côncava: um segmento linear parte de  até um ponto de tangência, segue-se um segmento curvo da fronteira eficiente original (onde o investidor não empresta nem toma emprestado), e então um novo segmento linear parte de outro ponto de tangência com inclinação menor, baseada na taxa de empréstimo mais alta.41

## Avaliação de Desempenho: O Índice de Sharpe

A geometria da CML forneceu a base direta para uma das métricas mais onipresentes na avaliação de investimentos: o Índice de Sharpe. Introduzido por William Sharpe em 1966 como "Reward-to-Variability Ratio", o índice operacionaliza o conceito de eficiência média-variância.49

## Definição e Interpretação

O Índice de Sharpe  quantifica o excesso de retorno por unidade de risco total. Matematicamente:


Geometricamente, o Índice de Sharpe de um portfólio é a inclinação da linha que conecta a taxa livre de risco a esse portfólio no gráfico média-desvio padrão (GUNDERSEN, 2022). Quanto maior a inclinação, melhor o desempenho ajustado ao risco.

## Importância e Aplicação

A maximização do Índice de Sharpe é equivalente a encontrar o Portfólio de Tangência na MPT. Em um mercado em equilíbrio, o portfólio de mercado  deve ser aquele com o maior Índice de Sharpe possível (GUIDOLIN, 2017). A métrica permite comparar fundos e estratégias heterogêneas, nivelando o campo de jogo ao penalizar a volatilidade. No entanto, o índice herda as limitações da variância: se os retornos não forem normais (ex: fundos de hedge com estratégias de opções), o Índice de Sharpe pode ser enganoso, penalizando a volatilidade positiva ou subestimando riscos de cauda, o que levou ao desenvolvimento de métricas alternativas como o **Índice de Sortino** (baseado na semivariância/downside deviation) (DUBRA, MACCHERONI, 2004).


## O Modelo de Precificação de Ativos de Capital (CAPM)


Enquanto a MPT de Markowitz é normativa (diz ao investidor como construir um portfólio), o *Capital Asset Pricing Model* (CAPM) é positivo (explica como os preços dos ativos são determinados se todos seguirem a MPT).

## Origem e Desenvolvedores

O CAPM foi desenvolvido independentemente na primeira metade da década de 1960 por William Sharpe (1964), John Lintner (1965), Jan Mossin (1966) e Jack Treynor (1961/1962) (FAMA, FRENCH, 2004). A unificação dessas teorias rendeu a Sharpe, Markowitz e Merton Miller o Prêmio Nobel de Economia em 1990 (garvin, 2013). A intuição central é que, se todos os investidores são racionais, possuem expectativas homogêneas e otimizam seus portfólios segundo a média-variância (usando o Teorema da Separação de Tobin), então todos demandarão o mesmo portfólio de ativos de risco: o **Portfólio de Mercado** . Para que o mercado "limpe" (oferta iguale demanda), os preços dos ativos devem se ajustar até que o portfólio de tangência seja, de fato, o portfólio de mercado ponderado por valor (FAMA, FRENCH, 2004).

## Decomposição do Risco: Sistemático vs. Não Sistemático

O CAPM introduz uma distinção fundamental na natureza do risco, decompondo a variância total de um ativo  em dois componentes (ROSS, WESTERFIELD, JORDAN, 2010):
**Risco Sistemático (Risco de Mercado):** É a parcela da volatilidade do ativo que está correlacionada com os movimentos do mercado como um todo. Origina-se de fatores macroeconômicos inelutáveis — inflação, juros, ciclos econômicos, guerras — que afetam todas as empresas simultaneamente. Este risco *não pode* ser eliminado pela diversificação.
**Risco Não Sistemático (Idiossincrático/Específico):** É a parcela da volatilidade exclusiva da empresa ou setor (ex: sucesso de um novo produto, greve na fábrica, fraude contábil). Como esses eventos são estatisticamente independentes entre empresas, em um portfólio amplo eles tendem a se cancelar mutuamente (lei dos grandes números).
A conclusão revolucionária do CAPM é que **o mercado não remunera o risco não sistemático**. Como ele pode ser eliminado gratuitamente através da diversificação, os investidores não devem esperar nenhum prêmio de retorno por assumi-lo. O único risco que justifica um retorno esperado acima da taxa livre de risco é o risco sistemático (ROSS, WESTERFIELD, JORDAN, 2010).

### O Coeficiente Beta e a Reta do Mercado de Títulos (SML)

Para mensurar o risco sistemático, o CAPM utiliza o coeficiente **Beta** . O Beta é uma medida padronizada da covariância do ativo com o mercado, definida como:


- Se *β*>1: O ativo tem um risco sistemático superior ao mercado (mais volátil).
- Se *β*<1: O ativo tem um risco sistemático inferior ao mercado (menos volátil).

Um ativo com  move-se, em média, na mesma proporção que o mercado. Um ativo com  amplifica os movimentos do mercado (mais risco sistemático), enquanto  os atenua.

- A Reta do Mercado de Títulos (SML)
- 
- A equação do CAPM define uma relação linear entre o retorno esperado e o Beta, e essa relação é representada graficamente pela **Security Market ****Line**** (SML)**, ou **Linha do Mercado de Títulos (LMT)**. O CAPM estabelece que o retorno esperado do ativo () é dado pela equação da SML:
- 
- 
- A SML é crucial porque todo ativo individual, ou portfólio eficiente e não eficiente, deve se situar sobre ela em um mercado de equilíbrio

- **Diferença entre CML e SML:**

A distinção fundamental entre a CML e a SML reside na medida de risco utilizada.
- **CML (Capital Market ****Line****): **É a fronteira eficiente que relaciona o retorno esperado com o **Risco Total **(medido pelo desvio-padrão, *σ*). O Índice de Sharpe avalia o prêmio de risco por unidade de risco total (medido ao longo da CML).
- **SML (Security Market ****Line****):** Relaciona o retorno esperado com o **Risco Sistemático **(medido pelo Beta, *β*). O CAPM demonstra que os investidores são compensados apenas pelo risco sistemático, pois o risco não sistemático pode ser eliminado pela diversificação.

**Tabela 1: Comparação entre Capital Market Line (CML) e Security Market Line (SML)**

| Característica | Capital Market Line (CML) | Security Market Line (SML) |
| --- | --- | --- |
| Medida de Risco | Desvio Padrão Total | Beta Sistemático |
| Aplicação | Apenas Portfólios Eficientes | Qualquer Ativo Individual ou Portfólio |
| Definição de Risco | Risco Total (Sistemático + Idiossincrático) | Apenas Risco Sistemático (Covariância com Mercado) |
| Ponto de Intercepto | Taxa Livre de Risco | Taxa Livre de Risco |
| Inclinação (Slope) | Índice de Sharpe do Mercado | Prêmio de Risco de Mercado |
| Fundamentação | Teorema da Separação de Tobin | Modelo de Equilíbrio de Mercado (CAPM) |

Fonte: Elaboração própria com base em (BOASSON, BOASSON, ZHOU).

- **Pressupostos, Críticas e Limitações Teóricas**
- 

A elegância matemática da MPT e do CAPM repousa sobre um conjunto de axiomas sobre o comportamento humano e a estrutura dos mercados. A validade desses modelos depende, portanto, da robustez de seus pressupostos.

- Pressupostos Fundamentais: A Racionalidade VNM

A teoria assume que os investidores são agentes perfeitamente racionais que tomam decisões sob incerteza maximizando a Utilidade Esperada, conforme axiomatizado por John von Neumann e Oskar Morgenstern (VNM) em *Theory of Games and Economic Behavior* (1944).63 Para que uma função de utilidade esperada exista e represente as preferências do investidor, cinco axiomas fundamentais devem ser satisfeitos 63:
**Completude (Completeness):** O investidor tem preferências bem definidas. Para quaisquer duas loterias (investimentos) A e B, ele pode afirmar se prefere A a B ($A \succ B$), B a A ($B \succ A$) ou se é indiferente ($A \sim B$). A indecisão não é permitida.63
**Transitividade (Transitivity):** As preferências são consistentes. Se $A \succ B$ e $B \succ C$, então logicamente $A \succ C$. A violação deste axioma implicaria comportamento cíclico e irracional ("money pump").49
**Continuidade (Continuity):** Também conhecido como axioma de Arquimedes. Se $A \succ B \succ C$, existe uma probabilidade $p$ tal que o investidor é indiferente entre receber B com certeza ou uma loteria que paga A com probabilidade $p$ e C com probabilidade $1-p$. Isso impede que qualquer resultado seja infinitamente desejável ou indesejável (como o paraíso ou a morte) a ponto de ignorar probabilidades.49
**Independência (Independence):** A preferência entre duas opções não deve ser alterada pela introdução de uma terceira opção comum a ambas. Se $A \succ B$, então uma mistura de A com C deve ser preferida à mesma mistura de B com C. Este é o axioma mais controverso e frequentemente violado em testes empíricos (ex: Paradoxo de Allais).49
**Dominância (Dominance/Monotonicity):** Se uma opção A oferece resultados melhores que B em pelo menos um estado da natureza e resultados iguais ou melhores em todos os outros estados, então A deve ser estritamente preferida a B. Este axioma encapsula a ideia racional de que "mais é melhor que menos" e violações a ele (como escolher uma opção dominada estocasticamente) são consideradas erros graves de decisão.65
**Tabela 2: Axiomas da Teoria da Utilidade Esperada (VNM)**

| Axioma | Definição Simplificada | Implicação Financeira |
| --- | --- | --- |
| Completude | Capacidade de ranquear qualquer par de ativos. | O mercado pode precificar todos os ativos. |
| Transitividade | Consistência lógica ($A>B, B>C \Rightarrow A>C$). | Evita arbitragem cíclica irracional. |
| Continuidade | Existência de "pontos de indiferença" probabilísticos. | Permite modelar o trade-off risco-retorno de forma contínua. |
| Independência | Preferências não mudam com opções irrelevantes. | A diversificação é consistente independentemente do resto da carteira. |
| Dominância | Preferência por "mais riqueza" e "menos risco". | Fundamenta a fronteira eficiente (ninguém escolhe portfólios dominados). |

Fonte: Elaboração própria baseada em.65

- Limitações e a Realidade dos Mercados
- 
As críticas à MPT e ao CAPM surgem da desconexão entre esses axiomas ideais e a realidade empírica dos mercados financeiros.
**Distribuições Não-Normais (Caudas Gordas):** A MPT assume que os retornos seguem uma distribuição Normal (Gaussiana), o que justifica o uso da variância como medida completa de risco. Contudo, estudos seminais de Benoit Mandelbrot (1963) e Eugene Fama (1965) demonstraram que os preços de ativos exibem "caudas gordas" (*fat tails*) e leptocurtose excessiva.76 Na realidade, eventos extremos (como *crashes* de mercado de 10 ou 20 desvios padrão) ocorrem com frequência muito maior do que a prevista pela curva normal. O uso da variância subestima drasticamente o risco real de eventos catastróficos ("Cisnes Negros"), tornando a MPT perigosa em momentos de crise.78
**Limitações da Variância:** Como discutido na seção 2.2, a variância penaliza igualmente a volatilidade para cima (lucro) e para baixo (perda). Investidores reais, no entanto, exibem aversão à perda, não à volatilidade *per se*. A semivariância ou métricas de *downside risk* seriam descritores mais precisos da utilidade do investidor, mas a inércia da tradição MPT mantém a variância como padrão.12
**Violações da Racionalidade:** A Economia Comportamental (Kahneman e Tversky) documentou sistemáticas violações dos axiomas VNM. O "efeito certeza" e a "aversão à perda" (Teoria da Perspectiva) mostram que investidores reais frequentemente violam os axiomas de Independência e Dominância, comportando-se de maneira inconsistente com a maximização da utilidade esperada.80
Apesar dessas falhas descritivas, a estrutura criada por Markowitz, Tobin e Sharpe permanece a *lingua franca* das finanças. Conceitos como diversificação, fronteira eficiente, Beta e Índice de Sharpe fornecem as ferramentas heurísticas indispensáveis para a alocação de ativos institucional, servindo como um modelo normativo de como o mercado *deveria* funcionar sob condições ideais, mesmo que a realidade frequentemente divirja do modelo.
### 

- **Capítulo 2: A Teoria Pós-Moderna do Portfólio (PMPT) e a Gestão de Risco Assimétrica**

- A Insuficiência da Variância e a Gênese da PMPT

Embora a Teoria Moderna do Portfólio (MPT), estabelecida por Markowitz (1952), tenha revolucionado as finanças ao quantificar a diversificação, sua dependência da variância como única medida de risco impõe limitações severas em mercados reais. A MPT assume implicitamente que os retornos dos ativos seguem uma distribuição normal (Gaussiana) e que a função de utilidade do investidor é quadrática. Contudo, evidências empíricas robustas demonstram que os retornos financeiros, especialmente em mercados emergentes como o brasileiro, apresentam distribuições leptocúrticas (caudas pesadas) e assimetria negativa 
Neste contexto, a variância falha por ser uma medida simétrica: ela penaliza os desvios positivos (ganhos acima da média) com a mesma severidade que os desvios negativos (perdas) (NAWROCKI, 1999). A Teoria Pós-Moderna do Portfólio (PMPT) surge, portanto, como uma evolução necessária, fundamentada na premissa de que o risco deve ser tratado como a possibilidade de não atingir um retorno mínimo aceitável (Target Minimum Return), focando exclusivamente no *downside risk*. 
A formalização da PMPT é creditada a Rom e Ferguson (1993, 1994), que identificaram falhas críticas nos softwares de otimização baseados na MPT e propuseram uma estrutura que incorpora a assimetria das distribuições. Paralelamente, o *Pension Research Institute*, através de pesquisadores como Frank Sortino, operacionalizou a teoria dos Momentos Parciais Inferiores (LPM - *Lower Partial Moments*), desenvolvendo métricas como o Índice de Sortino, que ajusta o retorno pelo risco de *downside* em vez do desvio padrão total.

- Métricas de Risco: Do VaR às Medidas Coerentes

Para operacionalizar a PMPT em modelos de otimização, é necessário definir métricas que capturem o risco de cauda. O Value at Risk (VaR), popularizado na década de 1990, tornou-se um padrão regulatório. O VaR estima a perda máxima esperada para um determinado nível de confiança e horizonte de tempo. No entanto, o VaR possui limitações teóricas graves para a otimização de portfólios: ele não é uma medida subaditiva, o que significa que, em certas condições, o VaR de uma carteira diversificada pode ser maior que a soma dos VaRs individuais dos ativos, violando o princípio da diversificação.
Em resposta, Artzner et al. (1999) estabeleceram os axiomas que definem uma Medida de Risco Coerente: monotonicidade, subaditividade, homogeneidade positiva e invariância à translação. Com base nesses axiomas, o Conditional Value at Risk (CVaR), também conhecido como Expected Shortfall (ES), emergiu como a métrica superior.
O CVaR mede a perda esperada dado que a perda excedeu o limite do VaR, capturando a severidade dos eventos extremos na cauda esquerda da distribuição. Diferentemente do VaR, o CVaR é uma medida coerente e convexa, o que permite sua minimização eficiente através de técnicas de programação linear, conforme demonstrado por Rockafellar e Uryasev (2000, 2002).

- Métricas de Risco: Do VaR às Medidas Coerentes

A transição da MPT para a PMPT no contexto deste trabalho implica a substituição da função objetivo do otimizador. Enquanto o modelo clássico de Markowitz minimiza a variância , o modelo Pós-Moderno aqui proposto busca minimizar o CVaR para um dado nível de retorno.
A formulação do problema de otimização de Média-CVaR pode ser descrita como a busca pelos pesos (w) que minimizam as perdas extremas ponderadas pela distribuição de probabilidade dos retornos, sujeitos às restrições de alocação. Estudos empíricos no mercado brasileiro indicam que carteiras otimizadas por Média-CVaR tendem a apresentar melhor desempenho ajustado ao risco e maior proteção contra drawdowns em períodos de crise, comparativamente às carteiras de Média-Variância, devido à sua sensibilidade aos momentos de ordem superior (assimetria e curtose).
Portanto, ao comparar carteiras geradas por diferentes otimizadores, espera-se que o otimizador PMPT (Mínimo-CVaR) gere alocações mais defensivas e robustas a eventos de cauda, refletindo de forma mais fidedigna a aversão à perda descrita pelas Finanças Comportamentais


- **Desconstrução Crítica da MPT: As Falácias da Normalidade e da Utilidade Quadrática**

A resiliência da MPT no meio acadêmico e profissional, apesar de suas limitações conhecidas, deve-se à sua simplicidade pedagógica. No entanto, a aplicação da MPT em mercados reais exige a aceitação de pressupostos que, quando violados, podem levar a alocações de ativos subótimas e a uma subestimação perigosa dos riscos extremos. A PMPT surge como uma resposta direta a duas críticas estruturais à MPT: a suposição de distribuição normal dos retornos e a função de utilidade quadrática do investidor.

- A Tirania da Curva de Sino: Caudas Gordas e Assimetria

A MPT assume que os retornos dos ativos financeiros são variáveis aleatórias independentes e identicamente distribuídas (i.i.d.) que seguem uma distribuição normal (Gaussiana). Esta suposição é conveniente porque uma distribuição normal é perfeitamente descrita por apenas dois parâmetros: média ($\mu$) e desvio padrão ($\sigma$). Sob esta ótica, a probabilidade de eventos extremos diminui exponencialmente à medida que nos afastamos da média.8
No entanto, evidências empíricas exaustivas demonstram que as séries temporais financeiras exibem características que violam sistematicamente a normalidade:
**Leptocurtose**** (Caudas Gordas):** Os mercados financeiros apresentam uma frequência de eventos extremos (tanto positivos quanto negativos) significativamente maior do que a prevista pela distribuição normal. Eventos de "seis sigmas" ($6\sigma$), que teoricamente deveriam ocorrer uma vez a cada milhões de anos, ocorrem com uma regularidade alarmante em crises financeiras.21
**Assimetria (****Skewness****):** Os retornos não são simétricos. Em mercados de ações, por exemplo, observa-se frequentemente uma assimetria negativa, onde as quedas são mais abruptas e profundas do que as altas.23
Implicação para a Gestão de Portfólio:
Ao utilizar o desvio padrão como medida de risco, a MPT falha em distinguir entre a volatilidade gerada por "saltos" positivos e a volatilidade gerada por "crashes". Mais grave ainda, a MPT subestima o risco de cauda. Um fundo de hedge que opera estratégias de venda de opções fora do dinheiro pode apresentar um desvio padrão baixo e um Índice de Sharpe alto durante longos períodos de calmaria, ocultando um risco latente de ruína que só é capturado por métricas que consideram a curtose e a assimetria, como preconizado pela PMPT.23 A PMPT, ao não assumir normalidade, permite o uso de distribuições mais flexíveis ou métodos não paramétricos que capturam a verdadeira natureza do risco de cauda.16

**2.2.2 A Função de Utilidade e a Teoria da Perspectiva**

A MPT baseia-se na Teoria da Utilidade Esperada, assumindo implicitamente que a função de utilidade do investidor é quadrática. Matematicamente, isso implica que o investidor penaliza desvios positivos e negativos da média com a mesma intensidade. Em termos práticos, sob a MPT, um retorno excepcionalmente alto é tão indesejável quanto um retorno excepcionalmente baixo, pois ambos aumentam a variância do portfólio.4
Esta premissa entra em conflito direto com as descobertas das Finanças Comportamentais, especificamente a **Teoria da Perspectiva (Prospect ****Theory****)** desenvolvida por Daniel Kahneman e Amos Tversky. A Teoria da Perspectiva demonstra que os investidores exibem **aversão à perda** (*loss* *aversion*) em vez de aversão ao risco (*risk* *aversion*).27
**Aversão à Perda:** A dor psicológica de perder $100 é aproximadamente duas vezes mais intensa do que o prazer de ganhar $100.
**Ponto de Referência:** Os investidores avaliam o desempenho não em relação à média do portfólio, mas em relação a um ponto de referência ou alvo (*target **return*). Retornos acima do alvo são vistos como "ganhos" e retornos abaixo como "perdas".28
A PMPT operacionaliza a Teoria da Perspectiva ao substituir a média pelo **Retorno Mínimo Aceitável (MAR)** e a variância pelo risco de *downside*. Dessa forma, a PMPT alinha a matemática da otimização de portfólio com a psicologia real do investidor: minimizando a probabilidade e a magnitude de falhar em atingir os objetivos financeiros, enquanto deixa o *upside* livre para capturar retornos excessivos.5
**Tabela 2.1: Comparação Estrutural: MPT vs. PMPT**

| Dimensão Analítica | Moderna Teoria do Portfólio (MPT) | Teoria Pós-Moderna do Portfólio (PMPT) |
| --- | --- | --- |
| Medida de Risco Central | Variância / Desvio Padrão ($\sigma^2, \sigma$) | Downside Deviation / LPM / CVaR |
| Distribuição de Retornos | Normal (Simétrica, Paramétrica) | Qualquer (Não-Normal, Assimétrica, Empírica) |
| Definição de Risco | Dispersão em torno da média (Incerteza Total) | Fracasso em atingir o Retorno Mínimo (MAR) |
| Visão do Investidor | Avesso à variância (Quadrática) | Avesso à perda (Loss Aversion - Prospect Theory) |
| Tratamento do Upside | Penalizado como risco (aumenta $\sigma$) | Ignorado ou valorizado (Upside Potential) |
| Objetivo da Otimização | Maximizar Retorno para dado $\sigma$ | Maximizar Retorno para dado Downside Risk |

Fonte: Elaboração baseada em.4

**2.3 Conceitos Fundamentais de '****Downside**** Risk': A Estrutura dos Momentos Parciais Inferiores (LPM)**

Para superar as limitações da variância, a PMPT adota a estrutura matemática dos Momentos Parciais Inferiores (*Lower **Partial* *Moments* - LPM). Desenvolvida teoricamente por Bawa (1975) e expandida por Fishburn (1977), a família de métricas LPM oferece uma generalização flexível para mensurar o risco abaixo de um limiar específico.31 A elegância dos LPMs reside na sua capacidade de incorporar diferentes graus de aversão ao risco através de um único parâmetro, $n$ (a ordem do momento).

**2.3.1 Definição Matemática dos ****LPMs**

Seja $R$ a variável aleatória que representa os retornos do ativo e $\tau$ (tau) o Retorno Mínimo Aceitável (MAR) ou *target **return*. O LPM de ordem $n$ é definido pela integral:

$$LPM_n(\tau) = \int_{-\infty}^{\tau} (\tau - r)^n f(r) \, dr$$
No caso discreto, onde temos uma série temporal de $T$ observações de retorno ($R_1, R_2,..., R_T$), a fórmula torna-se:

$$LPM_n(\tau) = \frac{1}{T} \sum_{t=1}^{T} \max(0, \tau - R_t)^n$$
Nesta formulação, apenas os retornos que ficam abaixo do alvo $\tau$ contribuem para a medida de risco. A função $\max(0, \tau - R_t)$ atua como um filtro, zerando qualquer contribuição de retornos positivos (acima do alvo), o que reflete matematicamente a premissa de que o *upside* não é risco.33

**2.3.2 A Hierarquia dos Graus de LPM e suas Interpretações**

A escolha do grau $n$ permite ajustar a métrica à psicologia do investidor, ponderando a severidade das perdas de maneira distinta 33:
**LPM de Ordem 0 ($n=0$) – Probabilidade de Perda (****Safety** **First****):**
Mede a frequência com que o retorno cai abaixo do alvo.
Matematicamente, equivale a $P(R < \tau)$.
*Interpretação:* Responde à pergunta "Qual a chance de eu perder dinheiro?". No entanto, falha em distinguir entre uma perda pequena e uma perda catastrófica (uma perda de 1% conta o mesmo que uma de 50%).15
**LPM de Ordem 1 ($n=1$) – Déficit Esperado (*****Target ******Shortfall*****):**
Mede a magnitude média das perdas. Os desvios abaixo do alvo são ponderados linearmente.
*Interpretação:* Responde à pergunta "Se eu perder dinheiro, quanto espero perder em média?". É a medida de risco fundamental para o cálculo do Índice Omega (discutido na Seção 2.5) e reflete um investidor neutro ao risco em relação à severidade da perda, desde que a média seja controlada.33
**LPM de Ordem 2 ($n=2$) – ****Semivariância**** (*****Target ******Semivariance*****):**
Mede a dispersão quadrática dos retornos abaixo do alvo. Semelhante à variância, mas unilateral.
*Interpretação:* Penaliza desproporcionalmente as grandes perdas. Uma perda duas vezes maior pesa quatro vezes mais no cálculo do risco. Esta é a medida preferida por Markowitz (1959) e a base para o **Desvio Padrão de ****Downside** ($Downside Deviation = \sqrt{LPM_2}$), que é o denominador do Índice de Sortino.10
**LPM de Ordens Superiores ($n > 2$):**
Refletem uma aversão extrema a perdas catastróficas. À medida que $n$ aumenta, o foco da métrica desloca-se quase exclusivamente para a cauda esquerda extrema da distribuição, ignorando pequenas flutuações negativas.41

**2.3.3 ****Semivariância**** vs. Variância: O Impacto na Alocação**

A substituição da variância pela semivariância tem implicações profundas na construção de portfólios. Em distribuições simétricas (normais), a semivariância é proporcional à variância, e a fronteira eficiente da PMPT converge para a da MPT. No entanto, na presença de assimetria (skewness), as fronteiras divergem.42
Um ativo com alta assimetria positiva (como uma opção de compra longa ou uma startup de venture capital) terá uma variância alta (devido ao potencial de ganho ilimitado) mas uma semivariância baixa (perda limitada ao capital investido). A MPT penalizaria este ativo, reduzindo sua alocação para diminuir o risco total. A PMPT, utilizando a semivariância, reconheceria o perfil favorável de risco/retorno e aumentaria a alocação, capturando o "upside potential".12 Estudos empíricos mostram que, em mercados emergentes ou durante crises, portfólios otimizados via semivariância tendem a preservar capital de forma mais eficiente do que aqueles baseados em média-variância.45

**2.4 Métricas Avançadas de Risco e Propriedades de Coerência**

A evolução da gestão de riscos não parou nos LPMs. A necessidade de quantificar o capital regulatório bancário e o risco sistêmico levou ao desenvolvimento de métricas baseadas em quantis, como o *Value* *at** Risk* (VaR) e o *Expected* *Shortfall* (ES/CVaR). A análise dessas métricas sob a perspectiva da teoria axiomática de riscos revela distinções cruciais sobre sua confiabilidade.

**2.4.1 ****Value** **at**** Risk (****VaR****): A Revolução Incoerente**

Popularizado em 1994 pelo J.P. Morgan através do sistema *RiskMetrics*, o VaR tornou-se o padrão da indústria para a gestão de riscos de mercado e regulação bancária (Acordos de Basileia I e II).47 O VaR é definido como a perda máxima esperada em um determinado horizonte de tempo, com um certo nível de confiança ($1-\alpha$).
Por exemplo, um VaR de 99% de $10 milhões em 1 dia implica que há apenas 1% de chance de a perda exceder $10 milhões.
Apesar de sua ubiquidade, o VaR apresenta falhas estruturais graves sob a ótica da PMPT e da teoria estatística:
**Cegueira da Cauda (*****Tail*** ***Blindness*****):** O VaR indica o limiar da perda, mas nada diz sobre a severidade da perda caso esse limiar seja ultrapassado. Em distribuições de cauda gorda, a perda média além do VaR pode ser muitas vezes superior ao próprio VaR, ocultando riscos catastróficos.20
**Violação da Subaditividade:** Artzner et al. (1999), em seu artigo fundamental sobre medidas de risco coerentes, demonstraram que o VaR **não é subaditivo**. Isso significa que o VaR de um portfólio diversificado pode ser maior do que a soma dos VaRs dos ativos individuais ($\text{VaR}(A+B) > \text{VaR}(A) + \text{VaR}(B)$). Essa propriedade perversa desencoraja a diversificação e viola um dos princípios basilares da gestão de portfólio.50 Exemplos teóricos e práticos mostram que, em distribuições muito assimétricas ou com caudas pesadas, a fusão de riscos pode parecer aumentar o risco medido pelo VaR, uma anomalia teórica inaceitável.53

**2.4.2 Medidas de Risco Coerentes e os Axiomas de ****Artzner**

Para remediar as falhas do VaR, Artzner, Delbaen, Eber e Heath (1999) estabeleceram quatro axiomas que uma medida de risco $\rho$ deve satisfazer para ser considerada "coerente" e segura para alocação de capital 50:
**Monotonicidade****:** Se o portfólio $X$ tem retornos sempre melhores que $Y$, o risco de $X$ deve ser menor ($\text{Se } X \ge Y, \text{então } \rho(X) \le \rho(Y)$).
**Subaditividade:** O risco do todo não pode exceder a soma dos riscos das partes ($\rho(X+Y) \le \rho(X) + \rho(Y)$). Garante que a diversificação reduz o risco.
**Homogeneidade Positiva:** O risco escala linearmente com o tamanho da posição ($\rho(\lambda X) = \lambda \rho(X)$ para $\lambda > 0$).
**Invariância de Translação:** Adicionar um montante garantido de caixa $k$ reduz o risco nesse mesmo montante ($\rho(X + k) = \rho(X) - k$).

**2.4.3 Conditional Value at Risk (****CVaR****) / Expected Shortfall (ES)**

Como resposta direta à incoerência do VaR, Rockafellar e Uryasev (2000, 2002) propuseram e operacionalizaram o *Conditional* *Value* *at** Risk* (CVaR), também conhecido como *Expected* *Shortfall* (ES). O CVaR é definido como a média das perdas que ocorrem na cauda da distribuição, estritamente além do ponto de corte do VaR.56

$$CVaR_{\alpha}(X) = E$$
**Superioridade do ****CVaR**** na PMPT:**
**Coerência:** O CVaR satisfaz todos os axiomas de Artzner, incluindo a subaditividade. Ele reconhece corretamente os benefícios da diversificação mesmo em cenários de estresse extremo.26
**Convexidade e Otimização:** Diferentemente do VaR, que é uma função não-convexa e difícil de otimizar (com múltiplos mínimos locais), o CVaR é convexo. Isso permitiu a Rockafellar e Uryasev desenvolver algoritmos de programação linear que podem otimizar portfólios com milhares de ativos e cenários de forma extremamente eficiente, minimizando diretamente o risco de cauda.58
**Sensibilidade à Cauda:** O CVaR captura a forma da distribuição na região de perdas extremas. Se um ativo possui "cisnes negros" latentes, o CVaR será significativamente maior que o VaR, alertando o gestor sobre a verdadeira dimensão do risco.61
A transição regulatória global, exemplificada pela *Fundamental Review **of* *the** Trading Book* (FRTB) do Comitê de Basileia, que substituiu o VaR pelo Expected Shortfall para o cálculo de capital de risco de mercado, constitui a validação institucional definitiva dos princípios defendidos pela PMPT: o risco real reside na cauda, e métricas incoerentes são inadequadas para a segurança sistêmica.26

**2.5 Indicadores de Desempenho Ajustados: ****Sortino****, ****Omega**** e a Generalização Kappa**

A PMPT não se limita a medir o risco; ela redefine a avaliação de desempenho. O onipresente Índice de Sharpe, ao penalizar a volatilidade de alta, falha em capturar o valor gerado por gestores que produzem assimetria positiva. A PMPT propõe alternativas que integram os conceitos de *downside* *risk* e momentos superiores.

**2.5.1 O Índice de ****Sortino****: Refinando Sharpe**

Desenvolvido por Frank Sortino no início dos anos 1980 e popularizado nos anos 1990, o Índice de Sortino é a modificação mais direta e amplamente adotada do Índice de Sharpe.13 Ele substitui o desvio padrão total pelo **Desvio de ****Downside** ($TDD$ ou $\sigma_d$) no denominador.

$$\text{Sortino Ratio} = \frac{R_p - MAR}{TDD} = \frac{R_p - MAR}{\sqrt{LPM_2(MAR)}}$$
Onde:
$R_p$ é o retorno médio do portfólio.
$MAR$ (*Minimum* *Acceptable* *Return*) é o retorno alvo definido pelo investidor.
$TDD$ (*Target **Downside* *Deviation*) é a raiz quadrada da semivariância em relação ao MAR.
Análise Comparativa:
O Índice de Sortino e o Sharpe convergem quando a distribuição dos retornos é normal e o MAR é igual à média. Contudo, para estratégias com alta assimetria positiva (e.g., trend following, opções longas), o Sortino será consistentemente superior ao Sharpe, pois não penaliza os ganhos voláteis. Inversamente, para estratégias com assimetria negativa (e.g., venda de volatilidade), o Sortino revelará um desempenho ajustado ao risco inferior, expondo os riscos ocultos que o Sharpe mascara.13

**2.5.2 O Índice ****Omega****: Capturando Todos os Momentos**

Introduzido por Keating e Shadwick em 2002, o Índice Omega ($\Omega$) representa um salto conceitual ao dispensar completamente a necessidade de estimar momentos estatísticos (média, variância) e operar diretamente sobre a distribuição de probabilidade cumulativa dos retornos.64
O Omega é definido como a razão entre a probabilidade ponderada de ganhos e a probabilidade ponderada de perdas em relação a um limiar $L$:

$$\Omega(L) = \frac{\int_{L}^{\infty} [1 - F(r)] \, dr}{\int_{-\infty}^{L} F(r) \, dr}$$
Vantagem Crítica:
O Omega captura implicitamente todos os momentos da distribuição (média, variância, assimetria, curtose e momentos superiores) em uma única métrica. Ao variar o limiar $L$, o Omega fornece um perfil completo de risco-retorno, em vez de uma estimativa pontual. Isso o torna a ferramenta predileta para analisar ativos complexos e não lineares, como fundos de hedge e criptoativos, onde a suposição de normalidade é fatalmente falha.64
Adicionalmente, existe uma relação direta entre o conceito de *Upside* *Potential* *Ratio* e o Omega. O numerador do Omega corresponde ao potencial de alta (*Upside* *Potential*), enquanto o denominador corresponde ao potencial de baixa (*Downside* *Potential*), alinhando a métrica com a intuição econômica de ganho *versus* dor.68

**2.5.3 O Índice Kappa: A Generalização Unificadora**

Kaplan e Knowles (2004) propuseram o Índice Kappa ($K_n$) como uma medida generalizada que unifica o Sortino e o Omega sob uma única estrutura matemática baseada em LPMs.70

$$K_n(\tau) = \frac{\mu - \tau}{\sqrt[n]{LPM_n(\tau)}}$$
A elegância do Kappa reside na sua capacidade de recuperar as outras métricas através do ajuste do parâmetro $n$:
Quando $n=1$, o Kappa é funcionalmente equivalente ao **Índice ****Omega** (ranking idêntico).
Quando $n=2$, o Kappa torna-se o **Índice de ****Sortino**.
Para $n=3$ ou superior, o Kappa penaliza severamente a curtose e riscos extremos de cauda.
Essa generalização permite que gestores de portfólio calibrem a métrica de desempenho especificamente para a função de utilidade de seus clientes. Para um investidor avesso a perdas catastróficas, um $K_3$ ou $K_4$ seria mais apropriado; para um investidor focado na probabilidade geral de ganho, um $K_1$ (Omega) seria ideal.73

**2.6 Fronteiras Eficientes: A Geometria da Assimetria**

A aplicação das métricas de PMPT altera a geometria da fronteira eficiente. Enquanto a fronteira eficiente da MPT (média-variância) é sempre uma hipérbole suave e convexa, a fronteira eficiente da PMPT (retorno-LPM ou retorno-CVaR) pode assumir formas irregulares e não-suaves, especialmente quando composta por ativos com distribuições heterogêneas (mistura de ativos normais e não-normais).43
Em particular, a fronteira da PMPT tende a sugerir alocações mais concentradas em ativos com assimetria positiva e a evitar ativos com caudas esquerdas pesadas, mesmo que estes possuam alta média de retorno. Estudos recentes sobre criptoativos mostram que a otimização via PMPT resulta em portfólios com melhor proteção contra *drawdowns* severos do que a otimização via MPT, dado o perfil extremamente leptocúrtico desses ativos.9

**2.7 Avanços Recentes e Integração com Machine Learning (2024-2025)**

A fronteira atual da pesquisa em PMPT reside na sua integração com a Inteligência Artificial. Publicações e estudos de 2024 e 2025 indicam uma tendência crescente no uso de algoritmos de **Machine Learning**, como redes neurais recorrentes (LSTM) e Deep Learning, para estimar dinamicamente os Momentos Parciais Inferiores e otimizar portfólios.78
Ao contrário dos modelos estáticos tradicionais que dependem de dados históricos passados, modelos híbridos (PMPT + ML) conseguem prever mudanças nos regimes de volatilidade e na forma das caudas (*tail* *risk* *forecasting*), ajustando as alocações em tempo real para minimizar o CVaR futuro. Essa abordagem, denominada "Otimização Robusta Dinâmica", supera as limitações da MPT e da PMPT clássica, oferecendo resultados superiores em *backtests* e aplicações reais, especialmente em mercados voláteis e durante transições de regime econômico.80
Além disso, a PMPT tem sido fundamental na integração de critérios ESG (Environmental, Social, and Governance) na gestão de portfólios. Estudos recentes sugerem que o uso de métricas de *downside* *risk* como o Índice de Sortino revela melhor o perfil de risco ajustado de empresas com altas pontuações ESG, que tendem a ter menor risco de cauda (menor risco reputacional e regulatório) do que empresas convencionais, algo que o Índice de Sharpe muitas vezes falha em capturar.82

**2.8 Conclusão**

A Teoria Pós-Moderna do Portfólio representa a maturidade da gestão de investimentos quantitativa. Ao rejeitar a simplificação excessiva da normalidade e abraçar a complexidade assimétrica dos mercados e da psicologia humana, a PMPT oferece ferramentas — LPM, CVaR, Sortino, Omega — que são não apenas teoricamente superiores, mas pragmaticamente indispensáveis. Em um ambiente financeiro caracterizado por crises recorrentes e incerteza radical, a capacidade de distinguir entre o risco de ruína e a volatilidade de oportunidade é o que separa a sobrevivência da extinção. A PMPT é a linguagem matemática dessa distinção.

**Tabela 2.2: Resumo Analítico dos Indicadores de Desempenho (MPT vs. PMPT)**

| Indicador | Base Teórica | Fórmula Conceitual | Sensibilidade à Cauda | Principal Aplicação |
| --- | --- | --- | --- | --- |
| Sharpe | MPT (Variância) | $\frac{Retorno - R_f}{\sigma_{total}}$ | Baixa (Assume Normalidade) | Ativos tradicionais, Benchmark relativo |
| Sortino | PMPT (LPM 2) | $\frac{Retorno - MAR}{\sigma_{downside}}$ | Média (Foca no Downside) | Fundos Assimétricos, Hedge Funds |
| Omega | PMPT (Todos Momentos) | $\frac{\text{Prob. Ponderada Ganhos}}{\text{Prob. Ponderada Perdas}}$ | Alta (Captura toda distribuição) | Derivativos, Cripto, Private Equity |
| Kappa ($K_3$) | PMPT (LPM 3) | $\frac{Retorno - MAR}{\sqrt[1]{LPM_3}}$ | Muito Alta (Penaliza extremos) | Gestão de Risco de Cauda, Seguros |

Fonte: Elaboração do autor baseada em.71

- **Capítulo 3: O Modelo de Black-****Litterman****: Uma Reconstrução Bayesiana da Alocação de Ativos**


- **As Limitações da Média-Variância e a Gênese do Black-Litterman**

Embora a Teoria Moderna do Portfólio (MPT) tenha estabelecido os fundamentos da diversificação, sua implementação prática via otimização de Média-Variância (MV) enfrenta desafios críticos. Conforme apontam Michaud (1989) e Best e Grauer (1991), o otimizador MV tende a funcionar como um "maximizador de erros", sendo extremamente sensível aos inputs de retorno esperado. Pequenas variações nas estimativas podem resultar em carteiras extremas, pouco diversificadas e instáveis (soluções de canto), que não refletem a intuição do investidor.
Em resposta a essas limitações, Black e Litterman (1990, 1992) propuseram um modelo que mitiga a sensibilidade aos erros de estimação e produz alocações mais estáveis e robustas. O Modelo Black-Litterman (BL) não substitui a otimização MV, mas aprimora a estimativa dos retornos esperados — o input mais volátil do processo — utilizando uma abordagem Bayesiana para combinar informações de mercado com expectativas específicas do investidor.


- **A Estrutura Bayesiana: Prior, Visões e Posterior**


A inovação central do modelo BL reside na combinação de duas fontes distintas de informação para gerar um novo vetor de retornos esperados (distribuição Posterior):
- O Prior (Equilíbrio de Mercado): Diferentemente de Markowitz, que muitas vezes utiliza médias históricas, o BL assume como ponto de partida neutro que o mercado está em equilíbrio. Utilizando um processo de "Otimização Reversa" (Baseada no CAPM), o modelo deriva os **Retornos de Equilíbrio Implícitos (Π)** a partir das capitalizações de mercado atuais. Esse vetor atua como um "centro de gravidade", garantindo que, na ausência de novas informações, a alocação ótima seja a carteira de mercado, evitando posições extremas.
- **As Visões (****Views**** - Q) e a Incerteza (Ω):** O modelo permite que o investidor incorpore suas expectativas subjetivas ou quantitativas sobre o desempenho dos ativos. No contexto deste trabalho, as "Visões" não são opiniões discricionárias, mas sim as projeções de retorno geradas pelos modelos preditivos **ARIMA e Redes Neurais LSTM**. Essas visões são expressas no vetor Q e associadas a uma matriz de incerteza diagonal Ω, que reflete o grau de confiança em cada previsão (baseado, por exemplo, no erro quadrático médio dos modelos preditivos).

- A Fórmula Mestra e a Aplicação no Estudo

A combinação do equilíbrio de mercado **(Π) **com as previsões dos modelos (Q), ponderada pela incerteza (Ω) e pelo escalar de confiança no prior (τ), resulta no vetor de Retornos Esperados de Black-Litterman (E[R]), calculado pela equação canônica do modelo:

Onde Σ representa a matriz de covariância dos retornos dos ativos.
O vetor resultante E[R] é então utilizado como input no otimizador de média-variância. A vantagem desta abordagem para o presente estudo é dupla: (i) permite testar se a inteligência computacional (LSTM) e econométrica (ARIMA) agrega valor estatístico ao portfólio (via vetor Q); e (ii) utiliza a estrutura Bayesiana para "suavizar" os erros de previsão desses modelos, ancorando as decisões no equilíbrio de mercado quando as previsões são incertas. Dessa forma, espera-se que as carteiras geradas via Black-Litterman apresentem desempenho ajustado ao risco superior e menor turnover do que aquelas baseadas puramente em otimização histórica.

**3.1.1 O Contexto da Goldman Sachs e a Colaboração Black-****Litterman**
A transição de Fischer Black da academia para a prática financeira em 1984, ao juntar-se à Goldman Sachs, marcou o início de uma era de ouro na engenharia financeira aplicada. Black, já reverenciado por sua contribuição seminal ao modelo de precificação de opções Black-Scholes (1973), assumiu a liderança do Grupo de Estratégias Quantitativas da firma. Neste ambiente, ele colaborou estreitamente com Robert Litterman, um econometrista renomado e então vice-presidente da divisão de pesquisa de Renda Fixa.3
A motivação primordial para o desenvolvimento do modelo não foi puramente acadêmica, mas sim uma necessidade comercial urgente. A Goldman Sachs buscava oferecer aos seus clientes institucionais uma abordagem quantitativa e disciplinada para estruturar portfólios de títulos internacionais (*global **bonds*) e moedas. No entanto, Black e Litterman observaram que os modelos de otimização quantitativa existentes, baseados na MPT clássica, eram raramente utilizados na sua forma pura. Para tornar os resultados da otimização "palatáveis", os gestores eram forçados a impor restrições artificiais severas — como limites rígidos de posição por ativo ou proibição de vendas a descoberto — que, na prática, anulavam a inteligência matemática do otimizador.3
Em 1990, a dupla apresentou internamente uma abordagem inovadora que permitia aos gestores incorporar suas visões de mercado sem destruir a estrutura de diversificação do portfólio. Inicialmente focado em renda fixa, o modelo foi expandido para ações em 1991 e formalizado academicamente com a publicação de dois artigos fundamentais: "Asset Allocation: Combining Investor Views with Market Equilibrium" no *The **Journal* *of* *Fixed** Income* (1991) e "Global Portfolio Optimization" no *Financial **Analysts* *Journal* (1992).5 Estes trabalhos estabeleceram o BL não apenas como uma ferramenta proprietária da GSAM, mas como o novo padrão da indústria para a alocação de ativos, resolvendo o dilema da sensibilidade aos *inputs*.
**3.1.2 A Crítica à MPT: O Dilema da "Maximização de Erros" e as Soluções de Canto**
A inovação de Black e Litterman foi uma resposta direta e técnica às falhas patológicas da otimização de Markowitz quando alimentada com estimativas ruidosas. A literatura acadêmica da época, com destaque para os trabalhos de Richard Michaud (1989), já havia diagnosticado que a MVO atua, na prática, como um "maximizador de erros" (*error* *maximizer*).6
O mecanismo da "Maximização de Erros" opera da seguinte forma: os algoritmos de otimização quadrática são matematicamente desenhados para explorar as características extremas dos dados. Eles buscam ativos com a maior razão retorno/risco marginal. No entanto, em finanças, as estimativas de retorno esperado ($\mu$) são notoriamente imprecisas e ruidosas. Quando um ativo apresenta uma estimativa de retorno excepcionalmente alta, é estatisticamente provável que essa estimativa contenha um erro positivo significativo (viés de otimismo ou ruído de amostra). O otimizador, incapaz de distinguir entre um "alpha" verdadeiro e um erro de estimação, aloca agressivamente capital neste ativo. Inversamente, ativos com erros de estimação negativos são penalizados e removidos do portfólio. Consequentemente, o portfólio "ótimo" resultante é, na verdade, uma coleção concentrada dos ativos com os maiores erros de estimação positiva, desempenhando frequentemente pior fora da amostra do que um portfólio ingênuo de pesos iguais ($1/N$).6
Este fenômeno manifesta-se em duas patologias observáveis que inviabilizam o uso institucional da MPT pura:
**Instabilidade Crônica dos Pesos:** A topologia da fronteira eficiente em torno do ótimo é frequentemente "plana" ou instável. Pequenas alterações nos *inputs* (ex: alterar a expectativa de retorno de um ativo em 0,5%) podem causar mudanças drásticas nas alocações sugeridas (ex: o peso do ativo salta de 0% para 40%). Isso gera custos de transação proibitivos e mina a confiança do comitê de investimento na robustez do modelo.4
**Soluções de Canto (*****Corner ******Solutions*****):** Quando restrições de não-negatividade (proibição de *short **selling*) são aplicadas, o otimizador tende a colapsar a diversificação. A solução matemática frequentemente reside nos vértices do conjunto viável, resultando em portfólios binários onde a vasta maioria dos ativos tem peso zero e o capital é concentrado em poucos "vencedores" estatísticos. Tais portfólios são intuitivamente rejeitados por gestores prudentes, pois contradizem o princípio fundamental da diversificação.11
Black e Litterman identificaram que a raiz desse problema não estava na otimização em si, mas na impossibilidade de estimar o vetor de retornos esperados ($\mu$) com precisão suficiente usando apenas dados históricos. A solução proposta foi, portanto, metodológica: substituir a estimativa histórica puramente estatística por uma estimativa Bayesiana ancorada na teoria econômica.13

**3.2 A Abordagem Bayesiana: O Coração Conceitual do Modelo**
O rigor matemático e a elegância prática do Modelo Black-Litterman residem na sua formulação como um problema de **inferência Bayesiana**. Ao contrário da estatística frequentista clássica, que trata os parâmetros (como o retorno esperado) como constantes fixas e desconhecidas, a abordagem Bayesiana trata os parâmetros como variáveis aleatórias que possuem uma distribuição de probabilidade própria. Isso permite incorporar explicitamente a incerteza sobre a estimativa e atualizar essa crença à medida que novas informações (visões) se tornam disponíveis.2
A estrutura conceitual do BL segue o silogismo Bayesiano clássico:
**3.2.1 Prior: O Equilíbrio de Mercado**
O ponto de partida do modelo, ou distribuição *a priori*, é a premissa de neutralidade. Na ausência de qualquer informação específica ou visão profética por parte do gestor, qual é a melhor estimativa racional para os retornos futuros? A resposta de Black e Litterman baseia-se na Hipótese de Mercados Eficientes e no CAPM (*Capital **Asset* *Pricing** Model*).
Assume-se que, no agregado, o mercado está em equilíbrio. Portanto, o portfólio de mercado (ponderado pela capitalização de todos os ativos) deve ser o portfólio ótimo para o investidor médio avesso ao risco. A partir dessa observação observável (os pesos de mercado), o modelo "engenharia reversa" os retornos que justificam esses pesos. Este vetor, denominado **Retornos de Equilíbrio Implícitos** ($\Pi$), serve como a âncora gravitacional do modelo. Ele garante que, se o gestor não tiver visões ("eu não sei nada"), o modelo recomendará manter o portfólio de mercado passivo, evitando as alocações extremas da MPT.13
**3.2.2 ****Likelihood****: As Visões do Investidor (*****Views*****)**
A "verossimilhança" ou informação nova entra no modelo através das Visões. Diferente da MPT, que exige um vetor completo de retornos para todos os ativos, o BL permite que o gestor expresse opiniões apenas sobre um subconjunto de ativos (Visões Parciais). Estas visões podem ser absolutas ("Petrobras vai subir 10%") ou relativas ("Bancos vão superar Varejo em 2%"). Crucialmente, cada visão é acompanhada por um grau de incerteza (variância do erro), permitindo que o modelo pondere matematicamente a convicção do gestor.17
**3.2.3 Posterior: A Nova Estimativa Combinada**
O resultado final é a distribuição *a posteriori*, calculada aplicando a Regra de Bayes. O vetor de retornos esperados BL ($E_{BL}$) é uma média ponderada complexa entre o Prior (Equilíbrio) e a Likelihood (Visões).
Se o gestor tem baixa confiança nas suas visões, o Posterior converge para o Prior (o portfólio tende ao índice de mercado).
Se o gestor tem alta confiança, o Posterior afasta-se do equilíbrio na direção das visões, alterando os pesos do portfólio.
Essa mecânica atua como um filtro de estabilidade (shrinkage estimator), mitigando a "maximização de erros" ao ancorar as estimativas em valores economicamente plausíveis.19

**3.3 Derivação Matemática Detalhada: A "Fórmula Mestra"**
A implementação do modelo exige a manipulação precisa de álgebra matricial para combinar as distribuições normais assumidas para o Prior e as Visões. A seguir, detalha-se a derivação dos componentes críticos e a estrutura das matrizes envolvidas.
**3.3.1 O Vetor de Retornos Implícitos ($\Pi$) e a Otimização Reversa**
O cálculo do Prior baseia-se na inversão da equação de otimização de Markowitz. O problema de maximização da utilidade quadrática do investidor representativo é dado por:
$$\max_w U = w^T \Pi - \frac{\lambda}{2} w^T \Sigma w$$
Onde:
$w$ ($N \times 1$): Vetor de pesos dos ativos no portfólio de mercado.
$\Pi$ ($N \times 1$): Vetor desconhecido de retornos em excesso de equilíbrio.
$\Sigma$ ($N \times N$): Matriz de covariância dos retornos dos ativos (estimada historicamente ou via modelos GARCH).
$\lambda$ (escalar): Coeficiente de aversão ao risco do mercado.
A condição de primeira ordem para a otimização (derivada igual a zero) é $\Pi - \lambda \Sigma w = 0$. Reorganizando para isolar $\Pi$, obtemos a fórmula da **Otimização Reversa**:
$$\Pi = \lambda \Sigma w_{mkt}$$
Este vetor $\Pi$ representa os retornos que o mercado *precisa* esperar para que os atuais pesos de capitalização ($w_{mkt}$) sejam ótimos. O parâmetro de aversão ao risco global $\lambda$ é frequentemente calibrado como $\lambda = \frac{E - R_f}{\sigma^2_m}$, situando-se tipicamente entre 2 e 4 em estudos empíricos.16
A incerteza associada a esta estimativa do Prior é modelada como $\tau\Sigma$, onde $\tau$ é um escalar de proporcionalidade. Portanto, a distribuição do Prior é:
$$\mu \sim N(\Pi, \tau\Sigma)$$
**3.3.2 A Estrutura das Visões: Matrizes $P$, $Q$ e $\****Omega****$**
As visões subjetivas são modeladas como um sistema linear estocástico:
$$P \cdot \mu = Q + \varepsilon$$
Com termo de erro $\varepsilon \sim N(0, \Omega)$.
**A Matriz de Projeção / Identificação ($P$)**
É uma matriz de dimensão $K \times N$, onde $K$ é o número de visões e $N$ o número de ativos. Cada linha $k$ mapeia uma visão sobre os ativos.
**Visão Absoluta:** Para uma visão sobre o Ativo A (índice $i$), o elemento $P_{k,i} = 1$ e os demais são 0.
**Visão Relativa:** Para uma visão "Ativo A supera Ativo B", a linha contém valores positivos para A e negativos para B. A soma da linha é tipicamente zero. A ponderação pode ser igualitária ($+1, -1$ ou $+0.5, -0.5$) ou ponderada por capitalização (*value-weighted*), o que reduz o ruído em visões sobre setores inteiros.15
**O Vetor de Expectativas das Visões ($Q$)**
É um vetor coluna $K \times 1$. Cada elemento $Q_k$ representa o retorno esperado da visão $k$. Para visões relativas, $Q_k$ é o *spread* ou diferencial de retorno esperado, não o retorno total absoluto.22
**A Matriz de Incerteza das Visões ($Ω$)**
É uma matriz de covariância $K \times K$ dos termos de erro $\varepsilon$. Assume-se geralmente que as visões são independentes, tornando $\Omega$ uma matriz diagonal:
$$\Omega = \text{diag}(\omega_1, \omega_2,..., \omega_k)$$
A magnitude de $\omega_k$ representa a incerteza da visão $k$. Se $\omega_k \to 0$, o investidor tem certeza absoluta (confiança infinita), e o modelo forçará o portfólio a satisfazer a visão exatamente. Se $\omega_k \to \infty$, a visão é ignorada.17
**3.3.3 A Fórmula Mestra de Black-****Litterman**
Combinando o Prior ($N(\Pi, \tau\Sigma)$) e a Likelihood ($N(Q, \Omega)$) via Teorema de Bayes, obtemos a distribuição Posterior $\mu_{BL} \sim N(E_{BL}, \Sigma_{BL})$. O vetor de retornos esperados combinados é dado pela "Fórmula Mestra":
$$E_{BL} =^{-1}$$
Esta equação, embora intimidante, é intuitivamente uma **média ponderada pela precisão** (inverso da variância).
O termo $(\tau\Sigma)^{-1}$ é a precisão do Prior (Equilíbrio).
O termo $P^T \Omega^{-1} P$ é a precisão das Visões projetada no espaço dos ativos.
O modelo pondera $\Pi$ e $Q$ com base nessas precisões relativas.
Para fins computacionais, utiliza-se frequentemente a **Identidade de Matrizes de ****Woodbury** para reescrever a fórmula de modo a evitar a inversão da matriz $\Sigma$ (que pode ser singular ou mal condicionada em grandes dimensões), resultando na forma alternativa mais estável numericamente:
$$E_{BL} = \Pi + \tau\Sigma P^T^{-1} [Q - P\Pi]$$
Nesta forma, o retorno BL é explicitamente o Retorno de Equilíbrio ($\Pi$) mais um termo de ajuste (*tilt*). O ajuste depende da discrepância entre a visão e o equilíbrio ($Q - P\Pi$), escalado pela razão entre incerteza do Prior e incerteza da Visão.23
A nova matriz de covariância a posteriori, que deve alimentar o otimizador, é:
$$\Sigma_{BL} = \Sigma +^{-1}$$
Note que $\Sigma_{BL}$ é maior que a covariância histórica $\Sigma$. O modelo adiciona uma camada extra de risco, refletindo a incerteza epistêmica sobre a verdadeira média dos retornos.22

**3.4 A Controvérsia Teórica sobre o Escalar Tau ($\tau$)**
O parâmetro $\tau$ permanece como um dos componentes mais esotéricos e debatidos na literatura do BL, gerando interpretações conflitantes sobre sua calibração e impacto.
**A Visão Original (Black & ****Litterman****, 1992):** Os autores sugeriram que $\tau$ deveria ser um valor pequeno (próximo de zero), argumentando que a incerteza sobre a média de longo prazo é muito menor que a volatilidade dos retornos. Valores entre 0,025 e 0,05 são comuns nesta abordagem.24
**A Abordagem Estatística (Walters, 2014; ****Meucci****, 2005):** Argumentam que, se o Prior é derivado de uma série histórica, $\tau$ deve ser calibrado como o erro padrão da média, ou seja, $\tau \approx 1/T$, onde $T$ é o número de observações da amostra. Para 5 anos de dados mensais, $\tau \approx 1/60$. Esta visão fornece uma base empírica objetiva para o parâmetro.24
**A Abordagem de ****Satchell**** e ****Scowcroft**** (2000):** Propuseram fixar $\tau = 1$. Embora simplifique a álgebra, essa escolha altera drasticamente o peso relativo do Prior, exigindo que a matriz $\Omega$ seja recalibrada proporcionalmente para evitar que as visões dominem completamente o portfólio. Eles tratam a incerteza do prior e das visões como magnitudes comparáveis *a priori*.24
Em última análise, como demonstrado por **Thomas ****Idzorek**** (2005)**, a escolha do valor escalar de $\tau$ torna-se irrelevante para o cálculo do vetor de retornos ($E_{BL}$) se a matriz $\Omega$ for calibrada endogenamente proporcional a $\tau$. Contudo, $\tau$ continua a afetar a matriz de covariância posterior $\Sigma_{BL}$, influenciando a magnitude absoluta do risco estimado.17

**3.5 Inovações Práticas: O Método de ****Idzorek**** e a Matriz $\****Omega****$**
A maior barreira para a adoção generalizada do BL não foi teórica, mas operacional: a especificação da matriz $\Omega$. Solicitar a um gestor que quantifique a "variância do erro da sua previsão" (ex: "Minha visão tem variância de 0.0045") é contra-intuitivo e propenso a erros de calibragem.
**3.5.1 O Algoritmo de Confiança Percentual (****Idzorek****, 2005)**
Thomas Idzorek propôs uma solução pragmática que traduz a intuição humana para a álgebra matricial. Seu método permite que o usuário especifique apenas um **nível de confiança percentual** (0% a 100%) para cada visão. O algoritmo então "implica" matematicamente o valor de $\Omega$ necessário.21
O processo, detalhado no trabalho seminal "A Step-by-Step Guide to the Black-Litterman Model" (2005), segue os seguintes passos lógicos:
**Cálculo do Portfólio de Certeza Total:** O modelo calcula qual seria o vetor de retornos se o investidor tivesse 100% de confiança na visão (o que equivaleria a $\omega_k \approx 0$). Isso gera um vetor de pesos de alocação de "certeza total".
**Determinação do Desvio Máximo:** Calcula-se a diferença de alocação (vetor de *tilts*) entre o portfólio de equilíbrio (sem visões) e o portfólio de certeza total.
**Interpolação Linear pela Confiança:** Se o investidor declara 50% de confiança, o algoritmo define que o *tilt* alvo deve ser 50% do desvio máximo calculado no passo anterior.
**Engenharia Reversa de $\****Omega****$:** O algoritmo resolve iterativamente ou analiticamente para encontrar os valores da diagonal de $\Omega$ que, quando inseridos na fórmula mestra do BL, resultam exatamente nesses pesos-alvo interpolados.
A fórmula implícita derivada por Idzorek assume que a variância da visão é proporcional à variância do portfólio da visão ($p_k \Sigma p_k^T$) ajustada por um fator de escala $\alpha$ derivado da confiança ($C$):
$$\omega_k = \tau \cdot (p_k \Sigma p_k^T) \cdot \left(\frac{1-C}{C}\right)$$
Essa inovação democratizou o modelo, permitindo que gestores fundamentais utilizassem a ferramenta quantitativa sem necessidade de doutorado em estatística, expressando visões como "Tenho 80% de confiança que Tech superará Energy".21

**3.6 Comparação Crítica: BL, MPT e PMPT**
A análise da evolução dos modelos de alocação exige distinguir claramente o papel de cada teoria. Uma confusão comum é tratar BL e PMPT como concorrentes diretos, quando na verdade atuam em dimensões distintas do problema de portfólio.
**3.6.1 MPT vs. BL: A Correção da Estabilidade**
A MPT (Markowitz) falha primariamente na **sensibilidade aos inputs**. Como discutido (Seção 3.1.2), a MPT maximiza erros de estimação, levando a soluções de canto. O BL corrige isso não alterando o otimizador, mas "limpando" os inputs. Ao ancorar o retorno esperado ($\mu$) no equilíbrio, o BL atua como um filtro Bayesiano que remove o ruído estatístico. O resultado são portfólios que, mesmo sem restrições, tendem a ser diversificados e intuitivos, ao contrário das alocações binárias da MPT pura.4
**3.6.2 BL vs. PMPT: Complementaridade Estrutural**
A Teoria Pós-Moderna do Portfólio (PMPT) critica a MPT por um motivo diferente: a **medida de risco**. A PMPT argumenta que a variância (utilizada tanto na MPT quanto no BL clássico) é uma medida falha porque penaliza a volatilidade positiva (*upside*) tanto quanto a negativa. A PMPT propõe métricas assimétricas como Semivariância, *Downside* *Deviation* e CVaR (*Conditional* *Value* *at** Risk*).26
A relação entre BL e PMPT é de **complementaridade**, não substituição:
**Black-****Litterman** foca na melhoria da **Estimativa de Retorno** (Primeiro Momento, $\mu$).
**PMPT** foca na melhoria da **Medição de Risco** (Segundos Momentos e Caudas).
Consequentemente, a fronteira da pesquisa atual em finanças quantitativas propõe modelos híbridos **"BL-****Mean****-****CVaR****"**. Nesta abordagem, utiliza-se a estrutura Bayesiana do BL para derivar o vetor de retornos esperados robustos ($\mu_{BL}$) e, subsequentemente, alimenta-se este vetor em um otimizador que minimiza o CVaR ou maximiza o Índice de Sortino (PMPT), em vez de minimizar a variância. Estudos empíricos indicam que essa combinação "Inputs BL + Otimizador PMPT" gera os portfólios mais robustos *out-**of**-sample*, protegendo contra riscos de cauda enquanto evita a instabilidade de alocação.28
**Tabela 3.1: Síntese Comparativa dos Modelos**

| Dimensão Analítica | MPT (Markowitz) | Black-Litterman (BL) | PMPT (Pós-Moderna) |
| --- | --- | --- | --- |
| Foco Principal | Diversificação Matemática | Estabilidade da Estimativa ($\mu$) | Assimetria do Risco (Downside) |
| Input de Retorno | Histórico (Instável) | Equilíbrio + Visões (Bayesiano) | Histórico ou Subjetivo |
| Tratamento de Erros | Maximiza Erros (Michaud) | Mitiga via Shrinkage (Prior) | Neutro (Depende do Input) |
| Medida de Risco | Variância (Simétrica) | Variância (Canônico) | Semivariância, CVaR, LPM |
| Resultado Típico | Soluções de Canto (Instáveis) | Portfólio Diversificado (Estável) | Proteção de Cauda e Assimetria |


**3.7 Limitações e Extensões Modernas**
Apesar de sua elegância, o modelo BL clássico de 1992 não é isento de falhas, muitas das quais derivam de suas premissas simplificadoras herdadas da MPT.
**3.7.1 A Dependência da Normalidade e do CAPM**
O modelo assume que os retornos dos ativos seguem uma distribuição Normal Multivariada. Esta suposição é empiricamente rejeitada pela presença observada de "caudas gordas" (leptocurtose) e assimetria (*skewness*) nos mercados financeiros, especialmente em períodos de crise.30 O uso da distribuição normal subestima a probabilidade de eventos extremos, tornando o BL clássico vulnerável a "Cisnes Negros". Adicionalmente, o Prior depende da validade do CAPM. Se o mercado for ineficiente ou se o *proxy* do portfólio de mercado for inadequado, o ponto de ancoragem $\Pi$ estará enviesado ("Garbage In"), contaminando toda a alocação subsequente.11
**3.7.2 Entropy Pooling e Fully Flexible Views (****Meucci****)**
Para superar a restrição da normalidade, Attilio Meucci (2008, 2010) introduziu a generalização conhecida como **Entropy** **Pooling** (Agrupamento de Entropia). Diferente do BL que usa fórmulas fechadas para conjugados gaussianos, o Entropy Pooling utiliza otimização numérica para minimizar a **Divergência de ****Kullback-Leibler** (Entropia Relativa) entre a distribuição Prior e a Posterior.30
As vantagens desta extensão são profundas:
**Prior Genérico:** O Prior não precisa ser normal ou de equilíbrio. Pode ser uma distribuição empírica histórica, uma distribuição de Monte Carlo com caudas pesadas, ou derivada de Cópulas para modelar dependência não-linear nas caudas.
**Visões Flexíveis:** O gestor não se limita a visões sobre médias ($Q$). É possível inserir visões sobre volatilidade ("A vol vai aumentar"), correlação, ou medidas de cauda como o VaR ("O risco de perda máxima será de 15%").
**Consistência:** O método garante que a distribuição Posterior seja a mais próxima possível do Prior (preservando a estrutura de mercado) enquanto satisfaz as restrições impostas pelas visões complexas.
Essa abordagem representa o estado da arte na alocação de ativos, permitindo a fusão da estabilidade Bayesiana do BL com a consciência de risco de cauda da PMPT em um framework matemático unificado e agnóstico quanto à distribuição subjacente.33
**3.8 Conclusão do Capítulo**
O Modelo de Black-Litterman transcendeu sua origem como uma ferramenta proprietária da Goldman Sachs para se tornar um pilar fundamental das Finanças Quantitativas modernas. Sua contribuição não foi refutar Markowitz, mas sim "salvar" a MPT de si mesma, introduzindo uma camada Bayesiana de bom senso econômico que estabiliza as alocações. Ao permitir a fusão elegante entre a disciplina passiva do equilíbrio de mercado e a inteligência ativa das visões do gestor, o BL resolveu o dilema da "maximização de erros". As suas extensões modernas, como o método de confiança de Idzorek e a *Entropy* *Pooling* de Meucci, asseguram que o modelo permaneça adaptável a um mundo financeiro cada vez mais complexo e não-normal, servindo como a ponte ideal entre a teoria de eficiência de mercado e a gestão ativa prática.


# METODOLOGIA DA PESQUISA
# 
A presente pesquisa caracteriza-se quanto à sua natureza como aplicada e quantitativa, utilizando técnicas de modelagem e simulação para avaliar a eficiência de diferentes estratégias de alocação de ativos. O objetivo é analisar comparativamente o desempenho de portfólios construídos sob a ótica da Teoria Moderna do Portfólio (TMP), Teoria Pós-Moderna do Portfólio (PMPT) e o modelo de Black-Litterman (BL), variando os métodos de estimação dos parâmetros de entrada (*inputs*) e as funções objetivo de otimização.

# Universo, Amostra e Dados

O universo da pesquisa compreende as ações negociadas na B3 (Brasil, Bolsa, Balcão). Para garantir a liquidez e a operacionalidade das carteiras simuladas, a amostra foi constituída pelos ativos que compõem o Índice Bovespa (Ibovespa) e/ou IBrX-100, rebalanceados quadrimestralmente, excluindo-se aqueles que não apresentaram negociação contínua no período de análise.
O período de análise estende-se de janeiro de 2010 a dezembro de 2025 (considerando dados projetados ou realizados até a data de corte efetiva). Os dados de preços de fechamento ajustados por proventos (dividendos, desdobramentos e bonificações) foram coletados através de bases de dados financeiras confiáveis (Economatica, Banco Central do Brasil). Como ativo livre de risco (proxy para , utilizou-se a taxa do Certificado de Depósito Interbancário (CDI).

# Tratamento dos Dados

Os preços ajustados  foram convertidos em log-retornos diários ,  visando obter propriedades estatísticas mais adequadas para a modelagem econométrica e de machine learning, como a normalidade, estacionariedade e a aditividade temporal. A fórmula utilizada é dada por:

Foram aplicados os testes Shapiro-Wilk** e **de raiz unitária (Dickey-Fuller Aumentado - ADF) para verificar a normalidade e estacionariedade das séries temporais, este, pré-requisito para os modelos ARIMA e GARCH.

# Definição dos *Inputs *e Modelos de Previsão

A principal inovação metodológica deste trabalho reside na variação da estimação do vetor de retornos esperados (μ), mitigando o problema da "maximização de erro" inerente ao uso de médias históricas,. Foram definidos três conjuntos de inputs de retorno:

- **Média Histórica:** Média aritmética simples dos retornos passados na janela de estimação .Utilizada como *benchmark* da abordagem ingênua e base para a MPT tradicional.
- **ARIMA (****AutoRegressive** **Integrated**** Moving ****Average****):** Utilização de modelos Auto-Regressivos Integrados de Médias Móveis (ARIMA) para a média condicional, ajustados pela volatilidade condicional via GARCH (Generalized Autoregressive Conditional Heteroskedasticity), capturando o agrupamento de volatilidade típico de séries financeiras.
- **Inteligencia**** Artificial (****LSTM ****- ****Long**** Short-****Term** **Memory****):** Aplicação de Redes Neurais Recorrentes do tipo Long Short-Term Memory (LSTM), capazes de capturar dependências não lineares de longo prazo e padrões sequenciais complexos nas séries temporais, superando as limitações de modelos lineares.

# Modelos de Otimização de Portfólio

Os vetores de retorno estimados e a matriz de covariância (Σ) foram submetidos a cinco motores de otimização distintos, abrangendo a evolução da teoria de finanças:

# Otimização Média-Variância (Markowitz)

Baseada na Teoria Moderna do Portifólio, busca maximizar o índice de Sharpe. Ela assume a normalidade dos retornos e utiliza a variância como medida de risco.


Sujeito a :  e  (Restrição de venda a descoberto)

### Carteira de Mínima Variância Global (PMVG)

Foca exclusivamente na minimização do risco , independentemente das estimativas de retorno esperado, sendo teoricamente mais robusta a erros de estimação.

### Otimização Pós-Moderna (PMPT): Mínimo CvaR

Em resposta às críticas sobre a normalidade dos retornos, utiliza-se o Conditional Value at Risk (CVaR) como função objetivo. O CVaR minimiza a perda esperada na cauda esquerda da distribuição (piores 5% dos cenários), sendo uma medida de risco coerente e convexa,,.

### Otimização Pós-Moderna: Máximo Índice de Sortino
- 
Substitui o desvio padrão pela semivariância (*downside deviation*), penalizando apenas a volatilidade negativa (retornos abaixo do alvo), alinhando-se à aversão à perda descrita nas Finanças Comportamentais
### Modelo Black-Litterman (Abordagem Mista)

- **Prior(): **Retornos de equilibrio de mercado.
- **Visões(Q): **Retornos projetados pelos modelos ARIMA e LSTM.
- **Posterior****: **Novo vetor de retornos esperados, calculado pela “Formula Mestra” de Black-Litterman, utilizado para reotimizar os pesos da carteira.

# Desenho Experimental e Protocolo de Teste (Backtesting)

A avaliação de desempenho será realizada através de janelas móveis (rolling windows):
- **Janela de Treinamento****(Loopback)**: Dados dos primeiros 60 meses  serão usados para treinar os modelos (ARIMA/LSTM) e estimar a matriz de covariância.
- **Janela de Teste**: 21 dias úteis (1 mês).
- **Rebalanceamento:** Mensal. A cada mês, a janela se desloca, os modelos são re-treinados, e os pesos ótimos são recalculados e mantidos para o mes seguinte.
- **Custos de Transação:** (Opcional, mas recomendado) erá considerada uma taxa de corretagem/emolumentos (ex: 0,1% por transação) para penalizar o excesso de turnover, garantindo realismo aos resultados líquidos.
Este método simula a decisão de um investidor real que dispõe apenas de dados passados para tomar decisões futuras.

# Métricas de Avaliação de Desempenho

A comparação entre as estratégias e os benchmarks (Ibovespa e CDI) baseou-se em métricas de retorno ajustado ao risco e eficiência,:
- Retorno Acumulado e Anualizado: Rentabilidade total no período.
- Volatilidade Anualizada: Desvio padrão dos retornos.
- Índice de Sharpe (IS): Retorno excedente por unidade de risco total.
- Índice de Sortino: Retorno excedente por unidade de risco de downside.
- Maximum Drawdown (MDD): Perda máxima observada do pico ao vale.
- Turnover: Taxa de rotatividade da carteira, indicativo de custos transacionais.
A significância estatística das diferenças de desempenho entre as carteiras propostas e a carteira ingênua (1/N) ou benchmark de mercado será verificada, quando aplicável, por testes de robustez (e.g., teste de Jobson-Korkie ou Ledoit-Wolf)


| 1 | Vale ON (VALE3) | 28 | Telef Brasil ON (VIVT3) | 55 | Klabin S/A UNT N2 (KLBN11) |
| --- | --- | --- | --- | --- | --- |
| 2 | ItauUnibanco PN (ITUB4) | 29 | Porto Seguro ON (PSSA3) | 56 | Allos ON (ALOS3) |
| 3 | Petrobras PN (PETR4) | 30 | Taesa UNT N2 (TAEE11) | 57 | Btgp Banco UNT (BPAC11) |
| 4 | Eletrobras ON (ELET3) | 31 | Cyrela Realt ON (CYRE3) | 58 | Assai ON (ASAI3) |
| 5 | Bradesco PN (BBDC4) | 32 | Totvs ON (TOTS3) | 59 | Rumo S.A. ON (RAIL3) |
| 6 | Petrobras ON (PETR3) | 33 | CPFL Energia ON (CPFE3) | 60 | Hapvida ON (HAPV3) |
| 7 | Sabesp ON (SBSP3) | 34 | Gerdau PN (GGBR4) | 61 | Csn Mineracao ON (CMIN3) |
| 8 | B3 ON (B3SA3) | 35 | Bradesco ON (BBDC3) | 62 | Petrorio ON (PRIO3) |
| 9 | Itausa PN (ITSA4) | 36 | Copel PNB (CPLE6) | 63 | Vibra ON (VBBR3) |
| 10 | Brasil ON (BBAS3) | 37 | Tim ON (TIMS3) | 64 | Suzano S.A. ON (SUZB3) |
| 11 | Embraer ON (EMBR3) | 38 | Natura ON (NATU3) | 65 | Rede D Or ON (RDOR3) |
| 12 | Weg ON (WEGE3) | 39 | Hypera ON (HYPE3) | 66 | Caixa Seguri ON (CXSE3) |
| 13 | Ambev S/A ON (ABEV3) | 40 | Sid Nacional ON (CSNA3) | 67 | Brava ON (BRAV3) |
| 14 | Energisa UNT N2 (ENGI11) | 41 | Marcopolo PN (POMO4) | 68 | Cogna ON ON (COGN3) |
| 15 | RaiaDrogasil ON (RADL3) | 42 | Direcional ON (DIRR3) | 69 | Iguatemi SA UNT (IGTI11) |
| 16 | Equatorial ON (EQTL3) | 43 | Fleury ON (FLRY3) | 70 | Cury S/A ON (CURY3) |
| 17 | Cemig PN (CMIG4) | 44 | Cosan ON (CSAN3) | 71 | Irbbrasil Re ON (IRBR3) |
| 18 | Localiza ON (RENT3) | 45 | Bradespar PN (BRAP4) | 72 | Auren ON (AURE3) |
| 19 | Eneva ON (ENEV3) | 46 | MRV ON (MRVE3) | 73 | Azzas 2154 ON (AZZA3) |
| 20 | Eletrobras PNB (ELET6) | 47 | Minerva ON (BEEF3) | 74 | Petrorecsa ON (RECV3) |
| 21 | Marfrig ON (MBRF3) | 48 | SLC Agricola ON (SLCE3) | 75 | Vivara S.A. ON (VIVA3) |
| 22 | Motiva SA ON (MOTV3) | 49 | Braskem PNA (BRKM5) | 76 | Magaz Luiza ON (MGLU3) |
| 23 | Engie Brasil ON (EGIE3) | 50 | Usiminas PNA (USIM5) | 77 | Cea Modas ON (CEAB3) |
| 24 | Lojas Renner ON (LREN3) | 51 | Yduqs Part ON (YDUQ3) | 78 | P.Acucar-Cbd ON (PCAR3) |
| 25 | Isa Energia PN (ISAE4) | 52 | Gerdau Met PN (GOAU4) | 79 | Vamos ON (VAMO3) |
| 26 | Santander BR UNT (SANB11) | 53 | BBSeguridade ON (BBSE3) | 80 | Raizen PN (RAIZ4) |
| 27 | Multiplan ON (MULT3) | 54 | Ultrapar ON (UGPA3) | 81 | Cvc Brasil ON (CVCB3) |


# Fonte dos Dados
Os dados serão obtidos da Economática, consistindo dos dados de fechamento ajustado diáro, de todo o período disponível, dentro da janela temporal de 2010 a 2024.

# Tratamendo dos dados

Os dados do fechamento ajustado serão tratados calculando o retorno logarítmico diário.

# Desenho Experimental
# 
Será utilizada uma Janela Deslizante de 60 meses (Moving* Window*), que no primeiro momento será composta pelo ano de 2010 a 2014, e posteriormente expandirá a cada mês.
O Período de Teste será de 1 mês.
A **Frequência de Rebalanceamento **da carteira será mensal, para capturar as novas previsões dos modelos sem gerar custos de transação excessivos.

# Modelagem dos *Inputs* (As Três Carteiras)


Para cada período de rebalanceamento no *backtest*, como os *inputs* (Retorno µ e Matriz de Covariância Σ) serão calculados expandindo a janela até o mes anterior.
**A**** Matriz de Covariância ****s**erá a mesma para todas as carteiras.

| Metodologia |  |
| --- | --- |
| Input 1 | (Baseline 1: Ingênuo) |
| Input 2 | П (Baseline 2: Equilibrio de Mercado/Neutro) |
| Input 3 | (Sintese: П + Visão ) |
| Input 4 | (Sintese: П + Visão ) |
| Otimizador 1 | M-V (Markowitz) |
| Otimizador 2 | PMPT (CVaR) |
| Hipotese | "A síntese Bayesiana de informações (mercado + previsão ponderada pela confiança) gera um input superior, que por sua vez gera uma carteira mais robusta, especialmente quando usada com um otimizador (CVaR) que respeita o tail risk." |


# Processo de Otimização (O Método de Markowitz)
O portfólio de Markowitz a ser montado será a Carteira de **Máximo Índice de Sharpe**** e a Média Variância**. A *proxy* para a Taxa Livre de Risco será a Selic, o CDI e o Ibovespa.
Os Portifólios PMPT serão montados com o máximo índice de Sortino, mínimo CVaR. Os portifólios Black-Litterman serão montados com o auxilio do MAD , para  ARIMA, LSTM e Máximo Indice de Sharpe. 
As **restrições**** serão carteira **100% comprados, proibição de vendas a descoberto.
# Métricas de Avaliação de Desempenho
As carteiras serão comparadas das seguintes formas:
**Retorno:** Retorno Total Acumulado e Retorno Médio Anualizado.
- **Risco (MPT):** Volatilidade (Desvio Padrão) Anualizada.
- **Risco (PMPT):** Semivariância Anualizada e Máximo *Drawdown*.
- **Retorno/Risco (MPT):** Índice de Sharpe.
- **Retorno/Risco (PMPT):** Índice de Sortino.
- **Benchmarks:** Comparar contra Selic, IBOVESPA e CDI.


# 
# 
# ANÁLISE E DISCUSSÃO DOS RESULTADOS

# Estatísticas Descritivas dos Dados
- 
- 
- Descrição da Amostra Final:
- Total de Ativos (Tickers): 81
- Total de Setores B3 Representados: 11.
- 2. Distribuição por Setor B3 (Contagem)A tabela a seguir mostra o número exato de empresas pertencentes a cada um dos 10 Setores identificados na sua amostra

Distribuição por Setor B3 (Contagem)


| Setor B3 | Quantidade de Ativos | % do Total da Amostra |
| --- | --- | --- |
| Financeiro | 18 | 22,22% |
| Utilidade Pública | 14 | 17,28% |
| Consumo Cíclico | 13 | 16,05% |
| Materiais Básicos | 9 | 11,11% |
| Consumo Não Cíclico | 9 | 11,11% |
| Petróleo, Gás e Biocombustíveis | 7 | 8,64% |
| Bens Industriais | 6 | 7,41% |
| Saúde | 5 | 6,17% |
| Imobiliário | 4 | 4,94% |
| Comunicações | 2 | 2,47% |
| TOTAL | 81 | 100,00% |


Distribuição por Subsetor (Top 5)


| Subsetor B3 | Quantidade de Ativos | Setor Principal |
| --- | --- | --- |
| Intermediários Financeiros (Bancos) | 8 | Financeiro |
| Energia Elétrica | 12 | Utilidade Pública |
| Construção Civil | 5 | Consumo Cíclico |
| Mineração | 3 | Materiais Básicos |
| Alimentos Processados | 3 | Consumo Não Cíclico |


Análise da Normalidade dos Dados

A análise das estatísticas descritivas  revela, de forma conclusiva, que os retornos diários dos ativos no mercado brasileiro não seguem uma distribuição normal, o que corrobora as críticas à MPT (discutidas no Capítulo 2) e justifica a abordagem desta pesquisa. 

Dois indicadores principais confirmam essa constatação:

- **Assimetria (Skewness):** Uma distribuição normal é perfeitamente simétrica (assimetria igual a 0). Na amostra , a maioria dos ativos apresenta valores de assimetria diferentes de zero. Ativos como Petrobras (PETR4: -0,94), Weg (WEGE3: -0,45) e, de forma mais extrema, Natura (NATU3: -0,98) e Pão de Açúcar (PCAR3: -3,23), exibem assimetria negativa. Isso indica que, embora os retornos médios diários sejam positivos, a "cauda esquerda" da distribuição é mais longa, sugerindo que grandes perdas são comparativamente mais frequentes do que grandes ganhos de magnitude similar. Em contrapartida, ativos como Eletrobras (ELET3: 0,59) e Suzano (SUZB3: 0,35) mostram assimetria positiva.

- **Curtose (Kurtosis):** Este é o indicador mais crítico. A curtose mede o "achatamento" da distribuição e o peso de suas caudas. Uma distribuição normal possui uma curtose excessiva (Excess Kurtosis) de 0. Os dados da amostra  demonstram valores de curtose dramaticamente elevados para quase todos os ativos, um fenômeno conhecido como leptocurtose.

Valores leptocúrticos (muito maiores que 0) significam que a distribuição dos retornos é mais "pontuda" no centro e possui "caudas pesadas", que pode indicar que eventos extremos (tanto grandes perdas quanto grandes ganhos) ocorrem com uma frequência muito maior do que a teoria de distribuição normal (usada pela MPT clássica) prevê.

Na amostra , observa-se que mesmo ativos de grande liquidez apresentam alta curtose, como Vale (VALE3: 9,40), Petrobras (PETR4: 14,13) e Eletrobras (ELET3: 15,49). Alguns casos são extremos, como BB Seguridade (BBSE3: 790,65), Assaí (ASAI3: 2469,69) e Pão de Açúcar (PCAR3: 408,26), refletindo períodos de volatilidade extrema ou eventos idiossincráticos.   

Implicações para a Pesquisa
A constatação empírica de que os retornos dos ativos brasileiros são assimétricos e fortemente leptocúrticos  fornece a justificativa central para este trabalho. A falha da premissa de normalidade valida: 
- O uso de métricas de risco da Pós-Moderna Teoria de Carteiras (PMPT), como o Índice de Sortino, que focam no risco de downside (semivariância) em vez da variância total.
- A exploração de modelos preditivos (ARIMA e, especialmente, LSTM), que são mais adequados para capturar as dinâmicas não-lineares, a assimetria e os padrões temporais que a simples média histórica e a variância não conseguem modelar


# 
# Resultados do *Backtest* (Comparação de Desempenho)
# 
Apresentar o gráfico da evolução do patrimônio (R$ 100,00 iniciais) ao longo do tempo (Período de Teste) para as 3 carteiras + 2 benchmarks (IBOV, CDI). Este é o gráfico principal.
Apresentar a tabela-resumo que responde à pergunta de pesquisa.


# CONCLUSÃO


# 6 CRONOGRAMA


| ATIVIDADES | ATIVIDADES | Março | Abril | Maio | Junho | Julho |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Entrega da carta de aceite |  |  |  |  |  |
| 2 | Realização da matricula pela secretaria acadêmica |  |  |  |  |  |
| 3 | Definição do tema do projeto |  |  |  |  |  |
| 4 | Definição da estrutura |  |  |  |  |  |
| 5 | Realização do Tópico 1 do referencial teórico |  |  |  |  |  |
| 6 | Realização do Tópico 2 do referencial teórico |  |  |  |  |  |
| 7 | Introdução |  |  |  |  |  |
| 8 | Introdução Ajustes finais da introdução |  |  |  |  |  |
| 9 | Metodologia Definição do modelo e operacionalização da pesquisa |  |  |  |  |  |
| 10 | Metodologia Ajuste final da metodologia |  |  |  |  |  |
| 10 | Entrega - Formatação ABNT |  |  |  |  |  |

Tabela 1 - Cronograma da Pesquisa


# 7-REFERÊNCIAS


Berk, J.; Demarzo, P. & Harford, J. (2012). Fundamentals of Corporate Finance. Boston: Prentice Hall.

Bodie, Z., Kane A., & Marcus, A. J. (2011). Investments. New York: McGraw-Hill/Irwin.


CHIAN, Swee C.; TAN, Kay C.; MAMUM, Abdullah Al. Evolutionary multi-objective
portfolio optimization in practical context. International Journal of Automation and
Computing, v. 5, p. 67-80, 2008.

Damodaran, A. (2007). Strategic Risk Taking: A Framework for Risk Management. London: FT Press.

DEMIGUEL, Victor; NOGALES, Francisco J. Portfolio selection with robust
estimation. Operations Research, v. 57, n. 3, p. 560-577, 2009.


Elton, E. J., Gruber, M. J., Brown, S. J. & Goetzmann, W. N. (2012). Moderna Teoria de Carteiras e Análise de Investimentos. Rio de Janeiro: Elsevier.

Elton, E. J., & Gruber, M. J. (1997). Modern portfolio theory, 1950 to date. Journal of Banking & Finance, 21(17), 1743-1759.

Fabozzi, F. J., & Markowitz, H. M. (2011). The Theory and Practice of Investment Management. Hoboken: John Wiley & Sons.

Gitman, L. J. (2010). Princípios de Administração Financeira (12ª ed.). São Paulo: Pearson.

Markowitz, H. M. (1952). Portfolio Selection. Journal of Finance, 7(1), 77-91.

Markowitz, H. (1959). Portfolio Selection: Efficient Diversification of Investments. New York: John Wiley & Sons.

Reilly, F. K., & Brown, K. C. (2011). Investment Analysis & Portfolio Management. Mason: South-Western Cengage Learning.

Rockafellar, R. T., & Uryasev, S. (2002). Conditional value-at-risk for general loss distributions. Journal of Banking & Finance, 26(7), 1443-1471.

SANTOS, André A. P.; TESSARI, Cristina. Técnicas quantitativas de otimização de carteiras
aplicadas ao mercado de ações brasileiro. Revista Brasileira de Finanças, v. 10, n. 3, p. 369-
393, 2012.

Vernimmen, P., Quiry, P., Dallocchio, M., Le Fur, Y., & Salvi, A. (2014). Corporate Finance: Theory and Practice. Hoboken: Wiley.
