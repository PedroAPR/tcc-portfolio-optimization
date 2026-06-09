# Avaliação Estratégica das Fontes Enviadas para o TCC "Moderna Teoria das Carteiras no Mercado de Ações Brasileiro"

Data: 25 de Novembro de 2025
Para: Pedro Augusto Pinheiro Reis, Faculdade de Administração, Ciências Contábeis e Ciências Econômicas, UFG
De: Especialista em Teoria de Portfólios e Modelagem Econométrica (PhD em Finanças Quantitativas)
Assunto: Avaliação da contribuição dos arquivos "Lecture 05: Portfolio Choice, CAPM, Black-Litterman" (Arquivo 2) e "An Application of the Black-Litterman Model with ARIMA-ARCH" (Arquivo 1) para o Trabalho de Conclusão de Curso (TCC).

## Sumário Executivo (Tese Central da Avaliação)

Após uma análise aprofundada dos dois arquivos enviados, em conjunto com o rascunho do Trabalho de Conclusão de Curso (TCC) 1 e o material de pesquisa contextual 1, conclui-se que as fontes fornecidas são de relevância *excepcional*. A contribuição destes materiais transcende a mera validação das escolhas metodológicas existentes; eles introduzem um *framework* teórico e prático – o **Modelo Black-Litterman (BL)** – que tem o potencial de unificar e elevar fundamentalmente a pesquisa.
O TCC 1 está corretamente estruturado como uma *competição* entre diferentes estimadores do vetor de retorno esperado ($\mu$) para a otimização de Média-Variância (M-V) de Markowitz. O estudo compara o desempenho de carteiras (Máximo Índice de Sharpe) geradas por: 1. Média Histórica (clássico), 2. ARIMA (estatístico) e 3. LSTM (machine learning).
Os dois arquivos enviados para avaliação 1 propõem, em vez de competição, uma *síntese*. Eles demonstram que o Modelo Black-Litterman é uma estrutura Bayesiana projetada especificamente para *combinar* um "prior" de equilíbrio (baseado em dados históricos e no CAPM) com "visões" preditivas (exatamente os *inputs* gerados pelos modelos ARIMA e LSTM). O Arquivo 1 1 fornece um precedente metodológico direto, usando ARIMA como a "visão". O Arquivo 2 1 fornece a base teórica para essa fusão.
Este relatório detalhará como essas fontes podem e devem ser usadas para:
**Validar a Justificativa (Problema):** Reforçar a crítica central ao "erro de estimação" (*Estimation Error*) da Média-Variância (M-V) de Markowitz.1
**Validar a Metodologia (Solução):** Fornecer um precedente acadêmico robusto para o uso de ARIMA e, por extensão, LSTM, para prever retornos no contexto de otimização de portfólio.1
**Validar a Avaliação (Risco):** Justificar a escolha de métricas da Pós-Moderna Teoria do Portfólio (PMPT) (Índice de Sortino, Semivariância), demonstrando as falhas da Variância em capturar o *tail risk* (risco de cauda) em dados não normais.1
**Propor uma Elevação Estratégica:** Sugerir uma oportunidade de transformar a tese de uma "competição" para uma "síntese", implementando uma "Carteira 4 (Black-Litterman)", que é o foco central de ambos os documentos fornecidos.
A análise detalhada é apresentada a seguir.

## I. Análise Crítica das Fontes Enviadas e Relevância para o TCC

Esta seção avalia cada um dos dois arquivos enviados 1 de forma isolada, dissecando seu conteúdo e estabelecendo sua relevância direta para as seções do TCC.1

### 1.1. O Alicerce Teórico (Arquivo 2: Slides MPT/CAPM/BL)

Os slides da "Lecture 05" 1 servem como um roteiro teórico perfeito para justificar a pergunta de pesquisa do TCC.1 Eles constroem a exata progressão lógica necessária para a fundamentação teórica.
O Ponto de Partida (Markowitz M-V)
Os slides iniciam definindo o problema clássico de Média-Variância (M-V) de Markowitz. Eles estabelecem a matemática da otimização para $N$ ativos arriscados, incluindo a derivação das primeiras condições de ordem (FOC) para encontrar os pesos da carteira ($w_p$).1 Crucialmente, eles introduzem o ativo livre de risco, o que lineariza a fronteira eficiente, criando a Reta do Mercado de Capitais (CML).1 O portfólio de tangência nesta reta é identificado como o "Portfólio com o maior sharp ratio" (Índice de Sharpe).1
**Contribuição ao TCC:** Esta seção valida diretamente a metodologia do TCC 1, que define o "Portfólio de Markowitz" a ser montado como a "Carteira de Máximo Índice de Sharpe". Os slides fornecem o fundamento teórico exato para essa escolha.
A Justificativa do Problema (Erro de Estimação)
Os slides, em alinhamento direto com o referencial teórico do TCC 1, identificam a falha crítica deste modelo: os inputs.
A Seção 3, "Estimating Mean and Co-Variance" 1, é notavelmente contundente. Ao discutir a estimação do "Mean return (drift)" usando dados históricos, o slide afirma que a "Estimação é muito imprecisa!" (Estimation is very imprecise!).1
A Seção 4, "Black-Litterman Model" 1, aprofunda essa crítica, explicando *por que* os dados históricos são estimadores ruins. O modelo M-V clássico ignora "priors estatísticos" e "priors econômicos".1 Um setor com um retorno passado atipicamente alto seria, pela M-V, assumido como tendo o mesmo retorno alto no futuro. O modelo atribui incorretamente o que poderia ser "sorte" como uma característica persistente.1
**Contribuição ao TCC:** Esta é a justificativa *central* para a pergunta de pesquisa do TCC. Os slides 1 fornecem uma base teórica robusta para a Seção 2.11 do TCC 1, que cita DeMiguel e Nogales (2009) e a natureza do otimizador M-V como um "maximizador de erros".
A Solução Teórica (Black-Litterman)
Os slides 1 não param na crítica; eles apresentam a solução. O Modelo Black-Litterman (BL) é introduzido como o framework que resolve o problema dos inputs.1
O modelo BL o faz através de uma síntese Bayesiana:
**O "Prior" ($\Pi$):** O modelo não começa do zero. Ele começa com um "bom ponto de partida" 1, que é o "Black Litterman Prior".1 Este "prior" ($\Pi$) é o vetor de retornos de equilíbrio de mercado, derivado do CAPM (ou seja, retornos proporcionais ao risco sistemático, $\beta$).1 A fórmula específica é dada como o prêmio de risco de equilíbrio: $\Pi = \gamma \Sigma w^{eq}$ 1, onde $\gamma$ é o coeficiente de aversão ao risco, $\Sigma$ é a matriz de covariância e $w^{eq}$ são os pesos de equilíbrio do mercado (por exemplo, capitalização de mercado).
**As "Visões" ($Q$):** O modelo, então, *ajusta* este "prior" de equilíbrio com base nas "visões" (views) do investidor.1 Essas "visões" são precisamente as previsões que o TCC 1 está gerando com ARIMA e LSTM. As visões são expressas na forma $P\mu = Q + \epsilon_v$ 1, onde $P$ é uma matriz que identifica os ativos na visão, $Q$ é o vetor de retornos esperados para essas visões, e $\Omega$ (a variância de $\epsilon_v$) é a matriz de confiança nessas visões.
A Síntese (Posterior): A "Master Formula" Bayesiana (o retorno "posterior") é apresentada na página 38 1:
$E =^{-1}$
**Contribuição ao TCC:** Esta fórmula 1 é a *conexão crítica* que o TCC pode explorar. Ela mostra analiticamente como *combinar* o "prior" de equilíbrio ($\Pi$, derivado de dados históricos/mercado) com a "visão" preditiva ($Q$, derivada dos modelos ARIMA/LSTM), ponderada pela confiança ($\tau$ e $\Omega$). Esta é a solução teórica para o problema que o TCC identifica.

### 1.2. O Precedente Metodológico (Arquivo 1: Artigo ARIMA-ARCH)

Se os slides 1 fornecem o *porquê* (teoria), o artigo de Widodo, Achsani e Andati 1 fornece o *como* (prática). Este artigo é uma referência de extrema valia para a metodologia do TCC, pois executa uma versão sofisticada do que o TCC propõe.
Validação da Escolha do Modelo (ARIMA)
O objetivo principal do artigo é claro: 1) "fazer a previsão do retorno das ações usando o método ARIMA-ARCH" e 2) "formar a combinação de carteira de ações islâmicas ideal usando o método de Black Litterman com ARIMA-ARCH".1
**Contribuição ao TCC:** Isso fornece um precedente acadêmico publicável e robusto para a "Carteira 2 (ARIMA)".1 O TCC pode (e deve) citar este artigo 1 em sua metodologia 1 como justificativa para a escolha de modelos ARIMA para previsão de retornos de ativos no contexto de otimização de portfólio. O artigo também reforça a necessidade de modelar a volatilidade (ARCH/GARCH), algo que o TCC 1 menciona na seção de PMPT e que é evidente nos dados não-normais.1
Metodologia Detalhada para Geração de "Views" (Visões)
O artigo 1 não apenas usa ARIMA, ele detalha exatamente como essa previsão se torna um input para o modelo de portfólio.
A Seção 3.2.2.5, "Estabilishing Investors's View" 1, afirma: "o input view dos investidores foi assumido que... foi buscado usando o modelo de ARIMA-ARCH forecasting". Para a "Visão Absoluta", a metodologia é direta: a matriz $P$ é 1, e o "valor Q... de return forecasting" é usado.1
**Contribuição ao TCC:** Isso valida diretamente a "Carteira 2", onde o vetor $\mu$ no otimizador M-V é simplesmente o *output* da previsão do ARIMA. O artigo 1 faz o mesmo, mas o chama de $Q$ para usá-lo dentro da estrutura BL.
Metodologia Inovadora para Quantificar Confiança ($\Omega$)
Esta é a contribuição mais sutil e poderosa do artigo.1 O modelo BL 1 requer uma matriz de confiança $\Omega$ (o quão certo o investidor está da sua visão?). O TCC 1 não aborda como quantificar a "confiança" em suas previsões de ARIMA ou LSTM. O artigo 1 oferece uma solução elegante e praticável.
A Seção 3.2.2.6, "Estabilishing the Level of Confidence" 1, detalha o processo:
O nível de confiança é estabelecido usando uma previsão de "4 semanas antes" do período de teste.
O "Return forecasting" (retorno previsto) é "comparado com o real return" (retorno real).
Essa comparação é quantificada usando o **"Mean Absolute Deviation (MAD)"** (Desvio Absoluto Médio).
Um limiar é estabelecido: Se o **MAD for > 0.02**, a confiança é baixa (definida como 1/3). Se o **MAD for < 0.02**, a confiança é alta (definida como 2/3).1
**Contribuição ao TCC:** Esta técnica 1 é uma adição metodológica de alto impacto. Ela fornece uma ferramenta para *quantificar e comparar* o poder preditivo do ARIMA vs. LSTM. O TCC pode adotar este *backtest* de 1 mês (conforme sua metodologia de rebalanceamento mensal 1) dentro da "Janela de Treinamento" 1 para gerar um MAD para o ARIMA e um MAD para o LSTM. O modelo com o *menor MAD* é objetivamente o melhor modelo preditivo, e seu valor MAD pode ser usado para *calibrar* a confiança ($\Omega$) caso o BL seja implementado.

## II. Síntese da Contribuição: Integrando as Fontes no Argumento do TCC

A fusão das contribuições de ambos os arquivos 1 revela o argumento central que o TCC 1 pode construir, transformando-o de um estudo comparativo para um estudo sintético.

### 2.1. O Problema dos Inputs: A Justificativa Central do TCC

A pergunta de pesquisa do TCC 1 é fundamentalmente sobre o "problema do erro de estimação". O TCC testa se previsões (ARIMA, LSTM) são estimadores de $\mu$ superiores à Média Histórica.
A validade desta premissa é inequivocamente apoiada pelos materiais. Os slides 1 e o referencial teórico do TCC (que cita DeMiguel e Nogales (2009) e o "maximizador de erros" 1) estão em perfeito alinhamento. A otimização M-V clássica é *extremamente sensível* a *inputs* de retorno esperado.1 O uso da Média Histórica simples, como os slides 1 apontam, é "muito impreciso".
Os arquivos, portanto, validam que esta é uma questão de pesquisa central e relevante em finanças modernas.

### 2.2. O "Galho" do ARIMA: Usando o Artigo
1

O TCC 1 propõe uma "competição": Média Histórica vs. ARIMA vs. LSTM.
O artigo de Widodo 1 atua como um *precedente direto* para a "Carteira 2 (ARIMA)". Ele prova que o uso de modelos ARIMA-ARCH para gerar *inputs* de retorno é uma abordagem metodológica válida e publicável.1
A "Carteira 3 (LSTM)" 1 pode, então, ser posicionada como uma extensão lógica e moderna desta abordagem. O TCC pode argumentar que, se Widodo 1 validou o uso de modelos *estatísticos* (ARIMA) para gerar visões, o trabalho atual dá o próximo passo, testando modelos de *machine learning* (LSTM) para a mesma tarefa. Esta abordagem é teoricamente mais adequada para capturar as dinâmicas não-lineares dos mercados financeiros, que a própria análise de dados do TCC 1 já identificou (caudas pesadas, assimetria).

### 2.3. A Conexão Crítica (e Perdida): O Modelo Black-Litterman como Síntese

Este é o *insight* mais importante derivado da *combinação* dos dois arquivos enviados 1 em contraponto ao TCC.1
**O Paradoxo da Metodologia do TCC:** O TCC 1 enquadra a Média Histórica (HA) e o ARIMA como *concorrentes* mutuamente exclusivos. O TCC cria $\mu_{\text{HA}}$ e otimiza (Carteira 1). Depois, cria $\mu_{\text{ARIMA}}$ e otimiza (Carteira 2). Isso força o otimizador a *confiar 100%* em um ou no outro.
**A Crítica a esta Competição:** O problema com a Carteira 1 ($\mu_{\text{HA}}$) é que ela é estável, mas "burra" (ignora *priors* econômicos, como os slides 1 apontam). O problema com a Carteira 2 ($\mu_{\text{ARIMA}}$) é que ela é "inteligente", mas *instável*. Ao alimentar *apenas* a previsão ARIMA no otimizador M-V, o portfólio torna-se *ainda mais* suscetível ao "maximizador de erros" 1 do que com a média histórica. O otimizador M-V atribuirá pesos extremos (e não-intuitivos) a quaisquer ativos que o modelo ARIMA preveja ter um retorno marginalmente maior.
**A Solução (Black-Litterman):** Os *dois* arquivos que o TCC enviou para análise 1 são sobre o modelo Black-Litterman (BL), que foi *literalmente inventado* por Fischer Black e Robert Litterman para resolver este exato problema de otimizadores instáveis e *inputs* preditivos.1
O modelo BL (conforme descrito nos slides 1) não descarta a Média Histórica. Ele a usa (via pesos de capitalização de mercado) para calcular o "prior" de equilíbrio, $\Pi$.1 Este $\Pi$ é o "ponto de partida" estável, que representa o consenso do mercado. Em seguida, o modelo BL pega a previsão (o *output* do ARIMA, como em 1) e a trata como uma "visão" ($Q$).
A fórmula BL 1 então *mistura* (via lógica Bayesiana) o $\Pi$ estável com a visão $Q$ preditiva, ponderada pela confiança ($\Omega$) que se tem na visão. O resultado é um *novo vetor de retorno esperado*, $E$, que é uma *mistura ponderada* e mais robusta. É o "melhor dos dois mundos": a estabilidade do mercado e a inteligência da previsão.
**Implicação para o TCC:** O TCC está atualmente comparando A vs. B. A literatura enviada 1 sugere que a melhor resposta não é A ou B, mas sim C = $\text{BL}(\text{A}, \text{B})$. Isso representa uma oportunidade de "nível A+" para o TCC, que será explorada na Seção IV de recomendações.

## III. Aprofundamento da Análise de Risco (Além da MPT)

O TCC 1 tem uma segunda linha de investigação: a crítica à *métrica de risco* (Variância) da MPT, que justifica o uso da Pós-Moderna Teoria do Portfólio (PMPT). O material de pesquisa coletado 1 valida fortemente essa abordagem.

### 3.1. Validando a PMPT: A Evidência de Não Normalidade no TCC

A premissa central da MPT para que a Variância ($\sigma^2$) seja uma medida de risco "suficiente" é que os retornos dos ativos sigam uma distribuição normal (Gaussiana).
A própria análise de dados do TCC na Seção 4.1 1 *refuta* essa premissa para o mercado brasileiro.
**Assimetria (Skewness):** O TCC relata que "a maioria dos ativos apresenta valores de assimetria diferentes de zero". Ativos como PETR4 (-0.94), NATU3 (-0.98) e PCAR3 (-3.23) exibem forte assimetria negativa. Isso indica que, como o TCC observa, "grandes perdas são comparativamente mais frequentes do que grandes ganhos de magnitude similar".1
**Curtose (Kurtosis):** Este é o indicador *crítico*. O TCC relata (corretamente) que "A curtose mede... o peso de suas caudas". O TCC encontrou "valores de curtose dramaticamente elevados para quase todos os ativos, um fenômeno conhecido como leptocurtose".1 Os valores citados (VALE3: 9.40, PETR4: 14.13, ELET3: 15.49, ASAI3: 2469.69) 1 são prova conclusiva de "caudas pesadas".
A *implicação* desses números 1 é que a **Variância é uma métrica de risco falha, incompleta e perigosa** para esta amostra. A alta curtose (caudas pesadas) significa que *eventos extremos* (crashes, picos) ocorrem com uma frequência muito maior do que o modelo de distribuição normal da MPT prevê. A variância, sendo uma medida simétrica 1, não captura esse *tail risk* (risco de cauda) e a assimetria (aversão a perdas).
Os próprios dados do TCC 1 fornecem a *justificativa empírica* para rejeitar a MPT clássica *e* para justificar a escolha de métricas de avaliação da PMPT (Índice de Sortino, Semivariância).1

### 3.2. Reforço Teórico para as Métricas de Avaliação
1

O artigo de Lovatto et al. (2017) 1 fornece o *reforço teórico* para a justificativa empírica. Este artigo compara diretamente a otimização M-V (Variância) com a otimização M-CVaR (Conditional Value-at-Risk), uma métrica da PMPT.
Os resultados de Lovatto 1 são diretamente aplicáveis:
A principal constatação é que "a métrica de risco variância, por sua vez, subestimou a probabilidade de eventos oriundos de tail risk".1
Eles descobriram que o CVaR "minimizou perdas mais acentuadas, decorridas de seu foco em risco downside".1
Em suma, Lovatto 1 conclui que, especialmente para investidores focados em *minimizar perdas*, a Variância (MPT) é sub-ótima e o CVaR (PMPT) é superior.
Este artigo 1 valida *exatamente* a escolha metodológica do TCC.1 O TCC está (corretamente) estruturado para:
**Otimizar** usando M-V (Variância), pois é o modelo clássico que está sendo testado.
**Avaliar** o desempenho *out-of-sample* usando métricas da PMPT (Índice de Sortino, Semivariância, Máximo Drawdown).1
O artigo 1 e os dados do TCC 1 provam por que esta avaliação dupla é necessária. O TCC *deve* avaliar com o Índice de Sortino porque ele (ao contrário do Índice de Sharpe) usa o *downside deviation* (semivariância) no denominador.1 O Índice de Sharpe, ao usar o desvio-padrão total (variância), penaliza a volatilidade positiva (o que é bom) e subestima o *tail risk*.1 Portanto, o Índice de Sortino é a métrica-chave para provar qual das carteiras (HA, ARIMA, LSTM) é *realmente* a melhor em termos de risco ajustado.

## IV. Recomendações Estratégicas para o TCC

Com base nesta análise, os arquivos enviados 1 não são apenas referências passivas; eles são um *chamado à ação* para elevar o nível analítico do TCC. A seguir, recomendações estratégicas acionáveis.

### Recomendação 1: Revisar o Referencial Teórico para Incluir Black-Litterman

**Problema:** O referencial teórico do TCC 1 salta de Markowitz (1952) e CAPM (1964) diretamente para PMPT (1990s) e "Estimation Error" (DeMiguel 2009). Ele omite completamente o Modelo Black-Litterman (1990), que foi a *principal solução* de consenso da indústria (Goldman Sachs) para o problema do "estimation error" por décadas.
**Ação:** É altamente recomendável incluir uma seção sobre o Modelo Black-Litterman no Referencial Teórico (Capítulo 2). Os slides 1 podem ser usados como fonte primária para explicar sua lógica Bayesiana, o "prior" de equilíbrio ($\Pi$) 1, o vetor de "visões" ($Q$) 1 e a "Master Formula".1 Isso posicionará o TCC como ciente da principal alternativa ao M-V ingênuo.

### Recomendação 2: Adotar a Metodologia MAD para Quantificar a Confiança da Previsão

**Problema:** O TCC 1 irá, inevitavelmente, descobrir que nem o ARIMA nem o LSTM são 100% precisos. Mas quão *imprecisos* eles são, e qual é o *melhor*?
**Ação:** Adotar a metodologia da Seção 3.2.2.6 do artigo de Widodo.1
Na estrutura de *backtest* de "Janela Expansível" 1, antes de cada rebalanceamento mensal, executar uma previsão de 1 mês *out-of-sample* (dentro da janela de treino).
Calcular o **MAD (Mean Absolute Deviation)** entre a previsão (ARIMA e LSTM) e o retorno real.
Relatar isso nos resultados. O TCC terá agora uma *métrica objetiva* para declarar qual modelo preditivo (ARIMA ou LSTM) foi *estatisticamente superior* na amostra, com base no *menor erro de previsão (MAD)*.

### Recomendação 3 (A "Tese A+"): Implementar uma "Carteira 4 (Black-Litterman)"

Esta é a recomendação mais avançada, mas que *unifica* todos os conceitos deste relatório e o conteúdo dos arquivos enviados.
**Problema:** O TCC 1 atualmente força uma escolha binária: ou o gestor confia 100% na Média Histórica (Carteira 1) ou 100% na previsão (Carteira 2 ou 3). Como os slides 1 e o TCC 1 apontam, ambas as abordagens são falhas (instáveis ou imprecisas).
**Ação (Metodologia):** Criar uma "Carteira 4 - Síntese Black-Litterman":
**Prior ($\Pi$):** Calcular o vetor de retornos de equilíbrio implícito (o $\Pi$ de 1) usando os pesos de capitalização de mercado da amostra de 81 ativos.1 Este é o *input* da "Média Histórica / Mercado".
**Visão ($Q$):** Usar o *output* de previsão do *melhor* modelo preditivo (seja ARIMA ou LSTM, conforme determinado pelo MAD da Recomendação 2). Este é o *input* de "visão".1
**Confiança ($\Omega$):** Usar o valor do MAD 1 do modelo vencedor para calibrar a matriz de confiança $\Omega$. (Um MAD alto significa baixa confiança, $\Omega$ grande; um MAD baixo significa alta confiança, $\Omega$ pequeno).
**Otimização:** Alimentar $\Pi$, $Q$, e $\Omega$ na "Master Formula" do Black-Litterman 1 para gerar o *novo vetor de retorno esperado* $E$.
**Carteira:** Usar este $E$ (em vez de $\mu_{\text{HA}}$ ou $\mu_{\text{ARIMA}}$) no otimizador M-V (Máximo Índice de Sharpe).
**Hipótese de Pesquisa:** A "Carteira 4 (BL)" deverá superar as Carteiras 1, 2 e 3 em métricas ajustadas ao risco (especialmente no Índice de Sortino), pois ela mitiga o "erro de estimação" ao *não* confiar 100% na previsão, mas sim ao usá-la para "puxar" o equilíbrio de mercado estável.

### Recomendação 4: Enfatizar o Índice de Sortino como a Métrica-Chave de Avaliação

**Ação:** Na "Análise e Discussão dos Resultados" 1, o TCC deve *liderar* com o Índice de Sortino e o Máximo Drawdown, e tratar o Índice de Sharpe como uma métrica secundária (clássica, porém falha).
**A Justificativa:** A própria análise de dados do TCC 1 e o artigo de Lovatto 1 provam conclusivamente que a Variância (e, portanto, o Índice de Sharpe) é uma medida de risco inadequada para a amostra, pois ignora o *tail risk*.1 O Índice de Sortino, que usa a Semivariância (focada no *downside risk*), é a única métrica que pode responder verdadeiramente à pergunta de pesquisa sobre desempenho *ajustado ao risco*.

#### Tabela Sugerida para o TCC (Capítulo 3 ou 4)

Para sintetizar a contribuição desta revisão, sugere-se a inclusão de uma tabela no TCC que compare a metodologia atual com os *frameworks* mais avançados que foram identificados.1
**Tabela 1: Comparação dos Modelos de Otimização de Portfólio**


| Característica | Carteira 1 (TCC - M-V Clássica) | Carteira 2/3 (TCC - M-V Preditiva) | Carteira 4 (Sugerida - Black-Litterman) |
| --- | --- | --- | --- |
| Fonte do Retorno ($\mu$) | Média Histórica Simples ($\mu_{\text{HA}}$) | Previsão Pura (e.g., $\mu_{\text{ARIMA}}$) | Misto: $E = f(\Pi, Q)$ 1 |
| Input 1: Equilíbrio ($\Pi$) | Ignorado. | Ignorado. | Retornos implícitos do mercado 1 |
| Input 2: Visão ($Q$) | Ignorado. | Previsão ARIMA / LSTM 1 | Previsão ARIMA / LSTM 1 |
| Input 3: Confiança ($\Omega$) | Implícita (100% na Média Hist.) | Implícita (100% na Previsão) | Explícita. Calibrada via MAD 1 |
| Problema Principal | "Muito impreciso".1 Ignora priors econômicos. | Instável. Vítima do "Maximizador de Erros".1 | Maior complexidade computacional. |
| Referência do TCC | Markowitz (1952) 1 | Baseado na crítica 1 | Widodo 1 / Slides 1 |

Esta tabela visualiza o *insight* central deste relatório. Ela mostra (coluna 2 vs 3) a "competição" que o TCC 1 estabeleceu. Mais importante, ela introduz a coluna 4, que demonstra a *síntese*. Ela força o leitor (e o autor do TCC) a ver que os *inputs* não são apenas o $\mu$, mas sim um sistema de $\Pi$, $Q$, e $\Omega$. Ela posiciona a Carteira 4 (BL) como a solução lógica para as fraquezas *combinadas* das Carteiras 1, 2 e 3.

## V. Conclusão da Avaliação

Os dois arquivos enviados 1 são de qualidade e relevância excepcionais para o TCC.1
Eles **validam** a premissa do TCC (o "erro de estimação" da M-V).
Eles **apoiam** a metodologia (o uso de ARIMA para prever retornos).
Eles **justificam** a estrutura de avaliação (a necessidade de métricas PMPT como Sortino, dado o *tail risk* que 1 e 1 identificam).
Mais importante, eles oferecem um *caminho claro para aprimoramento*, introduzindo o Modelo Black-Litterman como a estrutura teórica para *sintetizar* os *inputs* concorrentes, e o artigo de Widodo 1 como o *manual prático* para implementar essa síntese, incluindo a inovadora métrica de confiança baseada em MAD.1
A implementação das recomendações deste relatório, particularmente a inclusão do Modelo Black-Litterman como referencial ou como uma "Carteira 4" experimental, elevará significativamente o rigor acadêmico e a sofisticação do TCC.
#### Referências citadas
Análise comparativa de distintas métricas de risco na composição de um fundo de fundos de investimento imobiliário.pdf
