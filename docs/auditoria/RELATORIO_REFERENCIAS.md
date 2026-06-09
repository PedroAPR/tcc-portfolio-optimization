# Relatório de Auditoria — Referências e Originalidade (Fase P4)

**Objetivo:** Identificar e documentar desvios nas citações no corpo do texto do TCC e na lista de referências bibliográficas finais com base nas normas ABNT NBR 10520 e NBR 6023, além de realizar a higiene de originalidade acadêmica.

---

## 1. Reconciliação Citação ↔ Referência

Esta seção apresenta o cruzamento entre as obras citadas no texto (`docs/auditoria/Entrega_12_Pedro_Reis_07062026_1500_corrigido.txt`) e a lista final de referências bibliográficas.

### 1.1. Citações Órfãs (Citadas no corpo, mas ausentes na bibliografia)

Foram identificadas **21 ocorrências** de citações na prosa que não possuem correspondência na lista de referências. Vários destes nomes são fundamentais para o arcabouço do CAPM, PMPT e calibração de Black-Litterman:

| Citação Identificada | Exemplo de Ocorrência (Parágrafo) | Contexto e Impacto Teórico |
| :--- | :--- | :--- |
| **Litterman (1992)** | `P289` | Co-criador do modelo Black-Litterman. Falta a referência clássica de 1992. |
| **Lintner (1965)** | `P469` | Co-desenvolvedor do CAPM clássico. |
| **Treynor (1962)** | `P469` | Co-desenvolvedor do CAPM clássico. |
| **Scholes (1973)** | `P800` | Co-criador do modelo Black-Scholes para opções. |
| **Best e Grauer (1991)** | `P809` | Críticos fundamentais da instabilidade de inputs de Markowitz. |
| **Satchell e Scowcroft (2000)** | `P914` | Autores clássicos sobre a calibração do escalar $\tau=1$ no Black-Litterman. |
| **Iglewicz e Hoaglin (1993)** | `P1006` | Autores do método Z-score modificado por MAD utilizado na filtragem de anomalias. |
| **Ross, Westerfield, Jordan (2010)**| `P475` | Manual clássico de Finanças Corporativas usado para justificar decomposição de risco. |
| **Boyd, Johansson et al. (2024)** | `P326` | Ocorrência no histórico de Value Investing. |
| **Hicks (1939)** | `P332` | Histórico de formação de portfólios. |
| **Marschak (1938)** | `P332` | Histórico de formação de portfólios. |
| **Estrada (2007)** | `P352` | Referência sobre a origem da semivariância. |
| **Hebner (2022)** | `P381` | Utilizado para fundamentar a correlação de diversificação. |
| **Gundersen (2022)** | `P398` | Fronteira eficiente com vendas a descoberto. |
| **Qi (2019)** | `P400` | Explicação de "corner portfolios" (portfólios de canto). |
| **Garvin (2013)** | `P470` | Menção ao Prêmio Nobel de 1990 de Markowitz, Sharpe e Miller. |
| **Nawrocki (1999)** | `P614` | Crítica à simetria da variância. |
| **Guerard (2010)** | `P325` | Rigor matemático na avaliação de equities. |
| **Holton (2025)** | `P420` | Tomada de empréstimo livre de risco e alavancagem. |
| **Dubra; Maccheroni (2004)** | `P461` | Crítica e limitações do Índice de Sharpe sob não-normalidade. |
| **Garlappi e Uppal (2009)** | `P1084` | Co-autores do benchmark global 1/N contra otimizadores (DeMiguel et al., 2009). |

### 1.2. Referências Fantasmas (Listadas na bibliografia, mas nunca citadas)

Foram identificadas **22 obras** listadas na seção de referências bibliográficas que não possuem qualquer citação correspondente no corpo do texto. Destacam-se vários trabalhos de redes neurais LSTM que foram descartados no setup final do projeto:

| Chave na Bibliografia | Entrada Bibliográfica Afetada | Motivo da Inconsistência / Origem |
| :--- | :--- | :--- |
| **BACHELIER (1900)** | `BACHELIER, Louis. Théorie de la spéculation...` | Obra histórica não citada no texto. |
| **BOLLERSLEV (1986)** | `BOLLERSLEV, Tim. Generalized autoregressive...` | Modelagem GARCH não aplicada diretamente na branch final. |
| **HOCHREITER (1997)** | `HOCHREITER, Sepp; SCHMIDHUBER, Jürgen. Long...` | Algoritmo LSTM abortado do escopo. |
| **YILMAZ (2023)** | `YILMAZ, Tuncay et al. Investment portfolio...` | Artigo sobre LSTM e RNN não utilizado. |
| **BARBER (2001)** | `BARBER, Brad M. Boys will be boys...` | Finanças Comportamentais (mencionada apenas em tabelas de anexo). |
| **THALER (1999)** | `THALER, Richard H. Mental accounting matters...` | Finanças Comportamentais (mencionada apenas em tabelas de anexo). |
| **NOFSINGER (1999)** | `NOFSINGER, John R. Herding and feedback trading...`| Finanças Comportamentais (mencionada apenas em tabelas de anexo). |
| **CHIAN (2008)** | `CHIAN, Swee C. Evolutionary multi-objective...` | Otimização evolucionária multi-objetivo não aplicada. |
| **DEMIGUEL (2009)** | `DEMIGUEL, Victor. Portfolio selection with robust...`| Otimização robusta de parâmetros (só citou DeMiguel 2009a). |
| **ELTON (1997)** | `ELTON, Edwin J. Modern portfolio theory, 1950...` | Revisão de MPT não citada. |
| **FABOZZI (2011)** | `FABOZZI, Frank J. The theory and practice of...` | Manual clássico não citado. |
| **KONNO (1991)** | `KONNO, Hiroshi. Mean-absolute deviation...` | Otimização MAD de Konno-Yamazaki não utilizada. |
| **PELSSER (1996)** | `PELSSER, Antoon. Transaction costs and efficiency...`| Fricção de transação não citada com esta fonte. |
| **REILLY (2011)** | `REILLY, Frank K. Investment analysis...` | Manual clássico não citado. |
| **ROLL (1977)** | `ROLL, Richard. A critique of the asset pricing...` | Crítica de Roll ao CAPM. |
| **RONCALLI (2025)** | `RONCALLI, Thierry. Risk Factor, Risk Premium...` | Notas de aula/livro sobre BL não citadas. |
| **TVERSKY (1974)** | `TVERSKY, Amos. Judgment under uncertainty...` | Finanças Comportamentais clássica (mencionada apenas em anexo). |
| **VERNIMMEN (2014)** | `VERNIMMEN, Pierre et al. Corporate finance...` | Finanças corporativas não citado. |
| **LUND UNIVERSITY (2025)** | `LUND UNIVERSITY. The Black-Litterman Model...` | Duplicata indesejada (Lund University). |
| **UNIVERSIDADE DE LUND (2025)**| `UNIVERSIDADE DE LUND. Testing...` | Duplicata indesejada (Lund University). |
| **PIRES (2021)** | `PIRES, Arthur Martinez. Impactos da Crise Hídrica...`| TCC anterior não citado na prosa. |
| **MORGAN (1996)** | `MORGAN, J. P. RiskMetrics: technical document...` | Fusão física com Meucci (detalhes na Seção 2). |

---

## 2. Inconformidades Críticas de Estilo ABNT NBR 6023 (Bibliografia)

Identificaram-se quatro defeitos severos de formatação e integridade acadêmica na lista de referências finais:

1.  **Erro de Fusão/Concatenação Física (Linhas Coladas):**
    *   **Evidência (`P1432`):** As referências de `MEUCCI, Attilio (2008)` e `MORGAN, J. P. (1996)` estão aglutinadas no mesmo parágrafo sem quebra de linha. O final de Meucci emenda diretamente no início de Morgan:
        `... p. 97-102, 2008.MORGAN, J. P. **RiskMetrics: technical document**...`
2.  **Nota Administrativa Oculta (Comentário do Orientador):**
    *   **Evidência (`P1449`):** A entrada de Rockafellar e Uryasev traz instruções internas de orientação mantidas no texto final:
        `ROCKAFELLAR, R. Tyrrell; URYASEV, Stanislav. Optimization of conditional value-at-risk. Journal of Risk, Londres, v. 2, n. 3, p. 21-41, 2000. (Nota do Orientador: Esta é a substituição oficial do link Forrs.de para justificar o CVaR).`
3.  **Metadados de Classificação de Biblioteca Física:**
    *   **Evidência (`P1387`):** A entrada de Damodaran contém dados de indexação interna de biblioteca que devem ser limpos:
        `DAMODARAN, Aswath. Avaliação de empresas. São Paulo: Pearson Education do Brasil, 2007. xiii, 464 p. ISBN 978-85-7605-105-3. Call number: 658.15 D163av 2007.`
4.  **Duplicidade Redundante:**
    *   **Evidência (`P1424` e `P1476`):** Há duas entradas quase idênticas referentes a trabalhos da Universidade de Lund catalogadas sob chaves distintas (`LUND UNIVERSITY` e `UNIVERSIDADE DE LUND`), nenhuma das quais é citada no texto.

---

## 3. Inconformidades de Estilo NBR 10520 (Citações no Corpo do Texto)

*   **Uso Incorreto de Caixa Alta:** Pela norma NBR 10520, autores citados fora de parênteses devem ter apenas a primeira letra maiúscula (ex.: *DeMiguel (2009)*). O texto do TCC apresenta desvios, mantendo caixa alta total fora de parênteses em alguns trechos.
*   **Separadores de Autores:** Citações multifontes dentro de parênteses devem utilizar ponto e vírgula `;` como separador. Há ocorrências com vírgula `,` (ex.: `(Meucci, 2005, Walters, 2014)` no parágrafo `P911`).
*   **Citações de Três ou Mais Autores:** O texto oscila entre citar nominalmente todos os autores de uma obra com 5 autores (ex.: `P326`: `(Boyd, Johansson, Kahn, Schiele, Schmelzer, 2024)`) e o uso correto do termo `et al.` prescrito para obras com mais de três autores.

---

## 4. Higiene de Originalidade Interna

*   **Autoparentesco de Parágrafos:** Não foram identificadas ocorrências de plágio direto ou quebra de integridade acadêmica. O texto apresenta paráfrases bem estruturadas.
*   **Higiene de Modelos Descartados:** A presença das referências fantasmas de LSTM (`Hochreiter & Schmidhuber`, `Yilmaz`) denota falta de limpeza da bibliografia após a simplificação do projeto físico para modelos estatísticos puros (sem Deep Learning). Essas referências devem ser inteiramente removidas.
*   **Consistência das Siglas:** Recomenda-se a revisão para que referências bibliográficas clássicas de modelos de cauda sejam associadas às primeiras menções das siglas correspondentes na introdução.

---

## Seção "NÃO VERIFICADO"

*   **Existência de URL e DOIs específicos:** Não foi validada a validade e status atualizado de todos os links `Disponível em: <...>` devido ao ambiente read-only off-line. Presume-se que os links reais da B3 e de repositórios universitários listados requeiram verificação pelo Turnitin da UFG.
