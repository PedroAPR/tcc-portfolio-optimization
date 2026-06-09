# Relatório Crítico e Recomendações Estratégicas sobre o TCC "Moderna Teoria das Carteiras no Mercado de Ações Brasileiro"

PARA: Pedro Augusto Pinheiro Reis
DE: Pesquisador Sênior (Ph.D.) em Finanças Quantitativas
DATA: 25 de novembro de 2025

## Preâmbulo: A Contradição Central entre a Crítica Teórica e a Execução Metodológica

Recebi sua solicitação para uma análise crítica e "contundente" do seu trabalho de conclusão de curso (TCC), "Moderna Teoria das Carteiras no Mercado de Ações Brasileiro". O objetivo não é uma revisão superficial, mas um *peer review* acadêmico rigoroso que identifique as falhas centrais e, o mais importante, forneça um "caminho a melhorar" claro e acionável.
Compreendo que o usuário é o autor do trabalho (Pedro Augusto Pinheiro Reis), um estudante de Ciências Contábeis na Universidade Federal de Goiás. O documento principal é um rascunho de TCC 1, que parece estar em fase de desenvolvimento, como evidenciado por seções incompletas e marcadores de posição ("placeholders").
A solicitação para ser "contundente" e a recente atualização bibliográfica 1 são cruciais. Isso indica que você, o autor, está ciente das limitações do seu modelo atual e busca uma orientação robusta para elevar o nível do trabalho, potencialmente incorporando críticas mais profundas à Teoria Moderna do Portfólio (MPT) e explorando a Teoria Pós-Moderna (PMPT).
**Temas Centrais e Análise Preliminar do Material**
A análise do material de pesquisa 1 revela uma tensão fundamental que será o cerne deste relatório crítico:
**A Contradição Central:** Seu Referencial Teórico (Cap. 2) e sua Análise Descritiva (Cap. 4) constroem um argumento devastador *contra* a aplicação da Média-Variância (M-V) de Markowitz. Você corretamente aponta a falha da premissa de normalidade, a inadequação da variância (que penaliza ganhos) e o "erro de estimação" (*estimation error*) como problemas críticos. Sua análise de dados (Cap. 4.1) confirma isso empiricamente, encontrando assimetria e curtose (leptocurtose) extremas (ex: ASAI3 com curtose de 2469,69), o que torna a M-V uma ferramenta inadequada.
**A Desconexão Metodológica:** Apesar de provar que a M-V é a ferramenta errada, sua Metodologia (Cap. 3) a utiliza como *único* método de otimização. O seu desenho experimental (Cap 3.4) propõe-se a comparar três carteiras (Média Histórica, ARIMA, LSTM) otimizadas pelo *mesmo* e *falho* critério de Markowitz (Máximo Índice de Sharpe, que depende da M-V).
**O "Caminho" Inexplorado (PMPT):** Você introduz a Pós-Moderna Teoria do Portfólio (PMPT), CVaR e Sortino na Introdução e no Cap. 2, e sua nova referência 1 é inteiramente sobre a superioridade do CVaR. No entanto, sua metodologia *ignora* completamente essas métricas de *downside risk*. O trabalho critica A, elogia B, mas testa apenas A.
**Status de Rascunho:** O documento está repleto de problemas estruturais: capítulos vazios (Cap. 5, Conclusão), seções com marcadores de posição ("placeholders"), duplicação no Sumário (Seções 2.6 e 2.7 são idênticas), e uma metodologia (Cap 3.4) que faz perguntas ao invés de afirmar o desenho ("Como p,d,q serão escolhidos? Auto-ARIMA?", "Definir a arquitetura?"). O Cronograma (Cap. 6) está incompleto e as Referências (Cap. 7) estão ausentes.
**Plano e Estrutura do Relatório Crítico**
Meu relatório fornecerá a análise "contundente" solicitada, estruturada não como um TCC, mas como um relatório de *peer review* sênior, focado em dissecar as falhas e construir uma solução.
Persona do Usuário Sugerida: Aluno de graduação (Ciências Contábeis).
Estilo e Tom: Tom formal, acadêmico e analítico. Conforme solicitado ("críticas contundentes"), o tom será direto, rigoroso e incisivo, mas com o objetivo pedagógico de "mostrar o caminho", típico de um orientador de PhD ou revisor de periódico.
Extensão do Relatório Sugerida: 12.000 palavras.
**ESTRUTURA DETALHADA DO RELATÓRIO CRÍTICO**
**Assunto:** Relatório Crítico e Recomendações Estratégicas para o TCC "Moderna Teoria das Carteiras no Mercado de Ações Brasileiro"
PARA: Pedro Augusto Pinheiro Reis
DE: Ph.D., Pesquisador Sênior em Finanças Quantitativas
DATA: 25 de Novembro de 2025
**Preâmbulo: A Contradição Central entre a Crítica Teórica e a Execução Metodológica**
**Ponto Central:** O seu trabalho, na forma atual, está em guerra consigo mesmo. Ele sofre de uma dissonância cognitiva fundamental: a metodologia (Capítulo 3) ignora ativamente as conclusões devastadoras do seu próprio referencial teórico (Capítulo 2) e dos seus resultados preliminares (Capítulo 4.1).
**A "Acusação" (Cap. 2 e 4.1):** Você constrói um argumento robusto de que a Teoria Moderna do Portfólio (MPT) de Markowitz é inadequada para o mercado brasileiro. Você (corretamente) ataca seus pilares:
A premissa de **Normalidade**.1
A métrica de **Variância**.1
A estabilidade dos **Inputs**.1
**A "Confissão" (Cap. 3):** Após provar que o modelo M-V é a ferramenta errada, sua metodologia 1 declara que usará *exclusivamente* o "portfólio de Markowitz... a Carteira de Máximo Índice de Sharpe". O Índice de Sharpe é, por definição, a epítome do modelo M-V que você acabou de invalidar.
A Oportunidade 1: Sua nova referência 1 sobre otimização Média-CVaR é o seu "mapa de saída". Ela demonstra empiricamente a superioridade dos modelos de *downside risk* (PMPT) em contextos de *tail risk* — exatamente o que seus dados em 4.1 1 (curtose extrema) diagnosticam.
**Insight de Segunda Ordem (A Causa Raiz):** A sua questão de pesquisa 1 está errada. Você pergunta: "qual *input* (Média, ARIMA, LSTM) é melhor para o *mesmo otimizador* (M-V)?". A pergunta que seu Cap. 2 implora para ser feita é: "É mais importante melhorar o *input* (LSTM) ou melhorar o *otimizador* (CVaR)?"
**Conclusão do Preâmbulo:** Este relatório irá dissecar essa contradição. A crítica será "contundente", como solicitado, não para depreciar o esforço, mas para forçar o alinhamento e elevar o trabalho do nível de "exercício de graduação" para "pesquisa publicável".
**Parte 1: Análise da Estrutura, Coerência e Nível de Prontidão do Documento**
Esta seção audita as falhas formais do manuscrito.1 Um trabalho não pode ser academicamente sólido se sua estrutura for amadora.
**1.1. Incompletude e Marcadores de Posição (Placeholders)**
**Observação:** O documento está em estado de rascunho bruto. Seções inteiras (Cap. 5, 8, 9, 10, 11, 12) são compostas por texto de preenchimento (ex: "Sfgsdgsd", "Gdfsgsdg").1 A Conclusão (Cap. 13) está vazia. Os Resultados do Backtest (Cap. 6) estão vazios.
**Crítica:** Isso é esperado de um rascunho, mas indica que o trabalho está, no máximo, 40% concluído. O cronograma 1 que termina em Julho está perigosamente desalinhado com o estado atual do documento em Novembro.
**1.2. Caos Estrutural no Sumário (Capítulo 2)**
**Observação:** O sumário do Capítulo 2 1 apresenta duplicatas exatas, o que é um erro editorial grave:
"2.6. Métricas e Modelos de Equilíbrio Derivados da MPT" (p. 14)
"2.7. Métricas e Modelos de Equilíbrio Derivados da MPT" (p. 15)
"2.6.1. O Índice de Sharpe (IS)..." (p. 14)
"2.7.1. O Índice de Sharpe (IS)..." (p. 15)
**Crítica (Insight Causal):** Esta não é apenas uma falha de digitação. Ela reflete uma desorganização no fluxo lógico do seu argumento. Você (corretamente) agrupa MPT, CML, SML, CAPM e Beta.1 No entanto, a repetição sugere que você escreveu seções isoladas sem integrá-las, resultando em redundância e confusão para o leitor. Isso deve ser consolidado em uma única narrativa coesa..1
**1.3. A Metodologia como "Lista de Desejos" (Capítulo 3)**
**Observação:** A Seção 3.4 1 não é uma metodologia; é um conjunto de perguntas para seu orientador.
"Carteira 2 (ARIMA):... (Como p,d,q serão escolhidos? Auto-ARIMA?)"
"Carteira 3 (LSTM):... (Definir a arquitetura: quantas camadas? neurônios? lookback period?)"
**Crítica:** Uma metodologia, por definição, torna a pesquisa *replicável*. Essas perguntas tornam seu estudo *irreplicável*. Você, o pesquisador, deve *definir* esses hiperparâmetros. A ausência dessas definições invalida todo o Capítulo 3.
**1.4. Integridade do Referencial (Capítulo 7)**
**Observação:** O Capítulo 7 (Referências) está ausente.1 As citações no texto (ex: "Damoradan, 2007", "Rockafellar e Uryasev 2000, 2002") estão presentes, mas a lista bibliográfica que lhes dá suporte não está..1
**Crítica:** Esta é η falha acadêmica mais básica. Um referencial teórico sem referências é plágio ou ficção. A correção é urgente.
**Parte 2: Auditoria Crítica do Referencial Teórico (Capítulo 2)**
O conteúdo do seu Capítulo 2 1 é, paradoxalmente, o ponto mais forte do seu TCC e a principal evidência contra sua metodologia.
**2.1. O Problema da Estimação de Parâmetros (Inputs)**
**Análise:** Sua discussão 1 é excelente. Você identifica corretamente que o otimizador M-V é um "maximizador de erro" (*error maximizer*). Você nota que ele "tende a alocar pesos significativos nos ativos que... apresentaram as características mais atraentes" no passado, que são "justamente onde o erro da estimação é maior".
**Insight (Implicação):** Você diagnosticou a doença. O M-V é "extremamente instável em relação aos retornos esperados". Sua proposta de usar ARIMA e LSTM 1 é uma tentativa de *tratar* essa doença, fornecendo um vetor de retorno esperado (μ) melhor do que a "inadequação da média histórica". Esta é uma linha de pesquisa válida.
**2.2. A Falha da Premissa de Normalidade e a Inadequação da Variância**
**Análise:** Esta é a sua segunda (e mais importante) crítica. Você escreve 1: "A variância... trata os desvios positivos (ganhos) e negativos (perdas) em relação à média com pesos iguais." Você (corretamente) contrasta isso com a "aversão à perda" e o *downside risk*.1
**Insight (Implicação):** Esta crítica *não* é resolvida pela sua metodologia. Usar um LSTM para prever retornos (μ) não muda o fato de que o otimizador (M-V) ainda usará a *variância* (σ²) como medida de risco. O otimizador ainda irá "penalizar" portfólios com alta volatilidade *positiva* (ganhos) e tratará ganhos e perdas simetricamente, o que você já argumentou ser conceitualmente errado.
**2.3. A Introdução da PMPT (Pós-Moderna Teoria do Portfólio)**
**Análise:** Você introduz a PMPT, o Índice de Sortino e, crucialmente, o *Conditional Value at Risk (CVaR)* 1 como as *soluções* para as falhas da MPT. Você os posiciona como métricas superiores que focam no *downside risk*.
**Insight (A Contradição):** Você apresenta a PMPT/CVaR como a "cavalaria" teórica que resolve os problemas da MPT. E então, na sua metodologia, você deixa η cavalaria no forte. Ela nunca entra na batalha. A sua nova referência 1 é *inteiramente* sobre essa batalha e conclui que o CVaR vence.1
**2.4. Síntese da Crítica ao Cap. 2**
Seu Capítulo 2 identifica dois problemas distintos na MPT:
**Problema de Input:** O vetor de retorno (μ) é mal estimado ("maximizador de erros").
**Problema de Modelo:** O otimizador (M-V) é conceitualmente falho (usa variância, assume normalidade).
Sua metodologia (Cap. 3) propõe uma solução *apenas* para o Problema 1 (usando ARIMA/LSTM). Ela *ignora completamente* o Problema 2, que você (e seus dados em 4.1) argumenta ser o mais grave.
**Parte 3: Dissecação da Metodologia (Cap. 3) e dos Resultados Preliminares (Cap. 4)**
Esta seção demonstra como sua metodologia (Cap. 3) falha em responder aos desafios levantados pelo seu referencial (Cap. 2) e é diretamente invalidada por seus próprios dados (Cap. 4.1).
**3.1. A Insuficiência da Questão de Pesquisa**
**Sua Pergunta:** "Qual é o impacto no desempenho... de carteiras Média-Variância... quando o input de retorno esperado é estimado por modelos preditivos (ARIMA e LSTM) em comparação com a tradicional média histórica...?".1
**Crítica:** Esta pergunta é *trivial* no contexto da sua revisão de literatura. Ela presume que a Média-Variância é o campo de batalha correto. Você *já sabe* que os retornos não são normais (Cap 4.1) e que a M-V é um "maximizador de erros" (Cap 2.9).
**Insight (A Pergunta Correta):** Uma pergunta de nível superior, derivada do seu próprio trabalho, seria: "A melhoria do desempenho do portfólio vem da substituição de *inputs* (Média Histórica -> LSTM) ou da substituição do *modelo* (M-V -> M-CVaR)?" Seu TCC, como está, não pode responder a isso.
**3.2. Usando seus Próprios Dados (Cap 4.1) Contra sua Metodologia (Cap 3.5)**
Seu Dado 1: Você observa "valores de curtose dramaticamente elevados", citando Assaí (ASAI3) com uma curtose de **2469,69** e Pão de Açúcar (PCAR3) com **408,26**. Você (corretamente) identifica isso como *leptocurtose* ("caudas pesadas").
Sua Metodologia 1: Você propõe otimizar para o "Máximo Índice de Sharpe".
**A Contradição (Insight Causal):** O Índice de Sharpe = (Rp - Rf) / **σp**. O denominador é o *desvio padrão* (a raiz da variância). A variância/desvio padrão só é uma medida de risco completa e suficiente se a distribuição for normal (ou, no máximo, elíptica). Seus dados (curtose de 2469,69) não são normais; eles são um *pesadelo* de "caudas pesadas".
**Raciocínio (Chain-of-Thought):**
Curtose > 3 (leptocurtose) significa que eventos extremos ("tail risk") são *muito* mais prováveis do que o modelo normal (M-V) prevê.1
A M-V, ao minimizar a variância, otimiza para o *segundo momento* da distribuição.
Em distribuições com caudas pesadas, os *momentos superiores* (como a curtose, o quarto momento) *dominam* o risco. Otimizar apenas para o segundo momento (variância) é inútil; é como tentar parar um tsunami com um guarda-chuva.
Portanto, usar o Índice de Sharpe (que usa σp) em dados com curtose de 2469,69 é um erro metodológico fundamental. O otimizador M-V irá *ignorar* o risco de cauda, que é o *único* risco que importa nesses ativos.
**3.3. O "Ato Falho" Metodológico (Cap 4.1)**
**Observação:** No final da Seção 4.1 1, você escreve a "arma fumegante" deste relatório:"A constatação empírica [de leptocurtose]... fornece a justificativa central para este trabalho... A falha da premissa de normalidade valida: **O uso de métricas de risco da Pós-Moderna Teoria de Carteiras (PMPT), como o Índice de Sortino**... e a exploração de modelos preditivos (ARIMA e, especialmente, LSTM)..."
**Crítica:** Você escreveu isso, e está 100% correto. Seus dados validam o *Sortino* (PMPT). Mas veja sua própria Metodologia 1: você lista "Retorno/Risco (PMPT): Índice de Sortino". Isso é bom. Mas você *ignora* o passo mais importante: a *otimização*.
**Insight (O Salto Lógico Perdido):** Você não pode apenas *avaliar* com o Sortino (PMPT) se você *otimizou* com o Sharpe (MPT). Isso é misturar paradigmas. Se seus dados validam a PMPT, você deve *OTIMIZAR* usando métricas da PMPT (ex: minimizar a Semivariância para maximizar o Sortino, ou minimizar o CVaR). Você usou seu diagnóstico de PMPT apenas para *validar* seu tratamento de MPT, o que é logicamente incoerente.
3.4. O Papel da Sua Nova Referência 1
Análise de 1: Este artigo (Lovatto, Henrique, & Lima, 2017) faz *exatamente* o que seu TCC deveria fazer. Ele compara "risco-variância" (MPT) com "risco downside" (PMPT/CVaR).1
Conclusão de 1: "o CVaR minimizou perdas mais acentuadas... A métrica de risco variância... **subestimou a probabilidade de eventos oriundos de tail risk**...".1
**Síntese:** Seus dados 1 mostram *tail risk* (leptocurtose). Sua nova referência 1 *prova* que o CVaR é superior para *tail risk*. O caminho a melhorar é autoevidente. Você deve incorporar a metodologia de 1 no seu TCC.
**Parte 4: O Caminho a Melhorar (Recomendações Estratégicas)**
Como solicitado, aqui está o "caminho a melhorar". Você tem duas opções. O Caminho A é o "suficiente" (e medíocre). O Caminho B é o "excelente" (e publicável).
**4.1. Caminho A (O TCC "Suficiente"): O Refoco na Estimação de Retornos (μ)**
**Ação:** Este caminho *aceita* a sua metodologia falha e a torna *coerente*.
**Execução:**
**Mude o Título:** Para algo como: "O Impacto de Modelos Preditivos (ARIMA, LSTM) na Estimação de Retornos Esperados para Otimização Média-Variância no Brasil".
**Exclua a PMPT:** *Delete* todas as menções a PMPT, CVaR, Sortino, "risco downside", "semivariância" e "aversão à perda" dos seus Capítulos 1, 2 e 4.
**Delete a Crítica à Variância:** Delete a seção 2.9 1 que critica a variância como simétrica.
**Delete a Análise de Curtose/Assimetria:** Delete a seção 4.1 1 ou reescreva-a para minimizar sua importância.
**Resultado:** Você terá um TCC *coerente*, mas *fraco*. Ele responderá *apenas* à sua questão de pesquisa original (trivial). Ele ainda usará um otimizador falho (M-V), mas pelo menos não estará em guerra consigo mesmo.
**Veredito:** Não recomendado. É um desperdício do seu excelente trabalho teórico.
**4.2. Caminho B (O TCC "Excelente"): Alinhando a Metodologia à Crítica Teórica**
**Ação:** Este caminho *abraça* a sua crítica. Ele transforma seu TCC de um teste de *inputs* para um teste de *modelos*. Ele *incorpora*.1
**Nova Questão de Pesquisa:** "No mercado brasileiro (caracterizado por 'caudas pesadas'), o desempenho do portfólio é mais sensível à melhoria dos *inputs* (via LSTM) ou à melhoria do *otimizador* (via CVaR)?"
**Novo Desenho Experimental (Cap. 3):** Você não testará 3 carteiras. Você testará 6 (ou 9). O objetivo é criar uma "matriz de competição" que separe o efeito do *input* (Eixo X) do efeito do *otimizadador* (Eixo Y).
Tabela 1: Proposta de Matriz de Competição para o Backtest (Novo Cap. 3.4)Esta tabela deve ser incluída em seu TCC para explicar o desenho experimental.


| Otimizador \ Input de Retorno (μ) | C1: Média Histórica (Baseline) | C2: ARIMA (Preditivo Linear) | C3: LSTM (Preditivo Não-Linear) |
| --- | --- | --- | --- |
| Linha 1: MPT (Média-Variância)(Otimizador: Máx. Índice de Sharpe) | Portfólio 1(MPT Clássico - Seu plano atual) | Portfólio 2(Seu plano atual) | Portfólio 3(Seu plano atual) |
| Linha 2: PMPT (Média-CVaR)(Otimizador: Min. CVaR para um Retorno-Alvo) | Portfólio 4(Novo - PMPT com input simples) | Portfólio 5(Novo) | Portfólio 6(Novo - Modelo mais avançado) |
| (Opcional) Linha 3: Risco Ingênuo(Otimizador: 1/N - Pesos Iguais) | Portfólio 7 1 | (Não aplicável) | (Não aplicável) |


*   **Implicação:**
    *   Ao comparar *horizontalmente* (ex: Portfólio 1 vs 2 vs 3), você responde à sua pergunta *original* (Qual *input* é melhor para MPT?).
    *   Ao comparar *verticalmente* (ex: Portfólio 3 vs 6), você responde à pergunta *nova* (Qual *otimizador* é melhor para o input LSTM?).
    *   Ao comparar *diagonalmente* (ex: Portfólio 1 vs 6), você testa o modelo "totalmente ingênuo" contra o "totalmente avançado".
    *   O Portfólio 7 (1/N) serve como o *benchmark* definitivo contra o *estimation error*, conforme a literatura que você já citou.

**4.3. Novas Métricas de Avaliação (Cap. 3.6)**
Sua metodologia deve *privilegiar* as métricas de PMPT, dado que seus dados 1 provam que elas são necessárias. O Índice de Sharpe deve ser incluído apenas como um benchmark do modelo MPT.
**Métricas Primárias (PMPT):**
**Índice de Sortino:** A métrica de retorno/risco que *se alinha* à sua crítica da variância (usa semivariância).
**Maximum Drawdown (MDD):** A medida mais prática de risco de perda para um investidor.
**CVaR (ou Expected Shortfall):** O valor real do risco de cauda (o que você minimizou no Portfólio 4-6).
**Métricas Secundárias (MPT/Outras):**
**Índice de Sharpe:** Para comparar (e provavelmente mostrar sua inferioridade).
**Volatilidade (σp):** Para mostrar como a M-V e a M-CVaR alocam o risco de forma diferente.1
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

**4.4. Ações Imediatas para o Cap. 3 (Metodologia)**
Você *deve* transformar suas "perguntas" 1 em "decisões".
**Para ARIMA (Carteira 2 e 5):** *Decida.* A recomendação é: "Para cada ativo, em cada janela de rebalanceamento, um modelo Auto-ARIMA (usando, por exemplo, o critério AIC ou BIC) será ajustado para selecionar os parâmetros (p,d,q) e prever o retorno do mês seguinte."
**Para LSTM (Carteira 3 e 6):** *Decida.* Você não pode deixar isso em aberto. Exemplo: "Uma arquitetura LSTM univariada será treinada para cada ativo. A rede consistirá em 2 camadas LSTM empilhadas com 50 neurônios cada, seguidas por uma camada Densa. O modelo usará um *lookback period* de 60 dias (3 meses de pregão) para prever o retorno do mês seguinte (Período de Teste)."
**Para CVaR (Carteira 4, 5, 6):** Siga a literatura.1 A otimização M-CVaR é tipicamente resolvida por Programação Linear. Você não maximiza um "Índice de CVaR"; você *minimiza o CVaR* (risco) sujeito a uma *restrição de retorno mínimo* (μ). Você terá que definir qual será esse retorno mínimo (ex: o retorno do CDI, ou o retorno esperado do input).
**Conclusão do Relatório Crítico**
Seu rascunho 1 é paradoxal. Ele contém os elementos de um TCC fraco e, simultaneamente, os elementos de uma pesquisa de mestrado. Seu referencial teórico e sua análise de dados (Cap 2 e 4.1) são fortes e demonstram uma compreensão profunda das limitações da MPT. Sua metodologia (Cap 3) é fraca e ignora essa compreensão.
A solicitação de uma crítica "contundente" é justificada. O "Caminho B" (a Matriz de Competição 3x2) é a única trajetória que alinha sua metodologia à sua crítica. Embora exija mais trabalho computacional (implementar a otimização M-CVaR), ele utiliza *toda* a pesquisa que você já realizou (MPT, PMPT, ARIMA, LSTM) e responde a uma pergunta de pesquisa genuinamente interessante e relevante. A referência 1 que você acabou de encontrar não é apenas uma citação; é o seu guia prático para fazer essa transição.Este relatório fornece uma análise crítica e recomendações estratégicas para o trabalho "Moderna Teoria das Carteiras no Mercado de Ações Brasileiro".1 A análise foi solicitada como "contundente" e focada em "mostrar o caminho a melhorar", e será estruturada como um *peer review* acadêmico sênior.
O documento enviado 1, um trabalho de conclusão de curso (TCC), encontra-se em um estado de contradição fundamental: o referencial teórico (Capítulo 2) e a análise de dados preliminar (Capítulo 4.1) constroem um argumento devastador *contra* a aplicação da otimização Média-Variância (M-V) de Markowitz em mercados emergentes. No entanto, a metodologia (Capítulo 3) propõe usar *exclusivamente* essa mesma abordagem M-V que o trabalho já invalidou teoricamente.
Este relatório está estruturado em quatro partes:
**Análise Estrutural:** Uma auditoria das falhas formais, coerência e nível de prontidão do documento.
**Auditoria do Referencial Teórico:** Uma análise crítica do fluxo de argumentos no Capítulo 2.
**Dissecação da Metodologia:** Uma demonstração de como os Capítulos 3 e 4.1 estão em conflito direto.
**Recomendações Estratégicas:** O "caminho a melhorar", oferecendo um redesenho metodológico robusto que alinha a prática à teoria.

## Parte 1: Análise da Estrutura, Coerência e Nível de Prontidão do Documento

Um trabalho acadêmico só pode ser robusto se sua estrutura for coesa e profissional. O manuscrito atual 1 falha em diversos pontos editoriais e estruturais básicos, indicando um estado de rascunho inicial que requer atenção imediata.

### 1.1. Incompletude e Marcadores de Posição

O documento está repleto de seções inacabadas. Capítulos e seções cruciais, incluindo 5, 8, 9, 10, 11 e 12, contêm apenas texto de preenchimento (placeholders) como "Sfgsdgsd" e "Gdfsgsdg".1 Notavelmente, o Capítulo 6 (Resultados do Backtest) e o Capítulo 13 (Conclusão) estão vazios.1
Isso é esperado de um rascunho, mas o cronograma apresentado (Capítulo 6 no sumário, mas Tabela 1 na prática) 1 sugere que a metodologia já deveria ter sido finalizada em junho e a formatação ABNT concluída em julho. O estado atual do documento em novembro está perigosamente desalinhado com o cronograma proposto.

### 1.2. Caos Estrutural no Sumário (Capítulo 2)

O sumário apresenta um erro editorial grave que reflete desorganização no fluxo de argumentos.1 As seções 2.6 e 2.7 são idênticas, assim como suas subseções 2.6.1 e 2.7.1:
2.6. Métricas e Modelos de Equilíbrio Derivados da MPT
2.6.1. O Índice de Sharpe (IS): Métrica de Desempenho Ajustado ao Risco Total
2.7. Métricas e Modelos de Equilíbrio Derivados da MPT
2.7.1. O Índice de Sharpe (IS): Métrica de Desempenho Ajustado ao Risco Total
Isso não é apenas um erro de digitação; sugere que seções foram escritas de forma isolada, sem uma integração lógica. A discussão sobre a MPT, CAPM, CML, SML e o Índice de Sharpe deve ser consolidada em uma narrativa única e coesa, eliminando a redundância.1

### 1.3. A Metodologia como "Lista de Desejos"

A seção 3.4 (Modelagem dos Inputs) não é uma metodologia; é um conjunto de perguntas em aberto.1 Por exemplo:
"Carteira 2 (ARIMA):... (Como p,d,q serão escolhidos? Auto-ARIMA?)"
"Carteira 3 (LSTM):... (Definir a arquitetura: quantas camadas? neurônios? lookback period?)"
Uma metodologia científica deve ser *replicável*. Essas perguntas tornam o estudo *irreplicável*. O pesquisador deve *definir* esses hiperparâmetros e abordagens *antes* da execução, e não deixar isso em aberto no documento final. A ausência dessas definições operacionais invalida, por enquanto, todo o Capítulo 3.

### 1.4. Integridade do Referencial (Capítulo 7)

O Capítulo 7 (Referências) está ausente no corpo do documento.1 Embora o sumário liste a seção 1, a lista bibliográfica que dá suporte às citações no texto (ex: "Damodaran, 2007", "Rockafellar e Uryasev 2000, 2002") não está presente.1 Esta é uma falha acadêmica elementar que deve ser corrigida com urgência.

## Parte 2: Auditoria Crítica do Referencial Teórico (Capítulo 2)

O conteúdo do Capítulo 2 é, paradoxalmente, o ponto mais forte do TCC e, ao mesmo tempo, a principal evidência contra sua própria metodologia. O autor demonstra uma compreensão profunda das limitações da MPT.

### 2.1. O Problema da Estimação de Parâmetros (Inputs)

A discussão sobre o "Problema do Erro de Estimação" (*Estimation Error*) é excelente.1 O trabalho identifica corretamente que o otimizador M-V de Markowitz é frequentemente descrito como um "maximizador de erro".1 O texto aponta que o modelo "tende a alocar pesos significativos nos ativos que... apresentaram as características mais atraentes" na amostra de treino, que são "justamente onde o erro da estimação é maior".1
O autor diagnostica corretamente que o modelo M-V é "extremamente instável em relação aos retornos esperados".1 A proposta de usar ARIMA e LSTM (Cap 3.4) 1 é, portanto, uma tentativa de tratar essa "doença", fornecendo um vetor de retorno esperado ($\mu$) superior à "inadequação da média histórica".1 Esta é uma linha de pesquisa válida e central para o trabalho.

### 2.2. A Falha da Premissa de Normalidade e a Inadequação da Variância

Esta é a segunda e mais importante crítica desenvolvida no Capítulo 2. O trabalho afirma que "A variância... trata os desvios positivos (ganhos) e negativos (perdas) em relação à média com pesos iguais".1 Isso é corretamente contrastado com a "aversão à perda" e a preferência do investidor por métricas de *downside risk*.1
No entanto, esta crítica fundamental *não é resolvida* pela metodologia proposta no Capítulo 3. Usar um modelo LSTM para prever $\mu$ não altera o fato de que o otimizador (M-V, via Índice de Sharpe) ainda usará a *variância* ($\sigma^2$) como medida de risco.1 O otimizador continuará a penalizar portfólios com alta volatilidade *positiva* (ganhos) e tratará ganhos e perdas simetricamente, um comportamento que o próprio autor já argumentou ser conceitualmente falho.

### 2.3. A Introdução da PMPT (Pós-Moderna Teoria do Portfólio)

O TCC introduz a PMPT, o Índice de Sortino e, crucialmente, o *Conditional Value at Risk (CVaR)* como as *soluções* para as falhas da MPT.1 O texto os posiciona como métricas superiores que focam no *downside risk*, citando Rockafellar e Uryasev (2000, 2002).1
Aqui reside a contradição central. O trabalho apresenta a PMPT/CVaR como a solução teórica para os problemas da MPT. No entanto, na metodologia (Capítulo 3), essa solução é completamente ignorada. A nova referência bibliográfica 1, recentemente adicionada, é inteiramente sobre a superioridade da otimização Média-CVaR em contextos de *tail risk* (risco de cauda).1 O trabalho elogia a PMPT, mas se propõe a testar apenas a MPT.

### 2.4. Síntese da Crítica ao Capítulo 2

O Capítulo 2 identifica dois problemas distintos na MPT:
**Problema de Input:** O vetor de retorno ($\mu$) é mal estimado (o "maximizador de erros").1
**Problema de Modelo:** O otimizador (M-V) é conceitualmente falho (usa variância, assume normalidade).1
A metodologia proposta (Capítulo 3) oferece uma solução (ARIMA/LSTM) *apenas* para o Problema 1. Ela *ignora completamente* o Problema 2, que o próprio autor e seus dados (como veremos na Parte 3) argumentam ser o mais grave.

## Parte 3: Dissecação da Metodologia (Cap. 3) e dos Resultados Preliminares (Cap. 4)

Esta seção demonstra como a metodologia falha em responder aos desafios levantados pelo referencial teórico e é, de fato, invalidada pelos próprios dados preliminares do autor.

### 3.1. A Insuficiência da Questão de Pesquisa

A questão de pesquisa declarada é: "Qual é o impacto no desempenho... de carteiras Média-Variância... quando o input de retorno esperado é estimado por modelos preditivos (ARIMA e LSTM) em comparação com a tradicional média histórica...?".1
No contexto da revisão de literatura, essa pergunta é trivial. Ela presume que a Média-Variância é o campo de batalha correto. O autor já sabe, com base no Capítulo 2 1 e na literatura de finanças 1, que os retornos não são normais e que a M-V é um "maximizador de erros".1
Uma questão de pesquisa de nível superior, derivada do próprio trabalho, seria: "A melhoria do desempenho do portfólio no Brasil (um mercado não-normal) vem da substituição de *inputs* (Média Histórica $\rightarrow$ LSTM) ou da substituição do *modelo* (M-V $\rightarrow$ M-CVaR)?" O TCC, como está desenhado, não pode responder a isso.

### 3.2. Usando os Próprios Dados (Cap 4.1) Contra a Metodologia (Cap 3.5)

Este é o ponto mais crítico do relatório. A análise de dados do próprio autor invalida sua metodologia.
**O Dado (Cap 4.1):** O autor observa "valores de curtose dramaticamente elevados".1 Especificamente, cita-se Assaí (ASAI3) com uma curtose de **2469,69** e Pão de Açúcar (PCAR3) com **408,26**. O autor identifica isso corretamente como *leptocurtose* ("caudas pesadas"), indicando que eventos extremos são muito mais frequentes do que a distribuição normal prevê.1
**A Metodologia (Cap 3.5):** O autor propõe otimizar para o "Máximo Índice de Sharpe".1
**A Contradição:** O Índice de Sharpe é definido como $IS = (R_p - R_f) / \sigma_p$. O denominador é o *desvio padrão* ($\sigma_p$), a raiz quadrada da variância. A variância e o desvio padrão são medidas de risco completas e suficientes *apenas* se a distribuição dos retornos for normal (ou, no máximo, elíptica).
Os dados (curtose de 2469,69) não são normais; eles são um exemplo extremo de "caudas pesadas". A MPT (Média-Variância) otimiza para o *segundo momento* da distribuição (a variância). Em distribuições leptocúrticas, os *momentos superiores* (como a curtose, o quarto momento) dominam o risco. Otimizar apenas para o segundo momento (variância) é, portanto, um erro metodológico fundamental. O otimizador M-V irá *ignorar* o risco de cauda (tail risk), que é justamente o risco mais perigoso e proeminente diagnosticado nos dados.
A nova referência 1 corrobora exatamente isso, afirmando que a métrica de risco variância "subestimou a probabilidade de eventos oriundos de *tail risk*".1

### 3.3. O "Ato Falho" Metodológico (Cap 4.1)

No final da Seção 4.1, o autor escreve a "arma fumegante" que prova a dissonância do trabalho:
"A constatação empírica [de leptocurtose]... fornece a justificativa central para este trabalho... A falha da premissa de normalidade valida: **O uso de métricas de risco da Pós-Moderna Teoria de Carteiras (PMPT), como o Índice de Sortino**... e a exploração de modelos preditivos (ARIMA e, especialmente, LSTM)..." 1
Esta afirmação está 100% correta. Os dados *validam* o Índice de Sortino (PMPT). No entanto, a Metodologia (Cap 3.6) lista o Sortino apenas como uma *métrica de avaliação*, enquanto o processo de *otimização* (Cap 3.5) ainda é baseado no Índice de Sharpe (MPT).1
Não se pode apenas *avaliar* com a PMPT se a carteira foi *otimizada* com a MPT. Isso é misturar paradigmas de forma incoerente. Se os dados validam a PMPT, o autor deve *OTIMIZAR* usando métricas da PMPT (ex: minimizar a Semivariância para maximizar o Sortino, ou minimizar o CVaR). O diagnóstico de PMPT foi usado apenas para justificar um tratamento de MPT, o que é logicamente falho.

## Parte 4: O Caminho a Melhorar (Recomendações Estratégicas)

Existem duas trajetórias para corrigir o trabalho. O Caminho A é "suficiente", mas medíocre. O Caminho B é "excelente" e transforma este TCC em uma pesquisa de alto nível.

### 4.1. Caminho A (O TCC "Suficiente"): O Refoco na Estimação de Retornos (**$\mu$**)

Esta abordagem *aceita* a metodologia falha e a torna *coerente* através da exclusão.
**Mudar o Título:** Para algo como: "O Impacto de Modelos Preditivos (ARIMA, LSTM) na Estimação de Retornos para Otimização Média-Variância no Brasil".
**Remover a PMPT:** Excluir *todas* as menções a PMPT, CVaR, Sortino, "risco downside", "semivariância" e "aversão à perda" dos Capítulos 1, 2 e 4.
**Remover a Crítica à Variância:** Excluir a seção que critica a variância como simétrica.1
**Remover a Análise de Curtose/Assimetria:** Excluir a Seção 4.1 ou reescrevê-la para minimizar sua importância.1
**Resultado:** O TCC se tornará *coerente*, mas *fraco*. Ele responderá apenas à questão de pesquisa original (trivial), usando um otimizador que o próprio autor sabe ser falho. **Veredito: Não recomendado.** É um desperdício do excelente trabalho teórico já realizado.

### 4.2. Caminho B (O TCC "Excelente"): Alinhando a Metodologia à Crítica Teórica

Esta abordagem *abraça* a crítica teórica e a nova referência.1 Ela transforma o TCC de um teste de *inputs* para um teste de *modelos vs. inputs*.
**Nova Questão de Pesquisa:** "No mercado brasileiro (caracterizado por 'caudas pesadas'), o desempenho do portfólio é mais sensível à melhoria dos *inputs* (via LSTM) ou à melhoria do *otimizador* (via CVaR)?"
**Novo Desenho Experimental (Cap. 3):** O TCC não testará 3 carteiras. Testará 6 (ou 9). O objetivo é criar uma "matriz de competição" que separe o efeito do *input* (Eixo X) do efeito do *otimizador* (Eixo Y).
Tabela 1: Proposta de Matriz de Competição para o Backtest (Novo Cap. 3.4)
Esta tabela deve ser incluída no TCC para explicar o desenho experimental.


| Otimizador \ Input de Retorno (μ) | C1: Média Histórica (Baseline) | C2: ARIMA (Preditivo Linear) | C3: LSTM (Preditivo Não-Linear) |
| --- | --- | --- | --- |
| Linha 1: MPT (Média-Variância)(Otimizador: Máx. Índice de Sharpe) | Portfólio 1(MPT Clássico - Plano atual) | Portfólio 2(Plano atual) | Portfólio 3(Plano atual) |
| Linha 2: PMPT (Média-CVaR)(Otimizador: Min. CVaR para um Retorno-Alvo) | Portfólio 4(Novo - PMPT com input simples) | Portfólio 5(Novo) | Portfólio 6(Novo - Modelo mais avançado) |
| (Opcional) Linha 3: Risco Ingênuo(Otimizador: 1/N - Pesos Iguais) | Portfólio 7(Benchmark 1/N - Essencial para comparar com DeMiguel & Nogales, 2009 1) | (Não aplicável) | (Não aplicável) |

**Implicações deste Desenho:**
Comparar *horizontalmente* (Port. 1 vs 2 vs 3) responde à pergunta *original* (Qual *input* é melhor para MPT?).
Comparar *verticalmente* (Port. 3 vs 6) responde à pergunta *nova* (Qual *otimizador* é melhor para o input LSTM?).
Comparar *diagonalmente* (Port. 1 vs 6) testa o modelo "totalmente ingênuo" contra o "totalmente avançado".
O Portfólio 7 (1/N) serve como o *benchmark* definitivo contra o *estimation error*, conforme a literatura já citada.1

### 4.3. Novas Métricas de Avaliação (Cap. 3.6)

A metodologia de avaliação deve *privilegiar* as métricas da PMPT, dado que os dados (Cap 4.1) 1 provam sua necessidade.
**Métricas Primárias (PMPT):**
**Índice de Sortino:** A métrica de retorno/risco que *se alinha* à crítica da variância (usa semivariância).1
**Maximum Drawdown (MDD):** A medida mais prática de risco de perda.
**CVaR (ou Expected Shortfall):** O valor real do risco de cauda.1
**Métricas Secundárias (MPT/Outras):**
**Índice de Sharpe:** Para comparar (e mostrar sua provável inferioridade).1
**Volatilidade ($\sigma_p$):** Para mostrar como M-V e M-CVaR alocam o risco de forma diferente.1
**Retorno Anualizado.**
Tabela 2: Proposta de Tabela de Resultados Finais (Novo Cap. 6)
Esta tabela será a resposta final à sua pesquisa.

| Métrica | Port. 1 (MPT-Média) | Port. 2 (MPT-ARIMA) | Port. 3 (MPT-LSTM) | Port. 4 (CVaR-Média) | Port. 5 (CVaR-ARIMA) | Port. 6 (CVaR-LSTM) | Port. 7 (1/N) | IBOV | CDI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Retorno Anual. |  |  |  |  |  |  |  |  |  |
| Volatilidade Anual. ($\sigma_p$) |  |  |  |  |  |  |  |  |  |
| Índice de Sharpe |  |  |  |  |  |  |  |  |  |
| Índice de Sortino |  |  |  |  |  |  |  |  |  |
| Max Drawdown (MDD) |  |  |  |  |  |  |  |  |  |
| CVaR (95%) Histórico |  |  |  |  |  |  |  |  |  |


### 4.4. Ações Imediatas para o Cap. 3 (Metodologia)

As "perguntas" na metodologia 1 devem ser transformadas em "decisões":
**Para ARIMA (Carteira 2 e 5):** *Definir:* "Para cada ativo, em cada janela de rebalanceamento, um modelo Auto-ARIMA (usando, por exemplo, o critério AIC ou BIC) será ajustado para selecionar os parâmetros (p,d,q) e prever o retorno do mês seguinte."
**Para LSTM (Carteira 3 e 6):** *Definir:* "Uma arquitetura LSTM univariada será treinada para cada ativo. A rede consistirá em 2 camadas LSTM empilhadas com 50 neurônios cada, seguidas por uma camada Densa. O modelo usará um *lookback period* de 60 dias (aprox. 3 meses de pregão) para prever o retorno do mês seguinte."
**Para CVaR (Carteira 4, 5, 6):** *Definir:* "Seguindo a literatura (Rockafellar e Uryasev 2000, 2002) 1, a otimização M-CVaR será resolvida por Programação Linear. O objetivo será *minimizar o CVaR (95%)* sujeito a uma *restrição de retorno mínimo* (ex: o retorno-alvo será o retorno esperado do input, $\mu$, ou o retorno do CDI)."

## Conclusão do Relatório Crítico

O rascunho atual 1 é paradoxal. Ele contém os elementos de um TCC fraco e, simultaneamente, os elementos de uma pesquisa de nível de mestrado. O referencial teórico (Cap. 2) e a análise de dados (Cap. 4.1) são fortes e demonstram uma compreensão profunda das limitações da MPT. A metodologia (Cap. 3) é fraca e ignora essa compreensão.
O "Caminho B" (a Matriz de Competição 3x2) é a única trajetória que alinha a metodologia à crítica teórica. Embora exija mais trabalho computacional (implementar a otimização M-CVaR), ele utiliza *toda* a pesquisa que já foi realizada (MPT, PMPT, ARIMA, LSTM) e responde a uma pergunta de pesquisa genuinamente interessante e relevante. A referência 1 recém-adicionada não é apenas uma citação; é o guia prático para essa transição.
#### Referências citadas
Entrega_14_11_25_Pedro_Reis_TMP.docx
