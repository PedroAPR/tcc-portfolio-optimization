# Prompt para Claude Code — Auditoria dos notebooks e relatório de atualização dos apêndices

> Cole o bloco abaixo no Claude Code, na raiz do repositório do TCC. Antes de colar, garanta que o `.docx` atual do TCC (ou ao menos os apêndices em texto) esteja acessível no repositório — de preferência em `docs/` — para que a reconciliação código ↔ documento seja feita. Se não houver, o Claude Code vai gerar os apêndices a partir do código.

---

## PROMPT (copiar a partir daqui)

**Papel e contexto**

Você é um engenheiro de pesquisa quantitativa auditando o repositório de um TCC de Ciências Contábeis intitulado *"Moderna Teoria das Carteiras no Mercado de Ações Brasileiro: Comparação entre Otimizadores e Inputs"*. O pipeline computacional está distribuído em notebooks Jupyter (`.ipynb`) e, possivelmente, módulos `.py` auxiliares. Todos os notebooks foram escritos seguindo o framework **"Ten Simple Rules for Writing and Sharing Computational Analyses in Jupyter Notebooks" (Rule et al., 2019, PLOS Comput Biol 15(7):e1007007)** — ou seja, cada notebook deve contar uma história, documentar o processo, dividir etapas em células, registrar dependências e funcionar como registro do pipeline.

O documento escrito (capítulo de Metodologia e **Apêndices A–J**) descreve esse pipeline em prosa, mas **divergiu do código** ao longo do desenvolvimento. Sua tarefa é produzir um **relatório de atualização dos apêndices** que reconcilie o que o código *de fato faz hoje* com o que os apêndices *afirmam*.

**Não execute treinamentos pesados nem reprocessamentos longos.** Extraia os valores lendo (a) o código-fonte e (b) artefatos já salvos (CSV/parquet/pickle/figuras/logs). Se um valor só puder ser obtido executando uma célula barata e determinística, você pode rodá-la; mas se exigir reprocessar a base inteira ou re-treinar a LSTM, **não rode** — marque o valor como `[NÃO VERIFICADO — requer execução]`. Trate o repositório como leitura; não altere notebooks nem dados.

---

**Etapa 1 — Inventário do pipeline**

Liste todos os `.ipynb` e `.py` relevantes. Para cada notebook, em ordem de execução do pipeline, registre:
- caminho e nome do arquivo;
- a **história/objetivo** declarado (Regra 1) — extraia do título e das células markdown de abertura;
- **entradas** (arquivos/variáveis lidos) e **saídas** (arquivos/variáveis gravados) — Regra 8 e Regra 7;
- **dependências** (imports, versões em `requirements.txt`/`environment.yml`/`pip freeze` se houver) — Regra 5;
- a **posição no pipeline** (de qual notebook recebe dados, para qual entrega) — Regra 7;
- uma avaliação curta de aderência às Ten Simple Rules (sobretudo Regra 2 — processo documentado, e Regra 9 — executável de ponta a ponta sem estado oculto). Aponte estados ocultos, ordem de execução não-linear, ou caminhos hard-coded que quebrem reprodutibilidade.

---

**Etapa 2 — Extração dos parâmetros canônicos (a "fonte da verdade" é o código)**

Localize no código os valores efetivos dos parâmetros abaixo. Para cada um, registre **valor encontrado + arquivo:linha** onde aparece. Se houver mais de um valor no repositório, liste todos e sinalize o conflito.

- **Universo e janela:** N de ativos no universo investável final; intervalo de datas; nº total de pregões (antes e depois da limpeza); primeiro pregão exigido.
- **Filtro de liquidez:** limiar de presença em pregões (ex.: 95%); critério de ADTV (decil inferior P10?) e a janela em que o ADTV é medido.
- **Limpeza/anomalias:** multiplicador do IQR (ex.: 3,0); método de imputação (interpolação linear temporal, ffill/bfill); tratamento de preços negativos.
- **Retornos:** definição de retorno simples e log; fator de anualização (252?); proxy de taxa livre de risco (CDI diário); valor médio do CDI no período.
- **Covariância:** estimador (amostral? Ledoit-Wolf shrinkage?); fator de anualização da Σ (×252 ou ×21? — verifique especificamente o que é usado **no BL**).
- **Otimização:** conjunto de restrições (long-only, soma=1, teto por emissor); valor do teto (`c10` = 10%?); **custo de transação / penalidade L1** (c = 0,5%? 0,2%?); solvers (SLSQP, CLARABEL/ECOS/SCS).
- **PMPT:** MAR (τ); nível de confiança do CVaR/CDaR (95%?); ordens dos LPM usadas (Sortino n=2, Kappa n=3, Omega n=1).
- **Black-Litterman:** como as **visões (Q)** são geradas — *momentum* 12-1, **LSTM**, ARIMA, ou outro?; matriz P; construção de Ω; valor de τ (0,05?); valor de δ (2,5 fixo? otimização reversa? deu negativo?); **portfólio de referência do prior** (equiponderado 1/N **ou** capitalização de mercado? e de qual data?).
- **LSTM (se existir no código):** arquitetura (camadas, unidades), janela de lookback, horizonte de previsão, função de perda, otimizador, épocas, regularização/dropout, esquema de validação, e como o output vira o vetor Q.
- **Backtest:** data de início do out-of-sample por estratégia; período mínimo de formação (60 meses?); nº de rebalanceamentos (132?); frequência (mensal); como benchmarks (IBOV, CDI) são alinhados.
- **Resultados por estratégia:** para cada estratégia efetivamente rodada, os valores de Retorno Acumulado, CAGR, Volatilidade anualizada, Sharpe, Sortino, Max Drawdown e Turnover médio — **lidos dos artefatos de saída**. Liste quais estratégias têm resultados completos e quais têm métricas faltando.

---

**Etapa 3 — Mapeamento apêndice ↔ notebook**

Associe cada apêndice ao(s) notebook(s) que o implementa(m). Use este mapeamento esperado como ponto de partida e corrija conforme o repositório real:

| Apêndice | Conteúdo declarado | Notebook(s) provável(is) |
|---|---|---|
| A | Universo investável (N), filtro de liquidez ADTV, presença ≥95%, lista nominal e composição setorial | pipeline de seleção/universo |
| B | Higienização: IQR 3,0, imputação, preços negativos | `4_1_Pipeline_Dados` ou equivalente |
| C | Transformação em retornos simples e log | pipeline de retornos |
| D | Base mestre, merge de CDI/SELIC/IBOV, truncamento 31/12/2025, look-ahead | consolidação |
| E | Prêmio de risco / retornos em excesso | excess returns |
| F | Covariância anualizada, Beta, Sharpe analítico | parâmetros inferenciais |
| G | Fronteira eficiente (Monte Carlo 50.000 + SLSQP) | fronteira |
| H | Covariâncias negativas / hedge (heatmap) | covariância negativa |
| I | Correlação de Pearson + clusterização hierárquica (Ward, euclidiana) | correlação/clusters |
| J | Engenharia reversa BL: extração do Π | black-litterman |

Para cada apêndice, indique se o notebook correspondente **existe, está completo e roda**, ou se a descrição do apêndice não tem implementação correspondente (apêndice "órfão") — e vice-versa (notebook sem apêndice).

---

**Etapa 4 — Verificação dirigida de discrepâncias conhecidas**

Estas inconsistências já foram detectadas no texto. **Confirme contra o código qual é o valor correto** e reporte cada uma com veredito (`CÓDIGO confirma X` / `TEXTO está errado` / `ambíguo`):

1. **N do universo:** o texto cita 118, 120, 130, 135 e 136 em pontos diferentes. Os "8.385 pares de covariância" do texto correspondem a C(130,2)=8.385, sugerindo que parte do código rodou com 130, não 118. Determine o N efetivo do código e quantos pares ele gera.
2. **Visões do BL:** a metodologia descreve visões por *momentum* 12-1, mas a tabela de resultados rotula "BL + LSTM". Verifique o que o código realmente usa para gerar Q.
3. **Métricas faltantes:** Sharpe, Volatilidade e Max Drawdown das estratégias Mínima Variância L1 e Máximo Sharpe L1 estão em branco no texto ("a completar com notebooks 14_1_4 e 14_2_4"). Localize esses valores nos artefatos e reporte-os, ou marque como ausentes se os notebooks não os gravaram.
4. **Prior do BL:** equiponderado 1/N (como diz a metodologia) ou capitalização de mercado de mai/2026 (como diz a seção de limitações)? Verifique no código.
5. **Penalidade L1:** c = 0,5% (metodologia) ou 0,2% (análise de resultados)?
6. **Nº de pregões:** 3.967 (metodologia/resultados) ou 4.030 (Apêndice B)?
7. **Escala da Σ no BL:** anualizada ×252 ou mensalizada ×21? (a seção de limitações afirma que foi ×21 por engano).
8. **δ do CAPM reverso:** confirme se a otimização reversa produz δ negativo e se o código substitui por 2,5.
9. **Datas de início do OOS:** confirme se as estratégias L1 começam em data diferente do BL+LSTM (set/2015 vs jan/2015), o que desalinha os benchmarks.
10. **Tickers:** verifique se "GOLL54" e "RCSL4" são os códigos efetivamente usados (GOLL4 é o esperado para a Gol).
11. **ARIMA:** o resumo/introdução citam ARIMA como método de input. Existe implementação de ARIMA no código? Se não, confirme que deve ser removido das menções.

---

**Etapa 5 — Saída: o relatório**

Gere um único arquivo markdown em `docs/RELATORIO_ATUALIZACAO_APENDICES.md` com:

1. **Sumário executivo** (1 página): estado do pipeline, principais divergências código↔texto e o que exige uma execução para ser fechado.
2. **Tabela-mestre de parâmetros canônicos** (parâmetro · valor no código · arquivo:linha · valor atualmente no texto · status). Esta tabela é a referência única de verdade para revisar o documento inteiro.
3. **Tabela de veredito das 11 discrepâncias** da Etapa 4.
4. **Bloco por apêndice (A–J):** para cada um —
   - *O que o notebook faz hoje* (resumo fiel ao código, com a "história" no espírito da Regra 1/2);
   - *O que o apêndice afirma hoje* (se o texto estiver disponível);
   - *Texto de atualização sugerido*, em prosa pronta para colar no apêndice, com os números corretos e coerentes com a tabela-mestre. Use português acadêmico no mesmo registro do TCC. Não invente valores: todo número vem do código/artefato, e o que faltar fica explicitamente marcado como pendente de execução.
5. **Lista de pendências de execução:** o que precisa ser rodado (e qual notebook/célula) para fechar os valores ainda ausentes — em especial as métricas de risco da Etapa 4, item 3.
6. **Aderência às Ten Simple Rules:** notebooks que violam reprodutibilidade (estado oculto, ordem não-linear, caminhos absolutos, dependências não fixadas) e o ajuste mínimo para sustentar a alegação de "reprodutibilidade algorítmica" feita nos apêndices.

**Regras de redação do relatório:** seja específico e rastreável (sempre `arquivo:linha` ou nome do artefato). Não corrija o código nem o documento agora — apenas relate e proponha. Marque claramente toda inferência incerta. Não reproduza blocos longos de código no relatório; cite trechos curtos só quando necessário para evidenciar um valor.

## FIM DO PROMPT
