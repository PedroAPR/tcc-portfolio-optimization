# Capítulo 1: Fundamentação Teórica e Revisão Bibliográfica da Moderna Teoria do Portfólio


## 1. Introdução: A Evolução Histórica da Gestão de Investimentos

A compreensão contemporânea dos mercados financeiros e a gestão de ativos apoiam-se sobre um edifício teórico construído em meados do século XX, cujos alicerces foram lançados por Harry Markowitz. No entanto, para apreciar a magnitude da revolução intelectual provocada pela Teoria Moderna do Portfólio (Modern Portfolio Theory - MPT), é imperativo contextualizar o ambiente acadêmico e profissional que a precedeu. Antes de 1952, a gestão de investimentos carecia de uma estrutura formalizada para o tratamento do risco e da diversificação, operando sob paradigmas que privilegiavam a seleção individual de ativos em detrimento da construção holística de carteiras.

### 1.1 O Paradigma Pré-Markowitz: A Era da Seleção de Ativos

No período que antecedeu a década de 1950, a literatura financeira e a prática de mercado eram dominadas pela doutrina da "análise de segurança" (*security analysis*). A obra seminal de John Burr Williams, *The Theory of Investment Value* (1938), estabeleceu o Modelo de Desconto de Dividendos (Dividend Discount Model - DDM) como a ferramenta primária de avaliação.1 Williams postulou que o valor intrínseco de uma ação deveria ser igual ao valor presente dos seus dividendos futuros, descontados a uma taxa de juros apropriada que refletisse o custo do dinheiro e o risco do negócio.1
Sob essa ótica, a tarefa do investidor resumia-se a identificar ativos subvalorizados – aqueles cujos preços de mercado estivessem abaixo do seu valor intrínseco calculado. O risco era tratado de forma qualitativa ou através de ajustes na taxa de desconto, sem uma medida estatística precisa de incerteza baseada na dispersão de retornos.1 A diversificação, embora praticada intuitivamente e recomendada por adágios populares como "não coloque todos os ovos na mesma cesta", não possuía uma justificativa matemática rigorosa.3 A visão predominante era a de que, se um investidor pudesse identificar o ativo com o maior valor presente líquido ou o maior retorno esperado, a lógica da maximização de riqueza ditaria a concentração total de recursos nesse único ativo.2
A ausência de uma definição operacional de risco como uma variável quantificável permitia um hiato entre a teoria e a prática. Enquanto a teoria de Williams sugeria concentração (para maximizar o retorno), a prática observada mostrava investidores mantendo carteiras diversificadas. Esse paradoxo evidenciava a necessidade de um modelo que explicasse a aversão ao risco e formalizasse o benefício da diversificação, não apenas como uma defesa contra a ignorância, mas como uma estratégia ótima de alocação de capital.5

### 1.2 A Transição para a Análise Quantitativa

O final da década de 1940 testemunhou o início da aplicação de métodos estatísticos e de pesquisa operacional à economia. Foi neste cenário que Harry Markowitz, então doutorando na Universidade de Chicago, buscou aplicar conceitos de programação linear e estatística ao problema da escolha de investimentos. Ao analisar a obra de Williams, Markowitz percebeu que a variância dos retornos – uma medida de dispersão em torno da média – poderia servir como uma *proxy* matemática tratável para o risco financeiro.5 Essa percepção permitiu a transição da gestão de investimentos de uma "arte" baseada em julgamentos subjetivos para uma "ciência" baseada em otimização numérica, estabelecendo o terreno para o que viria a ser conhecido como a Teoria Moderna do Portfólio.

## 2. A Revolução de Markowitz: O Modelo Média-Variância

A publicação do artigo "Portfolio Selection" no *Journal of Finance* em março de 1952 marcou o nascimento oficial da MPT.5 Neste trabalho, Markowitz rejeitou a hipótese de que os investidores deveriam apenas maximizar os retornos esperados, propondo em seu lugar uma estrutura de decisão bicritério: a análise Média-Variância.

### 2.1 A Rejeição da Maximização Pura do Retorno

Markowitz argumentou que a regra de maximização do valor presente dos retornos futuros era inadequada porque ignorava a variância dos retornos, que ele associou ao risco. Se os investidores apenas maximizassem o retorno, eles jamais diversificariam; eles simplesmente manteriam o único ativo com a maior expectativa de retorno.2 Para racionalizar a diversificação, Markowitz introduziu a suposição de que os investidores consideram o retorno esperado uma coisa desejável e a variância do retorno uma coisa indesejável.2
Esta formulação implica que os investidores são, por natureza, avessos ao risco. Para aceitar um nível maior de incerteza (variância), eles exigem uma compensação na forma de maior retorno esperado. O problema da seleção de portfólio transformou-se, portanto, em um problema de otimização: minimizar a variância do portfólio para um dado nível de retorno esperado, ou maximizar o retorno esperado para um dado nível de variância.5

### 2.2 O Conceito de Risco como Variância

A escolha da variância (ou seu equivalente, o desvio padrão) como medida de risco foi uma simplificação pragmática crucial. Embora o risco real para um investidor possa incluir a probabilidade de ruína ou a falha em atingir objetivos financeiros (downside risk), a variância oferece propriedades algébricas que permitem a manipulação analítica de portfólios compostos por múltiplos ativos.2
Sob a estrutura Média-Variância, o risco de um portfólio não é simplesmente a soma dos riscos dos ativos individuais. Markowitz demonstrou que o risco de um portfólio depende crucialmente de como os ativos interagem entre si – especificamente, de suas covariâncias. A intuição central é que o risco de um ativo individual deve ser avaliado não por sua volatilidade isolada, mas por sua contribuição marginal ao risco total do portfólio.5 Um ativo altamente volátil pode, paradoxalmente, reduzir o risco de um portfólio se seus retornos não estiverem correlacionados ou forem negativamente correlacionados com os demais ativos da carteira.9

## 3. Risco, Retorno e Covariância: A Matemática da Diversificação

A formalização matemática proposta por Markowitz permitiu quantificar exatamente como a diversificação reduz o risco. A análise baseia-se em três estatísticas fundamentais derivadas de séries históricas de preços ou de projeções probabilísticas: o retorno esperado (média), o risco (variância/desvio padrão) e a interdependência (covariância/correlação).

### 3.1 Retorno Esperado do Portfólio

O retorno esperado de um portfólio, denotado por $E(R_p)$, é a média ponderada dos retornos esperados dos ativos individuais que o compõem. Para um portfólio com $n$ ativos, onde $w_i$ representa o peso do ativo $i$ na carteira (tal que $\sum w_i = 1$) e $E(R_i)$ é o retorno esperado do ativo $i$, temos:

$$E(R_p) = \sum_{i=1}^{n} w_i E(R_i)$$
Esta relação linear indica que a diversificação não altera o potencial de retorno médio do portfólio além da simples ponderação dos ativos. Não há "ganho mágico" de retorno através da diversificação; o benefício reside inteiramente na redução do risco.7

### 3.2 Variância e Covariância

A inovação de Markowitz reside na fórmula da variância do portfólio ($\sigma_p^2$). Ao contrário do retorno, o risco do portfólio não é uma média ponderada linear dos riscos individuais. A variância é dada por:
$$ \sigma_p^2 = \sum_{i=1}^{n} w_i^2 \sigma_i^2 + \sum_{i=1}^{n} \sum_{j=1, j \neq i}^{n} w_i w_j \sigma_{ij} $$
Onde:
$\sigma_i^2$ é a variância do ativo $i$.
$\sigma_{ij}$ é a covariância entre os retornos dos ativos $i$ e $j$.
A covariância pode ser expressa em termos do coeficiente de correlação ($\rho_{ij}$) e dos desvios padrão individuais: $\sigma_{ij} = \rho_{ij} \sigma_i \sigma_j$. Assim, a equação expandida torna-se:
$$ \sigma_p^2 = \sum_{i=1}^{n} w_i^2 \sigma_i^2 + \sum_{i=1}^{n} \sum_{j=1, j \neq i}^{n} w_i w_j \rho_{ij} \sigma_i \sigma_j $$
Esta equação revela o mecanismo da diversificação:
**Termo de Variância Individual:** O primeiro somatório representa a contribuição do risco isolado de cada ativo. À medida que $n$ aumenta, os pesos $w_i$ diminuem (assumindo pesos iguais, $w_i = 1/n$, então $w_i^2 = 1/n^2$), fazendo com que este termo tenda a zero rapidamente.4
**Termo de Covariância:** O segundo somatório (duplo) representa as interações entre os pares de ativos. Como existem $n(n-1)$ termos de covariância contra apenas $n$ termos de variância, o risco do portfólio é dominado pelas covariâncias à medida que o número de ativos cresce.

### 3.3 O Papel da Correlação

O coeficiente de correlação ($\rho_{ij}$), que varia entre -1 e +1, é o determinante crítico da eficácia da diversificação.
Se $\rho_{ij} = 1$ (correlação positiva perfeita), não há benefício de redução de risco; o desvio padrão do portfólio é simplesmente a média ponderada dos desvios padrão dos ativos.
Se $\rho_{ij} < 1$, o desvio padrão do portfólio será menor que a média ponderada dos riscos individuais.
Se $\rho_{ij} = -1$ (correlação negativa perfeita), é teoricamente possível construir um portfólio com variância zero.2
Portanto, a MPT estabelece que o objetivo da construção de portfólio não é apenas selecionar ativos com boas perspectivas de retorno, mas selecionar ativos cujos preços não se movam em uníssono. A covariância negativa ou baixa entre ativos é o "combustível" que permite a redução do risco total sem sacrificar necessariamente o retorno esperado.4

## 4. A Fronteira Eficiente: Otimização e Geometria

A aplicação dos princípios de média-variância a todo o universo de ativos disponíveis permite a construção do "conjunto de oportunidades de investimento". Dentro deste conjunto, Markowitz identificou um subconjunto ótimo de portfólios, conhecido como **Fronteira Eficiente**.5

### 4.1 Derivação e Definição

A Fronteira Eficiente é o locus geométrico dos portfólios que oferecem o máximo retorno esperado para cada nível de risco, ou o mínimo risco para cada nível de retorno esperado.5 Matematicamente, a fronteira é derivada resolvendo um problema de otimização quadrática: minimizar $\sigma_p^2$ sujeito a um retorno alvo fixo $E(R_p) = \mu$ e à restrição orçamentária $\sum w_i = 1$.12
O resultado dessa otimização, quando plotado em um gráfico com o Risco (Desvio Padrão) no eixo horizontal e o Retorno Esperado no eixo vertical, forma uma curva côncava (hiperbólica no espaço média-desvio padrão).13 Todos os portfólios que se situam abaixo desta curva são considerados "ineficientes" ou "dominados", pois existe uma combinação alternativa de ativos que oferece um perfil risco-retorno superior.14

### 4.2 O Portfólio de Mínima Variância Global

O vértice esquerdo da hipérbole é denominado Portfólio de Mínima Variância Global (Global Minimum Variance Portfolio - GMVP). Este ponto representa a combinação de ativos que resulta no menor risco absoluto possível, independentemente do retorno.15 A Fronteira Eficiente compreende apenas o segmento da curva que parte do GMVP e se estende para cima e para a direita. O segmento inferior da hipérbole (abaixo do GMVP) é ineficiente, pois para qualquer ponto nesta região, existe um ponto na parte superior com o mesmo risco, mas maior retorno.15
A curvatura da fronteira eficiente reflete o princípio dos retornos marginais decrescentes do risco: para obter incrementos adicionais de retorno esperado, o investidor deve aceitar incrementos cada vez maiores de risco.16 A localização ótima de um investidor específico ao longo desta fronteira, na ausência de um ativo livre de risco, seria determinada pela tangência entre a fronteira eficiente e as curvas de indiferença da função de utilidade do investidor, refletindo seu grau pessoal de aversão ao risco.17

## 5. O Ativo Livre de Risco e o Teorema da Separação

A estrutura original de Markowitz considerava apenas ativos com risco. Em 1958, James Tobin expandiu significativamente a teoria ao introduzir o conceito de um ativo livre de risco (*risk-free asset*) e analisar suas implicações para a escolha de portfólio.18

### 5.1 O Ativo Livre de Risco

Um ativo livre de risco é definido teoricamente como um investimento com variância zero ($\sigma_{rf} = 0$) e, consequentemente, covariância zero com qualquer ativo de risco ($\sigma_{i,rf} = 0$).20 Na prática acadêmica e de mercado, títulos soberanos de curto prazo de economias estáveis (como *T-Bills* nos EUA ou *Tesouro Selic* no Brasil) são utilizados como *proxies* para este ativo.21
A introdução deste ativo altera o conjunto de oportunidades de investimento. O investidor não está mais restrito à curva hiperbólica da fronteira eficiente de ativos de risco; ele pode agora combinar o ativo livre de risco com qualquer portfólio de ativos arriscados. Essa combinação gera uma relação linear entre risco e retorno.20

### 5.2 O Teorema da Separação de Tobin

A contribuição mais profunda de Tobin foi o **Teorema da Separação**. Este teorema postula que a decisão de investimento pode ser decomposta em dois passos distintos e independentes 18:
**A Decisão Técnica (Otimização):** Identificar o portfólio ótimo de ativos de risco. Este portfólio é o ponto onde uma linha reta partindo da taxa livre de risco ($R_f$) tangencia a fronteira eficiente de Markowitz. Este portfólio de tangência é conhecido como o **Portfólio de Mercado** e é puramente determinado pelas estatísticas dos ativos (retornos, variâncias, covariâncias), sendo independente das preferências de risco do investidor.
**A Decisão de Alocação (Preferência):** Uma vez identificado o Portfólio de Mercado, o investidor decide como dividir seu capital entre este portfólio arriscado e o ativo livre de risco. Investidores conservadores alocarão uma grande parte em ativos livres de risco e uma pequena parte no portfólio de mercado; investidores agressivos podem até tomar emprestado à taxa livre de risco (alavancagem) para investir mais de 100% de seu capital no portfólio de mercado.19

### 5.3 A Reta do Mercado de Capitais (Capital Market Line - CML)

A linha reta que conecta a taxa livre de risco ao Portfólio de Mercado na fronteira eficiente é denominada **Capital Market Line (CML)**. A CML representa a nova fronteira eficiente na presença de um ativo sem risco. Todos os investidores racionais devem situar seus portfólios sobre esta reta.23
A equação da CML é dada por:
$$E(R_p) = R_f + \sigma_p \left$$
O termo entre colchetes representa o preço de mercado do risco: o retorno excedente que o mercado paga por unidade de risco total ($\sigma$). A CML demonstra que o retorno esperado de um portfólio eficiente é composto pela taxa livre de risco mais um prêmio pelo risco total assumido.20 Portfólios que estão na fronteira eficiente original de Markowitz (mas abaixo da CML) tornam-se subótimos, pois a combinação linear oferecida pela CML proporciona um retorno superior para o mesmo nível de risco.26

## 6. Avaliação de Desempenho: O Índice de Sharpe

A consolidação da CML e da importância do trade-off entre risco e retorno criou a necessidade de métricas padronizadas para comparar o desempenho de diferentes investimentos. Em 1966, William F. Sharpe introduziu o "reward-to-variability ratio", hoje universalmente conhecido como **Índice de Sharpe**.27

### 6.1 Definição e Interpretação

O Índice de Sharpe mensura o excesso de retorno de um portfólio sobre a taxa livre de risco, normalizado pelo seu risco total (desvio padrão). A fórmula é expressa como:

$$S_p = \frac{E(R_p) - R_f}{\sigma_p}$$
Geometricamente, o Índice de Sharpe corresponde à inclinação da reta que conecta a taxa livre de risco ao portfólio analisado no plano risco-retorno. O Portfólio de Mercado (o ponto de tangência da CML) é, por definição, o portfólio que possui o maior Índice de Sharpe possível entre todas as combinações de ativos de risco.29

### 6.2 Importância e Aplicação

Esta métrica revolucionou a avaliação de gestores de fundos. Antes do Índice de Sharpe, comparavam-se fundos apenas pelos seus retornos absolutos. Sharpe mostrou que um retorno mais alto não implica necessariamente uma gestão superior se foi obtido através da exposição a níveis desproporcionais de risco. O índice permite "ajustar pelo risco" os retornos, nivelando o campo de jogo e permitindo comparações justas entre estratégias conservadoras e agressivas.21 Um índice de Sharpe elevado indica que o investidor está sendo eficientemente recompensado por cada unidade de volatilidade suportada.

## 7. O Modelo de Precificação de Ativos de Capital (CAPM)

Enquanto a MPT de Markowitz e a análise de Tobin eram teorias normativas (prescrevendo como os investidores *deveriam* agir), o **Capital Asset Pricing Model (CAPM)** surgiu na década de 1960 como uma teoria positiva de equilíbrio, descrevendo como os preços dos ativos se comportariam se todos os investidores seguissem as recomendações da MPT.32

### 7.1 Origem e Desenvolvedores

O CAPM foi desenvolvido de forma independente e quase simultânea por William Sharpe (1964), John Lintner (1965), Jan Mossin (1966) e Jack Treynor (1962). Este esforço intelectual coletivo buscou determinar qual seria o retorno de equilíbrio de um ativo individual num mercado dominado por investidores diversificadores.34

### 7.2 Decomposição do Risco: Sistemático vs. Não Sistemático

A contribuição central do CAPM é a distinção entre dois tipos de risco:
**Risco Não Sistemático (Idiossincrático/Diversificável):** O risco específico de uma empresa ou setor. Como demonstrado por Markowitz, este risco pode ser eliminado quase inteiramente através da diversificação eficiente. Portanto, em um mercado competitivo, os investidores não devem ser remunerados por assumir riscos que podem ser eliminados sem custo.23
**Risco Sistemático (De Mercado/Não Diversificável):** O risco inerente a todo o sistema econômico (ex: variações na taxa de juros, recessões, choques inflacionários). Este risco não pode ser eliminado pela diversificação.
O CAPM postula que o mercado remunera *apenas* a exposição ao risco sistemático. O risco total ($\sigma$) torna-se irrelevante para a precificação de ativos individuais, sendo substituído pelo conceito de **Beta ($\beta$)**.16

### 7.3 O Coeficiente Beta e a Reta do Mercado de Títulos (SML)

O Beta mede a sensibilidade dos retornos de um ativo em relação aos movimentos do Portfólio de Mercado. É definido como:

$$\beta_i = \frac{\text{Cov}(R_i, R_M)}{\sigma_M^2}$$
A relação fundamental do CAPM é expressa pela equação da **Security Market Line (SML)**:

$$E(R_i) = R_f + \beta_i$$
A SML difere fundamentalmente da CML. Enquanto a CML usa o desvio padrão ($\sigma$) no eixo horizontal e aplica-se apenas a portfólios eficientes (sem risco não sistemático), a SML usa o Beta ($\beta$) no eixo horizontal e aplica-se a *qualquer* ativo ou portfólio, eficiente ou não.23
Um ativo com $\beta = 1$ tem o mesmo risco sistemático que o mercado.
Um ativo com $\beta > 1$ é mais volátil que o mercado (agressivo).
Um ativo com $\beta < 1$ é menos volátil que o mercado (defensivo).
Segundo o CAPM, em equilíbrio, todos os ativos devem estar situados sobre a SML. Qualquer ativo acima da linha estaria "barato" (oferecendo retorno excessivo para seu risco sistemático), e qualquer ativo abaixo estaria "caro".25

## 8. Pressupostos, Críticas e Limitações Teóricas

A elegância matemática da MPT e do CAPM baseia-se em um conjunto de pressupostos simplificadores que têm sido objeto de intenso debate acadêmico e testes empíricos.

### 8.1 Pressupostos Fundamentais

As teorias pressupõem 39:
**Racionalidade:** Investidores são agentes racionais avessos ao risco que buscam maximizar a utilidade da riqueza esperada.
**Distribuição Normal:** Os retornos dos ativos seguem uma distribuição normal, sendo completamente descritos por média e variância.
**Mercados Perfeitos:** Não existem custos de transação, impostos ou restrições a vendas a descoberto. Ativos são infinitamente divisíveis e a informação é gratuita e instantânea.
**Expectativas Homogêneas:** Todos os investidores concordam sobre os retornos esperados, variâncias e covariâncias dos ativos.

### 8.2 Limitações e a Realidade dos Mercados

Críticos apontam que a distribuição dos retornos financeiros no mundo real frequentemente exibe "caudas gordas" (*fat tails*) e assimetria, violando a suposição de normalidade e subestimando a probabilidade de eventos extremos (*crashes*).29 Além disso, a escola de Finanças Comportamentais desafia a premissa de racionalidade, demonstrando que vieses cognitivos influenciam as decisões de investimento de forma sistemática.
A suposição de correlações estáticas também é problemática; em momentos de crise financeira, as correlações entre ativos tendem a convergir para 1, reduzindo os benefícios da diversificação justamente quando eles são mais necessários.39 Apesar destas limitações, a Teoria Moderna do Portfólio permanece a pedra angular das finanças acadêmicas e o ponto de partida para modelos mais complexos de gestão de risco e precificação de ativos.6

### Tabela Resumo: Comparação entre CML e SML


| Característica | Capital Market Line (CML) | Security Market Line (SML) |
| --- | --- | --- |
| Medida de Risco | Desvio Padrão Total ($\sigma$) | Beta Sistemático ($\beta$) |
| Aplicação | Apenas Portfólios Eficientes | Qualquer Ativo ou Portfólio |
| Definição de Risco | Risco Total (Sistemático + Idiossincrático) | Apenas Risco Sistemático |
| Ponto de Intercepto | Taxa Livre de Risco ($R_f$) | Taxa Livre de Risco ($R_f$) |
| Inclinação (Slope) | Índice de Sharpe do Mercado | Prêmio de Risco de Mercado ($R_M - R_f$) |
| Contexto Teórico | Teorema da Separação de Tobin | Modelo CAPM |

Este capítulo consolidou os fundamentos teóricos necessários para a análise subsequente. A transição do paradigma de seleção de ações de Williams para a alocação de ativos baseada em covariância de Markowitz, refinada pela separação de Tobin e pelo modelo de equilíbrio do CAPM, constitui a base da moderna gestão financeira. Estes conceitos fornecem a linguagem e as métricas essenciais para a construção, análise e avaliação de portfólios de investimento no contexto contemporâneo.
#### Referências citadas
Understanding The History Of The Modern Portfolio - Investopedia, acessado em novembro 27, 2025, 
Portfolio Selection Harry Markowitz The Journal of Finance, Vol. 7, No. 1. (Mar., 1952), pp. 77-91., acessado em novembro 27, 2025, 
Harry Markowitz: The Father of Modern Portfolio Theory | Index Fund Advisors, Inc., acessado em novembro 27, 2025, 
The Evolution of Modern Portfolio Theory for the Institutional Investor - NMS Management, acessado em novembro 27, 2025, 
Modern portfolio theory - Wikipedia, acessado em novembro 27, 2025, 
Harry M. Markowitz: Father of modern finance - Invesco, acessado em novembro 27, 2025, 
Modern Portfolio Theory: What MPT Is and How Investors Use It - Investopedia, acessado em novembro 27, 2025, 
Modern Portfolio Theory (MPT) - Overview, Diversification - Corporate Finance Institute, acessado em novembro 27, 2025, 
Harry Markowitz's Modern Portfolio Theory: The Efficient Frontier - GuidedChoice, acessado em novembro 27, 2025, 
teoria moderna de carteiras - Repositório Institucional - Universidade Federal de Uberlândia, acessado em novembro 27, 2025, 
Understanding the Efficient Frontier: Maximize Returns, Minimize Risk - Investopedia, acessado em novembro 27, 2025, 
Geometry of the Efficient Frontier - Gregory Gundersen, acessado em novembro 27, 2025, 
An analytical derivation of the efficient surface in portfolio selection with three criteria - Terry College of Business, acessado em novembro 27, 2025, 
Chapters 21 & 22 Modern Portfolio Theory & Equilibrium Asset Pricing - DSpace@MIT, acessado em novembro 27, 2025, 
Lecture 07: Mean-Variance Analysis & Variance Analysis & Capital Asset Pricing Model (CAPM) (CAPM), acessado em novembro 27, 2025, 
The Capital Asset Pricing Model: Theory and Evidence - Tuck School of Business, acessado em novembro 27, 2025, 
TEORIA MODERNA DE PORTFÓLIO APLICADA AO MERCADO BRASILEIRO. MARKOWITZ VS DIVERSIFICAÇÃO INGÊNUA - Insper, acessado em novembro 27, 2025, 
Capital Market Line - GlynHolton.com, acessado em novembro 27, 2025, 
Universidade de Brasília Faculdade de Administração, Contabilidade, Economia e Gestão de Políticas Públicas Departamento d - BDM UnB, acessado em novembro 27, 2025, 
The Capital Market Theory: Markowitz, CML, and Separation Theorem - ResearchGate, acessado em novembro 27, 2025, 
What Is the Sharpe Ratio? - Morningstar Community, acessado em novembro 27, 2025, 
manualmoedamercados.pdf.txt, acessado em novembro 27, 2025, 
Understanding Capital Market Line (CML) and How to Calculate It - Investopedia, acessado em novembro 27, 2025, 
Tobin's Separation Theorem - It Can Be Applied Anywhere - IASG, acessado em novembro 27, 2025, 
UNIVERSIDADE DE SÃO PAULO FACULDADE DE ECONOMIA, ADMINISTRAÇÃO E CONTABILIDADE DEPARTAMENTO DE ADMINISTRAÇÃO PROGRAMA DE P - Biblioteca Digital de Teses e Dissertações da USP, acessado em novembro 27, 2025, 
UFSC CENTRO SÓCIO-ECONÔMICO - CSE DEPARTAMENTO DE ECONOMIA E RELAÇÕES INTERNACIO, acessado em novembro 27, 2025, 
acessado em novembro 27, 2025, 
Sharpe ratio - Wikipedia, acessado em novembro 27, 2025, 
A Brief History of Sharpe Ratio and Beyond - Elm Wealth, acessado em novembro 27, 2025, 
The Sharpe Ratio - Stanford University, acessado em novembro 27, 2025, 
Calculate the Sharpe Ratio to Gauge Risk | Charles Schwab, acessado em novembro 27, 2025, 
The Capital Asset Pricing Model - American Economic Association, acessado em novembro 27, 2025, 
Capital Asset Pricing Model (CAPM) - SimTrade blog, acessado em novembro 27, 2025, 
Capital asset pricing model - Wikipedia, acessado em novembro 27, 2025, 
APUBEF Proceedings - Fall 2006 A BRIEF HISTORY OF THE CAPITAL ASSET PRICING MODEL Edward J. Sullivan, Lebanon Valley College ABS - NABET, acessado em novembro 27, 2025, 
What is the difference between the CML vs SML? - Fitch Learning Support, acessado em novembro 27, 2025, 
SML vs CML: Understanding the Key Differences - Bajaj Broking, acessado em novembro 27, 2025, 
SML vs CML: Key Differences for Investors | Kotak Securities, acessado em novembro 27, 2025, 
Definition and Assumptions of Modern Portfolio Theory - College Hive, acessado em novembro 27, 2025, 
Modern Portfolio Theory (MPT) and the Capital Asset Pricing Model - MidhaFin(MF), acessado em novembro 27, 2025, 
Modern Portfolio Theory Explained: A Guide to MPT for Investors - Range.com, acessado em novembro 27, 2025, 
CAPM - Modern Portfolio Theory - Zoo | Yale University, acessado em novembro 27, 2025,
