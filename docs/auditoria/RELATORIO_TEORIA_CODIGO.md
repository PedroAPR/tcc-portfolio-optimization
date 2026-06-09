# Relatório de Rastreabilidade — Teoria ↔ Código (Fase P5)

**Objetivo:** Mapear os modelos matemáticos, hipóteses e otimizadores descritos no Referencial Teórico e na Metodologia da dissertação para a sua implementação física na branch `tcc-aprimoramento`, identificando lacunas e divergências conceituais.

---

## 1. Matriz de Rastreabilidade Teoria ↔ Código

A tabela a seguir cruza cada formulação teórica presente na prosa do TCC (`docs/auditoria/Entrega_12_Pedro_Reis_07062026_1500_corrigido.txt`) com a respectiva linha de código nos arquivos do diretório `src/`:

| Modelo / Método / Equação | Descrição na Prosa (Parágrafo) | Arquivo no `src/` | Linha / Função no Código | Status de Implementação |
| :--- | :--- | :--- | :--- | :--- |
| **Ledoit-Wolf Shrinkage** | Ledoit & Wolf (2004) `P1060`, `P1279` | [covariancia.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/06_Estimacao_Covariancia/utils/covariancia.py) | L17: `def ledoit_wolf(X)` | **Implementado** |
| **Semicovariância Estrada**| Matriz downside de Estrada (2008) `P1193` | [otimizacao.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/utils/otimizacao.py) | L55: `def estrada_semicov(X, mar)` | **Implementado** |
| **Carteira 1/N (Equiponderada)**| Benchmark ingênuo `P1083` | [otimizacao.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/utils/otimizacao.py) | L109: `def w_equal(n)` | **Implementado** |
| **Inverso da Volatilidade**| Pesos inversos ao desvio-padrão `P1089` | [otimizacao.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/utils/otimizacao.py) | L114: `def w_inv_vol(S)` | **Implementado** |
| **Mínima Variância Global**| Minimiza $w'\Sigma w$ `P1093` | [otimizacao.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/utils/otimizacao.py) | L132: `def w_min_var(S, ...)` | **Implementado** |
| **Máximo Sharpe (Código)** | Maximiza razão Sharpe diretamente | [otimizacao.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/utils/otimizacao.py) | L161: `def w_max_sharpe(mu, S, ...)` | **Implementado** (com conflito na teoria, ver Seção 2) |
| **Máximo Sharpe (Teoria)** | Maximiza utilidade média-variância $\delta=3$ `P1104` | *Nenhum* | *Não implementado na forma quadrática* | **Divergente** (ver Seção 2) |
| **Momentos Parciais (LPM)**| Medida geral de risco de cauda `P1116` | [otimizacao.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/utils/otimizacao.py) | L203: `def w_max_kappa(..., n)` | **Implementado** (via resolvedor Kappa) |
| **Máximo Índice Ômega** | Razão de LPM com ordem $n=1$ `P1123` | [otimizacao.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/utils/otimizacao.py) | L203: `w_max_kappa` (com `n=1`) | **Implementado** (mapeado via Kappa) |
| **Máximo Índice de Sortino**| Razão de LPM com ordem $n=2$ `P1131` | [otimizacao.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/utils/otimizacao.py) | L203: `w_max_kappa` (com `n=2`) | **Implementado** (mapeado via Kappa) |
| **Máximo Kappa de Ordem 3** | Razão de LPM com ordem $n=3$ `P1139` | [otimizacao.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/utils/otimizacao.py) | L203: `w_max_kappa` (com `n=3`) | **Implementado** |
| **Mínimo CVaR** | LP de Rockafellar & Uryasev (2000) `P1145` | [otimizacao.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/utils/otimizacao.py) | L302: `def w_min_cvar(...)` | **Implementado** (via CVXPY) |
| **Mínimo CDaR** | LP de Chekhlov et al. (2005) `P1159` | [otimizacao.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/utils/otimizacao.py) | L328: `def w_min_cdar(...)` | **Implementado** (com correções numéricas de reescala) |
| **Black-Litterman Prior** | CAPM reverso $\Pi = \delta \Sigma w_m$ `P1172` | [otimizacao.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/utils/otimizacao.py) | L458: `S_anual`, L461: `DELTA * S_anual @ wm`| **Implementado** (com limitações de $w_m$ e $\delta$, ver Seção 3) |
| **Visões BL (Momentum)** | Sinais ex-ante via momentum 12-1 `P1178` | [otimizacao.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/utils/otimizacao.py) | L72: `def visoes_momentum(...)` | **Implementado** |
| **Fórmula Mestra BL** | Posterior $\mu_{BL}$ Bayesiano `P1186` | [otimizacao.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/utils/otimizacao.py) | L92: `def bl_posterior(...)` | **Implementado** |
| **Matriz $\Sigma_{BL}$ Posterior** | Incerteza $\Sigma_{BL} = \Sigma + ...$ `P905` | *Nenhum* | *Não calculada no pipeline* | **Divergente** (ver Seção 2) |
| **Calibração de Idzorek** | Calibração de $\Omega$ via confiança `P923` | *Nenhum* | *Não implementada* | **Não Implementado** (sugestão de extensão futuro, `P1353`) |
| **Modelos Fama-French** | Fatores FF3 (`P515`) e FF5 (`P527`) | *Nenhum* | *Não implementados* | **Não Implementado** (limitação metodológica tácita) |
| **Teste Spanning (HK)** | Huberman-Kandel (1987) spanning test | [inferencia.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/09_Inferencia_Econometrica/utils/inferencia.py) | L76: `def _wald_spanning(y, X_const)`| **Implementado** (Wald HAC) |
| **Teste Jobson-Korkie** | Comparação de Sharpe com Memmel (2003) | [inferencia.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/09_Inferencia_Econometrica/utils/inferencia.py) | L82: `def _jk_memmel(exc_a, exc_b)` | **Implementado** |
| **Ledoit-Wolf Bootstrap** | Teste de Sharpe por bootstrap (2008) | [inferencia.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/09_Inferencia_Econometrica/utils/inferencia.py) | L144: `def lw_bootstrap_sharpe(...)` | **Implementado** |

---

## 2. Análise Detalhada das Discrepâncias Críticas

### 2.1. Conflito Sharpe vs. Utilidade Média-Variância (`MaxSharpe`)

*   **O que diz a Prosa do TCC (`P1104`, `P1108`):**
    A tese afirma que a estratégia `MaxSharpe` maximiza uma *função de utilidade quadrática média-variância* ($U(w) = w'\mu - \frac{\delta}{2} w'\Sigma w$ com $\delta=3.0$). O autor afirma textualmente:
    > "Cabe a ressalva metodológica de que esta formulação não maximiza diretamente o Índice de Sharpe — problema não-convexo —, mas sim a utilidade média-variância, que produz o portfólio de tangência apenas sob condições específicas." (`P1108`)
*   **O que faz o Código (`otimizacao.py:L161-L200`):**
    O código **maximiza diretamente a razão de Sharpe clássica** (ou seja, $\frac{w'\mu - r_f}{\sqrt{w'\Sigma w}}$). O resolvedor SLSQP recebe a função objetivo `neg_sharpe` e utiliza a derivada exata (gradiente analítico) da razão de Sharpe pela regra do quociente.
*   **Impacto Teórico:**
    Há um descompasso epistemológico completo entre a prosa e o código. A prosa afirma que maximizar o Sharpe Ratio diretamente é inviável por não-convexidade e, portanto, resolve-se o problema quadrático (utilidade) com $\delta=3.0$. O código prova o contrário: maximiza diretamente o Sharpe através de otimização não-linear com restrições via SLSQP. A prosa precisa ser reescrita para refletir que a razão de Sharpe real foi maximizada diretamente, eliminando a menção incorreta à função de utilidade de $\delta=3.0$ e à não-convexidade intransponível.

### 2.2. Omissão da Incerteza Posterior de Black-Litterman ($\Sigma_{BL}$) no Otimizador

*   **O que diz a Prosa do TCC (`P905-P907`):**
    A tese descreve a covariância a posteriori de Black-Litterman ($\Sigma_{BL}$):
    $$\Sigma_{BL} = \Sigma + [(\tau\Sigma)^{-1} + P^T\Omega^{-1}P]^{-1}$$
    E define textualmente:
    > "A nova matriz de covariância a posteriori, que deve alimentar o otimizador, é: $\Sigma_{BL}$ ... Note que $\Sigma_{BL}$ é maior que a covariância histórica $\Sigma$. O modelo adiciona uma camada extra de risco, refletindo a incerteza epistêmica..." (`P905`, `P907`)
*   **O que faz o Código (`otimizacao.py:L461-L467`):**
    Durante a tarefa de rebalanceamento mensal, o código calcula `mu_bl` usando a função `bl_posterior` (que calcula corretamente o vetor posterior $\mu_{BL}$). Entretanto, ao chamar a otimização da carteira, o código executa:
    ```python
    alvos[f"BL_{nome}"] = w_max_sharpe(mu_bl, Sg, rf_a, None, w0=_w0.get(f"BL_{nome}"))
    ```
    Onde `Sg` é a **matriz de covariância a priori** (clássica anualizada ou a semicovariância de Estrada).
*   **Impacto Teórico:**
    A matriz de covariância posterior $\Sigma_{BL}$ que incorpora o termo de incerteza Bayesiana **nunca é calculada no pipeline e nunca alimenta o otimizador**. Isso significa que as carteiras do modelo Black-Litterman são formadas maximizando o Sharpe com base nos retornos a posteriori, mas usando o risco a priori (volatilidade e correlações históricas sem o acréscimo de incerteza). O código descumpre a teoria explicada no texto. Para alinhar os dois, ou o código deve ser alterado para computar e usar $\Sigma_{BL}$ (o que alteraria ligeiramente os resultados numéricos do TCC), ou o texto deve admitir que, por simplicidade e estabilidade numérica, utilizou-se apenas o vetor de retornos atualizado pelo BL e manteve-se a covariância original na otimização.

---

## 3. Lacunas de Implementação e Limitações

### 3.1. Ausência Física dos Modelos Multifatoriais (Fama-French)
Os modelos de 3 fatores (Fama-French, 1993) e 5 fatores (Fama-French, 2015) são amplamente descritos na teoria (`P515`, `P527`), apresentando seus fundamentos econômicos (prêmios de Tamanho, Valor, Lucratividade e Investimento). No entanto:
*   Não há qualquer regressão de fatores, banco de dados de fatores ou otimização fatorial implementada no código.
*   O modelo Black-Litterman utiliza apenas o sinal de momentum 12-1 de forma direta nas cotações históricas, sem extrair os betas fatoriais de Fama-French.
*   **Recomendação:** O texto deve deixar mais explícito que o referencial teórico discute Fama-French como o estado da arte em precificação multifatorial de mercado (para contrapor ao CAPM), mas que a implementação física do TCC limita-se à abordagem unifatorial clássica e ao momentum técnico direto na alocação Bayesiana.

### 3.2. Calibração de Confiança de Idzorek
O algoritmo de Idzorek (2005) para engenharia reversa da matriz de incerteza das visões $\Omega$ baseado em "confiança de 0% a 100%" é detalhado matematicamente (`P921-P931`). Contudo:
*   O código utiliza o método de proporcionalidade estrita de He & Litterman (1999): $\Omega = \text{diag}(P(\tau\Sigma)P^T)$, com limite inferior de $10^{-8}$.
*   **Consistência:** Esta lacuna está declarada de forma correta e explícita no texto final sob as sugestões de pesquisa futura (`P1353`), não constituindo um erro, mas sim uma limitação voluntária do escopo implementado.

---

## Seção "NÃO VERIFICADO"

*   **Implementações históricas deletadas:** Não foi verificado se versões anteriores do código continham o cálculo de Fama-French ou a matriz $\Sigma_{BL}$ antes da consolidação do pipeline atual na branch `tcc-aprimoramento`. A análise foi realizada estritamente sobre a versão atual presente nos arquivos de código do workspace.
