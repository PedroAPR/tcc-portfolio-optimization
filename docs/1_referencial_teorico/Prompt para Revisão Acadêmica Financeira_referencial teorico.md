# **Estrutura Avançada de Revisão Acadêmica em Finanças: Rigor Teórico, Normatização e Engenharia de Prompt para Correção de TCCs**

## **1\. Introdução: O Desafio da Revisão Crítica na Era da Inteligência Artificial**

A elaboração de um Trabalho de Conclusão de Curso (TCC) na área de Finanças Quantitativas e Gestão de Portfólios exige do estudante a navegação por um oceano teórico que se estende desde os axiomas de racionalidade de meados do século XX até as complexas modelagens multifatoriais contemporâneas. Para o revisor acadêmico — e, por extensão, para os sistemas de Inteligência Artificial incumbidos de auxiliar nessa tarefa —, o desafio transcende a mera verificação gramatical. Trata-se de validar a integridade epistemológica dos argumentos, a precisão das definições matemáticas e a aderência estrita às normas técnicas, que no cenário brasileiro são regidas pela Associação Brasileira de Normas Técnicas (ABNT). Com a atualização da NBR 10520 em julho de 2023, a complexidade normativa aumentou, criando um hiato entre o hábito acadêmico consolidado e a nova exigência regulatória.1  
Este relatório técnico tem como objetivo estabelecer as bases teóricas, metodológicas e normativas para a construção de um "Super-Prompt" de revisão para o NotebookLLM. A premissa central é que uma IA só pode corrigir um TCC com nível de excelência se for instruída com a profundidade de um examinador sênior. Portanto, não basta solicitar "corrija o texto"; é imperativo fornecer os critérios de demarcação científica que separam uma análise superficial de uma contribuição acadêmica robusta.  
O documento disseca os pilares fundamentais da teoria financeira — Teoria da Utilidade, Modern Portfolio Theory (MPT), Post-Modern Portfolio Theory (PMPT), Modelo Black-Litterman e Fatores Fama-French — identificando os erros conceituais mais frequentes em monografias de graduação e pós-graduação. Simultaneamente, analisa as nuances da escrita acadêmica, focando na impessoalidade, coesão textual e nas especificidades da nova norma de citações. A síntese desses elementos resulta em uma estratégia de Engenharia de Prompt capaz de transformar o NotebookLLM em um orientador virtual de alta precisão.

## **2\. Fundamentos da Decisão Racional: A Teoria da Utilidade**

Antes de adentrar nos modelos de otimização de portfólio, qualquer revisão bibliográfica em finanças deve demonstrar um entendimento sólido sobre *por que* e *como* os investidores tomam decisões sob incerteza. A ausência dessa fundamentação ou sua apresentação equivocada é um dos primeiros sinais de fragilidade teórica em um TCC.

### **2.1 O Teorema da Utilidade de Von Neumann-Morgenstern (VNM)**

A base axiomática da moderna teoria financeira repousa sobre o trabalho seminal de John von Neumann e Oskar Morgenstern, publicado em "Theory of Games and Economic Behavior" (1944). O teorema VNM estabelece que um agente racional, ao se deparar com escolhas arriscadas (loterias), não maximiza o valor monetário esperado, mas sim o valor esperado de uma função de utilidade.3  
Para um revisor de TCC, é crucial verificar se o estudante compreende que a racionalidade VNM não é uma afirmação sobre como as pessoas *realmente* agem (descritiva), mas sobre como elas *deveriam* agir para serem consistentes com suas preferências (normativa). O teorema depende de quatro axiomas fundamentais que devem ser rigorosamente definidos em qualquer trabalho que se proponha a discutir as bases da MPT:

1. **Completude (Completeness):** O investidor é capaz de ordenar qualquer par de loterias. Diante de A e B, ele prefere A (![][image1]), prefere B (![][image2]) ou é indiferente (![][image3]). A falha em reconhecer este axioma leva a modelos onde a decisão é paralisada pela indecisão.3  
2. **Transitividade (Transitivity):** A consistência lógica das preferências. Se um investidor prefere A a B, e B a C, ele obrigatoriamente deve preferir A a C. Violações deste axioma, comuns em experimentos psicológicos, destroem a possibilidade de criar uma função de utilidade coerente.3  
3. **Continuidade (Continuity):** Este axioma, frequentemente negligenciado em textos introdutórios, afirma que não há "infinitos" na preferência. Se ![][image4], existe uma probabilidade ![][image5] tal que o investidor é indiferente entre receber B com certeza ou participar de uma loteria que oferece A com probabilidade ![][image5] e C com probabilidade ![][image6]. É a base para o cálculo do "Equivalente de Certeza".3  
4. **Independência (Independence):** Talvez o mais controverso. Afirma que se ![][image1], então qualquer mistura de A com uma terceira loteria C deve ser preferida à mesma mistura de B com C. É a violação deste axioma que dá origem aos famosos paradoxos comportamentais discutidos mais adiante.3

Um TCC robusto deve conectar explicitamente a concavidade da função de utilidade (![][image7]) ao conceito de aversão ao risco. É comum encontrar estudantes que definem aversão ao risco meramente como "medo de perder dinheiro", sem a formalização matemática de que a utilidade marginal da riqueza é decrescente.5 O prompt de revisão deve, portanto, ser capaz de detectar a ausência dessa conexão formal.

### **2.2 Limitações e Paradoxos: A Crítica Necessária**

A revisão crítica não pode aceitar a Teoria da Utilidade VNM como um dogma inquestionável. O "Paradoxo de Allais" e o "Paradoxo de Ellsberg" são contraexemplos clássicos que demonstram violações do axioma da independência e a aversão à ambiguidade, respectivamente.3 Se o capítulo de revisão bibliográfica apresenta a utilidade esperada como uma descrição perfeita do comportamento humano, ignorando décadas de pesquisa em economia comportamental e psicologia cognitiva, ele falha em seu propósito acadêmico. A "nested gambling" (risco sobre riscos) é outro ponto cego que a teoria clássica VNM simplifica, mas que investidores reais enfrentam constantemente.3

## **3\. Modern Portfolio Theory (MPT): O Paradigma e suas Falhas**

Harry Markowitz, em 1952, revolucionou as finanças não por descobrir a diversificação, mas por quantificá-la. A Modern Portfolio Theory (MPT) transformou a gestão de investimentos de uma arte de seleção de ações ("stock picking") para uma ciência de construção de portfólios baseada em covariâncias. Contudo, a MPT é frequentemente mal interpretada ou aplicada fora de contexto em trabalhos acadêmicos.

### **3.1 A Mecânica Média-Variância**

O cerne da MPT é a simplificação do problema de decisão do investidor para dois momentos estatísticos: a média (retorno esperado) e a variância (risco). A fórmula da variância do portfólio é a equação mais emblemática deste campo e sua presença (e correta interpretação) é mandatória:  
$$ \\sigma\_p^2 \= \\sum\_{i} w\_i^2 \\sigma\_i^2 \+ \\sum\_{i} \\sum\_{j \\neq i} w\_i w\_j \\sigma\_i \\sigma\_j \\rho\_{ij} $$  
Um erro recorrente em TCCs é a afirmação de que a diversificação elimina o risco. O revisor deve exigir precisão: a diversificação, através de correlações imperfeitas (![][image8]), reduz o **risco idiossincrático** (ou não sistemático), mas é impotente contra o **risco sistemático** (de mercado).6 A distinção entre esses dois tipos de risco é o que justifica a existência de modelos de precificação como o CAPM, e a confusão entre eles denota falta de profundidade teórica.  
Além disso, a Fronteira Eficiente deve ser descrita não apenas como um lugar geométrico, mas como o conjunto de soluções ótimas para um problema de maximização de utilidade quadrática. Se o estudante discute a fronteira eficiente sem mencionar que ela pressupõe investidores racionais e avessos ao risco, a explicação está incompleta.6

### **3.2 As Premissas Frágeis e a Crítica Acadêmica**

A aplicação cega da MPT é um dos maiores alvos de crítica em bancas de defesa. O prompt de revisão deve verificar se o trabalho aborda as limitações estruturais do modelo:

1. **Normalidade dos Retornos:** A MPT assume que os retornos seguem uma distribuição elíptica conjunta, tipicamente a Normal (Gaussiana).10 No mundo real, os retornos financeiros exibem assimetria (skewness) e curtose (fat tails). Aplicar MPT em ativos como criptomoedas ou derivativos, que são inerentemente não normais, sem tecer ressalvas, é um erro metodológico grave. O revisor deve buscar termos como "leptocúrtico" ou "caudas gordas" na discussão das limitações.11  
2. **Variância como Proxy de Risco:** A MPT penaliza igualmente a volatilidade positiva (lucros acima da média) e a negativa (prejuízos). Racionalmente, investidores gostam de surpresas positivas. Tratar a variância total como "risco" é uma simplificação que, embora útil matematicamente, contradiz a intuição econômica básica.10  
3. **Estabilidade das Correlações:** O modelo assume que a matriz de covariância é conhecida e estável. Contudo, em momentos de crise ("market crashes"), as correlações tendem a convergir para 1, eliminando os benefícios da diversificação exatamente quando são mais necessários. Um TCC crítico deve mencionar esse fenômeno de "breakdown" das correlações.6

### **3.3 O Problema da Maximização de Erros**

Um aspecto prático frequentemente ignorado em trabalhos de graduação é a sensibilidade do otimizador de média-variância. O algoritmo de Markowitz é frequentemente chamado de "maximizador de erros" porque tende a alocar capital excessivo nos ativos com os maiores retornos esperados estimados e as menores correlações/variâncias estimadas.9 Como essas estimativas carregam erros estatísticos, o portfólio "ótimo" ex-ante costuma ter performance pobre ex-post. O revisor deve sugerir a discussão de técnicas de robustez, como o uso de estimadores de encolhimento (shrinkage) ou restrições de peso, para mitigar esse problema.11

## **4\. Post-Modern Portfolio Theory (PMPT): A Evolução Assimétrica**

A Post-Modern Portfolio Theory (PMPT) surgiu como uma resposta direta às limitações da MPT, especificamente no que tange à definição de risco e à distribuição dos retornos. O termo foi cunhado em 1991 pelos empreendedores de software Brian M. Rom e Kathleen Ferguson, ganhando tração acadêmica ao longo da década de 1990\.7

### **4.1 Histórico e Autoria Seminal**

É imperativo que a revisão bibliográfica atribua corretamente a paternidade da PMPT. Embora Frank Sortino seja frequentemente associado ao conceito (devido ao índice Sortino), os trabalhos fundadores que estabeleceram a rubrica "Post-Modern" são os artigos de Rom e Ferguson publicados no *The Journal of Investing* em 1993 ("Post-Modern Portfolio Theory Comes of Age") e 1994\.10 A confusão entre os autores ou a omissão de Rom e Ferguson deve ser corrigida pelo prompt. Além disso, a menção ao Pension Research Institute (PRI) da Universidade de São Francisco é relevante para traçar a genealogia acadêmica da teoria.12

### **4.2 Downside Risk vs. Desvio Padrão**

A ruptura epistemológica da PMPT reside na redefinição de risco. Enquanto a MPT vê risco como volatilidade em torno da média, a PMPT o define como a probabilidade e a magnitude dos retornos abaixo de um alvo específico, denominado Retorno Mínimo Aceitável (MAR \- Minimum Acceptable Return).12  
Essa distinção leva ao conceito de **Semivariância** ou **Desvio Padrão de Downside**. A tabela a seguir resume as diferenças fundamentais que o TCC deve explicitar:

| Característica | Modern Portfolio Theory (MPT) | Post-Modern Portfolio Theory (PMPT) |
| :---- | :---- | :---- |
| **Definição de Risco** | Variância / Desvio Padrão (Total) | Downside Deviation (Abaixo do MAR) |
| **Distribuição Assumida** | Normal (Simétrica) | Log-Normal ou Qualquer Distribuição Assimétrica |
| **Objetivo do Investidor** | Maximizar Retorno para dada Variância | Maximizar Retorno para dado Downside Risk |
| **Métrica de Performance** | Índice de Sharpe | Índice de Sortino |
| **Premissa Psicológica** | Aversão à Variância | Aversão à Perda (Loss Aversion) |

### **4.3 O Índice de Sortino e a Assimetria de Volatilidade**

Um erro técnico comum em TCCs é a formulação do Índice de Sortino. Muitos estudantes substituem apenas o denominador do Sharpe (Desvio Padrão) pelo Downside Deviation, mantendo o Ativo Livre de Risco no numerador. A formulação purista da PMPT, contudo, sugere que o numerador deve refletir o retorno excedente sobre o MAR (Target Return), garantindo consistência entre a medida de retorno e a medida de risco.10  
Adicionalmente, Rom e Ferguson introduziram o conceito de **Assimetria de Volatilidade (Volatility Skewness)**, que mede a razão entre a variância dos retornos acima da média e a variância abaixo da média.

* Se Volatility Skewness \= 1, a distribuição é simétrica (MPT funciona).  
* Se \> 1, há mais volatilidade positiva (bom para o investidor).  
* Se \< 1, há mais volatilidade negativa (perigoso).

Se o TCC analisa fundos de hedge ou estratégias de opções, a omissão dessas métricas da PMPT em favor do tradicional Sharpe é uma falha analítica que o revisor deve apontar.9

## **5\. Modelos de Fatores: A Revolução Fama-French**

A evolução da precificação de ativos moveu-se do modelo de fator único (CAPM) para modelos multifatoriais, culminando nos trabalhos de Eugene Fama e Kenneth French. A revisão de um TCC atualizado deve distinguir com clareza cristalina entre o modelo de 1993 e o de 2015, pois as implicações teóricas são drasticamente diferentes.

### **5.1 O Modelo de Três Fatores (1993)**

O modelo original expandiu o CAPM adicionando dois fatores baseados em anomalias empíricas observadas:

1. **SMB (Small Minus Big):** O prêmio de tamanho. Historicamente, empresas de pequena capitalização (Small Caps) tendem a superar as de grande capitalização (Large Caps), compensando o maior risco idiossincrático e menor liquidez.8  
2. **HML (High Minus Low):** O prêmio de valor. Empresas com alta razão Book-to-Market (Valor) superam empresas com baixa razão (Crescimento). Este fator foi a pedra angular do "Value Investing" acadêmico por décadas.8

### **5.2 O Modelo de Cinco Fatores (2015)**

Em 2015, Fama e French responderam às evidências de que o modelo de 3 fatores deixava muita variação inexplicada (alfa significativo), introduzindo dois novos fatores baseados no modelo de desconto de dividendos: 3\. **RMW (Robust Minus Weak):** O prêmio de rentabilidade. Empresas com rentabilidade operacional robusta superam aquelas com rentabilidade fraca. 4\. **CMA (Conservative Minus Aggressive):** O prêmio de investimento. Empresas que investem de forma conservadora (baixo crescimento de ativos) superam aquelas que investem agressivamente.16  
**Detalhe Crítico de Revisão:** O revisor deve verificar as definições precisas. A "Rentabilidade Operacional" no modelo FF5 não é o Lucro Líquido contábil simples. É definida como (Vendas \- Custos das Mercadorias Vendidas \- Despesas Gerais e Administrativas \- Juros) dividido pelo Patrimônio Líquido Contábil.16 O "Investimento" é medido pelo crescimento total de ativos. TCCs que usam definições genéricas de "lucro" falham em replicar a metodologia correta.

### **5.3 A Redundância do Fator HML**

O insight mais sofisticado que um prompt de revisão deve buscar é a discussão sobre a redundância do fator HML. No artigo de 2015, Fama e French descobriram que, ao incluir RMW e CMA, o fator HML (Valor) perde sua significância estatística para explicar os retornos médios no mercado americano.8 O fator HML torna-se redundante porque suas informações sobre retorno esperado são capturadas pelos fatores de rentabilidade e investimento. Um TCC que apresenta o modelo de 5 fatores e continua a exaltar o HML como um pilar independente, sem mencionar essa descoberta de redundância, demonstra falta de leitura crítica da fonte primária.

### **5.4 Metodologia de Construção (Double Sorting)**

Para trabalhos empíricos, é vital mencionar a metodologia de "2x3 double sorting". Os fatores não são construídos isoladamente; as ações são ordenadas primeiro por Tamanho (Small/Big) e depois pela característica de interesse (ex: High/Neutral/Low Book-to-Market). Isso resulta em 6 portfólios base para a construção dos fatores.8 A omissão desse detalhe metodológico compromete a replicabilidade do estudo.

## **6\. O Modelo Black-Litterman: A Abordagem Bayesiana**

O Modelo Black-Litterman (BL), desenvolvido no início da década de 1990 na Goldman Sachs por Fischer Black e Robert Litterman, representa a resposta da indústria às "soluções de canto" (corner solutions) irracionais produzidas pela otimização de média-variância pura.18

### **6.1 A Intuição e o Mecanismo**

Diferente de Markowitz, que exige que o investidor estime retornos absolutos do zero (uma tarefa propensa a erros massivos), o BL inverte o problema. Ele parte da premissa de que o mercado está em equilíbrio.

1. **O Prior (Equilíbrio de Mercado):** O ponto de partida é o portfólio de mercado implícito no CAPM. Assume-se que, se todos os investidores fossem racionais, os pesos de capitalização de mercado seriam ótimos. Isso gera um vetor de retornos esperados de equilíbrio (![][image9]).18  
2. **As Views (Opiniões Subjetivas):** O investidor insere suas visões específicas, que podem ser absolutas ("Petróleo vai render 10%") ou relativas ("Tecnologia vai superar Varejo em 2%"). A capacidade de processar views relativas é uma das grandes inovações práticas do modelo.18  
3. **A Combinação Bayesiana:** O modelo usa estatística bayesiana (ou a estratégia de estimativa mista de Theil) para "atualizar" o prior com as views, gerando um novo vetor de retornos esperados (![][image10]) que é uma média ponderada entre o equilíbrio e a opinião do investidor, ajustada pela confiança.20

### **6.2 O Parâmetro Tau (![][image11]) e a Incerteza**

Um ponto de profundidade técnica que o prompt deve verificar é a discussão sobre o escalar ![][image11]. Este parâmetro controla a incerteza associada ao Prior (Equilíbrio).

* Se ![][image11] é grande, o modelo confia pouco no equilíbrio e muito nas views.  
* Se ![][image11] é próximo de zero, o modelo adere quase totalmente ao portfólio de mercado.

A literatura acadêmica diverge sobre a calibração de ![][image11]. Alguns autores (Satchell e Scowcroft) sugerem ![][image12], enquanto outros (Meucci, Idzorek) argumentam por valores muito menores (![][image13], onde T é o tamanho da amostra). Um TCC que aplica Black-Litterman sem discutir a calibração de ![][image11] está incompleto metodologicamente.20

### **6.3 Cronologia e Fontes**

O revisor deve estar atento à cronologia. Embora desenvolvido internamente na Goldman Sachs em 1990, as publicações seminais ocorreram em 1991 (*Journal of Fixed Income*) e 1992 (*Financial Analysts Journal*).19 Citar apenas "Black & Litterman (1990)" refere-se geralmente a working papers ou à data de criação, mas para rigor acadêmico, os artigos publicados devem ser referenciados.

## **7\. Finanças Comportamentais: O Desafio à Racionalidade**

Nenhum TCC moderno sobre gestão de portfólio está completo sem abordar o "elefante na sala": a irracionalidade do investidor. As Finanças Comportamentais atacam diretamente os axiomas da Teoria da Utilidade VNM apresentados na Seção 2\.

### **7.1 Teoria do Prospecto (Prospect Theory)**

Desenvolvida por Daniel Kahneman e Amos Tversky em 1979, a Teoria do Prospecto é a principal alternativa descritiva à Utilidade Esperada. A revisão deve identificar três componentes chaves:

1. **Aversão à Perda (Loss Aversion):** A dor de perder $100 é psicologicamente cerca de duas vezes mais intensa do que o prazer de ganhar $100. Isso cria uma função de valor que é mais íngreme no domínio das perdas.22  
2. **Ponto de Referência:** Diferente da teoria clássica que foca na riqueza final, a Teoria do Prospecto foca em mudanças (ganhos e perdas) em relação a um ponto de referência neutro.22  
3. **Sensibilidade Decrescente:** A função de valor é côncava para ganhos (aversão ao risco) mas convexa para perdas (busca pelo risco). Isso explica o "Efeito Disposição" — a tendência de vender vencedores cedo demais e segurar perdedores por tempo demais, na esperança de recuperação.22

### **7.2 Contabilidade Mental e Heurísticas**

O conceito de **Contabilidade Mental** (Thaler, 1985\) viola o princípio da fungibilidade do dinheiro. Investidores separam dinheiro em "contas" mentais (ex: dinheiro do dividendo vs. dinheiro do salário) e têm propensões ao consumo diferentes para cada uma.24  
O revisor deve também verificar a correta aplicação de heurísticas:

* **Representatividade:** Julgar a probabilidade de um evento baseando-se em quão semelhante ele é a um estereótipo, ignorando as taxas base (base rate neglect). No mercado, isso se traduz em assumir que "boas empresas" são sempre "bons investimentos".15  
* **Ancoragem:** A fixação em valores passados irrelevantes (como o preço de compra) para tomar decisões de venda atuais.15

Se o TCC utiliza a hipótese de mercados eficientes como única verdade, o prompt de revisão deve sugerir a inclusão dessas críticas comportamentais para enriquecer a discussão.25

## **8\. Normatização Acadêmica: A Nova ABNT NBR 10520:2023**

A "forma" na academia é tão importante quanto o "conteúdo". No Brasil, a recente atualização da NBR 10520 (Citações), vigente desde 19 de julho de 2023, introduziu mudanças visuais drásticas. Muitos orientadores e alunos ainda operam sob a norma antiga (2002), tornando este um ponto crítico para a correção automatizada.

### **8.1 Principais Alterações da Norma**

A tabela abaixo deve ser utilizada pelo prompt para verificar a conformidade do texto:

| Elemento | Regra Antiga (2002) | Regra Nova (2023) | Impacto Visual |
| :---- | :---- | :---- | :---- |
| **Autor entre parênteses** | Caixa Alta: (SILVA, 2019\) | Caixa Baixa/Alta: (Silva, 2019\) | **Alto:** O texto fica "mais limpo". |
| **Pontuação em Citação Direta** | Ponto dentro das aspas: "texto." (AUTOR, ano). | Ponto após parênteses: "texto" (Autor, ano). | **Médio:** Alteração na lógica sintática. |
| **Uso de *et al.*** | Obrigatório para \>3 autores. | Opcional para qualquer nº de autores. | **Médio:** Permite citar todos se desejado. |
| **Indicação de Página** | Obrigatória em citações diretas. | Obrigatória. Se não houver (e-book), indicar localização/parágrafo. | **Baixo:** Mantém o rigor de localização. |
| **Citação de Entidade** | (BANCO CENTRAL, 2020\) | (Banco Central, 2020\) | **Alto:** Segue a regra de nomes próprios. |

.1

### **8.2 Impessoalidade e Coesão Textual**

Além das citações, a linguagem acadêmica brasileira exige impessoalidade. O uso da primeira pessoa ("Eu analisei", "Nós concluímos") é vedado em favor da voz passiva sintética ou analítica ("Analisou-se", "Foi concluído") ou da indeterminação do sujeito ("O estudo aponta").29  
A coesão textual é outro ponto de falha. Capítulos de revisão bibliográfica frequentemente se tornam "colchas de retalhos" ou listas de resumos ("Markowitz disse X. Sharpe disse Y. Fama disse Z."). O prompt deve exigir o uso de operadores argumentativos que conectem os autores em um diálogo (ex: "Em contrapartida à visão de Markowitz, Rom e Ferguson propõem...", "Corroborando a tese de Fama, Asness demonstra que...").32

## **9\. Estratégia de Engenharia de Prompt para o NotebookLLM**

Transformar este corpo de conhecimento em um prompt executável requer técnicas avançadas de Prompt Engineering. O NotebookLLM, sendo baseado em modelos de linguagem grandes, responde melhor a instruções estruturadas que definem persona, contexto, restrições e formato de saída.

### **9.1 Persona e Contexto (Role-Based Prompting)**

A instrução deve ancorar o modelo em uma persona de autoridade: *"Atue como um Professor Titular de Finanças Quantitativas e Metodologia Científica com 20 anos de experiência em bancas de doutorado."* Isso ajusta o tom (tone) para ser formal, crítico e didático, evitando a linguagem coloquial de chatbot.33

### **9.2 Cadeia de Pensamento (Chain of Thought \- CoT)**

Para garantir que a IA verifique a lógica interna dos modelos financeiros, o prompt deve instruir o raciocínio passo-a-passo. Exemplo: *"Para cada modelo discutido no texto, primeiro identifique se as premissas fundamentais (como normalidade ou racionalidade) foram apresentadas. Em seguida, verifique se as limitações críticas (como erro de estimação ou anomalias comportamentais) foram debatidas."*.34

### **9.3 Restrições Negativas e Instruções de Formato**

É vital instruir o modelo sobre o que *não* fazer.

* *"Não reescreva o texto do aluno, apenas aponte o erro e sugira a correção."*  
* *"Não invente referências. Use apenas o conhecimento canônico da literatura financeira."*  
* *"O output deve ser estruturado em seções Markdown claras, separando a Crítica Teórica da Correção Normativa."*.35

## **10\. O "Super-Prompt" Otimizado (Resultado Final)**

Com base na análise exaustiva acima, apresentamos a reescrita completa do prompt solicitado pelo usuário. Este prompt encapsula todo o rigor teórico de MPT, PMPT, Black-Litterman, Fatores e Comportamental, juntamente com as novas regras da ABNT 2023\.

# **Role: Examinador Sênior de TCC em Finanças e Especialista em Normas ABNT**

## **Contexto e Objetivo**

Você está atuando como um membro rigoroso de uma banca examinadora de TCC. Sua tarefa é revisar criticamente o capítulo de **Revisão Bibliográfica** submetido. O foco é duplo: (1) Garantir a precisão e profundidade teórica dos modelos financeiros discutidos e (2) Assegurar a conformidade estrita com a norma culta acadêmica e a **ABNT NBR 10520:2023**.

## **Instruções de Análise Teórica (Pilar de Conteúdo)**

Ao analisar o texto, verifique a presença e a correção dos seguintes conceitos fundamentais. Se houver superficialidade, erro conceitual ou omissão, aponte especificamente e explique o que falta, baseando-se na literatura canônica:

### **1\. Teoria da Utilidade e Racionalidade**

* **Verificação:** O texto menciona os axiomas de Von Neumann-Morgenstern (Completude, Transitividade, Continuidade, Independência)?  
* **Crítica:** Se o texto assume racionalidade perfeita sem mencionar as críticas comportamentais (Paradoxos de Allais/Ellsberg), aponte essa lacuna como falta de profundidade.

### **2\. Modern Portfolio Theory (MPT) \- Markowitz**

* **Erro Comum:** Verifique se o aluno afirma que a diversificação elimina *todo* o risco. Corrija para "risco idiossincrático/não-sistemático".  
* **Limitações:** O texto DEVE discutir a limitação da premissa de **Normalidade** dos retornos (assimetria/curtose) e o fato de que a variância penaliza ganhos (upside).  
* **Problema de Estimação:** Verifique se há menção ao problema de "maximização de erros" (sensibilidade extrema aos inputs de média e covariância).

### **3\. Post-Modern Portfolio Theory (PMPT)**

* **Autoria:** Certifique-se de que **Rom & Ferguson (1993/1994)** são citados como os criadores do termo PMPT, e não apenas Sortino.  
* **Conceitos Chave:** O texto distingue claramente **Downside Deviation** (risco abaixo do MAR) de Desvio Padrão? O **Índice de Sortino** está definido com o MAR (Target Return) e não apenas com a taxa livre de risco?  
* **Skewness:** Há menção à Assimetria de Volatilidade?

### **4\. Modelo Black-Litterman**

* **Mecanismo:** O texto explica que o modelo combina o **Equilíbrio de Mercado (CAPM Prior)** com **Views do Investidor** via abordagem Bayesiana?  
* **Vantagem:** O texto destaca que o BL resolve o problema das "soluções de canto" (portfólios concentrados) da MPT?  
* **Parâmetro Tau:** Existe discussão sobre a incerteza do prior (parâmetro ![][image11])?  
* **Citação:** As referências devem ser Black & Litterman (1991 ou 1992).

### **5\. Fatores Fama-French**

* **Distinção Crítica:** O texto confunde o modelo de 3 fatores (1993) com o de 5 fatores (2015)?  
* **Fatores 2015:** Se usar o modelo de 5 fatores, as definições de **RMW** (Rentabilidade Operacional) e **CMA** (Investimento/Crescimento de Ativos) estão corretas?  
* **Redundância do Valor:** O texto menciona a descoberta crucial de 2015 de que o fator **HML (Valor)** se torna redundante na presença de RMW e CMA? Se não, exija essa atualização.

### **6\. Finanças Comportamentais**

* **Teoria do Prospecto:** Verifique a correta aplicação dos conceitos de Aversão à Perda (Kahneman & Tversky, 1979\) e o formato em "S" da função de valor.

## **Instruções de Análise Normativa (Pilar ABNT NBR 10520:2023)**

Aplique rigorosamente as regras da atualização de **Julho de 2023**:

1. **Citações (AUTORIA):**  
   * **Regra:** Autores dentro dos parênteses devem ter apenas a primeira letra maiúscula (Caixa Alta/Baixa).  
   * *Errado:* (SILVA, 2020\)  
   * *Correto:* (Silva, 2020\)  
   * **Ação:** Se encontrar caixa alta, marque como erro de norma desatualizada.  
2. **Pontuação em Citações Diretas:**  
   * **Regra:** O ponto final deve ficar FORA dos parênteses de citação.  
   * *Errado:* "...conclusão do autor." (Souza, 2023).  
   * *Correto:* "...conclusão do autor" (Souza, 2023).  
3. **Uso de *et al.*:**  
   * Verifique a consistência. Se o texto usa *et al.* para 4 autores em um parágrafo e cita todos os nomes em outro, aponte a falta de padronização.  
4. **Estilo Acadêmico:**  
   * **Impessoalidade:** O texto deve estar em 3ª pessoa. Marque qualquer uso de "Eu", "Nós", "Meu trabalho".  
   * **Coesão:** Exija conectivos entre parágrafos. O texto não pode parecer uma lista de tópicos desconexos.

## **Formato de Saída (Output)**

Apresente sua revisão no seguinte formato estruturado:

1. **Diagnóstico Geral:** Um parágrafo resumindo a qualidade do capítulo.  
2. **Análise de Profundidade Teórica:**  
   * *Pontos Fortes:* (O que o aluno acertou).  
   * *Lacunas Críticas:* (Conceitos ausentes ou errados, detalhando o porquê com base na teoria financeira).  
3. **Revisão Normativa (ABNT 2023):**  
   * Lista de exemplos errados encontrados no texto vs. a forma correta.  
4. **Recomendações de Melhoria:**  
   * Sugestões de tópicos ou autores específicos para adicionar.

**Tom de Voz:** Construtivo, acadêmico, exigente, mas encorajador.

## **11\. Conclusão e Implicações para a Pesquisa Acadêmica**

A reescrita deste prompt não é um exercício trivial de formatação; é a cristalização de um corpo teórico denso em instruções algorítmicas. Ao integrar as nuances da redundância do fator HML, a distinção entre risco e incerteza na teoria da utilidade, e as especificidades da regra de caixa alta/baixa da ABNT 2023, criamos uma ferramenta poderosa.  
Este relatório demonstra que a qualidade da interação com a IA (NotebookLLM) é diretamente proporcional à qualidade da "engenharia de conhecimento" inserida no prompt. Sem o entendimento profundo de que a PMPT usa MAR e não Risk-Free, ou de que o BL é uma atualização Bayesiana, a IA produziria uma revisão genérica. Com estas instruções, ela simula a expertise de um orientador humano, elevando o padrão do trabalho acadêmico final. O uso de tal prompt garante que o TCC resultante não seja apenas um requisito burocrático cumprido, mas uma peça de pesquisa que respeita a história e o rigor da ciência financeira.

#### **Referências citadas**

1. Nova Norma de Citações de Documentos \- UNIDAVI, acessado em dezembro 5, 2025, [https://www.unidavi.edu.br/fiqueAtento/2024/4/nova-norma-citacoes-documentos](https://www.unidavi.edu.br/fiqueAtento/2024/4/nova-norma-citacoes-documentos)  
2. ABNT NBR 10520 \- Casa de Oswaldo Cruz, acessado em dezembro 5, 2025, [https://coc.fiocruz.br/wp-content/uploads/2024/03/Abnt\_nbr\_10520\_2023.pdf](https://coc.fiocruz.br/wp-content/uploads/2024/03/Abnt_nbr_10520_2023.pdf)  
3. Von Neumann–Morgenstern utility theorem \- Wikipedia, acessado em dezembro 5, 2025, [https://en.wikipedia.org/wiki/Von\_Neumann%E2%80%93Morgenstern\_utility\_theorem](https://en.wikipedia.org/wiki/Von_Neumann%E2%80%93Morgenstern_utility_theorem)  
4. Von Neumann–Morgenstern utility theorem \- Grokipedia, acessado em dezembro 5, 2025, [https://grokipedia.com/page/Von\_Neumann%E2%80%93Morgenstern\_utility\_theorem](https://grokipedia.com/page/Von_Neumann%E2%80%93Morgenstern_utility_theorem)  
5. Von Neumann–Morgenstern utility function | Definition & Facts | Britannica, acessado em dezembro 5, 2025, [https://www.britannica.com/topic/von-Neumann-Morgenstern-utility-function](https://www.britannica.com/topic/von-Neumann-Morgenstern-utility-function)  
6. Portfolio Optimization Methods, Their Application and Evaluation \- Repositório do Iscte, acessado em dezembro 5, 2025, [https://repositorio.iscte-iul.pt/bitstream/10071/18261/1/master\_tomas\_hlavaty.pdf](https://repositorio.iscte-iul.pt/bitstream/10071/18261/1/master_tomas_hlavaty.pdf)  
7. What is the post-modern portfolio theory in investing? \- Quora, acessado em dezembro 5, 2025, [https://www.quora.com/What-is-the-post-modern-portfolio-theory-in-investing](https://www.quora.com/What-is-the-post-modern-portfolio-theory-in-investing)  
8. Five-factor Fama-French asset pricing model: How does the model perform in developed countries?, acessado em dezembro 5, 2025, [http://arno.uvt.nl/show.cgi?fid=153561](http://arno.uvt.nl/show.cgi?fid=153561)  
9. Portfolio Optimisation In Practice: Risk and Return \- DiVA portal, acessado em dezembro 5, 2025, [http://www.diva-portal.org/smash/get/diva2:1971492/FULLTEXT01.pdf](http://www.diva-portal.org/smash/get/diva2:1971492/FULLTEXT01.pdf)  
10. Post-modern portfolio theory \- Wikipedia, acessado em dezembro 5, 2025, [https://en.wikipedia.org/wiki/Post-modern\_portfolio\_theory](https://en.wikipedia.org/wiki/Post-modern_portfolio_theory)  
11. The top 7 portfolio optimization problems | Portfolio Probe | Generate random portfolios. Fund management software by Burns Statistics, acessado em dezembro 5, 2025, [https://www.portfolioprobe.com/2012/01/05/the-top-7-portfolio-optimization-problems/](https://www.portfolioprobe.com/2012/01/05/the-top-7-portfolio-optimization-problems/)  
12. Post-Modern Portfolio Theory \- Wikipedia | PDF \- Scribd, acessado em dezembro 5, 2025, [https://www.scribd.com/document/480225639/Post-modern-portfolio-theory-Wikipedia](https://www.scribd.com/document/480225639/Post-modern-portfolio-theory-Wikipedia)  
13. Post-Modern Portfolio Theory Comes of Age (1993) | Brian M. Rom | 157 Citations, acessado em dezembro 5, 2025, [https://scispace.com/papers/post-modern-portfolio-theory-comes-of-age-4r0fa11p33](https://scispace.com/papers/post-modern-portfolio-theory-comes-of-age-4r0fa11p33)  
14. Post-modern portfolio theory supports diversification in an investment portfolioto measure investmentâ€™s performance \- IDEAS/RePEc, acessado em dezembro 5, 2025, [https://ideas.repec.org/a/spt/fininv/v1y2012i1f1\_1\_3.html](https://ideas.repec.org/a/spt/fininv/v1y2012i1f1_1_3.html)  
15. Behavioural Finance \- the AERC Publications Repository, acessado em dezembro 5, 2025, [https://publication.aercafricalibrary.org/server/api/core/bitstreams/de1eba3a-aa97-4603-a8e2-96fde2f18a1c/content](https://publication.aercafricalibrary.org/server/api/core/bitstreams/de1eba3a-aa97-4603-a8e2-96fde2f18a1c/content)  
16. A global implementation of the fama-french 5-factor model, acessado em dezembro 5, 2025, [https://www.nbim.no/contentassets/710da79eaa8a48859ddfa59c8d353e8b/global-fama-french-model-specification.pdf](https://www.nbim.no/contentassets/710da79eaa8a48859ddfa59c8d353e8b/global-fama-french-model-specification.pdf)  
17. Factor-Based Investing in Market Cycles: Fama–French Five-Factor Model of Market Interest Rate and Market Sentiment \- MDPI, acessado em dezembro 5, 2025, [https://www.mdpi.com/1911-8074/15/10/460](https://www.mdpi.com/1911-8074/15/10/460)  
18. (PDF) The Black-Litterman Model: Extensions and Asset Allocation \- ResearchGate, acessado em dezembro 5, 2025, [https://www.researchgate.net/publication/336664376\_The\_Black-Litterman\_Model\_Extensions\_and\_Asset\_Allocation](https://www.researchgate.net/publication/336664376_The_Black-Litterman_Model_Extensions_and_Asset_Allocation)  
19. Innovative Black-Litterman Global Asset Allocation Model Is Developed at Goldman Sachs, acessado em dezembro 5, 2025, [https://www.goldmansachs.com/our-firm/history/moments/1990-black-litterman-model](https://www.goldmansachs.com/our-firm/history/moments/1990-black-litterman-model)  
20. Reading on Black-Litterman Model \- Medium, acessado em dezembro 5, 2025, [https://medium.com/@li.ying.explore/reading-on-black-litterman-model-beecfcd0a82c](https://medium.com/@li.ying.explore/reading-on-black-litterman-model-beecfcd0a82c)  
21. Black–Litterman model \- Wikipedia, acessado em dezembro 5, 2025, [https://en.wikipedia.org/wiki/Black%E2%80%93Litterman\_model](https://en.wikipedia.org/wiki/Black%E2%80%93Litterman_model)  
22. Prospect theory \- Wikipedia, acessado em dezembro 5, 2025, [https://en.wikipedia.org/wiki/Prospect\_theory](https://en.wikipedia.org/wiki/Prospect_theory)  
23. Role of behavioural finance in portfolio selection and investment decision-making, acessado em dezembro 5, 2025, [https://www.researchgate.net/publication/362862119\_Role\_of\_behavioural\_finance\_in\_portfolio\_selection\_and\_investment\_decision-making](https://www.researchgate.net/publication/362862119_Role_of_behavioural_finance_in_portfolio_selection_and_investment_decision-making)  
24. A note on portfolio choice and behavioral finance: Some food for thought | Cairn.info, acessado em dezembro 5, 2025, [https://shs.cairn.info/revue-bankers-markets-et-investors-2021-1-page-48?lang=en](https://shs.cairn.info/revue-bankers-markets-et-investors-2021-1-page-48?lang=en)  
25. IMPLICATIONS FROM EXPERIMENTAL BEHAVIORAL FINANCE FOR IMPROVING PORTFOLIO SELECTION \- TIAA, acessado em dezembro 5, 2025, [https://www.tiaa.org/content/dam/tiaa/institute/pdf/full-report/2017-02/ti-portfolio1210.pdf](https://www.tiaa.org/content/dam/tiaa/institute/pdf/full-report/2017-02/ti-portfolio1210.pdf)  
26. ABNT NBR 10520:2023: saiba o que mudou com a atualização da norma de citações, acessado em dezembro 5, 2025, [https://unifor.br/web/bibliotecaunifor/abnt-nbr-10520-2023-saiba-o-que-mudou-com-a-atualizacao-da-norma-de-citacoes](https://unifor.br/web/bibliotecaunifor/abnt-nbr-10520-2023-saiba-o-que-mudou-com-a-atualizacao-da-norma-de-citacoes)  
27. Elaborado pela Biblioteca da Escola de Arquitetura da UFMG \- NORMALIZAÇÃO DE TRABALHO ACADÊMICO, acessado em dezembro 5, 2025, [https://sites.arq.ufmg.br/biblioteca/wp-content/uploads/2024/04/Cita%C3%A7%C3%B5es-5abr2024\_.pdf](https://sites.arq.ufmg.br/biblioteca/wp-content/uploads/2024/04/Cita%C3%A7%C3%B5es-5abr2024_.pdf)  
28. Normas para Citações \- NBR 10520/2023 | Programa de Pós-Graduação em Educação, acessado em dezembro 5, 2025, [https://posedu.ufop.br/como-fazer-cita%C3%A7%C3%B5es-abnt-de-acordo-com-nbr-105202023](https://posedu.ufop.br/como-fazer-cita%C3%A7%C3%B5es-abnt-de-acordo-com-nbr-105202023)  
29. Orientações Editoriais — Revista de Informação Legislativa \- Senado Federal, acessado em dezembro 5, 2025, [https://www12.senado.leg.br/ril/como-publicar](https://www12.senado.leg.br/ril/como-publicar)  
30. Guia de Atributos e Elementos da Redação Oficial \- Linguagem Simples, acessado em dezembro 5, 2025, [https://linguagemsimples.unicamp.br/arquivo/uploads/guia-de-atributos-e-elementos-da-redacao-oficial-sem-formatacao-pdf/](https://linguagemsimples.unicamp.br/arquivo/uploads/guia-de-atributos-e-elementos-da-redacao-oficial-sem-formatacao-pdf/)  
31. MANUAL DE NORMAS PARA ELABORAÇÃO DE TRABALHOS ACADÊMICOS \- UNIESP S.A., acessado em dezembro 5, 2025, [https://uniesp.edu.br/sites/\_biblioteca/manuais\_portarias/20170502120113.pdf](https://uniesp.edu.br/sites/_biblioteca/manuais_portarias/20170502120113.pdf)  
32. MANUAL DE REDAÇÃO DA PRESIDÊNCIA DA REPÚBLICA \- Planalto, acessado em dezembro 5, 2025, [https://www4.planalto.gov.br/centrodeestudos/assuntos/manual-de-redacao-da-presidencia-da-republica/manual-de-redacao.pdf](https://www4.planalto.gov.br/centrodeestudos/assuntos/manual-de-redacao-da-presidencia-da-republica/manual-de-redacao.pdf)  
33. Effective Prompts for AI: The Essentials \- MIT Sloan Teaching & Learning Technologies, acessado em dezembro 5, 2025, [https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/](https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/)  
34. I Studied 1500 Academic Papers on Prompt Engineering. Here's Why Everything You Know Is Wrong. \- Aakash Gupta, acessado em dezembro 5, 2025, [https://aakashgupta.medium.com/i-studied-1-500-academic-papers-on-prompt-engineering-heres-why-everything-you-know-is-wrong-391838b33468](https://aakashgupta.medium.com/i-studied-1-500-academic-papers-on-prompt-engineering-heres-why-everything-you-know-is-wrong-391838b33468)  
35. Prompt Engineering for AI Guide | Google Cloud, acessado em dezembro 5, 2025, [https://cloud.google.com/discover/what-is-prompt-engineering](https://cloud.google.com/discover/what-is-prompt-engineering)  
36. Best practices for prompt engineering with the OpenAI API, acessado em dezembro 5, 2025, [https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAAaCAYAAADrCT9ZAAACSklEQVR4Xu2Wz0sVURTHj1QSUWmCSSWlK9sUQZuihe6MapPUKgjSTYgWghFRQWFuzEiRNqWCiygIA6FNgdCmVATBTQtxJYILl/4B9f1y5r6ZOc17M703SOj9wAeGOffdd3+dc0fE49mVNMD7sMYGdiJV8CFchMdNbLs5At/DDfg7kM8c2xrcgt/hNdFxl8U5uBrI5/+BVrgpeuqi7Icjootw2cQywQ7G4AJchxfi4US4sgfsy5zpEZ0wJ25pF935URvIwlX4FPaKdsLO0jgIn8NaG8iJvfAtnIPHTIxwMTjWfhtIox6+g40SdnIj1iIZ7vATeNEGcoKT5GSnRE9glJPwB/wmZdSbbngzeHbHhBPPQjN8I1rd84ZpxfR6LNq/k6fxJ3wBDxVaZ+S0aO7yeBI34UeFFumcgR/hFbjPxCrB5e8EHIr4GU7ClrBpNji4QYkfSbeq/1oIeOS64Cwch3fgJYnvjFvULJTKX477tej1lFTMitIm8XsualLepLEHnhcdDBdtWbTqcze4M7fCpqmUyl/iTuKwDRTjsGjuMQejcCfm4SfJviOcaAf8Cu+J9sl3lVDs/nV0ik54wAaKcRfeti8lnDAr4FETS8KlRZ8k70S5lLp/6+AX+AueNbG/4FXCPOVu8BqycOdnRCedpfJehw+kgs+7BLhwPMpJn7in4LRo/rJal4TFiavi8nRJ4pXumWhHLs7nV7A60iYKB/YSNpn35cKd+yDhGPi97OoAXQnkf54IfrOt8A7kHZ7nUfZ4PB6Px7MD+AOGmnDalr1lWgAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAAaCAYAAADrCT9ZAAACW0lEQVR4Xu2Xz0tUURTHv5FBkf2gkCCzpoiCVoUk2cYQQaGFFa1a1KJNhNiigqSVSIuyCGlRtFACaWFBIESbQlpERVRQ0CIKWhQt2gj9Afr9dt5zZo4zc9/omLO4H/gg3PPmvvvePefcJxCJROqY47TLD1aijb6lf+lM4lf6nk7T3/QB3Z3+oI7YCVvnBR/IwhD9Tg+48V30FZ2iW11sOWmgN2EbNOJiQRrpI/qCbnYxoQk1cbcPONbQlX5wiThCn9Of9D7sBWQmRz/Q23RFcWjuZfygB4tD8zhLD/nBJUBrugt76Dew9WksMz2wGj7tA+QYrI6vIfwWO+lFzH9pteYMPU+3wB74Kd1YdEWAAdgOqttpEtlCL9GP9ASypeoqep12+EAN2Ubv0E3IZ58eWmvORPqjT7CUvpF4C1bTV+i6uavDrIfVvHZai6olypyrsIwU6dpVjrlkLEgO5et3O6xDP6NNLlYJzXOYPqZP6GVYw1PWpBmkl+HvF6KVDsMySajE1LC+0f3pRSEq1a/Qbile1eGeoPTrh5WFznad95OwDNJObchfGmQ1HUP+W6HQP6iijMqdv0I3GUeVE5K9dAKWNfqw0TyLRc2zVEPsQ7Yj8x+h87cd1sweInvbP0pHabMPLAJ98NxD6bJKH/icD5RiD/0M63qFb04dWSn8BXa4q/aysANWU7VsVmthDVQnRil6YQ+sBy+Ldk6tXN/Kuljn7DtYjenvL/oa9iFRTTqqD5z0gwtE99VGpGtUHxksiO+jL5PxNK71q4T+G6dQn/9kRCKRSCQSWSZmAUo0cHB/zKA8AAAAAElFTkSuQmCC>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAAaCAYAAADrCT9ZAAACNElEQVR4Xu2Wz4tOURjHv2KkmBHFxExkgxqJ3ViNFcpsZmJFFlbyIxs1TZNSKBlCQhFlIQuZmprNWCn5Fc1kYyErKQvL+QPG99tzz9xzn95739sUV5xPfep9z3M6neec55xzgUTiv6SbnqWrfeBfZAkdoR/oRhf706yhT+gPOp+p35rbNzpHX9JB2LwXxS76NVO//wYG6E9Y1cWsoDdhi3DAxWqhAW7T9/Q77S+GG+M0LGEl7tkP2/lbPlCHg/Q8PQMbRIM1zTJ6n76lG1xMaDE013M+0I519AHtRT7IoUKPZlCSSvYxrAJjNtHX9AUWcd+cpIez36FMlHjT6FjpeI3BXo+gqvENvUQ7F3rXZDvs7K7K/oeERxd6VKMJ3INdHh/pMF1a6JGjBHb6xgrC+X1Ir0ZO0Ed0W961Hh30Mt0TtYVVrXMRqMzu0qOwZ6QPNrkrWcwzRLf6xhKqzq/mfQP2PLW6zErZi+I7F9vq3Hi0OEdcm3b3FOwN7Ynat8BKsN2YgarzK0IlXvOBMrroHdhEYlSi7+gz5GVehnZsh2+EfQjso7Ow0lPJv6K7405tKHt/A8dhCV/0gTJO0GO+EXnCugHXu5hHt3ur1Q+shFWRdmNtMdSWqvdXY03Rz6hxJ2j1VYrTsGfIo52fhCWt5JtAi6hSbvWJu5k+h51f3daV6HLSqoRzOoPiTXcBNlCI6/d1ujzq8zvRzj1FPgd9L3+Cff3JL5njKN4PiUQikUgkEs3yC7VOblm5gQpaAAAAAElFTkSuQmCC>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGcAAAAaCAYAAACq/ULmAAADo0lEQVR4Xu2Y2etNURTHlwzJzzxPGVKGfpHhhSRSIkMZo5TCi2RISKbMZQzJgzGSKFEKRYkHY79SUh7kQVIePPoD+H5/62733OXcs/e999wfsj/1rdNZ956z915rr7X2EYlEIpH/kj7QRqiLNUSC6A5Ng2ZDg6BWifs9C9dVwQdtg5qg/sbW0nSDrkNfoR8F8Zpj+wx9h55Cc6W4AH8Kvn8K9AR6C52A1kAXoDNQI3QbGu7+UA1joY8F8fpvYCr0TXQ3J2kPnRJ12Cxja0kaoJPQB2gR1LrULEtEx3gH6mRswXCy9PJr6As0sdScCiOmg72ZM+tEnUMnWWaK7qjT1mBoB7W1N3OgM3QNeg+NNzZHD+gxdMAaKmEOtBtaLzphTtxHR2gf1NUacqINdB56CfUzNkLHcaxbrMHAuSy2N2uEgblfNHDmG1sSrtEt0fWtil6i+XGgFCccMhkOcBc0yRpygg6hY66K7uwkLLbPoUfir4+joMOS7+7hnD+JLjwdUA7azkkN9WataG4kLlXQSSEMhc6Kdnl5w9TKFLtT9PlOjMIX0EEJy+MMok3QssJ1rXBHc84hQcz3MbPYWhTESNFa47zvnLP91y/8jIZuiraPeUanqzeXoKMJsbhehkYUf+qF49ohuoOYIWrB7eh3UsOO8MEBH5LStOSi1VdkLUw7q0WL30VoJTRZSiM+a/tbsuoNx80OiS11WqOQBR1Kxz6A9kLzoGFSHCNTvC/KXVd7X+pXb5sPS8lzRFJped4HJzVBdOHoYPb87P64GIz45cWfesmqN8Tt8OPWEAAPhCtEz0l0MMf4UPR8wiLPepaFc46v3jClbRZN/RXBNpB50/6R0fNK/C9OQqcsFJ3gBtFn+qLPR7nzjWOVqHMqaVEHiM75CjRdwudnGQK9Ef8acR2OSHpwZcITLKPH4pzDTqi3saXhUiMLbsWDyCDrfMPIvyd6vhhjbOUYJ7qYjdZQBZwn6yDfz04wDa7LHil//kmFW411hVGeVhi5o+6KOiikA1sAbZV8uiAHJ8901iS/t8mDRT+FMB2Fnh04J9YvmyVqgYtO57CZajA2dpBM46Hja4aFnw90dYVbM9nx7BWdtLPzmnmYJ+w0uIjHRLd5HnBH3JDiGPj9zNUtip9IKL6TKSoU7j7fQbUauBufiY6RtWqp6CclzqGSTrIuMEJ4RsozndWDGVK/gzJrK9tpdn1sUvpKvlkkEolEIpFIJBKJRP5JfgJq7aY7MrpLMQAAAABJRU5ErkJggg==>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAbCAYAAABFuB6DAAAA6ElEQVR4XmNgGAXUBLxA7ALEMlA+NxA7ALEBEDNDxRg4gLgNiPOA+CwQVwPxLCAOgdJdQMwKUmgPxAVArAbEl4G4B6oZBAyB+BpUDUMEEBsBsQcQP4cJQoEFED8B4gwkMYZKID4OxJJIYnFA/B+IvZHEiFPIBcQrGCCOZ4GKgWgQH+RukPvBQAGIzwFxDkwACOSB+DQQdzAgNIM98hmIS6B8RiAuB+I9QCwLUwQCIPeBgmETEM8E4jUMEGvFkRXxAPFqIF7IAAk/IagYBlBgwHQfVhDLAHFfGBDzo8mhAFBcwnAgmtzwBACPyiVxtmWwyAAAAABJRU5ErkJggg==>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAC4AAAAaCAYAAADIUm6MAAABYklEQVR4Xu3VvytFYRzH8a9Q8jtCFLEYlDKJDAwGMSmbUmQwGAw2o80gkoHNRsqgDBhkosTAZrL5M3h/e87pPufHvd1TOM/N86lXnfs9z6nvPef5IeLj8//Sh/l40dUMYhln+MR+9La70cZnMYonqaDGw3ThUXzjmVKNMYwE10qvp9BQGJaePBtfxCausIdjrGIDN+gtDE0mr8bbsYtOnOAeA8G9JlxgO/idmqyN14l5phxtqDKPJTKEFXTjQaJNtor5Cqeot+qRZG18Gjtl2kKLeaxodI5/YMaq6Y73hgMp/sczN/7TWcML+q3aAr6wZNUSybPxGjEL8hyNVu0Qd+gJaqkJGy/5WX4p4fy+RHNQG8cr5sJB8UyKOTH1uNfPot5xK2bh/EXC+a07iL71I1xjwhrjZNbFLEJdjDpVSu1CziRtfjufWjFH+7OY6dEh5rh3PsMS3e/12K+Yt+7j4xPLNz3CQZfr3h6HAAAAAElFTkSuQmCC>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGUAAAAaCAYAAACuCJLbAAAEm0lEQVR4Xu2Z66tmUxzHf3JJ7ncZJke5TVIukUJOSobhhfDKRC5TU6OkSBiaCDGkcSkkxi23SCJFTHJPxgs1L8QbKS+mpPwBfD+z1upZz+9Z69l7PefMRGd/6tuZs9Zz9l7P7773mA0MDOwadpcOlfaMv+8nHTjanoDPHyTt5jcWiQNsdJYlyznS79LF0h7Sc9LbFpzjwVh3Sqv8xiJyhvSkBef8r7lb+k36J+ov6WPp+Lh/tvRztv+HdH3cWyt9Lx0rHSF9Jd0W9zx8doONsuQk6UsbXRd9Ih0tnSZ9l63/Lb0jHbLjL83uiGtp74G4DldLD9t/I2NOkNZLj0hXSnuPb08nGXRL/LcHQz4h3WihBEHKjMfjPlnzowWDek6WPrTgPM8m6U9p3q1zTaL+V+l0twcXSc9LB7t1vviLtnMzsg+XSZ9Jp1qoHATS69aQxakMYYRSvd9fekaay9ZwHk68MP5OJrxqk9HA9YhkVLo2JY2IpwTmJKdwLs6XQxZwPZxd4grpPWswQE/2sX4ZeIz0hXRVtkYvJTBvyNamcq0Fw/CzxInSszbeKzDUmxa+OFmD0zCG5yjpc+kCvxG52cK9fWSfKf0S97zD5i0EQcnJMGehNHpnzgpliO//lHSY2yuBMzh7XjVSkNV67hjpw/4iOSstpF8ODkxeZwLj0KXShzMojcv8RiQFBM5JkG30BUqjdwpf6EHp8GzNQ0S/Id3iNxrALgTGWxaykujvy/1WtielequNV5wiGPTTKP5d4j4Ljskhe1I931c6JdvLwdjTogODe6dcKt0U1/weUZiXhRoYoFaOp0HPPF96V7rHRsNFC9y75pTS+gQ0UZppatgejPm09fBuBQ7CQECJK5Gc8mj8HSM8FH96h5FtZFDNwTldweDBGZdI70u3Wuijs8D9uG/J+L2d0tVP5iw4pe+X83AQVIMDctD0mWssZArkDiNgMNZ83OsCp9BYabDToHHTCz+S1ljI+oWQSmfJ+L2ckvpJbeyEUj9poa9TyCZKIpmQJjj60XYLf8+kdZfVM86DU+hlpT6Xc570jXSdTU6Os1Izfm19jJRqtcPjtA3SuW69hS6nzFlofjwc0rtoronkMCY7HnJrI3CJlvKVZ8s6m710JRjzS8bHDjxs14aeHaRUo6mVDoKBNlq/2bwGB+Qe3KvEkdK3Ft4q0FjzvpacwsPl7W6vi677lkh9hbI3a5MHqgtvPvLHALLwpajOjCRtf5JWuHXK2WZpuVtvhV41bbJLbxN+kI5ze8lhPIi1jKSpLDOazoIfhzlHCzjzAxt/5cR3I0vIyE7IgnulbRYaKY32NQvPHa2HKUG0Y1T6RYlUQvOxN8H9qfe8z2qB5o5R/BjfCs5h1H9FeszKr4lqENRfWyiHl1vIPkpwU9UhEpl6mHhK/WVWeOJnzKw9W9C4z7Ly1MMeEduZ7g6ut8XajNgF11pvk9k8Db7TvAW7tmT6LoFIf9najTsLRDfTImrpQUsOStRm6/+MsRCIZBr8QnvhkgAjvRB/7iyo17yZWOU3BurQ7Blt9/Ibi8RqG/1XwsDAwMDAwJLmX7U21CEIi+5VAAAAAElFTkSuQmCC>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAAaCAYAAAAEy1RnAAACRUlEQVR4Xu2WT0sVURjG38ggUlMKEYUQhBIVwhREBOWSiKKbBBduVJACKTHaBC10oYgLFRVcqBAICaJCqVQLv4BtxIW4c+HCDyD4Aex5eM/gmXF07tw7/rkyP/hxnXPO9c5z3nPOjEhMTEzM3eY1THgb7yM18BP8A0/ggLs7s3gEn3gbfWDoFtgMDyVDQ+fCL3AL1nr6rqJK0gj9VHRf1IvO9k1RCMfgmmjYh+7uQFIKzYAf4U/YCUfhiugkXCclcAr+gJXwgbs7aUKH5g/xMFiX85Cc+X+wzxkUMS/hgpF/p0vo0PzCAXxrtTmhZ622RqMXHiTcDkFwcllNVpXVZZWjInTob3AHFlltdfAYTprrLNFxCWdAQLsfBaJ7dkZ0UqMkVOgc0WW9KBrAoQeewg6rLQrsanMVRbG0SajQr+C+uAc/hsvwN3wmWpVx+FXcJ3opnICfPe3JwsCc7HQPMRIqdKtoRe3B7+AerBa9kS7Rm9qAL8yYYvjefP6FFaY9FezHFV82UgnvhGYBAuGjaVd0xnmSLsFNWGb6ueRZUU7OvLkmvNHn8A1chfmmPR24qoZEH5sNktyzulf0/vkKembkocz/wTPkAvZ+5vLkj+a5RigMOif++5t7f1pSq85lZMMPsN3bEQV++9kPjuNrYTnslvOA/GRgvsxkDFyyR6KPp6vggcMlzIOME+DA5f1LdD9lDKzwtuiyDoInOrVhWL6qRrGfbwwuz2QOCxsG/w4H4Qjsd3ffTzhRbXAYNpnrmJiY2+c/1RpZP4tAQYsAAAAASUVORK5CYII=>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAaCAYAAABozQZiAAAAbElEQVR4XmNgGJkgB4j/k4hXAzEPSDMM5EMl3JEFocAAiO8A8Tog5kWTAwOYC/BpxrARBkY1o4LhrhlEowOCmmHJkyTN8UB8EYg/M0A0fwDis0BsD8RaQLwHiJ9D5UD4FhBPA2IukOZRMPwBAEEOQUtDYdR0AAAAAElFTkSuQmCC>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAbCAYAAAB1NA+iAAABCElEQVR4XmNgGAXowAWIPwPxfyJwBlQPVjARiJ8AsQWaOCMQ6wPxCSD2RpODAwEg3grEx4FYEk0OBnqA2B5dEAZ0gPgmEM8CYhaoGIjWBWJWKL8Jqg4rCGGA+DEHSQzkEpCtXFA+yPn8CGlUAFL4FIi9gFgciGWBuAuIK5EV4QIw/z8H4tNAfBKIL0L5OP2MDAyA+A4Dqv95gXgGECtA+cxQMawA5n/kOBYD4hYg5oDyA4E4ESGNCigyAJRI+hmwJyAY4AHiyUAsjy4BArAAPMoAsRUbCGWAuAZkGQbAFoAwwA3EuUB8CYhN0eTA0XMWiD8wQPyPHIUg/AgqDsJLGBBhMQpGAfUAAEv+N+RjTXuOAAAAAElFTkSuQmCC>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAbCAYAAACqenW9AAAAgElEQVR4XmNgGAX0BqxALAbE4lgwD5I6BlMgvgTE/3HghUDMAVKoCMSrgdiJAWKKFxC3QNkwDFYIAoFQDTBQCcRxSHycQACI1wCxBboENkCSYgMg3g3EUugS2EAOEK8DYl50CXQA8vESIJ6ILoENqDBAwpqokGAGYiEoPQoGEAAAlHASiyeC5aEAAAAASUVORK5CYII=>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADEAAAAaCAYAAAAe97TpAAABoklEQVR4Xu2UTSuEURTHj0TyngWhRCkLFiyUkg2iWHhnoawlWdkoC8nKio0spMRCec0CZcEHYEN2fAIb34D/cZ7puXM88zz3Lmim7q9+NXPumZn7n/vcQ+TxeHKNfDgCG/RCtlMEB+E6fIRvsD2tIwfgEP2wGy7TP4eoCIwjDxbqYgyL5BCiAFbDmghLjb4o6uAl/Aq8hz0kG9Zw75QuxmAdohM+U7gJ7QHJEUfB9S2S4+dLyBtvhVdwD9aHrT9rC3DUqCVhFaIJnsBekn99CG4Er1NmCsA0whldJAk0Dl9Ivn8T3sJdWG70JWEVYowkSIoVOGe8T4I3VKuLBiUkk2aJZCMczgWrECaV8BR26YUE+DHpg0fwGE5Q5tOrIpk6tjiH4MY7ksvnwjy8hrNwEh7CB4q+3Pwb3GeLcwj+wDks0wsx8ERbJZluJi3wBu7DNpK7NQwvKP3xTcIpBB8/Pw7beiEB3uCALgbwd06TnMoHPCMJ5wKHeIcdeiGKZpIx63Kp/4piuANfKRzzn/AJroVtv+GpwZfOdXp4PB6Px5PVfAP1pENmtGzizwAAAABJRU5ErkJggg==>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAaCAYAAAA9rOU8AAABo0lEQVR4Xu2WPy8EQRjGH6EQIRGCUKAQCVFQEIkIUSokEiWFSqNQiErlXxQSEQXxDXwAUVyhEkStIEqJwofgeTJ3t7PjZs2eW6e4X/Ir9t3Z2Xd3nps9oEa2NNE6t1gNOukObXRPVIJeuugWE9DYVet4mt7Sh0BnzGURgzATXtJ3ehI/7aWB7sFcL7RU+/QM5qEKS3dEP+hc/rieTtE7OpavFdFk83SCPiK8GV13CNOU0JKd047iCKCVXsHcuNuqN9NT2mPVYnTRe4Q3o7dpL6le+Zp1LEboM71A1LRQk7u0xarFSNOMAqvX32fVFuiAdSyW6Cddd+ptdAUJv8I0zYzTbSRMlkcNv9FJ98RPpGlmA1EgffjyEkRoM7qJxrS7JxxG6Su+5yWI0GYU1E23WAJfXoIIaUYZUVaUmSQ07hhl5kWENKO11020TyTxq7yIQjPajHy/Enf791F2XpQB7bz6FGiN5QvN0WFrnCY9oENWzUZ7zDV9QjRPYa4bmAYrRj/MtyjVk2bFMtJ90TOj1PZfNZSTLfiD/afMwvwHqVHj3/AFO0JMrn/fY7QAAAAASUVORK5CYII=>