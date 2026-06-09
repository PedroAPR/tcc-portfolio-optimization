# Relatório de Diagnóstico — TCC "Moderna Teoria das Carteiras no Mercado de Ações Brasileiro"

**Autor:** Pedro Augusto Pinheiro Reis · **Orientador:** Prof. Dr. Moisés Ferreira da Cunha · **UFG — Ciências Contábeis**
**Objeto da revisão:** versão "Entrega 12" · **Foco:** estado atual e adequações necessárias

---

## 1. Avaliação geral

O trabalho tem uma base teórica sólida e ambiciosa: percorre de forma competente a trajetória MPT → CAPM → PMPT → Black-Litterman, com derivações matemáticas, axiomas VNM, momentos parciais inferiores e medidas coerentes de risco. O desenho empírico (backtesting com janela expansiva, vedação ao *look-ahead*, penalidade L1, estimador de Ledoit-Wolf) é metodologicamente maduro para um TCC de graduação.

O problema central **não é de qualidade teórica, e sim de consistência interna e de fechamento empírico**. Há um descasamento sério entre o que o trabalho *promete* (resumo, introdução, metodologia) e o que *entrega* (capítulo de resultados), além de inconsistências numéricas que se repetem em várias seções. Nada disso é fatal, mas precisa ser resolvido antes da entrega — a banca de Contábeis com perfil quantitativo (e o próprio orientador) baterá exatamente nesses pontos.

Abaixo, os achados estão ordenados por severidade. Cada item indica **onde** está o problema para localização rápida.

---

## 2. Problemas CRÍTICOS (comprometem a validade ou serão questionados em arguição)

### C1 — O tamanho da amostra (N) muda ao longo do texto

O número de ativos é citado com **cinco valores diferentes**:

| Valor | Onde aparece |
|---|---|
| **118** | Metodologia §3.2.1 ("amostra final de 118 ativos"); Resultados §4.1.1; BL ("N = 118"); Apêndice A (lista nominal de 118) |
| **120** | Metodologia §3.5.1 ("eficiente para N ≤ 120") |
| **130** | Tabelas 5 e 6 (títulos); textos "130/130 ativos"; "8.385 pares" |
| **135** | Metodologia §3.4.2 ("matriz 135×135"); título da Tabela 7; Conclusão §5.1 ("135 ações") |
| **136** | Apêndice B ("reteve 136 ativos") |

Confirmei numericamente: os **"8.385 cruzamentos possíveis"** citados em §4.1.4 correspondem exatamente a C(130,2) = 8.385 — ou seja, esse trecho foi rodado com **130** ativos, não 118. Para 118 ativos seriam 6.903 pares; para 135, 9.045.

**Ação:** definir o N final (o Apêndice A sustenta **118** com lista nominal). Depois, **propagar 118 em todo o documento, em todo o código e em todos os apêndices**, e **recalcular** tudo que dependa de N: "130/130" dos testes econométricos → "118/118"; "8.385 pares" → "6.903"; dimensão da matriz "135×135" → "118×118". Esta é a correção mais visível e mais danosa se passar.

### C2 — A família PMPT inteira não tem resultados

O título do trabalho, o resumo e a metodologia (§3.5, Família II) formalizam cinco estratégias PMPT — **MaxOmega, MaxSortino, MaxKappa3, MinCVaR, MinCDaR** — que são um dos três pilares anunciados (PMPT está literalmente no título). O Quadro de Consolidação lista **15 modelos**.

Mas o Capítulo 4 reporta **apenas 3 estratégias** (Mínima Variância L1, Máximo Sharpe L1, BL+LSTM) mais o benchmark 1/N. **Nenhum** resultado de Sortino, Omega, Kappa, CVaR ou CDaR aparece. Também não há resultados separados para EqualWeight, InvVol, MinVar_c10, MaxSharpe_c10 nem para 3 das 4 variantes BL.

Isto é a maior lacuna do trabalho: metade do aparato teórico-metodológico — incluindo o pilar que dá nome à pesquisa — **não é testada empiricamente**. Há duas saídas legítimas:

- **(a) Rodar e reportar** ao menos as cinco estratégias PMPT (caminho que honra o título e o resumo); ou
- **(b) Reduzir o escopo declarado**: ajustar título, resumo, introdução, objetivos e metodologia para refletir que o estudo compara especificamente MinVar, MaxSharpe e BL+LSTM — eliminando a promessa de PMPT que não foi cumprida.

A opção (a) é claramente superior para o mérito do trabalho, mas exige tempo de execução. A (b) é a contenção de dano se o prazo for curto. **O que não pode acontecer é o documento prometer PMPT no título e não trazer um único número de PMPT nos resultados.**

### C3 — Descasamento metodologia × resultados no Black-Litterman: momentum vs. LSTM

A metodologia (§3.5.3 / Família III) descreve as visões do BL como geradas pelo **fator de *momentum* 12-1** ("As visões são absolutas e geradas pelo fator de momentum 12-1... o vetor de visões Q contém os retornos previstos por momentum"). **Não há descrição da rede LSTM no corpo do texto.** A seção "3.5.3 — Modelo Black-Litterman com Visões LSTM" consta no sumário, mas o conteúdo correspondente formaliza visões por momentum.

Já os resultados (Tabela 10) reportam **"Black-Litterman + LSTM"**, e a análise das causas (§4.3.3) e a conclusão discutem extensamente o "fracasso da LSTM".

Ou seja: o resultado central sobre os "limites do *machine learning* em finanças" repousa sobre um modelo (LSTM) cuja **arquitetura, janela de treino, número de camadas/unidades, função de perda, regularização, esquema de validação e hiperparâmetros estão completamente ausentes**. Sem isso, o achado não é reproduzível nem defensável.

**Ação:** decidir o que o BL de fato usou. Se foi LSTM, escrever uma subseção metodológica completa da LSTM (item obrigatório). Se foram visões de *momentum*, então a Tabela 10 e toda a narrativa de "fracasso do ML" precisam ser reescritas. As duas versões coexistindo no mesmo documento é o ponto mais frágil para a arguição.

### C4 — As métricas de risco das duas melhores estratégias estão em branco

Nas Tabelas 8 (MinVar L1) e 9 (MaxSharpe L1), as células de **Volatilidade Anualizada, Índice de Sharpe e Maximum Drawdown** estão vazias ("-", com nota "a completar com os outputs do notebook 14_2_4 / 14_1_4"). As Tabelas 11 e 12 repetem "a completar".

O trabalho **afirma** a superioridade "ajustada ao risco" da Mínima Variância, mas **não apresenta o Sharpe nem o MDD dela**. A afirmação central fica sem suporte numérico. Enquanto essas células não forem preenchidas, a tese ("a estratégia mais simples vence inclusive em base ajustada ao risco") está apenas parcialmente demonstrada — só com retorno acumulado e CAGR.

**Ação:** preencher as células com os *outputs* dos notebooks 14_1_4 e 14_2_4 e refletir nas Tabelas 11 e 12. Sem isso, a conclusão usa um adjetivo ("ajustado ao risco") que os dados ainda não sustentam.

### C5 — Contradição direta sobre o portfólio de referência do *prior* do BL

- **Metodologia (Família III):** "adota-se um portfólio de referência estritamente **equiponderado** (1/N)... para eliminar qualquer viés de antecipação no vetor de pesos".
- **Limitação 1 (§5.4):** "Os pesos de mercado utilizados no cálculo do *prior* foram obtidos com as **capitalizações de mercado vigentes em maio de 2026**... introduz um viés de antecipação no *prior*."

As duas afirmações são mutuamente exclusivas: ou o *prior* usou 1/N (sem look-ahead) ou usou capitalizações de mai/2026 (com look-ahead). **Ação:** verificar no código qual foi efetivamente usado e alinhar metodologia e limitações. Se foi 1/N, a Limitação 1 deve ser removida; se foram capitalizações, a metodologia está incorreta.

---

## 3. Problemas de ALTO impacto (inconsistências numéricas e factuais)

### A1 — Penalidade L1 / custo de transação com dois valores
Metodologia §3.5.1: **c = 0,5%** (Φ(w) com c = 0,005). Mas §4.3.3 e Limitação 3 falam em **"penalidade L1 de 0,2%"**. Definir o valor real e padronizar.

### A2 — Número de pregões inconsistente
Metodologia §3.2: **3.967 pregões**. Apêndice B: **4.030 pregões contínuos**. Resultados §4.1.1: **3.967 observações**. Conciliar (provavelmente 4.030 antes da limpeza e 3.967 depois — se for isso, deixar explícito).

### A3 — Período OOS com datas de início divergentes
As estratégias L1 começam em **set/2015**; o BL+LSTM começa em **jan/2015**; e "132 pontos mensais" pressupõe início em jan/2015. A própria Limitação 4 reconhece que a comparação direta está "prejudicada". **Padronizar a data de início é pré-requisito** para que a Tabela 11 (comparação unificada) seja válida — hoje ela compara estratégias em janelas diferentes.

### A4 — IBOVESPA e CDI com três valores distintos
Decorre de A3, mas aparece como erro numérico aos olhos do leitor:

| Fonte | IBOVESPA | CDI |
|---|---|---|
| Tabela 8 / 9 | +215,00% | +166,14% |
| Tabela 10 | +243,49% | +171,10% |
| Tabela 11 | +232%* | +174%* |

O mesmo benchmark, no mesmo período nominal, não pode ter três retornos acumulados. Resolver A3 e unificar.

### A5 — Sinais e unidades em índices adimensionais
Tabela 10: Sharpe "**-0,14%**" e Sortino "**-0,15%**" estão com símbolo de porcentagem — Sharpe e Sortino são adimensionais (devem ser -0,14 e -0,15, sem "%"). A volatilidade "+38,56%" não precisa do sinal "+". Padronizar em todas as tabelas.

### A6 — Tickers possivelmente inválidos
"**GOLL54**" aparece em §4.1.4 e no Apêndice A (linha 46) — o código da Gol é **GOLL4**. O par de covariância negativa "RCSL4 e GOLL54" depende de tickers corretos; verificar ambos na base da B3/Economática.

---

## 4. Problemas de MÉDIO impacto (estrutura, títulos, formatação)

### M1 — Títulos duplicados/errados no Capítulo 4
- §4.2.2 e §4.2.3 têm **o mesmo título** ("Estratégia 2 — Máximo Índice de Sharpe com L1"). O §4.2.3 deveria ser **"Estratégia 3 — Black-Litterman + LSTM"**.
- §4.4 está intitulada apenas **"l"** (placeholder). O conteúdo é a análise do benchmark 1/N → renomear para algo como **"Análise do Benchmark 1/N"**.
- §4.1.1 está intitulada **"Modelo Black-Litterman com Visões LSTM"**, mas o conteúdo é a caracterização setorial da amostra → corrigir o título (ex.: "Caracterização da Amostra Final").
- Cabeçalho de §4.2 está colado: "Resultados do Backtest Out-of-Sample (2015–2025)**Caracterização da Amostra Final**" — separar.

### M2 — Equações ausentes ou não exibidas
Várias fórmulas centrais não aparecem no corpo (podem ser objetos de equação que não foram inseridos, ou que se perderam):
- §3.3.2: as fórmulas de **retornos simples** e **log-retornos** são anunciadas ("calculados como...") mas não exibidas.
- §3.4.1: o prêmio de risco de mercado "foi calculado como **.**" — a fórmula está literalmente faltando.
- §3.4.2: as expressões de **μ anualizado** e **Σ anualizada** estão descritas em texto, sem a equação.

**Ação:** abrir o `.docx` no Word e conferir cada equation object; inserir as que faltam.

### M3 — Numeração de tabelas inconsistente
Convivem três sistemas: sequencial (Tabela 1…15), por capítulo ("Tabela 4.1", "Tabela 4.3") e até **em inglês** ("**Table** 1 - Quadro de Consolidação dos 15 modelos"). Há ainda **duas "Tabela 1"** (a CML/SML no referencial e o Quadro dos 15 modelos). A "Tabela 2 — Axiomas VNM" não consta na Lista de Tabelas. Padronizar todo o esquema de numeração e atualizar a Lista de Tabelas.

### M4 — Sumário desatualizado
O sumário reflete os títulos errados (4.2.3 duplicado, 4.4 = "l", 4.1.1 = LSTM). Regerar o sumário **por último**, depois de corrigir os títulos.

### M5 — ARIMA prometido e não usado
Resumo e Introdução citam "modelos **ARIMA**" como um dos métodos de estimação de inputs. ARIMA não aparece na metodologia nem nos resultados. **Remover** das menções ou **implementar** — coerência entre objetivos e execução.

---

## 5. Problemas de BAIXO impacto (refinamento e precisão acadêmica)

- **B1 — Epígrafe:** "Jim Simons – Criador da Análise Quantitativa" é impreciso (Simons foi pioneiro do *investimento quantitativo*, não o criador da análise quantitativa, que o antecede). Suavizar a atribuição e, idealmente, citar a fonte da frase.
- **B2 — Resumo desatualizado:** descreve o desenho, mas não traz o achado central (o "paradoxo da complexidade" / a vitória da MinVar). Um resumo de TCC deve sintetizar **resultado e conclusão**. Reescrever depois de consolidar os números.
- **B3 — Auditoria de citações × referências:** o texto usa autor-data e cita várias obras **sem entrada na lista de Referências** — p.ex. Michaud (1989), Estrada (2007/2008), Tobin (1958), Mossin, Treynor, Keating & Shadwick (2002), Kaplan & Knowles (2004), Artzner et al. (1999), Idzorek (2005), Meucci, Mandelbrot (1963), Williams, Graham & Dodd, Guerard (2010), Rubinstein (2002), Gundersen (2022), Kim & Boyd (2007). Além disso, Rockafellar & Uryasev é citado como **(2000)** no texto e listado como **2002** nas Referências; e o texto cita "Sortino & Van der Meer (1991)", mas a lista traz "Sortino & Price (1994)". Fazer auditoria completa: toda citação no corpo precisa de entrada nas Referências, e vice-versa.
- **B4 — Apêndices C–J** formalizam etapas (fronteira de Markowitz por Monte Carlo com 50.000 carteiras, *heatmap* de covariâncias negativas, clusterização hierárquica) que **não reaparecem nos resultados**. Conectá-las ao corpo ou sinalizar claramente que são material de apoio.
- **B5 — Cronograma (Tabela 13):** tem **duas linhas numeradas "10"** e cobre Março–Julho com cara de cronograma de *projeto*, não de TCC concluído. Revisar a coerência com a fase atual.

---

## 6. Checklist priorizado de ações

**Antes de qualquer coisa (bloqueiam a validade):**
1. [ ] Fixar **N = 118** e propagar em texto, código e apêndices; recalcular "130/130", "8.385 pares", "135×135". *(C1)*
2. [ ] Decidir e documentar: BL com **LSTM** (escrever a metodologia da rede) **ou** com *momentum* (reescrever Tabela 10 e narrativa). *(C3)*
3. [ ] Preencher **Sharpe, Volatilidade e MDD** de MinVar e MaxSharpe (notebooks 14_1_4 e 14_2_4). *(C4)*
4. [ ] Resolver a contradição do *prior* do BL (1/N vs. capitalização mai/2026). *(C5)*
5. [ ] Decidir: **rodar a família PMPT** (Sortino/Omega/Kappa/CVaR/CDaR) **ou** reduzir o escopo declarado no título/resumo/objetivos. *(C2)*

**Em seguida (consistência numérica):**
6. [ ] **Padronizar a data de início do OOS** e refazer a Tabela 11; unificar IBOV/CDI. *(A3, A4)*
7. [ ] Definir o valor real da penalidade L1 (0,2% ou 0,5%). *(A1)*
8. [ ] Conciliar nº de pregões (3.967 vs. 4.030). *(A2)*
9. [ ] Corrigir unidades de Sharpe/Sortino e tickers (GOLL4). *(A5, A6)*

**Por fim (forma):**
10. [ ] Corrigir títulos de §4.1.1, §4.2.2/4.2.3, §4.4 e o cabeçalho de §4.2. *(M1)*
11. [ ] Inserir equações faltantes (§3.3.2, §3.4.1, §3.4.2). *(M2)*
12. [ ] Padronizar numeração de tabelas e atualizar a Lista de Tabelas. *(M3)*
13. [ ] Auditar citações × referências. *(B3)*
14. [ ] Reescrever o **Resumo** com o achado central e **regerar o Sumário**. *(B2, M4)*
15. [ ] Resolver ARIMA, epígrafe, apêndices órfãos e cronograma. *(M5, B1, B4, B5)*

---

## 7. Comentário final

O esqueleto teórico e o desenho de *backtesting* são o ponto forte e estão acima da média de um TCC. O risco real está na **distância entre o que o documento promete e o que demonstra**, e nas **inconsistências numéricas que se repetem** (sobretudo o N e os benchmarks). Os itens C1–C5 são os que um arguidor experiente identifica em minutos; resolvidos esses cinco, o trabalho passa de "frágil sob escrutínio" para "consistente e defensável". A decisão estratégica mais importante é a do item C2/PMPT: vale muito a pena rodar a família PMPT se houver tempo, porque é o que entrega de fato a comparação tripla (MPT × PMPT × BL) anunciada no título.
