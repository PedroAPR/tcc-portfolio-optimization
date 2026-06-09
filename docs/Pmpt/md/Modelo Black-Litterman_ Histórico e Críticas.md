# Capítulo 3: O Modelo de Black-Litterman (BL) – Uma Reconstrução Bayesiana da Alocação de Ativos


## 3.1 Introdução: A Gênese Histórica e a Motivação Teórica

A evolução da gestão de portfólios institucionais sofreu uma inflexão paradigmática no início da década de 1990, impulsionada pelas limitações práticas da Teoria Moderna do Portfólio (MPT) de Harry Markowitz. Embora a MPT tenha fornecido a fundação matemática para a diversificação, a sua aplicação direta através da Otimização de Média-Variância (MVO) revelou-se problemática para gestores profissionais. Foi neste contexto de dissonância entre a elegância teórica e a frustração prática que Fischer Black e Robert Litterman, atuando na divisão de Gestão de Ativos da Goldman Sachs, desenvolveram o Modelo Black-Litterman (BL) (Goldman Sachs, 2025).

### 3.1.1 O Contexto da Goldman Sachs e a Colaboração Black-Litterman

Fischer Black, reverenciado no meio acadêmico e financeiro por sua contribuição fundamental ao modelo de precificação de opções Black-Scholes (1973), juntou-se à Goldman Sachs em 1984. Sua transição da academia para a prática financeira marcou um período de intensa inovação quantitativa na firma. Black assumiu a liderança do Grupo de Estratégias Quantitativas, onde colaborou estreitamente com Robert Litterman, então vice-presidente da divisão de pesquisa de Renda Fixa e um econometrista renomado (Goldman Sachs, 2025).
A motivação primordial para o desenvolvimento do modelo surgiu da observação de que os modelos de otimização quantitativa existentes eram raramente utilizados na sua forma pura pelos gestores de portfólio. Black e Litterman notaram que a imposição de restrições artificiais (como limites de posição longa ou proibição de vendas a descoberto) era a norma, utilizada para "domar" os resultados erráticos produzidos pela otimização de média-variância (Goldman Sachs, 2025).
Em 1990, a dupla apresentou internamente na Goldman Sachs uma abordagem inovadora para a alocação de ativos globais, inicialmente focada em mercados de títulos (bonds). O sucesso inicial levou à expansão do modelo para ações e moedas em 1991. A formalização acadêmica ocorreu com a publicação de dois artigos seminais: "Asset Allocation: Combining Investor Views with Market Equilibrium" no *The Journal of Fixed Income* (1991) e "Global Portfolio Optimization" no *Financial Analysts Journal* (1992) (Goldman Sachs, 2025). Estes trabalhos estabeleceram o BL não apenas como uma ferramenta proprietária, mas como um padrão da indústria para a gestão de ativos quantitativa.

### 3.1.2 A Crítica à MPT: O Dilema da Sensibilidade e a "Maximização de Erros"

A inovação de Black e Litterman foi uma resposta direta às falhas patológicas da otimização de Markowitz quando alimentada com estimativas ruidosas. A literatura acadêmica, notadamente os trabalhos de Michaud (1989) e Best e Grauer (1991), já havia identificado que a MVO atua como um "maximizador de erros" (Pires, 2021). O algoritmo de otimização, ao buscar matematicamente a fronteira eficiente, tende a sobrealocar capital em ativos com retornos esperados marginalmente superiores e subestimar aqueles com retornos inferiores, ignorando que essas diferenças podem ser meramente fruto de erros de estimação ou ruído estatístico.
Black e Litterman (1992) articularam que o problema central não residia na matemática da otimização em si, mas na dificuldade intrínseca de estimar o vetor de retornos esperados ($\mu$) (Black; Litterman, 1991). Enquanto a matriz de covariância ($\Sigma$) é relativamente estável e previsível ao longo do tempo, os retornos esperados são notoriamente voláteis e difíceis de prever. Na abordagem tradicional da MPT, um gestor é forçado a fornecer uma estimativa de retorno pontual para cada ativo no universo de investimento. Para um fundo global, isso poderia significar estimar retornos para centenas de ativos, muitos dos quais o gestor não possui uma opinião formada (visão neutra). A inserção de estimativas "neutras" ou baseadas apenas em médias históricas introduzia vieses que resultavam em portfólios extremos, instáveis e pouco diversificados, conhecidos como "soluções de canto" (corner solutions) (Risk..., 2025).
A solução proposta pelo modelo BL foi inverter o processo de engenharia do portfólio. Em vez de exigir que o investidor construísse as estimativas de retorno "do zero" (from scratch), o modelo parte de uma premissa de neutralidade baseada no equilíbrio de mercado. A filosofia subjacente é que, se o investidor não possui informações privilegiadas ou visões específicas que contradigam o mercado, a melhor estimativa de retorno é aquela que justifica a atual capitalização de mercado dos ativos. Apenas quando o investidor possui uma convicção forte (uma "visão") é que o portfólio deve desviar-se deste equilíbrio (Diversification.com, 2025).

## 3.2 Fundamentos Matemáticos: A Arquitetura Bayesiana

O rigor matemático do Modelo Black-Litterman reside na sua formulação como um problema de **inferência Bayesiana**. O modelo trata o vetor de retornos esperados verdadeiros ($\mu$) como uma variável aleatória não observável que deve ser estimada. O processo combina duas fontes de informação independentes — a distribuição a priori (Equilíbrio de Mercado) e a distribuição de verossimilhança (Visões do Investidor) — para gerar uma distribuição a posteriori dos retornos esperados (Dealing..., 2025).

### 3.2.1 A Otimização Reversa e os Retornos de Equilíbrio Implícitos (**$\Pi$**)

O primeiro passo do algoritmo BL é estabelecer o ponto de partida neutro, conhecido como **Prior**. Black e Litterman assumem que o mercado é eficiente e que a alocação média dos investidores é representada pelo portfólio de mercado (ponderado por capitalização).
Utilizando a formulação de média-variância, o problema de maximização da utilidade do investidor representativo é dado por:


$$\max_w U = w^T \Pi - \frac{\lambda}{2} w^T \Sigma w$$

Onde:
$w$ é o vetor de pesos dos ativos.
$\Pi$ é o vetor de retornos esperados em excesso (acima da taxa livre de risco).
$\Sigma$ é a matriz de covariância dos retornos dos ativos ($N \times N$).
$\lambda$ é o coeficiente de aversão ao risco do mercado.
Derivando em relação a $w$ e igualando a zero para encontrar o ótimo, obtemos a condição de primeira ordem:


$$\Pi = \lambda \Sigma w_{mkt}$$

Esta equação é conhecida como Otimização Reversa (Reverse Optimization). Ela permite calcular o vetor de retornos de equilíbrio implícitos ($\Pi$) que tornaria o portfólio de capitalização de mercado ($w_{mkt}$) o portfólio ótimo (Enhancing..., 2025).
O coeficiente de aversão ao risco ($\lambda$) é frequentemente calibrado empiricamente pela razão entre o prêmio de risco esperado do mercado e a variância do mercado:


$$\lambda = \frac{E - R_f}{\sigma^2_m}$$

Comumente, valores entre 2 e 4 são utilizados na prática, refletindo a aversão média ao risco dos investidores institucionais (Financial Edge, 2025).
Este vetor $\Pi$ serve como a média da distribuição a priori dos retornos esperados. A incerteza associada a esta estimativa a priori é modelada como proporcional à covariância dos retornos históricos, escalada por um parâmetro $\tau$:


$$E \sim N(\Pi, \tau\Sigma)$$

Onde $\tau$ (tau) é um escalar que reflete a confiança no modelo de equilíbrio (CAPM) (Jauk, 2025).

### 3.2.2 A Estrutura das Visões: Matrizes **$P$**, **$Q$** e **$\Omega$**

A segunda fonte de informação no modelo BL são as "visões" (views) subjetivas do investidor. Estas visões são expressas matematicamente como um sistema linear de equações com um termo de erro:


$$P \cdot \mu = Q + \varepsilon$$

Onde $\varepsilon \sim N(0, \Omega)$.
A especificação destas matrizes é crucial para a implementação correta do modelo:
**Matriz de Identificação ($P$):** Uma matriz de dimensão $K \times N$, onde $K$ é o número de visões e $N$ é o número de ativos. Cada linha $k$ representa uma visão específica.
**Visões Absolutas:** Se o investidor tem uma visão sobre o retorno absoluto de um único ativo (ex: "Ações Brasileiras retornarão 10%"), a linha correspondente em $P$ terá o valor 1 na coluna do ativo e 0 nas demais.
**Visões Relativas:** Se a visão é comparativa (ex: "Tecnologia superará Energia em 2%"), a linha terá pesos positivos para os ativos "long" e negativos para os ativos "short", tipicamente somando 0. A ponderação dentro de $P$ pode ser igualitária ou baseada em capitalização de mercado, conforme discutido por Satchell e Scowcroft (2000) e Idzorek (2005) (Black-Litterman..., 2025).
**Vetor de Visões ($Q$):** Um vetor coluna $K \times 1$ que contém os retornos esperados numéricos para cada visão. Para visões relativas, $Q$ representa o diferencial de retorno esperado (spread) (Financial Edge, 2025).
Matriz de Incerteza ($\Omega$): Uma matriz diagonal $K \times K$ que quantifica a incerteza ou o erro de estimação associado a cada visão. A diagonalidade implica que as visões são assumidas como independentes (os erros não são correlacionados).

$$\Omega = \text{diag}(\omega_1, \omega_2,..., \omega_k)$$

Se o investidor tem total confiança (certeza) em uma visão, o termo correspondente $\omega_k$ seria zero. Na prática, $\omega_k$ é sempre positivo, refletindo que nenhuma previsão é perfeita (Dealing..., 2025).

### 3.2.3 A Derivação da Distribuição Posterior (Fórmula Mestra)

Aplicando o Teorema de Bayes, combinamos a distribuição Prior ($N(\Pi, \tau\Sigma)$) com a distribuição de verossimilhança das visões ($N(Q, \Omega)$). Como ambas são gaussianas, a distribuição resultante (Posterior) também é gaussiana:


$$E_{BL} \sim N(\mu_{BL}, \Sigma_{BL})$$
A média a posteriori ($\mu_{BL}$), que representa o novo vetor de retornos esperados combinados, é dada pela "Fórmula Mestra" de Black-Litterman:

$$\mu_{BL} =^{-1}$$
Esta equação pode ser interpretada como uma média ponderada entre os retornos de equilíbrio ($\Pi$) e as visões ($Q$). Os pesos são determinados pela precisão das estimativas (o inverso da variância). Se $\Omega$ é grande (baixa confiança nas visões), o termo $P^T \Omega^{-1} P$ tende a zero e o retorno converge para o equilíbrio $\Pi$. Se $\tau$ é grande (baixa confiança no equilíbrio), o retorno converge para as visões $Q$ (Black-Litterman..., 2025).
Utilizando a Identidade de Matrizes de Woodbury, a equação é frequentemente reescrita para evitar a inversão da matriz de covariância completa, tornando o cálculo computacionalmente mais eficiente e intuitivo:
$$\mu_{BL} = \Pi + \tau\Sigma P^T^{-1} [Q - P\Pi]$$
Nesta forma, fica evidente que o retorno BL é o retorno de equilíbrio mais um termo de ajuste (tilt). O ajuste é proporcional ao desvio da visão em relação ao equilíbrio ($Q - P\Pi$), escalado pela incerteza relativa (Financial Edge, 2025).
A covariância a posteriori ($\Sigma_{BL}$), que deve ser utilizada no otimizador de portfólio, é dada por:


$$\Sigma_{BL} = \Sigma +^{-1}$$

O termo adicional representa a incerteza da estimativa da média, que deve ser incorporada ao risco total do portfólio (Black-Litterman..., 2025).

### 3.2.4 O Debate Acadêmico sobre o Escalar Tau (**$\tau$**)

O parâmetro $\tau$ permanece como um dos aspectos mais controversos e debatidos na literatura do modelo BL. Ele teoricamente representa a incerteza da estimativa da média dos retornos em relação à volatilidade dos próprios retornos.
**Black e Litterman (1992):** Originalmente argumentaram que $\tau$ deveria ser um valor pequeno, próximo de zero, pois a incerteza sobre a média é significativamente menor que a volatilidade diária dos ativos (The..., 2025).
**Satchell e Scowcroft (2000):** Propuseram que $\tau$ fosse definido como 1, simplificando a interpretação bayesiana, mas exigindo ajustes na matriz $\Omega$ para compensar (A..., 2025).
**Walters (2014) e Meucci (2005):** Sugerem calibrar $\tau$ com base no inverso do tamanho da amostra histórica ($1/T$), tratando-o como o erro padrão da média (Deconstructing..., 2025).
A contribuição crítica de **Thomas Idzorek (2005)** foi demonstrar que, sob o método de calibração de $\Omega$ proposto por He e Litterman (1999) — onde a variância da visão é proporcional à variância do prior — o valor escalar de $\tau$ torna-se matematicamente irrelevante para o cálculo do vetor de retornos esperados $\mu_{BL}$, pois ele se cancela na equação. No entanto, $\tau$ ainda afeta a matriz de covariância posterior, influenciando a magnitude do risco estimado (Jauk, 2025).

## 3.3 A Resolução das Falhas da MPT: Estabilidade e Intuição

A adoção generalizada do modelo BL por instituições financeiras deve-se, primariamente, à sua capacidade de resolver as patologias práticas da otimização de média-variância (MVO).

### 3.3.1 Mitigação da "Maximização de Erros"

A crítica seminal de Michaud (1989) rotulou a MVO como uma "maximizadora de erros" porque o algoritmo não distingue entre uma oportunidade real de arbitragem e um erro de estimação nos dados de entrada. Se o Ativo A tem um retorno esperado de 10% e o Ativo B de 10,1%, e ambos têm o mesmo risco, a MVO alocará agressivamente no Ativo B. Se essa diferença de 0,1% for ruído, a otimização amplifica o erro (Pires, 2021).
O modelo BL mitiga este problema através do mecanismo de *shrinkage* (ancoragem). Ao utilizar os retornos de equilíbrio implícitos como base, o modelo "puxa" as estimativas em direção a um prior robusto e economicamente fundamentado. Apenas visões com alta confiança (baixo $\Omega$) conseguem deslocar significativamente os pesos do portfólio para longe do benchmark de mercado. Isso resulta em uma distribuição de pesos mais suave e estável ao longo do tempo, reduzindo drasticamente o turnover e os custos de transação associados ao rebalanceamento frequente causado por ruído nos dados (Mean-Variance..., 2025).

### 3.3.2 Eliminação de Soluções de Canto (Corner Solutions)

As "soluções de canto" ocorrem quando o otimizador atinge os limites das restrições impostas (ex: 0% ou 100% de alocação em um ativo), resultando em portfólios binários e não diversificados. Na MVO tradicional, isso é quase inevitável sem a imposição de restrições de limites de posição arbitrárias (hard constraints) (Risk..., 2025).
Como o modelo BL gera um vetor de retornos que é, por construção, consistente com a matriz de covariância e os pesos de mercado (exceto onde há visões ativas), o portfólio resultante da otimização tende a ser naturalmente diversificado. As posições ativas (overweight/underweight) são tomadas apenas na medida da confiança do gestor, eliminando a necessidade de "forçar" a diversificação através de restrições exógenas que poderiam subotimizar o portfólio (Goldman Sachs, 2025).

### 3.3.3 Decomposição Intuitiva dos Pesos

Uma vantagem pedagógica e operacional do BL é a clareza na atribuição de alocação. O peso final de qualquer ativo no portfólio BL pode ser decomposto em:


$$w_{BL} = w_{mkt} + w_{views}$$

Ou seja, a alocação final é a soma da alocação passiva de mercado mais um portfólio de "visões" de soma zero (long/short). Isso permite que o gestor explique intuitivamente suas posições: "Estou comprado em Tecnologia acima do índice porque tenho uma visão otimista confiável sobre o setor", em oposição à "caixa preta" da MVO que poderia sugerir uma alocação inexplicável baseada em correlações espúrias (Black; Litterman, 1992).

## 3.4 Relação e Distinção frente à Teoria Pós-Moderna do Portfólio (PMPT)

A relação entre o Modelo Black-Litterman e a Teoria Pós-Moderna do Portfólio (PMPT) é frequentemente debatida no contexto de qual abordagem oferece a melhor "correção" para a MPT. A análise aprofundada revela que são abordagens complementares, atacando vetores distintos do problema de otimização (Not..., 2025).

### 3.4.1 Diferenças Ontológicas: Estimativa de Retorno vs. Medida de Risco

A distinção fundamental reside no foco de cada teoria:
**O Modelo Black-Litterman** é, primariamente, uma metodologia de **estimativa de parâmetros**. Seu foco está na melhoria da qualidade do vetor de *Retornos Esperados* (primeiro momento). O BL tradicional ainda utiliza a variância (segundo momento) como medida de risco e assume a normalidade dos retornos na sua derivação canônica (Wikipedia, 2025). Ele responde à pergunta: "Como posso obter uma estimativa de retorno futuro que incorpore minhas visões sem destruir a estabilidade do portfólio?"
**A PMPT (Post-Modern Portfolio Theory)**, introduzida por Rom e Ferguson (1993) e desenvolvida por Sortino, foca na redefinição da **medida de Risco**. A PMPT argumenta que a variância é uma medida falha porque penaliza a volatilidade positiva (upside) tanto quanto a negativa. A PMPT substitui a variância por medidas de *Downside Risk*, como a Semi-variância, o Desvio Abaixo do Alvo (Target Downside Deviation) ou o Conditional Value-at-Risk (CVaR). Ela responde à pergunta: "Como posso otimizar meu portfólio considerando que os investidores só se importam com as perdas e que os retornos não são normais (assimetria e curtose)?" (Wikipedia, 2025).

### 3.4.2 Integração Prática: O Modelo BL-Mean-CVaR

Dada a natureza não excludente das duas abordagens, a fronteira da pesquisa em finanças quantitativas tem avançado na integração do BL com a PMPT. É perfeitamente viável utilizar o arcabouço Bayesiano do BL para derivar o vetor de retornos esperados "limpo" ($E_{BL}$) e, subsequentemente, utilizar este vetor como input em um otimizador que minimiza o CVaR ou a Semi-variância, em vez da variância tradicional (Black-Litterman..., 2025).
Estudos empíricos, como os realizados por Teplova et al. (2022) e outros pesquisadores, demonstram que a combinação "BL + CVaR" (frequentemente utilizando Cópulas para modelar a dependência não-linear nas caudas) produz resultados superiores em testes fora da amostra (out-of-sample), especialmente durante regimes de crise financeira. Esta abordagem híbrida aproveita a robustez das estimativas de retorno do BL (evitando a maximização de erros) e a sensibilidade a caudas da PMPT (proteção contra downside) (Black-Litterman..., 2025).

### 3.4.3 Tabela Comparativa: MPT vs. BL vs. PMPT


| Característica | MPT (Markowitz) | Black-Litterman (BL) | PMPT (Post-Modern) |
| --- | --- | --- | --- |
| Input de Retorno | Histórico ou Subjetivo (Instável) | Equilíbrio + Visões (Bayesiano) | Histórico ou Subjetivo |
| Medida de Risco | Variância ($\sigma^2$) | Variância ($\sigma^2$) | Downside Risk / Semi-variância / CVaR |
| Distribuição Assumida | Normal (Gaussiana) | Normal (no modelo canônico) | Assimétrica / Caudas Gordas |
| Foco Principal | Diversificação matemática | Estabilidade e Incorporação de Visões | Assimetria de preferências do investidor |
| Resultado Típico | Soluções de Canto (Corner Solutions) | Portfólio Diversificado ancorado no Mercado | Portfólio com proteção de cauda |

(Grokipedia, 2025)

## 3.5 Aplicações Práticas, Extensões e Limitações

A transição do modelo teórico para a prática de mercado exigiu desenvolvimentos adicionais para tornar o BL acessível e aplicável a realidades complexas.

### 3.5.1 O Método de Idzorek: Democratizando a Matriz **$\Omega$**

Uma das maiores barreiras para a implementação do BL por gestores fundamentais era a complexidade na especificação da matriz de incerteza $\Omega$. O método original exigia que o gestor especificasse a variância do erro da sua visão, um conceito estatístico abstrato e difícil de intuir.
Thomas Idzorek (2005) propôs uma solução pragmática que revolucionou a usabilidade do modelo. Seu método permite que o usuário especifique um **Nível de Confiança** percentual (0% a 100%) para cada visão. O algoritmo de Idzorek funciona revertendo a lógica do modelo:
Calcula-se o vetor de retornos assumindo 100% de confiança na visão.
Deduz-se o peso implícito no portfólio que essa visão geraria.
Utiliza-se o percentual de confiança informado pelo usuário para interpolar linearmente entre o peso de mercado (0% confiança) e o peso da visão total (100% confiança).
A partir deste peso alvo, o algoritmo "implica" matematicamente qual o valor de $\Omega$ necessário para gerar tal resultado.
Esta abordagem removeu a necessidade de calibrar explicitamente o escalar $\tau$ e a matriz $\Omega$, permitindo que gestores expressassem visões de forma natural (ex: "Tenho 70% de confiança que o Tech vai subir") (Idzorek, 2005).

### 3.5.2 A Evolução Moderna: Fully Flexible Views (Meucci)

A limitação da suposição de normalidade no BL original tornou-se crítica após a crise de 2008, que evidenciou a prevalência de caudas gordas e assimetrias nos mercados. Attilio Meucci (2008, 2010) introduziu a extensão **"Fully Flexible Views"**, que generaliza o conceito do BL utilizando a teoria da **Entropy Pooling** (Meucci, 2008).
Nesta abordagem:
O Prior não precisa ser normal; pode ser uma distribuição empírica, uma distribuição de cópula ou qualquer distribuição de Monte Carlo.
As visões não se limitam a retornos esperados (médias). O gestor pode inserir visões sobre volatilidade ("A vol vai aumentar"), correlação ("A correlação vai quebrar") ou caudas ("O risco de crash é alto").
O processamento matemático minimiza a Entropia Relativa (Divergência de Kullback-Leibler) entre a distribuição a priori e a posterior, sujeita às restrições das visões.
O método de Meucci representa o "estado da arte" atual, permitindo que o BL seja aplicado em fundos de hedge complexos que operam derivativos e estratégias não-lineares, onde a normalidade é uma suposição perigosa (Combining..., 2025).

### 3.5.3 Limitações Críticas

Apesar das evoluções, o modelo BL não é uma panaceia e apresenta limitações que devem ser geridas:
**Dependência do Modelo de Equilíbrio:** O BL assume que o CAPM (ou modelo multifatorial escolhido) descreve corretamente o equilíbrio. Se o mercado for estruturalmente ineficiente ou se o proxy do "portfólio de mercado" for falho (Crítica de Roll), os retornos de ancoragem ($\Pi$) estarão enviesados, contaminando todo o processo (Toolshero, 2025).
**Qualidade das Visões (Garbage In, Garbage Out):** O modelo processa visões de forma coerente, mas não valida a sua qualidade. Se um gestor inserir visões errôneas com alta confiança (baixo $\Omega$), o modelo gerará portfólios eficientes ex-ante, mas desastrosos ex-post. A subjetividade humana continua sendo o elo mais fraco (Diversification.com, 2025).
**Estacionariedade:** O modelo assume implicitamente que a matriz de covariância histórica ($\Sigma$) é um bom previsor do risco futuro. Em regimes de mudança estrutural de mercado (quebra de correlações), essa suposição falha, exigindo o uso de modelos dinâmicos (GARCH/DCC) para estimar $\Sigma$, o que aumenta a complexidade computacional (Testing..., 2025).

## Conclusão do Capítulo

O Modelo de Black-Litterman transcendeu sua origem como uma ferramenta proprietária da Goldman Sachs para se tornar um pilar fundamental das Finanças Quantitativas modernas. Sua contribuição não foi refutar Markowitz, mas sim "salvar" a MPT de si mesma, introduzindo uma camada Bayesiana de bom senso econômico que estabiliza as alocações. Ao permitir a fusão elegante entre a disciplina passiva do equilíbrio de mercado e a inteligência ativa das visões do gestor, o BL resolveu o dilema da "maximização de erros". As suas extensões modernas, como o método de confiança de Idzorek e a Entropy Pooling de Meucci, juntamente com a integração com medidas de risco de cauda (CVaR), asseguram que o modelo permaneça na fronteira do conhecimento, adaptável a um mundo financeiro cada vez mais complexo e não-normal.
#### Referências citadas
GOLDMAN SACHS. **Innovative Black-Litterman Global Asset Allocation Model Is Developed at Goldman Sachs**. New York: Goldman Sachs, 2025. Disponível em: <https://www.goldmansachs.com/our-firm/history/moments/1990-black-litterman-model>. Acesso em: 28 nov. 2025.

BLACK–LITTERMAN model. In: **WIKIPEDIA: the free encyclopedia**. [S. l.]: Wikimedia Foundation, 2025. Disponível em: <https://en.wikipedia.org/wiki/Black%E2%80%93Litterman_model>. Acesso em: 28 nov. 2025.

LLM-ENHANCED Black-Litterman Portfolio Optimization. **arXiv**, 2025. Disponível em: <https://arxiv.org/abs/2309.00000>. Acesso em: 28 nov. 2025.

BLACK, Fischer; LITTERMAN, Robert. Global portfolio optimization. **Financial Analysts Journal**, Charlottesville, v. 48, n. 5, p. 28-43, set./out. 1992. Disponível em: <https://www.cfainstitute.org/research/financial-analysts-journal/1992/global-portfolio-optimization>. Acesso em: 28 nov. 2025.

PIRES, Arthur Martinez. **Impactos da Crise Hídrica na Matriz Energética Brasileira: uma Abordagem via Teoria de Portfólios**. 2021. Trabalho de Conclusão de Curso (Graduação em Engenharia de Produção) - Escola Politécnica, Universidade de São Paulo, São Paulo, 2021. Acesso em: 28 nov. 2025.

CORPORATE FINANCE INSTITUTE (CFI). **Breaking Down the Black-Litterman Model: Optimal Asset Allocation**. 2025. Disponível em: <https://corporatefinanceinstitute.com/resources/wealth-management/black-litterman-model/>. Acesso em: 28 nov. 2025.

BLACK, Fischer; LITTERMAN, Robert. Asset allocation: combining investor views with market equilibrium. **The Journal of Fixed Income**, v. 1, n. 2, p. 7-18, dez. 1991. Disponível em: <https://people.duke.edu/~charvey/Teaching/BA453_2006/Black_Litterman_1991.pdf>. Acesso em: 28 nov. 2025.

RISK budgeting and portfolio optimization - Constraints robust methods and black-litterman. 2025. Disponível em: <https://www.google.com>. Acesso em: 28 nov. 2025.

DIVERSIFICATION.COM. **Black litterman model: Meaning, Criticisms & Real-World Uses**. 2025. Disponível em: <https://www.diversification.com/black-litterman-model/>. Acesso em: 28 nov. 2025.

INVESTOPEDIA. **Understanding the Black-Litterman Model for Portfolio Optimization**. 2025. Disponível em: <https://www.investopedia.com/terms/b/black-litterman_model.asp>. Acesso em: 28 nov. 2025.

DEALING with Data: An Empirical Analysis of Bayesian Extensions to the Black-Litterman Model. 2025. Disponível em: <https://www.google.com>. Acesso em: 28 nov. 2025.

THE Black-Litterman Asset Allocation Model. **KTH Royal Institute of Technology**, Estocolmo, 2025. Disponível em: <https://www.diva-portal.org/>. Acesso em: 28 nov. 2025.

ENHANCING Black-Litterman Portfolio via Hybrid Forecasting Model Combining Multivariate Decomposition and Noise Reduction. **arXiv**, 2025. Disponível em: <https://arxiv.org/>. Acesso em: 28 nov. 2025.

BLACK-LITTERMAN Model: Advanced Portfolio Optimization with Market Equilibrium. 2025. Disponível em: <https://www.google.com>. Acesso em: 28 nov. 2025.

FINANCIAL EDGE. **Black-Litterman Model - Definition, Example, Formula, Pros n Cons**. 2025. Disponível em: <https://www.fe.training/>. Acesso em: 28 nov. 2025.

JAUK, Josef. **Portfolio Construction using the Black-Litterman Model and Factors**. London: CQF, CIIA, 2025. Disponível em: <https://www.google.com>. Acesso em: 28 nov. 2025.

TESTING the Black- Litterman Model. **Lund University**, Lund, 2025. Disponível em: <https://lup.lub.lu.se/>. Acesso em: 28 nov. 2025.

BLACK-LITTERMAN Model. 2025. Disponível em: <https://www.google.com>. Acesso em: 28 nov. 2025.

THE Black-Litterman Model In Detail. 2025. Disponível em: <https://www.google.com>. Acesso em: 28 nov. 2025.

A STEP-BY-STEP GUIDE TO THE BLACK-LITTERMAN MODEL. **Global Risk Guard**, 2025. Disponível em: <https://www.google.com>. Acesso em: 28 nov. 2025.

K2 CAPITAL. **The BlackLitterman Model: A Detailed Exploration**. 2025. Disponível em: <https://www.google.com>. Acesso em: 28 nov. 2025.

BLACK-LITTERMAN allocation model: Application and comparision with OMX Stockholm Benchmark PI (OMXSBPI). 2025. Disponível em: <https://www.google.com>. Acesso em: 28 nov. 2025.

THE Black Litterman Asset Allocation Model. **DiVA portal**, 2025. Disponível em: <https://www.diva-portal.org/>. Acesso em: 28 nov. 2025.

THE value of sell-side analysts' recommendations in active portfolio management. 2025. Disponível em: <https://www.google.com>. Acesso em: 28 nov. 2025.

THE Factor Tau in the Black-Litterman Model. **ResearchGate**, 2025. Disponível em: <https://www.researchgate.net/>. Acesso em: 28 nov. 2025.

A comparison of the black- litterman model and the mean- variance approach. **CBS Research Portal**, 2025. Disponível em: <https://www.google.com>. Acesso em: 28 nov. 2025.

DECONSTRUCTING Black-Litterman: How to Get the Portfolio You Already Knew You Wanted. 2025. Disponível em: <https://www.google.com>. Acesso em: 28 nov. 2025.

IDZOREK, Thomas M. **A Step-by-Step Guide to the Black-Litterman Model: Incorporating User-Specified Confidence Levels**. Chicago: Ibbotson Associates, 2005. Disponível em: <https://people.duke.edu/~charvey/Teaching/BA453_2006/Idzorek_onBL.pdf>. Acesso em: 28 nov. 2025.

MEAN-VARIANCE Optimization – an Overview. **CFA, FRM, and Actuarial Exams Study Notes**, 2025. Disponível em: <https://www.google.com>. Acesso em: 28 nov. 2025.

THE Black-Litterman Model: Extensions and Asset Allocation. **ResearchGate**, 2025. Disponível em: <https://www.researchgate.net/>. Acesso em: 28 nov. 2025.

IDZOREK, Thomas M. **A Step-by-Step Guide to the Black-Litterman Model: Incorporating User-Specified Confidence Levels**. Chicago: Ibbotson Associates, 2005. Disponível em: <https://people.duke.edu/~charvey/Teaching/BA453_2006/Idzorek_onBL.pdf>. Acesso em: 28 nov. 2025.

BLACK-LITTERMAN model with copula-based views in mean-CVaR portfolio optimization framework with weight constraints. **PMC - PubMed Central**, 2025. Disponível em: <https://www.google.com>. Acesso em: 28 nov. 2025.

BLACK-LITTERMAN Portfolio Allocation Stability and Financial Performance with MGARCH-M Derived Views. 2025. Disponível em: <https://www.google.com>. Acesso em: 28 nov. 2025.

(NOT So) Modern Portfolio Theory — "How To" Balance Expected Returns Against Risk. 2025. Disponível em: <https://www.google.com>. Acesso em: 28 nov. 2025.

MASTERING Investment Strategies with MPT. **PyQuant News**, 2025. Disponível em: <https://pyquantnews.com/>. Acesso em: 28 nov. 2025.

MODERN portfolio theory. In: **WIKIPEDIA: the free encyclopedia**. [S. l.]: Wikimedia Foundation, 2025. Disponível em: <https://en.wikipedia.org/wiki/Modern_portfolio_theory>. Acesso em: 28 nov. 2025.

MARKOWITZ model. In: **GROKIPEDIA**. [S. l.], 2025. Disponível em: <https://grokipedia.com/>. Acesso em: 28 nov. 2025.

POST-MODERN Portfolio Theory (PMPT). **DayTrading.com**, 2025. Disponível em: <https://www.daytrading.com/pmpt>. Acesso em: 28 nov. 2025.

BLACK–LITTERMAN Portfolio Optimization with Dynamic CAPM via ABC-MCMC. **MDPI**, 2025. Disponível em: <https://www.mdpi.com/>. Acesso em: 28 nov. 2025.

THE Black-Litterman Model: An Investigation of Confidence. **Lund University**, Lund, 2025. Disponível em: <https://lup.lub.lu.se/>. Acesso em: 28 nov. 2025.

IDENTIFYING the optimal level of gold as a reserve asset using Black–Litterman model: The case for Malaysia, Turkey, KSA and Pakistan. **Emerald Publishing**, 2025. Disponível em: <https://www.google.com>. Acesso em: 28 nov. 2025.

MEUCCI, Attilio. Fully flexible views: theory and practice. **Risk**, London, v. 21, n. 10, p. 100-105, out. 2008. Disponível em: <https://ssrn.com/abstract=1213091>. Acesso em: 28 nov. 2025.

COMBINING Tactical Views with Black-Litterman and Entropy Pooling. **Flirting with Models**, 2025. Disponível em: <https://www.google.com>. Acesso em: 28 nov. 2025.

ENTROPY Pooling vs Black-Litterman. **Medium**, 2025. Disponível em: <https://medium.com/>. Acesso em: 28 nov. 2025.

MEUCCI, Attilio. Fully flexible views: theory and practice. **Risk**, London, v. 21, n. 10, p. 100-105, out. 2008. Disponível em: <https://ssrn.com/abstract=1213091>. Acesso em: 28 nov. 2025.

TOOLSHERO. **Black Litterman Model Explained: Theory and Criticism**. 2025. Disponível em: <https://www.toolshero.com/>. Acesso em: 28 nov. 2025.
