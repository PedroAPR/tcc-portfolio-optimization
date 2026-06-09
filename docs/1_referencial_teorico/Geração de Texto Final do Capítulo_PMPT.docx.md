

# **Capítulo 2: A Teoria Pós-Moderna do Portfólio (PMPT) e a Gestão de Risco Assimétrica**

## **2.1 Introdução: A Evolução Paradigmática e a Necessidade Histórica da PMPT**

A história das finanças quantitativas é, em grande medida, a história da busca por uma métrica de risco que reflita fidedignamente a experiência humana de perda e incerteza. A Moderna Teoria do Portfólio (MPT), introduzida pelo trabalho seminal de Harry Markowitz em 1952, *Portfolio Selection*, estabeleceu o alicerce sobre o qual a gestão moderna de investimentos foi construída, formalizando a intuição da diversificação através da análise de média-variância.2 No entanto, a hegemonia da MPT, embora duradoura, fundamentou-se em simplificações matemáticas — notadamente a distribuição normal dos retornos e a variância como *proxy* de risco — que se mostraram cada vez mais dissonantes da realidade empírica dos mercados globais e da psicologia do investidor.4

O surgimento da Teoria Pós-Moderna do Portfólio (PMPT) não deve ser interpretado como uma refutação do trabalho de Markowitz, mas sim como a sua evolução necessária e, ironicamente, um retorno às intenções originais do próprio autor. A PMPT emergiu formalmente no início da década de 1990, impulsionada pelo aumento exponencial da capacidade computacional, que permitiu aos pesquisadores e praticantes modelar a assimetria inerente aos retornos financeiros.6 Enquanto a MPT opera sob a suposição de simetria, tratando ganhos e perdas de igual magnitude como eventos de risco equivalentes, a PMPT reconhece a assimetria fundamental da preferência do investidor: a aversão à perda (downside) em detrimento da mera aversão à volatilidade.5

Este capítulo dedica-se a uma exegese profunda da PMPT, explorando suas raízes históricas, sua fundamentação matemática nos Momentos Parciais Inferiores (Lower Partial Moments \- LPM), e a superioridade de suas métricas de risco — como a Semivariância, o Expected Shortfall (CVaR) e os índices de Sortino e Omega — em comparação com os análogos da MPT. A análise demonstrará que a PMPT oferece um arcabouço mais robusto para a construção de portfólios em um mundo caracterizado por distribuições de cauda gorda (*fat tails*), cisnes negros e comportamento irracional dos agentes.8

### **2.1.1 O "Esquecimento Tecnológico" e as Origens em Markowitz (1959)**

É um equívoco comum na literatura financeira atribuir a invenção do foco no *downside risk* exclusivamente aos teóricos da década de 1990\. Uma análise historiográfica rigorosa revela que Harry Markowitz, em sua monografia de 1959, *Portfolio Selection: Efficient Diversification of Investments*, dedicou um capítulo inteiro à semivariância.10 Markowitz postulou explicitamente que a semivariância — a variância calculada apenas sobre os retornos que caem abaixo da média ou de um alvo — produzia portfólios "intuitivamente melhores" do que aqueles baseados na variância total, pois os investidores não percebem a volatilidade positiva (ganhos acima da média) como risco, mas sim como oportunidade.12

A decisão de Markowitz de fundamentar a MPT na variância, e não na semivariância, foi uma concessão pragmática imposta pelas restrições tecnológicas da época. Na década de 1950, o custo computacional para calcular a covariância de *downside* para um portfólio diversificado era proibitivo. A variância, com suas propriedades algébricas elegantes e simétricas, permitia soluções analíticas fechadas que podiam ser resolvidas com os recursos limitados disponíveis.11

Consequentemente, a indústria financeira passou as três décadas seguintes otimizando portfólios com base em uma medida de risco (desvio padrão) que o próprio criador da teoria considerava uma segunda melhor opção.14 Foi somente com o advento dos microcomputadores de alta performance nas décadas de 1980 e 1990 que a barreira computacional foi superada, permitindo o renascimento da semivariância sob a égide da PMPT.15

### **2.1.2 A Consolidação da PMPT: Rom, Ferguson e o Instituto de Pesquisa de Pensões**

A formalização do termo "Teoria Pós-Moderna do Portfólio" é creditada aos desenvolvedores de software Brian M. Rom e Kathleen Ferguson, que publicaram trabalhos seminais em 1993 e 1994 no *The Journal of Investing*.6 Rom e Ferguson identificaram falhas críticas nos softwares de otimização baseados na MPT e propuseram uma nova estrutura que incorporava a assimetria das distribuições de retorno.17

Paralelamente, o suporte acadêmico para a PMPT foi solidificado pelo *Pension Research Institute* (PRI) na Universidade Estadual de São Francisco. Pesquisadores como Dr. Frank Sortino e Dr. Hal Forsey, trabalhando com base nos teoremas de Bawa (1975) e Fishburn (1977), desenvolveram algoritmos práticos para calcular o risco de *downside* e a distribuição log-normal de três parâmetros, que se ajustava melhor aos dados de mercado do que a distribuição normal da MPT.16 O trabalho de Sortino, em particular, foi crucial para traduzir a teoria complexa dos momentos parciais em ferramentas aplicáveis, culminando na criação do Índice de Sortino, que se tornou o estandarte da análise de desempenho ajustada ao risco de *downside*.13

---

## **2.2 Desconstrução Crítica da MPT: As Falácias da Normalidade e da Utilidade Quadrática**

A resiliência da MPT no meio acadêmico e profissional, apesar de suas limitações conhecidas, deve-se à sua simplicidade pedagógica. No entanto, a aplicação da MPT em mercados reais exige a aceitação de pressupostos que, quando violados, podem levar a alocações de ativos subótimas e a uma subestimação perigosa dos riscos extremos. A PMPT surge como uma resposta direta a duas críticas estruturais à MPT: a suposição de distribuição normal dos retornos e a função de utilidade quadrática do investidor.

### **2.2.1 A Tirania da Curva de Sino: Caudas Gordas e Assimetria**

A MPT assume que os retornos dos ativos financeiros são variáveis aleatórias independentes e identicamente distribuídas (i.i.d.) que seguem uma distribuição normal (Gaussiana). Esta suposição é conveniente porque uma distribuição normal é perfeitamente descrita por apenas dois parâmetros: média ($\\mu$) e desvio padrão ($\\sigma$). Sob esta ótica, a probabilidade de eventos extremos diminui exponencialmente à medida que nos afastamos da média.8

No entanto, evidências empíricas exaustivas demonstram que as séries temporais financeiras exibem características que violam sistematicamente a normalidade:

1. **Leptocurtose (Caudas Gordas):** Os mercados financeiros apresentam uma frequência de eventos extremos (tanto positivos quanto negativos) significativamente maior do que a prevista pela distribuição normal. Eventos de "seis sigmas" ($6\\sigma$), que teoricamente deveriam ocorrer uma vez a cada milhões de anos, ocorrem com uma regularidade alarmante em crises financeiras.21  
2. **Assimetria (Skewness):** Os retornos não são simétricos. Em mercados de ações, por exemplo, observa-se frequentemente uma assimetria negativa, onde as quedas são mais abruptas e profundas do que as altas.23

Implicação para a Gestão de Portfólio:  
Ao utilizar o desvio padrão como medida de risco, a MPT falha em distinguir entre a volatilidade gerada por "saltos" positivos e a volatilidade gerada por "crashes". Mais grave ainda, a MPT subestima o risco de cauda. Um fundo de hedge que opera estratégias de venda de opções fora do dinheiro pode apresentar um desvio padrão baixo e um Índice de Sharpe alto durante longos períodos de calmaria, ocultando um risco latente de ruína que só é capturado por métricas que consideram a curtose e a assimetria, como preconizado pela PMPT.23 A PMPT, ao não assumir normalidade, permite o uso de distribuições mais flexíveis ou métodos não paramétricos que capturam a verdadeira natureza do risco de cauda.16

### **2.2.2 A Função de Utilidade e a Teoria da Perspectiva**

A MPT baseia-se na Teoria da Utilidade Esperada, assumindo implicitamente que a função de utilidade do investidor é quadrática. Matematicamente, isso implica que o investidor penaliza desvios positivos e negativos da média com a mesma intensidade. Em termos práticos, sob a MPT, um retorno excepcionalmente alto é tão indesejável quanto um retorno excepcionalmente baixo, pois ambos aumentam a variância do portfólio.4

Esta premissa entra em conflito direto com as descobertas das Finanças Comportamentais, especificamente a **Teoria da Perspectiva (Prospect Theory)** desenvolvida por Daniel Kahneman e Amos Tversky. A Teoria da Perspectiva demonstra que os investidores exibem **aversão à perda** (*loss aversion*) em vez de aversão ao risco (*risk aversion*).27

* **Aversão à Perda:** A dor psicológica de perder $100 é aproximadamente duas vezes mais intensa do que o prazer de ganhar $100.  
* **Ponto de Referência:** Os investidores avaliam o desempenho não em relação à média do portfólio, mas em relação a um ponto de referência ou alvo (*target return*). Retornos acima do alvo são vistos como "ganhos" e retornos abaixo como "perdas".28

A PMPT operacionaliza a Teoria da Perspectiva ao substituir a média pelo **Retorno Mínimo Aceitável (MAR)** e a variância pelo risco de *downside*. Dessa forma, a PMPT alinha a matemática da otimização de portfólio com a psicologia real do investidor: minimizando a probabilidade e a magnitude de falhar em atingir os objetivos financeiros, enquanto deixa o *upside* livre para capturar retornos excessivos.5

**Tabela 2.1: Comparação Estrutural: MPT vs. PMPT**

| Dimensão Analítica | Moderna Teoria do Portfólio (MPT) | Teoria Pós-Moderna do Portfólio (PMPT) |
| :---- | :---- | :---- |
| **Medida de Risco Central** | Variância / Desvio Padrão ($\\sigma^2, \\sigma$) | Downside Deviation / LPM / CVaR |
| **Distribuição de Retornos** | Normal (Simétrica, Paramétrica) | Qualquer (Não-Normal, Assimétrica, Empírica) |
| **Definição de Risco** | Dispersão em torno da média (Incerteza Total) | Fracasso em atingir o Retorno Mínimo (MAR) |
| **Visão do Investidor** | Avesso à variância (Quadrática) | Avesso à perda (Loss Aversion \- Prospect Theory) |
| **Tratamento do Upside** | Penalizado como risco (aumenta $\\sigma$) | Ignorado ou valorizado (Upside Potential) |
| **Objetivo da Otimização** | Maximizar Retorno para dado $\\sigma$ | Maximizar Retorno para dado Downside Risk |

Fonte: Elaboração baseada em.4

---

## **2.3 Conceitos Fundamentais de 'Downside Risk': A Estrutura dos Momentos Parciais Inferiores (LPM)**

Para superar as limitações da variância, a PMPT adota a estrutura matemática dos Momentos Parciais Inferiores (*Lower Partial Moments* \- LPM). Desenvolvida teoricamente por Bawa (1975) e expandida por Fishburn (1977), a família de métricas LPM oferece uma generalização flexível para mensurar o risco abaixo de um limiar específico.31 A elegância dos LPMs reside na sua capacidade de incorporar diferentes graus de aversão ao risco através de um único parâmetro, $n$ (a ordem do momento).

### **2.3.1 Definição Matemática dos LPMs**

Seja $R$ a variável aleatória que representa os retornos do ativo e $\\tau$ (tau) o Retorno Mínimo Aceitável (MAR) ou *target return*. O LPM de ordem $n$ é definido pela integral:

$$LPM\_n(\\tau) \= \\int\_{-\\infty}^{\\tau} (\\tau \- r)^n f(r) \\, dr$$  
No caso discreto, onde temos uma série temporal de $T$ observações de retorno ($R\_1, R\_2,..., R\_T$), a fórmula torna-se:

$$LPM\_n(\\tau) \= \\frac{1}{T} \\sum\_{t=1}^{T} \\max(0, \\tau \- R\_t)^n$$  
Nesta formulação, apenas os retornos que ficam abaixo do alvo $\\tau$ contribuem para a medida de risco. A função $\\max(0, \\tau \- R\_t)$ atua como um filtro, zerando qualquer contribuição de retornos positivos (acima do alvo), o que reflete matematicamente a premissa de que o *upside* não é risco.33

### **2.3.2 A Hierarquia dos Graus de LPM e suas Interpretações**

A escolha do grau $n$ permite ajustar a métrica à psicologia do investidor, ponderando a severidade das perdas de maneira distinta 33:

1. **LPM de Ordem 0 ($n=0$) – Probabilidade de Perda (Safety First):**  
   * Mede a frequência com que o retorno cai abaixo do alvo.  
   * Matematicamente, equivale a $P(R \< \\tau)$.  
   * *Interpretação:* Responde à pergunta "Qual a chance de eu perder dinheiro?". No entanto, falha em distinguir entre uma perda pequena e uma perda catastrófica (uma perda de 1% conta o mesmo que uma de 50%).15  
2. **LPM de Ordem 1 ($n=1$) – Déficit Esperado (*Target Shortfall*):**  
   * Mede a magnitude média das perdas. Os desvios abaixo do alvo são ponderados linearmente.  
   * *Interpretação:* Responde à pergunta "Se eu perder dinheiro, quanto espero perder em média?". É a medida de risco fundamental para o cálculo do Índice Omega (discutido na Seção 2.5) e reflete um investidor neutro ao risco em relação à severidade da perda, desde que a média seja controlada.33  
3. **LPM de Ordem 2 ($n=2$) – Semivariância (*Target Semivariance*):**  
   * Mede a dispersão quadrática dos retornos abaixo do alvo. Semelhante à variância, mas unilateral.  
   * *Interpretação:* Penaliza desproporcionalmente as grandes perdas. Uma perda duas vezes maior pesa quatro vezes mais no cálculo do risco. Esta é a medida preferida por Markowitz (1959) e a base para o **Desvio Padrão de Downside** ($Downside Deviation \= \\sqrt{LPM\_2}$), que é o denominador do Índice de Sortino.10  
4. **LPM de Ordens Superiores ($n \> 2$):**  
   * Refletem uma aversão extrema a perdas catastróficas. À medida que $n$ aumenta, o foco da métrica desloca-se quase exclusivamente para a cauda esquerda extrema da distribuição, ignorando pequenas flutuações negativas.41

### **2.3.3 Semivariância vs. Variância: O Impacto na Alocação**

A substituição da variância pela semivariância tem implicações profundas na construção de portfólios. Em distribuições simétricas (normais), a semivariância é proporcional à variância, e a fronteira eficiente da PMPT converge para a da MPT. No entanto, na presença de assimetria (skewness), as fronteiras divergem.42

Um ativo com alta assimetria positiva (como uma opção de compra longa ou uma startup de venture capital) terá uma variância alta (devido ao potencial de ganho ilimitado) mas uma semivariância baixa (perda limitada ao capital investido). A MPT penalizaria este ativo, reduzindo sua alocação para diminuir o risco total. A PMPT, utilizando a semivariância, reconheceria o perfil favorável de risco/retorno e aumentaria a alocação, capturando o "upside potential".12 Estudos empíricos mostram que, em mercados emergentes ou durante crises, portfólios otimizados via semivariância tendem a preservar capital de forma mais eficiente do que aqueles baseados em média-variância.45

---

## **2.4 Métricas Avançadas de Risco e Propriedades de Coerência**

A evolução da gestão de riscos não parou nos LPMs. A necessidade de quantificar o capital regulatório bancário e o risco sistêmico levou ao desenvolvimento de métricas baseadas em quantis, como o *Value at Risk* (VaR) e o *Expected Shortfall* (ES/CVaR). A análise dessas métricas sob a perspectiva da teoria axiomática de riscos revela distinções cruciais sobre sua confiabilidade.

### **2.4.1 Value at Risk (VaR): A Revolução Incoerente**

Popularizado em 1994 pelo J.P. Morgan através do sistema *RiskMetrics*, o VaR tornou-se o padrão da indústria para a gestão de riscos de mercado e regulação bancária (Acordos de Basileia I e II).47 O VaR é definido como a perda máxima esperada em um determinado horizonte de tempo, com um certo nível de confiança ($1-\\alpha$).

Por exemplo, um VaR de 99% de $10 milhões em 1 dia implica que há apenas 1% de chance de a perda exceder $10 milhões.

Apesar de sua ubiquidade, o VaR apresenta falhas estruturais graves sob a ótica da PMPT e da teoria estatística:

1. **Cegueira da Cauda (*Tail Blindness*):** O VaR indica o limiar da perda, mas nada diz sobre a severidade da perda caso esse limiar seja ultrapassado. Em distribuições de cauda gorda, a perda média além do VaR pode ser muitas vezes superior ao próprio VaR, ocultando riscos catastróficos.20  
2. **Violação da Subaditividade:** Artzner et al. (1999), em seu artigo fundamental sobre medidas de risco coerentes, demonstraram que o VaR **não é subaditivo**. Isso significa que o VaR de um portfólio diversificado pode ser maior do que a soma dos VaRs dos ativos individuais ($\\text{VaR}(A+B) \> \\text{VaR}(A) \+ \\text{VaR}(B)$). Essa propriedade perversa desencoraja a diversificação e viola um dos princípios basilares da gestão de portfólio.50 Exemplos teóricos e práticos mostram que, em distribuições muito assimétricas ou com caudas pesadas, a fusão de riscos pode parecer aumentar o risco medido pelo VaR, uma anomalia teórica inaceitável.53

### **2.4.2 Medidas de Risco Coerentes e os Axiomas de Artzner**

Para remediar as falhas do VaR, Artzner, Delbaen, Eber e Heath (1999) estabeleceram quatro axiomas que uma medida de risco $\\rho$ deve satisfazer para ser considerada "coerente" e segura para alocação de capital 50:

1. **Monotonicidade:** Se o portfólio $X$ tem retornos sempre melhores que $Y$, o risco de $X$ deve ser menor ($\\text{Se } X \\ge Y, \\text{então } \\rho(X) \\le \\rho(Y)$).  
2. **Subaditividade:** O risco do todo não pode exceder a soma dos riscos das partes ($\\rho(X+Y) \\le \\rho(X) \+ \\rho(Y)$). Garante que a diversificação reduz o risco.  
3. **Homogeneidade Positiva:** O risco escala linearmente com o tamanho da posição ($\\rho(\\lambda X) \= \\lambda \\rho(X)$ para $\\lambda \> 0$).  
4. **Invariância de Translação:** Adicionar um montante garantido de caixa $k$ reduz o risco nesse mesmo montante ($\\rho(X \+ k) \= \\rho(X) \- k$).

### **2.4.3 Conditional Value at Risk (CVaR) / Expected Shortfall (ES)**

Como resposta direta à incoerência do VaR, Rockafellar e Uryasev (2000, 2002\) propuseram e operacionalizaram o *Conditional Value at Risk* (CVaR), também conhecido como *Expected Shortfall* (ES). O CVaR é definido como a média das perdas que ocorrem na cauda da distribuição, estritamente além do ponto de corte do VaR.56

$$CVaR\_{\\alpha}(X) \= E$$  
**Superioridade do CVaR na PMPT:**

* **Coerência:** O CVaR satisfaz todos os axiomas de Artzner, incluindo a subaditividade. Ele reconhece corretamente os benefícios da diversificação mesmo em cenários de estresse extremo.26  
* **Convexidade e Otimização:** Diferentemente do VaR, que é uma função não-convexa e difícil de otimizar (com múltiplos mínimos locais), o CVaR é convexo. Isso permitiu a Rockafellar e Uryasev desenvolver algoritmos de programação linear que podem otimizar portfólios com milhares de ativos e cenários de forma extremamente eficiente, minimizando diretamente o risco de cauda.58  
* **Sensibilidade à Cauda:** O CVaR captura a forma da distribuição na região de perdas extremas. Se um ativo possui "cisnes negros" latentes, o CVaR será significativamente maior que o VaR, alertando o gestor sobre a verdadeira dimensão do risco.61

A transição regulatória global, exemplificada pela *Fundamental Review of the Trading Book* (FRTB) do Comitê de Basileia, que substituiu o VaR pelo Expected Shortfall para o cálculo de capital de risco de mercado, constitui a validação institucional definitiva dos princípios defendidos pela PMPT: o risco real reside na cauda, e métricas incoerentes são inadequadas para a segurança sistêmica.26

---

## **2.5 Indicadores de Desempenho Ajustados: Sortino, Omega e a Generalização Kappa**

A PMPT não se limita a medir o risco; ela redefine a avaliação de desempenho. O onipresente Índice de Sharpe, ao penalizar a volatilidade de alta, falha em capturar o valor gerado por gestores que produzem assimetria positiva. A PMPT propõe alternativas que integram os conceitos de *downside risk* e momentos superiores.

### **2.5.1 O Índice de Sortino: Refinando Sharpe**

Desenvolvido por Frank Sortino no início dos anos 1980 e popularizado nos anos 1990, o Índice de Sortino é a modificação mais direta e amplamente adotada do Índice de Sharpe.13 Ele substitui o desvio padrão total pelo **Desvio de Downside** ($TDD$ ou $\\sigma\_d$) no denominador.

$$\\text{Sortino Ratio} \= \\frac{R\_p \- MAR}{TDD} \= \\frac{R\_p \- MAR}{\\sqrt{LPM\_2(MAR)}}$$  
Onde:

* $R\_p$ é o retorno médio do portfólio.  
* $MAR$ (*Minimum Acceptable Return*) é o retorno alvo definido pelo investidor.  
* $TDD$ (*Target Downside Deviation*) é a raiz quadrada da semivariância em relação ao MAR.

Análise Comparativa:  
O Índice de Sortino e o Sharpe convergem quando a distribuição dos retornos é normal e o MAR é igual à média. Contudo, para estratégias com alta assimetria positiva (e.g., trend following, opções longas), o Sortino será consistentemente superior ao Sharpe, pois não penaliza os ganhos voláteis. Inversamente, para estratégias com assimetria negativa (e.g., venda de volatilidade), o Sortino revelará um desempenho ajustado ao risco inferior, expondo os riscos ocultos que o Sharpe mascara.13

### **2.5.2 O Índice Omega: Capturando Todos os Momentos**

Introduzido por Keating e Shadwick em 2002, o Índice Omega ($\\Omega$) representa um salto conceitual ao dispensar completamente a necessidade de estimar momentos estatísticos (média, variância) e operar diretamente sobre a distribuição de probabilidade cumulativa dos retornos.64

O Omega é definido como a razão entre a probabilidade ponderada de ganhos e a probabilidade ponderada de perdas em relação a um limiar $L$:

$$\\Omega(L) \= \\frac{\\int\_{L}^{\\infty} \[1 \- F(r)\] \\, dr}{\\int\_{-\\infty}^{L} F(r) \\, dr}$$  
Vantagem Crítica:  
O Omega captura implicitamente todos os momentos da distribuição (média, variância, assimetria, curtose e momentos superiores) em uma única métrica. Ao variar o limiar $L$, o Omega fornece um perfil completo de risco-retorno, em vez de uma estimativa pontual. Isso o torna a ferramenta predileta para analisar ativos complexos e não lineares, como fundos de hedge e criptoativos, onde a suposição de normalidade é fatalmente falha.64  
Adicionalmente, existe uma relação direta entre o conceito de *Upside Potential Ratio* e o Omega. O numerador do Omega corresponde ao potencial de alta (*Upside Potential*), enquanto o denominador corresponde ao potencial de baixa (*Downside Potential*), alinhando a métrica com a intuição econômica de ganho *versus* dor.68

### **2.5.3 O Índice Kappa: A Generalização Unificadora**

Kaplan e Knowles (2004) propuseram o Índice Kappa ($K\_n$) como uma medida generalizada que unifica o Sortino e o Omega sob uma única estrutura matemática baseada em LPMs.70

$$K\_n(\\tau) \= \\frac{\\mu \- \\tau}{\\sqrt\[n\]{LPM\_n(\\tau)}}$$  
A elegância do Kappa reside na sua capacidade de recuperar as outras métricas através do ajuste do parâmetro $n$:

* Quando $n=1$, o Kappa é funcionalmente equivalente ao **Índice Omega** (ranking idêntico).  
* Quando $n=2$, o Kappa torna-se o **Índice de Sortino**.  
* Para $n=3$ ou superior, o Kappa penaliza severamente a curtose e riscos extremos de cauda.

Essa generalização permite que gestores de portfólio calibrem a métrica de desempenho especificamente para a função de utilidade de seus clientes. Para um investidor avesso a perdas catastróficas, um $K\_3$ ou $K\_4$ seria mais apropriado; para um investidor focado na probabilidade geral de ganho, um $K\_1$ (Omega) seria ideal.73

---

## **2.6 Fronteiras Eficientes: A Geometria da Assimetria**

A aplicação das métricas de PMPT altera a geometria da fronteira eficiente. Enquanto a fronteira eficiente da MPT (média-variância) é sempre uma hipérbole suave e convexa, a fronteira eficiente da PMPT (retorno-LPM ou retorno-CVaR) pode assumir formas irregulares e não-suaves, especialmente quando composta por ativos com distribuições heterogêneas (mistura de ativos normais e não-normais).43

Em particular, a fronteira da PMPT tende a sugerir alocações mais concentradas em ativos com assimetria positiva e a evitar ativos com caudas esquerdas pesadas, mesmo que estes possuam alta média de retorno. Estudos recentes sobre criptoativos mostram que a otimização via PMPT resulta em portfólios com melhor proteção contra *drawdowns* severos do que a otimização via MPT, dado o perfil extremamente leptocúrtico desses ativos.9

## **2.7 Avanços Recentes e Integração com Machine Learning (2024-2025)**

A fronteira atual da pesquisa em PMPT reside na sua integração com a Inteligência Artificial. Publicações e estudos de 2024 e 2025 indicam uma tendência crescente no uso de algoritmos de **Machine Learning**, como redes neurais recorrentes (LSTM) e Deep Learning, para estimar dinamicamente os Momentos Parciais Inferiores e otimizar portfólios.78

Ao contrário dos modelos estáticos tradicionais que dependem de dados históricos passados, modelos híbridos (PMPT \+ ML) conseguem prever mudanças nos regimes de volatilidade e na forma das caudas (*tail risk forecasting*), ajustando as alocações em tempo real para minimizar o CVaR futuro. Essa abordagem, denominada "Otimização Robusta Dinâmica", supera as limitações da MPT e da PMPT clássica, oferecendo resultados superiores em *backtests* e aplicações reais, especialmente em mercados voláteis e durante transições de regime econômico.80

Além disso, a PMPT tem sido fundamental na integração de critérios ESG (Environmental, Social, and Governance) na gestão de portfólios. Estudos recentes sugerem que o uso de métricas de *downside risk* como o Índice de Sortino revela melhor o perfil de risco ajustado de empresas com altas pontuações ESG, que tendem a ter menor risco de cauda (menor risco reputacional e regulatório) do que empresas convencionais, algo que o Índice de Sharpe muitas vezes falha em capturar.82

## **2.8 Conclusão**

A Teoria Pós-Moderna do Portfólio representa a maturidade da gestão de investimentos quantitativa. Ao rejeitar a simplificação excessiva da normalidade e abraçar a complexidade assimétrica dos mercados e da psicologia humana, a PMPT oferece ferramentas — LPM, CVaR, Sortino, Omega — que são não apenas teoricamente superiores, mas pragmaticamente indispensáveis. Em um ambiente financeiro caracterizado por crises recorrentes e incerteza radical, a capacidade de distinguir entre o risco de ruína e a volatilidade de oportunidade é o que separa a sobrevivência da extinção. A PMPT é a linguagem matemática dessa distinção.

---

**Tabela 2.2: Resumo Analítico dos Indicadores de Desempenho (MPT vs. PMPT)**

| Indicador | Base Teórica | Fórmula Conceitual | Sensibilidade à Cauda | Principal Aplicação |
| :---- | :---- | :---- | :---- | :---- |
| **Sharpe** | MPT (Variância) | $\\frac{Retorno \- R\_f}{\\sigma\_{total}}$ | Baixa (Assume Normalidade) | Ativos tradicionais, Benchmark relativo |
| **Sortino** | PMPT (LPM 2\) | $\\frac{Retorno \- MAR}{\\sigma\_{downside}}$ | Média (Foca no Downside) | Fundos Assimétricos, Hedge Funds |
| **Omega** | PMPT (Todos Momentos) | $\\frac{\\text{Prob. Ponderada Ganhos}}{\\text{Prob. Ponderada Perdas}}$ | Alta (Captura toda distribuição) | Derivativos, Cripto, Private Equity |
| **Kappa ($K\_3$)** | PMPT (LPM 3\) | $\\frac{Retorno \- MAR}{\\sqrt\[1\]{LPM\_3}}$ | Muito Alta (Penaliza extremos) | Gestão de Risco de Cauda, Seguros |

Fonte: Elaboração do autor baseada em.71

#### **Referências citadas**

1. Modern portfolio theory \- Wikipedia, acessado em novembro 28, 2025, [https://en.wikipedia.org/wiki/Modern\_portfolio\_theory](https://en.wikipedia.org/wiki/Modern_portfolio_theory)  
2. Estrutura Tópicos \_2026.docx  
3. Post-Modern Portfolio Theory (PMPT) \- DayTrading.com, acessado em novembro 28, 2025, [https://www.daytrading.com/post-modern-portfolio-theory-pmpt](https://www.daytrading.com/post-modern-portfolio-theory-pmpt)  
4. Post moderne portfolio theorie: Meaning, Criticisms & Real-World Uses \- Diversification.com, acessado em novembro 28, 2025, [https://diversification.com/term/post-moderne-portfolio-theorie](https://diversification.com/term/post-moderne-portfolio-theorie)  
5. Post-Modern Portfolio Theory (PMPT): What it is, How it Works \- Investopedia, acessado em novembro 28, 2025, [https://www.investopedia.com/terms/p/pmpt.asp](https://www.investopedia.com/terms/p/pmpt.asp)  
6. Downside risk \- Wikipedia, acessado em novembro 28, 2025, [https://en.wikipedia.org/wiki/Downside\_risk](https://en.wikipedia.org/wiki/Downside_risk)  
7. Tail Risk Explained: Managing Rare Events Leading to Portfolio Losses \- Investopedia, acessado em novembro 28, 2025, [https://www.investopedia.com/terms/t/tailrisk.asp](https://www.investopedia.com/terms/t/tailrisk.asp)  
8. Cryptocurrencies as an asset class in portfolio optimisation \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/344389567\_Cryptocurrencies\_as\_an\_asset\_class\_in\_portfolio\_optimisation](https://www.researchgate.net/publication/344389567_Cryptocurrencies_as_an_asset_class_in_portfolio_optimisation)  
9. Measuring downside risk — realised semivariance \- Duke Economics, acessado em novembro 28, 2025, [https://public.econ.duke.edu/\~get/browse/courses/201/spr08/DOWNLOADS/New\_Methods\_and\_JumpTests/BNKS-semivariance-2008.pdf](https://public.econ.duke.edu/~get/browse/courses/201/spr08/DOWNLOADS/New_Methods_and_JumpTests/BNKS-semivariance-2008.pdf)  
10. View PDF \- Journal of Investment Managment, acessado em novembro 28, 2025, [https://joim.com/wp-content/uploads/emember/downloads/p0528.pdf](https://joim.com/wp-content/uploads/emember/downloads/p0528.pdf)  
11. Turkish Journal of Computer and Mathematics Education Vol.12 No. 5 (2021), 903-917 Research Article Mean- Adjusted Variance \- Semantic Scholar, acessado em novembro 28, 2025, [https://pdfs.semanticscholar.org/39d1/3494e672ad33c326afa7470eadbaac73f1d6.pdf](https://pdfs.semanticscholar.org/39d1/3494e672ad33c326afa7470eadbaac73f1d6.pdf)  
12. Sortino: A 'Sharper' Ratio | By Thomas N. Rollinger & Scott T. Hoffman | Red Rock Capital \- CME Group, acessado em novembro 28, 2025, [https://www.cmegroup.com/education/files/rr-sortino-a-sharper-ratio.pdf](https://www.cmegroup.com/education/files/rr-sortino-a-sharper-ratio.pdf)  
13. Portfolio Insurance, Portfolio Theory, Market Simulation, and Risks of Portfolio Leverage \- Jacobs Levy Equity Management, acessado em novembro 28, 2025, [https://jlem.com/documents/FG/jlem/news/634593\_Jacobs\_and\_Levy\_-\_Portfolio\_Insurance\_Portfolio\_Theory\_Market\_Simulation\_and\_Risks\_of\_Portfolio\_Leverage.pdf](https://jlem.com/documents/FG/jlem/news/634593_Jacobs_and_Levy_-_Portfolio_Insurance_Portfolio_Theory_Market_Simulation_and_Risks_of_Portfolio_Leverage.pdf)  
14. A Brief History of Downside Risk Measures \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/2382526\_A\_Brief\_History\_of\_Downside\_Risk\_Measures](https://www.researchgate.net/publication/2382526_A_Brief_History_of_Downside_Risk_Measures)  
15. Post-modern portfolio theory \- Wikipedia, acessado em novembro 28, 2025, [https://en.wikipedia.org/wiki/Post-modern\_portfolio\_theory](https://en.wikipedia.org/wiki/Post-modern_portfolio_theory)  
16. Post-modern portfolio theory supports diversification in an investment portfolio to measure investment's performance \- EconStor, acessado em novembro 28, 2025, [https://www.econstor.eu/bitstream/10419/58003/1/688930476.pdf](https://www.econstor.eu/bitstream/10419/58003/1/688930476.pdf)  
17. Post-Modern Portfolio Theory Comes of Age \- Casualty Actuarial Society, acessado em novembro 28, 2025, [https://www.casact.org/abstract/post-modern-portfolio-theory-comes-age](https://www.casact.org/abstract/post-modern-portfolio-theory-comes-age)  
18. Sortino Ratio: Definition, Formula, Calculation, and Example \- Investopedia, acessado em novembro 28, 2025, [https://www.investopedia.com/terms/s/sortinoratio.asp](https://www.investopedia.com/terms/s/sortinoratio.asp)  
19. Expected shortfall \- Wikipedia, acessado em novembro 28, 2025, [https://en.wikipedia.org/wiki/Expected\_shortfall](https://en.wikipedia.org/wiki/Expected_shortfall)  
20. Optimal Portfolio Choice with Fat Tails \- National Bureau of Economic Research, acessado em novembro 28, 2025, [https://www.nber.org/sites/default/files/2023-06/orrc09-16-VD.pdf](https://www.nber.org/sites/default/files/2023-06/orrc09-16-VD.pdf)  
21. Portfolio skew and kurtosis \- Risk.net, acessado em novembro 28, 2025, [https://www.risk.net/sites/default/files/import\_unmanaged/risk.net/data/risk/pdf/technical/risk\_0605\_technical\_buckle.pdf](https://www.risk.net/sites/default/files/import_unmanaged/risk.net/data/risk/pdf/technical/risk_0605_technical_buckle.pdf)  
22. Modern Portfolio Theory: Bruised, Broken, Misunderstood, Misapplied? \- CFA Institute Blogs, acessado em novembro 28, 2025, [https://blogs.cfainstitute.org/investor/2012/10/18/modern-portfolio-theory-bruised-broken-misunderstood-or-misapplied/](https://blogs.cfainstitute.org/investor/2012/10/18/modern-portfolio-theory-bruised-broken-misunderstood-or-misapplied/)  
23. Full article: Portfolio optimisation with higher moments of risk at the Pakistan Stock Exchange \- Taylor & Francis Online, acessado em novembro 28, 2025, [https://www.tandfonline.com/doi/full/10.1080/1331677X.2017.1340182](https://www.tandfonline.com/doi/full/10.1080/1331677X.2017.1340182)  
24. Limitations of the Sharpe Ratio: Understanding Risk in Hedge Funds \- Investopedia, acessado em novembro 28, 2025, [https://www.investopedia.com/articles/07/sharperatio.asp](https://www.investopedia.com/articles/07/sharperatio.asp)  
25. Conditional Value at Risk (CVaR) Template \- Financial Edge, acessado em novembro 28, 2025, [https://www.fe.training/free-resources/portfolio-management/conditional-value-at-risk/](https://www.fe.training/free-resources/portfolio-management/conditional-value-at-risk/)  
26. The clash between titans \- behavioral portfolio theory versus Markowitz's modern portfolio theory \- Monetary research center, acessado em novembro 28, 2025, [https://mrcenter.info/Doc/ConferencePapers/2017/The%20clash%20between%20titans%20-%20behavioral%20portfolio%20theory%20versus%20Markowitz%E2%80%99s%20modern%20portfolio%20theory.pdf](https://mrcenter.info/Doc/ConferencePapers/2017/The%20clash%20between%20titans%20-%20behavioral%20portfolio%20theory%20versus%20Markowitz%E2%80%99s%20modern%20portfolio%20theory.pdf)  
27. Modern Prospect Theory: The Missing Link Between Modern Portfolio Theory and Prospect Theory \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/266794096\_Modern\_Prospect\_Theory\_The\_Missing\_Link\_Between\_Modern\_Portfolio\_Theory\_and\_Prospect\_Theory](https://www.researchgate.net/publication/266794096_Modern_Prospect_Theory_The_Missing_Link_Between_Modern_Portfolio_Theory_and_Prospect_Theory)  
28. What is the post-modern portfolio theory in investing? \- Quora, acessado em novembro 28, 2025, [https://www.quora.com/What-is-the-post-modern-portfolio-theory-in-investing](https://www.quora.com/What-is-the-post-modern-portfolio-theory-in-investing)  
29. Difference Between the Modern Portfolio Theory and the Post-Modern Portfolio Theory \- Teji mandi, acessado em novembro 28, 2025, [https://tejimandi.com/blog/tm-learn/difference-between-the-modern-portfolio-theory-and-the-post-modern-portfolio-theory](https://tejimandi.com/blog/tm-learn/difference-between-the-modern-portfolio-theory-and-the-post-modern-portfolio-theory)  
30. Portfolio Selection and Lower Partial Moments \- Department of Mathematics, acessado em novembro 28, 2025, [https://www.math.kth.se/matstat/seminarier/reports/M-exjobb09/091214b.pdf](https://www.math.kth.se/matstat/seminarier/reports/M-exjobb09/091214b.pdf)  
31. Downside Risk-Based Six-Factor Capital Asset Pricing Model (CAPM): A New Paradigm in Asset Pricing \- MDPI, acessado em novembro 28, 2025, [https://www.mdpi.com/2071-1050/12/17/6756](https://www.mdpi.com/2071-1050/12/17/6756)  
32. Lower Partial Moments under Gram Charlier Distribution: Performance Measures and Efficient Frontiers∗, acessado em novembro 28, 2025, [https://www.ucm.es/data/cont/media/www/pag-37515/LeonMarch05.pdf](https://www.ucm.es/data/cont/media/www/pag-37515/LeonMarch05.pdf)  
33. lpm \- Compute sample lower partial moments of data \- MATLAB \- MathWorks, acessado em novembro 28, 2025, [https://www.mathworks.com/help/finance/lpm.html](https://www.mathworks.com/help/finance/lpm.html)  
34. The role of lower partial moments in stochastic modeling, acessado em novembro 28, 2025, [https://www.dss.uniroma1.it/RePec/mtn/articoli/2008-2-6.pdf](https://www.dss.uniroma1.it/RePec/mtn/articoli/2008-2-6.pdf)  
35. Using Sample and Expected Lower Partial Moments \- MATLAB & Simulink \- MathWorks, acessado em novembro 28, 2025, [https://www.mathworks.com/help/finance/sample-and-expected-lower-partial-moments.html](https://www.mathworks.com/help/finance/sample-and-expected-lower-partial-moments.html)  
36. Lower Partial Moments as Measures of Perceived Risk \- An Experimental Study Matthias Unser \- Universität Münster, acessado em novembro 28, 2025, [https://www.uni-muenster.de/Physik.TP/\~lemm/econoWS99/lower-partial.pdf](https://www.uni-muenster.de/Physik.TP/~lemm/econoWS99/lower-partial.pdf)  
37. CHARACTERISTICS OF OMEGA-OPTIMIZED PORTFOLIOS AT DIFFERENT LEVELS OF THRESHOLD RETURNS \- Vilnius Tech, acessado em novembro 28, 2025, [https://journals.vilniustech.lt/index.php/BMEE/article/download/3517/2948/7654](https://journals.vilniustech.lt/index.php/BMEE/article/download/3517/2948/7654)  
38. Understanding Downside Risk in Investments: Definition and Calculation \- Investopedia, acessado em novembro 28, 2025, [https://www.investopedia.com/terms/d/downsiderisk.asp](https://www.investopedia.com/terms/d/downsiderisk.asp)  
39. Downside Risk \- Overview, How To Calculate and Manage \- Corporate Finance Institute, acessado em novembro 28, 2025, [https://corporatefinanceinstitute.com/resources/career-map/sell-side/capital-markets/downside-risk/](https://corporatefinanceinstitute.com/resources/career-map/sell-side/capital-markets/downside-risk/)  
40. A Brief History of Downside Risk Measures \- Portfolio Management Research, acessado em novembro 28, 2025, [https://www.pm-research.com/content/iijinvest%3A%3A%3A8%3A%3A%3A3%3A%3A%3A9.full.pdf?implicit-login=true\&sigma-token=odAGsFRmFlsRqq7IrQy5zdxeYP6m3d88742LqRu9\_Ow](https://www.pm-research.com/content/iijinvest%3A%3A%3A8%3A%3A%3A3%3A%3A%3A9.full.pdf?implicit-login=true&sigma-token=odAGsFRmFlsRqq7IrQy5zdxeYP6m3d88742LqRu9_Ow)  
41. Risk measurement in post-modern portfolio theory: Differences from modern portfolio theory, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/286072010\_Risk\_measurement\_in\_post-modern\_portfolio\_theory\_Differences\_from\_modern\_portfolio\_theory](https://www.researchgate.net/publication/286072010_Risk_measurement_in_post-modern_portfolio_theory_Differences_from_modern_portfolio_theory)  
42. Post-Modern Portfolio Theory Explained | PDF \- Scribd, acessado em novembro 28, 2025, [https://www.scribd.com/document/165205048/Ferguson-Rom-1](https://www.scribd.com/document/165205048/Ferguson-Rom-1)  
43. A PRACTITIONER'S GUIDE TO ADDRESS FAT TAILS AND DOWNSIDE RISK IN PORTFOLIO CONSTRUCTION \- Journal of Investment Managment, acessado em novembro 28, 2025, [https://www.joim.com/wp-content/uploads/emember/downloads/p0725.pdf](https://www.joim.com/wp-content/uploads/emember/downloads/p0725.pdf)  
44. Multicriteria Portfolio Choice and Downside Risk \- MDPI, acessado em novembro 28, 2025, [https://www.mdpi.com/1911-8074/16/8/367](https://www.mdpi.com/1911-8074/16/8/367)  
45. The introduction of emerging currencies into a portfolio: Towards a more complete diversification model \- Cairn, acessado em novembro 28, 2025, [https://shs.cairn.info/revue-economie-internationale-2010-1-page-5?lang=en\&tab=texte-integral](https://shs.cairn.info/revue-economie-internationale-2010-1-page-5?lang=en&tab=texte-integral)  
46. What Is RiskMetrics in Value at Risk (VaR); Meaning, Methodolgy \- Investopedia, acessado em novembro 28, 2025, [https://www.investopedia.com/ask/answers/041615/what-riskmetrics-value-risk-var.asp](https://www.investopedia.com/ask/answers/041615/what-riskmetrics-value-risk-var.asp)  
47. RiskMetrics \- Value-at-Risk: Theory and Practice, acessado em novembro 28, 2025, [https://www.value-at-risk.net/riskmetrics/](https://www.value-at-risk.net/riskmetrics/)  
48. Comparative analyses of expected shortfall and value-at-risk under market stress \- Bank for International Settlements, acessado em novembro 28, 2025, [https://www.bis.org/cgfs/conf/mar02p.pdf](https://www.bis.org/cgfs/conf/mar02p.pdf)  
49. Coherent risk measure \- Wikipedia, acessado em novembro 28, 2025, [https://en.wikipedia.org/wiki/Coherent\_risk\_measure](https://en.wikipedia.org/wiki/Coherent_risk_measure)  
50. What Is a Coherent Risk Measure? \- CQF, acessado em novembro 28, 2025, [https://www.cqf.com/blog/quant-finance-101/what-is-a-coherent-risk-measure](https://www.cqf.com/blog/quant-finance-101/what-is-a-coherent-risk-measure)  
51. Counterexample to prove that the Value-at-Risk is not subadditive, acessado em novembro 28, 2025, [https://www.karlin.mff.cuni.cz/\~vitali/documentsCourses/ValueatRisk\_notSubadd.pdf](https://www.karlin.mff.cuni.cz/~vitali/documentsCourses/ValueatRisk_notSubadd.pdf)  
52. The Theory, Estimation, and Insurance Applications of Quantile-Based Risk Measures \- University of Nottingham, acessado em novembro 28, 2025, [https://www.nottingham.ac.uk/business/who-we-are/centres-and-institutes/gcbfi/documents/cris-reports/cris-paper-2006-2.pdf](https://www.nottingham.ac.uk/business/who-we-are/centres-and-institutes/gcbfi/documents/cris-reports/cris-paper-2006-2.pdf)  
53. What is an example where VAR does not follow sub-additivity? \- Quora, acessado em novembro 28, 2025, [https://www.quora.com/What-is-an-example-where-VAR-does-not-follow-sub-additivity](https://www.quora.com/What-is-an-example-where-VAR-does-not-follow-sub-additivity)  
54. On Structural Properties of Risk-Averse Optimal Stopping Problems \- arXiv, acessado em novembro 28, 2025, [https://arxiv.org/html/2511.01022v2](https://arxiv.org/html/2511.01022v2)  
55. Conditional Value-at-Risk for General Loss Distributions \- University of Washington Math Department, acessado em novembro 28, 2025, [https://sites.math.washington.edu/\~rtr/papers/rtr187-CVaR2.pdf](https://sites.math.washington.edu/~rtr/papers/rtr187-CVaR2.pdf)  
56. Optimization of Conditional Value-at-Risk \- University of Washington Math Department, acessado em novembro 28, 2025, [https://sites.math.washington.edu/\~rtr/papers/rtr179-CVaR1.pdf](https://sites.math.washington.edu/~rtr/papers/rtr179-CVaR1.pdf)  
57. Conditional Value-at-Risk (CVaR): Algorithms and Applications, acessado em novembro 28, 2025, [https://www2.mathematik.hu-berlin.de/\~romisch/SP01/Uryasev.pdf](https://www2.mathematik.hu-berlin.de/~romisch/SP01/Uryasev.pdf)  
58. Value at Risk or Expected Shortfall | Quantdare, acessado em novembro 28, 2025, [https://quantdare.com/value-at-risk-or-expected-shortfall/](https://quantdare.com/value-at-risk-or-expected-shortfall/)  
59. VaR and CVaR, acessado em novembro 28, 2025, [https://www.karlin.mff.cuni.cz/\~rusy/NMEK613/Seminar/1415z/1415z\_Bejda.pdf](https://www.karlin.mff.cuni.cz/~rusy/NMEK613/Seminar/1415z/1415z_Bejda.pdf)  
60. Value at Risk (VaR) vs Expected Shortfall (ES) \- Forrs.de, acessado em novembro 28, 2025, [https://www.forrs.de/en/news/var-vs-es](https://www.forrs.de/en/news/var-vs-es)  
61. Dynamic asset allocation techniques \- International Actuarial Association, acessado em novembro 28, 2025, [https://actuaries.org/app/uploads/2025/07/ICA2010\_AFIR\_32\_final-paper\_Jarvis.pdf](https://actuaries.org/app/uploads/2025/07/ICA2010_AFIR_32_final-paper_Jarvis.pdf)  
62. Using the Sortino Ratio to Gauge Downside Risk | Charles Schwab, acessado em novembro 28, 2025, [https://www.schwab.com/learn/story/using-sortino-ratio-to-gauge-downside-risk](https://www.schwab.com/learn/story/using-sortino-ratio-to-gauge-downside-risk)  
63. Omega Ratio: Risk Metrics Series | Swan Insights, acessado em novembro 28, 2025, [https://www.swanglobalinvestments.com/advisor/omega-ratio/](https://www.swanglobalinvestments.com/advisor/omega-ratio/)  
64. What is Omega ratio | Capital.com, acessado em novembro 28, 2025, [https://capital.com/en-int/learn/glossary/omega-ratio-definition](https://capital.com/en-int/learn/glossary/omega-ratio-definition)  
65. Omega ratio \- Wikipedia, acessado em novembro 28, 2025, [https://en.wikipedia.org/wiki/Omega\_ratio](https://en.wikipedia.org/wiki/Omega_ratio)  
66. (PDF) A Universal Performance Measure \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/228550687\_A\_Universal\_Performance\_Measure](https://www.researchgate.net/publication/228550687_A_Universal_Performance_Measure)  
67. Is the omega ratio a good portfolio optimization criterion? \- SciELO México, acessado em novembro 28, 2025, [https://www.scielo.org.mx/article\_plus.php?pid=S0186-10422023000100097\&tlng=en\&lng=es](https://www.scielo.org.mx/article_plus.php?pid=S0186-10422023000100097&tlng=en&lng=es)  
68. WORKING PAPER: Picking the Right Risk-Adjusted Performance Metric HIGH LEVEL ANALYSIS, acessado em novembro 28, 2025, [https://s9d6e62ac19c21f7a.jimcontent.com/download/version/1537296680/module/13787459130/name/Picking%20the%20Right%20Risk-Adjusted%20Performance%20Metric.pdf](https://s9d6e62ac19c21f7a.jimcontent.com/download/version/1537296680/module/13787459130/name/Picking%20the%20Right%20Risk-Adjusted%20Performance%20Metric.pdf)  
69. Measures of Risk-adjusted Return \- Turing Finance, acessado em novembro 28, 2025, [http://www.turingfinance.com/computational-investing-with-python-week-one/](http://www.turingfinance.com/computational-investing-with-python-week-one/)  
70. Omega and Kappa Statistics for Hedge Funds \- ABC Quant, acessado em novembro 28, 2025, [https://www.abcquant.com/omega-and-kappa-statistics](https://www.abcquant.com/omega-and-kappa-statistics)  
71. Kappa: A Generalized Downside Risk-Adjusted Performance Measure \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/284690156\_Kappa\_A\_Generalized\_Downside\_Risk-Adjusted\_Performance\_Measure](https://www.researchgate.net/publication/284690156_Kappa_A_Generalized_Downside_Risk-Adjusted_Performance_Measure)  
72. Alternative relative performance measure to Sharpe ratio for non-IID return, acessado em novembro 28, 2025, [https://quant.stackexchange.com/questions/48720/alternative-relative-performance-measure-to-sharpe-ratio-for-non-iid-return](https://quant.stackexchange.com/questions/48720/alternative-relative-performance-measure-to-sharpe-ratio-for-non-iid-return)  
73. Pitfalls of downside performance measures with arbitrary targets \- Fakultät für Wirtschaftswissenschaft \-, acessado em novembro 28, 2025, [https://www.fww.ovgu.de/fww\_media/femm/femm\_2015/2015\_18.pdf](https://www.fww.ovgu.de/fww_media/femm/femm_2015/2015_18.pdf)  
74. Kappa: A Generalized Downside Risk-Adjusted Performance Measure, acessado em novembro 28, 2025, [http://w.performance-measurement.org/KaplanKnowles2004.pdf](http://w.performance-measurement.org/KaplanKnowles2004.pdf)  
75. Cryptocurrencies as an asset class in portfolio optimisation \- IDEAS/RePEc, acessado em novembro 28, 2025, [https://ideas.repec.org/a/vrs/ceuecj/v7y2020i54p33-55n2.html](https://ideas.repec.org/a/vrs/ceuecj/v7y2020i54p33-55n2.html)  
76. 'Portfolio Optimization – Bitcoin & Downside Risk' \- Lund University Publications, acessado em novembro 28, 2025, [https://lup.lub.lu.se/student-papers/record/9082849/file/9082852.pdf](https://lup.lub.lu.se/student-papers/record/9082849/file/9082852.pdf)  
77. Project Portfolio Management Trends: Navigating the Future in 2025 and Beyond, acessado em novembro 28, 2025, [https://blog.greenprojectmanagement.org/index.php/2025/01/21/project-portfolio-management-trends-navigating-future-2025-beyond/](https://blog.greenprojectmanagement.org/index.php/2025/01/21/project-portfolio-management-trends-navigating-future-2025-beyond/)  
78. Top Project Management Trends for 2025 \- PMI California Inland Empire Chapter, acessado em novembro 28, 2025, [https://pmicie.org/articles/114-top-project-management-trends-for-2025](https://pmicie.org/articles/114-top-project-management-trends-for-2025)  
79. Investment Portfolio Optimization: Integrating Portfolio Allocation Methods with RNN LSTM | IEEE Conference Publication | IEEE Xplore, acessado em novembro 28, 2025, [https://ieeexplore.ieee.org/document/10317711/](https://ieeexplore.ieee.org/document/10317711/)  
80. Advancing Investment Frontiers: Industry-grade Deep Reinforcement Learning for Portfolio Optimization \- arXiv, acessado em novembro 28, 2025, [https://arxiv.org/html/2403.07916v1](https://arxiv.org/html/2403.07916v1)  
81. View of Effectiveness of the ESG approach in portfolio selection – an empirical evidence from the US stock market \- Vilnius Tech, acessado em novembro 28, 2025, [https://journals.vilniustech.lt/index.php/JBEM/article/view/24751/13067](https://journals.vilniustech.lt/index.php/JBEM/article/view/24751/13067)  
82. Application of a Robust Maximum Diversified Portfolio to a Small Economy's Stock Market: An Application to Fiji's South Pacific Stock Exchange \- MDPI, acessado em novembro 28, 2025, [https://www.mdpi.com/1911-8074/17/9/388](https://www.mdpi.com/1911-8074/17/9/388)  
83. Sortino, Omega, Kappa: The Algebra of Financial Asymmetry | Request PDF \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/305673511\_Sortino\_Omega\_Kappa\_The\_Algebra\_of\_Financial\_Asymmetry](https://www.researchgate.net/publication/305673511_Sortino_Omega_Kappa_The_Algebra_of_Financial_Asymmetry)