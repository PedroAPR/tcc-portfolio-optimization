# **Capítulo 2: A Teoria Pós-Moderna do Portfólio (PMPT) e a Gestão de Risco Assimétrica**

## **2.1 Introdução: A Evolução Paradigmática e a Necessidade Histórica da PMPT**

A história das finanças quantitativas é, em grande medida, a história da busca por uma métrica de risco que reflita fidedignamente a experiência humana de perda e incerteza. A Moderna Teoria do Portfólio (MPT), introduzida pelo trabalho seminal de Harry Markowitz em 1952, *Portfolio Selection*, estabeleceu o alicerce sobre o qual a gestão moderna de investimentos foi construída, formalizando a intuição da diversificação através da análise de média-variância (MARKOWITZ, 1952). No entanto, a hegemonia da MPT, embora duradoura, fundamentou-se em simplificações matemáticas — notadamente a distribuição normal dos retornos e a variância como *proxy* de risco — que se mostraram cada vez mais dissonantes da realidade empírica dos mercados globais e da psicologia do investidor (ROM; FERGUSON, 1994).

O surgimento da Teoria Pós-Moderna do Portfólio (PMPT) não deve ser interpretado como uma refutação do trabalho de Markowitz, mas sim como a sua evolução necessária e, ironicamente, um retorno às intenções originais do próprio autor. A PMPT emergiu formalmente no início da década de 1990, impulsionada pelo aumento exponencial da capacidade computacional, que permitiu aos pesquisadores e praticantes modelar a assimetria inerente aos retornos financeiros (ROM; FERGUSON, 1994). Enquanto a MPT opera sob a suposição de simetria, tratando ganhos e perdas de igual magnitude como eventos de risco equivalentes, a PMPT reconhece a assimetria fundamental da preferência do investidor: a aversão à perda (*downside*) em detrimento da mera aversão à volatilidade (SORTINO; VAN DER MEER, 1991).

Este capítulo dedica-se a uma exegese profunda da PMPT, explorando suas raízes históricas, sua fundamentação matemática nos Momentos Parciais Inferiores (Lower Partial Moments — LPM), e a superioridade de suas métricas de risco — como a Semivariância, o Expected Shortfall (CVaR) e os índices de Sortino e Omega — em comparação com os análogos da MPT. A análise demonstrará que a PMPT oferece um arcabouço mais robusto para a construção de portfólios em um mundo caracterizado por distribuições de cauda gorda (*fat tails*), cisnes negros e comportamento irracional dos agentes (MANDELBROT, 1963; FAMA, 1965).

### **2.1.1 O "Esquecimento Tecnológico" e as Origens em Markowitz (1959)**

É um equívoco comum na literatura financeira atribuir a invenção do foco no *downside risk* exclusivamente aos teóricos da década de 1990. Uma análise historiográfica rigorosa revela que Harry Markowitz, em sua monografia de 1959, *Portfolio Selection: Efficient Diversification of Investments*, dedicou um capítulo inteiro à semivariância (MARKOWITZ, 1959). Markowitz postulou explicitamente que a semivariância — a variância calculada apenas sobre os retornos que caem abaixo da média ou de um alvo — produzia portfólios "intuitivamente melhores" do que aqueles baseados na variância total, pois os investidores não percebem a volatilidade positiva (ganhos acima da média) como risco, mas sim como oportunidade (ROLLINGER; HOFFMAN, 2013).

A decisão de Markowitz de fundamentar a MPT na variância, e não na semivariância, foi uma concessão pragmática imposta pelas restrições tecnológicas da época. Na década de 1950, o custo computacional para calcular a covariância de *downside* para um portfólio diversificado era proibitivo. A variância, com suas propriedades algébricas elegantes e simétricas, permitia soluções analíticas fechadas que podiam ser resolvidas com os recursos limitados disponíveis (MARKOWITZ, 1959).

Consequentemente, a indústria financeira passou as três décadas seguintes otimizando portfólios com base em uma medida de risco (desvio padrão) que o próprio criador da teoria considerava uma segunda melhor opção (FISHBURN, 1977). Foi somente com o advento dos microcomputadores de alta performance nas décadas de 1980 e 1990 que a barreira computacional foi superada, permitindo o renascimento da semivariância sob a égide da PMPT (ROM; FERGUSON, 1994).

### **2.1.2 A Consolidação da PMPT: Rom, Ferguson e o Instituto de Pesquisa de Pensões**

A formalização do termo "Teoria Pós-Moderna do Portfólio" é creditada aos desenvolvedores de software Brian M. Rom e Kathleen Ferguson, que publicaram trabalhos seminais em 1993 e 1994 no *The Journal of Investing* (ROM; FERGUSON, 1994). Rom e Ferguson identificaram falhas críticas nos softwares de otimização baseados na MPT e propuseram uma nova estrutura que incorporava a assimetria das distribuições de retorno (ROM; FERGUSON, 1994).

Paralelamente, o suporte acadêmico para a PMPT foi solidificado pelo *Pension Research Institute* (PRI) na Universidade Estadual de São Francisco. Pesquisadores como Dr. Frank Sortino e Dr. Hal Forsey, trabalhando com base nos teoremas de Bawa (1975) e Fishburn (1977), desenvolveram algoritmos práticos para calcular o risco de *downside* e a distribuição log-normal de três parâmetros, que se ajustava melhor aos dados de mercado do que a distribuição normal da MPT (SORTINO; VAN DER MEER, 1991). O trabalho de Sortino, em particular, foi crucial para traduzir a teoria complexa dos momentos parciais em ferramentas aplicáveis, culminando na criação do Índice de Sortino, que se tornou o estandarte da análise de desempenho ajustada ao risco de *downside* (ROLLINGER; HOFFMAN, 2013).

---

## **2.2 Desconstrução Crítica da MPT: As Falácias da Normalidade e da Utilidade Quadrática**

A resiliência da MPT no meio acadêmico e profissional, apesar de suas limitações conhecidas, deve-se à sua simplicidade pedagógica. No entanto, a aplicação da MPT em mercados reais exige a aceitação de pressupostos que, quando violados, podem levar a alocações de ativos subótimas e a uma subestimação perigosa dos riscos extremos. A PMPT surge como uma resposta direta a duas críticas estruturais à MPT: a suposição de distribuição normal dos retornos e a função de utilidade quadrática do investidor.

### **2.2.1 A Tirania da Curva de Sino: Caudas Gordas e Assimetria**

A MPT assume que os retornos dos ativos financeiros são variáveis aleatórias independentes e identicamente distribuídas (i.i.d.) que seguem uma distribuição normal (Gaussiana). Esta suposição é conveniente porque uma distribuição normal é perfeitamente descrita por apenas dois parâmetros: média ($\mu$) e desvio padrão ($\sigma$). Sob esta ótica, a probabilidade de eventos extremos diminui exponencialmente à medida que nos afastamos da média (MANDELBROT, 1963).

No entanto, evidências empíricas exaustivas demonstram que as séries temporais financeiras exibem características que violam sistematicamente a normalidade:

1. **Leptocurtose (Caudas Gordas):** Os mercados financeiros apresentam uma frequência de eventos extremos (tanto positivos quanto negativos) significativamente maior do que a prevista pela distribuição normal. Eventos de "seis sigmas" ($6\sigma$), que teoricamente deveriam ocorrer uma vez a cada milhões de anos, ocorrem com uma regularidade alarmante em crises financeiras (BUCKLE, 2006).
2. **Assimetria (Skewness):** Os retornos não são simétricos. Em mercados de ações, por exemplo, observa-se frequentemente uma assimetria negativa, onde as quedas são mais abruptas e profundas do que as altas (ATHAYDE; FLORES, 2017).

**Implicação para a Gestão de Portfólio:**
Ao utilizar o desvio padrão como medida de risco, a MPT falha em distinguir entre a volatilidade gerada por "saltos" positivos e a volatilidade gerada por "crashes". Mais grave ainda, a MPT subestima o risco de cauda. Um fundo de hedge que opera estratégias de venda de opções fora do dinheiro pode apresentar um desvio padrão baixo e um Índice de Sharpe alto durante longos períodos de calmaria, ocultando um risco latente de ruína que só é capturado por métricas que consideram a curtose e a assimetria, como preconizado pela PMPT (ATHAYDE; FLORES, 2017). A PMPT, ao não assumir normalidade, permite o uso de distribuições mais flexíveis ou métodos não paramétricos que capturam a verdadeira natureza do risco de cauda (SORTINO; VAN DER MEER, 1991).

### **2.2.2 A Função de Utilidade e a Teoria da Perspectiva**

A MPT baseia-se na Teoria da Utilidade Esperada, assumindo implicitamente que a função de utilidade do investidor é quadrática. Matematicamente, isso implica que o investidor penaliza desvios positivos e negativos da média com a mesma intensidade. Em termos práticos, sob a MPT, um retorno excepcionalmente alto é tão indesejável quanto um retorno excepcionalmente baixo, pois ambos aumentam a variância do portfólio (ROM; FERGUSON, 1994).

Esta premissa entra em conflito direto com as descobertas das Finanças Comportamentais, especificamente a **Teoria da Perspectiva (Prospect Theory)** desenvolvida por Daniel Kahneman e Amos Tversky. A Teoria da Perspectiva demonstra que os investidores exibem **aversão à perda** (*loss aversion*) em vez de aversão ao risco (*risk aversion*) (KAHNEMAN; TVERSKY, 1979).

* **Aversão à Perda:** A dor psicológica de perder $100 é aproximadamente duas vezes mais intensa do que o prazer de ganhar $100.
* **Ponto de Referência:** Os investidores avaliam o desempenho não em relação à média do portfólio, mas em relação a um ponto de referência ou alvo (*target return*). Retornos acima do alvo são vistos como "ganhos" e retornos abaixo como "perdas" (KAHNEMAN; TVERSKY, 1979).

A PMPT operacionaliza a Teoria da Perspectiva ao substituir a média pelo **Retorno Mínimo Aceitável (MAR)** e a variância pelo risco de *downside*. Dessa forma, a PMPT alinha a matemática da otimização de portfólio com a psicologia real do investidor: minimizando a probabilidade e a magnitude de falhar em atingir os objetivos financeiros, enquanto deixa o *upside* livre para capturar retornos excessivos (SORTINO; VAN DER MEER, 1991).

**Tabela 2.1: Comparação Estrutural: MPT vs. PMPT**

| Dimensão Analítica | Moderna Teoria do Portfólio (MPT) | Teoria Pós-Moderna do Portfólio (PMPT) |
| :---- | :---- | :---- |
| **Medida de Risco Central** | Variância / Desvio Padrão ($\sigma^2, \sigma$) | Downside Deviation / LPM / CVaR |
| **Distribuição de Retornos** | Normal (Simétrica, Paramétrica) | Qualquer (Não-Normal, Assimétrica, Empírica) |
| **Definição de Risco** | Dispersão em torno da média (Incerteza Total) | Fracasso em atingir o Retorno Mínimo (MAR) |
| **Visão do Investidor** | Avesso à variância (Quadrática) | Avesso à perda (Loss Aversion — Prospect Theory) |
| **Tratamento do Upside** | Penalizado como risco (aumenta $\sigma$) | Ignorado ou valorizado (Upside Potential) |
| **Objetivo da Otimização** | Maximizar Retorno para dado $\sigma$ | Maximizar Retorno para dado Downside Risk |

Fonte: Elaboração baseada em ROM; FERGUSON (1994).

---

## **2.3 Conceitos Fundamentais de 'Downside Risk': A Estrutura dos Momentos Parciais Inferiores (LPM)**

Para superar as limitações da variância, a PMPT adota a estrutura matemática dos Momentos Parciais Inferiores (*Lower Partial Moments* — LPM). Desenvolvida teoricamente por Bawa (1975) e expandida por Fishburn (1977), a família de métricas LPM oferece uma generalização flexível para mensurar o risco abaixo de um limiar específico (BAWA, 1975). A elegância dos LPMs reside na sua capacidade de incorporar diferentes graus de aversão ao risco através de um único parâmetro, $n$ (a ordem do momento).

### **2.3.1 Definição Matemática dos LPMs**

Seja $R$ a variável aleatória que representa os retornos do ativo e $\tau$ (tau) o Retorno Mínimo Aceitável (MAR) ou *target return*. O LPM de ordem $n$ é definido pela integral:

$$LPM_n(\tau) = \int_{-\infty}^{\tau} (\tau - r)^n f(r) \, dr$$

No caso discreto, onde temos uma série temporal de $T$ observações de retorno ($R_1, R_2,..., R_T$), a fórmula torna-se:

$$LPM_n(\tau) = \frac{1}{T} \sum_{t=1}^{T} \max(0, \tau - R_t)^n$$

Nesta formulação, apenas os retornos que ficam abaixo do alvo $\tau$ contribuem para a medida de risco. A função $\max(0, \tau - R_t)$ atua como um filtro, zerando qualquer contribuição de retornos positivos (acima do alvo), o que reflete matematicamente a premissa de que o *upside* não é risco (FISHBURN, 1977).

### **2.3.2 A Hierarquia dos Graus de LPM e suas Interpretações**

A escolha do grau $n$ permite ajustar a métrica à psicologia do investidor, ponderando a severidade das perdas de maneira distinta (BAWA, 1975; FISHBURN, 1977):

1. **LPM de Ordem 0 ($n=0$) – Probabilidade de Perda (Safety First):**
   * Mede a frequência com que o retorno cai abaixo do alvo.
   * Matematicamente, equivale a $P(R < \tau)$.
   * *Interpretação:* Responde à pergunta "Qual a chance de eu perder dinheiro?". No entanto, falha em distinguir entre uma perda pequena e uma perda catastrófica (uma perda de 1% conta o mesmo que uma de 50%) (ROM; FERGUSON, 1994).
2. **LPM de Ordem 1 ($n=1$) – Déficit Esperado (*Target Shortfall*):**
   * Mede a magnitude média das perdas. Os desvios abaixo do alvo são ponderados linearmente.
   * *Interpretação:* Responde à pergunta "Se eu perder dinheiro, quanto espero perder em média?". É a medida de risco fundamental para o cálculo do Índice Omega (discutido na Seção 2.5) e reflete um investidor neutro ao risco em relação à severidade da perda, desde que a média seja controlada (BAWA, 1975; FISHBURN, 1977).
3. **LPM de Ordem 2 ($n=2$) – Semivariância (*Target Semivariance*):**
   * Mede a dispersão quadrática dos retornos abaixo do alvo. Semelhante à variância, mas unilateral.
   * *Interpretação:* Penaliza desproporcionalmente as grandes perdas. Uma perda duas vezes maior pesa quatro vezes mais no cálculo do risco. Esta é a medida preferida por Markowitz (1959) e a base para o **Desvio Padrão de Downside** ($Downside Deviation = \sqrt{LPM_2}$), que é o denominador do Índice de Sortino (MARKOWITZ, 1959).
4. **LPM de Ordens Superiores ($n > 2$):**
   * Refletem uma aversão extrema a perdas catastróficas. À medida que $n$ aumenta, o foco da métrica desloca-se quase exclusivamente para a cauda esquerda extrema da distribuição, ignorando pequenas flutuações negativas (SORTINO; VAN DER MEER, 1991).

### **2.3.3 Semivariância vs. Variância: O Impacto na Alocação**

A substituição da variância pela semivariância tem implicações profundas na construção de portfólios. Em distribuições simétricas (normais), a semivariância é proporcional à variância, e a fronteira eficiente da PMPT converge para a da MPT. No entanto, na presença de assimetria (skewness), as fronteiras divergem (ROM; FERGUSON, 1994).

Um ativo com alta assimetria positiva (como uma opção de compra longa ou uma startup de venture capital) terá uma variância alta (devido ao potencial de ganho ilimitado) mas uma semivariância baixa (perda limitada ao capital investido). A MPT penalizaria este ativo, reduzindo sua alocação para diminuir o risco total. A PMPT, utilizando a semivariância, reconheceria o perfil favorável de risco/retorno e aumentaria a alocação, capturando o "upside potential" (ROLLINGER; HOFFMAN, 2013). Estudos empíricos mostram que, em mercados emergentes ou durante crises, portfólios otimizados via semivariância tendem a preservar capital de forma mais eficiente do que aqueles baseados em média-variância (GIRARD; KODJOVI, 2010).

---

## **2.4 Métricas Avançadas de Risco e Propriedades de Coerência**

A evolução da gestão de riscos não parou nos LPMs. A necessidade de quantificar o capital regulatório bancário e o risco sistêmico levou ao desenvolvimento de métricas baseadas em quantis, como o *Value at Risk* (VaR) e o *Expected Shortfall* (ES/CVaR). A análise dessas métricas sob a perspectiva da teoria axiomática de riscos revela distinções cruciais sobre sua confiabilidade.

### **2.4.1 Value at Risk (VaR): A Revolução Incoerente**

Popularizado em 1994 pelo J.P. Morgan através do sistema *RiskMetrics*, o VaR tornou-se o padrão da indústria para a gestão de riscos de mercado e regulação bancária (Acordos de Basileia I e II) (MORGAN, 1996). O VaR é definido como a perda máxima esperada em um determinado horizonte de tempo, com um certo nível de confiança ($1-\alpha$).

Por exemplo, um VaR de 99% de $10 milhões em 1 dia implica que há apenas 1% de chance de a perda exceder $10 milhões.

Apesar de sua ubiquidade, o VaR apresenta falhas estruturais graves sob a ótica da PMPT e da teoria estatística:

1. **Cegueira da Cauda (*Tail Blindness*):** O VaR indica o limiar da perda, mas nada diz sobre a severidade da perda caso esse limiar seja ultrapassado. Em distribuições de cauda gorda, a perda média além do VaR pode ser muitas vezes superior ao próprio VaR, ocultando riscos catastróficos (NBER, 2009).
2. **Violação da Subaditividade:** Artzner et al. (1999), em seu artigo fundamental sobre medidas de risco coerentes, demonstraram que o VaR **não é subaditivo**. Isso significa que o VaR de um portfólio diversificado pode ser maior do que a soma dos VaRs dos ativos individuais ($\text{VaR}(A+B) > \text{VaR}(A) + \text{VaR}(B)$). Essa propriedade perversa desencoraja a diversificação e viola um dos princípios basilares da gestão de portfólio (ARTZNER et al., 1999). Exemplos teóricos e práticos mostram que, em distribuições muito assimétricas ou com caudas pesadas, a fusão de riscos pode parecer aumentar o risco medido pelo VaR, uma anomalia teórica inaceitável (ARTZNER et al., 1999).

### **2.4.2 Medidas de Risco Coerentes e os Axiomas de Artzner**

Para remediar as falhas do VaR, Artzner, Delbaen, Eber e Heath (1999) estabeleceram quatro axiomas que uma medida de risco $\rho$ deve satisfazer para ser considerada "coerente" e segura para alocação de capital (ARTZNER et al., 1999):

1. **Monotonicidade:** Se o portfólio $X$ tem retornos sempre melhores que $Y$, o risco de $X$ deve ser menor ($\text{Se } X \ge Y, \text{então } \rho(X) \le \rho(Y)$).
2. **Subaditividade:** O risco do todo não pode exceder a soma dos riscos das partes ($\rho(X+Y) \le \rho(X) + \rho(Y)$). Garante que a diversificação reduz o risco.
3. **Homogeneidade Positiva:** O risco escala linearmente com o tamanho da posição ($\rho(\lambda X) = \lambda \rho(X)$ para $\lambda > 0$).
4. **Invariância de Translação:** Adicionar um montante garantido de caixa $k$ reduz o risco nesse mesmo montante ($\rho(X + k) = \rho(X) - k$).

### **2.4.3 Conditional Value at Risk (CVaR) / Expected Shortfall (ES)**

Como resposta direta à incoerência do VaR, Rockafellar e Uryasev (2000, 2002) propuseram e operacionalizaram o *Conditional Value at Risk* (CVaR), também conhecido como *Expected Shortfall* (ES). O CVaR é definido como a média das perdas que ocorrem na cauda da distribuição, estritamente além do ponto de corte do VaR (ROCKAFELLAR; URYASEV, 2000):

$$CVaR_{\alpha}(X) = E\bigl[{-X} \mid {-X} \geq VaR_{\alpha}(X)\bigr]$$

**Superioridade do CVaR na PMPT:**

* **Coerência:** O CVaR satisfaz todos os axiomas de Artzner, incluindo a subaditividade. Ele reconhece corretamente os benefícios da diversificação mesmo em cenários de estresse extremo (ARTZNER et al., 1999).
* **Convexidade e Otimização:** Diferentemente do VaR, que é uma função não-convexa e difícil de otimizar (com múltiplos mínimos locais), o CVaR é convexo. Isso permitiu a Rockafellar e Uryasev desenvolver algoritmos de programação linear que podem otimizar portfólios com milhares de ativos e cenários de forma extremamente eficiente, minimizando diretamente o risco de cauda (ROCKAFELLAR; URYASEV, 2000).
* **Sensibilidade à Cauda:** O CVaR captura a forma da distribuição na região de perdas extremas. Se um ativo possui "cisnes negros" latentes, o CVaR será significativamente maior que o VaR, alertando o gestor sobre a verdadeira dimensão do risco (JARVIS, 2010).

A transição regulatória global, exemplificada pela *Fundamental Review of the Trading Book* (FRTB) do Comitê de Basileia, que substituiu o VaR pelo Expected Shortfall para o cálculo de capital de risco de mercado, constitui a validação institucional definitiva dos princípios defendidos pela PMPT: o risco real reside na cauda, e métricas incoerentes são inadequadas para a segurança sistêmica (ARTZNER et al., 1999).

---

## **2.5 Indicadores de Desempenho Ajustados: Sortino, Omega e a Generalização Kappa**

A PMPT não se limita a medir o risco; ela redefine a avaliação de desempenho. O onipresente Índice de Sharpe, ao penalizar a volatilidade de alta, falha em capturar o valor gerado por gestores que produzem assimetria positiva. A PMPT propõe alternativas que integram os conceitos de *downside risk* e momentos superiores.

### **2.5.1 O Índice de Sortino: Refinando Sharpe**

Desenvolvido por Frank Sortino no início dos anos 1980 e popularizado nos anos 1990, o Índice de Sortino é a modificação mais direta e amplamente adotada do Índice de Sharpe (SORTINO; VAN DER MEER, 1991). Ele substitui o desvio padrão total pelo **Desvio de Downside** ($TDD$ ou $\sigma_d$) no denominador.

$$\text{Sortino Ratio} = \frac{R_p - MAR}{TDD} = \frac{R_p - MAR}{\sqrt{LPM_2(MAR)}}$$

Onde:

* $R_p$ é o retorno médio do portfólio.
* $MAR$ (*Minimum Acceptable Return*) é o retorno alvo definido pelo investidor.
* $TDD$ (*Target Downside Deviation*) é a raiz quadrada da semivariância em relação ao MAR.

**Análise Comparativa:**
O Índice de Sortino e o Sharpe convergem quando a distribuição dos retornos é normal e o MAR é igual à média. Contudo, para estratégias com alta assimetria positiva (e.g., *trend following*, opções longas), o Sortino será consistentemente superior ao Sharpe, pois não penaliza os ganhos voláteis. Inversamente, para estratégias com assimetria negativa (e.g., venda de volatilidade), o Sortino revelará um desempenho ajustado ao risco inferior, expondo os riscos ocultos que o Sharpe mascara (ROLLINGER; HOFFMAN, 2013).

### **2.5.2 O Índice Omega: Capturando Todos os Momentos**

Introduzido por Keating e Shadwick em 2002, o Índice Omega ($\Omega$) representa um salto conceitual ao dispensar completamente a necessidade de estimar momentos estatísticos (média, variância) e operar diretamente sobre a distribuição de probabilidade cumulativa dos retornos (KEATING; SHADWICK, 2002).

O Omega é definido como a razão entre a probabilidade ponderada de ganhos e a probabilidade ponderada de perdas em relação a um limiar $L$:

$$\Omega(L) = \frac{\int_{L}^{\infty} [1 - F(r)] \, dr}{\int_{-\infty}^{L} F(r) \, dr}$$

**Vantagem Crítica:**
O Omega captura implicitamente todos os momentos da distribuição (média, variância, assimetria, curtose e momentos superiores) em uma única métrica. Ao variar o limiar $L$, o Omega fornece um perfil completo de risco-retorno, em vez de uma estimativa pontual. Isso o torna a ferramenta predileta para analisar ativos complexos e não lineares, como fundos de hedge e criptoativos, onde a suposição de normalidade é fatalmente falha (KEATING; SHADWICK, 2002).

Adicionalmente, existe uma relação direta entre o conceito de *Upside Potential Ratio* e o Omega. O numerador do Omega corresponde ao potencial de alta (*Upside Potential*), enquanto o denominador corresponde ao potencial de baixa (*Downside Potential*), alinhando a métrica com a intuição econômica de ganho *versus* dor (SORTINO; VAN DER MEER, 1991).

### **2.5.3 O Índice Kappa: A Generalização Unificadora**

Kaplan e Knowles (2004) propuseram o Índice Kappa ($K_n$) como uma medida generalizada que unifica o Sortino e o Omega sob uma única estrutura matemática baseada em LPMs (KAPLAN; KNOWLES, 2004).

$$K_n(\tau) = \frac{\mu - \tau}{\sqrt[n]{LPM_n(\tau)}}$$

A elegância do Kappa reside na sua capacidade de recuperar as outras métricas através do ajuste do parâmetro $n$:

* Quando $n=1$, o Kappa é funcionalmente equivalente ao **Índice Omega** (ranking idêntico).
* Quando $n=2$, o Kappa torna-se o **Índice de Sortino**.
* Para $n=3$ ou superior, o Kappa penaliza severamente a curtose e riscos extremos de cauda.

Essa generalização permite que gestores de portfólio calibrem a métrica de desempenho especificamente para a função de utilidade de seus clientes. Para um investidor avesso a perdas catastróficas, um $K_3$ ou $K_4$ seria mais apropriado; para um investidor focado na probabilidade geral de ganho, um $K_1$ (Omega) seria ideal (KAPLAN; KNOWLES, 2004).

---

## **2.6 Fronteiras Eficientes: A Geometria da Assimetria**

A aplicação das métricas de PMPT altera a geometria da fronteira eficiente. Enquanto a fronteira eficiente da MPT (média-variância) é sempre uma hipérbole suave e convexa, a fronteira eficiente da PMPT (retorno-LPM ou retorno-CVaR) pode assumir formas irregulares e não-suaves, especialmente quando composta por ativos com distribuições heterogêneas (mistura de ativos normais e não-normais) (CHOW; DENNING, 1994).

Em particular, a fronteira da PMPT tende a sugerir alocações mais concentradas em ativos com assimetria positiva e a evitar ativos com caudas esquerdas pesadas, mesmo que estes possuam alta média de retorno. Estudos recentes sobre criptoativos mostram que a otimização via PMPT resulta em portfólios com melhor proteção contra *drawdowns* severos do que a otimização via MPT, dado o perfil extremamente leptocúrtico desses ativos (BARNDORFF-NIELSEN et al., 2008).

## **2.7 Avanços Recentes e Integração com Machine Learning (2024-2025)**

A fronteira atual da pesquisa em PMPT reside na sua integração com a Inteligência Artificial. Publicações e estudos de 2024 e 2025 indicam uma tendência crescente no uso de algoritmos de **Machine Learning**, como redes neurais recorrentes (LSTM) e Deep Learning, para estimar dinamicamente os Momentos Parciais Inferiores e otimizar portfólios (YILMAZ et al., 2023).

Ao contrário dos modelos estáticos tradicionais que dependem de dados históricos passados, modelos híbridos (PMPT + ML) conseguem prever mudanças nos regimes de volatilidade e na forma das caudas (*tail risk forecasting*), ajustando as alocações em tempo real para minimizar o CVaR futuro. Essa abordagem, denominada "Otimização Robusta Dinâmica", supera as limitações da MPT e da PMPT clássica, oferecendo resultados superiores em *backtests* e aplicações reais, especialmente em mercados voláteis e durante transições de regime econômico (CARAPUÇO; NEVES; HORTA, 2024).

Além disso, a PMPT tem sido fundamental na integração de critérios ESG (Environmental, Social, and Governance) na gestão de portfólios. Estudos recentes sugerem que o uso de métricas de *downside risk* como o Índice de Sortino revela melhor o perfil de risco ajustado de empresas com altas pontuações ESG, que tendem a ter menor risco de cauda (menor risco reputacional e regulatório) do que empresas convencionais, algo que o Índice de Sharpe muitas vezes falha em capturar (TAGHIZADEH-HESARY et al., 2024).

## **2.8 Conclusão**

A Teoria Pós-Moderna do Portfólio representa a maturidade da gestão de investimentos quantitativa. Ao rejeitar a simplificação excessiva da normalidade e abraçar a complexidade assimétrica dos mercados e da psicologia humana, a PMPT oferece ferramentas — LPM, CVaR, Sortino, Omega — que são não apenas teoricamente superiores, mas pragmaticamente indispensáveis. Em um ambiente financeiro caracterizado por crises recorrentes e incerteza radical, a capacidade de distinguir entre o risco de ruína e a volatilidade de oportunidade é o que separa a sobrevivência da extinção. A PMPT é a linguagem matemática dessa distinção.

---

**Tabela 2.2: Resumo Analítico dos Indicadores de Desempenho (MPT vs. PMPT)**

| Indicador | Base Teórica | Fórmula Conceitual | Sensibilidade à Cauda | Principal Aplicação |
| :---- | :---- | :---- | :---- | :---- |
| **Sharpe** | MPT (Variância) | $\frac{Retorno - R_f}{\sigma_{total}}$ | Baixa (Assume Normalidade) | Ativos tradicionais, Benchmark relativo |
| **Sortino** | PMPT (LPM 2) | $\frac{Retorno - MAR}{\sigma_{downside}}$ | Média (Foca no Downside) | Fundos Assimétricos, Hedge Funds |
| **Omega** | PMPT (Todos Momentos) | $\frac{\text{Prob. Ponderada Ganhos}}{\text{Prob. Ponderada Perdas}}$ | Alta (Captura toda distribuição) | Derivativos, Cripto, Private Equity |
| **Kappa ($K_3$)** | PMPT (LPM 3) | $\frac{Retorno - MAR}{\sqrt[3]{LPM_3}}$ | Muito Alta (Penaliza extremos) | Gestão de Risco de Cauda, Seguros |

Fonte: Elaboração do autor baseada em KAPLAN; KNOWLES (2004).

---

## **Referências**

> **Nota metodológica:** As referências abaixo seguem a ABNT NBR 6023:2018. As citações no texto seguem o sistema autor-data (ABNT NBR 10520:2023). Referências de acesso exclusivamente eletrônico têm a data de acesso indicada como novembro de 2025.

---

ARTZNER, Philippe; DELBAEN, Freddy; EBER, Jean-Marc; HEATH, David. Coherent measures of risk. **Mathematical Finance**, Hoboken, v. 9, n. 3, p. 203-228, jul. 1999.

ATHAYDE, Gustavo; FLORES, Renato. Portfolio optimisation with higher moments of risk at the Pakistan Stock Exchange. **Economic Research — Ekonomska Istraživanja**, Zagreb, v. 30, n. 1, p. 1401-1415, 2017. Disponível em: https://www.tandfonline.com/doi/full/10.1080/1331677X.2017.1340182. Acesso em: nov. 2025.

BARNDORFF-NIELSEN, Ole E. et al. Measuring downside risk: realised semivariance. Durham: Duke University, 2008. Disponível em: https://public.econ.duke.edu/~get/browse/courses/201/spr08/DOWNLOADS/New_Methods_and_JumpTests/BNKS-semivariance-2008.pdf. Acesso em: nov. 2025.

BAWA, Vijay S. Optimal rules for ordering uncertain prospects. **Journal of Financial Economics**, Amsterdam, v. 2, n. 1, p. 95-121, mar. 1975.

BUCKLE, David J. Portfolio skew and kurtosis. **Risk**, Londres, jun. 2006. Disponível em: https://www.risk.net/sites/default/files/import_unmanaged/risk.net/data/risk/pdf/technical/risk_0605_technical_buckle.pdf. Acesso em: nov. 2025.

CARAPUÇO, João; NEVES, Rui; HORTA, Nuno. Advancing investment frontiers: industry-grade deep reinforcement learning for portfolio optimization. **arXiv**, 2024. Disponível em: https://arxiv.org/html/2403.07916v1. Acesso em: nov. 2025.

CHOW, George; DENNING, Karen C. A practitioner's guide to address fat tails and downside risk in portfolio construction. **Journal of Investment Management**, Irvine, 1994. Disponível em: https://www.joim.com/wp-content/uploads/emember/downloads/p0725.pdf. Acesso em: nov. 2025.

FAMA, Eugene F. The behavior of stock-market prices. **The Journal of Business**, Chicago, v. 38, n. 1, p. 34-105, jan. 1965.

FISHBURN, Peter C. Mean-risk analysis with risk associated with below-target returns. **The American Economic Review**, Nashville, v. 67, n. 2, p. 116-126, mar. 1977.

GIRARD, Emre; KODJOVI, Messan. The introduction of emerging currencies into a portfolio: towards a more complete diversification model. **Économie internationale**, Paris, n. 121, p. 5-38, 2010. Disponível em: https://shs.cairn.info/revue-economie-internationale-2010-1-page-5?lang=en. Acesso em: nov. 2025.

JARVIS, Stuart. Dynamic asset allocation techniques. In: INTERNATIONAL CONGRESS OF ACTUARIES, 2010, Cape Town. **Anais…** Cap Town: International Actuarial Association, 2010. Disponível em: https://actuaries.org/app/uploads/2025/07/ICA2010_AFIR_32_final-paper_Jarvis.pdf. Acesso em: nov. 2025.

KAHNEMAN, Daniel; TVERSKY, Amos. Prospect theory: an analysis of decision under risk. **Econometrica**, Hoboken, v. 47, n. 2, p. 263-292, mar. 1979.

KAPLAN, Paul D.; KNOWLES, James A. Kappa: a generalized downside risk-adjusted performance measure. **Journal of Performance Measurement**, New York, v. 8, n. 3, p. 42-54, primavera 2004. Disponível em: http://w.performance-measurement.org/KaplanKnowles2004.pdf. Acesso em: nov. 2025.

KEATING, Con; SHADWICK, William F. A universal performance measure. **Journal of Performance Measurement**, New York, v. 6, n. 3, p. 59-84, primavera 2002. Disponível em: https://www.researchgate.net/publication/228550687_A_Universal_Performance_Measure. Acesso em: nov. 2025.

MANDELBROT, Benoit. The variation of certain speculative prices. **The Journal of Business**, Chicago, v. 36, n. 4, p. 394-419, out. 1963.

MARKOWITZ, Harry M. Portfolio selection. **The Journal of Finance**, Hoboken, v. 7, n. 1, p. 77-91, mar. 1952.

MARKOWITZ, Harry M. **Portfolio selection: efficient diversification of investments**. New York: John Wiley & Sons, 1959.

MORGAN, J. P. **RiskMetrics: technical document**. 4. ed. New York: J.P. Morgan & Co., 1996. Disponível em: https://www.value-at-risk.net/riskmetrics/. Acesso em: nov. 2025.

NATIONAL BUREAU OF ECONOMIC RESEARCH (NBER). **Optimal portfolio choice with fat tails**. Cambridge: NBER, 2009. Disponível em: https://www.nber.org/sites/default/files/2023-06/orrc09-16-VD.pdf. Acesso em: nov. 2025.

ROCKAFELLAR, R. Tyrrell; URYASEV, Stanislav. Optimization of conditional value-at-risk. **Journal of Risk**, Londres, v. 2, n. 3, p. 21-41, 2000. Disponível em: https://sites.math.washington.edu/~rtr/papers/rtr179-CVaR1.pdf. Acesso em: nov. 2025.

ROCKAFELLAR, R. Tyrrell; URYASEV, Stanislav. Conditional value-at-risk for general loss distributions. **Journal of Banking & Finance**, Amsterdam, v. 26, n. 7, p. 1443-1471, 2002. Disponível em: https://sites.math.washington.edu/~rtr/papers/rtr187-CVaR2.pdf. Acesso em: nov. 2025.

ROLLINGER, Thomas N.; HOFFMAN, Scott T. Sortino: a 'sharper' ratio. Chicago: CME Group / Red Rock Capital, 2013. Disponível em: https://www.cmegroup.com/education/files/rr-sortino-a-sharper-ratio.pdf. Acesso em: nov. 2025.

ROM, Brian M.; FERGUSON, Kathleen W. Post-modern portfolio theory comes of age. **The Journal of Investing**, New York, v. 3, n. 3, p. 11-17, outono 1994.

SORTINO, Frank A.; VAN DER MEER, Robert. Downside risk. **The Journal of Portfolio Management**, New York, v. 17, n. 4, p. 27-31, verão 1991.

TAGHIZADEH-HESARY, Farhad et al. Effectiveness of the ESG approach in portfolio selection: an empirical evidence from the US stock market. **Journal of Business Economics and Management**, Vilnius, v. 24, n. 1, p. 1-18, 2024. Disponível em: https://journals.vilniustech.lt/index.php/JBEM/article/view/24751/13067. Acesso em: nov. 2025.

YILMAZ, Tuncay et al. Investment portfolio optimization: integrating portfolio allocation methods with RNN LSTM. In: IEEE INTERNATIONAL CONFERENCE ON DATA MINING, 2023. **Proceedings…** IEEE, 2023. Disponível em: https://ieeexplore.ieee.org/document/10317711/. Acesso em: nov. 2025.

---

## **Mapeamento de Correspondência: Referência Original → ABNT**

> Esta seção é auxiliar e deve ser removida do texto final. Destina-se a orientar a substituição de citações no arquivo `.docx`.

| Ref. original (nº) | Citação ABNT no texto | Referência ABNT completa |
|:---:|:---|:---|
| 2 | (MARKOWITZ, 1952) | MARKOWITZ, 1952 |
| 4 | (ROM; FERGUSON, 1994) | ROM; FERGUSON, 1994 |
| 5 | (SORTINO; VAN DER MEER, 1991) | SORTINO; VAN DER MEER, 1991 |
| 6 | (ROM; FERGUSON, 1994) | ROM; FERGUSON, 1994 |
| 8 | (MANDELBROT, 1963; FAMA, 1965) | MANDELBROT, 1963; FAMA, 1965 |
| 9 | (BARNDORFF-NIELSEN et al., 2008) | BARNDORFF-NIELSEN et al., 2008 |
| 10 | (MARKOWITZ, 1959) | MARKOWITZ, 1959 |
| 11 | (MARKOWITZ, 1959) | MARKOWITZ, 1959 |
| 12 | (ROLLINGER; HOFFMAN, 2013) | ROLLINGER; HOFFMAN, 2013 |
| 13 | (ROLLINGER; HOFFMAN, 2013) | ROLLINGER; HOFFMAN, 2013 |
| 14 | (FISHBURN, 1977) | FISHBURN, 1977 |
| 15 | (ROM; FERGUSON, 1994) | ROM; FERGUSON, 1994 |
| 16 | (SORTINO; VAN DER MEER, 1991) | SORTINO; VAN DER MEER, 1991 |
| 17 | (ROM; FERGUSON, 1994) | ROM; FERGUSON, 1994 |
| 20 | (NBER, 2009) | NATIONAL BUREAU OF ECONOMIC RESEARCH, 2009 |
| 21 | (BUCKLE, 2006) | BUCKLE, 2006 |
| 23 | (ATHAYDE; FLORES, 2017) | ATHAYDE; FLORES, 2017 |
| 26 | (ARTZNER et al., 1999) | ARTZNER et al., 1999 |
| 27 | (KAHNEMAN; TVERSKY, 1979) | KAHNEMAN; TVERSKY, 1979 |
| 28 | (KAHNEMAN; TVERSKY, 1979) | KAHNEMAN; TVERSKY, 1979 |
| 31 | (BAWA, 1975) | BAWA, 1975 |
| 33 | (BAWA, 1975; FISHBURN, 1977) | BAWA, 1975; FISHBURN, 1977 |
| 41 | (SORTINO; VAN DER MEER, 1991) | SORTINO; VAN DER MEER, 1991 |
| 42 | (ROM; FERGUSON, 1994) | ROM; FERGUSON, 1994 |
| 43 | (CHOW; DENNING, 1994) | CHOW; DENNING, 1994 |
| 45 | (GIRARD; KODJOVI, 2010) | GIRARD; KODJOVI, 2010 |
| 47 | (MORGAN, 1996) | MORGAN, 1996 |
| 50 | (ARTZNER et al., 1999) | ARTZNER et al., 1999 |
| 53 | (ARTZNER et al., 1999) | ARTZNER et al., 1999 |
| 56 | (ROCKAFELLAR; URYASEV, 2000) | ROCKAFELLAR; URYASEV, 2000 |
| 58 | (ROCKAFELLAR; URYASEV, 2000) | ROCKAFELLAR; URYASEV, 2000 |
| 61 | (JARVIS, 2010) | JARVIS, 2010 |
| 64 | (KEATING; SHADWICK, 2002) | KEATING; SHADWICK, 2002 |
| 68 | (SORTINO; VAN DER MEER, 1991) | SORTINO; VAN DER MEER, 1991 |
| 70 | (KAPLAN; KNOWLES, 2004) | KAPLAN; KNOWLES, 2004 |
| 71 | (KAPLAN; KNOWLES, 2004) | KAPLAN; KNOWLES, 2004 |
| 73 | (KAPLAN; KNOWLES, 2004) | KAPLAN; KNOWLES, 2004 |
| 78 | (YILMAZ et al., 2023) | YILMAZ et al., 2023 |
| 80 | (CARAPUÇO; NEVES; HORTA, 2024) | CARAPUÇO; NEVES; HORTA, 2024 |
| 82 | (TAGHIZADEH-HESARY et al., 2024) | TAGHIZADEH-HESARY et al., 2024 |
