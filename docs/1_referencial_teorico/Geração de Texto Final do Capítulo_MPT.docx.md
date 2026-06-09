

# **Capítulo 1: Fundamentação Teórica e Revisão Bibliográfica da Moderna Teoria do Portfólio**

## **1\. Introdução: A Evolução Histórica da Gestão de Investimentos**

A gestão de investimentos, historicamente uma arte dominada pela intuição e pela análise fundamentalista idiossincrática, sofreu uma revolução paradigmática em meados do século XX. Antes do advento da Teoria Moderna do Portfólio (Modern Portfolio Theory \- MPT), a prática de alocação de capital carecia de uma estrutura teórica unificada que quantificasse a relação entre risco e retorno de maneira sistemática. Este capítulo delineia a trajetória intelectual que transformou as finanças de uma disciplina descritiva em uma ciência normativa e quantitativa, culminando nos modelos de equilíbrio que sustentam a indústria global de gestão de ativos contemporânea.

### **1.1 O Paradigma Pré-Markowitz: A Era da Seleção de Ativos**

Até o início da década de 1950, a teoria de investimentos operava sob o "paradigma da seleção de ativos" (*stock picking*). A literatura seminal da época, epitomizada pelas obras de John Burr Williams e da dupla Benjamin Graham e David Dodd, focava quase exclusivamente na determinação do valor intrínseco de títulos individuais, tratando a construção do portfólio como uma consequência secundária da acumulação de ativos subavaliados.1

John Burr Williams, em sua *magnum opus* de 1938, *The Theory of Investment Value*, introduziu o Modelo de Desconto de Dividendos (Dividend Discount Model \- DDM), estabelecendo que o valor de um ativo é o valor presente de seus fluxos de caixa futuros esperados, descontados a uma taxa de juros apropriada.1 A fórmula de Williams, $V\_0 \= \\sum\_{t=1}^{\\infty} \\frac{d\_t}{(1+i)^t}$, onde $d\_t$ representa os dividendos e $i$ a taxa de desconto, proporcionou o primeiro rigor matemático para a avaliação de *equities*.3 Contudo, a abordagem de Williams sofria de uma limitação crítica: ela assumia que o risco poderia ser virtualmente eliminado através da diversificação, sem fornecer um mecanismo matemático para quantificar como a variabilidade dos retornos de diferentes ativos interagia.2 Williams focava na maximização do retorno esperado, acreditando que a "lei dos grandes números" protegeria o investidor que diversificasse suficientemente.2

Paralelamente, Benjamin Graham e David Dodd, em *Security Analysis* (1934), estabeleceram os princípios do *Value Investing*. Embora defendessem a diversificação como uma medida prudencial — sugerindo a detenção de dez a trinta papéis diferentes para mitigar o erro de análise — o conceito de risco em sua estrutura era fundamentalmente qualitativo.4 Para Graham, risco não era volatilidade, mas sim a possibilidade de perda permanente de capital decorrente da deterioração dos fundamentos da empresa ou de pagar um preço excessivo em relação ao valor intrínseco.3 A "Margem de Segurança" era a métrica de proteção, não o desvio padrão ou a covariância. Neste paradigma, o portfólio era visto como uma coleção de ativos individuais, onde cada componente era julgado por seus próprios méritos, isolado do contexto agregado da carteira.

### **1.2 A Transição para a Análise Quantitativa**

A ruptura com o paradigma da seleção individual de ativos não ocorreu abruptamente, mas foi precedida por desenvolvimentos teóricos que começaram a questionar a suficiência da maximização do valor presente. Economistas como Hicks (1939) e Marschak (1938) já exploravam as preferências sobre momentos estatísticos, e o matemático italiano Bruno de Finetti, em 1940, havia formulado um problema de alocação média-variância no contexto de resseguros, embora seu trabalho tenha permanecido desconhecido no mundo anglófono por décadas.5

O momento decisivo, contudo, surgiu da insatisfação intelectual de Harry Markowitz com a teoria vigente. Enquanto lia a obra de Williams na biblioteca da Universidade de Chicago, Markowitz teve um *insight* que desmantelaria a lógica da maximização pura do retorno.4 Ele percebeu que, se a regra de Williams fosse seguida estritamente em um mundo de incerteza, um investidor racional deveria alocar 100% de seu capital no único ativo com o maior retorno esperado descontado.6 Se dois ativos tivessem o mesmo retorno máximo, o investidor seria indiferente entre eles, mas a teoria não oferecia nenhuma razão intrínseca para manter ambos.

Markowitz identificou que a prática observada e intuitivamente racional da diversificação — "não colocar todos os ovos na mesma cesta" — era inconsistente com a teoria de maximização de valor presente de Williams.6 Para racionalizar a diversificação, era necessário introduzir uma segunda dimensão na função objetivo do investidor: o risco. A diversificação só faz sentido se o investidor estiver disposto a sacrificar uma parcela do retorno potencial para reduzir a incerteza do resultado final. Essa percepção marcou a transição da análise de títulos (*Security Analysis*) para a análise de portfólios (*Portfolio Analysis*), onde a unidade de análise deixa de ser a firma individual e passa a ser a carteira agregada.7

## **2\. A Revolução de Markowitz: O Modelo Média-Variância**

A formalização matemática dessa nova perspectiva ocorreu com a publicação do artigo "Portfolio Selection" no *Journal of Finance* em 1952, expandido posteriormente na monografia *Portfolio Selection: Efficient Diversification of Investments* (1959).9 A "Modern Portfolio Theory" (MPT) de Markowitz não apenas descreveu como os investidores agem, mas prescreveu como deveriam agir, fundamentando a decisão de investimento na interação estocástica entre ativos.

### **2.1 A Rejeição da Maximização Pura do Retorno**

A premissa fundadora da MPT é que os investidores são, simultaneamente, maximizadores de retorno e avessos ao risco.11 Markowitz rejeitou a hipótese de que os investidores consideram apenas o valor esperado (média) dos retornos futuros. Se os investidores focassem apenas na média, o conceito de um portfólio diversificado seria teoricamente injustificável, pois a diversificação quase sempre reduz o retorno esperado em comparação com a concentração no ativo de melhor desempenho.6

Portanto, a função de utilidade do investidor deve depender de dois parâmetros:

1. **Retorno Esperado ($\\mu$):** O valor médio ponderado das probabilidades dos retornos futuros.  
2. **Risco ($\\sigma$):** A dispersão ou incerteza desses retornos em torno da média.

A MPT postula que, para qualquer nível dado de risco, o investidor prefere o maior retorno possível; e para qualquer nível dado de retorno, prefere o menor risco possível. Essa estrutura de preferências cria um *trade-off* inevitável, substituindo a busca pelo "melhor ativo" pela construção do "melhor portfólio".7

### **2.2 O Conceito de Risco como Variância: Uma Escolha Pragmática**

A decisão de Markowitz de utilizar a variância (ou desvio padrão) como a medida universal de risco foi uma das escolhas mais consequentes na história das finanças, ditada tanto por conveniência matemática quanto por restrições computacionais da década de 1950\.

Em sua obra de 1959, Markowitz dedicou o Capítulo 9 para discutir uma medida alternativa de risco: a **semivariância**.12 A semivariância mensura apenas a dispersão dos retornos que caem abaixo de um determinado alvo (como a média ou zero), ignorando a volatilidade "positiva" (ganhos acima do esperado). Markowitz reconheceu explicitamente a superioridade teórica desta medida, afirmando que "a semivariância parece mais plausível do que a variância como uma medida de risco, uma vez que se preocupa apenas com desvios adversos".14 Investidores racionais não temem ganhos inesperados; eles temem perdas.

No entanto, Markowitz optou pela variância baseada em critérios de "custo, conveniência e familiaridade".12

* **Custo Computacional:** Na era dos mainframes primitivos e cartões perfurados, o custo de computação era uma barreira formidável. A otimização baseada na variância envolvia álgebra linear padrão e inversão de matrizes covariância, operações para as quais existiam algoritmos eficientes (como o *Critical Line Algorithm* desenvolvido pelo próprio Markowitz).18 A semivariância, por outro lado, exigia o dobro de dados de entrada (matrizes de semicovariância) e resultava em problemas de otimização mais complexos, onde a matriz de covariância se tornava endógena aos pesos do portfólio.12  
* **Convenência Analítica:** Se os retornos dos ativos seguirem uma distribuição normal (simétrica), a média e a variância são estatísticas suficientes para descrever toda a distribuição. Nesse caso específico, minimizar a variância é matematicamente equivalente a minimizar a semivariância.12 Markowitz apostou na aproximação normal como uma simplificação aceitável para tornar a teoria operacionalizável.

Apesar de Markowitz ter sugerido que a semivariância seria preferível com o aumento do poder computacional, a variância entrincheirou-se como o padrão da indústria, moldando décadas de teoria financeira, desde o Índice de Sharpe até o modelo Black-Scholes.12

## **3\. Risco, Retorno e Covariância: A Matemática da Diversificação**

A contribuição técnica mais duradoura de Markowitz foi a formulação estatística do risco do portfólio, demonstrando que o risco de um todo não é meramente a soma dos riscos das partes.

### **3.1 Retorno Esperado do Portfólio**

O retorno esperado de um portfólio ($E(R\_p)$) é uma função linear simples dos ativos que o compõem. É a média ponderada dos retornos esperados individuais ($E(R\_i)$), onde os pesos ($w\_i$) representam a fração do capital alocada em cada ativo:

$$E(R\_p) \= \\sum\_{i=1}^{n} w\_i E(R\_i)$$  
Esta linearidade implica que a diversificação não altera o potencial de retorno médio do portfólio; ela apenas dilui os retornos extremos dos ativos individuais.5

### **3.2 Variância e Covariância**

Diferentemente do retorno, a variância do portfólio ($\\sigma\_p^2$) não é linear. Ela depende crucialmente das **covariâncias** entre os ativos, capturando como os preços dos ativos se movem uns em relação aos outros. A fórmula da variância para um portfólio de $n$ ativos é:

$$\\sigma\_p^2 \= \\sum\_{i=1}^{n} w\_i^2 \\sigma\_i^2 \+ \\sum\_{i=1}^{n} \\sum\_{j=1, j \\neq i}^{n} w\_i w\_j \\sigma\_{ij}$$  
Ou, em notação matricial, $\\sigma\_p^2 \= \\mathbf{w}^T \\mathbf{\\Sigma} \\mathbf{w}$, onde $\\mathbf{\\Sigma}$ é a matriz de covariância.20

Markowitz demonstrou a "Lei da Covariância Média": à medida que o número de ativos ($n$) em um portfólio igualmente ponderado aumenta, a contribuição das variâncias individuais ($\\frac{1}{n}\\bar{\\sigma}^2$) para o risco total tende a zero, enquanto a contribuição das covariâncias ($\\frac{n-1}{n}\\bar{\\sigma}\_{ij}$) domina.22 No limite, o risco de um portfólio diversificado é determinado quase inteiramente pela covariância média entre os ativos, e não pela volatilidade individual de cada um.5

### **3.3 O Papel da Correlação**

A covariância ($\\sigma\_{ij}$) é o produto da correlação ($\\rho\_{ij}$) e dos desvios padrão ($\\sigma\_i, \\sigma\_j$). O coeficiente de correlação, variando entre \-1 e \+1, é o "motor" da diversificação:

* **Correlação Perfeita (+1):** O risco do portfólio é a média ponderada dos riscos individuais. Não há benefício de diversificação.  
* **Correlação Inferior a 1:** O risco do portfólio será sempre menor que a média ponderada dos riscos individuais. A volatilidade idiossincrática é cancelada.9  
* **Correlação Negativa (-1):** Permite, teoricamente, a construção de um portfólio com variância zero (hedge perfeito).

A intuição de Markowitz foi quantificar que, ao combinar ativos com correlação imperfeita, o investidor reduz a exposição a riscos específicos (choques que afetam apenas uma empresa), mantendo apenas a exposição aos riscos comuns que afetam todo o sistema.7

## **4\. A Fronteira Eficiente: Otimização e Geometria**

A aplicação dos princípios de média-variância a um universo de ativos resulta na construção da Fronteira Eficiente, o conjunto de todos os portfólios ótimos que dominam as demais alternativas.

### **4.1 Derivação e Definição**

A Fronteira Eficiente é o lugar geométrico no espaço risco-retorno que representa os portfólios que oferecem o retorno máximo para um dado nível de risco (ou risco mínimo para um dado retorno).24 Ela é obtida resolvendo um problema de otimização quadrática convexa:

$$\\min \\mathbf{w}^T \\mathbf{\\Sigma} \\mathbf{w}$$

$$\\text{sujeito a: } \\mathbf{w}^T \\mathbf{\\mu} \= R\_{alvo} \\text{ e } \\mathbf{w}^T \\mathbf{1} \= 1$$  
A forma geométrica exata desta fronteira depende criticamente das restrições impostas aos pesos ($w\_i$):

* **Sem Restrições a Vendas a Descoberto (Unconstrained/Short Selling Allowed):** Se o investidor pode vender a descoberto (assumir pesos negativos) ilimitadamente, a fronteira eficiente é uma **hipérbole** perfeita e suave no espaço média-desvio padrão.25 O ramo superior desta hipérbole (acima do vértice) é a fronteira eficiente propriamente dita.  
* **Com Restrições a Vendas a Descoberto (No Short Selling Constraint):** Quando impomos a restrição de não-negatividade ($w\_i \\geq 0$), a fronteira deixa de ser uma hipérbole única e torna-se uma curva convexa composta por uma série de **segmentos de hipérbole conectados** (*piecewise hyperbolic segments*).26  
  * *Mecanismo:* A transição de um segmento hiperbólico para outro ocorre nos "corner portfolios" (portfólios de canto). À medida que nos movemos ao longo da fronteira (aumentando o retorno esperado), a composição do portfólio muda. Quando o peso de um ativo atinge zero (sai do portfólio) ou quando um novo ativo entra no portfólio (peso torna-se positivo), a equação algébrica que descreve a curva muda, criando um "ponto de solda" entre dois arcos hiperbólicos distintos.29  
  * *Implicação:* A fronteira com restrições é finita, começando no portfólio de mínima variância global e terminando no ativo individual de maior retorno (e risco), ao contrário da fronteira sem restrições que se estende ao infinito através da alavancagem de posições vendidas.27

O algoritmo desenvolvido por Markowitz para traçar essa fronteira complexa com restrições de desigualdade é o **Critical Line Algorithm (CLA)**, um método de otimização quadrática paramétrica que precede e inspira os modernos solvers de programação quadrática.18

### **4.2 O Portfólio de Mínima Variância Global**

O vértice da fronteira (seja ela hiperbólica ou segmentada) é o Portfólio de Mínima Variância Global (GMV). Este é o único ponto na curva onde o risco é minimizado em termos absolutos, sem consideração pelo retorno.33 Em teoria, nenhum investidor racional avesso ao risco escolheria um portfólio localizado na parte "inferior" da fronteira (abaixo do GMV), pois para cada ponto nessa região existe um portfólio na parte superior com o mesmo risco, mas com retorno estritamente maior (dominância média-variância).25

## **5\. O Ativo Livre de Risco e o Teorema da Separação**

A introdução de um ativo livre de risco (*risk-free asset*) expande o conjunto de oportunidades do investidor além da fronteira de ativos de risco, alterando a geometria da escolha ótima e levando ao Teorema da Separação de Tobin.

### **5.1 O Ativo Livre de Risco**

Um ativo livre de risco é definido idealmente como um investimento com variância zero ($\\sigma\_{rf}^2 \= 0$) e, consequentemente, covariância zero com todos os ativos de risco ($\\sigma\_{i,rf} \= 0$).34 Na prática financeira, títulos governamentais de curto prazo, como as *Treasury Bills* dos EUA, são utilizados como *proxies*, assumindo-se ausência de risco de crédito e risco de reinvestimento negligenciável para o horizonte de um período.35

A inclusão deste ativo permite duas novas operações financeiras fundamentais:

1. **Empréstimo Livre de Risco (Lending):** O investidor pode aplicar parte de sua riqueza no ativo livre de risco, reduzindo a exposição total ao risco do mercado.  
2. **Tomada de Empréstimo Livre de Risco (Borrowing/Leverage):** O investidor pode tomar dinheiro emprestado à taxa livre de risco para alavancar sua posição nos ativos de risco.37

### **5.2 O Teorema da Separação de Tobin**

James Tobin, em seu artigo seminal de 1958 *Liquidity Preference as Behavior Towards Risk*, formalizou o impacto do ativo livre de risco na teoria da escolha de portfólio.39 Tobin demonstrou que, na presença de um ativo livre de risco, o processo de decisão de investimento pode ser decomposto em duas etapas distintas e independentes — um resultado conhecido como o **Teorema da Separação** (ou *Two-Fund Separation Theorem*).41

1. **Etapa 1: A Decisão Técnica (Seleção do Portfólio Ótimo de Risco).** O investidor deve primeiro identificar o portfólio de ativos de risco que maximiza o retorno por unidade de risco. Geometricamente, este é o **Portfólio de Tangência** (Tangency Portfolio), o ponto onde uma linha reta partindo da taxa livre de risco ($R\_f$) tangencia a fronteira eficiente hiperbólica dos ativos de risco.37 A composição deste portfólio é puramente técnica e objetiva, dependendo apenas das estimativas de médias, variâncias e covariâncias; ela é *independente* das preferências de risco do investidor individual.37  
2. **Etapa 2: A Decisão Pessoal (Alocação de Capital).** Uma vez identificado o Portfólio de Tangência, o investidor decide como alocar sua riqueza total entre este portfólio e o ativo livre de risco. Esta decisão depende inteiramente da função de utilidade (aversão ao risco) do indivíduo.37

### **5.3 A Reta do Mercado de Capitais (Capital Market Line \- CML)**

A combinação linear do ativo livre de risco com o Portfólio de Tangência gera a **Reta do Mercado de Capitais** (Capital Market Line \- CML). A CML torna-se a *nova* fronteira eficiente, pois domina qualquer portfólio situado na fronteira original de ativos de risco (a hipérbole fica inteiramente abaixo da reta CML, exceto no ponto de tangência).37

O posicionamento do investidor ao longo da CML é determinado pelo mecanismo de alavancagem:

* **Investidores Conservadores (Lending Portfolios):** Localizam-se à esquerda do ponto de tangência ($T$). Eles investem uma fração positiva de sua riqueza no ativo livre de risco e o restante no portfólio $T$. O risco total do portfólio é menor que o risco de $T$.37  
* **Investidores Agressivos (Borrowing Portfolios):** Localizam-se à direita do ponto de tangência ($T$). Eles tomam empréstimos à taxa $R\_f$ para investir mais de 100% de seu capital próprio no portfólio $T$, ampliando tanto o retorno esperado quanto a volatilidade.37

A equação que descreve a CML é:

$$E(R\_p) \= R\_f \+ \\left \\sigma\_p$$

Onde a inclinação (slope) da reta, $\\frac{E(R\_T) \- R\_f}{\\sigma\_T}$, representa o "preço de mercado do risco" — o retorno adicional que o mercado exige para aceitar uma unidade adicional de desvio padrão.44  
**Considerações sobre Taxas de Empréstimo Diferenciadas:** Na realidade, investidores raramente conseguem tomar empréstimos à mesma taxa livre de risco que o governo ($R\_{borrow} \> R\_{lending} \= R\_f$). Nesse cenário, a CML deixa de ser uma linha reta única e torna-se uma fronteira "quebrada" ou côncava: um segmento linear parte de $R\_f$ até um ponto de tangência, segue-se um segmento curvo da fronteira eficiente original (onde o investidor não empresta nem toma emprestado), e então um novo segmento linear parte de outro ponto de tangência com inclinação menor, baseada na taxa de empréstimo mais alta.41

## **6\. Avaliação de Desempenho: O Índice de Sharpe**

A geometria da CML forneceu a base direta para uma das métricas mais onipresentes na avaliação de investimentos: o Índice de Sharpe. Introduzido por William Sharpe em 1966 como "Reward-to-Variability Ratio", o índice operacionaliza o conceito de eficiência média-variância.49

### **6.1 Definição e Interpretação**

O Índice de Sharpe ($S\_p$) quantifica o excesso de retorno por unidade de risco total. Matematicamente:

$$S\_p \= \\frac{E(R\_p) \- R\_f}{\\sigma\_p}$$  
Geometricamente, o Índice de Sharpe de um portfólio é a inclinação da linha que conecta a taxa livre de risco a esse portfólio no gráfico média-desvio padrão.25 Quanto maior a inclinação, melhor o desempenho ajustado ao risco.

### **6.2 Importância e Aplicação**

A maximização do Índice de Sharpe é equivalente a encontrar o Portfólio de Tangência na MPT. Em um mercado em equilíbrio, o portfólio de mercado ($M$) deve ser aquele com o maior Índice de Sharpe possível.38 A métrica permite comparar fundos e estratégias heterogêneas, nivelando o campo de jogo ao penalizar a volatilidade. No entanto, o índice herda as limitações da variância: se os retornos não forem normais (ex: fundos de hedge com estratégias de opções), o Índice de Sharpe pode ser enganoso, penalizando a volatilidade positiva ou subestimando riscos de cauda, o que levou ao desenvolvimento de métricas alternativas como o **Índice de Sortino** (baseado na semivariância/downside deviation).51

## **7\. O Modelo de Precificação de Ativos de Capital (CAPM)**

Enquanto a MPT de Markowitz é normativa (diz ao investidor como construir um portfólio), o *Capital Asset Pricing Model* (CAPM) é positivo (explica como os preços dos ativos são determinados se todos seguirem a MPT).

### **7.1 Origem e Desenvolvedores**

O CAPM foi desenvolvido independentemente na primeira metade da década de 1960 por William Sharpe (1964), John Lintner (1965), Jan Mossin (1966) e Jack Treynor (1961/1962).53 A unificação dessas teorias rendeu a Sharpe, Markowitz e Merton Miller o Prêmio Nobel de Economia em 1990\.55 A intuição central é que, se todos os investidores são racionais, possuem expectativas homogêneas e otimizam seus portfólios segundo a média-variância (usando o Teorema da Separação de Tobin), então todos demandarão o mesmo portfólio de ativos de risco: o **Portfólio de Mercado** ($M$). Para que o mercado "limpe" (oferta iguale demanda), os preços dos ativos devem se ajustar até que o portfólio de tangência seja, de fato, o portfólio de mercado ponderado por valor.53

### **7.2 Decomposição do Risco: Sistemático vs. Não Sistemático**

O CAPM introduz uma distinção fundamental na natureza do risco, decompondo a variância total de um ativo ($\\sigma\_i^2$) em dois componentes 10:

1. **Risco Sistemático (Risco de Mercado):** É a parcela da volatilidade do ativo que está correlacionada com os movimentos do mercado como um todo. Origina-se de fatores macroeconômicos inelutáveis — inflação, juros, ciclos econômicos, guerras — que afetam todas as empresas simultaneamente. Este risco *não pode* ser eliminado pela diversificação.  
2. **Risco Não Sistemático (Idiossincrático/Específico):** É a parcela da volatilidade exclusiva da empresa ou setor (ex: sucesso de um novo produto, greve na fábrica, fraude contábil). Como esses eventos são estatisticamente independentes entre empresas, em um portfólio amplo eles tendem a se cancelar mutuamente (lei dos grandes números).

A conclusão revolucionária do CAPM é que **o mercado não remunera o risco não sistemático**. Como ele pode ser eliminado gratuitamente através da diversificação, os investidores não devem esperar nenhum prêmio de retorno por assumi-lo. O único risco que justifica um retorno esperado acima da taxa livre de risco é o risco sistemático.56

### **7.3 O Coeficiente Beta e a Reta do Mercado de Títulos (SML)**

Para mensurar o risco sistemático, o CAPM utiliza o coeficiente **Beta** ($\\beta$). O Beta é uma medida padronizada da covariância do ativo com o mercado, definida como:

$$\\beta\_i \= \\frac{\\sigma\_{i,M}}{\\sigma\_M^2} \= \\rho\_{i,M} \\frac{\\sigma\_i}{\\sigma\_M}$$  
Um ativo com $\\beta \= 1$ move-se, em média, na mesma proporção que o mercado. Um ativo com $\\beta \> 1$ amplifica os movimentos do mercado (mais risco sistemático), enquanto $\\beta \< 1$ os atenua.

A relação de equilíbrio entre risco sistemático e retorno esperado é expressa pela equação da **Reta do Mercado de Títulos** (Security Market Line \- SML):

$$E(R\_i) \= R\_f \+ \\beta\_i$$  
A SML difere fundamentalmente da CML. Enquanto a CML (usando $\\sigma$) aplica-se apenas a portfólios eficientes (que não possuem risco não sistemático), a SML (usando $\\beta$) aplica-se a *qualquer* ativo individual ou portfólio, eficiente ou não, precificando-os de acordo com sua contribuição marginal ao risco do portfólio de mercado.61

**Tabela 1: Comparação entre Capital Market Line (CML) e Security Market Line (SML)**

| Característica | Capital Market Line (CML) | Security Market Line (SML) |
| :---- | :---- | :---- |
| **Medida de Risco** | Desvio Padrão Total ($\\sigma$) | Beta Sistemático ($\\beta$) |
| **Aplicação** | Apenas Portfólios Eficientes | Qualquer Ativo Individual ou Portfólio |
| **Definição de Risco** | Risco Total (Sistemático \+ Idiossincrático) | Apenas Risco Sistemático (Covariância com Mercado) |
| **Ponto de Intercepto** | Taxa Livre de Risco ($R\_f$) | Taxa Livre de Risco ($R\_f$) |
| **Inclinação (Slope)** | Índice de Sharpe do Mercado ($\\frac{E(R\_M) \- R\_f}{\\sigma\_M}$) | Prêmio de Risco de Mercado ($E(R\_M) \- R\_f$) |
| **Fundamentação** | Teorema da Separação de Tobin | Modelo de Equilíbrio de Mercado (CAPM) |

Fonte: Elaboração própria com base em.61

## **8\. Pressupostos, Críticas e Limitações Teóricas**

A elegância matemática da MPT e do CAPM repousa sobre um conjunto de axiomas sobre o comportamento humano e a estrutura dos mercados. A validade desses modelos depende, portanto, da robustez de seus pressupostos.

### **8.1 Pressupostos Fundamentais: A Racionalidade VNM**

A teoria assume que os investidores são agentes perfeitamente racionais que tomam decisões sob incerteza maximizando a Utilidade Esperada, conforme axiomatizado por John von Neumann e Oskar Morgenstern (VNM) em *Theory of Games and Economic Behavior* (1944).63 Para que uma função de utilidade esperada exista e represente as preferências do investidor, cinco axiomas fundamentais devem ser satisfeitos 63:

1. **Completude (Completeness):** O investidor tem preferências bem definidas. Para quaisquer duas loterias (investimentos) A e B, ele pode afirmar se prefere A a B ($A \\succ B$), B a A ($B \\succ A$) ou se é indiferente ($A \\sim B$). A indecisão não é permitida.63  
2. **Transitividade (Transitivity):** As preferências são consistentes. Se $A \\succ B$ e $B \\succ C$, então logicamente $A \\succ C$. A violação deste axioma implicaria comportamento cíclico e irracional ("money pump").49  
3. **Continuidade (Continuity):** Também conhecido como axioma de Arquimedes. Se $A \\succ B \\succ C$, existe uma probabilidade $p$ tal que o investidor é indiferente entre receber B com certeza ou uma loteria que paga A com probabilidade $p$ e C com probabilidade $1-p$. Isso impede que qualquer resultado seja infinitamente desejável ou indesejável (como o paraíso ou a morte) a ponto de ignorar probabilidades.49  
4. **Independência (Independence):** A preferência entre duas opções não deve ser alterada pela introdução de uma terceira opção comum a ambas. Se $A \\succ B$, então uma mistura de A com C deve ser preferida à mesma mistura de B com C. Este é o axioma mais controverso e frequentemente violado em testes empíricos (ex: Paradoxo de Allais).49  
5. **Dominância (Dominance/Monotonicity):** Se uma opção A oferece resultados melhores que B em pelo menos um estado da natureza e resultados iguais ou melhores em todos os outros estados, então A deve ser estritamente preferida a B. Este axioma encapsula a ideia racional de que "mais é melhor que menos" e violações a ele (como escolher uma opção dominada estocasticamente) são consideradas erros graves de decisão.65

**Tabela 2: Axiomas da Teoria da Utilidade Esperada (VNM)**

| Axioma | Definição Simplificada | Implicação Financeira |
| :---- | :---- | :---- |
| **Completude** | Capacidade de ranquear qualquer par de ativos. | O mercado pode precificar todos os ativos. |
| **Transitividade** | Consistência lógica ($A\>B, B\>C \\Rightarrow A\>C$). | Evita arbitragem cíclica irracional. |
| **Continuidade** | Existência de "pontos de indiferença" probabilísticos. | Permite modelar o trade-off risco-retorno de forma contínua. |
| **Independência** | Preferências não mudam com opções irrelevantes. | A diversificação é consistente independentemente do resto da carteira. |
| **Dominância** | Preferência por "mais riqueza" e "menos risco". | Fundamenta a fronteira eficiente (ninguém escolhe portfólios dominados). |

Fonte: Elaboração própria baseada em.65

### **8.2 Limitações e a Realidade dos Mercados**

As críticas à MPT e ao CAPM surgem da desconexão entre esses axiomas ideais e a realidade empírica dos mercados financeiros.

* **Distribuições Não-Normais (Caudas Gordas):** A MPT assume que os retornos seguem uma distribuição Normal (Gaussiana), o que justifica o uso da variância como medida completa de risco. Contudo, estudos seminais de Benoit Mandelbrot (1963) e Eugene Fama (1965) demonstraram que os preços de ativos exibem "caudas gordas" (*fat tails*) e leptocurtose excessiva.76 Na realidade, eventos extremos (como *crashes* de mercado de 10 ou 20 desvios padrão) ocorrem com frequência muito maior do que a prevista pela curva normal. O uso da variância subestima drasticamente o risco real de eventos catastróficos ("Cisnes Negros"), tornando a MPT perigosa em momentos de crise.78  
* **Limitações da Variância:** Como discutido na seção 2.2, a variância penaliza igualmente a volatilidade para cima (lucro) e para baixo (perda). Investidores reais, no entanto, exibem aversão à perda, não à volatilidade *per se*. A semivariância ou métricas de *downside risk* seriam descritores mais precisos da utilidade do investidor, mas a inércia da tradição MPT mantém a variância como padrão.12  
* **Violações da Racionalidade:** A Economia Comportamental (Kahneman e Tversky) documentou sistemáticas violações dos axiomas VNM. O "efeito certeza" e a "aversão à perda" (Teoria da Perspectiva) mostram que investidores reais frequentemente violam os axiomas de Independência e Dominância, comportando-se de maneira inconsistente com a maximização da utilidade esperada.80

Apesar dessas falhas descritivas, a estrutura criada por Markowitz, Tobin e Sharpe permanece a *lingua franca* das finanças. Conceitos como diversificação, fronteira eficiente, Beta e Índice de Sharpe fornecem as ferramentas heurísticas indispensáveis para a alocação de ativos institucional, servindo como um modelo normativo de como o mercado *deveria* funcionar sob condições ideais, mesmo que a realidade frequentemente divirja do modelo.

#### **Referências citadas**

1. John Burr Williams The Theory Of Investment Value \- riomaisseguro.rio.rj.gov.br, acessado em novembro 28, 2025, [https://riomaisseguro.rio.rj.gov.br/default.aspx/textbook-solutions/HG2MH5/John%20Burr%20Williams%20The%20Theory%20Of%20Investment%20Value.pdf](https://riomaisseguro.rio.rj.gov.br/default.aspx/textbook-solutions/HG2MH5/John%20Burr%20Williams%20The%20Theory%20Of%20Investment%20Value.pdf)  
2. Markowitz's "Portfolio Selection": \- A Fifty-Year Retrospective \- York University, acessado em novembro 28, 2025, [http://www.yorku.ca/pshum/Courses/Markowitz](http://www.yorku.ca/pshum/Courses/Markowitz)  
3. Markowitz for the Masses: The Risk and Return of Equity and Portfolio Construction Techniques \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/225841950\_Markowitz\_for\_the\_Masses\_The\_Risk\_and\_Return\_of\_Equity\_and\_Portfolio\_Construction\_Techniques](https://www.researchgate.net/publication/225841950_Markowitz_for_the_Masses_The_Risk_and_Return_of_Equity_and_Portfolio_Construction_Techniques)  
4. Markowitz Portfolio Construction at Seventy \- Stanford University, acessado em novembro 28, 2025, [https://web.stanford.edu/\~boyd/papers/pdf/markowitz.pdf](https://web.stanford.edu/~boyd/papers/pdf/markowitz.pdf)  
5. Modern portfolio theory \- Wikipedia, acessado em novembro 28, 2025, [https://en.wikipedia.org/wiki/Modern\_portfolio\_theory](https://en.wikipedia.org/wiki/Modern_portfolio_theory)  
6. Portfolio Selection Harry Markowitz The Journal of Finance, Vol. 7, No. 1\. (Mar., 1952), pp. 77-91., acessado em novembro 28, 2025, [https://www.math.hkust.edu.hk/\~maykwok/courses/ma362/07F/markowitz\_JF.pdf](https://www.math.hkust.edu.hk/~maykwok/courses/ma362/07F/markowitz_JF.pdf)  
7. Harry Markowitz's Modern Portfolio Theory: The Efficient Frontier \- GuidedChoice, acessado em novembro 28, 2025, [https://guidedchoice.com/modern-portfolio-theory/](https://guidedchoice.com/modern-portfolio-theory/)  
8. Words From the Wise Harry Markowitz \- AQR Capital Management, acessado em novembro 28, 2025, [https://images.aqr.com/-/media/AQR/Documents/Insights/Interviews/Words-From-the-Wise-Harry-Markowitz-on-Portfolio-Theory-and-Practice.pdf](https://images.aqr.com/-/media/AQR/Documents/Insights/Interviews/Words-From-the-Wise-Harry-Markowitz-on-Portfolio-Theory-and-Practice.pdf)  
9. Harry Markowitz: The Father of Modern Portfolio Theory | Index Fund Advisors, Inc., acessado em novembro 28, 2025, [https://www.ifa.com/articles/harry\_markowitz\_father\_modern\_portfolio\_theory](https://www.ifa.com/articles/harry_markowitz_father_modern_portfolio_theory)  
10. Estrutura Tópicos \_2026.docx  
11. Modern Portfolio Theory: What MPT Is and How Investors Use It \- Investopedia, acessado em novembro 28, 2025, [https://www.investopedia.com/terms/m/modernportfoliotheory.asp](https://www.investopedia.com/terms/m/modernportfoliotheory.asp)  
12. Mean-Semivariance Optimization: A Heuristic Approach \- SciSpace, acessado em novembro 28, 2025, [https://scispace.com/pdf/mean-semivariance-optimization-a-heuristic-approach-2brneo21d9.pdf](https://scispace.com/pdf/mean-semivariance-optimization-a-heuristic-approach-2brneo21d9.pdf)  
13. PORTFOLIO OPTIMIZATION WITH SEMI-VARIANCE MODEL: AN APPLICATION ON BIST-100 INDEX\* \- DergiPark, acessado em novembro 28, 2025, [https://dergipark.org.tr/en/download/article-file/3502414](https://dergipark.org.tr/en/download/article-file/3502414)  
14. Harry M. Markowitz \- Prize Lecture, acessado em novembro 28, 2025, [https://www.nobelprize.org/uploads/2018/06/markowitz-lecture.pdf](https://www.nobelprize.org/uploads/2018/06/markowitz-lecture.pdf)  
15. Markowitz Semivariance 1959 | PDF | Sampling (Statistics) | Variance \- Scribd, acessado em novembro 28, 2025, [https://www.scribd.com/document/937635304/Markowitz-Semivariance-1959](https://www.scribd.com/document/937635304/Markowitz-Semivariance-1959)  
16. Mean-Semivariance Behavior: A Note \- IESE Blog Network, acessado em novembro 28, 2025, [https://blog.iese.edu/jestrada/files/2012/06/MSB-Note.pdf](https://blog.iese.edu/jestrada/files/2012/06/MSB-Note.pdf)  
17. Mean-Semivariance Analysis of Option-Based Strategies: A Total Asset Mix Perspective \- Hillsdale Investment Management Inc., acessado em novembro 28, 2025, [https://www.hillsdaleinv.com/uploads/Mean-Semivariance\_Analysis\_of\_Option-Based\_Strategies\_A\_Total\_Asset\_Mix\_Perspective%2C\_Harry\_S.\_Marmer%2C\_F.\_K.\_Louis\_Ng.pdf](https://www.hillsdaleinv.com/uploads/Mean-Semivariance_Analysis_of_Option-Based_Strategies_A_Total_Asset_Mix_Perspective%2C_Harry_S._Marmer%2C_F._K._Louis_Ng.pdf)  
18. Avoiding the Downside: A Practical Review of the Critical Line Algorithm for Mean-Semivariance Portfolio Optimization \- Hudson Bay Capital, acessado em novembro 28, 2025, [https://www.hudsonbaycapital.com/documents/FG/hudsonbay/research/599440\_paper.pdf](https://www.hudsonbaycapital.com/documents/FG/hudsonbay/research/599440_paper.pdf)  
19. A Brief History of Downside Risk Measures \- Portfolio Management Research, acessado em novembro 28, 2025, [https://www.pm-research.com/content/iijinvest%3A%3A%3A8%3A%3A%3A3%3A%3A%3A9.full.pdf?implicit-login=true\&sigma-token=odAGsFRmFlsRqq7IrQy5zdxeYP6m3d88742LqRu9\_Ow](https://www.pm-research.com/content/iijinvest%3A%3A%3A8%3A%3A%3A3%3A%3A%3A9.full.pdf?implicit-login=true&sigma-token=odAGsFRmFlsRqq7IrQy5zdxeYP6m3d88742LqRu9_Ow)  
20. Robust Efficient Frontier Analysis with a Separable Uncertainty Model \- Stanford University, acessado em novembro 28, 2025, [https://stanford.edu/\~boyd/papers/pdf/rob\_ef\_sep.pdf](https://stanford.edu/~boyd/papers/pdf/rob_ef_sep.pdf)  
21. An Application of Portfolio Mean-Variance and Semi-Variance Optimization Techniques: A Case of Fiji \- Semantic Scholar, acessado em novembro 28, 2025, [https://pdfs.semanticscholar.org/e268/395154276482f0ba10d8864949fa35a76b04.pdf](https://pdfs.semanticscholar.org/e268/395154276482f0ba10d8864949fa35a76b04.pdf)  
22. The Early History of Portfolio Theory: 1600-1960: Perspectives | PDF \- Scribd, acessado em novembro 28, 2025, [https://www.scribd.com/document/371666050/Markowitz-fm](https://www.scribd.com/document/371666050/Markowitz-fm)  
23. Mean–variance and mean–semivariance portfolio selection: a multivariate nonparametric approach \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/328509498\_Mean-variance\_and\_mean-semivariance\_portfolio\_selection\_a\_multivariate\_nonparametric\_approach](https://www.researchgate.net/publication/328509498_Mean-variance_and_mean-semivariance_portfolio_selection_a_multivariate_nonparametric_approach)  
24. Efficient frontier \- Wikipedia, acessado em novembro 28, 2025, [https://en.wikipedia.org/wiki/Efficient\_frontier](https://en.wikipedia.org/wiki/Efficient_frontier)  
25. Geometry of the Efficient Frontier \- Gregory Gundersen, acessado em novembro 28, 2025, [https://gregorygundersen.com/blog/2022/01/09/geometry-efficient-frontier/](https://gregorygundersen.com/blog/2022/01/09/geometry-efficient-frontier/)  
26. MOSEK Portfolio Optimization Cookbook \- Documentation, acessado em novembro 28, 2025, [https://docs.mosek.com/MOSEKPortfolioCookbook-a4paper.pdf](https://docs.mosek.com/MOSEKPortfolioCookbook-a4paper.pdf)  
27. Efficient Frontier in Constrained Portfolios \- VICBee Consulting, acessado em novembro 28, 2025, [https://vicbee.net/portfolio.html](https://vicbee.net/portfolio.html)  
28. \[PDF\] Applying Markowitz's Critical Line Algorithm | Semantic Scholar, acessado em novembro 28, 2025, [https://www.semanticscholar.org/paper/Applying-Markowitz's-Critical-Line-Algorithm-Niedermayer-Niedermayer/9927df863598a4343abfd646f274815faf63958c](https://www.semanticscholar.org/paper/Applying-Markowitz's-Critical-Line-Algorithm-Niedermayer-Niedermayer/9927df863598a4343abfd646f274815faf63958c)  
29. Parametrically computing efficient frontiers of portfolio selection and reporting and utilizing the piecewise-segment structure \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/333838206\_Parametrically\_computing\_efficient\_frontiers\_of\_portfolio\_selection\_and\_reporting\_and\_utilizing\_the\_piecewise-segment\_structure](https://www.researchgate.net/publication/333838206_Parametrically_computing_efficient_frontiers_of_portfolio_selection_and_reporting_and_utilizing_the_piecewise-segment_structure)  
30. Normal Asset Allocations and Their Statistical Properties \- MDPI, acessado em novembro 28, 2025, [https://www.mdpi.com/2227-7072/12/3/69](https://www.mdpi.com/2227-7072/12/3/69)  
31. HANDBOOK OF FINANCIAL ENGINEERING \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/profile/Panos-Pardalos/publication/228642734\_Handbook\_of\_Financial\_Engineering/links/0a85e5311e2a06f899000000/Handbook-of-Financial-Engineering.pdf](https://www.researchgate.net/profile/Panos-Pardalos/publication/228642734_Handbook_of_Financial_Engineering/links/0a85e5311e2a06f899000000/Handbook-of-Financial-Engineering.pdf)  
32. European Journal of Operational Research Computing cardinality constrained portfolio selection efficient frontiers via closest c, acessado em novembro 28, 2025, [https://www.terry.uga.edu/wp-content/uploads/Cardinality.pdf](https://www.terry.uga.edu/wp-content/uploads/Cardinality.pdf)  
33. Markowitz model \- Grokipedia, acessado em novembro 28, 2025, [https://grokipedia.com/page/Markowitz\_model](https://grokipedia.com/page/Markowitz_model)  
34. NPTEL Course \- Session-23 Capital Market Theory-I, acessado em novembro 28, 2025, [https://archive.nptel.ac.in/content/storage2/courses/110105036/m12l23.pdf](https://archive.nptel.ac.in/content/storage2/courses/110105036/m12l23.pdf)  
35. (PDF) Semi-Variance in Finance \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/304179735\_Semi-Variance\_in\_Finance](https://www.researchgate.net/publication/304179735_Semi-Variance_in_Finance)  
36. Understanding the CAPM: Key Formula, Assumptions, and Applications \- Investopedia, acessado em novembro 28, 2025, [https://www.investopedia.com/terms/c/capm.asp](https://www.investopedia.com/terms/c/capm.asp)  
37. Capital Market Line \- GlynHolton.com, acessado em novembro 28, 2025, [https://www.glynholton.com/notes/capital\_market\_line/](https://www.glynholton.com/notes/capital_market_line/)  
38. Lecture 2: Fundamentals of mean- variance analysis, acessado em novembro 28, 2025, [https://didattica.unibocconi.it/mypage/dwload.php?nomefile=Lec\_2\_Introduction\_to\_Mean\_Variance\_Analysis20170323213235.pdf](https://didattica.unibocconi.it/mypage/dwload.php?nomefile=Lec_2_Introduction_to_Mean_Variance_Analysis20170323213235.pdf)  
39. NBER WORKING PAPER SERIES JAMES TOBIN: AN APPRECIATION OF HIS CONTRIBUTION TO ECONOMICS Willem H. Buiter Working Paper 9753 http, acessado em novembro 28, 2025, [https://www.nber.org/system/files/working\_papers/w9753/w9753.pdf](https://www.nber.org/system/files/working_papers/w9753/w9753.pdf)  
40. Liquidity Preference as Behavior Towards Risk, acessado em novembro 28, 2025, [http://www.efalken.com/LowVolClassics/tobin1958.pdf](http://www.efalken.com/LowVolClassics/tobin1958.pdf)  
41. Two-Fund Separation under Model Mis-Specification \- Stanford University, acessado em novembro 28, 2025, [https://web.stanford.edu/\~boyd/papers/pdf/rob\_two\_fund\_sep.pdf](https://web.stanford.edu/~boyd/papers/pdf/rob_two_fund_sep.pdf)  
42. On Portfolio Separation Theorems with Heterogeneous Beliefs and Attitudes towards Risk, acessado em novembro 28, 2025, [https://www.bankofcanada.ca/2008/05/working-paper-2008-16/](https://www.bankofcanada.ca/2008/05/working-paper-2008-16/)  
43. CHAPTER 14: Leverage versus Concentration \- A Practitioner's Guide to Asset Allocation \[Book\] \- O'Reilly, acessado em novembro 28, 2025, [https://www.oreilly.com/library/view/a-practitioners-guide/9781119397809/c14.xhtml](https://www.oreilly.com/library/view/a-practitioners-guide/9781119397809/c14.xhtml)  
44. Understanding Capital Market Line (CML) and How to Calculate It \- Investopedia, acessado em novembro 28, 2025, [https://www.investopedia.com/terms/c/cml.asp](https://www.investopedia.com/terms/c/cml.asp)  
45. Fuzziness and funds allocation in portfolio optimization \- Smarandache Notions, acessado em novembro 28, 2025, [https://fs.unm.edu/Stat/FuzzinessAndFundsAllocation.pdf](https://fs.unm.edu/Stat/FuzzinessAndFundsAllocation.pdf)  
46. The Capital Market Theory: Markowitz, CML, and Separation Theorem \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/363639593\_The\_Capital\_Market\_Theory\_Markowitz\_CML\_and\_Separation\_Theorem](https://www.researchgate.net/publication/363639593_The_Capital_Market_Theory_Markowitz_CML_and_Separation_Theorem)  
47. The Capital Asset Pricing Model: An Overview of the Theory \- Canadian Center of Science and Education, acessado em novembro 28, 2025, [https://ccsenet.org/journal/index.php/ijef/article/download/41043/23869](https://ccsenet.org/journal/index.php/ijef/article/download/41043/23869)  
48. The Portfolio Separation Theorem \- Econlib, acessado em novembro 28, 2025, [https://www.econlib.org/archives/2010/07/the\_portfolio\_s.html](https://www.econlib.org/archives/2010/07/the_portfolio_s.html)  
49. Von Neumann–Morgenstern utility theorem \- Wikipedia, acessado em novembro 28, 2025, [https://en.wikipedia.org/wiki/Von\_Neumann%E2%80%93Morgenstern\_utility\_theorem](https://en.wikipedia.org/wiki/Von_Neumann%E2%80%93Morgenstern_utility_theorem)  
50. BA 513: Ph.D. Seminar on Choice Theory Professor Robert Nau Fall Semester 2008 \- Duke People, acessado em novembro 28, 2025, [https://people.duke.edu/\~rnau/choice/choice02.pdf](https://people.duke.edu/~rnau/choice/choice02.pdf)  
51. Expected Utility Theory without the Completeness Axiom∗, acessado em novembro 28, 2025, [https://cienciassociales.edu.uy/wp-content/uploads/2020/10/1era-1er-premio-t08-trajtenberg.pdf](https://cienciassociales.edu.uy/wp-content/uploads/2020/10/1era-1er-premio-t08-trajtenberg.pdf)  
52. the-sortino-ratio.pdf, acessado em novembro 28, 2025, [https://rpc.cfainstitute.org/sites/default/files/-/media/documents/code/gips/the-sortino-ratio.pdf](https://rpc.cfainstitute.org/sites/default/files/-/media/documents/code/gips/the-sortino-ratio.pdf)  
53. The Capital Asset Pricing Model: Theory and Evidence \- Tuck School of Business, acessado em novembro 28, 2025, [https://mba.tuck.dartmouth.edu/bespeneckbo/default/AFA611-Eckbo%20web%20site/AFA611-S6B-FamaFrench-CAPM-JEP04.pdf](https://mba.tuck.dartmouth.edu/bespeneckbo/default/AFA611-Eckbo%20web%20site/AFA611-S6B-FamaFrench-CAPM-JEP04.pdf)  
54. Capital asset pricing model \- Wikipedia, acessado em novembro 28, 2025, [https://en.wikipedia.org/wiki/Capital\_asset\_pricing\_model](https://en.wikipedia.org/wiki/Capital_asset_pricing_model)  
55. Capital asset pricing model \- Risk Management (FIN 4335\) Course Website, acessado em novembro 28, 2025, [http://fin4335.garven.com/wp-content/uploads/2013/12/Capital-asset-pricing-model.pdf](http://fin4335.garven.com/wp-content/uploads/2013/12/Capital-asset-pricing-model.pdf)  
56. 12 Return, Risk, and the, acessado em novembro 28, 2025, [http://faculty.bus.olemiss.edu/rvanness/Courses/Fin%20334/Chap12.pdf](http://faculty.bus.olemiss.edu/rvanness/Courses/Fin%20334/Chap12.pdf)  
57. Handout 8: Understanding the CAPM Corporate Finance, Sections 001 and 002 The CAPM consists of two statements 1\. The tangency po, acessado em novembro 28, 2025, [https://finance.wharton.upenn.edu/\~jwachter/fnce100/h08.pdf](https://finance.wharton.upenn.edu/~jwachter/fnce100/h08.pdf)  
58. Analysis of Systematic Risk: Decomposition and Portfolio Efficiency \- The Research Repository @ WVU \- West Virginia University, acessado em novembro 28, 2025, [https://researchrepository.wvu.edu/cgi/viewcontent.cgi?article=4463\&context=etd](https://researchrepository.wvu.edu/cgi/viewcontent.cgi?article=4463&context=etd)  
59. Specific risk \- SimTrade blog, acessado em novembro 28, 2025, [https://www.simtrade.fr/blog\_simtrade/specific-risk/](https://www.simtrade.fr/blog_simtrade/specific-risk/)  
60. The capital asset pricing model – part 3 \- ACCA Global, acessado em novembro 28, 2025, [https://www.accaglobal.com/us/en/student/exam-support-resources/fundamentals-exams-study-resources/f9/technical-articles/CAPM-theory.html](https://www.accaglobal.com/us/en/student/exam-support-resources/fundamentals-exams-study-resources/f9/technical-articles/CAPM-theory.html)  
61. “Portfolio optimization in a mean-semivariance framework” \- Business Perspectives, acessado em novembro 28, 2025, [https://www.businessperspectives.org/index.php/journals?controller=pdfview\&task=download\&item\_id=4193](https://www.businessperspectives.org/index.php/journals?controller=pdfview&task=download&item_id=4193)  
62. Isolating the Systematic Component of a Single Stock's (or Portfolio's) Standard Deviation \- CORE, acessado em novembro 28, 2025, [https://core.ac.uk/download/pdf/7191267.pdf](https://core.ac.uk/download/pdf/7191267.pdf)  
63. Expected utility hypothesis \- Wikipedia, acessado em novembro 28, 2025, [https://en.wikipedia.org/wiki/Expected\_utility\_hypothesis](https://en.wikipedia.org/wiki/Expected_utility_hypothesis)  
64. 3.4: Choice under Uncertainty \- Expected Utility Theory \- Business LibreTexts, acessado em novembro 28, 2025, [https://biz.libretexts.org/Bookshelves/Finance/Risk\_Management\_for\_Enterprises\_and\_Individuals/03%3A\_Risk\_Attitudes\_-\_Expected\_Utility\_Theory\_and\_Demand\_for\_Hedging/3.04%3A\_Choice\_under\_Uncertainty\_-\_Expected\_Utility\_Theory](https://biz.libretexts.org/Bookshelves/Finance/Risk_Management_for_Enterprises_and_Individuals/03%3A_Risk_Attitudes_-_Expected_Utility_Theory_and_Demand_for_Hedging/3.04%3A_Choice_under_Uncertainty_-_Expected_Utility_Theory)  
65. Insper Ciências Econômicas Matheus Pecorari A Racionalidade por trás de Escolhas sob Incertezas São Paulo 2022, acessado em novembro 28, 2025, [https://repositorio.insper.edu.br/bitstreams/0b50406e-7e00-41c0-b283-605cf87451a6/download](https://repositorio.insper.edu.br/bitstreams/0b50406e-7e00-41c0-b283-605cf87451a6/download)  
66. Cap 03 \- Teoria Da Escolha | PDF | Utilidade | Avaliação de risco \- Scribd, acessado em novembro 28, 2025, [https://pt.scribd.com/document/688730077/Cap-03-Teoria-da-Escolha](https://pt.scribd.com/document/688730077/Cap-03-Teoria-da-Escolha)  
67. Rationality in Economics: Theory and Evidence \- EconStor, acessado em novembro 28, 2025, [https://www.econstor.eu/bitstream/10419/174995/1/cesifo1\_wp6872.pdf](https://www.econstor.eu/bitstream/10419/174995/1/cesifo1_wp6872.pdf)  
68. The Axioms of Expected-Utility Theory \- Johan E. Gustafsson, acessado em novembro 28, 2025, [https://johanegustafsson.net/teaching/lectures/the-axioms-of-expected-utility-theory.pdf](https://johanegustafsson.net/teaching/lectures/the-axioms-of-expected-utility-theory.pdf)  
69. DECISION THEORY \- Survey Data Laundering, acessado em novembro 28, 2025, [http://datalaundering.com/download/notes.pdf](http://datalaundering.com/download/notes.pdf)  
70. Von Neumann–Morgenstern utility theorem \- Grokipedia, acessado em novembro 28, 2025, [https://grokipedia.com/page/Von\_Neumann%E2%80%93Morgenstern\_utility\_theorem](https://grokipedia.com/page/Von_Neumann%E2%80%93Morgenstern_utility_theorem)  
71. Rational Economic Decision Making: The Relevance Among The Axioms of The Theory of Expected Utility Rasyonel İktisadi \- DergiPark, acessado em novembro 28, 2025, [https://dergipark.org.tr/en/download/article-file/630892](https://dergipark.org.tr/en/download/article-file/630892)  
72. Choice Under Uncertainty, acessado em novembro 28, 2025, [http://efinance.org.cn/cn/AP/utility%20theory.pdf](http://efinance.org.cn/cn/AP/utility%20theory.pdf)  
73. Finanças Comp portamentais: o comportame, acessado em novembro 28, 2025, [https://repositorio.unesp.br/bitstreams/f932338b-091d-4dc0-a0f7-d6962dfb8525/download](https://repositorio.unesp.br/bitstreams/f932338b-091d-4dc0-a0f7-d6962dfb8525/download)  
74. UNIVERSIDADE FEDERAL DO RIO DE JANEIRO CAMPUS – MACAÉ DEPARTAMENTO DE ENGENHARIA Thais Monteiro Pinto FINANÇAS PESSOAIS E CO, acessado em novembro 28, 2025, [https://ipoli.macae.ufrj.br/wp-content/uploads/2023/11/TCC\_Thais\_Monteiro\_Pinto\_Producao.pdf](https://ipoli.macae.ufrj.br/wp-content/uploads/2023/11/TCC_Thais_Monteiro_Pinto_Producao.pdf)  
75. Lecture 4 – Introduction to Utility Theory under Certainty and Uncertainty, acessado em novembro 28, 2025, [https://didattica.unibocconi.it/mypage/dwload.php?nomefile=Lec\_4\_Introduction\_to\_Utility\_Theory\_Under\_Certainty\_and\_Uncertainty20180828010655.pdf](https://didattica.unibocconi.it/mypage/dwload.php?nomefile=Lec_4_Introduction_to_Utility_Theory_Under_Certainty_and_Uncertainty20180828010655.pdf)  
76. Reviews of The (Mis)behavior of Markets \[DOC\] \- Yale Math, acessado em novembro 28, 2025, [https://users.math.yale.edu/mandelbrot/web\_docs/SCRAPBOOKmisbehavior.doc](https://users.math.yale.edu/mandelbrot/web_docs/SCRAPBOOKmisbehavior.doc)  
77. Optimal Portfolio Choice with Fat Tails \- National Bureau of Economic Research, acessado em novembro 28, 2025, [https://www.nber.org/sites/default/files/2023-06/orrc09-16-VD.pdf](https://www.nber.org/sites/default/files/2023-06/orrc09-16-VD.pdf)  
78. Is modern portfolio theory seriously flawed? \- Proactive Advisor Magazine, acessado em novembro 28, 2025, [https://proactiveadvisormagazine.com/modern-portfolio-theory-seriously-flawed/](https://proactiveadvisormagazine.com/modern-portfolio-theory-seriously-flawed/)  
79. Revisiting Modern Portfolio Theory and Portfolio Construction, acessado em novembro 28, 2025, [https://www.smartportfolios.com/articles/revisiting\_modern\_portfolio\_theory.pdf](https://www.smartportfolios.com/articles/revisiting_modern_portfolio_theory.pdf)  
80. "Expected Utility \- Mean Absolute Semideviation" Model of Individual Decision Making under Risk Pavlo R. Blavatskyy In \- Cerge-Ei, acessado em novembro 28, 2025, [https://www.cerge-ei.cz/pdf/events/papers/100318\_t.pdf](https://www.cerge-ei.cz/pdf/events/papers/100318_t.pdf)  
81. Expected Utility Theory, acessado em novembro 28, 2025, [https://www.columbia.edu/\~md3405/Choice\_MA\_Risk\_1\_17.pdf](https://www.columbia.edu/~md3405/Choice_MA_Risk_1_17.pdf)