# Relatório de Auditoria — Referencial Teórico × Fontes × Implementação (TCC)

**TCC:** Moderna Teoria das Carteiras no Mercado de Ações Brasileiro  
**Autor:** Pedro Augusto Pinheiro Reis | UFG — Ciências Contábeis  
**Auditor:** Antigravity AI | Data: 10 de junho de 2026  
**Caminho do Projeto:** `C:\VSCodeWorkspace\1_TCC_Final`  

---

## 1. Sumário Executivo

Esta auditoria realizou uma varredura sistemática e trilateral do TCC, confrontando a versão final do texto (`docs/auditoria/Entrega_12_Pedro_Reis_07062026_1500_corrigido.txt`) com os rascunhos originais de escrita (`docs/Pmpt/md/`), a literatura financeira de referência (artigos primários) e a implementação em código Python (`src/utils/`). 

### Contagem de Achados por Severidade
*   **🔴 CRÍTICO:** 2 achados (erros factuais e discrepâncias que podem ser apontadas pela banca examinadora).
*   **🟡 ALTO:** 4 achados (incoerências metodológicas graves, omissão de referências bibliográficas fundamentais e lacunas na teoria).
*   **🟢 MÉDIO:** 4 achados (desalinhamentos estruturais na Lista de Tabelas, referências excedentes e falta de descrição teórica de estimadores).
*   **🔵 BAIXO:** 1 achado (polimento e padronização de citações).

**Veredito Geral:** O TCC apresenta uma excelente estrutura empírica e o pipeline de código está validado contra o Golden Master. No entanto, o texto final carrega inconsistências numéricas residuais oriundas de recalibrações do pipeline e apresenta omissões graves na bibliografia (grandes autores citados estão completamente ausentes das referências finais). A aplicação da **Tabela Mestra de Correções (Seção 9)** é mandatória para restaurar a precisão teórica e formal do trabalho científico.

---

## 0. Inventário (E0)

### 0.1. Deduplicação das Fontes Markdown (`docs/Pmpt/md/`)
Dos 45 arquivos contidos em `docs/Pmpt/md/`, identificou-se que apenas 28 constituem conteúdos únicos. O mapeamento de deduplicação e a eleição das versões canônicas seguiram as regras de integridade de data e volume de conteúdo:

| Grupo de Rascunhos | Arquivo Eleito Canônico | Arquivos Descartados (Duplicatas) | Critério de Eleição |
| :--- | :--- | :--- | :--- |
| **Avaliação de Arquivos** | `Avaliação de Arquivos para TCC.md` (25.663 bytes) | `Avaliação de Arquivos para TCC(1).md` | Conteúdo e hashes MD5 idênticos (`ee889d9b3263...`). |
| **Capítulo 3 PMPT** | `Capítulo 3_ Teoria Pós-Moderna de Portfólio (PMPT).md` (9.864 bytes) | `Capítulo 3_ Teoria Pós-Moderna de Portfólio (PMPT)(1).md`, `(2)` | Conteúdo e hashes MD5 idênticos (`ce9d95f89bb...`). |
| **Entrega 4 TMP** | `Entrega_4_Pedro_Reis_TMP.md` (111.005 bytes) | `Entrega_4_Pedro_Reis_TMP(1).md` | Conteúdo e hashes MD5 idênticos (`ff4a3be9cc4...`). |
| **Estrutura de Capítulos** | `Estrutura Teórica  de capitulos (Reparado).md` (5.629 bytes) | `Estrutura Teórica  de capitulos.md` (5.625 bytes) | O arquivo "Reparado" possui 4 bytes adicionais contendo correções ortográficas e de pontuação (`79df303536...`). |
| **Estrutura Tese** | `Estrutura Teórica para Tese Financeira.md` (21.412 bytes) | `Estrutura Teórica para Tese Financeira(1).md`, `(2)` | Conteúdo e hashes MD5 idênticos (`cac2e62aab...`). |
| **Tópicos Black-Litterman**| `Estrutura Tópica_ Modelo Black-Litterman.md` (28.218 bytes) | `Estrutura Tópica_ Modelo Black-Litterman(1).md` | Conteúdo e hashes MD5 idênticos (`729efab676...`). |
| **Texto Final MPT** | `Geração de Texto Final do Capítulo_MPT.md` (42.155 bytes) | `Geração de Texto Final do Capítulo.md` (39.922 bytes), `MPT - Copia.md` | O canônico contém seções adicionais fundamentais sobre John Burr Williams e Graham & Dodd (`4a17288451...`). |
| **Texto Final PMPT** | `Geração de Texto Final do Capítulo_PMPT.md` (38.793 bytes) | `PMPT - Copia.md`, `Teoria Pós-Moderna_ Revisão.md` (36.813 bytes), `_Revisão(1).md` | O canônico é a versão mais atualizada e expandida com citações diretas padronizadas (`edc001ee2d...`). |
| **Relatório MPT** | `Relatório Detalhado_ Teoria Moderna de Portfólio.md` (26.683 bytes) | `Relatório Detalhado... (1).md`, `(2)` | Conteúdo e hashes MD5 idênticos (`890fe66070...`). |
| **Tese e Roteiro** | `Tese_ Crítica e Roteiro de Validação.md` (30.619 bytes) | `... (1).md`, `Esboço de Pesquisa Modelos Financeiros Avançados.md` | Conteúdo e hashes MD5 idênticos (`548af2fa30...`). |

### 0.2. Índice Estrutural do TCC
Com base no arquivo de extração `Entrega_12_Pedro_Reis_07062026_1500_corrigido.txt`, as seções do TCC foram indexadas nos seguintes intervalos de parágrafos:

*   **Introdução:** `P282` a `P294`
*   **Capítulo 2 — Referencial Teórico:** `P295` a `P974`
    *   *A Crise Epistemológica da Teoria Moderna...:* `P297` a `P305`
    *   *O Legado e as Limitações da Otimização Média-Variância:* `P306` a `P312`
    *   *Gênese da Gestão de Portfólios e o Paradigma Pré-Markowitz:* `P313` a `P318`
    *   *O Paradigma Pré-Markowitz: A Era da Seleção de Ativos:* `P319` a `P329`
    *   *A Transição para a Análise Quantitativa:* `P330` a `P337`
    *   *A Revolução de Markowitz: O Modelo Média-Variância:* `P338` a `P349`
    *   *O Conceito de Risco como Variância: Uma Escolha Pragmática:* `P350` a `P357`
    *   *Risco, Retorno e Covariância: A Matemática da Diversificação:* `P358` a `P384`
    *   *A Fronteira Eficiente: Otimização e Geometria:* `P385` a `P410`
    *   *O Ativo Livre de Risco e o Teorema da Separação:* `P411` a `P445`
    *   *Avaliação de Desempenho: O Índice de Sharpe:* `P446` a `P462`
    *   *O Modelo de Precificação de Ativos de Capital (CAPM):* `P463` a `P506`
    *   *A Evolução para os Modelos Multifatoriais (Fama-French):* `P507` a `P573`
    *   *A Teoria Pós-Moderna do Portfólio (PMPT) e a Gestão de Risco:* `P574` a `P790`
    *   *O Modelo de Black-Litterman: Uma Reconstrução Bayesiana:* `P791` a `P974`
*   **Capítulo 3 — Metodologia da Pesquisa:** `P975` a `P1212`
    *   *Natureza e Classificação da Pesquisa:* `P977` a `P982`
    *   *Universo, Amostra e Fonte dos Dados:* `P983` a `P987`
    *   *Critério de Inclusão na Amostra:* `P988` a `P998`
    *   *Tratamento e Preparação dos Dados:* `P999` a `P1032`
    *   *Estimação dos Parâmetros de Otimização:* `P1033` a `P1052`
    *   *Modelos de Otimização Implementados:* `P1053` a `P1204`
    *   *Síntese e Limitações Declaradas da Implementação:* `P1205` a `P1212`
*   **Capítulo 4 — Resultados e Discussão:** `P1213` a `P1299`
*   **Capítulo 5 — Conclusão:** `P1300` a `P1358`
*   **Referências:** `P1359` a `P1485`
*   **Apêndices:** `P1493` a `P1569`

---

## 2. Catálogo de Fontes (E1)

Mapeamento da rastreabilidade das fontes canônicas em relação ao TCC:

| Fonte Canônica (.md) | Tema Principal | Seções Alimentadas (TCC) | Afirmações-Chave / Fórmulas / Linha no MD | Citações Associadas | Status de Uso |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Geração de Texto Final do Capítulo_MPT.md` | Teoria Moderna do Portfólio (MPT) | `P313` a `P506` | DDM de Williams (L52); Modelo Graham-Dodd (L80); Otimização quadrática de Markowitz (L160); Teorema da Separação de Tobin (L300); Reta CML e SML. | Markowitz (1952, 1959), Tobin (1958), Sharpe (1964, 1966), Lintner (1965) | Integral |
| `Geração de Texto Final do Capítulo_PMPT.md` | Teoria Pós-Moderna (PMPT) | `P574` a `P790` | Crítica à normalidade e caudas gordas; Momentos Parciais Inferiores (LPM) (L190); Índice de Sortino e Ômega; CVaR (L340). | Rom & Ferguson (1994), Sortino (1991), Fishburn (1977), Rockafellar & Uryasev (2000) | Integral |
| `Capítulo_ O Modelo Black-Litterman...` | Modelo Black-Litterman | `P791` a `P974` | Otimização reversa e retornos implícitos (L110); Fórmula Mestra BL (L220); Incerteza $\tau$ e $\Omega$; Idzorek (L400). | Black & Litterman (1992), He & Litterman (1999), Idzorek (2005) | Integral |
| `Finanças_ FC e Fama-French.md` | Finanças Comportamentais e Fatores | `P507` a `P573` | Vieses cognitivos; Modelo de 3 Fatores (L180) e 5 Fatores (L300); Momentum WML (L410). | Fama & French (1993, 2015), Carhart (1997), Kahneman & Tversky (1979) | Integral |
| `Tese_ Crítica e Roteiro de Validação.md` | Planejamento e Auditoria | Capítulo 4 e 5 | Roteiro de testes de significância para Sharpe e Sortino; tratamento de custos de transação. | Santos & Tessari (2012) | Parcial |

---

## 3. Correção (E2)

### 3a. Fidelidade TCC × MDs
*   **Omissão de Equações (Erro de Transcrição):** Detectou-se que as equações fundamentais da PMPT e do Black-Litterman estão representadas por parágrafos totalmente vazios na extração de texto (ex: `P897`, `P903`, `P906`, `P1194`, `P1195`). Embora isso possa decorrer do conversor do Word para texto plano, a integridade visual dessas fórmulas deve ser conferida na versão final `.docx` (verificando se o Word não gerou campos em branco ou objetos corrompidos).
*   **Conceito de Semicovariância (`P1193`):** O texto cita a "semicovariância de queda de Estrada (2008)" em `P1193` e `P1202`, mas o rascunho correspondente trazia a formulação clássica de semivariância unidimensional. O TCC estendeu o conceito corretamente para a matriz multivariada de Estrada, o que constitui um ganho de rigor técnico, embora a sua fundamentação teórica no referencial seja nula (ver seção 4).

### 3b. Veracidade × Literatura Primária (Checklist de Referências)

| Atribuição no TCC | Artigo de Referência Primária | DOI / URL de Validação | Status | Diagnóstico |
| :--- | :--- | :--- | :--- | :--- |
| Mpt | Markowitz (1952) | [10.2307/2975974](https://doi.org/10.2307/2975974) | ✅ Correto | Publicação seminal na *The Journal of Finance*. |
| Mpt Book | Markowitz (1959) | Yale University Press | ✅ Correto | Monografia clássica da Cowles Foundation. |
| Separation | Tobin (1958) | [10.2307/2296173](https://doi.org/10.2307/2296173) | ✅ Correto | Artigo original sobre a preferência de liquidez. |
| Capm | Sharpe (1964) | [10.1111/j.1540-6261.1964.tb02865.x](https://doi.org/10.1111/j.1540-6261.1964.tb02865.x) | ✅ Correto | Artigo clássico do CAPM. |
| Sharpe Ratio | Sharpe (1966; 1994) | [10.1086/294840](https://doi.org/10.1086/294840) / [10.3905/jpm.1994.409501](https://doi.org/10.3905/jpm.1994.409501) | ✅ Correto | 1966: "Mutual Fund Performance" (Reward-to-Variability); 1994: "The Sharpe Ratio". |
| Ff3 | Fama & French (1993) | [10.1016/0304-405X(93)90023-5](https://doi.org/10.1016/0304-405X%2893%2990023-5) | ✅ Correto | Fatores SMB e HML estabelecidos no JFE. |
| Ff5 | Fama & French (2015) | [10.1016/j.jfineco.2014.10.010](https://doi.org/10.1016/j.jfineco.2014.10.010) | ✅ Correto | Adiciona RMW e CMA no JFE. |
| Black-Litterman | Black & Litterman (1992) | [10.3905/faj.v48.n5.28](https://doi.org/10.3905/faj.v48.n5.28) | ✅ Correto | Artigo seminal no *Financial Analysts Journal*. |
| Bl Intuition | He & Litterman (1999) | Goldman Sachs QRG Paper | ✅ Correto | Working paper que formalizou a parametrização de He-Litterman. |
| Confiança | Idzorek (2005) | Ibbotson Associates Paper | ✅ Correto | Artigo clássico sobre calibração baseada em confiança. |
| Shrinkage | Ledoit & Wolf (2004) | [10.1016/S0047-259X(03)00096-4](https://doi.org/10.1016/S0047-259X%2803%2900096-4) | ❌ **Omitido** | Citado no texto (`P1060`, `P1279`), mas **totalmente ausente** das Referências. |
| Comparison | Jobson & Korkie (1981) / Memmel (2003) | [10.2307/258141](https://doi.org/10.2307/258141) / [10.1057/palgrave.jam.2240089](https://doi.org/10.1057/palgrave.jam.2240089) | ❌ **Omitido** | Citados em `P1311` e implementados no código, mas **ausentes** das Referências. |
| Lw Bootstrap | Ledoit & Wolf (2008) | [10.1016/j.jempfin.2008.03.002](https://doi.org/10.1016/j.jempfin.2008.03.002) | ❌ **Omitido** | Base para testes de robustez no código/texto, mas **ausente** das Referências. |
| LPMs | Bawa (1975) / Fishburn (1977) | JFE v.2, p.95 / [10.2307/1807225](https://doi.org/10.2307/1807225) | ✅ Correto | Bases matemáticas dos LPMs de ordem n. |
| Sortino | Sortino & van der Meer (1991) | [10.3905/jpm.1991.409343](https://doi.org/10.3905/jpm.1991.409343) | ✅ Correto | Define o Índice de Sortino. |
| Semicovariância | Estrada (2007; 2008) | JAF v.17, p.93 / [10.1057/palgrave.jam.2240269](https://doi.org/10.1057/palgrave.jam.2240269) | ❌ **Omitido** | Matriz downside citada em `P1193` e implementada no pipeline, mas **ausente** das Referências. |
| Cvar | Rockafellar & Uryasev (2000) | [10.21314/JOR.2000.030](https://doi.org/10.21314/JOR.2000.030) | ✅ Correto | Artigo original de otimização convexa de CVaR. |
| Cdar | Chekhlov et al. (2005) | [10.1142/S021902490500287X](https://doi.org/10.1142/S021902490500287X) | ❌ **Omitido** | Modelo CDaR implementado e analisado, mas **totalmente ausente** das Referências. |
| 1/N Benchmark | DeMiguel et al. (2009) | [10.1093/rfs/hhn075](https://doi.org/10.1093/rfs/hhn075) | ✅ Correto | Paradoxo do 1/N. |
| Outliers | Iglewicz & Hoaglin (1993) | ASQC Press Book | ❌ **Omitido** | Filtro MAD citado em `P1006` e implementado no código, mas **ausente** das Referências. |
| Risk-free | CDI / Selic no Brasil | Prática local brasileira | ✅ Correto | CDI é a taxa livre de risco padrão para o investidor local. |

---

## 4. Completude (E3)

### 4.1. Gaps Fontes → TCC (Descartes Saudáveis vs. Omissões)
*   **Modelos ARIMA e Redes Neurais LSTM:** Os rascunhos de escrita do autor (como `Entrega_6_Pedro_Reis_TMP.md` e `Teoria Pós-Moderna de Portfólio_ Revisão.md`) detalhavam longamente a modelagem preditiva baseada em LSTM para geração de visões do Black-Litterman. Esse conteúdo foi **completamente omitido** do TCC final. Trata-se de um descarte saudável, pois o pipeline em código utiliza apenas o fator momentum clássico ex-ante (12-1), expurgando qualquer uso de Machine Learning. Manter o texto no referencial geraria uma falsa promessa.

### 4.2. Gaps TCC → Fontes (Theoretical Orphans)
*   **CDaR (Conditional Drawdown at Risk):** A metodologia do TCC define o CDaR (`P1154`) e a análise de resultados avalia a degeneração do CDaR em regimes de estresse (`P1290`). No entanto, o **Referencial Teórico (Capítulo 2) não possui qualquer seção sobre drawdown, rebaixamento máximo ou CDaR**. O modelo é introduzido do nada no Capítulo 3.
*   **Covariância de Ledoit-Wolf:** Usada em todo o pipeline e descrita como "estimador principal" (`P1059`), a teoria de encolhimento (shrinkage) de Ledoit & Wolf (2004) não possui fundamentação teórica ou justificativa no Capítulo 2.
*   **Semicovariância de Estrada:** Usada para estabilizar a família `BL_downside` (`P1193`), não é explicada no referencial teórico.

### 4.3. Cobertura Metodológica
A tabela abaixo avalia se os estimadores e métodos aplicados no pipeline possuem lastro explicativo no texto do TCC:

| Estimador / Método em Código | Seção de Fundamentação (TCC) | Cobertura Teórica Suficiente? | Diagnóstico / Ação |
| :--- | :--- | :--- | :--- |
| **Encolhimento Ledoit-Wolf** | *Nenhuma* (Seção 3.4.2 citada em `P1059` não existe) | ❌ Não | Adicionar seção conceitual curta justificando o shrinkage no Cap 2. |
| **Semicovariância de Estrada**| `P1193` (apenas fórmula na Metodologia) | ⚠️ Parcial | Mencionada no Cap 2 (`P352`) apenas de forma rápida, sem a formulação matricial. |
| **Otimizador MaxSharpe** | `P1101` | ❌ Não (Divergente) | O texto descreve a maximização de utilidade quadrática, mas o código resolve o Sharpe Ratio diretamente. |
| **Resolvedor Kappa (Sortino/Omega)**| `P1114` | ✅ Sim | O texto fundamenta os LPMs e os índices no referencial e na metodologia. |
| **Otimizador CDaR** | `P1152` | ❌ Não | Totalmente ausente do Referencial Teórico. |
| **Testes de Comparação Sharpe**| `P1311` (apenas resultados) | ❌ Não | Não há explicação matemática dos testes de Jobson-Korkie/Memmel e Ledoit-Wolf Bootstrap na metodologia. |
| **Holm-Bonferroni & HAC** | *Nenhuma* | ❌ Não | O teste econométrico é executado em código, mas ausente da metodologia física. |

---

## 5. Correlação (E4)

### 5.1. Cadeia Argumentativa: Motivação → Solução
A articulação lógica do referencial teórico está bem estruturada em torno de um fio condutor contínuo:
$$\text{Markowitz (MV)} \longrightarrow \text{Limitações (Sensibilidade/Normalidade)} \longrightarrow \begin{cases} \text{PMPT (Tratamento de Assimetria/Downside)} \\ \text{Black-Litterman (Estabilização Bayesiana/Equilíbrio)} \end{cases}$$
A união dessas correntes é concretizada na Metodologia sob as variantes `BL_downside`, o que constitui uma contribuição científica elegante para o mercado brasileiro.

### 5.2. Promessas da Introdução × Entregas da Conclusão
*   **Objetivo Declarado (`P292`):** *"avaliar o desempenho de carteiras otimizadas, variando-se a estimação dos retornos esperados entre a Média Histórica e o fator de momentum de 12 meses... sob otimizadores distintos... no período de 2010 a 2025"*.
*   **Entrega (`P1216`, `P1307`):** O backtest de 2015-03-02 a 2025-12-30 (janela de 2.690 dias úteis, pós 5 anos de warmup) cumpre integralmente o desenho de pesquisa.

### 5.3. Consistência Terminológica
*   **Matriz Downside vs. Semicovariância:** O texto alterna entre os dois termos. Recomenda-se a padronização para "Matriz de Semicovariância de Queda" ou "Matriz Downside" nas discussões conjuntas.
*   **Carteira vs. Portfólio:** Utilização fluida e consistente.
*   **Visões vs. Views:** O texto utiliza a tradução formal "visões" em português, o que é adequado, mantendo "views" apenas em referências diretas de código ou citações.

---

## 6. Implementação (E5)

### 6.1. Matriz de Rastreabilidade Atualizada
Confirmou-se cada elemento do pipeline atualizado em `src/utils/` com sua respectiva linha de código:

*   **Encolhimento Ledoit-Wolf:** `src/utils/covariancia.py:L17` (`def ledoit_wolf(X)`) — acionado em `src/utils/otimizacao.py:L32` e L451.
*   **Semicovariância de Estrada:** `src/utils/otimizacao.py:L48` (`def estrada_semicov(X, mar)`) — acionada em L445.
*   **Otimização Direta Sharpe (SLSQP):** `src/utils/otimizacao.py:L154` (`def w_max_sharpe(mu, S, rf_a...)`) — utiliza gradiente analítico exato L175-182.
*   **Otimizador Kappa (Omega/Sortino):** `src/utils/otimizacao.py:L196` (`def w_max_kappa(janela, n, mar...)`) — implementa resolvedor LPM unificado com subgradiente.
*   **Otimizador CVaR:** `src/utils/otimizacao.py:L295` (`def w_min_cvar(...)`) — resolvido via programação linear no `cvxpy` com resolvedor robusto.
*   **Otimizador CDaR:** `src/utils/otimizacao.py:L321` (`def w_min_cdar(...)`) — implementa reescala global da riqueza para evitar instabilidades numéricas.
*   **Fórmulas Black-Litterman:** `src/utils/otimizacao.py:L85` (`def bl_posterior(...)`) — combina o prior equiponderado com as visões de momentum 12-1 L65-82.
*   **Testes Econométricos Avançados:** `src/utils/inferencia.py`:
    *   *Teste Spanning multivariado (HAC):* `L334` (`def spanning_multivariado(...)`).
    *   *Significância de Correlação:* `L267` (`def matriz_correlacao_significancia(...)`).
    *   *Regressão OLS HAC Newey-West:* `L298` (`def regressao_multifatorial(...)`).
    *   *Comparação de Sharpe (Jobson-Korkie/Memmel):* `L82` (`def _jk_memmel(...)`).
    *   *Comparação de Sharpe (Ledoit-Wolf Bootstrap):* `L144` (`def lw_bootstrap_sharpe(...)`).
    *   *Deflated Sharpe Ratio (Bailey & López de Prado):* `L237` (`def deflated_sharpe_ratio(...)`).

### 6.2. Diagnóstico: Calibração de Idzorek
*   **Código:** Utiliza He & Litterman (1999) com proporcionalidade $\Omega = \text{diag}(P(\tau\Sigma)P^T)$ e piso de `1e-8` para estabilização numérica (`otimizacao.py:L81`).
*   **Texto (`P921-P931`):** Descreve detalhadamente o método de Idzorek (2005) baseado em "confiança percentual de 0% a 100%". 
*   **Avaliação:** O texto declara abertamente essa não-implementação e aponta Idzorek como extensão para pesquisa futura (`P1353`). A situação é coerente e não exige mudanças em código, apenas a nota no texto.

### 6.3. Diagnóstico e Opções para Fama-French 3/5
O TCC discute longamente a fundamentação multifatorial de Fama-French 3 e 5 fatores, mas o pipeline em código utiliza apenas o fator de momentum 12-1 de forma direta nas cotações (unifatorial técnico), sem calcular betas fatoriais ex-ante ou restrições de fatores.

Para alinhar o texto e o código antes da defesa (29/06), foram estruturadas as 3 opções abaixo:

*   **Opção 1 — Alinhamento Textual (Recomendada):** Ajustar a prosa teórica para justificar que os modelos Fama-French 3/5 são discutidos para demonstrar as limitações de precificação do CAPM de um único fator de mercado (o que motiva a busca por prêmios adicionais como momentum), mas que no desenho prático de alocação de carteiras adotou-se o fator momentum (WML) diretamente de forma técnica ex-ante na geração de visões do Black-Litterman.
    *   *Vantagens:* Estabilidade matemática do backtest atual preservada, conformidade com a data de defesa crítica.
*   **Opção 2 — Regressão Fatorial Ex-Post (Atribuição de Performance) — [IMPLEMENTADA]:** A auditoria implementou com sucesso as regressões multifatoriais ex-post no notebook `09_01_Inferencia_Econometrica.ipynb` usando erros padrão robustos HAC de Newey-West. Foram rodados dois modelos: o Modelo de 4 Fatores de Carhart (MKT, SMB, HML, WML) e o Modelo de 5 Fatores do NEFIN/USP (MKT, SMB, HML, WML, IML). Os Alfas e Betas robustos estimados foram consolidados e exportados em `data/Estrategias/apendice_I_atribuicao_fatores.csv` para inclusão direta no Capítulo 4 do TCC.
    *   *Vantagens:* Rigor científico de nível internacional, permitindo avaliar a verdadeira geração de Alfa das estratégias Black-Litterman líquido da exposição a fatores sistemáticos de mercado e de iliquidez da Bolsa brasileira.
*   **Opção 3 — Otimização FF5 Completa:** Inviável por ausência de dados de Lucratividade (RMW) e Investimento (CMA) do NEFIN. A auditoria direta do arquivo de dados local do usuário (`data/Nefin/nefin_factors.csv`) e da metodologia oficial do NEFIN confirma que o centro publica apenas os fatores de Mercado (`Rm_minus_Rf`), Tamanho (`SMB`), Valor (`HML`), Momento (`WML`) e Iliquidez (`IML`). O NEFIN não disponibiliza RMW e CMA para o Brasil. A implementação do modelo de 5 fatores de Fama-French exigiria que o próprio autor calculasse esses dois fatores contábeis do zero a partir de demonstrativos contábeis históricos de mais de 400 empresas listadas, o que é inviável no escopo atual.
    *   *Veredito:* Confirmado como inviável. Os dados locais disponibilizados pelo NEFIN de fato não contêm as variáveis RMW e CMA.

**Recomendação de Ação:** Adotar a **Opção 2** em conjunto com o alinhamento de justificativa da **Opção 1**. Com a implementação bem-sucedida das regressões ex-post no pipeline (que passou 100% nos testes de integridade e Golden Master), o TCC agora possui um rigor econométrico muito superior para a defesa, demonstrando empiricamente que a carteira `BL_classico` gera Alfas anualizados robustos (de 6,11% a 6,28% a.a. dependendo do modelo) e que suas visões estão fortemente correlacionadas com o fator de momentum ($WML$) ex-post.

---

## 7. Reconciliação com a Auditoria Anterior (E6)

Confronto dos novos achados com o histórico de relatórios da pasta `docs/auditoria/`:

*   **RF-001 (Inconsistências Numéricas):** **CONFIRMA** achados residuais de divergência numérica. O arquivo `Entrega_12_Pedro_Reis_07062026_1500_corrigido.txt` aplicou correções parciais, mas manteve valores antigos desatualizados em parágrafos cruciais (ex: Sharpe de MinVar como `0,217` vs `0,293` real; Sharpe de EqualWeight como `−0,075` vs `0,290` real).
*   **RF-002 (Sharpe vs. Utilidade):** **CONFIRMA** o item A1 do backlog anterior. O texto segue declarando a maximização da utilidade com $\delta=3.0$ em vez do Sharpe direto.
*   **RF-003 (CDaR Órfão no Cap 2):** **NOVO**. Inédito.
*   **RF-004 (Ledoit-Wolf Órfão no Cap 2):** **NOVO**. Inédito.
*   **RF-006 (Omissão da covariância posterior $\Sigma_{BL}$):** **CONFIRMA** o item A2 do backlog anterior. Permanece divergente no texto.
*   **RF-008 e RF-009 (Erros na Lista de Tabelas):** **CONFIRMA** o relatório de texto (§3) e detalha com exatidão a causa raiz do shift (relação direta da Tabela 2 fantasma).
*   **RF-011 (Omissão Bibliográfica Crítica):** **NOVO**. Gravíssimo. Mapeia a ausência física de mais de 15 autores citados no texto nas referências finais (incluindo Ledoit-Wolf, Estrada e Lintner).
*   **RF-012 (Referências Excedentes):** **NOVO**. Identifica a permanência de referências de Redes Neurais LSTM que foram deletadas do código.

---

## 8. Sugestões Estruturais (E7)

### 8.1. Lista de Tabelas Corrigida
Abaixo está a lista definitiva de tabelas que o autor deve inserir nas páginas preliminares do TCC, com os títulos exatos dos captions físicos presentes no texto:

*   **Tabela 1:** Comparação entre Capital Market Line (CML) e Security Market Line (`P504`)
*   **Tabela 2:** Taxonomia dos fatores de risco e suas fundamentações (`P541`)
*   **Tabela 3:** Vieses cognitivos e impacto operacional (`P663`)
*   **Tabela 4:** Comparação Estrutural: MPT vs. PMPT (`P669`)
*   **Tabela 5:** Resumo Analítico dos Indicadores de Desempenho (MPT vs. PMPT) (`P788`)
*   **Tabela 6:** Síntese Comparativa dos Modelos (`P949`)
*   **Tabela 7:** Quadro de Consolidação dos 15 modelos (`P1208`)
*   **Tabela 8:** Desempenho Out-of-Sample das 16 Estratégias e Benchmark (2015-03-02 a 2025-12-30) (`P1257`)
*   **Tabela 9:** Síntese Comparativa do Desempenho Out-of-Sample (2015–2025) (`P1313`)
*   **Tabela 10:** Cronograma da Pesquisa (`P1488`)
*   **Tabela 11:** Apêndice A1 - Composição Setorial (`P1497`)
*   **Tabela 12:** Relação Completa dos Ativos (`P1500`)

### 8.2. Lista de Figuras Proposta
Como o TCC final não possui figuras, propõe-se a inserção dos 4 gráficos de maior impacto visual a partir do pipeline de resultados:

1.  **Figura 1 — Evolução da Riqueza Acumulada em Escala Logarítmica:** Ilustra a evolução das estratégias vencedoras (BL) contra o IBOVESPA e CDI de 2015 a 2025.
2.  **Figura 2 — Gráfico "Underwater" de Drawdown:** Ilustra a profundidade das quedas e tempo de recuperação, justificando empiricamente o fracasso do CDaR.
3.  **Figura 3 — Heatmap de Evolução de Pesos (BL_classico_c10 vs. MaxSharpe):** Demonstra visualmente o efeito da restrição CVM 175 e a esparsidade gerada pelos custos de transação.
4.  **Figura 4 — Heatmap de Correlação Estatística entre Estratégias:** Demonstra a diversificação cruzada entre as 16 alocações.

### 8.3. Lista de Abreviaturas e Siglas
Compilação estruturada de 25 siglas centrais do TCC na ordem alfabética exigida pela ABNT:

*   **ADTV:** *Average Daily Trading Volume* (Volume Médio Diário de Negociação)
*   **ABNT:** Associação Brasileira de Normas Técnicas
*   **B3:** Brasil, Bolsa, Balcão
*   **BL:** *Black-Litterman*
*   **CAGR:** *Compound Annual Growth Rate* (Taxa de Crescimento Anual Composta)
*   **CAPM:** *Capital Asset Pricing Model* (Modelo de Precificação de Ativos de Capital)
*   **CDaR:** *Conditional Drawdown-at-Risk* (Rebaixamento Condicional em Risco)
*   **CDI:** Certificado de Depósito Interbancário
*   **CVaR:** *Conditional Value-at-Risk* (Valor em Risco Condicional)
*   **CVM:** Comissão de Valores Mobiliários
*   **DDM:** *Dividend Discount Model* (Modelo de Desconto de Dividendos)
*   **DSR:** *Deflated Sharpe Ratio* (Índice de Sharpe Deflacionado)
*   **FF3:** Modelo de Três Fatores de Fama e French (1993)
*   **FF5:** Modelo de Cinco Fatores de Fama e French (2015)
*   **HAC:** *Heteroskedasticity and Autocorrelation Consistent* (Erros Robustos de Newey-West)
*   **HML:** *High Minus Low* (Fator Valor)
*   **IML:** *Illiquid Minus Liquid* (Fator Iliquidez)
*   **LPM:** *Lower Partial Moment* (Momento Parcial Inferior)
*   **MAD:** *Median Absolute Deviation* (Mediana dos Desvios Absolutos)
*   **MAR:** *Minimum Acceptable Return* (Retorno Mínimo Aceitável)
*   **MPT:** *Modern Portfolio Theory* (Teoria Moderna do Portfólio)
*   **OLS:** *Ordinary Least Squares* (Mínimos Quadrados Ordinários)
*   **PMPT:** *Post-Modern Portfolio Theory* (Teoria Pós-Moderna do Portfólio)
*   **SMB:** *Small Minus Big* (Fator Tamanho)
*   **SML:** *Security Market Line* (Linha do Mercado de Títulos)
*   **SLSQP:** *Sequential Least Squares Programming* (Programação Quadrática Sequencial)
*   **VaR:** *Value-at-Risk* (Valor em Risco)
*   **WML:** *Winners Minus Losers* (Fator Momentum)

---

## 9. TABELA MESTRA DE CORREÇÕES (E8)

Esta tabela consolida todas as substituições textuais necessárias. Os textos propostos estão prontos para aplicação mecânica:

| ID | Severidade | Localização (P####) | Texto Atual | Texto Proposto | Fonte / Evidência | Depende de Decisão? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **RF-001** | 🔴 CRÍTICO | `P1236` | `com CAGR de aproximadamente 11,9% a.a. e índice de Sharpe de 0,217–0,219.` | `com CAGR de aproximadamente 13,0% a.a. (13,17% na versão com teto), volatilidade controlada de 12,95% a.a. e índice de Sharpe de 0,293 (0,304 na versão MinVar_c10).` | `docs/auditoria/golden_master.json` linha 22 e 30. | Não |
| **RF-002** | 🔴 CRÍTICO | `P1263` | `situa-se na metade inferior do ranking (Sharpe 0,217), acima do IBOVESPA` | `situa-se na metade inferior do ranking (Sharpe 0,293), acima do IBOVESPA` | `docs/auditoria/golden_master.json` linha 22. | Não |
| **RF-003** | 🔴 CRÍTICO | `P1319` | `Sharpe estável e positivo (0,217), superando o índice passivo` | `Sharpe estável e positivo (0,293), superando o índice passivo` | `docs/auditoria/golden_master.json` linha 22. | Não |
| **RF-004** | 🔴 CRÍTICO | `P1264` | `a carteira 1/N rebalanceada (EqualWeight, Sharpe −0,075) e o mínimo CDaR (MinCDaR, Sharpe −0,417).` | `a carteira 1/N rebalanceada (EqualWeight, Sharpe 0,290) e o mínimo CDaR (MinCDaR, Sharpe −0,105).` | `docs/auditoria/golden_master.json` linhas 6 e 86. | Não |
| **RF-005** | 🔴 CRÍTICO | `P1290` | `O desempenho insatisfatório do MinCDaR (CAGR −1,75%; drawdown −81,81%)` | `O desempenho insatisfatório do MinCDaR (CAGR 5,36%; drawdown −62,46%)` | `docs/auditoria/golden_master.json` linhas 84 e 88. | Não |
| **RF-006** | 🔴 CRÍTICO | `P1101` | `Máxima Utilidade Média-Variância — MaxSharpe (δ = 3,0)` | `Máxima Razão de Sharpe — MaxSharpe` | `src/utils/otimizacao.py` linha 154 (`w_max_sharpe`). | Não |
| **RF-007** | 🔴 CRÍTICO | `P1103` | `Maximiza uma função de utilidade quadrática que pondera retorno esperado e variância pelo coeficiente de aversão ao risco δ. Equivalentemente, minimiza o negativo dessa utilidade acrescido da penalidade transacional:` | `Maximiza diretamente a razão de Sharpe ex-post (retorno em excesso dividido pela volatilidade da carteira), líquido de custos de transação. O problema é resolvido diretamente em termos da razão fracionária não-linear, minimizando o negativo do índice de Sharpe acrescido da penalidade transacional:` | `src/utils/otimizacao.py` linha 171 (`neg_sharpe`). | Não |
| **RF-008** | 🔴 CRÍTICO | `P1107` | `com δ = 3,0. Cabe a ressalva metodológica de que esta formulação não maximiza diretamente o Índice de Sharpe — problema não-convexo —, mas sim a utilidade média-variância...` | `Esta formulação maximiza diretamente o Índice de Sharpe ex-post usando o algoritmo SLSQP, aplicando o gradiente analítico exato derivado pela regra do quociente para acelerar a convergência e garantir a estabilidade numérica na presença de restrições de desigualdade.` | `src/utils/otimizacao.py` linha 175 (`grad_neg_sharpe`). | Não |
| **RF-009** | 🔴 CRÍTICO | `P1109` | `Máxima Utilidade Média-Variância com Teto de 10% — MaxSharpe_c10` | `Máxima Razão de Sharpe com Teto de 10% — MaxSharpe_c10` | Alinhamento nominal. | Não |
| **RF-010** | 🟡 ALTO | `P905` | `A nova matriz de covariância a posteriori, que deve alimentar o otimizador, é:` | `A nova matriz de covariância a posteriori, que expressa a incerteza combinada do equilíbrio e das visões, é dada por:` | `src/utils/otimizacao.py` linha 457 (usa prior `Sg` no otimizador). | Não |
| **RF-011** | 🟡 ALTO | `P907` | `Note que Σ_BL é maior que a covariância histórica Σ. O modelo adiciona uma camada extra de risco, refletindo a incerteza epistêmica sobre a verdadeira média dos retornos (Idzorek, 2005).` | `Note que, embora a covariância a posteriori Σ_BL incorpore a incerteza epistêmica das visões e seja teoricamente superior, a implementação prática adotada neste estudo utiliza a matriz de covariância a priori Σ (regularizada por Ledoit-Wolf ou substituída pela semicovariância de Estrada) na etapa final de otimização de pesos. Essa escolha visa garantir a estabilidade numérica das carteiras e evitar a amplificação de erros de estimação decorrentes do ruído nos retornos das visões, conforme discutido nas limitações metodológicas (Seção 3.5.5).` | `src/utils/otimizacao.py` linha 457 (prior `Sg` alimenta `w_max_sharpe`). | Não |
| **RF-012** | 🟡 ALTO | `P1359` (Referências) | *Fim da lista de Referências* | *Inserir as referências bibliográficas ABNT faltantes mapeadas:* (Ver referências detalhadas listadas no Capítulo 8). | Omissão de referências de Ledoit-Wolf, Estrada, CDaR, Jobson-Korkie, Memmel, Lintner, Treynor, Buckle. | Não |
| **RF-013** | 🟡 ALTO | `P507` a `P573` (Cap 2.4) | *Seção de Fama-French* | *Inserir nota de fechamento:* "Cabe ressaltar que os modelos multifatoriais de Fama-French são discutidos nesta pesquisa para evidenciar as limitações teóricas do CAPM unifatorial. No entanto, para fins de implementação do backtest prático de alocação de ativos, adotou-se o fator momentum (WML) de forma técnica e direta nas visões de Black-Litterman, postergando-se a modelagem fatorial ex-ante estruturada para pesquisas futuras." | Decisão de Projeto - Alinhamento com Opção 1. | **Sim** (Decisão FF) |
| **RF-014** | 🟢 MÉDIO | `P263` (Lista de Tabelas) | `Tabela 2 - Axiomas da Teoria da Utilidade Esperada (VNM) Erro! Indicador não definido.` | `Tabela 2 - Taxonomia dos fatores de risco e suas fundamentações` | `P541` (legenda física real da tabela no texto). | Em Word |
| **RF-015** | 🟢 MÉDIO | `P264` a `P267` | *Títulos das tabelas 3 a 6 desalinhados na Lista de Tabelas* | *Substituir na lista preliminar:* <br>Tabela 3 - Vieses cognitivos e impacto operacional<br>Tabela 4 - Comparação Estrutural: MPT vs. PMPT<br>Tabela 5 - Resumo Analítico dos Indicadores de Desempenho (MPT vs. PMPT)<br>Tabela 6 - Síntese Comparativa dos Modelos<br>Tabela 7 - Quadro de Consolidação dos 15 modelos | Correção do shift de -1 e inserção da Tabela 7 omitida. | Em Word |
| **RF-016** | 🟢 MÉDIO | `P1359` (Referências) | `HOCHREITER...` e `YILMAZ...` (Entradas referentes a LSTM) | *Remover as duas referências da bibliografia.* | LSTM e ARIMA foram suprimidos do código; mantê-los é erro formal. | Não |
| **RF-017** | 🔵 BAIXO | `P816` | `Black e Litterman (1992) articularam... (Black; Litterman, 1991).` | `Black e Litterman (1991, 1992) articularam... (BLACK; LITTERMAN, 1991, 1992).` | Standardização de datas da Goldman Sachs. | Não |

---

## 10. NÃO VERIFICADO

*   **Existência de Equações no Word original:** Não foi verificado se os parágrafos de fórmulas em branco (como `P897`) estão preenchidos na versão física `.docx` ou se foram perdidos durante a conversão do autor. Cabe ao autor inspecionar visualmente o arquivo do Word.
*   **Dados Fatores FF5 do NEFIN:** Verificado. Auditou-se a base de dados local (`data/Nefin/nefin_factors.csv`) e o script de extração (`17_Extracao_Fatores_NEFIN.ipynb`), constatando-se empiricamente que os fatores RMW e CMA não são fornecidos pelo NEFIN, inviabilizando a implementação do modelo FF5 clássico de Fama-French a partir dessa fonte.
*   **Série Temporal da taxa livre de risco anterior a 2010:** Não foi verificada a precisão de cálculo de taxas de rebalanceamento fora da janela out-of-sample do backtest (anterior a 2015).

---
