# Relatório de Auditoria de Texto e Formatação (Fase P3)

**TCC:** Moderna Teoria das Carteiras no Mercado de Ações Brasileiro  
**Autor:** Pedro Augusto Pinheiro Reis | UFG — Ciências Contábeis  
**Data:** 2026-06-09  
**Auditor:** Gemini (Antigravity)  
**Status da Auditoria:** Concluída (Fase Read-Only)

---

## 1. Sumário Executivo

Este relatório apresenta os resultados da **Fase P3 (Auditoria do Texto)** da revisão da tese de TCC. O objetivo desta etapa é analisar o texto da tese em busca de inconsistências numéricas entre a prosa e as tabelas, desvios de formatação perante as normas da ABNT, problemas na estrutura ou numeração de elementos gráficos, e incoerências textuais.

Foram identificados **três grandes blocos de inconformidades**:
1.  **Matriz de Consistência Numérica:** Ocorrência universal de métricas defasadas no corpo do texto (como índices de Sharpe de `0,217` em vez de `0,293` para a Mínima Variância) que contradizem as tabelas definitivas geradas pelo pipeline corrigido. Adicionalmente, identificou-se **incoerência interna no texto**, onde o mesmo indicador é citado com o valor correto em um parágrafo e com o valor defasado em outro.
2.  **Descompasso Estrutural de Tabelas:** O sumário de tabelas apresenta um erro de vínculo do Microsoft Word (`Erro! Indicador não definido`) na Tabela 2 original. A sua exclusão no corpo físico gerou um descolamento de indexação que faz com que todas as tabelas a partir da Tabela 2 no texto estejam desalinhadas com o sumário e com as referências cruzadas.
3.  **Desvios das Normas ABNT NBR 10520:** Inconformidade generalizada no padrão de citações indiretas dentro de parênteses (uso de caixa baixa, separadores por vírgula em vez de ponto e vírgula e enumeração exaustiva de mais de 3 autores em vez do termo `et al.`).

---

## 2. Matriz de Consistência Numérica (Prosa vs. Tabelas)

A tabela abaixo cruza cada citação de valores estatísticos realizada no texto da tese (capítulos 4 e 5) com as tabelas definitivas presentes no próprio documento (Tabela 9 e 10 da extração de dados, correspondentes à Tabela 8 e 9 do texto corporal).

| Linha/Parágrafo | Estratégia / Métrica | Valor Citado na Prosa | Valor Real na Tabela | Impacto e Explicação | Ação Recomendada |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **L1237 (P1236)** | `MinVar` - Sharpe | **0,217** | **0,293** | **Grave Contradição:** O texto cita um Sharpe substancialmente pior do que o real obtido. | Substituir `0,217` por `0,293`. |
| **L1237 (P1236)** | `MinVar` - CAGR | **11,9%** | **13,00%** | **Grave Contradição:** O retorno real anualizado é 1,1 p.p. superior ao descrito no texto. | Substituir `11,9%` por `13,00%`. |
| **L1237 (P1236)** | `MinVar` - MaxDD | **−25,62%** | **−25,05%** | O rebaixamento máximo real é ligeiramente mais suave do que o citado. | Substituir `−25,62%` por `−25,05%`. |
| **L1237 (P1236)** | `MinVar` - Volatilidade | **12,96%** | **12,95%** | Micro-divergência flutuante decimal. | Substituir `12,96%` por `12,95%`. |
| **L1237 (P1236)** | `MinVar_c10` - Sharpe | **0,219** | **0,304** | **Grave Contradição:** O Sharpe real da versão com limite é muito superior ao citado. | Substituir `0,219` por `0,304`. |
| **L1237 (P1236)** | `MinVar_c10` - CAGR | **11,9%** | **13,17%** | Retorno real anualizado é 1,27 p.p. superior ao citado. | Substituir `aproximadamente 11,9% a.a.` por `13,17% a.a.`. |
| **L1237 (P1236)** | `MinVar_c10` - MaxDD | **−25,63%** | **−25,00%** | O rebaixamento máximo real é ligeiramente melhor. | Substituir `−25,63%` por `−25,00%`. |
| **L1237 (P1236)** | `MinVar_c10` - Vol. | **12,99%** | **12,98%** | Micro-divergência decimal. | Substituir `12,99%` por `12,98%`. |
| **L1238 (P1237)** | `MaxSharpe` - Sharpe | **0,287** | **0,305** | O Sharpe real do portfólio de máxima utilidade é superior. | Substituir `0,287` por `0,305`. |
| **L1238 (P1237)** | `MaxSharpe` - CAGR | **13,60%** | **13,96%** | O CAGR real é superior ao descrito. | Substituir `13,60%` por `13,96%`. |
| **L1238 (P1237)** | `MaxSharpe_c10` - Sharpe | **0,243** | **0,261** | O Sharpe real é superior. | Substituir `0,243` por `0,261`. |
| **L1238 (P1237)** | `MaxSharpe_c10` - CAGR | **12,66%** | **12,99%** | O CAGR real é superior. | Substituir `12,66%` por `12,99%`. |
| **L1264 (P1263)** | `MinVar` - Sharpe | **0,217** | **0,293** | Repetição do erro do Sharpe de Mínima Variância em outra seção comparativa. | Substituir `0,217` por `0,293`. |
| **L1265 (P1264)** | `EqualWeight` - Sharpe | **−0,075** | **0,290** | **Crítico/Erro Conceitual:** O texto afirma que a carteira 1/N destruiu valor e gerou Sharpe negativo de `−0,075`, mas a tabela mostra Sharpe positivo de `0,290`. A tese alega que ela perdeu para o IBOVESPA (`0,178`), o que é falso, pois ela superou o índice. | Substituir `(EqualWeight, Sharpe −0,075)` por `(EqualWeight, Sharpe 0,290)` e readequar a narrativa de que ela gerou retorno positivo e bateu o benchmark. |
| **L1265 (P1264)** | `MinCDaR` - Sharpe | **−0,417** | **−0,105** | O Sharpe real é substancialmente menos severo após a correção numérica. | Substituir `−0,417` por `−0,105`. |
| **L1291 (P1290)** | `MinCDaR` - CAGR | **−1,75%** | **5,36%** | **Crítico/Erro Conceitual:** O texto descreve perda real anualizada de capital (`−1,75%`), mas a otimização correta obteve retorno nominal positivo de `5,36%`. | Substituir `CAGR −1,75%` por `CAGR 5,36%`. |
| **L1291 (P1290)** | `MinCDaR` - MaxDD | **−81,81%** | **−62,46%** | O texto reporta um colapso catastrófico de `−81,81%` (fruto de instabilidade numérica corrigida), mas o real foi de `−62,46%`. | Substituir `drawdown −81,81%` por `drawdown −62,46%`. |
| **L1320 (P1319)** | `MinVar` - Sharpe | **0,217** | **0,293** | Repetição no Resumo/Conclusão. | Substituir `0,217` por `0,293`. |
| **L1320 (P1319)** | `MinVar` - Volatilidade | **12,96%** | **12,95%** | Repetição no Resumo/Conclusão. | Substituir `12,96%` por `12,95%`. |
| **L1320 (P1319)** | `MinVar` - MaxDD | **−25,62%** | **−25,05%** | Repetição no Resumo/Conclusão. | Substituir `−25,62%` por `−25,05%`. |

### 2.1. Incoerência Interna da Prosa (Autocorreção Incompleta)
Nota-se que em algumas passagens o texto cita os números corretos da tabela atualizada, revelando que o autor atualizou apenas parcialmente o texto durante a revisão, gerando trechos conflitantes na mesma tese:
*   **Caso MinCDaR:**
    *   *Linha 1245 (P1244) e Linha 1318 (P1317):* Cita corretamente: `CAGR de 5,36% a.a., Sharpe de −0,105 e drawdown máximo de −62,46%`.
    *   *Linha 1265 (P1264) e Linha 1291 (P1290):* Cita incorretamente: `Sharpe −0,417`, `CAGR −1,75%`, `drawdown −81,81%`.
*   **Caso EqualWeight (1/N rebalanceada):**
    *   *Linha 1318 (P1317):* Cita corretamente: `reduziu o retorno ajustado ao risco (Sharpe 0,290) quando submetida a rebalanceamentos...`.
    *   *Linha 1265 (P1264):* Cita incorretamente: `carteira 1/N rebalanceada (EqualWeight, Sharpe −0,075)`.

---

## 3. Descompasso e Erros de Vínculo de Tabelas

### 3.1. Erro de Vínculo de Referência Cruzada (Word Link Error)
Na página de pré-textuais (Lista de Tabelas - Linha 264), há um erro clássico de geração de índice do Microsoft Word:
> `P263: Tabela 2 - Axiomas da Teoria da Utilidade Esperada (VNM) Erro! Indicador não definido.`

Esse indicador quebrado indica que a tabela contendo os axiomas da Utilidade Esperada (VNM) foi removida do corpo do documento ou teve seu indicador alterado, mas o Sumário de Tabelas não foi atualizado antes da exportação. Como consequência, o sumário lista uma tabela que **não existe** no corpo do TCC.

### 3.2. Desalinhamento Sequencial de Numeração
Como a tabela de Axiomas VNM (que seria a Tabela 2) não existe no corpo, a numeração física das tabelas no corpo do texto e no sumário foi deslocada. O mapeamento do desalinhamento é detalhado a seguir:

| Tabela no Corpo Físico do TCC | Título Real da Tabela no Corpo | Número no Sumário de Tabelas (L263-273) | Título Listado no Sumário | Status de Conformidade |
| :--- | :--- | :---: | :--- | :--- |
| **Tabela 1** | CML vs. SML | **Tabela 1** | CML vs. SML | ✅ Alinhado |
| - *(inexistente)* | *(tabela de VNM foi excluída)* | **Tabela 2** | Axiomas VNM (`Erro!`) | ❌ **Quebrado** |
| **Tabela 2** | Fatores de risco (Fama-French) | - | *(não consta no sumário)* | ❌ **Desalinhado/Omitido** |
| **Tabela 3** | Vieses cognitivos | - | *(não consta no sumário)* | ❌ **Desalinhado/Omitido** |
| **Tabela 4** | MPT vs. PMPT | **Tabela 3** | MPT vs. PMPT | ❌ **Desalinhado (Shift de -1)** |
| **Tabela 5** | Resumo dos Indicadores | **Tabela 4** | Resumo dos Indicadores | ❌ **Desalinhado (Shift de -1)** |
| **Tabela 6** | Síntese dos Modelos | **Tabela 5** | Síntese dos Modelos | ❌ **Desalinhado (Shift de -1)** |
| **Tabela 7** | Quadro de Consolidação | **Tabela 6** | Quadro de Consolidação | ❌ **Desalinhado (Shift de -1)** |
| - *(inexistente)* | *(no corpo pula de Tabela 7 para 8)* | **Tabela 7** | - *(omitida no sumário)* | ❌ **Quebrado** |
| **Tabela 8** | Desempenho OOS (16 estratégias) | **Tabela 8** | Desempenho OOS | ✅ Re-alinhado (por exclusão dupla) |
| **Tabela 9** | Síntese Comparativa OOS | **Tabela 9** | Síntese Comparativa OOS | ✅ Alinhado |
| **Tabela 10** | Cronograma da Pesquisa | **Tabela 10** | Cronograma da Pesquisa | ✅ Alinhado |
| **Tabela 11** | A1 - Composição Setorial | **Tabela 11** | A1 - Composição Setorial | ✅ Alinhado |
| **Tabela 12** | Relação Completa dos Ativos | **Tabela 12** | Relação Completa dos Ativos | ✅ Alinhado |

*Nota: No arquivo bruto de extração automática (`tabelas_extraidas.txt`), o índice extrai tabelas de 0 a 13. A Tabela 0 e Tabela 1 extraídas correspondem a elementos vazios de layout ou bordas do Word, o que explica por que a Tabela 2 da extração representa a Tabela 1 física.*

**Ação Recomendada:**
1.  Remover definitivamente a linha que cita a "Tabela 2 - Axiomas VNM" da lista de tabelas.
2.  Adicionar a "Tabela 2 - Taxonomia dos fatores de risco" e a "Tabela 3 - Vieses cognitivos" à Lista de Tabelas.
3.  Atualizar as referências cruzadas das Tabelas 4, 5, 6 e 7 no corpo do documento para que fiquem alinhadas com o Sumário de Tabelas.

---

## 4. Desvios das Normas ABNT NBR 10520 (Citações)

De acordo com a norma reguladora de citações em documentos acadêmicos (ABNT NBR 10520), existem regras claras de representação de autoria. Foram encontrados desvios recorrentes que devem ser sanados no editor Word:

### 4.1. Uso Incorreto de Caixa Baixa Dentro de Parênteses
A norma prescreve que o sobrenome do autor, quando inserido dentro dos parênteses da citação, deve ser escrito em **letras maiúsculas (caixa alta)**. A tese faz o oposto em quase todas as ocorrências:
*   *Como está:* `(Williams, 1938)`, `(Markowitz, 1959)`, `(Tobin, 1958)`, `(Sharpe, 1966)`, `(Estrada, 2007)`.
*   *Como deveria ser:* `(WILLIAMS, 1938)`, `(MARKOWITZ, 1959)`, `(TOBIN, 1958)`, `(SHARPE, 1966)`, `(ESTRADA, 2007)`.

### 4.2. Uso de Vírgula para Separar Coautores
Para citações parentéticas com múltiplos coautores (2 ou 3 autores), os sobrenomes devem ser separados por **ponto e vírgula (`;`)**, e não por vírgula simples:
*   *Como está na L375:* `(Kim, Boyd, 2007)`
*   *Como deveria ser:* `(KIM; BOYD, 2007)`
*   *Como está na L472:* `(Fama, French, 2004)`
*   *Como deveria ser:* `(FAMA; FRENCH, 2004)`

### 4.3. Listagem Exaustiva de Mais de 3 Autores (Uso do *et al.*)
A norma ABNT NBR 10520 estabelece que em obras com mais de três autores, indica-se apenas o primeiro autor, seguido da expressão *et al.* em itálico:
*   *Como está na L327 e L333:* `(Boyd, Johansson, Kahn, Schiele, Schmelzer, 2024)`
*   *Como deveria ser:* `(BOYD *et al.*, 2024)`
*   *Como está na L354:* `(MARKOWITZ, Starer, Fram, Gerber, 2019 )`
*   *Como deveria ser:* `(MARKOWITZ *et al.*, 2019)`
*   *Como está na L402:* `(Markowitz, Starer, Fram, Gerber, 2019)`
*   *Como deveria ser:* `(MARKOWITZ *et al.*, 2019)`

### 4.4. Omissão de Ano de Publicação
*   *Como está na L483:* `(Boasson, Boasson, Zhou)`
*   *Como deveria ser:* Adicionar o ano correspondente da publicação: `(BOASSON; BOASSON; ZHOU, [ano])`.

---

## 5. Inconsistências Semânticas, Terminológicas e de Coesão

### 5.1. Typo e Erro de Nomenclatura de Base de Dados (COTAHIST vs. CODAHIST)
*   *Linha 1509 (P1509):* O texto menciona a base de dados de cotações históricas da B3 como `CODAHIST` (`...situações especiais (CODAHIST)...`).
*   *Correção:* O nome correto da base de dados oficial de cotações históricas da B3 é **COTAHIST**.

### 5.2. Erro de Digitação / Parêntese Aberto Incorretamente na Seção de Risco
*   *Linha 689 (P688):* O texto apresenta um erro de digitação contendo um parêntese aberto no meio da frase sem nexo:
    > `A escolha do grau ( permite ajustar a métrica à psicologia do investidor, ponderando a severidade das perdas de maneira distinta (Bawa, 1975; Fishburn, 1977):`
*   *Correção:* O termo correto deveria ser a variável matemática do grau $\alpha$ (ou $a$): `A escolha do grau \alpha permite ajustar a métrica...`.

### 5.3. Siglas Não Definidas em sua Primeira Aparição
As seguintes siglas e abreviações técnicas fundamentais são introduzidas no texto sem a respectiva definição ou por extenso na primeira ocorrência:
*   **ADTV** (Linha 1509): Deve ser definida como *Average Daily Trading Volume* (Volume Médio Diário de Negociação).
*   **MAR** (Linha 655): Deve ser definida como *Minimum Acceptable Return* (Retorno Mínimo Aceitável).
*   **CDaR** (Linha 291): Deve ser definida como *Conditional Drawdown at Risk*.

### 5.4. Uso Inconsistente de "Carteira" vs. "Portfólio"
A tese alterna frequentemente e de forma assistemática entre as palavras "carteira" e "portfólio" em frases adjacentes. Embora na prática financeira sejam sinônimos, recomenda-se uniformizar o uso preferencial da palavra **carteira**, que é o termo canônico em língua portuguesa adotado pelos manuais de contabilidade brasileiros, mantendo "portfólio" apenas para variações estilísticas pontuais.

---

## 6. Conclusões e Recomendações

O TCC apresenta uma excelente fundamentação matemática e um backtesting extremamente rigoroso de 16 estratégias que agora bate 100% com o código de produção otimizado na Fase P1-P2. No entanto, os descompassos textuais e de formatação detalhados neste relatório representam riscos perante a banca examinadora, pois indicam falta de cuidado na revisão final do manuscrito.

Recomenda-se fortemente que o autor adote as ações recomendadas neste documento diretamente no editor Word antes da submissão definitiva da tese.
