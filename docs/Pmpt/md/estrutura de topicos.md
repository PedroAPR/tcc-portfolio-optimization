## A Teoria Moderna do Portfólio (MPT)

### O Problema da Seleção de Portfólio: A Revolução de Markowitz (1952)
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


- Dfgdsgds **A Inadequação da Média Histórica ****Simple**
- A Evidência Empírica (DeMiguel & Nogales, 2009)
- **Crítica 2: Sensibilidade Extrema aos Inputs e Imprecisão da Média Histórica**
- **Crítica 3: Geração de Portfólios Não-Intuitivos e Altamente Concentrados**
- **Crítica 4: Ignorando Priors (Informações de Equilíbrio e Visões Subjetivas)**

- 
## Finanças Comportamentais (FC)
A FC desafia a premissa da racionalidade, explicando as anomalias de mercado por meio de vieses.

| Conceito Chave | Explicação | Implicações no Investimento |
| --- | --- | --- |
| Teoria da Perspectiva | A dor da perda é psicologicamente mais forte do que o prazer de um ganho equivalente (Aversão à Perda). | Leva à propensão ao risco no domínio das perdas (segurar ações perdedoras). |
| Viés de Ancoragem | Confiança excessiva no primeiro preço ou informação recebida (ex: preço de compra). | O investidor se recusa a vender uma ação que caiu porque está ancorado no preço original. |
| Excesso de Confiança | Superestimação da própria habilidade de obter retornos superiores. | Leva a alta rotatividade (negociar demais) e sub-diversificação. |


**Modelos Evoluídos e Fatores de Risco**
**Modelos Multifatoriais (Fama-****French****)**
O modelo FF3 estende o CAPM adicionando fatores de risco que explicam os retornos anômalos.

| Fator | Nome | Racional |
| --- | --- | --- |
| SMB | Small Minus Big (Tamanho) | Compensa o investidor pelo maior risco de liquidez e vulnerabilidade das empresas menores (small-caps). |
| HML | High Minus Low (Valor) | Compensa o investidor pelo risco de falência e sensibilidade a recessões das empresas de Valor (ações baratas). |


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
