# Capítulo 1: Fundamentação Teórica e Revisão Bibliográfica da Moderna Teoria do Portfólio


## 1. Introdução: A Evolução Histórica da Gestão de Investimentos

A gestão de investimentos, historicamente uma arte dominada pela intuição e pela análise fundamentalista idiossincrática, sofreu uma revolução paradigmática em meados do século XX. Antes do advento da Teoria Moderna do Portfólio (Modern Portfolio Theory - MPT), a prática de alocação de capital carecia de uma estrutura teórica unificada que quantificasse a relação entre risco e retorno de maneira sistemática. Este capítulo delineia a trajetória intelectual que transformou as finanças de uma disciplina descritiva em uma ciência normativa e quantitativa, culminando nos modelos de equilíbrio que sustentam a indústria global de gestão de ativos contemporânea.

### 1.1 O Paradigma Pré-Markowitz: A Era da Seleção de Ativos

Até o início da década de 1950, a teoria de investimentos operava sob o "paradigma da seleção de ativos" (*stock picking*). A literatura seminal da época, epitomizada pelas obras de John Burr Williams e da dupla Benjamin Graham e David Dodd, focava quase exclusivamente na determinação do valor intrínseco de títulos individuais, tratando a construção do portfólio como uma consequência secundária da acumulação de ativos subavaliados (Williams, 1938).
John Burr Williams, em sua *magnum opus* de 1938, *The Theory of Investment Value*, introduziu o Modelo de Desconto de Dividendos (Dividend Discount Model - DDM), estabelecendo que o valor de um ativo é o valor presente de seus fluxos de caixa futuros esperados, descontados a uma taxa de juros apropriada (Williams, 1938). A fórmula de Williams, $V_0 = \sum_{t=1}^{\infty} \frac{d_t}{(1+i)^t}$, onde $d_t$ representa os dividendos e $i$ a taxa de desconto, proporcionou o primeiro rigor matemático para a avaliação de *equities* (Markowitz for the Masses..., 2025). Contudo, a abordagem de Williams sofria de uma limitação crítica: ela assumia que o risco poderia ser virtualmente eliminado através da diversificação, sem fornecer um mecanismo matemático para quantificar como a variabilidade dos retornos de diferentes ativos interagia (Rubinstein, 2002). Williams focava na maximização do retorno esperado, acreditando que a "lei dos grandes números" protegeria o investidor que diversificasse suficientemente (Rubinstein, 2002).
Paralelamente, Benjamin Graham e David Dodd, em *Security Analysis* (1934), estabeleceram os princípios do *Value Investing*. Embora defendessem a diversificação como uma medida prudencial — sugerindo a detenção de dez a trinta papéis diferentes para mitigar o erro de análise — o conceito de risco em sua estrutura era fundamentalmente qualitativo (Boyd et al., 2024). Para Graham, risco não era volatilidade, mas sim a possibilidade de perda permanente de capital decorrente da deterioração dos fundamentos da empresa ou de pagar um preço excessivo em relação ao valor intrínseco (Markowitz for the Masses..., 2025). A "Margem de Segurança" era a métrica de proteção, não o desvio padrão ou a covariância. Neste paradigma, o portfólio era visto como uma coleção de ativos individuais, onde cada componente era julgado por seus próprios méritos, isolado do contexto agregado da carteira.

### 1.2 A Transição para a Análise Quantitativa

A ruptura com o paradigma da seleção individual de ativos não ocorreu abruptamente, mas foi precedida por desenvolvimentos teóricos que começaram a questionar a suficiência da maximização do valor presente. Economistas como Hicks (1939) e Marschak (1938) já exploravam as preferências sobre momentos estatísticos, e o matemático italiano Bruno de Finetti, em 1940, havia formulado um problema de alocação média-variância no contexto de resseguros, embora seu trabalho tenha permanecido desconhecido no mundo anglófono por décadas (Wikipedia, 2025).
O momento decisivo, contudo, surgiu da insatisfação intelectual de Harry Markowitz com a teoria vigente. Enquanto lia a obra de Williams na biblioteca da Universidade de Chicago, Markowitz teve um *insight* que desmantelaria a lógica da maximização pura do retorno (Boyd et al., 2024). Ele percebeu que, se a regra de Williams fosse seguida estritamente em um mundo de incerteza, um investidor racional deveria alocar 100% de seu capital no único ativo com o maior retorno esperado descontado (Markowitz, 1952). Se dois ativos tivessem o mesmo retorno máximo, o investidor seria indiferente entre eles, mas a teoria não oferecia nenhuma razão intrínseca para manter ambos.
Markowitz identificou que a prática observada e intuitivamente racional da diversificação — "não colocar todos os ovos na mesma cesta" — era inconsistente com a teoria de maximização de valor presente de Williams (Markowitz, 1952). Para racionalizar a diversificação, era necessário introduzir uma segunda dimensão na função objetivo do investidor: o risco. A diversificação só faz sentido se o investidor estiver disposto a sacrificar uma parcela do retorno potencial para reduzir a incerteza do resultado final. Essa percepção marcou a transição da análise de títulos (*Security Analysis*) para a análise de portfólios (*Portfolio Analysis*), onde a unidade de análise deixa de ser a firma individual e passa a ser a carteira agregada (GuidedChoice, 2025).

## 2. A Revolução de Markowitz: O Modelo Média-Variância

A formalização matemática dessa nova perspectiva ocorreu com a publicação do artigo "Portfolio Selection" no *Journal of Finance* em 1952, expandido posteriormente na monografia *Portfolio Selection: Efficient Diversification of Investments* (1959) (IFA, 2025). A "Modern Portfolio Theory" (MPT) de Markowitz não apenas descreveu como os investidores agem, mas prescreveu como deveriam agir, fundamentando a decisão de investimento na interação estocástica entre ativos.

### 2.1 A Rejeição da Maximização Pura do Retorno

A premissa fundadora da MPT é que os investidores são, simultaneamente, maximizadores de retorno e avessos ao risco (Investopedia, 2025). Markowitz rejeitou a hipótese de que os investidores consideram apenas o valor esperado (média) dos retornos futuros. Se os investidores focassem apenas na média, o conceito de um portfólio diversificado seria teoricamente injustificável, pois a diversificação quase sempre reduz o retorno esperado em comparação com a concentração no ativo de melhor desempenho (Markowitz, 1952).
Portanto, a função de utilidade do investidor deve depender de dois parâmetros:
**Retorno Esperado ($\mu$):** O valor médio ponderado das probabilidades dos retornos futuros.
**Risco ($\sigma$):** A dispersão ou incerteza desses retornos em torno da média.
A MPT postula que, para qualquer nível dado de risco, o investidor prefere o maior retorno possível; e para qualquer nível dado de retorno, prefere o menor risco possível. Essa estrutura de preferências cria um *trade-off* inevitável, substituindo a busca pelo "melhor ativo" pela construção do "melhor portfólio" (GuidedChoice, 2025).

### 2.2 O Conceito de Risco como Variância: Uma Escolha Pragmática

A decisão de Markowitz de utilizar a variância (ou desvio padrão) como a medida universal de risco foi uma das escolhas mais consequentes na história das finanças, ditada tanto por conveniência matemática quanto por restrições computacionais da década de 1950.
Em sua obra de 1959, Markowitz dedicou o Capítulo 9 para discutir uma medida alternativa de risco: a **semivariância** (SciSpace, 2025). A semivariância mensura apenas a dispersão dos retornos que caem abaixo de um determinado alvo (como a média ou zero), ignorando a volatilidade "positiva" (ganhos acima do esperado). Markowitz reconheceu explicitamente a superioridade teórica desta medida, afirmando que "a semivariância parece mais plausível do que a variância como uma medida de risco, uma vez que se preocupa apenas com desvios adversos" (Markowitz, 1990). Investidores racionais não temem ganhos inesperados; eles temem perdas.
No entanto, Markowitz optou pela variância baseada em critérios de "custo, conveniência e familiaridade" (SciSpace, 2025).
**Custo Computacional:** Na era dos mainframes primitivos e cartões perfurados, o custo de computação era uma barreira formidável. A otimização baseada na variância envolvia álgebra linear padrão e inversão de matrizes covariância, operações para as quais existiam algoritmos eficientes (como o *Critical Line Algorithm* desenvolvido pelo próprio Markowitz) (Avoiding..., 2025). A semivariância, por outro lado, exigia o dobro de dados de entrada (matrizes de semicovariância) e resultava em problemas de otimização mais complexos, onde a matriz de covariância se tornava endógena aos pesos do portfólio (SciSpace, 2025).
**Convenência Analítica:** Se os retornos dos ativos seguirem uma distribuição normal (simétrica), a média e a variância são estatísticas suficientes para descrever toda a distribuição. Nesse caso específico, minimizar a variância é matematicamente equivalente a minimizar a semivariância (SciSpace, 2025). Markowitz apostou na aproximação normal como uma simplificação aceitável para tornar a teoria operacionalizável.
Apesar de Markowitz ter sugerido que a semivariância seria preferível com o aumento do poder computacional, a variância entrincheirou-se como o padrão da indústria, moldando décadas de teoria financeira, desde o Índice de Sharpe até o modelo Black-Scholes (SciSpace, 2025).

## 3. Risco, Retorno e Covariância: A Matemática da Diversificação

A contribuição técnica mais duradoura de Markowitz foi a formulação estatística do risco do portfólio, demonstrando que o risco de um todo não é meramente a soma dos riscos das partes.

### 3.1 Retorno Esperado do Portfólio

O retorno esperado de um portfólio ($E(R_p)$) é uma função linear simples dos ativos que o compõem. É a média ponderada dos retornos esperados individuais ($E(R_i)$), onde os pesos ($w_i$) representam a fração do capital alocada em cada ativo:

$$E(R_p) = \sum_{i=1}^{n} w_i E(R_i)$$
Esta linearidade implica que a diversificação não altera o potencial de retorno médio do portfólio; ela apenas dilui os retornos extremos dos ativos individuais (Wikipedia, 2025).

### 3.2 Variância e Covariância

Diferentemente do retorno, a variância do portfólio ($\sigma_p^2$) não é linear. Ela depende crucialmente das **covariâncias** entre os ativos, capturando como os preços dos ativos se movem uns em relação aos outros. A fórmula da variância para um portfólio de $n$ ativos é:

$$\sigma_p^2 = \sum_{i=1}^{n} w_i^2 \sigma_i^2 + \sum_{i=1}^{n} \sum_{j=1, j \neq i}^{n} w_i w_j \sigma_{ij}$$
Ou, em notação matricial, $\sigma_p^2 = \mathbf{w}^T \mathbf{\Sigma} \mathbf{w}$, onde $\mathbf{\Sigma}$ é a matriz de covariância (Stanford, 2025).
Markowitz demonstrou a "Lei da Covariância Média": à medida que o número de ativos ($n$) em um portfólio igualmente ponderado aumenta, a contribuição das variâncias individuais ($\frac{1}{n}\bar{\sigma}^2$) para o risco total tende a zero, enquanto a contribuição das covariâncias ($\frac{n-1}{n}\bar{\sigma}_{ij}$) domina (Scribd, 2025). No limite, o risco de um portfólio diversificado é determinado quase inteiramente pela covariância média entre os ativos, e não pela volatilidade individual de cada um (Wikipedia, 2025).

### 3.3 O Papel da Correlação

A covariância ($\sigma_{ij}$) é o produto da correlação ($\rho_{ij}$) e dos desvios padrão ($\sigma_i, \sigma_j$). O coeficiente de correlação, variando entre -1 e +1, é o "motor" da diversificação:
**Correlação Perfeita (+1):** O risco do portfólio é a média ponderada dos riscos individuais. Não há benefício de diversificação.
**Correlação Inferior a 1:** O risco do portfólio será sempre menor que a média ponderada dos riscos individuais. A volatilidade idiossincrática é cancelada (IFA, 2025).
**Correlação Negativa (-1):** Permite, teoricamente, a construção de um portfólio com variância zero (hedge perfeito).
A intuição de Markowitz foi quantificar que, ao combinar ativos com correlação imperfeita, o investidor reduz a exposição a riscos específicos (choques que afetam apenas uma empresa), mantendo apenas a exposição aos riscos comuns que afetam todo o sistema (GuidedChoice, 2025).

## 4. A Fronteira Eficiente: Otimização e Geometria

A aplicação dos princípios de média-variância a um universo de ativos resulta na construção da Fronteira Eficiente, o conjunto de todos os portfólios ótimos que dominam as demais alternativas.

### 4.1 Derivação e Definição

A Fronteira Eficiente é o lugar geométrico no espaço risco-retorno que representa os portfólios que oferecem o retorno máximo para um dado nível de risco (ou risco mínimo para um dado retorno) (Wikipedia, 2025). Ela é obtida resolvendo um problema de otimização quadrática convexa:

$$\min \mathbf{w}^T \mathbf{\Sigma} \mathbf{w}$$

$$\text{sujeito a: } \mathbf{w}^T \mathbf{\mu} = R_{alvo} \text{ e } \mathbf{w}^T \mathbf{1} = 1$$
A forma geométrica exata desta fronteira depende criticamente das restrições impostas aos pesos ($w_i$):
**Sem Restrições a Vendas a Descoberto (Unconstrained/Short Selling Allowed):** Se o investidor pode vender a descoberto (assumir pesos negativos) ilimitadamente, a fronteira eficiente é uma **hipérbole** perfeita e suave no espaço média-desvio padrão (Gundersen, 2025). O ramo superior desta hipérbole (acima do vértice) é a fronteira eficiente propriamente dita.
**Com Restrições a Vendas a Descoberto (No Short Selling Constraint):** Quando impomos a restrição de não-negatividade ($w_i \geq 0$), a fronteira deixa de ser uma hipérbole única e torna-se uma curva convexa composta por uma série de **segmentos de hipérbole conectados** (*piecewise hyperbolic segments*) (MOSEK, 2025).
*Mecanismo:* A transição de um segmento hiperbólico para outro ocorre nos "corner portfolios" (portfólios de canto). À medida que nos movemos ao longo da fronteira (aumentando o retorno esperado), a composição do portfólio muda. Quando o peso de um ativo atinge zero (sai do portfólio) ou quando um novo ativo entra no portfólio (peso torna-se positivo), a equação algébrica que descreve a curva muda, criando um "ponto de solda" entre dois arcos hiperbólicos distintos (ResearchGate, 2025).
*Implicação:* A fronteira com restrições é finita, começando no portfólio de mínima variância global e terminando no ativo individual de maior retorno (e risco), ao contrário da fronteira sem restrições que se estende ao infinito através da alavancagem de posições vendidas (VICBee Consulting, 2025).
O algoritmo desenvolvido por Markowitz para traçar essa fronteira complexa com restrições de desigualdade é o **Critical Line Algorithm (CLA)**, um método de otimização quadrática paramétrica que precede e inspira os modernos solvers de programação quadrática (Avoiding..., 2025).

### 4.2 O Portfólio de Mínima Variância Global

O vértice da fronteira (seja ela hiperbólica ou segmentada) é o Portfólio de Mínima Variância Global (GMV). Este é o único ponto na curva onde o risco é minimizado em termos absolutos, sem consideração pelo retorno (Grokipedia, 2025). Em teoria, nenhum investidor racional avesso ao risco escolheria um portfólio localizado na parte "inferior" da fronteira (abaixo do GMV), pois para cada ponto nessa região existe um portfólio na parte superior com o mesmo risco, mas com retorno estritamente maior (dominância média-variância) (Gundersen, 2025).

## 5. O Ativo Livre de Risco e o Teorema da Separação

A introdução de um ativo livre de risco (*risk-free asset*) expande o conjunto de oportunidades do investidor além da fronteira de ativos de risco, alterando a geometria da escolha ótima e levando ao Teorema da Separação de Tobin.

### 5.1 O Ativo Livre de Risco

Um ativo livre de risco é definido idealmente como um investimento com variância zero ($\sigma_{rf}^2 = 0$) e, consequentemente, covariância zero com todos os ativos de risco ($\sigma_{i,rf} = 0$) (NPTEL, 2025). Na prática financeira, títulos governamentais de curto prazo, como as *Treasury Bills* dos EUA, são utilizados como *proxies*, assumindo-se ausência de risco de crédito e risco de reinvestimento negligenciável para o horizonte de um período (ResearchGate, 2025).
A inclusão deste ativo permite duas novas operações financeiras fundamentais:
**Empréstimo Livre de Risco (Lending):** O investidor pode aplicar parte de sua riqueza no ativo livre de risco, reduzindo a exposição total ao risco do mercado.
**Tomada de Empréstimo Livre de Risco (Borrowing/Leverage):** O investidor pode tomar dinheiro emprestado à taxa livre de risco para alavancar sua posição nos ativos de risco (Holton, 2025).

### 5.2 O Teorema da Separação de Tobin

James Tobin, em seu artigo seminal de 1958 *Liquidity Preference as Behavior Towards Risk*, formalizou o impacto do ativo livre de risco na teoria da escolha de portfólio (Buiter, 2003). Tobin demonstrou que, na presença de um ativo livre de risco, o processo de decisão de investimento pode ser decomposto em duas etapas distintas e independentes — um resultado conhecido como o **Teorema da Separação** (ou *Two-Fund Separation Theorem*) (Stanford, 2025).
**Etapa 1: A Decisão Técnica (Seleção do Portfólio Ótimo de Risco).** O investidor deve primeiro identificar o portfólio de ativos de risco que maximiza o retorno por unidade de risco. Geometricamente, este é o **Portfólio de Tangência** (Tangency Portfolio), o ponto onde uma linha reta partindo da taxa livre de risco ($R_f$) tangencia a fronteira eficiente hiperbólica dos ativos de risco (Holton, 2025). A composição deste portfólio é puramente técnica e objetiva, dependendo apenas das estimativas de médias, variâncias e covariâncias; ela é *independente* das preferências de risco do investidor individual (Holton, 2025).
**Etapa 2: A Decisão Pessoal (Alocação de Capital).** Uma vez identificado o Portfólio de Tangência, o investidor decide como alocar sua riqueza total entre este portfólio e o ativo livre de risco. Esta decisão depende inteiramente da função de utilidade (aversão ao risco) do indivíduo (Holton, 2025).

### 5.3 A Reta do Mercado de Capitais (Capital Market Line - CML)

A combinação linear do ativo livre de risco com o Portfólio de Tangência gera a **Reta do Mercado de Capitais** (Capital Market Line - CML). A CML torna-se a *nova* fronteira eficiente, pois domina qualquer portfólio situado na fronteira original de ativos de risco (a hipérbole fica inteiramente abaixo da reta CML, exceto no ponto de tangência) (Holton, 2025).
O posicionamento do investidor ao longo da CML é determinado pelo mecanismo de alavancagem:
**Investidores Conservadores (Lending Portfolios):** Localizam-se à esquerda do ponto de tangência ($T$). Eles investem uma fração positiva de sua riqueza no ativo livre de risco e o restante no portfólio $T$. O risco total do portfólio é menor que o risco de $T$ (Holton, 2025).
**Investidores Agressivos (Borrowing Portfolios):** Localizam-se à direita do ponto de tangência ($T$). Eles tomam empréstimos à taxa $R_f$ para investir mais de 100% de seu capital próprio no portfólio $T$, ampliando tanto o retorno esperado quanto a volatilidade (Holton, 2025).
A equação que descreve a CML é:

$$E(R_p) = R_f + \left \sigma_p$$

Onde a inclinação (slope) da reta, $\frac{E(R_T) - R_f}{\sigma_T}$, representa o "preço de mercado do risco" — o retorno adicional que o mercado exige para aceitar uma unidade adicional de desvio padrão (Investopedia, 2025).
**Considerações sobre Taxas de Empréstimo Diferenciadas:** Na realidade, investidores raramente conseguem tomar empréstimos à mesma taxa livre de risco que o governo ($R_{borrow} > R_{lending} = R_f$). Nesse cenário, a CML deixa de ser uma linha reta única e torna-se uma fronteira "quebrada" ou côncava: um segmento linear parte de $R_f$ até um ponto de tangência, segue-se um segmento curvo da fronteira eficiente original (onde o investidor não empresta nem toma emprestado), e então um novo segmento linear parte de outro ponto de tangência com inclinação menor, baseada na taxa de empréstimo mais alta (Stanford, 2025).

## 6. Avaliação de Desempenho: O Índice de Sharpe

A geometria da CML forneceu a base direta para uma das métricas mais onipresentes na avaliação de investimentos: o Índice de Sharpe. Introduzido por William Sharpe em 1966 como "Reward-to-Variability Ratio", o índice operacionaliza o conceito de eficiência média-variância (Wikipedia, 2025).

### 6.1 Definição e Interpretação

O Índice de Sharpe ($S_p$) quantifica o excesso de retorno por unidade de risco total. Matematicamente:

$$S_p = \frac{E(R_p) - R_f}{\sigma_p}$$
Geometricamente, o Índice de Sharpe de um portfólio é a inclinação da linha que conecta a taxa livre de risco a esse portfólio no gráfico média-desvio padrão (Gundersen, 2025). Quanto maior a inclinação, melhor o desempenho ajustado ao risco.

### 6.2 Importância e Aplicação

A maximização do Índice de Sharpe é equivalente a encontrar o Portfólio de Tangência na MPT. Em um mercado em equilíbrio, o portfólio de mercado ($M$) deve ser aquele com o maior Índice de Sharpe possível (Lecture 2..., 2025). A métrica permite comparar fundos e estratégias heterogêneas, nivelando o campo de jogo ao penalizar a volatilidade. No entanto, o índice herda as limitações da variância: se os retornos não forem normais (ex: fundos de hedge com estratégias de opções), o Índice de Sharpe pode ser enganoso, penalizando a volatilidade positiva ou subestimando riscos de cauda, o que levou ao desenvolvimento de métricas alternativas como o **Índice de Sortino** (baseado na semivariância/downside deviation) (Expected..., 2025).

## 7. O Modelo de Precificação de Ativos de Capital (CAPM)

Enquanto a MPT de Markowitz é normativa (diz ao investidor como construir um portfólio), o *Capital Asset Pricing Model* (CAPM) é positivo (explica como os preços dos ativos são determinados se todos seguirem a MPT).

### 7.1 Origem e Desenvolvedores

O CAPM foi desenvolvido independentemente na primeira metade da década de 1960 por William Sharpe (1964), John Lintner (1965), Jan Mossin (1966) e Jack Treynor (1961/1962) (Fama; French, 2004). A unificação dessas teorias rendeu a Sharpe, Markowitz e Merton Miller o Prêmio Nobel de Economia em 1990.55 A intuição central é que, se todos os investidores são racionais, possuem expectativas homogêneas e otimizam seus portfólios segundo a média-variância (usando o Teorema da Separação de Tobin), então todos demandarão o mesmo portfólio de ativos de risco: o **Portfólio de Mercado** ($M$). Para que o mercado "limpe" (oferta iguale demanda), os preços dos ativos devem se ajustar até que o portfólio de tangência seja, de fato, o portfólio de mercado ponderado por valor (Fama; French, 2004).

### 7.2 Decomposição do Risco: Sistemático vs. Não Sistemático

O CAPM introduz uma distinção fundamental na natureza do risco, decompondo a variância total de um ativo ($\sigma_i^2$) em dois componentes 10:
**Risco Sistemático (Risco de Mercado):** É a parcela da volatilidade do ativo que está correlacionada com os movimentos do mercado como um todo. Origina-se de fatores macroeconômicos inelutáveis — inflação, juros, ciclos econômicos, guerras — que afetam todas as empresas simultaneamente. Este risco *não pode* ser eliminado pela diversificação.
**Risco Não Sistemático (Idiossincrático/Específico):** É a parcela da volatilidade exclusiva da empresa ou setor (ex: sucesso de um novo produto, greve na fábrica, fraude contábil). Como esses eventos são estatisticamente independentes entre empresas, em um portfólio amplo eles tendem a se cancelar mutuamente (lei dos grandes números).
A conclusão revolucionária do CAPM é que **o mercado não remunera o risco não sistemático**. Como ele pode ser eliminado gratuitamente através da diversificação, os investidores não devem esperar nenhum prêmio de retorno por assumi-lo. O único risco que justifica um retorno esperado acima da taxa livre de risco é o risco sistemático (Return..., 2025).

### 7.3 O Coeficiente Beta e a Reta do Mercado de Títulos (SML)

Para mensurar o risco sistemático, o CAPM utiliza o coeficiente **Beta** ($\beta$). O Beta é uma medida padronizada da covariância do ativo com o mercado, definida como:

$$\beta_i = \frac{\sigma_{i,M}}{\sigma_M^2} = \rho_{i,M} \frac{\sigma_i}{\sigma_M}$$
Um ativo com $\beta = 1$ move-se, em média, na mesma proporção que o mercado. Um ativo com $\beta > 1$ amplifica os movimentos do mercado (mais risco sistemático), enquanto $\beta < 1$ os atenua.
A relação de equilíbrio entre risco sistemático e retorno esperado é expressa pela equação da **Reta do Mercado de Títulos** (Security Market Line - SML):

$$E(R_i) = R_f + \beta_i$$
A SML difere fundamentalmente da CML. Enquanto a CML (usando $\sigma$) aplica-se apenas a portfólios eficientes (que não possuem risco não sistemático), a SML (usando $\beta$) aplica-se a *qualquer* ativo individual ou portfólio, eficiente ou não, precificando-os de acordo com sua contribuição marginal ao risco do portfólio de mercado (Business Perspectives, 2025).
**Tabela 1: Comparação entre Capital Market Line (CML) e Security Market Line (SML)**

| Característica | Capital Market Line (CML) | Security Market Line (SML) |
| --- | --- | --- |
| Medida de Risco | Desvio Padrão Total ($\sigma$) | Beta Sistemático ($\beta$) |
| Aplicação | Apenas Portfólios Eficientes | Qualquer Ativo Individual ou Portfólio |
| Definição de Risco | Risco Total (Sistemático + Idiossincrático) | Apenas Risco Sistemático (Covariância com Mercado) |
| Ponto de Intercepto | Taxa Livre de Risco ($R_f$) | Taxa Livre de Risco ($R_f$) |
| Inclinação (Slope) | Índice de Sharpe do Mercado ($\frac{E(R_M) - R_f}{\sigma_M}$) | Prêmio de Risco de Mercado ($E(R_M) - R_f$) |
| Fundamentação | Teorema da Separação de Tobin | Modelo de Equilíbrio de Mercado (CAPM) |

Fonte: Elaboração própria com base em (Business Perspectives, 2025).

## 8. Pressupostos, Críticas e Limitações Teóricas

A elegância matemática da MPT e do CAPM repousa sobre um conjunto de axiomas sobre o comportamento humano e a estrutura dos mercados. A validade desses modelos depende, portanto, da robustez de seus pressupostos.

### 8.1 Pressupostos Fundamentais: A Racionalidade VNM

A teoria assume que os investidores são agentes perfeitamente racionais que tomam decisões sob incerteza maximizando a Utilidade Esperada, conforme axiomatizado por John von Neumann e Oskar Morgenstern (VNM) em *Theory of Games and Economic Behavior* (1944) (Wikipedia, 2025). Para que uma função de utilidade esperada exista e represente as preferências do investidor, cinco axiomas fundamentais devem ser satisfeitos 63:
**Completude (Completeness):** O investidor tem preferências bem definidas. Para quaisquer duas loterias (investimentos) A e B, ele pode afirmar se prefere A a B ($A \succ B$), B a A ($B \succ A$) ou se é indiferente ($A \sim B$). A indecisão não é permitida (Wikipedia, 2025).
**Transitividade (Transitivity):** As preferências são consistentes. Se $A \succ B$ e $B \succ C$, então logicamente $A \succ C$. A violação deste axioma implicaria comportamento cíclico e irracional ("money pump") (Wikipedia, 2025).
**Continuidade (Continuity):** Também conhecido como axioma de Arquimedes. Se $A \succ B \succ C$, existe uma probabilidade $p$ tal que o investidor é indiferente entre receber B com certeza ou uma loteria que paga A com probabilidade $p$ e C com probabilidade $1-p$. Isso impede que qualquer resultado seja infinitamente desejável ou indesejável (como o paraíso ou a morte) a ponto de ignorar probabilidades (Wikipedia, 2025).
**Independência (Independence):** A preferência entre duas opções não deve ser alterada pela introdução de uma terceira opção comum a ambas. Se $A \succ B$, então uma mistura de A com C deve ser preferida à mesma mistura de B com C. Este é o axioma mais controverso e frequentemente violado em testes empíricos (ex: Paradoxo de Allais) (Wikipedia, 2025).
**Dominância (Dominance/Monotonicity):** Se uma opção A oferece resultados melhores que B em pelo menos um estado da natureza e resultados iguais ou melhores em todos os outros estados, então A deve ser estritamente preferida a B. Este axioma encapsula a ideia racional de que "mais é melhor que menos" e violações a ele (como escolher uma opção dominada estocasticamente) são consideradas erros graves de decisão (Pecorari, 2022).
**Tabela 2: Axiomas da Teoria da Utilidade Esperada (VNM)**

| Axioma | Definição Simplificada | Implicação Financeira |
| --- | --- | --- |
| Completude | Capacidade de ranquear qualquer par de ativos. | O mercado pode precificar todos os ativos. |
| Transitividade | Consistência lógica ($A>B, B>C \Rightarrow A>C$). | Evita arbitragem cíclica irracional. |
| Continuidade | Existência de "pontos de indiferença" probabilísticos. | Permite modelar o trade-off risco-retorno de forma contínua. |
| Independência | Preferências não mudam com opções irrelevantes. | A diversificação é consistente independentemente do resto da carteira. |
| Dominância | Preferência por "mais riqueza" e "menos risco". | Fundamenta a fronteira eficiente (ninguém escolhe portfólios dominados). |

Fonte: Elaboração própria baseada em (Pecorari, 2022).

### 8.2 Limitações e a Realidade dos Mercados

As críticas à MPT e ao CAPM surgem da desconexão entre esses axiomas ideais e a realidade empírica dos mercados financeiros.
**Distribuições Não-Normais (Caudas Gordas):** A MPT assume que os retornos seguem uma distribuição Normal (Gaussiana), o que justifica o uso da variância como medida completa de risco. Contudo, estudos seminais de Benoit Mandelbrot (1963) e Eugene Fama (1965) demonstraram que os preços de ativos exibem "caudas gordas" (*fat tails*) e leptocurtose excessiva (Mandelbrot; Hudson, 2004). Na realidade, eventos extremos (como *crashes* de mercado de 10 ou 20 desvios padrão) ocorrem com frequência muito maior do que a prevista pela curva normal. O uso da variância subestima drasticamente o risco real de eventos catastróficos ("Cisnes Negros"), tornando a MPT perigosa em momentos de crise (Proactive..., 2025).
**Limitações da Variância:** Como discutido na seção 2.2, a variância penaliza igualmente a volatilidade para cima (lucro) e para baixo (perda). Investidores reais, no entanto, exibem aversão à perda, não à volatilidade *per se*. A semivariância ou métricas de *downside risk* seriam descritores mais precisos da utilidade do investidor, mas a inércia da tradição MPT mantém a variância como padrão (SciSpace, 2025).
**Violações da Racionalidade:** A Economia Comportamental (Kahneman e Tversky) documentou sistemáticas violações dos axiomas VNM. O "efeito certeza" e a "aversão à perda" (Teoria da Perspectiva) mostram que investidores reais frequentemente violam os axiomas de Independência e Dominância, comportando-se de maneira inconsistente com a maximização da utilidade esperada (Blavatskyy, 2025).
Apesar dessas falhas descritivas, a estrutura criada por Markowitz, Tobin e Sharpe permanece a *lingua franca* das finanças. Conceitos como diversificação, fronteira eficiente, Beta e Índice de Sharpe fornecem as ferramentas heurísticas indispensáveis para a alocação de ativos institucional, servindo como um modelo normativo de como o mercado *deveria* funcionar sob condições ideais, mesmo que a realidade frequentemente divirja do modelo.
#### Referências citadas

1. WILLIAMS, John Burr. **The Theory of Investment Value**. [S. l.]: riomaisseguro.rio.rj.gov.br, 1938. Acesso em: 28 nov. 2025.

2. RUBINSTEIN, Mark. Markowitz's "Portfolio Selection": A Fifty-Year Retrospective. **The Journal of Finance**, v. 57, n. 3, p. 1041-1045, 2002. Acesso em: 28 nov. 2025.

3. **MARKOWITZ for the Masses: The Risk and Return of Equity and Portfolio Construction Techniques**. ResearchGate, 2025. Acesso em: 28 nov. 2025.

4. BOYD, Stephen et al. **Markowitz Portfolio Construction at Seventy**. Stanford University, 2024. Acesso em: 28 nov. 2025.

5. **MODERN portfolio theory**. Wikipedia, 2025. Acesso em: 28 nov. 2025.

6. MARKOWITZ, Harry. Portfolio Selection. **The Journal of Finance**, v. 7, n. 1, p. 77-91, Mar. 1952. Acesso em: 28 nov. 2025.

7. **HARRY Markowitz's Modern Portfolio Theory: The Efficient Frontier**. GuidedChoice, 2025. Acesso em: 28 nov. 2025.

8. **WORDS From the Wise Harry Markowitz**. AQR Capital Management, 2025. Acesso em: 28 nov. 2025.

9. **HARRY Markowitz: The Father of Modern Portfolio Theory**. Index Fund Advisors, Inc., 2025. Acesso em: 28 nov. 2025.

10. ESTRUTURA Tópicos _2026. [S. l.]: [s. n.], 2026. Documento de trabalho (Internal Document).

11. **MODERN Portfolio Theory: What MPT Is and How Investors Use It**. Investopedia, 2025. Acesso em: 28 nov. 2025.

12. **MEAN-SEMIVARIANCE Optimization: A Heuristic Approach**. SciSpace, 2025. Acesso em: 28 nov. 2025.

13. **PORTFOLIO OPTIMIZATION WITH SEMI-VARIANCE MODEL: AN APPLICATION ON BIST-100 INDEX***. DergiPark, 2025. Acesso em: 28 nov. 2025.

14. MARKOWITZ, Harry M. **Prize Lecture**: Portfolio Selection: Efficient Diversification of Investments. Nobel Prize, 1990. Acesso em: 28 nov. 2025.

15. **MARKOWITZ Semivariance 1959 | PDF | Sampling (Statistics) | Variance**. Scribd, 2025. Acesso em: 28 nov. 2025.

16. **MEAN-SEMIVARIANCE Behavior: A Note**. IESE Blog Network, 2025. Acesso em: 28 nov. 2025.

17. **MEAN-SEMIVARIANCE Analysis of Option-Based Strategies: A Total Asset Mix Perspective**. Hillsdale Investment Management Inc., 2025. Acesso em: 28 nov. 2025.

18. **AVOIDING the Downside: A Practical Review of the Critical Line Algorithm for Mean-Semivariance Portfolio Optimization**. Hudson Bay Capital, 2025. Acesso em: 28 nov. 2025.

19. **A Brief History of Downside Risk Measures**. Portfolio Management Research, 2025. Acesso em: 28 nov. 2025.

20. **ROBUST Efficient Frontier Analysis with a Separable Uncertainty Model**. Stanford University, 2025. Acesso em: 28 nov. 2025.

21. **AN Application of Portfolio Mean-Variance and Semi-Variance Optimization Techniques: A Case of Fiji**. Semantic Scholar, 2025. Acesso em: 28 nov. 2025.

22. **THE Early History of Portfolio Theory: 1600-1960: Perspectives | PDF**. Scribd, 2025. Acesso em: 28 nov. 2025.

23. **MEAN–VARIANCE and mean–semivariance portfolio selection: a multivariate nonparametric approach**. ResearchGate, 2025. Acesso em: 28 nov. 2025.

24. **EFFICIENT frontier**. Wikipedia, 2025. Acesso em: 28 nov. 2025.

25. GUNDERSEN, Gregory. **Geometry of the Efficient Frontier**. Gregory Gundersen Blog, 2025. Acesso em: 28 nov. 2025.

26. **MOSEK Portfolio Optimization Cookbook**. Documentation, 2025. Acesso em: 28 nov. 2025.

27. **EFFICIENT Frontier in Constrained Portfolios**. VICBee Consulting, 2025. Acesso em: 28 nov. 2025.

28. **[PDF] Applying Markowitz's Critical Line Algorithm**. Semantic Scholar, 2025. Acesso em: 28 nov. 2025.

29. **PARAMETRICALLY computing efficient frontiers of portfolio selection and reporting and utilizing the piecewise-segment structure**. ResearchGate, 2025. Acesso em: 28 nov. 2025.

30. **NORMAL Asset Allocations and Their Statistical Properties**. MDPI, 2025. Acesso em: 28 nov. 2025.

31. **HANDBOOK OF FINANCIAL ENGINEERING**. ResearchGate, 2025. Acesso em: 28 nov. 2025.

32. **EUROPEAN Journal of Operational Research Computing cardinality constrained portfolio selection efficient frontiers via closest c**. 2025. Acesso em: 28 nov. 2025.

33. **MARKOWITZ model**. Grokipedia, 2025. Acesso em: 28 nov. 2025.

34. **NPTEL Course - Session-23 Capital Market Theory-I**. 2025. Acesso em: 28 nov. 2025.

35. **(PDF) Semi-Variance in Finance**. ResearchGate, 2025. Acesso em: 28 nov. 2025.

36. **UNDERSTANDING the CAPM: Key Formula, Assumptions, and Applications**. Investopedia, 2025. Acesso em: 28 nov. 2025.

37. HOLTON, Glyn. **Capital Market Line**. GlynHolton.com, 2025. Acesso em: 28 nov. 2025.

38. **LECTURE 2: Fundamentals of mean- variance analysis**. 2025. Acesso em: 28 nov. 2025.

39. BUITER, Willem H. **James Tobin**: An Appreciation of his Contribution to Economics. NBER Working Paper Series, Working Paper 9753, 2003. Acesso em: 28 nov. 2025.

40. TOBIN, James. Liquidity Preference as Behavior Towards Risk. **The Review of Economic Studies**, v. 25, n. 2, p. 65-86, 1958. Acesso em: 28 nov. 2025.

41. **TWO-FUND Separation under Model Mis-Specification**. Stanford University, 2025. Acesso em: 28 nov. 2025.

42. **ON Portfolio Separation Theorems with Heterogeneous Beliefs and Attitudes towards Risk**. 2025. Acesso em: 28 nov. 2025.

43. **CHAPTER 14: Leverage versus Concentration - A Practitioner's Guide to Asset Allocation [Book]**. O'Reilly, 2025. Acesso em: 28 nov. 2025.

44. **UNDERSTANDING Capital Market Line (CML) and How to Calculate It**. Investopedia, 2025. Acesso em: 28 nov. 2025.

45. **FUZZINESS and funds allocation in portfolio optimization**. Smarandache Notions, 2025. Acesso em: 28 nov. 2025.

46. **THE Capital Market Theory: Markowitz, CML, and Separation Theorem**. ResearchGate, 2025. Acesso em: 28 nov. 2025.

47. **THE Capital Asset Pricing Model: An Overview of the Theory**. Canadian Center of Science and Education, 2025. Acesso em: 28 nov. 2025.

48. **THE Portfolio Separation Theorem**. Econlib, 2025. Acesso em: 28 nov. 2025.

49. **VON Neumann–Morgenstern utility theorem**. Wikipedia, 2025. Acesso em: 28 nov. 2025.

50. **BA 513: Ph.D. Seminar on Choice Theory Professor Robert Nau Fall Semester 2008**. Duke People, 2025. Acesso em: 28 nov. 2025.

51. **EXPECTED Utility Theory without the Completeness Axiom∗**. 2025. Acesso em: 28 nov. 2025.

52. **THE-SORTINO-RATIO.PDF**. 2025. Acesso em: 28 nov. 2025.

53. FAMA, Eugene F.; FRENCH, Kenneth R. The Capital Asset Pricing Model: Theory and Evidence. **Journal of Economic Perspectives**, v. 18, n. 3, p. 25-46, 2004. Acesso em: 28 nov. 2025.

54. **CAPITAL asset pricing model**. Wikipedia, 2025. Acesso em: 28 nov. 2025.

55. **CAPITAL asset pricing model**. Risk Management (FIN 4335) Course Website, 2025. Acesso em: 28 nov. 2025.

56. **12 Return, Risk, and the**. 2025. Acesso em: 28 nov. 2025.

57. **HANDOUT 8: Understanding the CAPM Corporate Finance, Sections 001 and 002 The CAPM consists of two statements 1. The tangency po**. 2025. Acesso em: 28 nov. 2025.

58. **ANALYSIS of Systematic Risk: Decomposition and Portfolio Efficiency - The Research Repository @ WVU**. West Virginia University, 2025. Acesso em: 28 nov. 2025.

59. **SPECIFIC risk**. SimTrade blog, 2025. Acesso em: 28 nov. 2025.

60. **THE capital asset pricing model – part 3**. ACCA Global, 2025. Acesso em: 28 nov. 2025.

61. **“PORTFOLIO optimization in a mean-semivariance framework”**. Business Perspectives, 2025. Acesso em: 28 nov. 2025.

62. **ISOLATING the Systematic Component of a Single Stock's (or Portfolio's) Standard Deviation**. CORE, 2025. Acesso em: 28 nov. 2025.

63. **EXPECTED utility hypothesis**. Wikipedia, 2025. Acesso em: 28 nov. 2025.

64. **3.4: Choice under Uncertainty - Expected Utility Theory**. Business LibreTexts, 2025. Acesso em: 28 nov. 2025.

65. PECORARI, Matheus. **A Racionalidade por trás de Escolhas sob Incertezas**. São Paulo: Insper, 2022. Acesso em: 28 nov. 2025.

66. **CAP 03 - Teoria Da Escolha | PDF | Utilidade | Avaliação de risco**. Scribd, 2025. Acesso em: 28 nov. 2025.

67. **RATIONALITY in Economics: Theory and Evidence**. EconStor, 2025. Acesso em: 28 nov. 2025.

68. GUSTAFSSON, Johan E. **The Axioms of Expected-Utility Theory**. Johan E. Gustafsson Blog, 2025. Acesso em: 28 nov. 2025.

69. **DECISION THEORY**. Survey Data Laundering, 2025. Acesso em: 28 nov. 2025.

70. **VON Neumann–Morgenstern utility theorem**. Grokipedia, 2025. Acesso em: 28 nov. 2025.

71. **RATIONAL Economic Decision Making: The Relevance Among The Axioms of The Theory of Expected Utility Rasyonel İktisadi**. DergiPark, 2025. Acesso em: 28 nov. 2025.

72. **CHOICE Under Uncertainty**. 2025. Acesso em: 28 nov. 2025.

73. **FINANÇAS Comp portamentais: o comportame**. 2025. Acesso em: 28 nov. 2025.

74. PINTO, Thais Monteiro. **Finanças Pessoais**. Macaé: UFRJ, 2025. Acesso em: 28 nov. 2025.

75. **LECTURE 4 – Introduction to Utility Theory under Certainty and Uncertainty**. 2025. Acesso em: 28 nov. 2025.

76. MANDELBROT, Benoit; HUDSON, Richard L. **The (Mis)behavior of Markets**: A Fractal View of Financial Turbulence. Yale Math, 2004. Acesso em: 28 nov. 2025.

77. **OPTIMAL Portfolio Choice with Fat Tails**. National Bureau of Economic Research, 2025. Acesso em: 28 nov. 2025.

78. **IS modern portfolio theory seriously flawed?**. Proactive Advisor Magazine, 2025. Acesso em: 28 nov. 2025.

79. **REVISITING Modern Portfolio Theory and Portfolio Construction**. 2025. Acesso em: 28 nov. 2025.

80. BLAVATSKYY, Pavlo R. **"Expected Utility - Mean Absolute Semideviation" Model of Individual Decision Making under Risk**. Cerge-Ei, 2025. Acesso em: 28 nov. 2025.

81. **EXPECTED Utility Theory**. 2025. Acesso em: 28 nov. 2025.
