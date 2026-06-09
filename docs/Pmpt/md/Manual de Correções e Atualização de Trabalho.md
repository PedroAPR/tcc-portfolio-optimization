# Relatório Técnico de Auditoria Acadêmica e Manual de Reestruturação Metodológica do Trabalho de Conclusão de Curso: "Teoria das Carteiras no Mercado de Ações Brasileiro"
## 1. Introdução: O Imperativo da Robustez Teórica e Normativa na Produção Científica Financeira
A produção de conhecimento na área de Finanças Quantitativas exige um alinhamento rigoroso entre a sofisticação dos modelos computacionais aplicados e a solidez dos fundamentos teóricos que os sustentam. O Trabalho de Conclusão de Curso (TCC) intitulado *"Teoria das Carteiras no Mercado de Ações Brasileiro: Comparação entre Otimizadores e Inputs"*, de autoria do discente Pedro Augusto Pinheiro Reis 1, apresenta uma proposta ambiciosa e relevante: integrar a tradição da Teoria Moderna do Portfólio (MPT) com inovações da Teoria Pós-Moderna (PMPT) e abordagens Bayesianas (Black-Litterman), alimentadas por algoritmos de Inteligência Artificial (LSTM).
No entanto, a análise preliminar realizada pela banca examinadora, consubstanciada no relatório *"Descobrindo Lacunas e Vieses do Trabalho"* 1, identificou fragilidades estruturais que comprometem a validade científica dos resultados. Estas fragilidades não residem apenas na execução dos modelos, mas na compreensão epistemológica de suas premissas e na conformidade com os padrões de comunicação científica vigentes, especificamente a norma **ABNT NBR 10520:2023**.
Este relatório técnico atua, portanto, como um manual exaustivo de procedimentos para a correção e reescrita do referido TCC. O objetivo é transcender a mera correção pontual, fornecendo uma base doutrinária profunda para cada alteração solicitada. A reestruturação proposta visa elevar o trabalho do nível de um exercício computacional para uma contribuição acadêmica robusta, que dialoga adequadamente com a literatura canônica e respeita as normas de citação atualizadas.
A análise a seguir divide-se em três pilares fundamentais: (1) **Conformidade Normativa**, detalhando as implicações da atualização da ABNT de 2023; (2) **Fundamentação Teórica**, aprofundando os conceitos de Racionalidade, MPT, PMPT, Black-Litterman e Fatores de Risco; e (3) **Rigor Metodológico**, abordando os desafios da implementação de Machine Learning em séries temporais financeiras.
## 2. Pilar Normativo: A Nova Dinâmica das Citações Acadêmicas (ABNT NBR 10520:2023)
A normalização acadêmica é a linguagem comum que permite a rastreabilidade e a verificação do conhecimento científico. A utilização de normas revogadas não constitui apenas um erro estético, mas sinaliza uma desconexão do pesquisador com o estado da arte da comunicação científica. O texto submetido pelo discente 1 utiliza padrões da NBR 10520:2002, que foi substituída em julho de 2023. A correção deste aspecto é mandatória e estrutural.
### 2.1. A Evolução da Grafia de Autoria: Do Destaque à Fluidez
Historicamente, a norma brasileira privilegiava o destaque visual dos sobrenomes dos autores nas citações entre parênteses, exigindo o uso de caixa alta (letras maiúsculas). A norma de 2002 estabelecia que citações indiretas no final de parágrafos deveriam seguir o formato (SOBRENOME, Ano). Esta prática, embora facilitasse a localização visual das referências, criava uma ruptura no fluxo de leitura e distanciava a norma brasileira dos padrões internacionais, como APA (*American Psychological Association*) e estilo Vancouver, que prezam pela fluidez do texto.
A **NBR 10520:2023** introduz uma mudança paradigmática: a uniformização da grafia dos sobrenomes em **Caixa Alta e Baixa** (apenas a primeira letra maiúscula), independentemente da posição da citação (dentro ou fora dos parênteses).2 Esta alteração reflete uma tendência de "limpeza" tipográfica, reduzindo a poluição visual do texto acadêmico.
Diagnóstico no TCC:
O texto atual apresenta consistentemente citações no formato revogado. No Resumo e na Introdução, observam-se ocorrências como (MARKOWITZ, 1952; 1959) e (SORTINO; VAN DER MEER, 1991).1 Estas formas violam a regra atual de apresentação.
Procedimento de Correção:
O discente deve realizar uma revisão global do documento, utilizando a ferramenta de "Localizar e Substituir" com supervisão manual, para converter todas as ocorrências de citações.
**De:** (MARKOWITZ, 1952)
**Para:** (Markowitz, 1952)
**De:** (BLACK; LITTERMAN, 1992)
**Para:** (Black; Litterman, 1992)
Esta alteração deve ser aplicada também às citações de pessoas jurídicas que possuem nomes por extenso (ex: (Banco Central do Brasil, 2023)), mantendo-se em caixa alta apenas as siglas consolidadas (ex: (IBGE, 2022)), conforme prevê a nova norma.2
### 2.2. A Lógica da Pontuação em Citações
Outra alteração crítica trazida pela atualização de 2023 refere-se à pontuação final em sentenças que terminam com citações. A norma anterior permitia ambiguidades ou interpretações variadas sobre a colocação do ponto final (antes ou depois dos parênteses) dependendo se a citação era direta ou indireta e de sua extensão.
A norma vigente estabelece inequivocamente que a citação entre parênteses é parte integrante da sentença. Portanto, o ponto final deve, obrigatoriamente, ser posicionado **após** o fechamento dos parênteses.3 O ponto final encerra a unidade de pensamento, e a autoria é componente fundamental dessa unidade.
Diagnóstico no TCC:
O relatório da banca aponta erros como "...conclusão do autor." (Souza, 2023)..1 Esta construção fragmenta a oração, isolando a referência bibliográfica num limbo sintático.
Procedimento de Correção:
O manual de correção exige que o discente verifique cada final de parágrafo.
**Incorreto:** ...risco sistêmico. (Markowitz, 1959)
**Incorreto:** ...risco sistêmico. (Markowitz, 1959). (Ponto duplicado ou antes).
**Correto:** ...risco sistêmico (Markowitz, 1959).
### 2.3. O Uso de ***et al.*** e Recursos Tipográficos
A expressão latina *et al.* (abreviação de *et alii*, significando "e outros") é utilizada para conferir concisão a citações de obras com múltiplos autores (quatro ou mais). A norma de 2023 clarifica que o uso de *et al.* é facultativo, mas exige padronização no documento. Se o autor optar por listar todos os autores na primeira citação, deve fazê-lo em todas, ou adotar o *et al.* consistentemente.2
Adicionalmente, a nova norma recomenda o uso de **itálico** para expressões latinas (*et al.*, *apud*, *ibidem*, *op. cit.*), uma prática que variava em interpretações anteriores. O uso do itálico destaca visualmente que se trata de termo estrangeiro, alinhando-se às regras gerais de formatação de textos em língua portuguesa.
**Tabela 1: Matriz de Convergência Normativa (NBR 10520)**

| Elemento Normativo | Padrão Revogado (2002) | Padrão Vigente (2023) | Ação Requerida no TCC |
| --- | --- | --- | --- |
| Autoria (Parênteses) | CAIXA ALTA: (SILVA, 2023) | Caixa Alta/Baixa: (Silva, 2023) | Substituição Integral |
| Ponto Final | Variável | Após parênteses: ...texto (Autor, 2023). | Revisão Sintática |
| Expressões Latinas | Fonte normal (usual) | Itálico recomendado: et al. | Formatação Estilística |
| Citação de Jurídica | (BANCO MUNDIAL, 2020) | (Banco Mundial, 2020) | Ajuste de Capitalização |

## 3. Pilar Teórico: Revisitando os Fundamentos da Gestão de Carteiras
A análise do referencial teórico submetido 1 revela um "salto" conceitual: o texto parte diretamente para a modelagem matemática de risco e retorno sem estabelecer as bases epistemológicas que justificam por que os agentes econômicos se comportam dessa maneira. O manual de correção impõe a necessidade de "voltar um passo atrás" para fundamentar a racionalidade.
### 3.1. A Gênese da Decisão: Teoria da Utilidade Esperada e seus Axiomas
A Moderna Teoria do Portfólio (MPT) não nasceu no vácuo; ela é uma aplicação direta da **Teoria da Utilidade Esperada (Expected Utility Theory - EUT)**, formalizada por Von Neumann e Morgenstern (1944). O texto do discente falha ao assumir a racionalidade do investidor como um dado axiomático implícito, sem explicitá-la.1
Para corrigir essa lacuna, é imperativo introduzir uma subseção dedicada aos **Axiomas de Von Neumann-Morgenstern**. Sem estes axiomas, a função de utilidade quadrática que Markowitz utiliza para justificar a média-variância não se sustenta logicamente.
**Os Quatro Pilares da Racionalidade VNM:**
**Completude (Completeness):** O investidor é capaz de comparar qualquer par de ativos ou portfólios. Para quaisquer opções A e B, ele prefere A, prefere B, ou é indiferente. Não existe "não sei".
**Transitividade (Transitivity):** As preferências são consistentes e não cíclicas. Se o investidor prefere A a B, e B a C, ele logicamente deve preferir A a C. A violação deste axioma permitiria a "arbitragem de dinheiro" (money pump), onde o agente pagaria infinitamente para trocar de C para B, de B para A, e de A para C.
**Continuidade (Continuity):** Não existem preferências "infinitas". Se A é preferível a B, e B a C, existe uma probabilidade $p$ tal que o investidor é indiferente entre receber B com certeza ou uma loteria entre A e C.
**Independência (Independence):** Este é o axioma mais crítico e o mais atacado pelas finanças comportamentais. Ele dita que se A é preferido a B, então uma mistura de A com um terceiro ativo C manterá a mesma ordem de preferência de uma mistura de B com C.
A Crítica Comportamental e o Paradoxo de Allais:
O relatório de crítica 1 exige que, ao apresentar a racionalidade, o texto discuta imediatamente suas limitações. O Paradoxo de Allais (1953) demonstra empiricamente que seres humanos violam sistematicamente o axioma da Independência quando confrontados com certezas versus probabilidades altas (o "Efeito Certeza").
Inserir essa discussão não é apenas "encher linguiça"; é fundamental para justificar o uso posterior da PMPT e de métricas como o Índice de Sortino e CVaR. Se o investidor não segue a utilidade esperada perfeitamente, mas sim a Teoria do Prospecto (aversão à perda e não à variância), então a MPT de Markowitz é uma aproximação imperfeita da satisfação do investidor.
### 3.2. Moderna Teoria do Portfólio (MPT): Correções Conceituais e "Maximização de Erros"
O texto original descreve a MPT corretamente em termos gerais, mas comete imprecisões que denotam superficialidade.
Mitigação vs. Eliminação de Risco:
O discente sugere em trechos que a diversificação elimina o risco. O manual deve corrigir essa afirmação terminante. A diversificação, segundo Markowitz, assintoticamente elimina o risco não-sistemático (idiossincrático). O risco de mercado (sistemático), representado pela covariância média entre os ativos, permanece irredutível apenas com a diversificação de ativos dentro do mesmo mercado.1
A Patologia da Otimização: "Maximização de Erros":
O relatório menciona o problema de estimação, mas o texto precisa atribuir a devida paternidade intelectual a esse conceito. Richard Michaud (1989) cunhou o termo "Otimizadores de Média-Variância são Maximizadores de Erros".
A explicação teórica necessária é: os algoritmos de otimização matemática são "cegos" à incerteza estatística dos inputs. Eles tratam a média estimada ($\bar{x}$) como se fosse a média populacional verdadeira ($\mu$).
Se um ativo tem um retorno verdadeiro de 10%, mas o erro de amostragem mostra 15%, o otimizador alocará excessivamente nele ("solução de canto").
Se o retorno amostral for 5% (subestimado), o otimizador venderá o ativo.
Resultado: O portfólio "ótimo" é, na verdade, uma coleção dos ativos com os maiores erros de estimação positiva.
A Falácia da Normalidade:
O texto deve ser expandido para incluir os momentos estatísticos superiores: Assimetria (Skewness) e Curtose (Kurtosis). O mercado brasileiro (B3) é historicamente leptocúrtico (caudas gordas). A MPT assume que retornos seguem uma distribuição Normal Gaussiana. Em uma distribuição normal, eventos de 5 ou 6 desvios padrão são virtualmente impossíveis. Na realidade financeira, eles ocorrem a cada década. O uso da variância (segundo momento) ignora o risco de cauda, subestimando a probabilidade de ruína.
### 3.3. Teoria Pós-Moderna do Portfólio (PMPT): Autoria e Definição Precisa
O discente associa a PMPT quase exclusivamente a Frank Sortino. Embora Sortino seja o grande divulgador, a estrutura teórica foi formalizada sob o nome PMPT por **Brian M. Rom e Kathleen W. Ferguson** (1993, 1994).1 A omissão desses autores é uma falha bibliográfica séria.
Diferenciação Matemática: Desvio Padrão vs. Desvio de Downside:
O texto precisa explicar a fórmula do LPM (Lower Partial Moment). Enquanto a variância mede a dispersão ao redor da média (tanto lucros quanto prejuízos), o LPM mede a dispersão apenas abaixo de um alvo (Target Return ou MAR - Minimum Acceptable Return).
A fórmula do Índice de Sortino deve ser corrigida e explicitada:


$$Sortino = \frac{R_p - MAR}{DD_{MAR}}$$

Onde $R_p$ é o retorno do portfólio, $MAR$ é o Retorno Mínimo Aceitável (que pode ser diferente da taxa livre de risco $R_f$), e $DD_{MAR}$ é o Desvio de Downside em relação a esse MAR. O Sharpe Ratio usa $R_f$ e Desvio Padrão Total ($\sigma$). A diferença é crucial: para um investidor, volatilidade para cima ("ganhar muito") não é risco, é felicidade. A MPT penaliza essa felicidade; a PMPT não.
### 3.4. O Modelo Black-Litterman: A Síntese Bayesiana
O capítulo sobre Black-Litterman (BL) 1 precisa transcender a descrição funcional e entrar na natureza estatística do modelo. O BL não é apenas uma "mistura"; é uma aplicação formal da **Inferência Bayesiana** em Finanças.
**A Mecânica do Modelo:**
**Prior (A Priori):** O estado de "neutralidade". Assume-se que o mercado é eficiente e que o CAPM é válido. Portanto, os retornos esperados "implícitos" são aqueles que fazem com que o Portfólio de Mercado atual seja o portfólio ótimo. Isso "ancora" a otimização na realidade da capitalização de mercado, evitando as soluções de canto extremas da MPT.
**Likelihood (Verossimilhança - As Visões):** As informações novas trazidas pelo investidor. No caso deste TCC, as "visões" não são opiniões subjetivas, mas sim as previsões quantitativas geradas pelos modelos ARIMA e LSTM.
**Posterior (A Posteriori):** O novo vetor de retornos esperados e a nova matriz de covariância.
O Parâmetro Tau ($\tau$) e a Controvérsia:
O parâmetro escalar $\tau$ representa o grau de incerteza sobre o Prior (equilíbrio). Existe um debate na literatura (Black & Litterman vs. Satchell & Scowcroft vs. Idzorek) sobre como calibrar $\tau$.
A visão original sugeria um $\tau$ pequeno (próximo de zero).
A visão moderna (Idzorek) sugere que o valor de $\tau$ torna-se irrelevante se a matriz de incerteza das visões ($\Omega$) for calibrada proporcionalmente a ele.
O TCC deve mencionar essa nuance para demonstrar profundidade. A calibração correta de $\Omega$ baseada na "confiança" (neste caso, talvez o erro quadrático médio dos modelos de Machine Learning) é o que dita o sucesso do BL.
### 3.5. Fama-French: O Salto de 3 para 5 Fatores e a Redundância do HML
O discente cita "Fatores Fama-French" sem distinguir claramente as versões do modelo, o que é perigoso dado o avanço da teoria em 2015.
O Modelo de 5 Fatores (2015):
Em 2015, Fama e French publicaram "A five-factor asset pricing model" 4, expandindo o modelo original de 1993 (Mercado, Tamanho-SMB, Valor-HML) para incluir:
**RMW (Robust Minus Weak):** Fator de Rentabilidade (Profitability). Empresas com alta rentabilidade operacional superam as de baixa.
**CMA (Conservative Minus Aggressive):** Fator de Investimento (Investment). Empresas que investem de forma conservadora (crescimento lento de ativos) superam as agressivas.
A Descoberta da Redundância do HML:
A instrução mais crítica para este capítulo é a inclusão da descoberta sobre a redundância do fator Valor (HML). Fama e French (2015) notaram que, ao regressar os retornos usando os 5 fatores, o coeficiente do HML tornava-se estatisticamente insignificante em muitos cenários.5
Explicação Econômica: O "efeito valor" (comprar empresas baratas em relação ao valor contábil) é, na verdade, uma proxy para rentabilidade e investimento. O modelo de desconto de dividendos mostra que, fixando-se o preço, um valor contábil mais alto implica menor rentabilidade esperada ou menor investimento. Assim, RMW e CMA "absorvem" o poder explicativo do HML.
Ignorar essa descoberta ao utilizar o modelo de 5 fatores é um erro grave. O aluno deve testar ou, no mínimo, discutir teoricamente se, no mercado brasileiro, essa redundância se mantém (estudos em mercados emergentes as vezes divergem).6
## 4. Pilar Metodológico: Robustez em Machine Learning e Backtesting
A metodologia proposta — usar ARIMA e LSTM para prever retornos e alimentar o Black-Litterman — é sofisticada, mas carrega riscos ocultos que o manual deve endereçar.
### 4.1. LSTM e o Espectro do Overfitting
Redes Neurais Recorrentes do tipo LSTM (Long Short-Term Memory) são excelentes em capturar dependências temporais não-lineares. Contudo, em finanças, a relação sinal-ruído é extremamente baixa. O risco é que a LSTM aprenda o "ruído" do passado (overfitting) em vez do padrão estrutural.
O texto deve detalhar os mecanismos de regularização utilizados:
**Dropout:** Desativação aleatória de neurônios durante o treinamento para forçar redundância e robustez.
**Early Stopping:** Interrupção do treinamento quando o erro no conjunto de validação começa a subir, mesmo que o erro no treino continue caindo.
**Validação Walk-Forward:** O uso estrito de janelas deslizantes onde o modelo nunca "vê" dados do futuro. O conjunto de teste deve ser sempre posterior ao de treino.
### 4.2. O Desafio do Benchmark: A Regra do 1/N
Um erro comum em teses complexas é comparar o "Super Modelo" apenas com o índice de mercado (Ibovespa). A literatura financeira (DeMiguel, Garlappi, & Uppal, 2009) estabeleceu um benchmark muito mais difícil: a Carteira Ingênua 1/N (pesos iguais em todos os ativos).
Devido aos erros de estimação nos modelos de otimização (mesmo no Black-Litterman), a carteira 1/N frequentemente supera modelos complexos fora da amostra porque ela não possui erro de estimação (não há parâmetros para estimar, apenas divide-se o dinheiro por N). Se o modelo proposto pelo aluno não bater o 1/N líquido de custos, isso é um achado científico relevante que deve ser discutido, e não escondido.
### 4.3. Custos de Transação e Turnover
Otimizadores de Média-Variância e modelos dinâmicos tendem a sugerir mudanças drásticas na carteira a cada rebalanceamento. Sem considerar custos de transação (corretagem e spread), o retorno teórico é ilusório. O backtest deve aplicar uma penalidade realista (ex: 0,10% sobre o volume financeiro transacionado) a cada rebalanceamento. Isso penalizará modelos instáveis e valorizará a estabilidade do Black-Litterman (que tende a ter menor turnover que o Média-Variância puro).
## 5. Manual de Procedimentos e Prompt Operacional
Com base na fundamentação acima, apresenta-se o **Manual de Reescrita**, estruturado como um prompt operacional para guiar o discente na correção do documento.
### Instruções Gerais para o Discente
Utilize a estrutura abaixo para revisar cada seção do seu trabalho. Este checklist deve ser verificado ponto a ponto.
#### FASE 1: Varredura Normativa (ABNT 2023)
**Ação Global:** Executar substituição de padrões de citação.
Localizar: (AUTOR, Ano) -> Substituir por: (Autor, Ano).
Verificar citações múltiplas: (SILVA; SOUZA, 2020) -> (Silva; Souza, 2020).
**Ação Pontual:** Revisão de finais de frase.
Mover todos os pontos finais para depois dos parênteses.
Exemplo: ...conclusão da análise (Silva, 2023).
**Estilo:** Aplicar itálico em todas as ocorrências de *et al.*, *ex ante*, *ex post*, *ceteris paribus*.
#### FASE 2: Reescrita do Referencial Teórico (Capítulo 2)
**Subseção: Racionalidade Econômica**
**Inserir:** Definição formal dos Axiomas VNM (Completude, Transitividade, Continuidade, Independência).
**Discutir:** O Paradoxo de Allais como evidência da violação da Independência. Conectar isso à necessidade de métricas de PMPT (aversão à perda).
**Subseção: MPT (Markowitz)**
**Corrigir:** Substituir "eliminação de risco" por "diversificação do risco idiossincrático".
**Adicionar:** Citação a **Michaud (1989)** sobre "Maximização de Erros".
**Expandir:** Discussão sobre Leptocurtose (Caudas Gordas) na B3 e como a variância falha em medir esse risco.
**Subseção: PMPT (Pós-Moderna)**
**Atribuir Autoria:** Citar **Rom & Ferguson (1993)** como criadores do termo e estrutura.
Precisão: Definir Índice de Sortino usando o MAR (Minimum Acceptable Return) e não apenas a taxa livre de risco.

$$Sortino = \frac{R_p - MAR}{\sigma_d}$$
**Subseção: Black-Litterman**
**Definir:** Explicar a estrutura Bayesiana (Prior + Likelihood = Posterior).
**Contextualizar:** Discutir o papel do parâmetro $\tau$ e a calibração da matriz de incerteza $\Omega$ (método de confiança de Idzorek).
**Subseção: Fatores de Risco (Fama-French)**
**Atualizar:** Transitar do modelo de 1993 para o de 2015 (5 Fatores).
**Explicitar:** A redundância estatística do fator HML (Valor) na presença de RMW (Rentabilidade) e CMA (Investimento). Discutir se essa redundância se aplica ao Brasil (citar estudos locais se houver, ou manter a dúvida teórica baseada no *paper* original de 2015).
#### FASE 3: Refinamento Metodológico (Capítulo 3)
**Subseção: Modelos Preditivos (LSTM)**
**Defesa:** Descrever explicitamente as técnicas anti-overfitting (Dropout, Early Stopping).
**Justificativa:** Explicar que o uso do Black-Litterman atua como um "filtro de robustez", pois as previsões da IA (Visões) são "puxadas" para o equilíbrio de mercado se a incerteza ($\Omega$) for alta.
**Subseção: Backtesting**
**Benchmark:** Adicionar explicitamente o portfólio 1/N nas tabelas de resultados.
**Custos:** Incluir parágrafo sobre a incidência de custos de transação e como isso afeta a comparação entre Média-Variância (alto giro) e BL (menor giro).
## 6. Conclusão do Relatório
A reestruturação do TCC *"Teoria das Carteiras no Mercado de Ações Brasileiro"* seguindo este manual garantirá não apenas a aprovação do discente, mas a produção de um documento academicamente relevante. A correção das normas ABNT sinaliza cuidado formal; a inclusão dos fundamentos da racionalidade e a atualização sobre Fama-French sinalizam maturidade teórica; e o rigor no tratamento do Machine Learning (overfitting e benchmarks adequados) sinaliza competência técnica.
O trabalho deixa de ser uma "colagem" de modelos para se tornar uma investigação crítica sobre a eficiência de diferentes paradigmas de alocação no contexto complexo e de caudas pesadas do mercado brasileiro.
**Anexos Sugeridos para o TCC:**
Tabela comparativa de retornos: MPT vs. BL vs. 1/N.
Gráfico de Fronteira Eficiente: Média-Variância vs. Média-CVaR (mostrando a contração da fronteira sob risco de cauda).
Snippet de código (Python/R) demonstrando a implementação da fórmula mestra de Black-Litterman (opcional, mas recomendado para apêndice).
Este relatório encerra a auditoria técnica e normativa, habilitando o discente a proceder com as correções finais para a defesa.
#### Referências citadas
Entrega_4_Pedro_Reis_TMP.docx
ABNT NBR 10520:2023: saiba o que mudou com a atualização da norma de citações, acessado em dezembro 9, 2025, 
Normas para Citações - NBR 10520/2023 | Programa de Pós-Graduação em Educação, acessado em dezembro 9, 2025, 
A five-factor asset pricing model - IDEAS/RePEc, acessado em dezembro 9, 2025, 
Resurrecting the Value Factor from its Redundancy - Financial Management Association, acessado em dezembro 9, 2025, 
FAMA-FRENCH FIVE FACTOR MODEL AND THE NECESSITY 0F VALUE FACTOR: EVIDENCE FROM ISTANBUL STOCK EXCHANGE - DergiPark, acessado em dezembro 9, 2025,
