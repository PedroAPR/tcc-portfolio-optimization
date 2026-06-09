# Referencial Teórico: Moderna Teoria das Carteiras (MPT)

> **Trabalho de Conclusão de Curso** — Moderna Teoria das Carteiras no Mercado de Ações Brasileiro  
> Faculdade de Administração, Ciências Contábeis e Ciências Econômicas — UFG  
> Autor: Pedro Augusto Pinheiro Reis

---

## Sumário

- [1. O Paradigma Pré-Markowitz: Da Seleção de Ativos à Análise Quantitativa](#1-o-paradigma-pré-markowitz-da-seleção-de-ativos-à-análise-quantitativa)
- [O Paradigma Pré-Markowitz: A Era da Seleção de Ativos](#o-paradigma-pré-markowitz-a-era-da-seleção-de-ativos)
  - [A Transição para a Análise Quantitativa](#a-transição-para-a-análise-quantitativa)
  - [1.1 O Paradigma Pré-Markowitz: A Era da Seleção de Ativos](#11-o-paradigma-pré-markowitz-a-era-da-seleção-de-ativos)
  - [1.2 A Transição para a Análise Quantitativa](#12-a-transição-para-a-análise-quantitativa)
- [2. A Revolução de Markowitz: O Modelo Média-Variância](#2-a-revolução-de-markowitz-o-modelo-média-variância)
  - [A Rejeição da Maximização Pura do Retorno](#a-rejeição-da-maximização-pura-do-retorno)
  - [2.1 A Rejeição da Maximização Pura do Retorno](#21-a-rejeição-da-maximização-pura-do-retorno)
- [3. A Revolução de Markowitz: A Formalização da Diversificação](#3-a-revolução-de-markowitz-a-formalização-da-diversificação)
- [3. Risco, Retorno e Covariância: A Matemática da Diversificação](#3-risco-retorno-e-covariância-a-matemática-da-diversificação)
- [Retorno Esperado do Portfólio](#retorno-esperado-do-portfólio)
- [Variância e Covariância](#variância-e-covariância)
- [O Papel da Correlação](#o-papel-da-correlação)
  - [3.1 Retorno Esperado do Portfólio](#31-retorno-esperado-do-portfólio)
  - [3.2 Variância e Covariância](#32-variância-e-covariância)
  - [3.3 O Papel da Correlação](#33-o-papel-da-correlação)
- [4. A Fronteira Eficiente e o Portfólio de Mínima Variância](#4-a-fronteira-eficiente-e-o-portfólio-de-mínima-variância)
- [Derivação e Definição](#derivação-e-definição)
- [O Portfólio de Mínima Variância Global](#o-portfólio-de-mínima-variância-global)
  - [Carteira de Mínima Variância Global (PMVG)](#carteira-de-mínima-variância-global-pmvg)
  - [2.2 A Fronteira Eficiente e a Geometria da Escolha Racional](#22-a-fronteira-eficiente-e-a-geometria-da-escolha-racional)
- [4. A Fronteira Eficiente: Otimização e Geometria](#4-a-fronteira-eficiente-otimização-e-geometria)
  - [4.1 Derivação e Definição](#41-derivação-e-definição)
  - [4.2 O Portfólio de Mínima Variância Global](#42-o-portfólio-de-mínima-variância-global)
  - [3.3. A Fronteira Eficiente e a Geometria da Escolha](#33-a-fronteira-eficiente-e-a-geometria-da-escolha)
- [5. O Ativo Livre de Risco e o Teorema da Separação de Tobin](#5-o-ativo-livre-de-risco-e-o-teorema-da-separação-de-tobin)
  - [O Ativo Livre de Risco e o Teorema da Separação](#o-ativo-livre-de-risco-e-o-teorema-da-separação)
  - [O Ativo Livre de Risco](#o-ativo-livre-de-risco)
- [O Teorema da Separação de Tobin](#o-teorema-da-separação-de-tobin)
  - [5.1 O Ativo Livre de Risco](#51-o-ativo-livre-de-risco)
  - [5.2 O Teorema da Separação de Tobin](#52-o-teorema-da-separação-de-tobin)
  - [4.1. O Teorema da Separação de Tobin](#41-o-teorema-da-separação-de-tobin)
- [6. A Reta do Mercado de Capitais (CML) e o Índice de Sharpe](#6-a-reta-do-mercado-de-capitais-cml-e-o-índice-de-sharpe)
- [A Reta do Mercado de Capitais (Capital Market Line - CML)](#a-reta-do-mercado-de-capitais-capital-market-line---cml)
- [Avaliação de Desempenho: O Índice de Sharpe](#avaliação-de-desempenho-o-índice-de-sharpe)
    - [2.3.1 O Teorema da Separação e a Reta do Mercado de Capitais (CML)](#231-o-teorema-da-separação-e-a-reta-do-mercado-de-capitais-cml)
  - [4.2 O Índice de Sortino vs. Índice de Sharpe](#42-o-índice-de-sortino-vs-índice-de-sharpe)
  - [5.3 A Reta do Mercado de Capitais (Capital Market Line - CML)](#53-a-reta-do-mercado-de-capitais-capital-market-line---cml)
  - [Tabela Resumo: Comparação entre CML e SML](#tabela-resumo-comparação-entre-cml-e-sml)
  - [5.1. Índice de Sharpe](#51-índice-de-sharpe)
- [7. O Modelo de Precificação de Ativos de Capital (CAPM)](#7-o-modelo-de-precificação-de-ativos-de-capital-capm)
  - [1.1. O Alicerce Teórico (Arquivo 2: Slides MPT/CAPM/BL)](#11-o-alicerce-teórico-arquivo-2-slides-mptcapmbl)
- [Decomposição do Risco: Sistemático vs. Não Sistemático](#decomposição-do-risco-sistemático-vs-não-sistemático)
  - [O Coeficiente Beta e a Reta do Mercado de Títulos (SML)](#o-coeficiente-beta-e-a-reta-do-mercado-de-títulos-sml)
  - [2.3 O Modelo de Precificação de Ativos de Capital (CAPM) e o Equilíbrio Geral](#23-o-modelo-de-precificação-de-ativos-de-capital-capm-e-o-equilíbrio-geral)
    - [2.3.2 Beta (**$\beta$**) e a Reta do Mercado de Títulos (SML)](#232-beta-beta-e-a-reta-do-mercado-de-títulos-sml)
  - [O Problema da Seleção de Portfólio: A Revolução de Markowitz](#o-problema-da-seleção-de-portfólio-a-revolução-de-markowitz)
  - [Definicao de risco](#definicao-de-risco)
  - [7.2 Decomposição do Risco: Sistemático vs. Não Sistemático](#72-decomposição-do-risco-sistemático-vs-não-sistemático)
  - [7.3 O Coeficiente Beta e a Reta do Mercado de Títulos (SML)](#73-o-coeficiente-beta-e-a-reta-do-mercado-de-títulos-sml)
- [4. A Evolução para o Equilíbrio Geral: CAPM e a Teoria da Separação](#4-a-evolução-para-o-equilíbrio-geral-capm-e-a-teoria-da-separação)
  - [4.3. Pressupostos Estruturais do CAPM](#43-pressupostos-estruturais-do-capm)
  - [4.4. A Derivação do Beta e a Linha do Mercado de Títulos (SML)](#44-a-derivação-do-beta-e-a-linha-do-mercado-de-títulos-sml)
- [8. Limitações e Críticas à MPT: O Problema do Erro de Estimação](#8-limitações-e-críticas-à-mpt-o-problema-do-erro-de-estimação)
    - [2.4.2 A Crítica de Michaud : O "Maximizador de Erros"](#242-a-crítica-de-michaud-o-maximizador-de-erros)
- [Referências Bibliográficas](#referências-bibliográficas)

---

## 1. O Paradigma Pré-Markowitz: Da Seleção de Ativos à Análise Quantitativa

## O Paradigma Pré-Markowitz: A Era da Seleção de Ativos

Até o início da década de 1950, a teoria de investimentos operava sob o "paradigma da seleção de ativos" (*stock picking*). A literatura seminal da época, epitomizada pelas obras de John Burr Williams e da dupla Benjamin Graham e David Dodd, focava quase exclusivamente na determinação do valor intrínseco de títulos individuais, tratando a construção do portfólio como uma consequência secundária da acumulação de ativos subavaliados (WILLIAMS, 2014).
John Burr Williams, em sua *magnum opus* de 1938, *The Theory of Investment Value*, introduziu o Modelo de Desconto de Dividendos (Dividend Discount Model - DDM), estabelecendo que o valor de um ativo é o valor presente de seus fluxos de caixa futuros esperados, descontados a uma taxa de juros apropriada (WILLIAMS, 2014). A fórmula de Williams,  , onde  representa os dividendos e  a taxa de desconto, proporcionou o primeiro rigor matemático para a avaliação de equities (GUERARD, 2010). Contudo, a abordagem de Williams sofria de uma limitação crítica: ela assumia que o risco poderia ser virtualmente eliminado através da diversificação, sem fornecer um mecanismo matemático para quantificar como a variabilidade dos retornos de diferentes ativos interagia (RUBINSTEIN, 2002). Williams focava na maximização do retorno esperado, acreditando que a "lei dos grandes números" protegeria o investidor que diversificasse suficientemente (RUBINSTEIN, 2002).
Paralelamente, Benjamin Graham e David Dodd, em *Security Analysis* , estabeleceram os princípios do *Value Investing*. Embora defendessem a diversificação como uma medida prudencial — sugerindo a detenção de dez a trinta papéis diferentes para mitigar o erro de análise — o conceito de risco em sua estrutura era fundamentalmente qualitativo (BOYD, JOHANSSON, KAHN, SCHIELE, SCHMELZER, 2024). Para Graham, risco não era volatilidade, mas sim a possibilidade de perda permanente de capital decorrente da deterioração dos fundamentos da empresa ou de pagar um preço excessivo em relação ao valor intrínseco (GUERARD, 2010). A "Margem de Segurança" era a métrica de proteção, não o desvio padrão ou a covariância. Neste paradigma, o portfólio era visto como uma coleção de ativos individuais, onde cada componente era julgado por seus próprios méritos, isolado do contexto agregado da carteira(GUERARD, 2010).

### A Transição para a Análise Quantitativa

A ruptura com o paradigma da seleção individual de ativos não ocorreu abruptamente, mas foi precedida por desenvolvimentos teóricos que começaram a questionar a suficiência da maximização do valor presente. Economistas como Hicks  e Marschak  já exploravam as preferências sobre momentos estatísticos, e o matemático italiano Bruno de Finetti, em 1940, havia formulado um problema de alocação média-variância no contexto de resseguros, embora seu trabalho tenha permanecido desconhecido no mundo anglófono por décadas (BOYD, JOHANSSON, KAHN, SCHIELE, SCHMELZER, 2024).
O momento decisivo, contudo, surgiu da insatisfação intelectual de Harry Markowitz com a teoria vigente. Enquanto lia a obra de Williams na biblioteca da Universidade de Chicago, Markowitz teve um *insight* que desmantelaria a lógica da maximização pura do retorno (MARKOWITZ, 1959). Ele percebeu que, se a regra de Williams fosse seguida estritamente em um mundo de incerteza, um investidor racional deveria alocar 100% de seu capital no único ativo com o maior retorno esperado descontado (WILLIAMS, 2014). Se dois ativos tivessem o mesmo retorno máximo, o investidor seria indiferente entre eles, mas a teoria não oferecia nenhuma razão intrínseca para manter ambos (MARKOWITZ, 1959).
Markowitz identificou que a prática observada e intuitivamente racional da diversificação — "não colocar todos os ovos na mesma cesta" — era inconsistente com a teoria de maximização de valor presente de Williams (MARKOWITZ, 1958). Para racionalizar a diversificação, era necessário introduzir uma segunda dimensão na função objetivo do investidor: o risco. A diversificação só faz sentido se o investidor estiver disposto a sacrificar uma parcela do retorno potencial para reduzir a incerteza do resultado final. Essa percepção marcou a transição da análise de títulos (*Security Analysis*) para a análise de portfólios (*Portfolio Analysis*), onde a unidade de análise deixa de ser a firma individual e passa a ser a carteira agregada (MARKOWITZ, 1958).

### 1.1 O Paradigma Pré-Markowitz: A Era da Seleção de Ativos

### 1.2 A Transição para a Análise Quantitativa

No período que antecedeu a década de 1950, a literatura financeira e a prática de mercado eram dominadas pela doutrina da "análise de segurança" (*security analysis*). A obra seminal de John Burr Williams, *The Theory of Investment Value* , estabeleceu o Modelo de Desconto de Dividendos (Dividend Discount Model - DDM) como a ferramenta primária de avaliação.1 Williams postulou que o valor intrínseco de uma ação deveria ser igual ao valor presente dos seus dividendos futuros, descontados a uma taxa de juros apropriada que refletisse o custo do dinheiro e o risco do negócio.
Sob essa ótica, a tarefa do investidor resumia-se a identificar ativos subvalorizados – aqueles cujos preços de mercado estivessem abaixo do seu valor intrínseco calculado. O risco era tratado de forma qualitativa ou através de ajustes na taxa de desconto, sem uma medida estatística precisa de incerteza baseada na dispersão de retornos.1 A diversificação, embora praticada intuitivamente e recomendada por adágios populares como "não coloque todos os ovos na mesma cesta", não possuía uma justificativa matemática rigorosa.3 A visão predominante era a de que, se um investidor pudesse identificar o ativo com o maior valor presente líquido ou o maior retorno esperado, a lógica da maximização de riqueza ditaria a concentração total de recursos nesse único ativo.
A ausência de uma definição operacional de risco como uma variável quantificável permitia um hiato entre a teoria e a prática. Enquanto a teoria de Williams sugeria concentração (para maximizar o retorno), a prática observada mostrava investidores mantendo carteiras diversificadas. Esse paradoxo evidenciava a necessidade de um modelo que explicasse a aversão ao risco e formalizasse o benefício da diversificação, não apenas como uma defesa contra a ignorância, mas como uma estratégia ótima de alocação de capital.
Benjamin Graham e David Dodd, operando a partir da Columbia Business School, estabeleceram em 1934 os preceitos do *Value Investing*. A filosofia central, imortalizada em *Security Analysis*, postulava que uma ação não era meramente um símbolo de cotação flutuante, mas uma fração de propriedade em um negócio real.4 Neste paradigma, o risco não era medido pela volatilidade dos preços, mas pela probabilidade de uma perda permanente de capital ou por um retorno inadequado sobre o investimento.
A metodologia de Graham focava obsessivamente na identificação do "Valor Intrínseco" — uma medida objetiva de valor derivada de ativos tangíveis, lucros, dividendos e perspectivas financeiras definitivas. A distinção crucial entre preço e valor permitia a definição da "Margem de Segurança": a diferença positiva entre o valor intrínseco calculado e o preço de mercado corrente. Quanto maior essa margem, menor o risco do investimento.
Um alfa positivo ($\alpha > 0$) sugere que o gestor "bateu o mercado" através de seleção de ativos (stock picking) ou timing de mercado, gerando retornos superiores aos justificados pelo risco sistemático assumido.
## 2. A Revolução de Markowitz: O Modelo Média-Variância

## A Revolução de Markowitz: O Modelo Média-Variância

A formalização matemática dessa nova perspectiva ocorreu com a publicação do artigo "Portfolio Selection" no *Journal of Finance* em 1952, expandido posteriormente na monografia *Portfolio Selection: Efficient Diversification of Investments*  (MARKOWITZ, 1959). A "Modern Portfolio Theory" (MPT) de Markowitz não apenas descreveu como os investidores agem, mas prescreveu como deveriam agir, fundamentando a decisão de investimento na interação estocástica entre ativos (MARKOWITZ, 1959).

### A Rejeição da Maximização Pura do Retorno

A premissa fundadora da MPT é que os investidores são, simultaneamente, maximizadores de retorno e avessos ao risco (MARKOWITZ, 1959). Markowitz rejeitou a hipótese de que os investidores consideram apenas o valor esperado (média) dos retornos futuros. Se os investidores focassem apenas na média, o conceito de um portfólio diversificado seria teoricamente injustificável, pois a diversificação quase sempre reduz o retorno esperado em comparação com a concentração no ativo de melhor desempenho (MARKOWITZ, 1952).
Portanto, a função de utilidade do investidor deve depender de dois parâmetros:
**Retorno Esperado (****µ****):** O valor médio ponderado das probabilidades dos retornos futuros.
**Risco (****σ****):** A dispersão ou incerteza desses retornos em torno da média.
A MPT postula que, para qualquer nível dado de risco, o investidor prefere o maior retorno possível; e para qualquer nível dado de retorno, prefere o menor risco possível. Essa estrutura de preferências cria um *trade-off* inevitável, substituindo a busca pelo "melhor ativo" pela construção do "melhor portfólio" (MARKOWITZ, 1952).

A história das finanças quantitativas é, em grande medida, a história da busca por uma métrica de risco que reflita fidedignamente a experiência humana de perda e incerteza. A Moderna Teoria do Portfólio (MPT), introduzida pelo trabalho seminal de Harry Markowitz em 1952, *Portfolio **Selection*, estabeleceu o alicerce sobre o qual a gestão moderna de investimentos foi construída, formalizando a intuição da diversificação através da análise de média-variância. No entanto, a hegemonia da MPT, embora duradoura, fundamentou-se em simplificações matemáticas — notadamente a distribuição normal dos retornos e a variância como *proxy* de risco — que se mostraram cada vez mais dissonantes da realidade empírica dos mercados globais e da psicologia do investidor.   
O surgimento da Teoria Pós-Moderna do Portfólio (PMPT) não deve ser interpretado como uma refutação do trabalho de Markowitz, mas sim como a sua evolução necessária e, ironicamente, um retorno às intenções originais do próprio autor. A PMPT emergiu formalmente no início da década de 1990, impulsionada pelo aumento exponencial da capacidade computacional, que permitiu aos pesquisadores e praticantes modelar a assimetria inerente aos retornos financeiros. Enquanto a MPT opera sob a suposição de simetria, tratando ganhos e perdas de igual magnitude como eventos de risco equivalentes, a PMPT reconhece a assimetria fundamental da preferência do investidor: a aversão à perda (downside) em detrimento da mera aversão à volatilidade.   
Este capítulo dedica-se a uma exegese profunda da PMPT, explorando suas raízes históricas, sua fundamentação matemática nos Momentos Parciais Inferiores (Lower Partial Moments - LPM), e a superioridade de suas métricas de risco — como a Semivariância, o Expected Shortfall (CVaR) e os índices de Sortino e Omega — em comparação com os análogos da MPT. A análise demonstrará que a PMPT oferece um arcabouço mais robusto para a construção de portfólios em um mundo caracterizado por distribuições de cauda gorda (*fat* *tails*), cisnes negros e comportamento irracional dos agentes.

É um equívoco comum na literatura financeira atribuir a invenção do foco no downside risk exclusivamente aos teóricos da década de 1990. Uma análise historiográfica rigorosa revela que Harry Markowitz, em sua monografia de 1959, Portfolio Selection: Efficient Diversification of Investments, dedicou um capítulo inteiro à semivariância. Markowitz postulou explicitamente que a semivariância — a variância calculada apenas sobre os retornos que caem abaixo da média ou de um alvo — produzia portfólios "intuitivamente melhores" do que aqueles baseados na variância total, pois os investidores não percebem a volatilidade positiva (ganhos acima da média) como risco, mas sim como oportunidade.
A decisão de Markowitz de fundamentar a MPT na variância, e não na semivariância, foi uma concessão pragmática imposta pelas restrições tecnológicas da época. Na década de 1950, o custo computacional para calcular a covariância de *downside* para um portfólio diversificado era proibitivo. A variância, com suas propriedades algébricas elegantes e simétricas, permitia soluções analíticas fechadas que podiam ser resolvidas com os recursos limitados disponíveis.
Consequentemente, a indústria financeira passou as três décadas seguintes otimizando portfólios com base em uma medida de risco (desvio padrão) que o próprio criador da teoria considerava uma segunda melhor opção. Foi somente com o advento dos microcomputadores de alta performance nas décadas de 1980 e 1990 que a barreira computacional foi superada, permitindo o renascimento da semivariância sob a égide da PMPT.

A inovação nuclear de Harry Markowitz não foi a descoberta da diversificação em si, um conceito conhecido desde os mercadores bíblicos, mas a sua formalização matemática. Antes de 1952, o risco era avaliado isoladamente. Markowitz demonstrou que o risco de um portfólio não é a soma linear dos riscos de seus componentes, mas uma função complexa que depende crucialmente da covariância entre eles.
A fórmula da variância do portfólio ($\sigma_p^2$) é a equação fundamental que sustenta toda a MPT:
$$ \sigma_p^2 = \sum_{i=1}^{N} w_i^2 \sigma_i^2 + \sum_{i=1}^{N} \sum_{j \neq i}^{N} w_i w_j \sigma_i \sigma_j \rho_{ij} $$
Nesta equação, $w$ representa os pesos dos ativos, $\sigma$ o desvio-padrão (risco) e $\rho_{ij}$ o coeficiente de correlação entre os ativos $i$ e $j$. A intuição poderosa aqui é que, à medida que o número de ativos ($N$) no portfólio aumenta, a importância da variância individual ($\sigma_i^2$) diminui quadraticamente, enquanto a importância das covariâncias ($\rho_{ij}$) assume o domínio do comportamento do risco total.1 Se a correlação entre os ativos for inferior a 1 ($\rho < 1$), o risco combinado será sempre menor que a média ponderada dos riscos individuais. Isso quantificou o "almoço grátis" da diversificação: a capacidade de reduzir o risco idiossincrático sem sacrificar o retorno esperado, restando apenas o risco sistemático ou de mercado.
## 2. A Revolução de Markowitz: O Modelo Média-Variância

### 2.1 A Rejeição da Maximização Pura do Retorno

A compreensão contemporânea dos mercados financeiros e a gestão de ativos apoiam-se sobre um edifício teórico construído em meados do século XX, cujos alicerces foram lançados por Harry Markowitz. No entanto, para apreciar a magnitude da revolução intelectual provocada pela Teoria Moderna do Portfólio (Modern Portfolio Theory - MPT), é imperativo contextualizar o ambiente acadêmico e profissional que a precedeu. Antes de 1952, a gestão de investimentos carecia de uma estrutura formalizada para o tratamento do risco e da diversificação, operando sob paradigmas que privilegiavam a seleção individual de ativos em detrimento da construção holística de carteiras.

A publicação do artigo "Portfolio Selection" no *Journal of Finance* em março de 1952 marcou o nascimento oficial da MPT.5 Neste trabalho, Markowitz rejeitou a hipótese de que os investidores deveriam apenas maximizar os retornos esperados, propondo em seu lugar uma estrutura de decisão bicritério: a análise Média-Variância.

O universo dos investimentos é complexo e multifacetado. A Teoria Moderna de Portfólio (MPT), inaugurada pelo trabalho seminal de Harry Markowitz  intitulado "Portfolio Selection", revolucionou a área de finanças ao propor um *framework* analítico para a seleção e alocação de ativos.
**Diversificação de Riscos**
Os ativos financeiros podem ser divididos em duas categorias principais: ativos com risco e ativos livres de risco. Um ativo livre de risco é aquele que oferece ao investidor a certeza do retorno esperado, resultando em uma variância (risco) dos retornos igual a zero (Reilly & Brown, 2011; Vernimmen et al., 2014).
Em contraste, os ativos de risco apresentam várias fontes de risco, que podem ser classificadas em riscos sistemáticos e não-sistemáticos. Os riscos não-sistemáticos (riscos específicos do ativo) podem ser minimizados pela diversificação, porém o risco sistemático (risco de mercado) não pode ser eliminado (Bodie et al., 2011; Berk et al., 2012).
Harry Markowitz (1952, 1959) elucidou como o risco de um portfólio estava conectado com as covariâncias dos ativos individuais que o compõem. Ele observou que a variância de um ativo por si só não era particularmente relevante, mas sim sua contribuição para a variância do portfólio (Elton et al., 2012). Dessa forma, o autor consolidou o que era conhecimento convencional e gerou um processo pelo qual os investidores poderiam escolher portfólios diversificados otimizados: a Análise Média-Variância (Damodaran, 2007).
**Análise Média-Variância**
A metodologia de seleção de portfólios proposta por Markowitz (1952, 1959) se preocupa com duas dimensões: o retorno esperado do portfólio (E(Rp)) e a variância dos retornos do portfólio ($\sigma^2$). O princípio central é o *trade-off* entre risco e retorno: o investidor racional busca maximizar o retorno esperado para um dado nível de risco, ou minimizar o risco para um retorno esperado pré-determinado.
Todas as combinações possíveis de ativos disponíveis formam o conjunto possível de portfólios (*feasible set*). No entanto, apenas os portfólios que oferecem o maior retorno esperado para um determinado risco são considerados portfólios eficientes. O conjunto desses portfólios eficientes é chamado de fronteira eficiente (Fabozzi & Markowitz, 2011). Um critério amplamente adotado para selecionar o portfólio ideal na fronteira eficiente é a maximização do Índice de Sharpe, que mede o excesso de retorno da carteira (acima da taxa livre de risco) por unidade de risco (desvio-padrão dos retornos).
A metodologia Média-Variância possui duas premissas básicas: a normalidade das distribuições dos retornos dos ativos e que as funções de utilidade de todos os investidores são quadráticas.

A gestão de investimentos, enquanto disciplina acadêmica e prática profissional, sofreu uma metamorfose radical ao longo do século XX. O que antes era considerado uma arte imprecisa, dominada pela intuição, rumores e análise subjetiva de balanços, transformou-se gradualmente em uma ciência rigorosa, fundamentada em estatística, teoria da probabilidade e modelagem econométrica. Este relatório propõe uma dissecação profunda da Teoria Moderna de Portfólio (MPT), não apenas como um conjunto de equações, mas como um movimento intelectual que redefiniu a relação humana com o risco financeiro.
Para compreender a magnitude da revolução iniciada em 1952, é imperativo contextualizar o ambiente pré-moderno. A história da gestão de risco não começou com Harry Markowitz; ela possui raízes que remontam aos contratos futuros de arroz no Japão de 1730 e à formalização dos mercados futuros em Chicago em 1864.1 Contudo, o tratamento matemático da especulação teve seu primeiro lampejo de genialidade com a tese de Louis Bachelier, "Théorie de la Spéculation", em 1900, que antecipou o uso do movimento browniano para modelar preços de ativos, embora seu trabalho tenha permanecido obscuro por décadas até ser redescoberto por economistas modernos.
A evolução subsequente, pontuada pela criação do *Journal of Risk and Insurance*  e do *Journal of Finance* , preparou o terreno para uma ruptura epistemológica.1 A transição da análise de segurança individual para a construção de portfólios ótimos, e posteriormente para o equilíbrio de mercado via CAPM, reflete uma busca incessante pela quantificação da incerteza. Este documento examina essa trajetória, desde os escombros de 1929 que informaram a prudência de Graham e Dodd, passando pela elegância da Fronteira Eficiente, até as críticas devastadoras de Richard Roll e Benoit Mandelbrot que expuseram as limitações do modelo gaussiano, culminando nas abordagens pós-modernas como o modelo Black-Litterman.

| Dimensão Analítica | Paradigma Graham & Dodd (Pré-1952) | Paradigma Markowitz (Pós-1952) |
| --- | --- | --- |
| Unidade de Análise | Ativo Individual (Security) | Portfólio Agregado |
| Definição de Risco | Perda de Capital / Falência | Variância dos Retornos (Volatilidade) |
| Métrica de Valor | Valor Intrínseco (Fundamentalista) | Retorno Esperado (Estatístico) |
| Atitude perante Volatilidade | Oportunidade de compra (Margem de Segurança) | Custo a ser minimizado |
| Horizonte Temporal | Longo Prazo (convergência preço-valor) | Período Único (Single-Period Model) |

## 3. A Revolução de Markowitz: A Formalização da Diversificação

A publicação do artigo "Portfolio Selection" no *Journal of Finance* em março de 1952 marcou o "Big Bang" das finanças modernas. Harry Markowitz, então um jovem doutorando de 24 anos na Universidade de Chicago e pesquisador da Cowles Commission, introduziu uma estrutura matemática rigorosa para a seleção de ativos, desafiando a sabedoria convencional de que os investidores deveriam simplesmente maximizar o valor presente descontado dos retornos futuros.
Embora o artigo de 1952 tenha lançado as bases, foi o livro de Markowitz de 1959, *Portfolio Selection: Efficient Diversification of Investments*, que refinou a teoria para aplicação prática. Durante seu tempo na Cowles Commission em Yale (1955-1956), Markowitz desenvolveu o "Critical Line Algorithm" (Algoritmo da Linha Crítica). Este método permitia a derivação computacional precisa do conjunto de portfólios eficientes, resolvendo o problema de otimização quadrática sujeito a restrições lineares.
Foi também no trabalho de 1959 que Markowitz discutiu a distinção entre a "primeira etapa" do investimento (formação de crenças sobre o desempenho futuro baseadas em observação) e a "segunda etapa" (escolha do portfólio baseada nessas crenças), focando sua teoria exclusivamente na segunda.11 Ele também reconheceu, já naquela época, que medidas de risco alternativas como a semivariância poderiam ser teoricamente superiores à variância, pois os investidores tipicamente se preocupam apenas com a volatilidade negativa (*downside*), mas optou pela variância devido à tratabilidade computacional da época.
## 3. Risco, Retorno e Covariância: A Matemática da Diversificação

## Risco, Retorno e Covariância: A Matemática da Diversificação

## Retorno Esperado do Portfólio

## Variância e Covariância
Diferentemente do retorno, a variância do portfólio   não é linear. Ela depende crucialmente das **covariâncias** entre os ativos, capturando como os preços dos ativos se movem uns em relação aos outros. A fórmula da variância para um portfólio de  ativos é:

## O Papel da Correlação
A covariância  é o produto da correlação e dos desvios padrão . O coeficiente de correlação, variando entre -1 e +1, é o "motor" da diversificação:
**Correlação Perfeita (+1):** O risco do portfólio é a média ponderada dos riscos individuais. Não há benefício de diversificação.
**Correlação Inferior a 1:** O risco do portfólio será sempre menor que a média ponderada dos riscos individuais. A volatilidade idiossincrática é cancelada(HEBNER, 2022) .
**Correlação Negativa (-1):** Permite, teoricamente, a construção de um portfólio com variância zero (hedge perfeito).
A intuição de Markowitz foi quantificar que, ao combinar ativos com correlação imperfeita, o investidor reduz a exposição a riscos específicos (choques que afetam apenas uma empresa), mantendo apenas a exposição aos riscos comuns que afetam todo o sistema (MARKOWITZ, 1959).

No contexto da tese, a rede LSTM é treinada não apenas com preços passados, mas com um vetor de *features* rico que inclui os fatores Fama-French (SMB, HML), indicadores macroeconômicos (juros, inflação) e dados técnicos. A capacidade da LSTM de mapear essas interações não-lineares em uma previsão de retorno ($t+1$) fornece ao modelo Black-Litterman um vetor de Visões ($Q$) muito superior ao gerado por analistas humanos ou modelos lineares simples. A rede aprende, por exemplo, que em cenários de alta volatilidade (input GARCH), a correlação entre ativos muda, ajustando sua previsão de retorno de acordo.
## 3. Risco, Retorno e Covariância: A Matemática da Diversificação

### 3.1 Retorno Esperado do Portfólio

### 3.2 Variância e Covariância

### 3.3 O Papel da Correlação

O coeficiente de correlação ($\rho_{ij}$), que varia entre -1 e +1, é o determinante crítico da eficácia da diversificação.
Se $\rho_{ij} = 1$ (correlação positiva perfeita), não há benefício de redução de risco; o desvio padrão do portfólio é simplesmente a média ponderada dos desvios padrão dos ativos.
Se $\rho_{ij} < 1$, o desvio padrão do portfólio será menor que a média ponderada dos riscos individuais.
Se $\rho_{ij} = -1$ (correlação negativa perfeita), é teoricamente possível construir um portfólio com variância zero.
Portanto, a MPT estabelece que o objetivo da construção de portfólio não é apenas selecionar ativos com boas perspectivas de retorno, mas selecionar ativos cujos preços não se movam em uníssono. A covariância negativa ou baixa entre ativos é o "combustível" que permite a redução do risco total sem sacrificar necessariamente o retorno esperado.
A inovação seminal de Markowitz não foi a ideia de diversificação em si, mas a demonstração quantitativa de *como* e *por que* ela funciona. Ele provou que o risco de um portfólio é menor que a média ponderada dos riscos individuais de seus componentes, desde que os retornos dos ativos não sejam perfeitamente correlacionados positivamente.
A fórmula da variância do portfólio ($\sigma_p^2$) revelou o poder da covariância:
$$\sigma_p^2 = \sum_{i}w_i^2\sigma_i^2 + \sum_{i}\sum_{j \neq i}w_iw_j\sigma_i\sigma_j\rho_{ij}$$
Onde $\rho_{ij}$ é o coeficiente de correlação entre os ativos $i$ e $j$. A implicação profunda desta equação é que um ativo altamente arriscado (alta variância individual) pode, paradoxalmente, *reduzir* o risco total de um portfólio se tiver uma correlação negativa ou baixa com os outros ativos existentes na carteira.12 Isso mudou o foco da análise de investimento: a questão deixou de ser "quão arriscado é este ativo?" para "qual é a contribuição deste ativo para o risco total do portfólio?".
## 4. A Fronteira Eficiente e o Portfólio de Mínima Variância

## . A Fronteira Eficiente: Otimização e Geometria
## 
A aplicação dos princípios de média-variância a um universo de ativos resulta na construção da Fronteira Eficiente, o conjunto de todos os portfólios ótimos que dominam as demais alternativas.

## Derivação e Definição

A Fronteira Eficiente é o lugar geométrico no espaço risco-retorno que representa os portfólios que oferecem o retorno máximo para um dado nível de risco (ou risco mínimo para um dado retorno) (MARKOWITZ, 1959). Ela é obtida resolvendo um problema de otimização quadrática convexa (GUNDERSEN, 2022).

A forma geométrica exata desta fronteira depende criticamente das restrições impostas aos pesos :
**Sem Restrições a Vendas a Descoberto (Unconstrained/Short Selling Allowed):** Se o investidor pode vender a descoberto (assumir pesos negativos) ilimitadamente, a fronteira eficiente é uma **hipérbole** perfeita e suave no espaço média-desvio padrão (GUNDERSEN, 2022). O ramo superior desta hipérbole (acima do vértice) é a fronteira eficiente propriamente dita.
**Com Restrições a Vendas a Descoberto (No Short Selling Constraint):** Quando impomos a restrição de não-negatividade , a fronteira deixa de ser uma hipérbole única e torna-se uma curva convexa composta por uma série de **segmentos de hipérbole conectados** (*piecewise hyperbolic segments*) (GUNDERSEN, 2022).
*Mecanismo:* A transição de um segmento hiperbólico para outro ocorre nos "corner portfolios" (portfólios de canto). À medida que nos movemos ao longo da fronteira (aumentando o retorno esperado), a composição do portfólio muda. Quando o peso de um ativo atinge zero (sai do portfólio) ou quando um novo ativo entra no portfólio (peso torna-se positivo), a equação algébrica que descreve a curva muda, criando um "ponto de solda" entre dois arcos hiperbólicos distintos (QI, 2019).
*Implicação:* A fronteira com restrições é finita, começando no portfólio de mínima variância global e terminando no ativo individual de maior retorno (e risco), ao contrário da fronteira sem restrições que se estende ao infinito através da alavancagem de posições vendidas (GUNDERSEN, 2022).
O algoritmo desenvolvido por Markowitz para traçar essa fronteira complexa com restrições de desigualdade é o **Critical Line Algorithm (CLA)**, um método de otimização quadrática paramétrica que precede e inspira os modernos solvers de programação quadrática (MARKOWITZ, STARER, FRAM, GERBER, 2019).

## O Portfólio de Mínima Variância Global
##

O vértice da fronteira (seja ela hiperbólica ou segmentada) é o Portfólio de Mínima Variância Global (GMV). Este é o único ponto na curva onde o risco é minimizado em termos absolutos, sem consideração pelo retorno (KIM, BOYD, 2007). Em teoria, nenhum investidor racional avesso ao risco escolheria um portfólio localizado na parte "inferior" da fronteira (abaixo do GMV), pois para cada ponto nessa região existe um portfólio na parte superior com o mesmo risco, mas com retorno estritamente maior (dominância média-variância) (GUNDERSEN, 2022).

**Considerações sobre Taxas de Empréstimo Diferenciadas:** Na realidade, investidores raramente conseguem tomar empréstimos à mesma taxa livre de risco que o governo . Nesse cenário, a CML deixa de ser uma linha reta única e torna-se uma fronteira "quebrada" ou côncava: um segmento linear parte de  até um ponto de tangência, segue-se um segmento curvo da fronteira eficiente original (onde o investidor não empresta nem toma emprestado), e então um novo segmento linear parte de outro ponto de tangência com inclinação menor, baseada na taxa de empréstimo mais alta.
| Axioma | Definição Simplificada | Implicação Financeira |
| --- | --- | --- |
| Completude | Capacidade de ranquear qualquer par de ativos. | O mercado pode precificar todos os ativos. |
| Transitividade | Consistência lógica ($A>B, B>C \Rightarrow A>C$). | Evita arbitragem cíclica irracional. |
| Continuidade | Existência de "pontos de indiferença" probabilísticos. | Permite modelar o trade-off risco-retorno de forma contínua. |
| Independência | Preferências não mudam com opções irrelevantes. | A diversificação é consistente independentemente do resto da carteira. |
| Dominância | Preferência por "mais riqueza" e "menos risco". | Fundamenta a fronteira eficiente (ninguém escolhe portfólios dominados). |

A substituição da variância pela semivariância tem implicações profundas na construção de portfólios. Em distribuições simétricas (normais), a semivariância é proporcional à variância, e a fronteira eficiente da PMPT converge para a da MPT. No entanto, na presença de assimetria (skewness), as fronteiras divergem.
Um ativo com alta assimetria positiva (como uma opção de compra longa ou uma startup de venture capital) terá uma variância alta (devido ao potencial de ganho ilimitado) mas uma semivariância baixa (perda limitada ao capital investido). A MPT penalizaria este ativo, reduzindo sua alocação para diminuir o risco total. A PMPT, utilizando a semivariância, reconheceria o perfil favorável de risco/retorno e aumentaria a alocação, capturando o "upside potential".12 Estudos empíricos mostram que, em mercados emergentes ou durante crises, portfólios otimizados via semivariância tendem a preservar capital de forma mais eficiente do que aqueles baseados em média-variância.
**2.6 Fronteiras Eficientes: A Geometria da Assimetria**

A aplicação das métricas de PMPT altera a geometria da fronteira eficiente. Enquanto a fronteira eficiente da MPT (média-variância) é sempre uma hipérbole suave e convexa, a fronteira eficiente da PMPT (retorno-LPM ou retorno-CVaR) pode assumir formas irregulares e não-suaves, especialmente quando composta por ativos com distribuições heterogêneas (mistura de ativos normais e não-normais).
Em particular, a fronteira da PMPT tende a sugerir alocações mais concentradas em ativos com assimetria positiva e a evitar ativos com caudas esquerdas pesadas, mesmo que estes possuam alta média de retorno. Estudos recentes sobre criptoativos mostram que a otimização via PMPT resulta em portfólios com melhor proteção contra *drawdowns* severos do que a otimização via MPT, dado o perfil extremamente leptocúrtico desses ativos.
### Carteira de Mínima Variância Global (PMVG)

- **Fronteiras Eficientes: A Geometria da Assimetria**

### 2.2 A Fronteira Eficiente e a Geometria da Escolha Racional

O conceito de racionalidade na MPT é estritamente definido: um investidor racional é avesso ao risco e busca maximizar a sua utilidade. Isso implica que, para qualquer nível de risco, ele prefere o maior retorno possível, e para qualquer nível de retorno, ele prefere o menor risco possível. Ao projetar todas as combinações possíveis de ativos disponíveis no mercado (o Conjunto Viável ou *Feasible Set*) em um plano cartesiano de Risco (eixo X) versus Retorno (eixo Y), a região delimitada assume uma forma convexa característica, frequentemente descrita como uma "bala" ou um guarda-chuva.
A borda superior esquerda desse conjunto é denominada **Fronteira Eficiente**. Qualquer portfólio situado sobre esta linha é considerado ótimo no sentido de Pareto. Portfólios abaixo da fronteira são ineficientes, pois carregam risco desnecessário para o retorno oferecido. O ponto de inflexão, onde o risco é minimizado absolutamente, é o **Portfólio de Mínima Variância Global (PMVG)**. A seleção específica de um ponto ao longo da fronteira eficiente depende exclusivamente da tolerância ao risco do investidor individual (sua função de utilidade).
## 4. A Fronteira Eficiente: Otimização e Geometria

### 4.1 Derivação e Definição

### 4.2 O Portfólio de Mínima Variância Global

A aplicação dos princípios de média-variância a todo o universo de ativos disponíveis permite a construção do "conjunto de oportunidades de investimento". Dentro deste conjunto, Markowitz identificou um subconjunto ótimo de portfólios, conhecido como **Fronteira Eficiente**.
A Fronteira Eficiente é o locus geométrico dos portfólios que oferecem o máximo retorno esperado para cada nível de risco, ou o mínimo risco para cada nível de retorno esperado.5 Matematicamente, a fronteira é derivada resolvendo um problema de otimização quadrática: minimizar $\sigma_p^2$ sujeito a um retorno alvo fixo $E(R_p) = \mu$ e à restrição orçamentária $\sum w_i = 1$.
O resultado dessa otimização, quando plotado em um gráfico com o Risco (Desvio Padrão) no eixo horizontal e o Retorno Esperado no eixo vertical, forma uma curva côncava (hiperbólica no espaço média-desvio padrão).13 Todos os portfólios que se situam abaixo desta curva são considerados "ineficientes" ou "dominados", pois existe uma combinação alternativa de ativos que oferece um perfil risco-retorno superior.
O vértice esquerdo da hipérbole é denominado Portfólio de Mínima Variância Global (Global Minimum Variance Portfolio - GMVP). Este ponto representa a combinação de ativos que resulta no menor risco absoluto possível, independentemente do retorno.15 A Fronteira Eficiente compreende apenas o segmento da curva que parte do GMVP e se estende para cima e para a direita. O segmento inferior da hipérbole (abaixo do GMVP) é ineficiente, pois para qualquer ponto nesta região, existe um ponto na parte superior com o mesmo risco, mas maior retorno.
A curvatura da fronteira eficiente reflete o princípio dos retornos marginais decrescentes do risco: para obter incrementos adicionais de retorno esperado, o investidor deve aceitar incrementos cada vez maiores de risco.16 A localização ótima de um investidor específico ao longo desta fronteira, na ausência de um ativo livre de risco, seria determinada pela tangência entre a fronteira eficiente e as curvas de indiferença da função de utilidade do investidor, refletindo seu grau pessoal de aversão ao risco.
Um ativo livre de risco é definido teoricamente como um investimento com variância zero ($\sigma_{rf} = 0$) e, consequentemente, covariância zero com qualquer ativo de risco ($\sigma_{i,rf} = 0$).20 Na prática acadêmica e de mercado, títulos soberanos de curto prazo de economias estáveis (como *T-Bills* nos EUA ou *Tesouro Selic* no Brasil) são utilizados como *proxies* para este ativo.
A introdução deste ativo altera o conjunto de oportunidades de investimento. O investidor não está mais restrito à curva hiperbólica da fronteira eficiente de ativos de risco; ele pode agora combinar o ativo livre de risco com qualquer portfólio de ativos arriscados. Essa combinação gera uma relação linear entre risco e retorno.
A aplicação dos princípios de média-variância a um universo de ativos resulta na construção da Fronteira Eficiente, o conjunto de todos os portfólios ótimos que dominam as demais alternativas.

### 3.3. A Fronteira Eficiente e a Geometria da Escolha

O conceito central derivado desse arcabouço é a "Fronteira Eficiente". Ao plotar todas as combinações possíveis de ativos em um gráfico de Risco (eixo x) versus Retorno Esperado (eixo y), a borda superior esquerda do conjunto viável forma uma curva côncava. Qualquer portfólio situado sobre esta linha oferece o máximo retorno possível para um dado nível de risco. Portfólios abaixo da fronteira são ineficientes; portfólios acima são inatingíveis com os ativos disponíveis.13 A racionalidade do investidor é definida, portanto, pela seleção de um portfólio que resida nesta fronteira, de acordo com sua tolerância individual ao risco.
## 5. O Ativo Livre de Risco e o Teorema da Separação de Tobin

### O Ativo Livre de Risco e o Teorema da Separação
## 
## 
A introdução de um ativo livre de risco (*risk-free asset*) expande o conjunto de oportunidades do investidor além da fronteira de ativos de risco, alterando a geometria da escolha ótima e levando ao Teorema da Separação de Tobin.

### O Ativo Livre de Risco

Um ativo livre de risco é definido idealmente como um investimento com variância zero  e, consequentemente, covariância zero com todos os ativos de risco .34 Na prática financeira, títulos governamentais de curto prazo, como as *Treasury Bills* dos EUA, são utilizados como *proxies*, assumindo-se ausência de risco de crédito e risco de reinvestimento negligenciável para o horizonte de um período (ROHATGI, 2011).
A inclusão deste ativo permite duas novas operações financeiras fundamentais:
**Empréstimo Livre de Risco (Lending):** O investidor pode aplicar parte de sua riqueza no ativo livre de risco, reduzindo a exposição total ao risco do mercado.
**Tomada de Empréstimo Livre de Risco (Borrowing/Leverage):** O investidor pode tomar dinheiro emprestado à taxa livre de risco para alavancar sua posição nos ativos de risco.
## O Teorema da Separação de Tobin

James Tobin, em seu artigo seminal de 1958 *Liquidity Preference as Behavior Towards Risk*, formalizou o impacto do ativo livre de risco na teoria da escolha de portfólio.39 Tobin demonstrou que, na presença de um ativo livre de risco, o processo de decisão de investimento pode ser decomposto em duas etapas distintas e independentes — um resultado conhecido como o **Teorema da Separação** (ou *Two-Fund Separation Theorem*) (BUITER, 2003).
**Etapa 1: A Decisão Técnica (Seleção do Portfólio Ótimo de Risco).** O investidor deve primeiro identificar o portfólio de ativos de risco que maximiza o retorno por unidade de risco. Geometricamente, este é o **Portfólio de Tangência** (Tangency Portfolio), o ponto onde uma linha reta partindo da taxa livre de risco   tangencia a fronteira eficiente hiperbólica dos ativos de risco (GUNDERSEN, 2022). A composição deste portfólio é puramente técnica e objetiva, dependendo apenas das estimativas de médias, variâncias e covariâncias; ela é *independente* das preferências de risco do investidor individual.
**Etapa 2: A Decisão Pessoal (Alocação de Capital).** Uma vez identificado o Portfólio de Tangência, o investidor decide como alocar sua riqueza total entre este portfólio e o ativo livre de risco. Esta decisão depende inteiramente da função de utilidade (aversão ao risco) do indivíduo.
O CAPM foi desenvolvido independentemente na primeira metade da década de 1960 por William Sharpe , John Lintner , Jan Mossin  e Jack Treynor (1961/1962) (FAMA, FRENCH, 2004). A unificação dessas teorias rendeu a Sharpe, Markowitz e Merton Miller o Prêmio Nobel de Economia em 1990 (garvin, 2013). A intuição central é que, se todos os investidores são racionais, possuem expectativas homogêneas e otimizam seus portfólios segundo a média-variância (usando o Teorema da Separação de Tobin), então todos demandarão o mesmo portfólio de ativos de risco: o **Portfólio de Mercado** . Para que o mercado "limpe" (oferta iguale demanda), os preços dos ativos devem se ajustar até que o portfólio de tangência seja, de fato, o portfólio de mercado ponderado por valor (FAMA, FRENCH, 2004).

### O Ativo Livre de Risco e o Teorema da Separação

A introdução de um ativo livre de risco (*risk-free asset*) expande o conjunto de oportunidades do investidor além da fronteira de ativos de risco, alterando a geometria da escolha ótima e levando ao Teorema da Separação de Tobin.

Um avanço crucial foi a introdução do Ativo Livre de Risco ($R_f$), teoricamente representado por títulos do governo de curto prazo. James Tobin, em 1958, demonstrou o Teorema da Separação, que postula que a tarefa de investimento pode ser decomposta em duas decisões independentes:
**A Decisão Técnica:** Identificar o portfólio ótimo de ativos de risco. Na presença de um ativo livre de risco que pode ser emprestado ou tomado emprestado, a fronteira eficiente deixa de ser uma curva e torna-se uma linha reta tangente à fronteira de Markowitz. Esta linha é a **Reta do Mercado de Capitais (CML)**. O ponto de tangência é o **Portfólio de Mercado**.
**A Decisão de Alocação:** O investidor decide quanto de sua riqueza alocar no Portfólio de Mercado e quanto manter no Ativo Livre de Risco, baseando-se na sua preferência pessoal.
Isso implica que todos os investidores racionais devem deter a mesma composição relativa de ativos de risco (o mercado inteiro), variando apenas a alavancagem. Esta é a fundação teórica da indústria de fundos de índice passivos.
## 5. O Ativo Livre de Risco e o Teorema da Separação

### 5.1 O Ativo Livre de Risco

### 5.2 O Teorema da Separação de Tobin

Este capítulo consolidou os fundamentos teóricos necessários para a análise subsequente. A transição do paradigma de seleção de ações de Williams para a alocação de ativos baseada em covariância de Markowitz, refinada pela separação de Tobin e pelo modelo de equilíbrio do CAPM, constitui a base da moderna gestão financeira. Estes conceitos fornecem a linguagem e as métricas essenciais para a construção, análise e avaliação de portfólios de investimento no contexto contemporâneo.
# Capítulo 1: Fundamentação Teórica e Revisão Bibliográfica da Moderna Teoria do Portfólio

A estrutura original de Markowitz considerava apenas ativos com risco. Em 1958, James Tobin expandiu significativamente a teoria ao introduzir o conceito de um ativo livre de risco (*risk-free asset*) e analisar suas implicações para a escolha de portfólio.
A contribuição mais profunda de Tobin foi o **Teorema da Separação**. Este teorema postula que a decisão de investimento pode ser decomposta em dois passos distintos e independentes 18:
**A Decisão Técnica (Otimização):** Identificar o portfólio ótimo de ativos de risco. Este portfólio é o ponto onde uma linha reta partindo da taxa livre de risco ($R_f$) tangencia a fronteira eficiente de Markowitz. Este portfólio de tangência é conhecido como o **Portfólio de Mercado** e é puramente determinado pelas estatísticas dos ativos (retornos, variâncias, covariâncias), sendo independente das preferências de risco do investidor.
**A Decisão de Alocação (Preferência):** Uma vez identificado o Portfólio de Mercado, o investidor decide como dividir seu capital entre este portfólio arriscado e o ativo livre de risco. Investidores conservadores alocarão uma grande parte em ativos livres de risco e uma pequena parte no portfólio de mercado; investidores agressivos podem até tomar emprestado à taxa livre de risco (alavancagem) para investir mais de 100% de seu capital no portfólio de mercado.
Um ativo livre de risco é definido idealmente como um investimento com variância zero ($\sigma_{rf}^2 = 0$) e, consequentemente, covariância zero com todos os ativos de risco ($\sigma_{i,rf} = 0$).34 Na prática financeira, títulos governamentais de curto prazo, como as *Treasury Bills* dos EUA, são utilizados como *proxies*, assumindo-se ausência de risco de crédito e risco de reinvestimento negligenciável para o horizonte de um período.
A inclusão deste ativo permite duas novas operações financeiras fundamentais:
**Empréstimo Livre de Risco (Lending):** O investidor pode aplicar parte de sua riqueza no ativo livre de risco, reduzindo a exposição total ao risco do mercado.
**Tomada de Empréstimo Livre de Risco (Borrowing/Leverage):** O investidor pode tomar dinheiro emprestado à taxa livre de risco para alavancar sua posição nos ativos de risco.
| Texto Original (do ) | Problema Identificado | Sugestão de Revisão e Justificativa |
| --- | --- | --- |
| "Apesar do avanço, observou-se também uma queda no saldo mediano em custódia — de R$ 7 mil para R$ 3 mil... — sugerindo a entrada de pequenos investidores..." | Coesão / Pontuação | "Apesar do avanço, observou-se também uma queda no saldo mediano em custódia (de R$ 7 mil para R$ 3 mil...), o que sugere a entrada de pequenos investidores..." Justificativa: O uso de travessões (—) é menos formal que parênteses () para intercalar dados em texto corrido. O gerúndio "sugerindo" é substituído por "o que sugere", uma oração adjetiva explicativa que oferece melhor coesão. |
| "...muitos dos quais sem conhecimento técnico profundo sobre gestão de portfólios." | Vocabulário / Preposição | "...muitos dos quais sem conhecimento técnico aprofundado em gestão de portfólios." Justificativa: "Aprofundado" é um termo mais formal. A regência de "conhecimento" é mais precisa com a preposição "em" ou "de" do que "sobre" neste contexto. |
| "Diante desse panorama, este trabalho busca responder à seguinte questão de pesquisa: q ual é o impacto..." | Formatação / Gramática | "Diante desse panorama, este trabalho busca responder à seguinte questão de pesquisa: Qual é o impacto..." Justificativa: Erro de formatação ("q ual") e uso de minúscula após dois-pontos que introduzem uma citação direta (a pergunta). A primeira letra da pergunta deve ser maiúscula.1 |
| "Um ativo livre de risco é aquele que oferece ao investidor a certeza do retorno esperado, resultando em um risco-variância igual a zero..." | Terminologia (Semântica) | "Um ativo livre de risco é aquele que oferece ao investidor a certeza do retorno esperado, resultando em uma variância (risco) dos retornos igual a zero..." Justificativa: Conforme 1, "risco-variância" é uma terminologia redundante no contexto da MPT, onde a variância é a métrica de risco. A correção clarifica o conceito. (Nota: O sobrenome "Reily" está grafado incorretamente no original, devendo ser "Reilly" 1). |
| "A metodologia Média-Variância possui duas premissas básicas: a normalidade das distribuições dos retornos dos ativos e que as funções de utilidade... são quadráticas." | Gramática (Paralelismo) | "A metodologia Média-Variância possui duas premissas básicas:  a normalidade das distribuições dos retornos dos ativos e  a suposição de que as funções de utilidade... são quadráticas." Justificativa: Quebra de paralelismo estrutural.1 O primeiro item da lista é um substantivo ("a normalidade"), enquanto o segundo é uma oração ("que as funções..."). A correção padroniza a lista (substantivo + substantivo). |

### 4.1. O Teorema da Separação de Tobin

Um elo crucial entre a MPT e o CAPM foi o trabalho de James Tobin. Em 1958, Tobin introduziu o "Teorema da Separação de Dois Fundos". Ele demonstrou que, na presença de um ativo livre de risco, a tarefa de alocação de ativos pode ser decomposta em duas decisões independentes:
**A Decisão Técnica:** Identificar o portfólio ótimo de ativos de risco. Em um mercado eficiente, este é o "Portfólio de Mercado" (tangente à fronteira eficiente).
**A Decisão Pessoal:** Determinar a alocação entre este portfólio de risco e o ativo livre de risco, baseando-se exclusivamente na preferência de risco (utilidade) do investidor.
Este teorema implica que todos os investidores racionais, independentemente de sua aversão ao risco, deveriam deter a mesma proporção relativa de ativos de risco. A única diferença entre um investidor conservador e um agressivo seria a quantidade de capital alocada ao ativo livre de risco (emprestando dinheiro ao governo) versus o portfólio de mercado (ou tomando dinheiro emprestado para alavancar essa posição).
## 6. A Reta do Mercado de Capitais (CML) e o Índice de Sharpe

Os slides da "Lecture 05" 1 servem como um roteiro teórico perfeito para justificar a pergunta de pesquisa do TCC.1 Eles constroem a exata progressão lógica necessária para a fundamentação teórica.
O Ponto de Partida (Markowitz M-V)
Os slides iniciam definindo o problema clássico de Média-Variância (M-V) de Markowitz. Eles estabelecem a matemática da otimização para $N$ ativos arriscados, incluindo a derivação das primeiras condições de ordem (FOC) para encontrar os pesos da carteira ($w_p$).1 Crucialmente, eles introduzem o ativo livre de risco, o que lineariza a fronteira eficiente, criando a Reta do Mercado de Capitais (CML).1 O portfólio de tangência nesta reta é identificado como o "Portfólio com o maior sharp ratio" (Índice de Sharpe).
**Contribuição ao TCC:** Esta seção valida diretamente a metodologia do TCC 1, que define o "Portfólio de Markowitz" a ser montado como a "Carteira de Máximo Índice de Sharpe". Os slides fornecem o fundamento teórico exato para essa escolha.
A Justificativa do Problema (Erro de Estimação)
Os slides, em alinhamento direto com o referencial teórico do TCC 1, identificam a falha crítica deste modelo: os inputs.
A Seção 3, "Estimating Mean and Co-Variance" 1, é notavelmente contundente. Ao discutir a estimação do "Mean return (drift)" usando dados históricos, o slide afirma que a "Estimação é muito imprecisa!" (Estimation is very imprecise!).
A Seção 4, "Black-Litterman Model" 1, aprofunda essa crítica, explicando *por que* os dados históricos são estimadores ruins. O modelo M-V clássico ignora "priors estatísticos" e "priors econômicos".1 Um setor com um retorno passado atipicamente alto seria, pela M-V, assumido como tendo o mesmo retorno alto no futuro. O modelo atribui incorretamente o que poderia ser "sorte" como uma característica persistente.
**Contribuição ao TCC:** Esta é a justificativa *central* para a pergunta de pesquisa do TCC. Os slides 1 fornecem uma base teórica robusta para a Seção 2.11 do TCC 1, que cita DeMiguel e Nogales  e a natureza do otimizador M-V como um "maximizador de erros".
A Solução Teórica (Black-Litterman)
Os slides 1 não param na crítica; eles apresentam a solução. O Modelo Black-Litterman (BL) é introduzido como o framework que resolve o problema dos inputs.
O modelo BL o faz através de uma síntese Bayesiana:
**O "Prior" ($\Pi$):** O modelo não começa do zero. Ele começa com um "bom ponto de partida" 1, que é o "Black Litterman Prior".1 Este "prior" ($\Pi$) é o vetor de retornos de equilíbrio de mercado, derivado do CAPM (ou seja, retornos proporcionais ao risco sistemático, $\beta$).1 A fórmula específica é dada como o prêmio de risco de equilíbrio: $\Pi = \gamma \Sigma w^{eq}$ 1, onde $\gamma$ é o coeficiente de aversão ao risco, $\Sigma$ é a matriz de covariância e $w^{eq}$ são os pesos de equilíbrio do mercado (por exemplo, capitalização de mercado).
**As "Visões" ($Q$):** O modelo, então, *ajusta* este "prior" de equilíbrio com base nas "visões" (views) do investidor.1 Essas "visões" são precisamente as previsões que o TCC 1 está gerando com ARIMA e LSTM. As visões são expressas na forma $P\mu = Q + \epsilon_v$ 1, onde $P$ é uma matriz que identifica os ativos na visão, $Q$ é o vetor de retornos esperados para essas visões, e $\Omega$ (a variância de $\epsilon_v$) é a matriz de confiança nessas visões.
A Síntese (Posterior): A "Master Formula" Bayesiana (o retorno "posterior") é apresentada na página 38 1:
$E =^{-1}$
**Contribuição ao TCC:** Esta fórmula 1 é a *conexão crítica* que o TCC pode explorar. Ela mostra analiticamente como *combinar* o "prior" de equilíbrio ($\Pi$, derivado de dados históricos/mercado) com a "visão" preditiva ($Q$, derivada dos modelos ARIMA/LSTM), ponderada pela confiança ($\tau$ e $\Omega$). Esta é a solução teórica para o problema que o TCC identifica.

Em sua obra de 1959, Markowitz dedicou um capítulo para discutir uma medida alternativa de risco: a **semivariância** (ESTRADA, 2007). A semivariância mensura apenas a dispersão dos retornos que caem abaixo de um determinado alvo (como a média ou zero), ignorando a volatilidade "positiva" (ganhos acima do esperado) " (MARKOWITZ, 1959). Markowitz reconheceu explicitamente a superioridade teórica desta medida, afirmando que "a semivariância parece mais plausível do que a variância como uma medida de risco, uma vez que se preocupa apenas com desvios adversos" (MARKOWITZ, 1990). Investidores racionais não temem ganhos inesperados; eles temem perdas.
No entanto, Markowitz optou pela variância baseada em critérios de "custo, conveniência e familiaridade" (ESTRADA, 2007).
**Custo Computacional:** Na era dos mainframes primitivos e cartões perfurados, o custo de computação era uma barreira formidável. A otimização baseada na variância envolvia álgebra linear padrão e inversão de matrizes covariância, operações para as quais existiam algoritmos eficientes (como o *Critical Line Algorithm* desenvolvido pelo próprio Markowitz) (MARKOWITZ, STARER, FRAM, GERBER, 2019 ). A semivariância, por outro lado, exigia o dobro de dados de entrada (matrizes de semicovariância) e resultava em problemas de otimização mais complexos, onde a matriz de covariância se tornava endógena aos pesos do portfólio (ESTRADA, 2007).
**Convenência Analítica:** Se os retornos dos ativos seguirem uma distribuição normal (simétrica), a média e a variância são estatísticas suficientes para descrever toda a distribuição. Nesse caso específico, minimizar a variância é matematicamente equivalente a minimizar a semivariância (ESTRADA, 2007). Markowitz apostou na aproximação normal como uma simplificação aceitável para tornar a teoria operacionalizável.
Apesar de Markowitz ter sugerido que a semivariância seria preferível com o aumento do poder computacional, a variância entrincheirou-se como o padrão da indústria, moldando décadas de teoria financeira, desde o Índice de Sharpe até o modelo Black-Scholes (ESTRADA, 2007).

## A Reta do Mercado de Capitais (Capital Market Line - CML)

A combinação linear do ativo livre de risco com o Portfólio de Tangência gera a **Reta do Mercado de Capitais** (Capital Market Line - CML). A CML torna-se a *nova* fronteira eficiente, pois domina qualquer portfólio situado na fronteira original de ativos de risco (a hipérbole fica inteiramente abaixo da reta CML, exceto no ponto de tangência).
O posicionamento do investidor ao longo da CML é determinado pelo mecanismo de alavancagem:
**Investidores Conservadores (Lending Portfolios):** Localizam-se à esquerda do ponto de tangência . Eles investem uma fração positiva de sua riqueza no ativo livre de risco e o restante no portfólio . O risco total do portfólio é menor que o risco de .
**Investidores Agressivos (Borrowing Portfolios):** Localizam-se à direita do ponto de tangência . Eles tomam empréstimos à taxa  para investir mais de 100% de seu capital próprio no portfólio  ampliando tanto o retorno esperado quanto a volatilidade.
A equação que descreve a CML é:

## Avaliação de Desempenho: O Índice de Sharpe

A geometria da CML forneceu a base direta para uma das métricas mais onipresentes na avaliação de investimentos: o Índice de Sharpe. Introduzido por William Sharpe em 1966 como "Reward-to-Variability Ratio", o índice operacionaliza o conceito de eficiência média-variância.
O Índice de Sharpe  quantifica o excesso de retorno por unidade de risco total. Matematicamente:

Geometricamente, o Índice de Sharpe de um portfólio é a inclinação da linha que conecta a taxa livre de risco a esse portfólio no gráfico média-desvio padrão (GUNDERSEN, 2022). Quanto maior a inclinação, melhor o desempenho ajustado ao risco.

A maximização do Índice de Sharpe é equivalente a encontrar o Portfólio de Tangência na MPT. Em um mercado em equilíbrio, o portfólio de mercado  deve ser aquele com o maior Índice de Sharpe possível (GUIDOLIN, 2017). A métrica permite comparar fundos e estratégias heterogêneas, nivelando o campo de jogo ao penalizar a volatilidade. No entanto, o índice herda as limitações da variância: se os retornos não forem normais (ex: fundos de hedge com estratégias de opções), o Índice de Sharpe pode ser enganoso, penalizando a volatilidade positiva ou subestimando riscos de cauda, o que levou ao desenvolvimento de métricas alternativas como o **Índice de Sortino** (baseado na semivariância/downside deviation) (DUBRA, MACCHERONI, 2004).

- **Diferença entre CML e SML:**

**Tabela 1: Comparação entre Capital Market Line (CML) e Security Market Line (SML)**

A MPT assume que os retornos dos ativos financeiros são variáveis aleatórias independentes e identicamente distribuídas (i.i.d.) que seguem uma distribuição normal (Gaussiana). Esta suposição é conveniente porque uma distribuição normal é perfeitamente descrita por apenas dois parâmetros: média ($\mu$) e desvio padrão ($\sigma$). Sob esta ótica, a probabilidade de eventos extremos diminui exponencialmente à medida que nos afastamos da média.
No entanto, evidências empíricas exaustivas demonstram que as séries temporais financeiras exibem características que violam sistematicamente a normalidade:
**Leptocurtose**** (Caudas Gordas):** Os mercados financeiros apresentam uma frequência de eventos extremos (tanto positivos quanto negativos) significativamente maior do que a prevista pela distribuição normal. Eventos de "seis sigmas" ($6\sigma$), que teoricamente deveriam ocorrer uma vez a cada milhões de anos, ocorrem com uma regularidade alarmante em crises financeiras.
**Assimetria (****Skewness****):** Os retornos não são simétricos. Em mercados de ações, por exemplo, observa-se frequentemente uma assimetria negativa, onde as quedas são mais abruptas e profundas do que as altas.
Implicação para a Gestão de Portfólio:
Ao utilizar o desvio padrão como medida de risco, a MPT falha em distinguir entre a volatilidade gerada por "saltos" positivos e a volatilidade gerada por "crashes". Mais grave ainda, a MPT subestima o risco de cauda. Um fundo de hedge que opera estratégias de venda de opções fora do dinheiro pode apresentar um desvio padrão baixo e um Índice de Sharpe alto durante longos períodos de calmaria, ocultando um risco latente de ruína que só é capturado por métricas que consideram a curtose e a assimetria, como preconizado pela PMPT.23 A PMPT, ao não assumir normalidade, permite o uso de distribuições mais flexíveis ou métodos não paramétricos que capturam a verdadeira natureza do risco de cauda.
A PMPT não se limita a medir o risco; ela redefine a avaliação de desempenho. O onipresente Índice de Sharpe, ao penalizar a volatilidade de alta, falha em capturar o valor gerado por gestores que produzem assimetria positiva. A PMPT propõe alternativas que integram os conceitos de *downside* *risk* e momentos superiores.

Desenvolvido por Frank Sortino no início dos anos 1980 e popularizado nos anos 1990, o Índice de Sortino é a modificação mais direta e amplamente adotada do Índice de Sharpe.13 Ele substitui o desvio padrão total pelo **Desvio de ****Downside** ($TDD$ ou $\sigma_d$) no denominador.

A fronteira atual da pesquisa em PMPT reside na sua integração com a Inteligência Artificial. Publicações e estudos de 2024 e 2025 indicam uma tendência crescente no uso de algoritmos de **Machine Learning**, como redes neurais recorrentes (LSTM) e Deep Learning, para estimar dinamicamente os Momentos Parciais Inferiores e otimizar portfólios.
Ao contrário dos modelos estáticos tradicionais que dependem de dados históricos passados, modelos híbridos (PMPT + ML) conseguem prever mudanças nos regimes de volatilidade e na forma das caudas (*tail* *risk* *forecasting*), ajustando as alocações em tempo real para minimizar o CVaR futuro. Essa abordagem, denominada "Otimização Robusta Dinâmica", supera as limitações da MPT e da PMPT clássica, oferecendo resultados superiores em *backtests* e aplicações reais, especialmente em mercados voláteis e durante transições de regime econômico.
Além disso, a PMPT tem sido fundamental na integração de critérios ESG (Environmental, Social, and Governance) na gestão de portfólios. Estudos recentes sugerem que o uso de métricas de *downside* *risk* como o Índice de Sortino revela melhor o perfil de risco ajustado de empresas com altas pontuações ESG, que tendem a ter menor risco de cauda (menor risco reputacional e regulatório) do que empresas convencionais, algo que o Índice de Sharpe muitas vezes falha em capturar.
Baseada na Teoria Moderna do Portifólio, busca maximizar o índice de Sharpe. Ela assume a normalidade dos retornos e utiliza a variância como medida de risco.

Ao utilizar o desvio padrão como medida de risco, a MPT falha em distinguir entre a volatilidade gerada por "saltos" positivos e a volatilidade gerada por "crashes". Mais grave ainda, a MPT subestima o risco de cauda. Um fundo de hedge que opera estratégias de venda de opções fora do dinheiro pode apresentar um desvio padrão baixo e um Índice de Sharpe alto durante longos períodos de calmaria, ocultando um risco latente de ruína que só é capturado por métricas que consideram a curtose e a assimetria, como preconizado pela PMPT. Esta, ao não assumir normalidade, permite o uso de distribuições mais flexíveis ou métodos não paramétricos que capturam a verdadeira natureza do risco de cauda.

A história da teoria moderna de gestão de carteiras não é apenas uma sucessão de fórmulas matemáticas, mas uma evolução contínua na compreensão humana sobre a natureza do risco e a incerteza dos mercados financeiros. Este relatório apresenta uma análise exaustiva e crítica desse arco evolutivo, iniciando-se nos fundamentos estabelecidos por Harry Markowitz com a Teoria Moderna de Portfólio (MPT), atravessando as críticas que deram origem à Teoria Pós-Moderna de Portfólio (PMPT) e ao modelo de Desvio Absoluto Médio (MAD), e culminando na integração bayesiana de visões subjetivas através do modelo Black-Litterman. O ápice desta análise reside na fronteira contemporânea, onde a econometria clássica (ARIMA, GARCH) e as arquiteturas de *Deep Learning* (Redes Neurais LSTM) convergem para gerar os *inputs* necessários para a otimização de portfólios, criando uma síntese entre o raciocínio econômico humano e o reconhecimento de padrões computacional.
A premissa central que guia esta investigação é a busca incessante pela robustez matemática. A dependência inicial da variância como *proxy* única para o risco foi desafiada pela distribuição não normal (não gaussiana) dos retornos dos ativos, fenômeno conhecido como leptocurtose ou "caudas gordas". Isso exigiu o desenvolvimento de medidas de risco de *downside* (PMPT) e abordagens de programação linear robusta (MAD). Simultaneamente, a sensibilidade extrema da otimização Média-Variância a pequenos erros nos *inputs* necessitou de uma abordagem bayesiana (Black-Litterman) para estabilizar os pesos dos ativos. Finalmente, as "visões" exigidas pelo modelo Black-Litterman — originalmente opiniões subjetivas de analistas — estão agora sendo rigorosamente derivadas de modelos de previsão de séries temporais, fechando o ciclo de um sistema quantitativo autônomo.
A relevância deste estudo é amplificada pelo contexto atual de alta volatilidade e complexidade dos mercados, onde modelos tradicionais frequentemente falham em proteger o capital do investidor. Ao examinar a literatura acadêmica e empírica, observa-se que a combinação de técnicas de aprendizado de máquina com estruturas de alocação teóricas robustas oferece um desempenho superior ajustado ao risco, medido não apenas pelo Índice de Sharpe, mas por métricas mais resilientes como o MAD e o Índice Sortino.
#### 2.3.1 O Teorema da Separação e a Reta do Mercado de Capitais (CML)

### 4.2 O Índice de Sortino vs. Índice de Sharpe

Como consequência direta da adoção da semi-variância, a métrica de avaliação de desempenho evolui do Índice de Sharpe para o Índice de Sortino:

### 5.3 A Reta do Mercado de Capitais (Capital Market Line - CML)

## 6. Avaliação de Desempenho: O Índice de Sharpe

### Tabela Resumo: Comparação entre CML e SML

A linha reta que conecta a taxa livre de risco ao Portfólio de Mercado na fronteira eficiente é denominada **Capital Market Line (CML)**. A CML representa a nova fronteira eficiente na presença de um ativo sem risco. Todos os investidores racionais devem situar seus portfólios sobre esta reta.
A equação da CML é dada por:
$$E(R_p) = R_f + \sigma_p \left$$
O termo entre colchetes representa o preço de mercado do risco: o retorno excedente que o mercado paga por unidade de risco total ($\sigma$). A CML demonstra que o retorno esperado de um portfólio eficiente é composto pela taxa livre de risco mais um prêmio pelo risco total assumido.20 Portfólios que estão na fronteira eficiente original de Markowitz (mas abaixo da CML) tornam-se subótimos, pois a combinação linear oferecida pela CML proporciona um retorno superior para o mesmo nível de risco.
A consolidação da CML e da importância do trade-off entre risco e retorno criou a necessidade de métricas padronizadas para comparar o desempenho de diferentes investimentos. Em 1966, William F. Sharpe introduziu o "reward-to-variability ratio", hoje universalmente conhecido como **Índice de Sharpe**.
O Índice de Sharpe mensura o excesso de retorno de um portfólio sobre a taxa livre de risco, normalizado pelo seu risco total (desvio padrão). A fórmula é expressa como:

$$S_p = \frac{E(R_p) - R_f}{\sigma_p}$$
Geometricamente, o Índice de Sharpe corresponde à inclinação da reta que conecta a taxa livre de risco ao portfólio analisado no plano risco-retorno. O Portfólio de Mercado (o ponto de tangência da CML) é, por definição, o portfólio que possui o maior Índice de Sharpe possível entre todas as combinações de ativos de risco.
Esta métrica revolucionou a avaliação de gestores de fundos. Antes do Índice de Sharpe, comparavam-se fundos apenas pelos seus retornos absolutos. Sharpe mostrou que um retorno mais alto não implica necessariamente uma gestão superior se foi obtido através da exposição a níveis desproporcionais de risco. O índice permite "ajustar pelo risco" os retornos, nivelando o campo de jogo e permitindo comparações justas entre estratégias conservadoras e agressivas.21 Um índice de Sharpe elevado indica que o investidor está sendo eficientemente recompensado por cada unidade de volatilidade suportada.

A decisão de Markowitz de utilizar a variância (ou desvio padrão) como a medida universal de risco foi uma das escolhas mais consequentes na história das finanças, ditada tanto por conveniência matemática quanto por restrições computacionais da década de 1950.
Em sua obra de 1959, Markowitz dedicou o Capítulo 9 para discutir uma medida alternativa de risco: a **semivariância**.12 A semivariância mensura apenas a dispersão dos retornos que caem abaixo de um determinado alvo (como a média ou zero), ignorando a volatilidade "positiva" (ganhos acima do esperado). Markowitz reconheceu explicitamente a superioridade teórica desta medida, afirmando que "a semivariância parece mais plausível do que a variância como uma medida de risco, uma vez que se preocupa apenas com desvios adversos".14 Investidores racionais não temem ganhos inesperados; eles temem perdas.
No entanto, Markowitz optou pela variância baseada em critérios de "custo, conveniência e familiaridade".
**Custo Computacional:** Na era dos mainframes primitivos e cartões perfurados, o custo de computação era uma barreira formidável. A otimização baseada na variância envolvia álgebra linear padrão e inversão de matrizes covariância, operações para as quais existiam algoritmos eficientes (como o *Critical Line Algorithm* desenvolvido pelo próprio Markowitz).18 A semivariância, por outro lado, exigia o dobro de dados de entrada (matrizes de semicovariância) e resultava em problemas de otimização mais complexos, onde a matriz de covariância se tornava endógena aos pesos do portfólio.
**Convenência Analítica:** Se os retornos dos ativos seguirem uma distribuição normal (simétrica), a média e a variância são estatísticas suficientes para descrever toda a distribuição. Nesse caso específico, minimizar a variância é matematicamente equivalente a minimizar a semivariância.12 Markowitz apostou na aproximação normal como uma simplificação aceitável para tornar a teoria operacionalizável.
Apesar de Markowitz ter sugerido que a semivariância seria preferível com o aumento do poder computacional, a variância entrincheirou-se como o padrão da indústria, moldando décadas de teoria financeira, desde o Índice de Sharpe até o modelo Black-Scholes.
O Índice de Sharpe ($S_p$) quantifica o excesso de retorno por unidade de risco total. Matematicamente:

$$S_p = \frac{E(R_p) - R_f}{\sigma_p}$$
Geometricamente, o Índice de Sharpe de um portfólio é a inclinação da linha que conecta a taxa livre de risco a esse portfólio no gráfico média-desvio padrão.25 Quanto maior a inclinação, melhor o desempenho ajustado ao risco.

A maximização do Índice de Sharpe é equivalente a encontrar o Portfólio de Tangência na MPT. Em um mercado em equilíbrio, o portfólio de mercado ($M$) deve ser aquele com o maior Índice de Sharpe possível.38 A métrica permite comparar fundos e estratégias heterogêneas, nivelando o campo de jogo ao penalizar a volatilidade. No entanto, o índice herda as limitações da variância: se os retornos não forem normais (ex: fundos de hedge com estratégias de opções), o Índice de Sharpe pode ser enganoso, penalizando a volatilidade positiva ou subestimando riscos de cauda, o que levou ao desenvolvimento de métricas alternativas como o **Índice de Sortino** (baseado na semivariância/downside deviation).
$$E(R_i) = R_f + \beta_i$$
A SML difere fundamentalmente da CML. Enquanto a CML (usando $\sigma$) aplica-se apenas a portfólios eficientes (que não possuem risco não sistemático), a SML (usando $\beta$) aplica-se a *qualquer* ativo individual ou portfólio, eficiente ou não, precificando-os de acordo com sua contribuição marginal ao risco do portfólio de mercado.
**Tabela 1: Comparação entre Capital Market Line (CML) e Security Market Line (SML)**

Status : A metodologia atual é vaga, desalinhada (fala em TMPT) e o critério de amostragem é fraco. É necessário detalhar o *processo quantitativo* de forma replicável.
**3.1. Tipo de Pesquisa**
(Reescrever): Esta pesquisa é classificada como **quantitativa**, **descritiva** e **aplicada**. Utiliza-se da **modelagem e simulação** (*backtesting*) como principal técnica de análise de dados.
**3.2. Definição da Amostra e Coleta de Dados**
Qual será o **Universo**? (Ações do IBOVESPA? IBrA-100?).
Qual será o **Período de Análise**? (Justificar o período 2010-2024).
Quais os **Critérios de Inclusão/Filtro**? (Substituir o critério "volume > 0" 1 por critérios rigorosos. Sugestão: "Ações que compuseram o IBrA-100 em pelo menos 80% dos meses do período de análise" ou "Ações com volume médio diário de negociação acima de R$ X").
Qual a **Fonte dos Dados**? (Economática 1, Profit? Yahoo Finance?).
Qual a **Frequência dos Dados**? (Diários? Semanais? Mensais?). (Sugestão: Diários).
Como os dados serão **Tratados**? (Cálculo dos retornos logarítmicos? Ajuste de dividendos e *splits*?).
**3.3. Desenho Experimental (A Estratégia de *****Backtest*****)**
Esta é a seção mais importante que falta.
Será utilizada uma **Janela Deslizante (*****Rolling Window*****)** ou **Janela Expansível (*****Expanding Window*****)**? (Justificar a escolha).
Qual o **Tamanho da Janela de Treino**? (Ex: 60 meses / 1250 dias de pregão).
Qual o **Período de Teste/Previsão**? (Ex: prever o $\mu$ para o próximo 1 mês / 21 dias).
Qual a **Frequência de Rebalanceamento** da carteira? (Mensal? Trimestral?). (Justificar. Ex: Mensal, para capturar as novas previsões dos modelos sem gerar custos de transação excessivos).
**3.4. Modelagem dos *****Inputs***** (As Três Carteiras)**
Para cada período de rebalanceamento no *backtest*, como os *inputs* (Retorno $\mu$ e Matriz de Covariância $\Sigma$) serão calculados?
**Cálculo da Matriz de Covariância ($\Sigma$)**: Será a mesma para todas as carteiras? (Sugestão: Sim, usar a covariância histórica da Janela de Treino. O foco do TCC é no $\mu$).
**Cálculo do Vetor de Retorno Esperado ($\mu$)**:
**Carteira 1 (Baseline - Média Histórica):** O $\mu$ de cada ativo será a média aritmética simples dos retornos na Janela de Treino.
**Carteira 2 (ARIMA):** Para cada ativo, um modelo ARIMA(p,d,q) será ajustado aos dados da Janela de Treino (Como p,d,q serão escolhidos? Auto-ARIMA?). O modelo fará uma previsão *out-of-sample* para o Período de Teste. O $\mu$ será essa previsão.
**Carteira 3 (LSTM):** Para cada ativo, um modelo LSTM será treinado na Janela de Treino (Definir a arquitetura: quantas camadas? neurônios? *lookback period*?). O modelo fará uma previsão *out-of-sample* para o Período de Teste. O $\mu$ será essa previsão.
**3.5. Processo de Otimização (O Método de Markowitz)**
Qual portfólio de Markowitz será montado? (Carteira de **Máximo Índice de Sharpe**? É a mais recomendada, pois usa o $\mu$ e o $\Sigma$).
Qual será a *proxy* para a Taxa Livre de Risco (R_f)? (O CDI, como citado em 1).
Haverá **restrições**? (Ex: Pesos 100% comprados ($w_i \ge 0$, $\Sigma w_i = 1$)? Peso máximo por ativo?).
**3.6. Métricas de Avaliação de Desempenho**
Como as carteiras serão comparadas? (Usar todas estas):
**Retorno:** Retorno Total Acumulado e Retorno Médio Anualizado.
**Risco (MPT):** Volatilidade (Desvio Padrão) Anualizada.
**Risco (PMPT):** Semivariância Anualizada e Máximo *Drawdown*.
**Retorno/Risco (MPT):** Índice de Sharpe.
**Retorno/Risco (PMPT):** Índice de Sortino.
**Benchmarks:** Comparar contra IBOVESPA e CDI.
| Métrica | Carteira Média Histórica | Carteira ARIMA | Carteira LSTM | IBOVESPA | CDI |
| --- | --- | --- | --- | --- | --- |
| Retorno Anualizado | X.X% | Y.Y% | Z.Z% | B.B% | C.C% |
| Volatilidade Anualizada | X.X% | Y.Y% | Z.Z% | B.B% | C.C% |
| Índice de Sharpe | X.X | Y.Y | Z.Z | B.B | C.C |
| Índice de Sortino | X.X | Y.Y | Z.Z | B.B | - |
| Máximo Drawdown | -X.X% | -Y.Y% | -Z.Z% | -B.B% | -C.C% |

Este capítulo também não existe.
**5.1. Síntese dos Achados**
Começar retomando a pergunta de pesquisa (Cap. 1): "Este trabalho se propôs a avaliar o impacto...".
Responder objetivamente: Qual foi o impacto? (Ex: "Os resultados do *backtest* demonstram que a substituição da média histórica por modelos LSTM resultou em um aumento de XX% no Índice de Sharpe...").
Resumir os achados da Tabela 2.
**5.2. Contribuições do Trabalho**
Qual a contribuição prática (para o investidor) e acadêmica (para a literatura em finanças no Brasil)?
**5.3. Limitações da Pesquisa**
O que o modelo *não* considerou?
Custos de transação (corretagem, impostos) e liquidez (impacto no preço).
Otimização apenas do $\mu$ (o $\Sigma$ também poderia ser previsto).
*Overfitting* (O LSTM pode ter se ajustado demais aos dados de treino?).
**5.4. Sugestões para Trabalhos Futuros**
O que pode ser feito a seguir?
(Usar as limitações): "Incluir custos de transação..."
"Testar outras arquiteturas de *machine learning* (ex: Transformers)..."
"Aplicar modelos para prever a matriz de covariância ($\Sigma$), não apenas o $\mu$..."

A principal crítica à MPT, conforme apontado por Damoradan , é que a premissa de normalidade raramente se sustenta, pois a maioria dos investimentos não possui retornos normalmente distribuídos e simétricos. A MPT utiliza a variância como medida de risco, que penaliza igualmente os desvios positivos (volatilidade "boa") e os desvios negativos (volatilidade "ruim").
A Pós-Moderna Teoria de Carteiras (PMPT) surge para endereçar essa limitação, alinhando-se às Finanças Comportamentais ao reconhecer que investidores são mais avessos a perdas do que à variabilidade geral (Roy, 1952). A PMPT foca, portanto, no **risco *****downside***.
**Semivariância e Índice de Sortino**
A principal métrica da PMPT é a **semivariância** (ou *downside deviation*). Diferente da variância (que mede a dispersão em torno da média), a semivariância mede apenas a dispersão dos retornos que caem *abaixo* de um retorno-alvo mínimo aceitável (MAR), frequentemente a própria média ou a taxa livre de risco.
Com base nessa métrica, Sortino e van der Meer  propuseram o **Índice de Sortino**. Ele é análogo ao Índice de Sharpe, mas substitui o desvio-padrão (risco total) no denominador pela semivariância (risco *downside*). Isso permite uma avaliação mais precisa do retorno ajustado ao risco, penalizando apenas a volatilidade indesejada (perdas).
**Value-at-Risk e Conditional Value-at-Risk**
Outras medidas de risco *downside* amplamente utilizadas são o Value-at-Risk (VaR) e sua adaptação, o Conditional Value-at-Risk (CVaR) (Dempster, 2002).
Jorion  define VaR como uma medida da maior potencial perda em valor de um ativo de risco ou portfólio em um dado período de tempo para um dado intervalo de confiança. Apesar do sucesso do VaR, ele foi criticado por duas razões principais: ele mede apenas os percentis da distribuição de perdas, ignorando perdas além do nível de VaR (chamado de *tail risk*); e não é uma medida coerente de risco, pois não é subaditivo (Artzner et al., 1997, 1999; Yamai & Yoshiba, 2005).
Para contornar o problema de *tail risk* e de subaditividade, Artzner et al. (1997, 1999) propuseram o CVaR (também chamado de *expected shortfall*). Satisfazendo todos os axiomas de uma medida coerente de risco, o CVaR pode ser definido como a média ponderada das expectativas de perdas quando essas são maiores que o VaR (Moreira, 2006).

Para cada uma das três carteiras, em cada período de rebalanceamento mensal, será calculado o portfólio de **Máximo Índice de Sharpe**.
A *proxy* para a Taxa Livre de Risco (R_f), necessária para o cálculo do Sharpe, será a taxa do **CDI** acumulada no período.
As **restrições** da otimização serão:  100% dos pesos alocados (soma dos pesos = 1) e  proibição de venda a descoberto (*short selling*), ou seja, todos os pesos devem ser maiores ou iguais a zero ($w_i \ge 0$).

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

| Otimizador \ Input de Retorno (μ) | C1: Média Histórica (Baseline) | C2: ARIMA (Preditivo Linear) | C3: LSTM (Preditivo Não-Linear) |
| --- | --- | --- | --- |
| Linha 1: MPT (Média-Variância)(Otimizador: Máx. Índice de Sharpe) | Portfólio 1(MPT Clássico - Seu plano atual) | Portfólio 2(Seu plano atual) | Portfólio 3(Seu plano atual) |
| Linha 2: PMPT (Média-CVaR)(Otimizador: Min. CVaR para um Retorno-Alvo) | Portfólio 4(Novo - PMPT com input simples) | Portfólio 5(Novo) | Portfólio 6(Novo - Modelo mais avançado) |
| (Opcional) Linha 3: Risco Ingênuo(Otimizador: 1/N - Pesos Iguais) | Portfólio 7 1 | (Não aplicável) | (Não aplicável) |

**4.3. Novas Métricas de Avaliação (Cap. 3.6)**
Sua metodologia deve *privilegiar* as métricas de PMPT, dado que seus dados 1 provam que elas são necessárias. O Índice de Sharpe deve ser incluído apenas como um benchmark do modelo MPT.
**Métricas Primárias (PMPT):**
**Índice de Sortino:** A métrica de retorno/risco que *se alinha* à sua crítica da variância (usa semivariância).
**Maximum Drawdown (MDD):** A medida mais prática de risco de perda para um investidor.
**CVaR (ou Expected Shortfall):** O valor real do risco de cauda (o que você minimizou no Portfólio 4-6).
**Métricas Secundárias (MPT/Outras):**
**Índice de Sharpe:** Para comparar (e provavelmente mostrar sua inferioridade).
**Volatilidade (σp):** Para mostrar como a M-V e a M-CVaR alocam o risco de forma diferente.
**Retorno Anualizado.**
Tabela 2: Proposta de Tabela de Resultados Finais (Novo Cap. 6)Esta tabela será a resposta final à sua pesquisa.

| Métrica | Port. 1 (MPT-Média) | Port. 2 (MPT-ARIMA) | Port. 3 (MPT-LSTM) | Port. 4 (CVaR-Média) | Port. 5 (CVaR-ARIMA) | Port. 6 (CVaR-LSTM) | Port. 7 (1/N) | IBOV | CDI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Retorno Anual. |  |  |  |  |  |  |  |  |  |
| Volatilidade Anual. (σp) |  |  |  |  |  |  |  |  |  |
| Índice de Sharpe |  |  |  |  |  |  |  |  |  |
| Índice de Sortino |  |  |  |  |  |  |  |  |  |
| Max Drawdown (MDD) |  |  |  |  |  |  |  |  |  |
| CVaR (95%) Histórico |  |  |  |  |  |  |  |  |  |

O sumário apresenta um erro editorial grave que reflete desorganização no fluxo de argumentos.1 As seções 2.6 e 2.7 são idênticas, assim como suas subseções 2.6.1 e 2.7.1:
2.6. Métricas e Modelos de Equilíbrio Derivados da MPT
2.6.1. O Índice de Sharpe (IS): Métrica de Desempenho Ajustado ao Risco Total
2.7. Métricas e Modelos de Equilíbrio Derivados da MPT
2.7.1. O Índice de Sharpe (IS): Métrica de Desempenho Ajustado ao Risco Total
Isso não é apenas um erro de digitação; sugere que seções foram escritas de forma isolada, sem uma integração lógica. A discussão sobre a MPT, CAPM, CML, SML e o Índice de Sharpe deve ser consolidada em uma narrativa única e coesa, eliminando a redundância.
Esta é a segunda e mais importante crítica desenvolvida no Capítulo 2. O trabalho afirma que "A variância... trata os desvios positivos (ganhos) e negativos (perdas) em relação à média com pesos iguais".1 Isso é corretamente contrastado com a "aversão à perda" e a preferência do investidor por métricas de *downside risk*.
No entanto, esta crítica fundamental *não é resolvida* pela metodologia proposta no Capítulo 3. Usar um modelo LSTM para prever $\mu$ não altera o fato de que o otimizador (M-V, via Índice de Sharpe) ainda usará a *variância* ($\sigma^2$) como medida de risco.1 O otimizador continuará a penalizar portfólios com alta volatilidade *positiva* (ganhos) e tratará ganhos e perdas simetricamente, um comportamento que o próprio autor já argumentou ser conceitualmente falho.

Este é o ponto mais crítico do relatório. A análise de dados do próprio autor invalida sua metodologia.
**O Dado (Cap 4.1):** O autor observa "valores de curtose dramaticamente elevados".1 Especificamente, cita-se Assaí (ASAI3) com uma curtose de **2469,69** e Pão de Açúcar (PCAR3) com **408,26**. O autor identifica isso corretamente como *leptocurtose* ("caudas pesadas"), indicando que eventos extremos são muito mais frequentes do que a distribuição normal prevê.
**A Metodologia (Cap 3.5):** O autor propõe otimizar para o "Máximo Índice de Sharpe".
**A Contradição:** O Índice de Sharpe é definido como $IS = (R_p - R_f) / \sigma_p$. O denominador é o *desvio padrão* ($\sigma_p$), a raiz quadrada da variância. A variância e o desvio padrão são medidas de risco completas e suficientes *apenas* se a distribuição dos retornos for normal (ou, no máximo, elíptica).
Os dados (curtose de 2469,69) não são normais; eles são um exemplo extremo de "caudas pesadas". A MPT (Média-Variância) otimiza para o *segundo momento* da distribuição (a variância). Em distribuições leptocúrticas, os *momentos superiores* (como a curtose, o quarto momento) dominam o risco. Otimizar apenas para o segundo momento (variância) é, portanto, um erro metodológico fundamental. O otimizador M-V irá *ignorar* o risco de cauda (tail risk), que é justamente o risco mais perigoso e proeminente diagnosticado nos dados.
A nova referência 1 corrobora exatamente isso, afirmando que a métrica de risco variância "subestimou a probabilidade de eventos oriundos de *tail risk*".
No final da Seção 4.1, o autor escreve a "arma fumegante" que prova a dissonância do trabalho:
"A constatação empírica [de leptocurtose]... fornece a justificativa central para este trabalho... A falha da premissa de normalidade valida: **O uso de métricas de risco da Pós-Moderna Teoria de Carteiras (PMPT), como o Índice de Sortino**... e a exploração de modelos preditivos (ARIMA e, especialmente, LSTM)..." 
Esta afirmação está 100% correta. Os dados *validam* o Índice de Sortino (PMPT). No entanto, a Metodologia (Cap 3.6) lista o Sortino apenas como uma *métrica de avaliação*, enquanto o processo de *otimização* (Cap 3.5) ainda é baseado no Índice de Sharpe (MPT).
Não se pode apenas *avaliar* com a PMPT se a carteira foi *otimizada* com a MPT. Isso é misturar paradigmas de forma incoerente. Se os dados validam a PMPT, o autor deve *OTIMIZAR* usando métricas da PMPT (ex: minimizar a Semivariância para maximizar o Sortino, ou minimizar o CVaR). O diagnóstico de PMPT foi usado apenas para justificar um tratamento de MPT, o que é logicamente falho.

A metodologia de avaliação deve *privilegiar* as métricas da PMPT, dado que os dados (Cap 4.1) 1 provam sua necessidade.
**Métricas Primárias (PMPT):**
**Índice de Sortino:** A métrica de retorno/risco que *se alinha* à crítica da variância (usa semivariância).
**Maximum Drawdown (MDD):** A medida mais prática de risco de perda.
**CVaR (ou Expected Shortfall):** O valor real do risco de cauda.
**Métricas Secundárias (MPT/Outras):**
**Índice de Sharpe:** Para comparar (e mostrar sua provável inferioridade).
**Volatilidade ($\sigma_p$):** Para mostrar como M-V e M-CVaR alocam o risco de forma diferente.
**Retorno Anualizado.**
Tabela 2: Proposta de Tabela de Resultados Finais (Novo Cap. 6)
Esta tabela será a resposta final à sua pesquisa.

### 5.1. Índice de Sharpe

O Índice de Sharpe é a métrica adequada quando o portfólio analisado representa a totalidade do patrimônio do investidor, pois penaliza a falta de diversificação (risco idiossincrático não eliminado).
| Métrica | Foco da Avaliação | Medida de Risco | Contexto de Aplicação Ideal |
| --- | --- | --- | --- |
| Índice de Sharpe | Retorno ajustado ao risco total | Desvio-Padrão ($\sigma$) | Portfólio isolado / Patrimônio total do investidor |
| Índice de Treynor | Retorno ajustado ao risco sistemático | Beta ($\beta$) | Sub-portfólio dentro de uma carteira diversificada |
| Alfa de Jensen | Retorno anormal (excesso) | Beta ($\beta$) | Avaliação da habilidade do gestor (Active Management) |

## 7. O Modelo de Precificação de Ativos de Capital (CAPM)

### 1.1. O Alicerce Teórico (Arquivo 2: Slides MPT/CAPM/BL)

## O Modelo de Precificação de Ativos de Capital (CAPM)

Enquanto a MPT de Markowitz é normativa (diz ao investidor como construir um portfólio), o *Capital Asset Pricing Model* (CAPM) é positivo (explica como os preços dos ativos são determinados se todos seguirem a MPT).

## Decomposição do Risco: Sistemático vs. Não Sistemático

O CAPM introduz uma distinção fundamental na natureza do risco, decompondo a variância total de um ativo  em dois componentes (ROSS, WESTERFIELD, JORDAN, 2010):
**Risco Sistemático (Risco de Mercado):** É a parcela da volatilidade do ativo que está correlacionada com os movimentos do mercado como um todo. Origina-se de fatores macroeconômicos inelutáveis — inflação, juros, ciclos econômicos, guerras — que afetam todas as empresas simultaneamente. Este risco *não pode* ser eliminado pela diversificação.
**Risco Não Sistemático (Idiossincrático/Específico):** É a parcela da volatilidade exclusiva da empresa ou setor (ex: sucesso de um novo produto, greve na fábrica, fraude contábil). Como esses eventos são estatisticamente independentes entre empresas, em um portfólio amplo eles tendem a se cancelar mutuamente (lei dos grandes números).
A conclusão revolucionária do CAPM é que **o mercado não remunera o risco não sistemático**. Como ele pode ser eliminado gratuitamente através da diversificação, os investidores não devem esperar nenhum prêmio de retorno por assumi-lo. O único risco que justifica um retorno esperado acima da taxa livre de risco é o risco sistemático (ROSS, WESTERFIELD, JORDAN, 2010).

### O Coeficiente Beta e a Reta do Mercado de Títulos (SML)

Para mensurar o risco sistemático, o CAPM utiliza o coeficiente **Beta** . O Beta é uma medida padronizada da covariância do ativo com o mercado, definida como:

- A Reta do Mercado de Títulos (SML)
- 
- A equação do CAPM define uma relação linear entre o retorno esperado e o Beta, e essa relação é representada graficamente pela **Security Market ****Line**** (SML)**, ou **Linha do Mercado de Títulos (LMT)**. O CAPM estabelece que o retorno esperado do ativo () é dado pela equação da SML:
- 
- 
- A SML é crucial porque todo ativo individual, ou portfólio eficiente e não eficiente, deve se situar sobre ela em um mercado de equilíbrio

A distinção fundamental entre a CML e a SML reside na medida de risco utilizada.
- **CML (Capital Market ****Line****): **É a fronteira eficiente que relaciona o retorno esperado com o **Risco Total **(medido pelo desvio-padrão, *σ*). O Índice de Sharpe avalia o prêmio de risco por unidade de risco total (medido ao longo da CML).
- **SML (Security Market ****Line****):** Relaciona o retorno esperado com o **Risco Sistemático **(medido pelo Beta, *β*). O CAPM demonstra que os investidores são compensados apenas pelo risco sistemático, pois o risco não sistemático pode ser eliminado pela diversificação.

| Característica | Capital Market Line (CML) | Security Market Line (SML) |
| --- | --- | --- |
| Medida de Risco | Desvio Padrão Total | Beta Sistemático |
| Aplicação | Apenas Portfólios Eficientes | Qualquer Ativo Individual ou Portfólio |
| Definição de Risco | Risco Total (Sistemático + Idiossincrático) | Apenas Risco Sistemático (Covariância com Mercado) |
| Ponto de Intercepto | Taxa Livre de Risco | Taxa Livre de Risco |
| Inclinação (Slope) | Índice de Sharpe do Mercado | Prêmio de Risco de Mercado |
| Fundamentação | Teorema da Separação de Tobin | Modelo de Equilíbrio de Mercado (CAPM) |

A elegância matemática da MPT e do CAPM repousa sobre um conjunto de axiomas sobre o comportamento humano e a estrutura dos mercados. A validade desses modelos depende, portanto, da robustez de seus pressupostos.

A inovação central do modelo BL reside na combinação de duas fontes distintas de informação para gerar um novo vetor de retornos esperados (distribuição Posterior):
- O Prior (Equilíbrio de Mercado): Diferentemente de Markowitz, que muitas vezes utiliza médias históricas, o BL assume como ponto de partida neutro que o mercado está em equilíbrio. Utilizando um processo de "Otimização Reversa" (Baseada no CAPM), o modelo deriva os **Retornos de Equilíbrio Implícitos (Π)** a partir das capitalizações de mercado atuais. Esse vetor atua como um "centro de gravidade", garantindo que, na ausência de novas informações, a alocação ótima seja a carteira de mercado, evitando posições extremas.
- **As Visões (****Views**** - Q) e a Incerteza (Ω):** O modelo permite que o investidor incorpore suas expectativas subjetivas ou quantitativas sobre o desempenho dos ativos. No contexto deste trabalho, as "Visões" não são opiniões discricionárias, mas sim as projeções de retorno geradas pelos modelos preditivos **ARIMA e Redes Neurais LSTM**. Essas visões são expressas no vetor Q e associadas a uma matriz de incerteza diagonal Ω, que reflete o grau de confiança em cada previsão (baseado, por exemplo, no erro quadrático médio dos modelos preditivos).

**3.2 A Abordagem Bayesiana: O Coração Conceitual do Modelo**
O rigor matemático e a elegância prática do Modelo Black-Litterman residem na sua formulação como um problema de **inferência Bayesiana**. Ao contrário da estatística frequentista clássica, que trata os parâmetros (como o retorno esperado) como constantes fixas e desconhecidas, a abordagem Bayesiana trata os parâmetros como variáveis aleatórias que possuem uma distribuição de probabilidade própria. Isso permite incorporar explicitamente a incerteza sobre a estimativa e atualizar essa crença à medida que novas informações (visões) se tornam disponíveis.
A estrutura conceitual do BL segue o silogismo Bayesiano clássico:
**3.2.1 Prior: O Equilíbrio de Mercado**
O ponto de partida do modelo, ou distribuição *a priori*, é a premissa de neutralidade. Na ausência de qualquer informação específica ou visão profética por parte do gestor, qual é a melhor estimativa racional para os retornos futuros? A resposta de Black e Litterman baseia-se na Hipótese de Mercados Eficientes e no CAPM (*Capital **Asset* *Pricing** Model*).
Assume-se que, no agregado, o mercado está em equilíbrio. Portanto, o portfólio de mercado (ponderado pela capitalização de todos os ativos) deve ser o portfólio ótimo para o investidor médio avesso ao risco. A partir dessa observação observável (os pesos de mercado), o modelo "engenharia reversa" os retornos que justificam esses pesos. Este vetor, denominado **Retornos de Equilíbrio Implícitos** ($\Pi$), serve como a âncora gravitacional do modelo. Ele garante que, se o gestor não tiver visões ("eu não sei nada"), o modelo recomendará manter o portfólio de mercado passivo, evitando as alocações extremas da MPT.
**3.2.2 ****Likelihood****: As Visões do Investidor (*****Views*****)**
A "verossimilhança" ou informação nova entra no modelo através das Visões. Diferente da MPT, que exige um vetor completo de retornos para todos os ativos, o BL permite que o gestor expresse opiniões apenas sobre um subconjunto de ativos (Visões Parciais). Estas visões podem ser absolutas ("Petrobras vai subir 10%") ou relativas ("Bancos vão superar Varejo em 2%"). Crucialmente, cada visão é acompanhada por um grau de incerteza (variância do erro), permitindo que o modelo pondere matematicamente a convicção do gestor.
**3.2.3 Posterior: A Nova Estimativa Combinada**
O resultado final é a distribuição *a posteriori*, calculada aplicando a Regra de Bayes. O vetor de retornos esperados BL ($E_{BL}$) é uma média ponderada complexa entre o Prior (Equilíbrio) e a Likelihood (Visões).
Se o gestor tem baixa confiança nas suas visões, o Posterior converge para o Prior (o portfólio tende ao índice de mercado).
Se o gestor tem alta confiança, o Posterior afasta-se do equilíbrio na direção das visões, alterando os pesos do portfólio.
Essa mecânica atua como um filtro de estabilidade (shrinkage estimator), mitigando a "maximização de erros" ao ancorar as estimativas em valores economicamente plausíveis.
**3.7 Limitações e Extensões Modernas**
Apesar de sua elegância, o modelo BL clássico de 1992 não é isento de falhas, muitas das quais derivam de suas premissas simplificadoras herdadas da MPT.
**3.7.1 A Dependência da Normalidade e do CAPM**
O modelo assume que os retornos dos ativos seguem uma distribuição Normal Multivariada. Esta suposição é empiricamente rejeitada pela presença observada de "caudas gordas" (leptocurtose) e assimetria (*skewness*) nos mercados financeiros, especialmente em períodos de crise.30 O uso da distribuição normal subestima a probabilidade de eventos extremos, tornando o BL clássico vulnerável a "Cisnes Negros". Adicionalmente, o Prior depende da validade do CAPM. Se o mercado for ineficiente ou se o *proxy* do portfólio de mercado for inadequado, o ponto de ancoragem $\Pi$ estará enviesado ("Garbage In"), contaminando toda a alocação subsequente.
**3.7.2 Entropy Pooling e Fully Flexible Views (****Meucci****)**
Para superar a restrição da normalidade, Attilio Meucci (2008, 2010) introduziu a generalização conhecida como **Entropy** **Pooling** (Agrupamento de Entropia). Diferente do BL que usa fórmulas fechadas para conjugados gaussianos, o Entropy Pooling utiliza otimização numérica para minimizar a **Divergência de ****Kullback-Leibler** (Entropia Relativa) entre a distribuição Prior e a Posterior.
As vantagens desta extensão são profundas:
**Prior Genérico:** O Prior não precisa ser normal ou de equilíbrio. Pode ser uma distribuição empírica histórica, uma distribuição de Monte Carlo com caudas pesadas, ou derivada de Cópulas para modelar dependência não-linear nas caudas.
**Visões Flexíveis:** O gestor não se limita a visões sobre médias ($Q$). É possível inserir visões sobre volatilidade ("A vol vai aumentar"), correlação, ou medidas de cauda como o VaR ("O risco de perda máxima será de 15%").
**Consistência:** O método garante que a distribuição Posterior seja a mais próxima possível do Prior (preservando a estrutura de mercado) enquanto satisfaz as restrições impostas pelas visões complexas.
Essa abordagem representa o estado da arte na alocação de ativos, permitindo a fusão da estabilidade Bayesiana do BL com a consciência de risco de cauda da PMPT em um framework matemático unificado e agnóstico quanto à distribuição subjacente.
**3.8 Conclusão do Capítulo**
O Modelo de Black-Litterman transcendeu sua origem como uma ferramenta proprietária da Goldman Sachs para se tornar um pilar fundamental das Finanças Quantitativas modernas. Sua contribuição não foi refutar Markowitz, mas sim "salvar" a MPT de si mesma, introduzindo uma camada Bayesiana de bom senso econômico que estabiliza as alocações. Ao permitir a fusão elegante entre a disciplina passiva do equilíbrio de mercado e a inteligência ativa das visões do gestor, o BL resolveu o dilema da "maximização de erros". As suas extensões modernas, como o método de confiança de Idzorek e a *Entropy* *Pooling* de Meucci, asseguram que o modelo permaneça adaptável a um mundo financeiro cada vez mais complexo e não-normal, servindo como a ponte ideal entre a teoria de eficiência de mercado e a gestão ativa prática.

- O Prior (Equilíbrio de Mercado): Diferentemente de Markowitz, que muitas vezes utiliza médias históricas, o BL assume como ponto de partida neutro que o mercado está em equilíbrio. Utilizando um processo de "Otimização Reversa" (Baseada no CAPM), o modelo deriva os **Retornos de Equilíbrio Implícitos (Π)** a partir das capitalizações de mercado atuais. Esse vetor atua como um "centro de gravidade", garantindo que, na ausência de novas informações, a alocação ótima seja a carteira de mercado, evitando posições extremas.
- **Likelihood****, a****s Visões (****Views**** - Q) e a Incerteza (Ω):** O modelo permite que o investidor incorpore suas expectativas subjetivas ou quantitativas sobre o desempenho dos ativos. Essas visões são expressas no vetor Q e associadas a uma matriz de incerteza diagonal Ω, que reflete o grau de confiança em cada previsão (baseado, por exemplo, no erro quadrático médio dos modelos preditivos).
- **Posterior****,**** a** **Nova Estimativa Combinada:** O resultado final é a distribuição a posteriori, calculada aplicando a Regra de Bayes. O vetor de retornos esperados BL  é uma média ponderada complexa entre o Prior (Equilíbrio) e a Likelihood (Visões).Se o gestor tem baixa confiança nas suas visões, o Posterior converge para o Prior (o portfólio tende ao índice de mercado).Se o gestor tem alta confiança, o Posterior afasta-se do equilíbrio na direção das visões, alterando os pesos do portfólio.Essa mecânica atua como um filtro de estabilidade (shrinkage estimator), mitigando a "maximização de erros" ao ancorar as estimativas em valores economicamente plausíveis.
O modelo assume que os retornos dos ativos seguem uma distribuição Normal Multivariada. Esta suposição é empiricamente rejeitada pela presença observada de "caudas gordas" (leptocurtose) e assimetria (*skewness*) nos mercados financeiros, especialmente em períodos de crise.30 O uso da distribuição normal subestima a probabilidade de eventos extremos, tornando o BL clássico vulnerável a "Cisnes Negros". Adicionalmente, o Prior depende da validade do CAPM. Se o mercado for ineficiente ou se o *proxy* do portfólio de mercado for inadequado, o ponto de ancoragem  estará enviesado ("Garbage In"), contaminando toda a alocação subsequente.
### 2.3 O Modelo de Precificação de Ativos de Capital (CAPM) e o Equilíbrio Geral

Enquanto Markowitz forneceu uma teoria normativa (o que o investidor *deve* fazer), o desenvolvimento subsequente do *Capital Asset Pricing Model* (CAPM) por William Sharpe, John Lintner e Jan Mossin na década de 1960 forneceu uma teoria positiva (o que acontece com os preços se todos seguirem Markowitz).
#### 2.3.2 Beta (**$\beta$**) e a Reta do Mercado de Títulos (SML)

O CAPM deduz que, em equilíbrio, o mercado não remunera o risco idiossincrático (específico da empresa), pois este pode ser eliminado via diversificação sem custo. O único risco precificado é o **Risco Sistemático** (risco de mercado). A medida desse risco é o Beta ($\beta$), que quantifica a sensibilidade do retorno do ativo às flutuações do mercado.
A equação fundamental do CAPM é representada pela **Reta do Mercado de Títulos (SML)**:

Apesar de sua hegemonia acadêmica, a MPT e o CAPM enfrentam críticas devastadoras que motivam a busca pelos modelos avançados discutidos neste relatório.

Richard Roll atacou a testabilidade empírica do CAPM. Ele argumentou que o verdadeiro "Portfólio de Mercado" deve incluir *todos* os ativos do universo, incluindo capital humano, arte, imóveis e ativos intangíveis. Como tal portfólio é inobservável, os testes usam proxies como o S&P 500. Roll provou matematicamente que se o proxy escolhido for eficiente na média-variância *ex-post*, o CAPM parecerá funcionar, independentemente da realidade econômica. Isso torna o CAPM, em muitos aspectos, uma tautologia matemática dependente do benchmark, levantando o "erro de benchmark" como um problema fatal para a avaliação de gestores.
A insuficiência do Beta único do CAPM para explicar os retornos observados levou à busca por modelos multifatoriais. Eugene Fama e Kenneth French, no início da década de 1990, desferiram um golpe empírico ao CAPM ao documentarem anomalias persistentes que o Beta não conseguia capturar.
| Fator | Denominação | Racional Econômico |
| --- | --- | --- |
| MKT-RF | Excesso de Retorno de Mercado | O risco sistemático tradicional do CAPM. |
| SMB | Small Minus Big (Tamanho) | As ações de pequena capitalização (small caps) historicamente superam as grandes. Fama e French argumentam que isso compensa o investidor pelo menor acesso a crédito, menor liquidez e maior vulnerabilidade a choques econômicos dessas empresas. |
| HML | High Minus Low (Valor) | As ações de "Valor" (alto book-to-market) superam as de "Crescimento". O racional é que empresas de valor são frequentemente empresas em dificuldades (distressed), com lucros voláteis, exigindo um prêmio de risco maior. |

| Etapa | Modelo/Componente | Função | Input | Output |
| --- | --- | --- | --- | --- |
| 1. Prior | CAPM Reverso | Estabelecer a âncora de equilíbrio. | Pesos de Mercado ($w_{mkt}$), Covariância Histórica ($\Sigma$). | Vetor de Retornos Implícitos ($\Pi$). |
| 2. Visão | LSTM (Deep Learning) | Capturar Alpha não-linear. | Séries Temporais (Preço, Volume, Macro, Fatores FF). | Previsão de Retornos ($Q$). |
| 3. Confiança | GARCH / EGARCH | Quantificar o Risco da Visão. | Resíduos da LSTM, Histórico de Volatilidade. | Matriz de Incerteza ($\Omega$). |
| 4. Fusão | Black-Litterman | Integração Bayesiana. | $\Pi$, $Q$, $\Omega$, $\tau$. | Retornos Posteriores ($\mu_{BL}$) e Covariância Posterior ($\Sigma_{BL}$). |
| 5. Otimização | MAD / PMPT | Construção Robusta de Portfólio. | $\mu_{BL}$, Retornos de Cenários. | Pesos Ótimos Finais ($w_{opt}$). |

### O Problema da Seleção de Portfólio: A Revolução de Markowitz 
### Definicao de risco
- **Pilares do Modelo de Otimização Média-Variância**
- **Retorno Esperado (****):**
- **Risco (Risco Total): A Quantificação como Variância  ****(****)**
- A Importância da Covariância e da Diversificação
- **Conjunto Viável **(Feasible Set)
- A Fronteira Eficiente
- O Portfólio de Mínima Variância Global (PMVG)
- A Introdução do Ativo Livre de Risco e o Portfólio Ótimo
- O Princípio da Separação e a Reta do Mercado de Capitais (CML)
- O Portfólio de Tangência e a Universalidade da Alocação de Ativos
- **Métricas e Modelos de Equilíbrio Derivados da MPT**
- O Índice de Sharpe
- O Capital Asset Pricing Model (CAPM): O Modelo de Equilíbrio
- O Coeficiente Beta (*β*): A Medida de Risco Sistemático
- A Reta do Mercado de Títulos (SML)
- **Diferença entre CML e SML:**
- Premissas Fundamentais, Críticas e Limitações Práticas
- Crítica à Premissa de Normalidade e a Evolução do Risco
- A Justificativa para Extensões e Modelos Alternativos
- **Pós-Moderna Teoria do Portfólio (PMPT) e Métricas Assimétricas:**
- **Métricas de Risco de Baixa: **A PMPT utiliza métricas que penalizam apenas os desvios abaixo de um alvo, incluindo:
- **Semivariância**** e Lower ****Partial** **Moment**** (LPM):** Focam na volatilidade ou dispersão dos retornos negativos.
- **Value** **at**** Risk (****VaR****):** Estima a perda máxima esperada em um determinado nível de confiança. O VaR é uma ferramenta que enriquece a gestão de risco na otimização de portfólios.
- **Conditional** **Value** **at**** Risk (****CVaR****):** Mede a perda média que excede o VaR, sendo considerado superior por capturar a magnitude das perdas extremas (cauda da distribuição).
- **Métricas de Avaliação Ajustadas ao Risco de Baixa:**
- **Índice de ****Sortino****:** Similar ao Índice de Sharpe, mas utiliza o *downside* *deviation* (risco de baixa) no denominador em vez do desvio padrão total (*σ**p*​). Sua relevância reside no foco exclusivo no risco negativo.
- **Maximum** **Drawdown**** (MD): **Embora não seja uma medida de risco para otimização em M-V, é uma métrica crucial de avaliação de desempenho *out-**of**-sample*, pois evidencia a **maior perda percentual **observada de um pico a um vale
- A Variância como Métrica de Risco
- **A Penalização da Volatilidade Positiva:**
- **A Distância da Aversão ao Risco *****Downside***
- 
- O Problema do Erro de Estimação (*Estimation Error*)

**Modelos Evoluídos e Fatores de Risco**
**Modelos Multifatoriais (Fama-****French****)**
O modelo FF3 estende o CAPM adicionando fatores de risco que explicam os retornos anômalos.

**2.1. A Evolução Histórica da Gestão de Portfólio**
2.1.1. O Paradigma Pré-Moderno: Graham & Dodd e o Risco como Perda Permanente.
2.1.2. A Revolução de Markowitz : A formalização da Variância e a descoberta da Covariância.
2.1.3. O Capital Asset Pricing Model (CAPM): O equilíbrio de mercado, a SML e a hegemonia do Beta.
**3.1. A Abordagem Bayesiana na Alocação de Ativos**
3.1.1. Inferência Bayesiana: Combinando *Priors* (Crenças Iniciais) e *Likelihood* (Evidências) para gerar *Posteriors*.
3.1.2. A superação da dicotomia entre gestão passiva (equilíbrio) e ativa (visões).
**3.2. Derivação Matemática e Componentes do Modelo**
3.2.1. O Prior de Equilíbrio ($\Pi$): Engenharia Reversa a partir dos pesos de capitalização de mercado (CAPM Reverso).
3.2.2. O Vetor de Visões ($Q$): A incorporação de expectativas absolutas e relativas.
3.2.3. A Matriz de Incerteza ($\Omega$): O papel crítico da confiança e os desafios de calibração.
3.2.4. A Solução Analítica: O cálculo do vetor de retornos esperados combinados ($\mu_{BL}$).
**3.3. A Inovação *****Data-******Driven*****: Black-****Litterman**** Dinâmico**
3.3.1. Substituição da subjetividade humana por sinais algorítmicos.
3.3.2. A necessidade de estimadores robustos para $Q$ e $\Omega$ (ponte para o próximo capítulo).

## 7. O Modelo de Precificação de Ativos de Capital (CAPM)

### 7.2 Decomposição do Risco: Sistemático vs. Não Sistemático

### 7.3 O Coeficiente Beta e a Reta do Mercado de Títulos (SML)

| Característica | Capital Market Line (CML) | Security Market Line (SML) |
| --- | --- | --- |
| Medida de Risco | Desvio Padrão Total ($\sigma$) | Beta Sistemático ($\beta$) |
| Aplicação | Apenas Portfólios Eficientes | Qualquer Ativo ou Portfólio |
| Definição de Risco | Risco Total (Sistemático + Idiossincrático) | Apenas Risco Sistemático |
| Ponto de Intercepto | Taxa Livre de Risco ($R_f$) | Taxa Livre de Risco ($R_f$) |
| Inclinação (Slope) | Índice de Sharpe do Mercado | Prêmio de Risco de Mercado ($R_M - R_f$) |
| Contexto Teórico | Teorema da Separação de Tobin | Modelo CAPM |

Enquanto a MPT de Markowitz e a análise de Tobin eram teorias normativas (prescrevendo como os investidores *deveriam* agir), o **Capital Asset Pricing Model (CAPM)** surgiu na década de 1960 como uma teoria positiva de equilíbrio, descrevendo como os preços dos ativos se comportariam se todos os investidores seguissem as recomendações da MPT.
O CAPM foi desenvolvido de forma independente e quase simultânea por William Sharpe , John Lintner , Jan Mossin  e Jack Treynor . Este esforço intelectual coletivo buscou determinar qual seria o retorno de equilíbrio de um ativo individual num mercado dominado por investidores diversificadores.
A contribuição central do CAPM é a distinção entre dois tipos de risco:
**Risco Não Sistemático (Idiossincrático/Diversificável):** O risco específico de uma empresa ou setor. Como demonstrado por Markowitz, este risco pode ser eliminado quase inteiramente através da diversificação eficiente. Portanto, em um mercado competitivo, os investidores não devem ser remunerados por assumir riscos que podem ser eliminados sem custo.
**Risco Sistemático (De Mercado/Não Diversificável):** O risco inerente a todo o sistema econômico (ex: variações na taxa de juros, recessões, choques inflacionários). Este risco não pode ser eliminado pela diversificação.
O CAPM postula que o mercado remunera *apenas* a exposição ao risco sistemático. O risco total ($\sigma$) torna-se irrelevante para a precificação de ativos individuais, sendo substituído pelo conceito de **Beta ($\beta$)**.
$$\beta_i = \frac{\text{Cov}(R_i, R_M)}{\sigma_M^2}$$
A relação fundamental do CAPM é expressa pela equação da **Security Market Line (SML)**:

$$E(R_i) = R_f + \beta_i$$
A SML difere fundamentalmente da CML. Enquanto a CML usa o desvio padrão ($\sigma$) no eixo horizontal e aplica-se apenas a portfólios eficientes (sem risco não sistemático), a SML usa o Beta ($\beta$) no eixo horizontal e aplica-se a *qualquer* ativo ou portfólio, eficiente ou não.
Um ativo com $\beta = 1$ tem o mesmo risco sistemático que o mercado.
Um ativo com $\beta > 1$ é mais volátil que o mercado (agressivo).
Um ativo com $\beta < 1$ é menos volátil que o mercado (defensivo).
Segundo o CAPM, em equilíbrio, todos os ativos devem estar situados sobre a SML. Qualquer ativo acima da linha estaria "barato" (oferecendo retorno excessivo para seu risco sistemático), e qualquer ativo abaixo estaria "caro".
A elegância matemática da MPT e do CAPM baseia-se em um conjunto de pressupostos simplificadores que têm sido objeto de intenso debate acadêmico e testes empíricos.

O CAPM introduz uma distinção fundamental na natureza do risco, decompondo a variância total de um ativo ($\sigma_i^2$) em dois componentes 10:
**Risco Sistemático (Risco de Mercado):** É a parcela da volatilidade do ativo que está correlacionada com os movimentos do mercado como um todo. Origina-se de fatores macroeconômicos inelutáveis — inflação, juros, ciclos econômicos, guerras — que afetam todas as empresas simultaneamente. Este risco *não pode* ser eliminado pela diversificação.
**Risco Não Sistemático (Idiossincrático/Específico):** É a parcela da volatilidade exclusiva da empresa ou setor (ex: sucesso de um novo produto, greve na fábrica, fraude contábil). Como esses eventos são estatisticamente independentes entre empresas, em um portfólio amplo eles tendem a se cancelar mutuamente (lei dos grandes números).
A conclusão revolucionária do CAPM é que **o mercado não remunera o risco não sistemático**. Como ele pode ser eliminado gratuitamente através da diversificação, os investidores não devem esperar nenhum prêmio de retorno por assumi-lo. O único risco que justifica um retorno esperado acima da taxa livre de risco é o risco sistemático.
Para mensurar o risco sistemático, o CAPM utiliza o coeficiente **Beta** ($\beta$). O Beta é uma medida padronizada da covariância do ativo com o mercado, definida como:

$$\beta_i = \frac{\sigma_{i,M}}{\sigma_M^2} = \rho_{i,M} \frac{\sigma_i}{\sigma_M}$$
Um ativo com $\beta = 1$ move-se, em média, na mesma proporção que o mercado. Um ativo com $\beta > 1$ amplifica os movimentos do mercado (mais risco sistemático), enquanto $\beta < 1$ os atenua.
A relação de equilíbrio entre risco sistemático e retorno esperado é expressa pela equação da **Reta do Mercado de Títulos** (Security Market Line - SML):

## 4. A Evolução para o Equilíbrio Geral: CAPM e a Teoria da Separação

Enquanto Markowitz forneceu uma teoria normativa (o que um investidor *deve* fazer), a década de 1960 viu o surgimento de uma teoria positiva de equilíbrio de mercado: se todos os investidores agirem conforme Markowitz, como os preços dos ativos serão formados? Esta questão levou ao desenvolvimento do *Capital Asset Pricing Model* (CAPM), através dos esforços independentes de William Sharpe , John Lintner , Jan Mossin  e Jack Treynor .
### 4.3. Pressupostos Estruturais do CAPM

### 4.4. A Derivação do Beta e a Linha do Mercado de Títulos (SML)

Sob esses pressupostos, o CAPM conclui que o mercado é eficiente e que o "Portfólio de Mercado" (que contém todos os ativos ponderados pelo valor de mercado) é o portfólio de variância mínima para seu nível de retorno. Consequentemente, o único risco que o mercado remunera é o **Risco Sistemático** (risco de mercado), pois o **Risco Idiossincrático** (específico da empresa) pode ser eliminado gratuitamente via diversificação.
Isso leva à equação fundamental do CAPM, representada graficamente pela *Security Market Line* (SML):
$$E = R_f + \beta_i (E - R_f)$$
Onde $\beta_i$ (Beta) mede a sensibilidade do retorno do ativo $i$ em relação ao retorno do mercado. A distinção entre a *Capital Market Line* (CML) e a SML é vital: a CML aplica-se apenas a portfólios eficientes e usa o desvio-padrão ($\sigma$) como medida de risco, enquanto a SML aplica-se a qualquer ativo (eficiente ou não) e usa o Beta ($\beta$) como medida de risco relevante.
A consolidação do CAPM permitiu o desenvolvimento de métricas padronizadas para avaliar o desempenho de gestores de investimento, separando a habilidade (*skill*) da sorte ou da mera exposição ao risco.

O Alfa de Jensen é uma medida absoluta de performance baseada na SML. Ele quantifica o retorno anormal de um portfólio em relação ao que seria previsto teoricamente pelo CAPM, dado o seu Beta.

Apesar de sua onipresença acadêmica e profissional, a MPT e o CAPM enfrentaram contestações teóricas severas que questionaram sua validade científica e utilidade prática.

Richard Roll apresentou uma crítica epistemológica devastadora conhecida como "Crítica de Roll". Ele argumentou que o CAPM é, em essência, impossível de ser testado empiricamente.
O argumento central repousa na definição do "Portfólio de Mercado". Para o CAPM ser válido, o portfólio de mercado deve incluir todos os ativos de risco do universo: ações, títulos, commodities, imóveis, arte, moedas e, crucialmente, capital humano. Como tal portfólio é inobservável, os pesquisadores utilizam proxies como o índice S&P 500.
Roll demonstrou uma tautologia matemática: se o proxy escolhido for eficiente na média-variância *ex-post*, a relação linear do CAPM (Beta vs. Retorno) será matematicamente verdadeira, independentemente da realidade econômica subjacente. Inversamente, se o teste falhar, isso pode significar apenas que o proxy escolhido é ineficiente, e não que o modelo CAPM é inválido.41 Isso cria um "erro de benchmark" que invalida potencialmente todas as medidas de performance baseadas no CAPM (como o Alfa de Jensen), pois um gestor pode parecer ter um Alfa negativo apenas porque o benchmark utilizado é ineficiente.
O pressuposto de racionalidade do investidor também foi desmantelado pelas Finanças Comportamentais. Kahneman e Tversky (Prospect Theory) demonstraram que os investidores sentem a dor da perda de forma mais aguda do que o prazer do ganho (aversão à perda vs. aversão ao risco) e cometem erros sistemáticos de julgamento.
Empiricamente, Fama e French  desferiram outro golpe ao CAPM ao mostrarem que o Beta sozinho não explica a variação transversal dos retornos das ações. Eles identificaram anomalias persistentes: ações de pequena capitalização (*Small Caps*) e ações de valor (*High Book-to-Market*) superam consistentemente o mercado, contradizendo a previsão do CAPM. Isso levou ao desenvolvimento do Modelo de Três Fatores de Fama-French, que incorpora tamanho e valor como fatores de risco adicionais, e mais tarde ao fenômeno "Betting Against Beta" (Apostando contra o Beta), onde ações de baixo beta geram alfas positivos, violando diretamente a SML.
Um dos avanços mais significativos na alocação de ativos institucional foi o modelo desenvolvido por Fischer Black e Robert Litterman na Goldman Sachs. Eles identificaram que a otimização de média-variância de Markowitz é extremamente sensível aos inputs: pequenas alterações nas estimativas de retorno esperado produzem portfólios extremos e concentrados ("maximizadores de erro de estimação").
O modelo Black-Litterman utiliza uma abordagem Bayesiana para resolver isso. Em vez de exigir que o investidor estime todos os retornos do zero, o modelo começa com o equilíbrio de mercado (os retornos implícitos pelo CAPM reverso) como a distribuição "a priori" neutra. O investidor então insere suas "visões" subjetivas (ex: "Acho que Tech vai superar Energia em 5%") apenas onde tem forte convicção. O modelo combina matematicamente o equilíbrio de mercado com essas visões, ponderadas pela confiança do investidor, gerando portfólios estáveis, intuitivos e diversificados.
A jornada da teoria de portfólio, de Graham a Markowitz, e de Sharpe a Black-Litterman, não é um caminho linear de substituição, mas de acumulação e refinamento. A MPT e o CAPM, apesar de suas falhas empíricas e pressupostos irreais, permanecem como os pilares pedagógicos e conceituais das finanças. Eles forneceram a linguagem — alfa, beta, correlação, sistemático vs. idiossincrático — que permite aos investidores estruturar o problema da alocação de capital.
A compreensão contemporânea exige, no entanto, o reconhecimento das "caudas gordas" de Mandelbrot, a cautela epistemológica de Roll e a incorporação de fatores multifatoriais de Fama-French. O investidor moderno não descarta Markowitz, mas o utiliza com a consciência de que o mapa (o modelo) não é o território (o mercado), integrando a disciplina quantitativa com a robustez necessária para enfrentar a incerteza radical.
# A Arquitetura da Alocação Moderna de Ativos: Uma Síntese Crítica entre a Abordagem Bayesiana de Black-Litterman, a Modelagem Não-Linear via Redes Neurais LSTM e a Otimização Robusta PMPT

## 8. Limitações e Críticas à MPT: O Problema do Erro de Estimação

A pergunta de pesquisa do TCC 1 é fundamentalmente sobre o "problema do erro de estimação". O TCC testa se previsões (ARIMA, LSTM) são estimadores de $\mu$ superiores à Média Histórica.
A validade desta premissa é inequivocamente apoiada pelos materiais. Os slides 1 e o referencial teórico do TCC (que cita DeMiguel e Nogales  e o "maximizador de erros" 1) estão em perfeito alinhamento. A otimização M-V clássica é *extremamente sensível* a *inputs* de retorno esperado.1 O uso da Média Histórica simples, como os slides 1 apontam, é "muito impreciso".
Os arquivos, portanto, validam que esta é uma questão de pesquisa central e relevante em finanças modernas.

Este é o *insight* mais importante derivado da *combinação* dos dois arquivos enviados 1 em contraponto ao TCC.
**O Paradoxo da Metodologia do TCC:** O TCC 1 enquadra a Média Histórica (HA) e o ARIMA como *concorrentes* mutuamente exclusivos. O TCC cria $\mu_{\text{HA}}$ e otimiza (Carteira 1). Depois, cria $\mu_{\text{ARIMA}}$ e otimiza (Carteira 2). Isso força o otimizador a *confiar 100%* em um ou no outro.
**A Crítica a esta Competição:** O problema com a Carteira 1 ($\mu_{\text{HA}}$) é que ela é estável, mas "burra" (ignora *priors* econômicos, como os slides 1 apontam). O problema com a Carteira 2 ($\mu_{\text{ARIMA}}$) é que ela é "inteligente", mas *instável*. Ao alimentar *apenas* a previsão ARIMA no otimizador M-V, o portfólio torna-se *ainda mais* suscetível ao "maximizador de erros" 1 do que com a média histórica. O otimizador M-V atribuirá pesos extremos (e não-intuitivos) a quaisquer ativos que o modelo ARIMA preveja ter um retorno marginalmente maior.
**A Solução (Black-Litterman):** Os *dois* arquivos que o TCC enviou para análise 1 são sobre o modelo Black-Litterman (BL), que foi *literalmente inventado* por Fischer Black e Robert Litterman para resolver este exato problema de otimizadores instáveis e *inputs* preditivos.
O modelo BL (conforme descrito nos slides 1) não descarta a Média Histórica. Ele a usa (via pesos de capitalização de mercado) para calcular o "prior" de equilíbrio, $\Pi$.1 Este $\Pi$ é o "ponto de partida" estável, que representa o consenso do mercado. Em seguida, o modelo BL pega a previsão (o *output* do ARIMA, como em 1) e a trata como uma "visão" ($Q$).
A fórmula BL 1 então *mistura* (via lógica Bayesiana) o $\Pi$ estável com a visão $Q$ preditiva, ponderada pela confiança ($\Omega$) que se tem na visão. O resultado é um *novo vetor de retorno esperado*, $E$, que é uma *mistura ponderada* e mais robusta. É o "melhor dos dois mundos": a estabilidade do mercado e a inteligência da previsão.
**Implicação para o TCC:** O TCC está atualmente comparando A vs. B. A literatura enviada 1 sugere que a melhor resposta não é A ou B, mas sim C = $\text{BL}(\text{A}, \text{B})$. Isso representa uma oportunidade de "nível A+" para o TCC, que será explorada na Seção IV de recomendações.

- Limitações e a Realidade dos Mercados
- 
As críticas à MPT e ao CAPM surgem da desconexão entre esses axiomas ideais e a realidade empírica dos mercados financeiros.
**Distribuições Não-Normais (Caudas Gordas):** A MPT assume que os retornos seguem uma distribuição Normal (Gaussiana), o que justifica o uso da variância como medida completa de risco. Contudo, estudos seminais de Benoit Mandelbrot  e Eugene Fama  demonstraram que os preços de ativos exibem "caudas gordas" (*fat tails*) e leptocurtose excessiva.76 Na realidade, eventos extremos (como *crashes* de mercado de 10 ou 20 desvios padrão) ocorrem com frequência muito maior do que a prevista pela curva normal. O uso da variância subestima drasticamente o risco real de eventos catastróficos ("Cisnes Negros"), tornando a MPT perigosa em momentos de crise.
**Limitações da Variância:** Como discutido na seção 2.2, a variância penaliza igualmente a volatilidade para cima (lucro) e para baixo (perda). Investidores reais, no entanto, exibem aversão à perda, não à volatilidade *per se*. A semivariância ou métricas de *downside risk* seriam descritores mais precisos da utilidade do investidor, mas a inércia da tradição MPT mantém a variância como padrão.
**Violações da Racionalidade:** A Economia Comportamental (Kahneman e Tversky) documentou sistemáticas violações dos axiomas VNM. O "efeito certeza" e a "aversão à perda" (Teoria da Perspectiva) mostram que investidores reais frequentemente violam os axiomas de Independência e Dominância, comportando-se de maneira inconsistente com a maximização da utilidade esperada.
Apesar dessas falhas descritivas, a estrutura criada por Markowitz, Tobin e Sharpe permanece a *lingua franca* das finanças. Conceitos como diversificação, fronteira eficiente, Beta e Índice de Sharpe fornecem as ferramentas heurísticas indispensáveis para a alocação de ativos institucional, servindo como um modelo normativo de como o mercado *deveria* funcionar sob condições ideais, mesmo que a realidade frequentemente divirja do modelo.
###

Embora a Teoria Moderna do Portfólio (MPT), estabelecida por Markowitz , tenha revolucionado as finanças ao quantificar a diversificação, sua dependência da variância como única medida de risco impõe limitações severas em mercados reais. A MPT assume implicitamente que os retornos dos ativos seguem uma distribuição normal (Gaussiana) e que a função de utilidade do investidor é quadrática. Contudo, evidências empíricas robustas demonstram que os retornos financeiros, especialmente em mercados emergentes como o brasileiro, apresentam distribuições leptocúrticas (caudas pesadas) e assimetria negativa 
Neste contexto, a variância falha por ser uma medida simétrica: ela penaliza os desvios positivos (ganhos acima da média) com a mesma severidade que os desvios negativos (perdas) (NAWROCKI, 1999). A Teoria Pós-Moderna do Portfólio (PMPT) surge, portanto, como uma evolução necessária, fundamentada na premissa de que o risco deve ser tratado como a possibilidade de não atingir um retorno mínimo aceitável (Target Minimum Return), focando exclusivamente no *downside risk*. 
A formalização da PMPT é creditada a Rom e Ferguson (1993, 1994), que identificaram falhas críticas nos softwares de otimização baseados na MPT e propuseram uma estrutura que incorpora a assimetria das distribuições. Paralelamente, o *Pension Research Institute*, através de pesquisadores como Frank Sortino, operacionalizou a teoria dos Momentos Parciais Inferiores (LPM - *Lower Partial Moments*), desenvolvendo métricas como o Índice de Sortino, que ajusta o retorno pelo risco de *downside* em vez do desvio padrão total.

A resiliência da MPT no meio acadêmico e profissional, apesar de suas limitações conhecidas, deve-se à sua simplicidade pedagógica. No entanto, a aplicação da MPT em mercados reais exige a aceitação de pressupostos que, quando violados, podem levar a alocações de ativos subótimas e a uma subestimação perigosa dos riscos extremos. A PMPT surge como uma resposta direta a duas críticas estruturais à MPT: a suposição de distribuição normal dos retornos e a função de utilidade quadrática do investidor.

Para superar as limitações da variância, a PMPT adota a estrutura matemática dos Momentos Parciais Inferiores (*Lower **Partial* *Moments* - LPM). Desenvolvida teoricamente por Bawa  e expandida por Fishburn , a família de métricas LPM oferece uma generalização flexível para mensurar o risco abaixo de um limiar específico.31 A elegância dos LPMs reside na sua capacidade de incorporar diferentes graus de aversão ao risco através de um único parâmetro, $n$ (a ordem do momento).

Embora a Teoria Moderna do Portfólio (MPT) tenha estabelecido os fundamentos da diversificação, sua implementação prática via otimização de Média-Variância (MV) enfrenta desafios críticos. Conforme apontam Michaud  e Best e Grauer , o otimizador MV tende a funcionar como um "maximizador de erros", sendo extremamente sensível aos inputs de retorno esperado. Pequenas variações nas estimativas podem resultar em carteiras extremas, pouco diversificadas e instáveis (soluções de canto), que não refletem a intuição do investidor.
Em resposta a essas limitações, Black e Litterman (1990, 1992) propuseram um modelo que mitiga a sensibilidade aos erros de estimação e produz alocações mais estáveis e robustas. O Modelo Black-Litterman (BL) não substitui a otimização MV, mas aprimora a estimativa dos retornos esperados — o input mais volátil do processo — utilizando uma abordagem Bayesiana para combinar informações de mercado com expectativas específicas do investidor.

**3.1.1 O Contexto da Goldman Sachs e a Colaboração Black-****Litterman**
A transição de Fischer Black da academia para a prática financeira em 1984, ao juntar-se à Goldman Sachs, marcou o início de uma era de ouro na engenharia financeira aplicada. Black, já reverenciado por sua contribuição seminal ao modelo de precificação de opções Black-Scholes , assumiu a liderança do Grupo de Estratégias Quantitativas da firma. Neste ambiente, ele colaborou estreitamente com Robert Litterman, um econometrista renomado e então vice-presidente da divisão de pesquisa de Renda Fixa.
A motivação primordial para o desenvolvimento do modelo não foi puramente acadêmica, mas sim uma necessidade comercial urgente. A Goldman Sachs buscava oferecer aos seus clientes institucionais uma abordagem quantitativa e disciplinada para estruturar portfólios de títulos internacionais (*global **bonds*) e moedas. No entanto, Black e Litterman observaram que os modelos de otimização quantitativa existentes, baseados na MPT clássica, eram raramente utilizados na sua forma pura. Para tornar os resultados da otimização "palatáveis", os gestores eram forçados a impor restrições artificiais severas — como limites rígidos de posição por ativo ou proibição de vendas a descoberto — que, na prática, anulavam a inteligência matemática do otimizador.
Em 1990, a dupla apresentou internamente uma abordagem inovadora que permitia aos gestores incorporar suas visões de mercado sem destruir a estrutura de diversificação do portfólio. Inicialmente focado em renda fixa, o modelo foi expandido para ações em 1991 e formalizado academicamente com a publicação de dois artigos fundamentais: "Asset Allocation: Combining Investor Views with Market Equilibrium" no *The **Journal* *of* *Fixed** Income*  e "Global Portfolio Optimization" no *Financial **Analysts* *Journal* .5 Estes trabalhos estabeleceram o BL não apenas como uma ferramenta proprietária da GSAM, mas como o novo padrão da indústria para a alocação de ativos, resolvendo o dilema da sensibilidade aos *inputs*.
**3.1.2 A Crítica à MPT: O Dilema da "Maximização de Erros" e as Soluções de Canto**
A inovação de Black e Litterman foi uma resposta direta e técnica às falhas patológicas da otimização de Markowitz quando alimentada com estimativas ruidosas. A literatura acadêmica da época, com destaque para os trabalhos de Richard Michaud , já havia diagnosticado que a MVO atua, na prática, como um "maximizador de erros" (*error* *maximizer*).
O mecanismo da "Maximização de Erros" opera da seguinte forma: os algoritmos de otimização quadrática são matematicamente desenhados para explorar as características extremas dos dados. Eles buscam ativos com a maior razão retorno/risco marginal. No entanto, em finanças, as estimativas de retorno esperado ($\mu$) são notoriamente imprecisas e ruidosas. Quando um ativo apresenta uma estimativa de retorno excepcionalmente alta, é estatisticamente provável que essa estimativa contenha um erro positivo significativo (viés de otimismo ou ruído de amostra). O otimizador, incapaz de distinguir entre um "alpha" verdadeiro e um erro de estimação, aloca agressivamente capital neste ativo. Inversamente, ativos com erros de estimação negativos são penalizados e removidos do portfólio. Consequentemente, o portfólio "ótimo" resultante é, na verdade, uma coleção concentrada dos ativos com os maiores erros de estimação positiva, desempenhando frequentemente pior fora da amostra do que um portfólio ingênuo de pesos iguais ($1/N$).
Este fenômeno manifesta-se em duas patologias observáveis que inviabilizam o uso institucional da MPT pura:
**Instabilidade Crônica dos Pesos:** A topologia da fronteira eficiente em torno do ótimo é frequentemente "plana" ou instável. Pequenas alterações nos *inputs* (ex: alterar a expectativa de retorno de um ativo em 0,5%) podem causar mudanças drásticas nas alocações sugeridas (ex: o peso do ativo salta de 0% para 40%). Isso gera custos de transação proibitivos e mina a confiança do comitê de investimento na robustez do modelo.
**Soluções de Canto (*****Corner ******Solutions*****):** Quando restrições de não-negatividade (proibição de *short **selling*) são aplicadas, o otimizador tende a colapsar a diversificação. A solução matemática frequentemente reside nos vértices do conjunto viável, resultando em portfólios binários onde a vasta maioria dos ativos tem peso zero e o capital é concentrado em poucos "vencedores" estatísticos. Tais portfólios são intuitivamente rejeitados por gestores prudentes, pois contradizem o princípio fundamental da diversificação.
Black e Litterman identificaram que a raiz desse problema não estava na otimização em si, mas na impossibilidade de estimar o vetor de retornos esperados ($\mu$) com precisão suficiente usando apenas dados históricos. A solução proposta foi, portanto, metodológica: substituir a estimativa histórica puramente estatística por uma estimativa Bayesiana ancorada na teoria econômica.
**3.6 Comparação Crítica: BL, MPT e PMPT**
A análise da evolução dos modelos de alocação exige distinguir claramente o papel de cada teoria. Uma confusão comum é tratar BL e PMPT como concorrentes diretos, quando na verdade atuam em dimensões distintas do problema de portfólio.
**3.6.1 MPT vs. BL: A Correção da Estabilidade**
A MPT (Markowitz) falha primariamente na **sensibilidade aos inputs**. Como discutido (Seção 3.1.2), a MPT maximiza erros de estimação, levando a soluções de canto. O BL corrige isso não alterando o otimizador, mas "limpando" os inputs. Ao ancorar o retorno esperado ($\mu$) no equilíbrio, o BL atua como um filtro Bayesiano que remove o ruído estatístico. O resultado são portfólios que, mesmo sem restrições, tendem a ser diversificados e intuitivos, ao contrário das alocações binárias da MPT pura.
**3.6.2 BL vs. PMPT: Complementaridade Estrutural**
A Teoria Pós-Moderna do Portfólio (PMPT) critica a MPT por um motivo diferente: a **medida de risco**. A PMPT argumenta que a variância (utilizada tanto na MPT quanto no BL clássico) é uma medida falha porque penaliza a volatilidade positiva (*upside*) tanto quanto a negativa. A PMPT propõe métricas assimétricas como Semivariância, *Downside* *Deviation* e CVaR (*Conditional* *Value* *at** Risk*).
A relação entre BL e PMPT é de **complementaridade**, não substituição:
**Black-****Litterman** foca na melhoria da **Estimativa de Retorno** (Primeiro Momento, $\mu$).
**PMPT** foca na melhoria da **Medição de Risco** (Segundos Momentos e Caudas).
Consequentemente, a fronteira da pesquisa atual em finanças quantitativas propõe modelos híbridos **"BL-****Mean****-****CVaR****"**. Nesta abordagem, utiliza-se a estrutura Bayesiana do BL para derivar o vetor de retornos esperados robustos ($\mu_{BL}$) e, subsequentemente, alimenta-se este vetor em um otimizador que minimiza o CVaR ou maximiza o Índice de Sortino (PMPT), em vez de minimizar a variância. Estudos empíricos indicam que essa combinação "Inputs BL + Otimizador PMPT" gera os portfólios mais robustos *out-**of**-sample*, protegendo contra riscos de cauda enquanto evita a instabilidade de alocação.
**Tabela 3.1: Síntese Comparativa dos Modelos**

| Dimensão Analítica | MPT (Markowitz) | Black-Litterman (BL) | PMPT (Pós-Moderna) |
| --- | --- | --- | --- |
| Foco Principal | Diversificação Matemática | Estabilidade da Estimativa ($\mu$) | Assimetria do Risco (Downside) |
| Input de Retorno | Histórico (Instável) | Equilíbrio + Visões (Bayesiano) | Histórico ou Subjetivo |
| Tratamento de Erros | Maximiza Erros (Michaud) | Mitiga via Shrinkage (Prior) | Neutro (Depende do Input) |
| Medida de Risco | Variância (Simétrica) | Variância (Canônico) | Semivariância, CVaR, LPM |
| Resultado Típico | Soluções de Canto (Instáveis) | Portfólio Diversificado (Estável) | Proteção de Cauda e Assimetria |

Em resposta às críticas sobre a normalidade dos retornos, utiliza-se o Conditional Value at Risk (CVaR) como função objetivo. O CVaR minimiza a perda esperada na cauda esquerda da distribuição (piores 5% dos cenários), sendo uma medida de risco coerente e convexa,,.

A formalização do termo "Teoria Pós-Moderna do Portfólio" é creditada aos desenvolvedores de software Brian M. Rom e Kathleen Ferguson, que publicaram trabalhos seminais em 1993 e 1994 no The Journal of Investing. Rom e Ferguson identificaram falhas críticas nos softwares de otimização baseados na MPT e propuseram uma nova estrutura que incorporava a assimetria das distribuições de retorno.
Paralelamente, o suporte acadêmico para a PMPT foi solidificado pelo Pension Research Institute (PRI) na Universidade Estadual de São Francisco. Pesquisadores como Dr. Frank Sortino e Dr. Hal Forsey, trabalhando com base nos teoremas de Bawa  e Fishburn , desenvolveram algoritmos práticos para calcular o risco de downside e a distribuição log-normal de três parâmetros, que se ajustava melhor aos dados de mercado do que a distribuição normal da MPT. O trabalho de Sortino, em particular, foi crucial para traduzir a teoria complexa dos momentos parciais em ferramentas aplicáveis, culminando na criação do Índice de Sortino, que se tornou o padrão da análise de desempenho ajustada ao risco de downside.

A crítica mais devastadora e pragmaticamente relevante à implementação institucional da MPT foi articulada por Richard Michaud , que cunhou o termo "maximizador de erros" (error maximizer) para descrever os otimizadores de média-variância. A intuição subjacente a esta crítica é estatisticamente profunda e deve ser o ponto de partida para qualquer discussão sobre o modelo Black-Litterman. Os algoritmos de otimização quadrática são desenhados para explorar as extremidades do conjunto de oportunidades de investimento. Eles buscam, matematicamente, os ativos que oferecem as maiores razões de retorno marginal por unidade de risco marginal. 
No entanto, em finanças, o vetor de retornos esperados  é uma variável estocástica não observável, que deve ser estimada a partir de dados históricos ou modelos preditivos. Essas estimativas são intrinsecamente ruidosas e instáveis. Quando um ativo apresenta uma estimativa de retorno excepcionalmente alta, é estatisticamente provável que essa estimativa contenha um componente significativo de erro positivo (viés de otimismo ou ruído amostral). O otimizador de Markowitz, cego à incerteza epistêmica da estimativa, trata esse valor como uma verdade determinística e aloca o máximo capital possível nesse ativo. Inversamente, ativos com erros de estimação negativos são penalizados e excluídos da carteira. 
O resultado prático, frequentemente observado em backtests no mercado brasileiro, é a construção de "Soluções de Canto" (Corner Solutions): portfólios binários, concentrados em poucos ativos, que contradizem o próprio princípio da diversificação que a teoria pretendia promover. Em um exercício de simulação, tais carteiras frequentemente apresentam desempenho fora da amostra (out-of-sample) inferior a estratégias ingênuas de equiponderação , pois o otimizador alavancou os erros de previsão em vez de capturar o prêmio de risco verdadeiro. Esta instabilidade — onde pequenas alterações nos inputs (ex: 0,1% na média estimada de uma blue chip como a Petrobras) geram mudanças drásticas nos pesos (ex: 0% para 40% de alocação) — torna a MPT pura inutilizável para a gestão profissional de grandes volumes de capital, onde os custos de transação e a coerência da estratégia são imperativos.

A evolução da gestão de portfólios institucionais sofreu uma inflexão paradigmática no início da década de 1990, impulsionada pelas limitações práticas da Teoria Moderna do Portfólio (MPT) de Harry Markowitz. Embora a MPT tenha fornecido a fundação matemática para a diversificação, estabelecendo a média-variância como o framework dominante para a análise de risco e retorno, a sua aplicação direta através da Otimização de Média-Variância (MVO) revelou-se profundamente problemática para gestores profissionais. Foi neste contexto de dissonância entre a elegância teórica acadêmica e a frustração prática operacional que Fischer Black e Robert Litterman, atuando na divisão de Gestão de Ativos da Goldman Sachs (GSAM), desenvolveram o Modelo Black-Litterman (BL).

- A Crítica à MPT: O Dilema da "Maximização de Erros" e as Soluções de Canto

A inovação de Black e Litterman foi uma resposta direta e técnica às falhas patológicas da otimização de Markowitz quando alimentada com estimativas ruidosas. A literatura acadêmica da época, com destaque para os trabalhos de Richard Michaud , já havia diagnosticado que a MVO atua, na prática, como um "maximizador de erros" (*error* *maximizer*). O algoritmo de otimização, ao buscar matematicamente a fronteira eficiente, tende a sobrealocar capital em ativos com retornos esperados marginalmente superiores e subestimar aqueles com retornos inferiores, ignorando que essas diferenças podem ser meramente fruto de erros de estimação ou ruído estatístico.
Black e Litterman  articularam que o problema central não residia na matemática da otimização em si, mas na dificuldade intrínseca de estimar o vetor de retornos esperados . Enquanto a matriz de covariância  é relativamente estável e previsível ao longo do tempo, os retornos esperados são notoriamente voláteis e difíceis de prever. Na abordagem tradicional da MPT, um gestor é forçado a fornecer uma estimativa de retorno pontual para cada ativo no universo de investimento. Para um fundo global, isso poderia significar estimar retornos para centenas de ativos, muitos dos quais o gestor não possui uma opinião formada (visão neutra). A inserção de estimativas "neutras" ou baseadas apenas em médias históricas introduzia vieses que resultavam em portfólios extremos, instáveis e pouco diversificados, conhecidos como "soluções de canto" (corner solutions).
A solução proposta pelo modelo BL foi inverter o processo de engenharia do portfólio. Em vez de exigir que o investidor construísse as estimativas de retorno "do zero" (from scratch), o modelo parte de uma premissa de neutralidade baseada no equilíbrio de mercado. A filosofia subjacente é que, se o investidor não possui informações privilegiadas ou visões específicas que contradigam o mercado, a melhor estimativa de retorno é aquela que justifica a atual capitalização de mercado dos ativos. Apenas quando o investidor possui uma convicção forte (uma "visão") é que o portfólio deve desviar-se deste equilíbrio

A MPT (Markowitz) falha primariamente na **sensibilidade aos inputs**. Como discutido (Seção 3.1.2), a MPT maximiza erros de estimação, levando a soluções de canto. O BL corrige isso não alterando o otimizador, mas "limpando" os inputs. Ao ancorar o retorno esperado  no equilíbrio, o BL atua como um filtro Bayesiano que remove o ruído estatístico. O resultado são portfólios que, mesmo sem restrições, tendem a ser diversificados e intuitivos, ao contrário das alocações binárias da MPT pura.
Apesar de sua elegância, o modelo BL clássico de 1992 não é isento de falhas, muitas das quais derivam de suas premissas simplificadoras herdadas da MPT.

Apesar de seu status de Prêmio Nobel, a MPT enfrenta severas limitações práticas e teóricas que impulsionaram a evolução subsequente da teoria das carteiras. A literatura aponta consistentemente que a MPT reduz as complexidades do universo de investimentos a apenas duas dimensões (risco e retorno), o que, embora elegante, é frequentemente insuficiente para modelar a realidade dos mercados.
O modelo Média-Variância é notoriamente sensível aos seus *inputs*: o vetor de retornos esperados e a matriz de covariância. Pequenas alterações nas estimativas de retorno esperado podem levar a mudanças drásticas nos pesos dos ativos, resultando frequentemente em "soluções de canto" (*corner solutions*), onde o portfólio se concentra excessivamente em poucos ativos e zera a posição em muitos outros.
Este fenômeno é frequentemente descrito como "maximização de erro de estimativa". O otimizador matemático não consegue distinguir entre uma oportunidade de investimento real e um erro de estimativa nos dados. Se um ativo tem um retorno histórico ligeiramente superestimado devido ao ruído estatístico, a MPT alocará agressivamente capital nesse ativo, amplificando o erro.9 Michaud  descreveu famosamente a otimização Média-Variância como um "amplificador de erros de estimativa".

Como consequência direta da adoção da PMPT, o Índice Sharpe foi substituído pelo Índice Sortino. Enquanto o Índice Sharpe divide o excesso de retorno pelo desvio padrão total (penalizando a volatilidade positiva), o Índice Sortino divide o excesso de retorno pelo **Desvio de Downside** ($\sigma_d$), que é a raiz quadrada do LPM de grau 2.
$$\text{Índice Sortino} = \frac{E - \tau}{\sqrt{LPM_2(\tau)}}$$
O Índice Sortino é superior para avaliar portfólios com distribuições não normais ou com estratégias que geram assimetria positiva (como opções ou *hedge funds*). Um Índice Sortino alto indica que o portfólio gera retornos elevados com baixo risco de perdas significativas, o que é a verdadeira meta da maioria dos investidores.
**Independência da Normalidade:** O modelo MAD não requer que os retornos sejam normalmente distribuídos, tornando-o mais robusto em mercados reais com caudas gordas.
**Eficiência Computacional:** Elimina a necessidade de calcular e armazenar a matriz de covariância, que cresce quadraticamente com o número de ativos. Para um universo de 1.000 ações, a MPT requer o cálculo de 500.000 covariâncias, enquanto o MAD trabalha diretamente com os dados históricos.
**Desempenho Empírico:** Estudos de backtesting (e.g., no S&P 500) mostram que portfólios MAD frequentemente superam portfólios Média-Variância, produzindo maiores Índices de Sharpe e retornos totais.
Uma extensão moderna significativa é o modelo **MAD-Entropia**. Pesquisas recentes sugerem incorporar a maximização da entropia (medida de diversidade de Shannon) à função objetivo do MAD. Enquanto o MAD minimiza o risco, a entropia força uma maior diversificação dos pesos, evitando as soluções de canto que afligem a otimização pura. Estudos indicam que o modelo MAD-Entropia supera tanto o MAD tradicional quanto a diversificação ingênua (1/N) em termos de retorno ajustado ao risco.
Outra hibridização poderosa é o modelo **Beta-CVaR**, que combina o MAD com o *Conditional Value at Risk* (CVaR). Esta abordagem multiobjetivo permite ao investidor ponderar entre minimizar o desvio médio (risco "normal") e minimizar o risco de cauda extrema (CVaR), oferecendo uma proteção superior em períodos de crise financeira.
#### 2.4.2 A Crítica de Michaud : O "Maximizador de Erros"

A crítica mais relevante para a prática de gestão de portfólio vem de Richard Michaud, que rotulou os otimizadores de Média-Variância como "maximizadores de erro de estimação" (error maximizers). O algoritmo de Markowitz é matematicamente agnóstico à qualidade dos dados de entrada. Ele trata as estimativas de retorno e covariância como verdades determinísticas.
Na realidade, essas estimativas são ruidosas. Estatisticamente, os ativos que apresentam os maiores retornos históricos (e que o otimizador selecionará agressivamente) são frequentemente aqueles que tiveram "sorte" ou erro de estimação positivo. Inversamente, ativos com retornos subestimados são descartados. O resultado são portfólios "extremos", altamente concentrados em poucos ativos e instáveis, que tendem a ter desempenho medíocre fora da amostra (out-of-sample).
- Dfgdsgds **A Inadequação da Média Histórica ****Simple**
- A Evidência Empírica (DeMiguel & Nogales, 2009)
- **Crítica 2: Sensibilidade Extrema aos Inputs e Imprecisão da Média Histórica**
- **Crítica 3: Geração de Portfólios Não-Intuitivos e Altamente Concentrados**
- **Crítica 4: Ignorando Priors (Informações de Equilíbrio e Visões Subjetivas)**

- **A Tese: O Modelo Black-Litterman como Solução para o Erro de Estimação**
- O Framework Black-Litterman: Uma Abordagem Bayesiana para Síntese
- O "Prior" (Crença Inicial): O Equilíbrio de Mercado (Π)
- Derivação do Prior: A Otimização Reversa
- 
- Componente 2: As "Visões" (**P** e **Q**) - A Incorporação da Previsão
- Componente 3: A Incerteza da Visão (**Ω**) - A Quantificação da Confiança
- A Importância de **Ω** como Peso Bayesiano
  - 
- O "Posterior" (Resultado): O Retorno Esperado Combinado ()
Vantagens do Modelo Black-Litterman
- As principais vantagens do modelo são:
- **Estabilidade e Intuição:** O BL produz carteiras mais **equilibradas e estáveis** no tempo, pois utiliza os retornos de equilíbrio (Π) como um **centro de gravidade**. Isso leva a carteiras **mais intuitivas e diversificadas** em comparação com as soluções extremas geradas pelo M-V.
- **Mitigação de Erros de Estimação:** O BL foi elaborado para **controlar os comportamentos instáveis** do otimizador de Markowitz. Ele **mitiga o problema de maximizar os erros de estimação** ao espalhar os erros ao longo do vetor de retornos esperados.
- **Flexibilidade e Disciplina:** O modelo permite que o gestor da carteira **inclua suas expectativas** sobre o mercado de forma transparente e disciplinada. O gestor precisa apenas estimar os retornos esperados para os ativos sobre os quais possui uma visão, sem a necessidade de estimar o retorno esperado para todos os ativos da carteira.
- **Coerência Teórica:** O modelo é coerente com a **teoria financeira moderna**: se o investidor não manifestar qualquer expectativa, os retornos esperados posteriores serão iguais aos retornos de equilíbrio ( = Π).
- Em suma, o BL fornece uma **abordagem quantitativa teórica** para dar suporte à tomada de decisão de investimento, transformando o vetor de retornos esperados, que é o *input* mais sensível do modelo de Markowitz, em um dado de entrada **robusto, estável e economicamente fundamentado**.
  -

**2.2. Limitações Críticas do Paradigma Média-Variância**
2.2.1. A Crítica de Roll : A inobservabilidade da carteira de mercado e problemas de *benchmark*.
2.2.2. Mandelbrot e a Realidade Fractal: Caudas Gordas (*Fat **Tails*), Leptocurtose e a falácia da distribuição normal.
2.2.3. O Problema do Erro de Estimação: A otimização quadrática como "maximizadora de erros" e a instabilidade das soluções de canto.
2.2.4. Finanças Comportamentais: Vieses cognitivos (ancoragem, excesso de confiança) como limitadores da gestão discricionária humana.
**2.3. Teoria Pós-Moderna de Portfólio (PMPT) e Otimização Robusta**
2.3.1. Redefinindo Risco: Assimetria, Risco de *Downside* e a inadequação da variância simétrica.
2.3.2. Métricas Avançadas: Momentos Parciais Inferiores (LPM), Índice de Sortino e CVaR.
2.3.3. O Modelo de Desvio Absoluto Médio (MAD):
A transição da Programação Quadrática para Linear.
Robustez contra *outliers* e eficiência computacional em cenários não-gaussianos.
As críticas à MPT e ao CAPM surgem da desconexão entre esses axiomas ideais e a realidade empírica dos mercados financeiros.
**Distribuições Não-Normais (Caudas Gordas):** A MPT assume que os retornos seguem uma distribuição Normal (Gaussiana), o que justifica o uso da variância como medida completa de risco. Contudo, estudos seminais de Benoit Mandelbrot  e Eugene Fama  demonstraram que os preços de ativos exibem "caudas gordas" (*fat tails*) e leptocurtose excessiva.76 Na realidade, eventos extremos (como *crashes* de mercado de 10 ou 20 desvios padrão) ocorrem com frequência muito maior do que a prevista pela curva normal. O uso da variância subestima drasticamente o risco real de eventos catastróficos ("Cisnes Negros"), tornando a MPT perigosa em momentos de crise.
**Limitações da Variância:** Como discutido na seção 2.2, a variância penaliza igualmente a volatilidade para cima (lucro) e para baixo (perda). Investidores reais, no entanto, exibem aversão à perda, não à volatilidade *per se*. A semivariância ou métricas de *downside risk* seriam descritores mais precisos da utilidade do investidor, mas a inércia da tradição MPT mantém a variância como padrão.
**Violações da Racionalidade:** A Economia Comportamental (Kahneman e Tversky) documentou sistemáticas violações dos axiomas VNM. O "efeito certeza" e a "aversão à perda" (Teoria da Perspectiva) mostram que investidores reais frequentemente violam os axiomas de Independência e Dominância, comportando-se de maneira inconsistente com a maximização da utilidade esperada.
Apesar dessas falhas descritivas, a estrutura criada por Markowitz, Tobin e Sharpe permanece a *lingua franca* das finanças. Conceitos como diversificação, fronteira eficiente, Beta e Índice de Sharpe fornecem as ferramentas heurísticas indispensáveis para a alocação de ativos institucional, servindo como um modelo normativo de como o mercado *deveria* funcionar sob condições ideais, mesmo que a realidade frequentemente divirja do modelo.
# Capítulo 1: Fundamentação Teórica e Revisão Bibliográfica da Moderna Teoria do Portfólio

O documento apresenta duas teses de pesquisa conflitantes 1:
**Tese do Resumo:** O objetivo é "avaliar o desempenho de carteiras desenvolvidas de acordo com a Moderna Teoria das Carteiras (MPT) com a Pós-Moderna Teoria do Portifolio (PMPT)".1 Isso sugere uma *comparação de frameworks de otimização* (ex: Média-Variância vs. Média-Semivariância).
**Tese da Introdução:** A questão de pesquisa é "qual é o impacto da substituição da média histórica ($\mu$) por modelos de previsão estatísticos (ARIMA) e de *machine learning* (LSTM) na performance de portfólios otimizados pelo método de Markowitz".1 Isso sugere uma *melhoria de inputs* ($\mu$) dentro de um único *framework* (MPT).
Estas são duas pesquisas distintas. A Tese 2 (ARIMA/LSTM) é tecnicamente mais sofisticada, mais original no contexto de um TCC de graduação e aborda uma das críticas mais relevantes à MPT: o *erro de estimação* (estimation risk) dos retornos esperados.
Direcionamento Metodológico:
O TCC deve adotar a Tese 2 (ARIMA/LSTM) como seu foco exclusivo. O Resumo atual 1 deve ser descartado e reescrito ao final. Os conceitos da PMPT (mencionados na Tese 1) não serão o foco da otimização, mas serão reintegrados de forma elegante: serão usados como métricas de avaliação de desempenho (ex: Índice de Sortino, CVaR) para comparar as carteiras geradas pela Tese 2. Isso unifica todas as ideias presentes no documento.

Para a conclusão bem-sucedida do TCC, recomenda-se a seguinte ordem de atividades ("atividades menores"):
**Fase 1: Definição e Estruturação (Atividades Imediatas)**
**Atividade:** Corrigir a estrutura do arquivo .docx.
**Detalhe:** Renomear e reordenar os capítulos no Sumário para refletir a estrutura correta (Intro, Ref. Teórico, Metodologia, Resultados, Conclusão).
**Atividade:** Reescrever o Capítulo 1 (Introdução).
**Detalhe:** Utilizar os prompts da Parte 4 deste relatório para redefinir o problema de pesquisa, objetivos (geral e específicos) e justificativa, focando *exclusivamente* no tema ARIMA/LSTM e no erro de estimação de $\mu$.
**Fase 2: Fundamentação Teórica (Redação)**
**Atividade:** Completar o Capítulo 2 (Referencial Teórico).
**Detalhe:** O material existente sobre MPT, VaR e CVaR é um bom começo.1 Utilizar os prompts da Parte 4 para *adicionar* as seções críticas que estão faltando 1:
2.X Pós-Moderna Teoria de Carteiras (foco em Semivariância e Índice de Sortino).
2.X Modelos de Previsão de Séries Temporais (ARIMA).
2.X Modelos de *Machine Learning* (Redes Neurais LSTM).
**Fase 3: Execução Metodológica (Coleta e Modelagem)**
**Atividade:** Redefinir a Amostra e Coletar os Dados.
**Detalhe:** Substituir o critério de amostra vago ("volume de negócios superior a zero" 1) por um critério rigoroso de liquidez (ex: presença no IBOVESPA, volume médio diário). Coletar as séries temporais de preços.
**Atividade:** Escrever o roteiro (script) de *backtest*.
**Detalhe:** Definir em código (Python ou R) a lógica de *backtesting* (ex: janela deslizante *walk-forward*), o período de treino (ex: 60 meses) e o período de teste/rebalanceamento (ex: 1 mês).
**Atividade:** Executar os modelos preditivos.
**Detalhe:** Em cada janela de treino, treinar os modelos (ARIMA, LSTM) para prever o $\mu$ do próximo período de teste para cada ativo.
**Atividade:** Otimizar as carteiras.
**Detalhe:** Em cada período de teste, utilizar os $\mu$ previstos (Histórico, ARIMA, LSTM) e a matriz de covariância ($\Sigma$) histórica para calcular os pesos da carteira otimizada (ex: Max Sharpe).
**Fase 4: Análise e Redação Final**
**Atividade:** Gerar os resultados consolidados.
**Detalhe:** Calcular as métricas de performance (Sharpe, Sortino, Drawdown, Retorno Anualizado) para a série temporal de retornos de cada uma das carteiras simuladas e dos *benchmarks* (IBOV, CDI).
**Atividade:** Escrever o Capítulo 4 (Análise e Discussão dos Resultados).
**Detalhe:** Preencher as tabelas de resultados e interpretar graficamente a evolução do patrimônio.
**Atividade:** Escrever o Capítulo 5 (Conclusão).
**Detalhe:** Responder objetivamente à nova pergunta de pesquisa, discutir limitações e propor trabalhos futuros.
**Fase 5: Revisão e Fechamento**
**Atividade:** Escrever o Resumo (Abstract).
**Detalhe:** *Somente agora*, escrever o Resumo, garantindo que ele reflita o trabalho que foi *realmente* executado (ARIMA/LSTM).
**Atividade:** Revisão final de formatação e referências.

**Contextualização (O Cenário):**
(Manter os parágrafos 1 e 2 sobre a democratização da B3 e a entrada de pessoas físicas 1).
Como a MPT de Markowitz  se propõe como a solução *tradicional* para o problema desses novos investidores? (Descrever brevemente o dilema risco vs. retorno).
Qual é a principal *crítica* ou *limitação* da MPT na prática, especificamente em relação aos seus *inputs* (parâmetros de entrada)? (Aponte para a dificuldade de estimar $\mu$, o retorno esperado).
**Problematização (A Lacuna):**
Por que usar a média histórica simples dos retornos passados como uma estimativa para o retorno futuro ($\mu$) é problematicamente ingênuo? (Citar DeMiguel e Nogales , já presente em 1).
Como a instabilidade dos mercados emergentes, como o Brasil (volatilidade, assimetria, caudas longas), torna essa estimativa histórica ainda menos confiável?
Se os *inputs* (estimativas de retorno) são ruins, a otimização de Markowitz, mesmo sendo matematicamente elegante, produzirá carteiras "ótimas" que são, na verdade, subótimas (o chamado *erro de estimação* ou *estimation risk*).
Como modelos estatísticos (ARIMA) e de *machine learning* (LSTM) surgem como alternativas potenciais para *melhorar* a estimação desse $\mu$? Qual a promessa teórica deles (capturar dinâmicas temporais e não-linearidades que a média histórica ignora)?
**Questão de Pesquisa (O Foco Central - Corrigido):**
(Substituir a pergunta existente em 1 por esta): "Qual é o impacto no desempenho, ajustado ao risco, de carteiras Média-Variância otimizadas no mercado brasileiro, quando o *input* de retorno esperado ($\mu$) é estimado por modelos preditivos (ARIMA e LSTM) em comparação com a tradicional média histórica?"
**Objetivos:**
**Geral:** Avaliar o ganho de performance (se houver) ao aplicar modelos de previsão de séries temporais (ARIMA) e *machine learning* (LSTM) na estimação de retornos esperados para a otimização de portfólios de Markowitz no Brasil.
**Específicos:**
Revisar a literatura sobre MPT, suas limitações (especialmente o erro de estimação) e os fundamentos dos modelos ARIMA e LSTM.
Coletar e tratar dados de séries temporais de ativos listados na B3 (definir o período e critérios de liquidez).
Implementar e treinar os modelos ARIMA e LSTM para prever os retornos dos ativos em um esquema de *backtesting* robusto.
Construir (via simulação) carteiras otimizadas (ex: Max Sharpe) usando três fontes de $\mu$: (a) Média Histórica, (b) Previsão ARIMA, (c) Previsão LSTM.
Comparar o desempenho das carteiras (e *benchmarks* como IBOV e CDI) usando métricas de risco-retorno (ex: Sharpe, Sortino, Max Drawdown).
**Justificativa:**
Por que esta pesquisa é relevante para o investidor pessoa física no Brasil? (Ajuda a navegar a volatilidade com ferramentas mais robustas).
Qual a contribuição acadêmica? (Testa a eficácia de modelos de ML, um tema atual, em um *framework* clássico (MPT) no contexto específico do mercado brasileiro).
**Estrutura do Trabalho:**
(Corrigir este parágrafo, que está errado em 1, para refletir a nova estrutura): "Este trabalho está estruturado da seguinte forma: o Capítulo 2 apresenta o referencial teórico... O Capítulo 3 descreve a metodologia... O Capítulo 4 analisa os resultados... O Capítulo 5 apresenta as conclusões."

## Referências Bibliográficas

BLACK, Fischer; LITTERMAN, Robert. Asset allocation: combining investor views with market equilibrium. **The Journal of Fixed Income**, v. 1, n. 2, p. 7-18, 1990.

BLACK, Fischer; LITTERMAN, Robert. Global portfolio optimization. **Financial Analysts Journal**, v. 48, n. 5, p. 28-43, 1992.

BOYD, Stephen; JOHANSSON, Kelly; KAHN, Ronald N.; SCHIELE, Philipp; SCHMELZER, Thomas. **Markowitz Portfolio Construction at Seventy**. Stanford: Stanford University, 2024.

DAMODARAN, Aswath. **Investment Valuation: Tools and Techniques for Determining the Value of Any Asset**. 3. ed. New York: John Wiley & Sons, 2012.

DEMIGUEL, Victor; GARLAPPI, Lorenzo; NOGALES, Francisco J.; UPPAL, Raman. A generalized approach to portfolio optimization: improving performance by constraining portfolio norms. **Management Science**, v. 55, n. 5, p. 798-812, 2009.

GRAHAM, Benjamin; DODD, David. **Security Analysis**. New York: McGraw-Hill, 1934.

GUERARD, John B. (ed.). **Handbook of Portfolio Construction: Contemporary Applications of Markowitz Techniques**. New York: Springer, 2010.

KAHNEMAN, Daniel; TVERSKY, Amos. Prospect theory: an analysis of decision under risk. **Econometrica**, v. 47, n. 2, p. 263-291, 1979.

MARKOWITZ, Harry. Portfolio selection. **The Journal of Finance**, v. 7, n. 1, p. 77-91, 1952.

MARKOWITZ, Harry. **Portfolio Selection: Efficient Diversification of Investments**. New York: John Wiley & Sons, 1959.

ROCKAFELLAR, R. Tyrrell; URYASEV, Stanislav. Optimization of conditional value-at-risk. **Journal of Risk**, v. 2, n. 3, p. 21-41, 2000.

ROM, Brian M.; FERGUSON, Kathleen W. Post-modern portfolio theory comes of age. **The Journal of Investing**, v. 3, n. 3, p. 11-17, 1994.

RUBINSTEIN, Mark. Markowitz's 'Portfolio Selection': a fifty-year retrospective. **The Journal of Finance**, v. 57, n. 3, p. 1041-1045, 2002.

SORTINO, Frank A.; VAN DER MEER, Robert. Downside risk. **The Journal of Portfolio Management**, v. 17, n. 4, p. 27-31, 1991.

WILLIAMS, John Burr. **The Theory of Investment Value**. Cambridge: Harvard University Press, 1938.
