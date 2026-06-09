UNIVERSIDADE FEDERAL DE GOIÁS
FACULDADE DE ADMINISTRAÇÃO, CIÊNCIAS CONTÁBEIS E CIÊNCIAS ECONÔMICAS
CURSO DE CIÊNCIAS CONTÁBEIS
PEDRO AUGUSTO PINHEIRO REIS
Moderna Teoria das Carteiras no Mercado de Ações Brasileiro:
Uma Opção para Diversificação e Gerenciamento do Risco
Goiânia 2024
UNIVERSIDADE FEDERAL DE GOIÁS
FACULDADE DE ADMINISTRAÇÃO, CIÊNCIAS CONTÁBEIS E CIÊNCIAS ECONÔMICAS
CURSO DE CIÊNCIAS CONTÁBEIS
PEDRO AUGUSTO PINHEIRO REIS
Moderna Teoria das Carteiras no Mercado de Ações Brasileiro:
Uma Opção para Diversificação e Gerenciamento do Risco
Goiânia
2024
Sumário
RESUMO 4
INTRODUÇÃO 5
REFERENCIAL TEÓRICO 7
METODOLOGIA DA PESQUISA 11
3.1. Tipo da Pesquisa 11
3.2. Definição da Amostra e Coleta de Dados 11
3.2.1. Universo 11
3.2.2. Amostra 11
3.2.3. Fonte dos Dados 13
3.2.4. Tratamendo dos dados 13
3.3. Desenho Experimental 13
3.4. Modelagem dos Inputs (As Três Carteiras) 13
3.5. Processo de Otimização (O Método de Markowitz) 13
3.6. Métricas de Avaliação de Desempenho 14
ANÁLISE E DISCUSSÃO DOS RESULTADOS 15
CONCLUSÃO 16
6 CRONOGRAMA 17
7-REFERÊNCIAS 18
RESUMO
Esse artigo avalia o desempenho de carteiras desenvolvidas de acordo com a Moderna Teoria das Carteiras (MPT) variando a estimação dos retornos esperados entre média historica, Arima e Redes Neurais Artificiais(LTSM) no mercado de ações brasileiro.
Os desempenhos das carteiras serão comparados entre si, além de benchmarks como o IBOVESPA e CDI, para o período de janeiro de 2010 a dezembro de 2024, demonstrando alternativas potenciais para investidores na elaboração de carteiras de ações no mercado brasileiro.
Palavras Chave: Carteira, Moderna Teoria das Carteiras, Markowitz, Variância
INTRODUÇÃO
Nos últimos anos, o mercado de capitais brasileiro passou por um processo de democratização expressiva, impulsionado principalmente pelo crescimento da participação dos investidores pessoas físicas.
Segundo relatório publicado pela B3 (Pessoas Físicas: uma análise da evolução dos investidores na B3, 2022), o número de CPFs ativos na bolsa passou de cerca de 1 milhão em 2017 para mais de 4,5 milhões em 2022. Apesar do avanço, observou-se também uma queda no saldo mediano em custódia — de R$ 7 mil para R$ 3 mil no mesmo intervalo — sugerindo a entrada de pequenos investidores, muitos dos quais sem conhecimento técnico profundo sobre gestão de portfólios.
Nesse cenário, cresce a relevância de estratégias eficazes de alocação de ativos, capazes de equilibrar retorno e risco de maneira acessível e objetiva.
A Moderna Teoria do Portfólio (Modern Portfolio Theory – MPT), proposta por Harry Markowitz em sua publicação seminal de 1952, inaugurou uma abordagem quantitativa para a seleção de ativos e a formação de carteiras eficientes.
Fundamentada nos conceitos de diversificação e fronteira eficiente, a teoria busca otimizar a alocação de recursos maximizando o retorno esperado e minimizando o risco, representado pela variância dos retornos (MARKOWITZ, 1952; 1959).
Posteriormente, William Sharpe (1966) contribuiu ao propor o Índice de Sharpe, que relaciona o retorno excedente ao risco total da carteira, oferecendo uma métrica objetiva de avaliação de desempenho ajustado ao risco.
Entretanto, a MPT assume hipóteses idealizadas — como a normalidade dos retornos e a simetria na distribuição dos riscos — que raramente se confirmam em mercados emergentes como o brasileiro.
Com base nessas limitações, diversos estudos passaram a explorar abordagens alternativas, culminando no desenvolvimento da Pós-Moderna Teoria do Portfólio (Post-Modern Portfolio Theory – PMPT).
Essa teoria propõe medidas mais adequadas ao comportamento do investidor real, como a semivariância, o Conditional Value at Risk (CVaR) e o Índice Ômega, priorizando a análise do risco de perdas ao invés da simples dispersão dos retornos (SORTINO; VAN DER MEER, 1991; ROM; FERGUSON, 1994).
A PMPT oferece, assim, uma visão mais realista e abrangente da gestão de portfólios, sobretudo em contextos de elevada volatilidade, assimetria e ocorrência de eventos extremos — características típicas de mercados emergentes (BROMBERG; COSTA JUNIOR, 2014).
Essa abordagem reconhece que os investidores não se preocupam apenas com a variabilidade, mas sim com o risco de perdas significativas, proporcionando métricas de avaliação mais sensíveis às preferências comportamentais dos agentes.
Diante desse panorama, este trabalho busca responder à seguinte questão de pesquisa: "Qual é o impacto no desempenho, ajustado ao risco, de carteiras Média-Variância otimizadas no mercado brasileiro, quando o input de retorno esperado ($\mu$) é estimado por modelos preditivos (ARIMA e LSTM) em comparação com a tradicional média histórica?"
no mercado brasileiro, no período de 2010 a 2024?
Este trabalho está estruturado da seguinte forma: o Capítulo 2 apresenta o referencial teórico... O Capítulo 3 descreve a metodologia... O Capítulo 4 analisa os resultados... O Capítulo 5 apresenta as conclusões.
REFERENCIAL TEÓRICO

### 2.1 A Moderna Teoria de Carteiras (MPT)

O universo dos investimentos é complexo e multifacetado. A Teoria Moderna de Portfólio (MPT), inaugurada pelo trabalho seminal de Harry Markowitz (1952) intitulado "Portfolio Selection", revolucionou a área de finanças ao propor um *framework* analítico para a seleção e alocação de ativos.
**Diversificação de Riscos**
Os ativos financeiros podem ser divididos em duas categorias principais: ativos com risco e ativos livres de risco. Um ativo livre de risco é aquele que oferece ao investidor a certeza do retorno esperado, resultando em uma variância (risco) dos retornos igual a zero (Reilly & Brown, 2011; Vernimmen et al., 2014).
Em contraste, os ativos de risco apresentam várias fontes de risco, que podem ser classificadas em riscos sistemáticos e não-sistemáticos. Os riscos não-sistemáticos (riscos específicos do ativo) podem ser minimizados pela diversificação, porém o risco sistemático (risco de mercado) não pode ser eliminado (Bodie et al., 2011; Berk et al., 2012).
Harry Markowitz (1952, 1959) elucidou como o risco de um portfólio estava conectado com as covariâncias dos ativos individuais que o compõem. Ele observou que a variância de um ativo por si só não era particularmente relevante, mas sim sua contribuição para a variância do portfólio (Elton et al., 2012). Dessa forma, o autor consolidou o que era conhecimento convencional e gerou um processo pelo qual os investidores poderiam escolher portfólios diversificados otimizados: a Análise Média-Variância (Damodaran, 2007).
**Análise Média-Variância**
A metodologia de seleção de portfólios proposta por Markowitz (1952, 1959) se preocupa com duas dimensões: o retorno esperado do portfólio (E(Rp)) e a variância dos retornos do portfólio ($\sigma^2$). O princípio central é o *trade-off* entre risco e retorno: o investidor racional busca maximizar o retorno esperado para um dado nível de risco, ou minimizar o risco para um retorno esperado pré-determinado.
Todas as combinações possíveis de ativos disponíveis formam o conjunto possível de portfólios (*feasible set*). No entanto, apenas os portfólios que oferecem o maior retorno esperado para um determinado risco são considerados portfólios eficientes. O conjunto desses portfólios eficientes é chamado de fronteira eficiente (Fabozzi & Markowitz, 2011). Um critério amplamente adotado para selecionar o portfólio ideal na fronteira eficiente é a maximização do Índice de Sharpe, que mede o excesso de retorno da carteira (acima da taxa livre de risco) por unidade de risco (desvio-padrão dos retornos).
A metodologia Média-Variância possui duas premissas básicas: a normalidade das distribuições dos retornos dos ativos e que as funções de utilidade de todos os investidores são quadráticas.

### 2.2 Pós-Moderna Teoria de Carteiras (PMPT) e Risco Downside

A principal crítica à MPT, conforme apontado por Damoradan (2007), é que a premissa de normalidade raramente se sustenta, pois a maioria dos investimentos não possui retornos normalmente distribuídos e simétricos. A MPT utiliza a variância como medida de risco, que penaliza igualmente os desvios positivos (volatilidade "boa") e os desvios negativos (volatilidade "ruim").
A Pós-Moderna Teoria de Carteiras (PMPT) surge para endereçar essa limitação, alinhando-se às Finanças Comportamentais ao reconhecer que investidores são mais avessos a perdas do que à variabilidade geral (Roy, 1952). A PMPT foca, portanto, no **risco *****downside***.
**Semivariância e Índice de Sortino**
A principal métrica da PMPT é a **semivariância** (ou *downside deviation*). Diferente da variância (que mede a dispersão em torno da média), a semivariância mede apenas a dispersão dos retornos que caem *abaixo* de um retorno-alvo mínimo aceitável (MAR), frequentemente a própria média ou a taxa livre de risco.
Com base nessa métrica, Sortino e van der Meer (1991) propuseram o **Índice de Sortino**. Ele é análogo ao Índice de Sharpe, mas substitui o desvio-padrão (risco total) no denominador pela semivariância (risco *downside*). Isso permite uma avaliação mais precisa do retorno ajustado ao risco, penalizando apenas a volatilidade indesejada (perdas).
**Value-at-Risk e Conditional Value-at-Risk**
Outras medidas de risco *downside* amplamente utilizadas são o Value-at-Risk (VaR) e sua adaptação, o Conditional Value-at-Risk (CVaR) (Dempster, 2002).
Jorion (2006) define VaR como uma medida da maior potencial perda em valor de um ativo de risco ou portfólio em um dado período de tempo para um dado intervalo de confiança. Apesar do sucesso do VaR, ele foi criticado por duas razões principais: ele mede apenas os percentis da distribuição de perdas, ignorando perdas além do nível de VaR (chamado de *tail risk*); e não é uma medida coerente de risco, pois não é subaditivo (Artzner et al., 1997, 1999; Yamai & Yoshiba, 2005).
Para contornar o problema de *tail risk* e de subaditividade, Artzner et al. (1997, 1999) propuseram o CVaR (também chamado de *expected shortfall*). Satisfazendo todos os axiomas de uma medida coerente de risco, o CVaR pode ser definido como a média ponderada das expectativas de perdas quando essas são maiores que o VaR (Moreira, 2006).

### 2.3 O Problema Fundamental dos Inputs na MPT

Apesar do apelo intuitivo do modelo Média-Variância, sua aplicação prática enfrenta desafios notáveis, sendo o mais grave o **erro de estimação** dos parâmetros de entrada (*inputs*). Elton e Gruber (1997) mostraram como a Análise Média-Variância é sensível à forma como os *inputs* (retorno esperado e variância) são calculados.
Estudos empíricos demonstram que os portfólios ótimos derivados do modelo MV são muito sensíveis e instáveis a pequenas variações nos dados de entrada. Em particular, erros de estimação do vetor de retornos esperados ($\mu$) são consideravelmente mais impactantes na composição final do portfólio do que os erros de estimação da matriz de covariância ($\Sigma$) (DeMiguel e Nogales, 2009).
A tese central desta pesquisa está fundamentada nesta lacuna da MPT: a qualidade do portfólio ótimo é diretamente dependente da qualidade da estimativa de $\mu$. Se os parâmetros são calculados a partir de dados passados, eles próprios estão sujeitos à incerteza, degradando substancialmente o desempenho da solução ótima (Santos e Tessari, 2012).

### 2.4 Abordagens para Estimação de **$\mu$**

Para enfrentar o problema de incerteza na estimativa de $\mu$, a literatura acadêmica tem explorado diversas metodologias. Este trabalho se propõe a comparar o desempenho *out-of-sample* (fora da amostra) de portfólios Máximo Sharpe gerados a partir de três abordagens distintas de previsão de retorno.
**2.4.1 Abordagem Clássica: A Média Histórica Simples**
A forma mais difundida e simples de estimar o retorno esperado de um ativo é assumir que os retornos históricos são representativos do comportamento futuro. Assim, o valor de $\mu$ é frequentemente calculado como a média aritmética simples dos retornos observados na série histórica.
Contudo, a premissa de que o passado é o melhor preditor do futuro apresenta uma limitação, tornando os parâmetros sensíveis à janela temporal utilizada. A fragilidade deste método manifesta-se em alocações pouco intuitivas e instáveis, frequentemente resultando em portfólios que, fora da amostra, podem ser superados até mesmo por estratégias simplórias como a carteira igualmente ponderada (1/N) (DeMiguel e Nogales, 2009).
**2.4.2 Abordagem Estatística: Modelos de Séries Temporais (ARIMA)**
Reconhecendo que os retornos financeiros são processos estocásticos com dinâmicas temporais, modelos estatísticos avançados são utilizados para gerar previsões mais robustas para $\mu$.
Modelos de Séries Temporais, como o ARIMA (Autoregressive Integrated Moving Average), são amplamente utilizados para prever valores futuros de séries temporais. O ARIMA generaliza o modelo ARMA e é capaz de transformar séries não estacionárias em estacionárias. Para lidar com a característica dos mercados financeiros que apresentam agrupamento de volatilidade (*volatility clustering*), modelos como o GARCH (Heterocedasticidade Condicional Autorregressiva Generalizada) são frequentemente conjugados ao ARIMA, permitindo gerar previsões condicionais de retorno e risco (*one step ahead*).
**2.4.3 Abordagem de Machine Learning: Redes Neurais (LSTM)**
Nos últimos anos, a previsão de retornos tem se beneficiado da utilização de algoritmos de *Machine Learning* (ML). As técnicas de ML são vantajosas por manipularem grandes volumes de dados e identificarem padrões complexos e não lineares nos dados financeiros que os métodos lineares tradicionais podem falhar em capturar.
Neste contexto, as Redes Neurais Recorrentes (RNN), particularmente as redes de Memória de Longo Curto Prazo (LSTM) (*Long Short-Term Memory*), destacam-se. A arquitetura LSTM é projetada especificamente para aprender dependências de longo prazo em dados sequenciais, capturando correlações ocultas e não lineares, o que as torna uma solução poderosa para a modelagem do retorno de ativos.
METODOLOGIA DA PESQUISA

### 3.1. Tipo da Pesquisa

Esta pesquisa é classificada como **quantitativa**, **descritiva** e **aplicada**. Utiliza-se da **modelagem e simulação** (*backtesting*) como principal técnica de análise de dados.
O foco metodológico é a construção e comparação de desempenho de três estratégias de portfólio que utilizam a otimização Média-Variância (Máximo Sharpe), mas que diferem fundamentalmente na metodologia de estimação do vetor de retornos esperados ($\mu$): (1) Média Histórica, (2) Previsão ARIMA e (3) Previsão LSTM. O desempenho das carteiras será analisado tanto entre si quanto comparado a *benchmarks* de mercado (IBOVESPA e CDI). A taxa do CDI (Certificado de Depósito Interbancário) será utilizada como *proxy* para a taxa livre de risco.

### 3.2. Definição da Amostra e Coleta de Dados


#### 3.2.1. Universo

O universo da pesquisa compreenderá as ações listadas na B3 no período de janeiro de 2010 a dezembro de 2024. A escolha deste período de 14 anos justifica-se pela necessidade de uma janela temporal longa o suficiente para o treinamento robusto dos modelos de redes neurais e para capturar múltiplos ciclos de mercado (ex: crises, períodos de alta).

#### 3.2.2. Amostra

A amostra será composta por um conjunto de ações selecionadas com base em critérios rigorosos de liquidez, visando garantir a replicabilidade da estratégia e evitar vieses de ativos pouco negociados. Serão incluídas na carteira teórica as ações que integraram o Índice Bovespa (IBOVESPA) ou o Índice Brasil 100 (IBrA-100) em, no mínimo, 80% dos pregões dentro do período de análise.

#### 3.2.3. Fonte dos Dados

Os dados serão obtidos da plataforma Economática, consistindo dos preços de fechamento ajustado diários para todos os ativos da amostra, bem como as séries históricas do IBOVESPA e do CDI, dentro da janela temporal de 2010 a 2024.

#### 3.2.4. Tratamento dos dados

Os dados de preço de fechamento ajustado serão transformados em retornos logarítmicos diários, que são preferíveis em análises financeiras devido às suas propriedades estatísticas (como a estacionariedade e a aditividade temporal).

### 3.3. Desenho Experimental

Para evitar o viés de *look-ahead* (uso de informações futuras) e simular realisticamente a decisão de um investidor, será utilizada uma metodologia de *backtesting* baseada em **Janela Deslizante (*****Rolling Window*****)**.
A **Janela de Treinamento** consistirá de **60 meses (5 anos)** de dados históricos diários. Esses dados serão usados para treinar os modelos preditivos (ARIMA, LSTM) e calcular os parâmetros de *input* (média histórica e matriz de covariância).
O **Período de Teste** (ou período de previsão) será de **1 mês** subsequente. Os modelos preverão o retorno esperado ($\mu$) para este mês.
A **Frequência de Rebalanceamento** da carteira será **mensal**. Ao final de cada mês de teste, a janela deslizará um mês para frente (descartando o mês mais antigo e incorporando o mês mais recente), e todo o processo de treinamento, previsão e otimização será repetido.

### 3.4. Modelagem dos Inputs (As Três Carteiras)

Para cada período de rebalanceamento no *backtest*, a Matriz de Covariância ($\Sigma$) será calculada usando os dados históricos da janela de treinamento e será a mesma para todas as carteiras. O diferencial da pesquisa reside no cálculo do Vetor de Retorno Esperado ($\mu$):
**Carteira 1 (Baseline - Média Histórica):** O $\mu$ de cada ativo será a média aritmética simples dos retornos diários observados na Janela de Treinamento de 60 meses.
**Carteira 2 (ARIMA):** Para cada ativo, um modelo ARIMA(p,d,q) será ajustado aos dados da Janela de Treinamento. Os parâmetros (p,d,q) serão definidos dinamicamente usando a função **Auto-ARIMA** (baseada em critérios de informação como AIC ou BIC). O modelo fará uma previsão *out-of-sample* para o Período de Teste (1 mês). O $\mu$ será essa previsão.
**Carteira 3 (LSTM):** Para cada ativo, um modelo LSTM será treinado na Janela de Treinamento. A arquitetura consistirá em **duas camadas LSTM de 50 neurônios** e um *lookback period* (janela de tempo de entrada) de 60 dias. O modelo fará uma previsão *out-of-sample* para o Período de Teste. O $\mu$ será essa previsão.

### 3.5. Processo de Otimização (O Método de Markowitz)

Para cada uma das três carteiras, em cada período de rebalanceamento mensal, será calculado o portfólio de **Máximo Índice de Sharpe**.
A *proxy* para a Taxa Livre de Risco (R_f), necessária para o cálculo do Sharpe, será a taxa do **CDI** acumulada no período.
As **restrições** da otimização serão: (1) 100% dos pesos alocados (soma dos pesos = 1) e (2) proibição de venda a descoberto (*short selling*), ou seja, todos os pesos devem ser maiores ou iguais a zero ($w_i \ge 0$).

### 3.6. Métricas de Avaliação de Desempenho

Ao final do *backtest* (de 2015 a 2024, após a primeira janela de treino de 60 meses), será gerada a série temporal de retornos diários para as três carteiras simuladas. Elas serão comparadas usando as seguintes métricas:
**Retorno:** Retorno Total Acumulado e Retorno Médio Anualizado.
**Risco (MPT):** Volatilidade (Desvio Padrão) Anualizada.
**Risco (PMPT):** Semivariância Anualizada e Máximo *Drawdown*.
**Retorno/Risco (MPT):** Índice de Sharpe.
**Retorno/Risco (PMPT):** Índice de Sortino.
**Benchmarks:** O desempenho será comparado ao IBOVESPA e ao CDI no mesmo período.
ANÁLISE E DISCUSSÃO DOS RESULTADOS
(Conteúdo a ser desenvolvido após a execução da metodologia)
CONCLUSÃO
(Conteúdo a ser desenvolvido após a análise dos resultados)
6 CRONOGRAMA

| ATIVIDADES | Março | Abril | Maio | Junho | Julho |
| --- | --- | --- | --- | --- | --- |
| 1 | Entrega da carta de aceite | X |  |  |  |
| 2 | Realização da matricula pela secretaria acadêmica | X |  |  |  |
| 3 | Definição do tema do projeto | X |  |  |  |
| 4 | Definição da estrutura |  | X |  |  |
| 5 | Realização do Tópico 1 do referencial teórico |  | X |  |  |
| 6 | Realização do Tópico 2 do referencial teórico |  |  | X |  |
| 7 | Introdução |  |  | X |  |
| 8 | Introdução Ajustes finais da introdução |  |  | X |  |
| 9 | Metodologia Definição do modelo e operacionalização da pesquisa |  |  |  | X |
| 10 | Metodologia Ajuste final da metodologia |  |  |  | X |
| 10 | Entrega - Formatação ABNT |  |  |  |  |

Tabela 1 - Cronograma da Pesquisa
7-REFERÊNCIAS
Berk, J.; Demarzo, P. & Harford, J. (2012). Fundamentals of Corporate Finance. Boston: Prentice Hall.
Bodie, Z., Kane A., & Marcus, A. J. (2011). Investments. New York: McGraw-Hill/Irwin.
CHIAN, Swee C.; TAN, Kay C.; MAMUM, Abdullah Al. Evolutionary multi-objective
portfolio optimization in practical context. International Journal of Automation and
Computing, v. 5, p. 67-80, 2008.
Damodaran, A. (2007). Strategic Risk Taking: A Framework for Risk Management. London: FT Press.
DEMIGUEL, Victor; NOGALES, Francisco J. Portfolio selection with robust
estimation. Operations Research, v. 57, n. 3, p. 560-577, 2009.
Elton, E. J., Gruber, M. J., Brown, S. J. & Goetzmann, W. N. (2012).
Moderna Teoria de Carteiras e Análise de Investimentos. Rio de Janeiro: Elsevier.
Elton, E. J., & Gruber, M. J. (1997). Modern portfolio theory, 1950 to date.
Journal of Banking & Finance, 21(17), 1743-1759.
Fabozzi, F. J., & Markowitz, H. M. (2011). The Theory and Practice of Investment Management. Hoboken: John Wiley & Sons.
Markowitz, H. M. (1952). Portfolio Selection. Journal of Finance, 7(1), 77-91.
Markowitz, H. (1959). Portfolio Selection: Efficient Diversification of Investments. New York: John Wiley & Sons.
Reilly, F. K., & Brown, K. C. (2011). Investment Analysis & Portfolio Management. Mason: South-Western Cengage Learning.
SANTOS, André A. P.; TESSARI, Cristina. Técnicas quantitativas de otimização de carteiras
aplicadas ao mercado de ações brasileiro. Revista Brasileira de Finanças, v. 10, n. 3, p. 369-
393, 2012.
Vernimmen, P., Quiry, P., Dallocchio, M., Le Fur, Y., & Salvi, A. (2014). Corporate Finance: Theory and Practice. Hoboken: Wiley.
(Referências sobre PMPT, Sortino, ARIMA e LSTM devem ser adicionadas conforme o desenvolvimento do Cap. 2)
