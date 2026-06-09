# Síntese Evolutiva da Gestão Quantitativa de Portfólio: Da Fronteira Média-Variância aos Frameworks Black-Litterman Aprimorados por Deep Learning


## 1. Introdução: A Trajetória Epistemológica da Alocação de Ativos

A história da teoria moderna de gestão de carteiras não é apenas uma sucessão de fórmulas matemáticas, mas uma evolução contínua na compreensão humana sobre a natureza do risco e a incerteza dos mercados financeiros. Este relatório apresenta uma análise exaustiva e crítica desse arco evolutivo, iniciando-se nos fundamentos estabelecidos por Harry Markowitz com a Teoria Moderna de Portfólio (MPT), atravessando as críticas que deram origem à Teoria Pós-Moderna de Portfólio (PMPT) e ao modelo de Desvio Absoluto Médio (MAD), e culminando na integração bayesiana de visões subjetivas através do modelo Black-Litterman. O ápice desta análise reside na fronteira contemporânea, onde a econometria clássica (ARIMA, GARCH) e as arquiteturas de *Deep Learning* (Redes Neurais LSTM) convergem para gerar os *inputs* necessários para a otimização de portfólios, criando uma síntese entre o raciocínio econômico humano e o reconhecimento de padrões computacional.
A premissa central que guia esta investigação é a busca incessante pela robustez matemática. A dependência inicial da variância como *proxy* única para o risco foi desafiada pela distribuição não normal (não gaussiana) dos retornos dos ativos, fenômeno conhecido como leptocurtose ou "caudas gordas". Isso exigiu o desenvolvimento de medidas de risco de *downside* (PMPT) e abordagens de programação linear robusta (MAD). Simultaneamente, a sensibilidade extrema da otimização Média-Variância a pequenos erros nos *inputs* necessitou de uma abordagem bayesiana (Black-Litterman) para estabilizar os pesos dos ativos. Finalmente, as "visões" exigidas pelo modelo Black-Litterman — originalmente opiniões subjetivas de analistas — estão agora sendo rigorosamente derivadas de modelos de previsão de séries temporais, fechando o ciclo de um sistema quantitativo autônomo.
A relevância deste estudo é amplificada pelo contexto atual de alta volatilidade e complexidade dos mercados, onde modelos tradicionais frequentemente falham em proteger o capital do investidor. Ao examinar a literatura acadêmica e empírica, observa-se que a combinação de técnicas de aprendizado de máquina com estruturas de alocação teóricas robustas oferece um desempenho superior ajustado ao risco, medido não apenas pelo Índice de Sharpe, mas por métricas mais resilientes como o MAD e o Índice Sortino.1

## 2. Teoria Moderna de Portfólio (MPT): Fundamentos e Limitações Estruturais


### 2.1 O Framework Média-Variância de Markowitz

A Teoria Moderna de Portfólio (MPT), introduzida por Harry Markowitz em 1952, revolucionou as finanças ao quantificar os benefícios da diversificação. Antes de Markowitz, a gestão de investimentos focava na seleção de ações individuais baseada em seus méritos isolados. A MPT introduziu a noção de que o risco e o retorno de um investimento não devem ser vistos isoladamente, mas sim avaliados por como o investimento afeta o risco e o retorno geral do portfólio.4
A premissa fundamental é que um investidor age racionalmente para maximizar o retorno esperado para um determinado nível de risco, ou minimizar o risco para um determinado nível de retorno esperado. A inovação crítica de Markowitz foi a definição matemática de risco como a variância ($\sigma^2$) ou desvio padrão ($\sigma$) dos retornos do portfólio.
A formulação matemática do problema de otimização da MPT é um problema de programação quadrática (QP), que busca minimizar a variância do portfólio:
$$\text{Minimizar } \sigma_p^2 = \sum_{i=1}^{n} \sum_{j=1}^{n} w_i w_j \sigma_{ij}$$
Sujeito às restrições lineares:
**Retorno Alvo:** $\sum_{i=1}^{n} w_i E = R_{target}$
**Orçamento Total:** $\sum_{i=1}^{n} w_i = 1$
**Restrição de Não-Negatividade (Opcional):** $w_i \geq 0$ (para portfólios *long-only*)
Onde $w_i$ representa o peso do ativo $i$, $\sigma_{ij}$ é a covariância entre os ativos $i$ e $j$, e $E$ é o retorno esperado. A covariância é o elemento que captura a interação entre os ativos; se a correlação entre dois ativos é inferior a 1, a variância do portfólio será menor que a média ponderada das variâncias individuais, concretizando o benefício da diversificação.5

### 2.2 Limitações Críticas e a Necessidade de Evolução

Apesar de seu status de Prêmio Nobel, a MPT enfrenta severas limitações práticas e teóricas que impulsionaram a evolução subsequente da teoria das carteiras. A literatura aponta consistentemente que a MPT reduz as complexidades do universo de investimentos a apenas duas dimensões (risco e retorno), o que, embora elegante, é frequentemente insuficiente para modelar a realidade dos mercados.3

#### 2.2.1 A Falácia da Distribuição Normal

A limitação mais citada é a suposição de que os retornos dos ativos seguem uma distribuição normal multivariada. A evidência empírica demonstra de forma esmagadora que os retornos financeiros exibem assimetria (*skewness*) e excesso de curtose (*fat tails*). Isso significa que eventos extremos — tanto positivos quanto negativos — ocorrem com muito mais frequência do que uma distribuição gaussiana preveria.3
Além disso, a MPT penaliza a volatilidade de alta (ganhos acima da média) da mesma forma que a volatilidade de baixa (perdas). Para um investidor racional, a volatilidade "positiva" é benéfica. Ao tratar todo desvio da média como "risco", a MPT pode levar à rejeição de ativos que têm alta probabilidade de grandes ganhos, apenas porque essa possibilidade aumenta a variância total.6 Esta discrepância entre a definição matemática de risco (variância) e a percepção psicológica de risco (perda de capital) é o cerne da crítica que levou à PMPT.

#### 2.2.2 Sensibilidade aos Inputs e Maximização de Erro

O modelo Média-Variância é notoriamente sensível aos seus *inputs*: o vetor de retornos esperados e a matriz de covariância. Pequenas alterações nas estimativas de retorno esperado podem levar a mudanças drásticas nos pesos dos ativos, resultando frequentemente em "soluções de canto" (*corner solutions*), onde o portfólio se concentra excessivamente em poucos ativos e zera a posição em muitos outros.7
Este fenômeno é frequentemente descrito como "maximização de erro de estimativa". O otimizador matemático não consegue distinguir entre uma oportunidade de investimento real e um erro de estimativa nos dados. Se um ativo tem um retorno histórico ligeiramente superestimado devido ao ruído estatístico, a MPT alocará agressivamente capital nesse ativo, amplificando o erro.9 Michaud (1989) descreveu famosamente a otimização Média-Variância como um "amplificador de erros de estimativa".

#### 2.2.3 Incerteza dos Parâmetros e Estacionariedade

A MPT assume que os parâmetros históricos (média e covariância) são os verdadeiros parâmetros da distribuição futura. No entanto, os mercados financeiros são "sistemas abertos" e não estacionários, onde o passado não é necessariamente representativo do futuro.6 A estimativa ruidosa dos retornos esperados usando médias amostrais é reconhecida como uma das principais causas do fraco desempenho fora da amostra dos portfólios MPT.10
Estas deficiências necessitaram o desenvolvimento de medidas de risco mais robustas (levando à PMPT e ao MAD) e técnicas de otimização que pudessem lidar com a incerteza dos parâmetros (levando ao modelo Black-Litterman).

## 3. Mensuração Robusta de Risco: PMPT e o Modelo de Desvio Absoluto Médio (MAD)

A evolução teórica bifurcou-se para resolver os problemas da MPT: uma vertente focou em redefinir o risco para se alinhar melhor à utilidade do investidor (PMPT), enquanto a outra focou em simplificar e robustecer a computação (MAD).

### 3.1 Teoria Pós-Moderna de Portfólio (PMPT): O Foco no Downside

A Teoria Pós-Moderna de Portfólio (PMPT) surgiu em resposta direta à simetria indesejada da variância. Criada por Rom e Ferguson em 1991, a PMPT argumenta que o risco deve ser definido exclusivamente como **risco de downside** — a probabilidade e magnitude dos retornos caírem abaixo de um retorno alvo ou Mínimo Aceitável (MAR - *Minimum Acceptable Return*).6

#### 3.1.1 Momentos Parciais Inferiores (LPM - Lower Partial Moments)

A ferramenta matemática central da PMPT é o Momento Parcial Inferior (LPM) de ordem $n$. Diferente da variância, que integra sobre toda a distribuição, o LPM integra apenas a cauda esquerda da distribuição, abaixo do alvo $\tau$.
A fórmula geral contínua para o LPM de grau $n$ é dada por:
$$LPM_n(\tau) = \int_{-\infty}^{\tau} (\tau - R)^n f(R) dR$$
Onde $f(R)$ é a função de densidade de probabilidade dos retornos.11 Na prática, para dados discretos (séries temporais de retornos), o estimador empírico é:
$$LPM_n(\tau) = \frac{1}{T} \sum_{t=1}^{T} \max(0, \tau - R_t)^n$$
A escolha do grau $n$ reflete a aversão ao risco do investidor 12:
**Grau 0 ($n=0$):** Representa a probabilidade de perda (frequência de retornos abaixo de $\tau$). Não considera a magnitude da perda.
**Grau 1 ($n=1$):** Representa o déficit esperado (*Expected Shortfall*). Mede a magnitude média das perdas.
**Grau 2 ($n=2$):** Representa a semi-variância ou desvio de downside. É a medida mais comum na PMPT, comparável à variância na MPT, mas focada apenas em perdas.

#### 3.1.2 O Índice Sortino e a Evolução das Métricas de Desempenho

Como consequência direta da adoção da PMPT, o Índice Sharpe foi substituído pelo Índice Sortino. Enquanto o Índice Sharpe divide o excesso de retorno pelo desvio padrão total (penalizando a volatilidade positiva), o Índice Sortino divide o excesso de retorno pelo **Desvio de Downside** ($\sigma_d$), que é a raiz quadrada do LPM de grau 2.14
$$\text{Índice Sortino} = \frac{E - \tau}{\sqrt{LPM_2(\tau)}}$$
O Índice Sortino é superior para avaliar portfólios com distribuições não normais ou com estratégias que geram assimetria positiva (como opções ou *hedge funds*). Um Índice Sortino alto indica que o portfólio gera retornos elevados com baixo risco de perdas significativas, o que é a verdadeira meta da maioria dos investidores.16

### 3.2 Modelo de Desvio Absoluto Médio (MAD)

Paralelamente à PMPT, Konno e Yamazaki (1991) propuseram o modelo de Desvio Absoluto Médio (MAD) para abordar a complexidade computacional e as suposições de normalidade da MPT.3

#### 3.2.1 Formulação Matemática e Linearização

O modelo MAD substitui a variância (norma L2) pelo Desvio Absoluto Médio (norma L1) como medida de risco. O risco do portfólio é definido como a média dos desvios absolutos dos retornos do portfólio em relação ao retorno esperado:
$$W(x) = E \left \right| \right]$$
A grande vantagem desta formulação é que ela pode ser transformada em um problema de **Programação Linear (PL)**, que é computacionalmente muito mais eficiente e estável do que a Programação Quadrática exigida pela MPT, especialmente para portfólios com milhares de ativos.3
A formulação linear equivalente minimiza:

$$\text{Minimizar } \frac{1}{T} \sum_{t=1}^{T} y_t$$
Sujeito a:

$$y_t + \sum_{j=1}^{n} (r_{jt} - r_j) x_j \geq 0, \quad t = 1, \dots, T$$
$$y_t - \sum_{j=1}^{n} (r_{jt} - r_j) x_j \geq 0, \quad t = 1, \dots, T$$
$$\sum_{j=1}^{n} r_j x_j \geq \rho$$
$$\sum_{j=1}^{n} x_j = 1$$
$$x_j \geq 0$$
Onde $y_t$ são variáveis auxiliares que representam o desvio absoluto no período $t$, $r_{jt}$ é o retorno do ativo $j$ no tempo $t$, e $r_j$ é o retorno médio do ativo $j$.19

#### 3.2.2 Vantagens e Extensões do MAD (Entropia e CVaR)

**Independência da Normalidade:** O modelo MAD não requer que os retornos sejam normalmente distribuídos, tornando-o mais robusto em mercados reais com caudas gordas.3
**Eficiência Computacional:** Elimina a necessidade de calcular e armazenar a matriz de covariância, que cresce quadraticamente com o número de ativos. Para um universo de 1.000 ações, a MPT requer o cálculo de 500.000 covariâncias, enquanto o MAD trabalha diretamente com os dados históricos.3
**Desempenho Empírico:** Estudos de backtesting (e.g., no S&P 500) mostram que portfólios MAD frequentemente superam portfólios Média-Variância, produzindo maiores Índices de Sharpe e retornos totais.3
Uma extensão moderna significativa é o modelo **MAD-Entropia**. Pesquisas recentes sugerem incorporar a maximização da entropia (medida de diversidade de Shannon) à função objetivo do MAD. Enquanto o MAD minimiza o risco, a entropia força uma maior diversificação dos pesos, evitando as soluções de canto que afligem a otimização pura. Estudos indicam que o modelo MAD-Entropia supera tanto o MAD tradicional quanto a diversificação ingênua (1/N) em termos de retorno ajustado ao risco.19
Outra hibridização poderosa é o modelo **Beta-CVaR**, que combina o MAD com o *Conditional Value at Risk* (CVaR). Esta abordagem multiobjetivo permite ao investidor ponderar entre minimizar o desvio médio (risco "normal") e minimizar o risco de cauda extrema (CVaR), oferecendo uma proteção superior em períodos de crise financeira.21

## 4. A Resolução Bayesiana: O Modelo Black-Litterman

Enquanto a PMPT e o MAD melhoraram a mensuração do risco, o problema da sensibilidade aos *inputs* de retorno esperado persistia. O modelo Black-Litterman (BL), desenvolvido por Fischer Black e Robert Litterman no Goldman Sachs em 1990, aborda diretamente este problema utilizando uma abordagem bayesiana.4

### 4.1 A Filosofia do Equilíbrio e Visões

A intuição central do BL é que a otimização não deve começar do zero (o que leva a pesos extremos baseados em dados históricos ruidosos), mas sim de um ponto de partida estável e teoricamente sólido: o portfólio de equilíbrio de mercado. O investidor então "inclina" (*tilts*) o portfólio para longe desse equilíbrio apenas quando possui uma visão subjetiva forte e confiável.8
O modelo combina duas fontes de informação:
**A Distribuição a Priori (Equilíbrio):** O retorno que o mercado espera, implícito nos preços atuais e na capitalização de mercado.
**A Distribuição de Verossimilhança (Visões):** As opiniões do investidor sobre o desempenho absoluto ou relativo de certos ativos, com um grau associado de incerteza.

### 4.2 O Arcabouço Matemático Detalhado


#### 4.2.1 O Prior: Retornos Implícitos de Equilíbrio (**$\Pi$**)

Diferente da MPT, que exige que o investidor forneça os retornos esperados, o BL calcula o que o mercado "pensa". Usando a "Otimização Reversa", inverte-se a fórmula da MPT para encontrar o vetor de retornos implícitos ($\Pi$) dado o vetor de pesos de capitalização de mercado ($w_{mkt}$) e a matriz de covariância histórica ($\Sigma$):
$$\Pi = \delta \Sigma w_{mkt}$$
Aqui, $\delta$ é o coeficiente de aversão ao risco do mercado, geralmente calculado como $(E - R_f) / \sigma_m^2$.9 Este vetor $\Pi$ atua como uma âncora gravitacional, estabilizando o modelo.

#### 4.2.2 As Visões e a Incerteza (**$P, Q, \Omega$**)

O investidor expressa $k$ visões sobre $n$ ativos. Estas são formalizadas em:
**$Q$ (Vetor $k \times 1$):** Os retornos esperados das visões (ex: "Ativo A retornará 5%").
**$P$ (Matriz $k \times n$):** A matriz de seleção que mapeia as visões aos ativos. Para uma visão relativa ("A superará B em 2%"), a linha correspondente teria +1 na coluna de A e -1 na de B.
**$\Omega$ (Matriz $k \times k$):** A matriz de covariância dos termos de erro das visões. Ela é diagonal, implicando que os erros das visões são independentes. O elemento $\omega_{ii}$ representa a incerteza (variância) da visão $i$.9
A calibração de $\Omega$ é o aspecto mais desafiador e subjetivo do modelo tradicional.

#### 4.2.3 A Fórmula Mestra e a Estimativa Posteriori

O modelo BL combina o *Prior* ($\Pi$) e as Visões ($Q$) para gerar um novo vetor de retornos esperados ($E$), que é uma média ponderada pela precisão (inverso da variância) de ambas as fontes:
$$E =^{-1}$$
Onde $\tau$ é um escalar que representa a incerteza sobre a estimativa do prior (frequentemente definido entre 0.025 e 1, dependendo da literatura).9 O resultado é um vetor de retornos posteriores que gera portfólios intuitivos, diversificados e menos sensíveis a ruídos do que a MPT pura.

### 4.3 A Evolução da Incerteza: O Método de Idzorek

Uma das maiores dificuldades práticas do BL original era definir matematicamente a matriz $\Omega$. Idzorek (2005) propôs um método intuitivo onde o usuário especifica um **nível de confiança percentual** ($0\%$ a $100\%$) para cada visão. O algoritmo então "engenheira reversamente" a variância necessária em $\Omega$ para que o peso final do ativo no portfólio reflita exatamente esse nível de confiança.27
O método de Idzorek transformou o BL de uma curiosidade teórica em uma ferramenta prática, permitindo que gestores calibrassem a influência de suas visões sem precisar estimar variâncias abstratas. Contudo, na era do *Big Data*, a subjetividade humana (mesmo calibrada) está sendo substituída por previsões algorítmicas.

## 5. Geração Econométrica de Visões: ARIMA e GARCH

Para remover a subjetividade e automatizar o processo BL, vetores $Q$ e matrizes $\Omega$ são hoje derivados de modelos econométricos de séries temporais. Isso cria um sistema "quase-objetivo".

### 5.1 ARIMA: Previsão do Primeiro Momento (**$Q$**)

O modelo *AutoRegressive Integrated Moving Average* (ARIMA) é utilizado para prever o nível (média condicional) dos retornos futuros. Um modelo ARIMA($p,d,q$) captura dependências lineares na série temporal:
**AR ($p$):** Regressão sobre valores passados.
**I ($d$):** Diferenciação para tornar a série estacionária (requisito crucial, verificado pelo teste Dickey-Fuller Aumentado - ADF).30
**MA ($q$):** Regressão sobre erros de previsão passados.
No contexto do BL, a previsão de um passo à frente ($t+1$) do modelo ARIMA para cada ativo torna-se diretamente o valor no vetor $Q$. Se o ARIMA prevê que a ação da Apple subirá 1,5%, então $Q_{AAPL} = 0.015$.1

### 5.2 GARCH: Dinâmica da Volatilidade e a Matriz **$\Omega$**

Enquanto o ARIMA prevê o retorno, modelos GARCH (*Generalized Autoregressive Conditional Heteroskedasticity*) modelam a variância condicional, capturando o fenômeno de "agrupamento de volatilidade" (*volatility clustering*) típico de mercados financeiros.
O modelo GARCH(1,1) padrão define a variância atual ($\sigma_t^2$) como função da variância passada e dos resíduos quadrados passados:

$$\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2$$
Aplicação Crítica no BL: A variância condicional prevista pelo GARCH ($\sigma_{t+1}^2$) é utilizada para popular a diagonal da matriz de incerteza $\Omega$.33
Se o modelo GARCH indica que o mercado está entrando em um regime de alta volatilidade, os valores em $\Omega$ aumentam. Matematicamente, isso reduz o peso que a Fórmula Mestra do BL atribui à previsão do ARIMA ($Q$). O sistema torna-se autoadaptativo: em tempos voláteis, o modelo "confia menos" nas suas próprias previsões de retorno e "cola" mais no portfólio de equilíbrio de mercado, protegendo o capital.36

## 6. A Fronteira Algorítmica: Redes Neurais e LSTM

A limitação fundamental dos modelos ARIMA é sua linearidade. Os mercados financeiros são sistemas complexos, não lineares e caóticos. Para capturar padrões ocultos que escapam à econometria clássica, a literatura avançou para o uso de Redes Neurais Recorrentes (RNNs), especificamente as *Long Short-Term Memory* (LSTM).

### 6.1 Arquitetura LSTM: Memória e Não-Linearidade

As redes LSTM foram projetadas para resolver o problema do "desvanecimento do gradiente" (*vanishing gradient*) que impedia RNNs tradicionais de aprender dependências de longo prazo. Uma célula LSTM possui uma estrutura interna sofisticada com três "portões" (*gates*) que regulam o fluxo de informação 37:
Portão de Esquecimento (Forget Gate): Decide qual informação do estado anterior da célula deve ser descartada ($f_t$).

$$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$
**Portão de Entrada (*****Input Gate*****):** Decide qual nova informação deve ser armazenada na célula ($i_t$).
**Portão de Saída (*****Output Gate*****):** Decide o que será enviado para a próxima camada/passo de tempo ($o_t$).
Essa arquitetura permite que o modelo "lembre" tendências de longo prazo enquanto reage a choques de curto prazo, capturando a dinâmica não linear dos preços.

### 6.2 Superioridade Empírica e Aplicação no BL

A literatura comparativa é contundente: LSTMs superam consistentemente modelos ARIMA e GARCH na previsão de séries financeiras, especialmente em ativos voláteis e índices de mercados emergentes. Estudos relatam reduções de erro (RMSE/MSE) da ordem de 84% a 87% ao substituir ARIMA por LSTM.39
Além do LSTM, pesquisas recentes exploram modelos híbridos como SSA-MAEMD-TCN (Decomposição Modal Empírica e Redes Convolucionais Temporais), que buscam reduzir ainda mais o ruído e capturar dependências de longuíssimo prazo melhor que o LSTM.7
**Integração no BL:**
**Vetor $Q$:** As previsões de retorno do LSTM substituem as do ARIMA.
**Matriz $\Omega$:** A calibração da incerteza torna-se mais sofisticada. Em vez de usar apenas a variância do GARCH, pode-se usar o erro quadrático médio (MSE) ou o desvio absoluto médio (MAD) dos resíduos do próprio LSTM no conjunto de validação como uma medida direta de confiança. Se o LSTM tem performado mal recentemente, a incerteza em $\Omega$ aumenta, reduzindo a aposta na visão.2

### 6.3 Comparativo Direto: ARIMA vs. LSTM


| Característica | ARIMA | LSTM |
| --- | --- | --- |
| Tipo de Modelo | Estatístico Linear | Deep Learning Não-Linear |
| Suposição de Dados | Estacionariedade Obrigatória (requer diferenciação) | Lida com Não-Estacionariedade e Ruído |
| Dependência | Curto Prazo (Lags fixos) | Longo Prazo (Memória sequencial) |
| Volume de Dados | Eficiente com poucos dados | Requer grandes datasets para evitar overfitting |
| Interpretabilidade | Alta (coeficientes claros) | Baixa ("Caixa Preta") |
| Performance (Erro) | Inferior em regimes voláteis | Superior (menor RMSE/MAD) 40 |


## 7. Síntese: O Framework Integrado BL-ML-MAD e Métricas de Avaliação

A culminação dessa evolução teórica é um framework híbrido que une a estabilidade do Black-Litterman, a acurácia preditiva do Deep Learning e a robustez da avaliação via MAD.

### 7.1 O Fluxo de Trabalho "A+"

Um modelo de alocação de "nota A+" contemporâneo segue o seguinte algoritmo:
**Definição do Prior:** Calcular $\Pi$ (retornos de equilíbrio) usando a matriz de covariância histórica $\Sigma$ (possivelmente filtrada por GARCH para capturar volatilidade recente) e pesos de mercado.
**Geração de Visões (A "Competição"):**
Treinar modelos ARIMA e LSTM paralelamente.
Selecionar as previsões do modelo com menor erro fora da amostra para preencher o vetor $Q$.
**Calibração Dinâmica de Confiança ($\Omega$):**
Utilizar as variâncias condicionais do GARCH ou o erro histórico (MAD) dos modelos preditivos para preencher a diagonal de $\Omega$.
Aplicar o método de Idzorek para mapear a acurácia do modelo (ex: acurácia direcional de 60%) em um nível de confiança percentual para ajustar $\Omega$ intuitivamente.27
**Cálculo Posterior:** Computar $E$ e a nova matriz de covariância $\Sigma_{BL}$ via fórmulas do Black-Litterman.
**Otimização Robusta (MAD-Entropy):**
Em vez de usar a otimização quadrática (Média-Variância) com os novos *inputs*, utilizar a **Otimização de Desvio Absoluto Médio (MAD)**.
Isso previne que os *inputs* aprimorados sejam distorcidos por suposições de normalidade na etapa final de construção do portfólio.
Incorporar restrições de Entropia para garantir diversificação efetiva.

### 7.2 Avaliação de Desempenho: Por que MAD?

A avaliação final deste framework deve utilizar métricas consistentes com a filosofia de robustez. O uso do Desvio Absoluto Médio (MAD) como métrica de avaliação *ex-post* é preferível ao Desvio Padrão. O MAD é menos sensível a *outliers* extremos (que podem distorcer a variância ao serem elevados ao quadrado) e oferece uma medida de erro mais linear e intuitiva.
Estudos empíricos mostram que portfólios construídos sob este framework (BL com visões LSTM/GARCH e otimização robusta) superam consistentemente benchmarks como o índice de mercado e portfólios MPT tradicionais, apresentando Índices de Sharpe e Sortino superiores e menores *drawdowns* máximos em períodos de estresse.1

## 8. Restrições Regulatórias e Considerações Práticas

Nenhum modelo teórico está completo sem considerar as restrições do mundo real. A literatura aponta para a importância de incorporar restrições de cardinalidade (número mínimo/máximo de ativos) e limites de exposição, como a regra **5/10/40** (comum em fundos UCITS na Europa), que proíbe que mais de 10% do fundo seja investido em um único emissor e que a soma das posições acima de 5% não exceda 40% do total.45
A flexibilidade da programação linear do modelo MAD facilita a incorporação dessas restrições "duras" sem tornar o problema computacionalmente intratável, ao contrário da MPT, onde tais restrições podem criar superfícies de erro não convexas difíceis de otimizar. Além disso, a incorporação de custos de transação na função objetivo é vital para garantir que o ganho teórico (alpha) gerado pelas previsões do LSTM não seja erodido pelo *turnover* excessivo do portfólio.46

## 9. Conclusão

A jornada da Média-Variância de Markowitz aos frameworks contemporâneos aprimorados por Inteligência Artificial representa uma mudança de paradigma: de suposições idealizadas para a robustez baseada em dados. A MPT forneceu o vocabulário essencial de risco e retorno, mas sua fragilidade diante da realidade não gaussiana exigiu a evolução para PMPT e MAD. O modelo Black-Litterman resolveu a crise de implementação ao ancorar portfólios no equilíbrio de mercado, permitindo desvios controlados.
Hoje, a integração de redes LSTM para gerar essas "visões", calibradas pela incerteza do GARCH e otimizadas sob a lógica robusta do MAD e Entropia, constitui o estado da arte. Esta síntese não descarta as teorias antigas, mas as subsume: a MPT fornece o esqueleto, o Black-Litterman o sistema nervoso bayesiano, e o Deep Learning os olhos preditivos, criando um organismo dinâmico e adaptativo capaz de navegar a complexidade não linear dos mercados financeiros modernos.
#### Referências citadas
An Application of the Black-Litterman Model with ARIMA-ARCH Views for Islamic Stock Portfolio in Indonesian Stock Exchange - Asian Online Journals, acessado em novembro 18, 2025, 
Black-Litterman Model with Views Prediction Using Elman Recurrent Neural Network, acessado em novembro 18, 2025, 
Mean-Variance vs. Mean-Absolute Deviation: A Performance Comparison of Portfolio Optimization Models - ResearchGate, acessado em novembro 18, 2025, 
Understanding the Black-Litterman Model for Portfolio Optimization - Investopedia, acessado em novembro 18, 2025, 
Portfolio Optimization: MAD vs. Markowitz - Rose-Hulman Scholar, acessado em novembro 18, 2025, 
Post-Modern Portfolio Theory (PMPT) - DayTrading.com, acessado em novembro 18, 2025, 
Enhancing Black-Litterman Portfolio via Hybrid Forecasting Model Combining Multivariate Decomposition and Noise Reduction - arXiv, acessado em novembro 18, 2025, 
Black-Litterman Model - Definition, Example, Formula, Pros n Cons - Financial Edge, acessado em novembro 18, 2025, 
A STEP-BY-STEP GUIDE TO THE BLACK-LITTERMAN MODEL Incorporating user-specified confidence levels - Duke People, acessado em novembro 18, 2025, 
7.5 Drawbacks | Portfolio Optimization - Bookdown, acessado em novembro 18, 2025, 
Post-Modern Portfolio Theory And The Sortino Ratio - Sears Merritt, acessado em novembro 18, 2025, 
Optimal Algorithms And Lower Partial Moment: Ex-Post Results - ResearchGate, acessado em novembro 18, 2025, 
Getting Started with NNS: Overview, acessado em novembro 18, 2025, 
Sortino Ratio vs Sharpe Ratio - Key Differences - Bajaj Finserv, acessado em novembro 18, 2025, 
The Difference Between the Sharpe Ratio and the Sortino Ratio - Investopedia, acessado em novembro 18, 2025, 
Sharpe vs Sortino: Risk Metrics for Growth Companies - Phoenix Strategy Group, acessado em novembro 18, 2025, 
Using the Sortino Ratio to Gauge Downside Risk | Charles Schwab, acessado em novembro 18, 2025, 
MAD portfolio optimization — Hands-On Mathematical Optimization with AMPL in Python, acessado em novembro 18, 2025, 
Portfolio Optimization with a Mean–Absolute Deviation–Entropy Multi-Objective Model - NIH, acessado em novembro 18, 2025, 
Enhancing Black-Litterman Portfolio via Hybrid Forecasting Model Combining Multivariate Decomposition and Noise Reduction - arXiv, acessado em novembro 18, 2025, 
Portfolio optimization using Mean Absolute Deviation (MAD) and Conditional Value-at-Risk (CVaR) - Redalyc, acessado em novembro 18, 2025, 
Portfolio optimization using Mean Absolute Deviation (MAD) and Conditional Value-at-Risk (CVaR) - Redalyc, acessado em novembro 18, 2025, 
Portfolio optimization using Mean Absolute Deviation (MAD) and Conditional Value-at-Risk (CVaR) - SciELO, acessado em novembro 18, 2025, 
The Black Litterman Asset Allocation Model - DiVA portal, acessado em novembro 18, 2025, 
Black-Litterman Allocation — PyPortfolioOpt 1.5.4 documentation, acessado em novembro 18, 2025, 
Black-Litterman Allocation — PyPortfolioOpt 1.4.1 documentation, acessado em novembro 18, 2025, 
The Black-Litterman Model: An Investigation of Confidence - Lund University Publications, acessado em novembro 18, 2025, 
The Black-Litterman Model In Detail, acessado em novembro 18, 2025, 
Idzorek's method for Black-Litterman · Issue #95 · robertmartin8/PyPortfolioOpt - GitHub, acessado em novembro 18, 2025, 
Time series prediction using ARIMA vs LSTM - Data Science Stack Exchange, acessado em novembro 18, 2025, 
Comparative Analysis of LSTM and ARIMA Models for Financial Time Series Forecasting: A Case Study of AMD Stock Price Prediction, acessado em novembro 18, 2025, 
ARIMA vs. Machine Learning in Portfolio Return Forecasting: A Comparative Study Integrating GARCH-Based Volatility Estimation an - SciTePress, acessado em novembro 18, 2025, 
The Black-Litterman model: The definition of views based on volatility forecasts, acessado em novembro 18, 2025, 
Portfolio return using Black-litterman single view model with ARMA-GARCH and Treynor Black model - ResearchGate, acessado em novembro 18, 2025, 
Multivariate GARCH models and the Black-Litterman approach for tracking error constrained portfolios: An empirical analysis - ResearchGate, acessado em novembro 18, 2025, 
Multivariate GARCH models and the Black-Litterman approach for tracking error constrained portfolios: an empirical analysis - SciSpace, acessado em novembro 18, 2025, 
ARIMA vs Prophet vs LSTM for Time Series Prediction - Neptune.ai, acessado em novembro 18, 2025, 
[1911.09512] A Comparative Analysis of Forecasting Financial Time Series Using ARIMA, LSTM, and BiLSTM - arXiv, acessado em novembro 18, 2025, 
A Comparison of Neural Networks with Time Series Models for Forecasting Returns on a Stock Market Index - ResearchGate, acessado em novembro 18, 2025, 
A Comparison of ARIMA and LSTM in Forecasting Time Series, acessado em novembro 18, 2025, 
Mariantonnia/BL-LSTM - GitHub, acessado em novembro 18, 2025, 
Portfolio Construction Based on LSTM RNN and Black-Litterman Model: Evidence from Yahoo Finance - SciTePress, acessado em novembro 18, 2025, 
Black–Litterman Portfolio Management Using the Investor's Views Generated by Recurrent Neural Networks and Support Vector Regression, acessado em novembro 18, 2025, 
A DYNAMIC ASSET ALLOCATION STRATEGY INTEGRATING LONG SHORT- TERM MEMORY (LSTM) WITH THE BLACK-LITTERMAN MODEL Lappeenranta–Lah - LUTPub, acessado em novembro 18, 2025, 
Application of Mean Absolute Deviation Optimization in Portfolio Management - kth .diva, acessado em novembro 18, 2025, 
What are pros and cons of mean absolute deviation portfolio optimization?, acessado em novembro 18, 2025,
