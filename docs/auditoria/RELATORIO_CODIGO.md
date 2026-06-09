# Relatório de Auditoria de Código (Fase P1)

**TCC:** Moderna Teoria das Carteiras no Mercado de Ações Brasileiro  
**Autor:** Pedro Augusto Pinheiro Reis | UFG — Ciências Contábeis  
**Data:** 2026-06-09  
**Branch:** `tcc-aprimoramento`  
**Auditor:** Gemini (Antigravity)

---

## 1. Sumário Executivo

A auditoria estática do código-fonte mapeou 33 arquivos sob `src/` e subpastas de utilitários, além das configurações de ambiente. Foram encontrados problemas críticos de **duplicação de lógica quantitativa**, **inconsistência no tratamento de solvers convexos** e **dependências de ambiente infladas e desnecessárias**. As correções propostas elevam a robustez do pipeline a nível de produção científica sem alterar as invariantes de resultados já consolidados.

---

## 2. Catálogo e Mapeamento de Arquivos Python (`src/` e `utils/`)

| Arquivo | Propósito | Inputs Principais | Outputs Principais | Parâmetros-chave (Valores e Linhas) |
| :--- | :--- | :--- | :--- | :--- |
| [generate_pipeline_doc.py](file:///C:/VSCodeWorkspace/1_TCC_Final/src/generate_pipeline_doc.py) | Gerador de documentação automática do pipeline. | Comentários e markdown das células dos notebooks. | `RELATORIO_ESTADO_PIPELINE.md` | `max_length = 80` |
| [run_etapa03.py](file:///C:/VSCodeWorkspace/1_TCC_Final/src/run_etapa03.py) | Orquestração da liquidez e integridade. | `dados_brutos_economatica.parquet` | Universo sanitizado em `.csv` | `PERCENTIL_LIQUIDEZ = 0.1` |
| [run_pipeline.py](file:///C:/VSCodeWorkspace/1_TCC_Final/src/run_pipeline.py) | Orquestrador central com cache inteligente MD5. | Códigos dos notebooks e dependências. | Execução inplace de notebooks. | `pipeline_stages` (L17), `cache_path` (L213) |
| [test_pipeline.py](file:///C:/VSCodeWorkspace/1_TCC_Final/src/test_pipeline.py) | Suite de testes de integração e sanidade física. | Arquivos de dados sob `data/`. | Log de sucesso (Exit 0) ou falha (Exit 1). | `K_MAD = 999.0` temporário (L83) |
| [worker.py](file:///C:/VSCodeWorkspace/1_TCC_Final/src/01_Conversao_Parquet/worker.py) | Conversor paralelo de Excel para Parquet. | Planilhas Excel da B3 (`.xlsx`). | Tabelas `.parquet` intermediárias. | `max_workers` do CPU (L14) |
| [filtros.py](file:///C:/VSCodeWorkspace/1_TCC_Final/src/03_Filtro_Liquidez/utils/filtros.py) | Rotinas de presença, IPO e liquidez longitudinal ADTV. | DataFrames de preços e volumes. | Tickers aprovados e reprovados. | `limiar = 0.95` (L8) |
| [auditoria_taxas.py](file:///C:/VSCodeWorkspace/1_TCC_Final/src/04_Taxas_Livres_Risco/utils/auditoria_taxas.py) | Validador de consistência de datas e taxas CDI/Selic. | `rf_diario.csv` | Asserções no log. | `tolerancia_gap = 5` |
| [conversoes.py](file:///C:/VSCodeWorkspace/1_TCC_Final/src/04_Taxas_Livres_Risco/utils/conversoes.py) | Converte taxas Selic meta/over e CDI de base diária/anual. | Taxas brutas. | Taxas convertidas equivalentes. | `DIAS_UTEIS = 252` |
| [sgs_api.py](file:///C:/VSCodeWorkspace/1_TCC_Final/src/04_Taxas_Livres_Risco/utils/sgs_api.py) | Conexão HTTP com a API do Banco Central (SGS). | Códigos de séries do BCB. | DataFrame de taxas históricas. | `limite_retries = 3` |
| [alinhamento.py](file:///C:/VSCodeWorkspace/1_TCC_Final/src/05_Alinhamento_Winsorizacao/utils/alinhamento.py) | Alinha séries temporais de ativos de cotação com a Selic/CDI. | Matriz de preços e taxas. | DataFrames alinhados de retornos simples/log. | `DATA_INICIO`, `DATA_FIM` |
| [winsorizacao.py](file:///C:/VSCodeWorkspace/1_TCC_Final/src/05_Alinhamento_Winsorizacao/utils/winsorizacao.py) | Truncamento robusto de caudas via MAD. | Retornos de ativos. | Retornos saneados e relatório de cercas. | `k = 3.5` (L14), `c = 0.6745` (L15) |
| [covariancia.py](file:///C:/VSCodeWorkspace/1_TCC_Final/src/06_Estimacao_Covariancia/utils/covariancia.py) | Estimadores amostrais e regularização Ledoit-Wolf (LW). | Retornos simples saneados. | Matriz de covariância anualizada. | `ledoit_wolf` (L17), `metodo = ledoit_wolf` (L66) |
| [otimizacao.py](file:///C:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/utils/otimizacao.py) | Otimizadores matemáticos das carteiras MPT/PMPT. | Retornos simples, covariâncias, MAR. | Vetores de pesos e retornos BL. | `_CVXPY_TOL = 1e-4` (L21), `_TOL_TAIL = 1e-6` (L26) |
| [fronteira.py](file:///C:/VSCodeWorkspace/1_TCC_Final/src/08_Fronteira_Eficiente/utils/fronteira.py) | Geração de fronteiras eficientes MPT/PMPT. | Retornos simples, covariâncias, retornos BL. | Curvas de pontos e pesos de fronteira. | `min_cvar` (L77) |
| [inferencia.py](file:///C:/VSCodeWorkspace/1_TCC_Final/src/09_Inferencia_Econometrica/utils/inferencia.py) | Testes econométricos e calibração de Bootstrap. | Retornos de estratégias, taxa livre de risco. | p-valores e estatísticas de teste. | `reps = 2000` (L144), `bloco = 10` (L144) |

---

## 3. Diagnóstico de Defeitos por Severidade

### 🔴 Alta Severidade

1.  **Duplicação de Código Matemático Central (Ledoit-Wolf)**
    *   **Arquivo/Linhas:** 
        *   [covariancia.py:L17](file:///C:/VSCodeWorkspace/1_TCC_Final/src/06_Estimacao_Covariancia/utils/covariancia.py#L17)
        *   [otimizacao.py:L29](file:///C:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/utils/otimizacao.py#L29)
        *   [fronteira.py:L12](file:///C:/VSCodeWorkspace/1_TCC_Final/src/08_Fronteira_Eficiente/utils/fronteira.py#L12)
    *   **Defeito:** O algoritmo vetorizado clássico de Ledoit & Wolf (2004) está inteiramente copiado e colado em 3 arquivos de utilitários diferentes. Pior ainda, a assinatura e retorno em `covariancia.py` é `return Sigma_shrunk, delta` (retorna tupla com matriz e intensidade de encolhimento), enquanto nos arquivos `otimizacao.py` e `fronteira.py` ela retorna apenas a matriz (`return delta * F + (1.0 - delta) * S`).
    *   **Impacto:** Risco severo de divergências e manutenção difícil se a matemática de encolhimento precisar ser atualizada ou corrigida.

2.  **Aceitação de Status `optimal_inaccurate` em CVXPY na Fronteira**
    *   **Arquivo/Linha:** [fronteira.py:L104](file:///C:/VSCodeWorkspace/1_TCC_Final/src/08_Fronteira_Eficiente/utils/fronteira.py#L104)
    *   **Defeito:** Na resolução do CVaR na fronteira eficiente, o código aceita `optimal_inaccurate` sem emitir warnings ou aplicar fallbacks: `if prob.status in ("optimal", "optimal_inaccurate"): break`. No entanto, em `otimizacao.py:L327`, o `optimal_inaccurate` é expressamente rejeitado para evitar alocações degeneradas ou corrupções numéricas nos backtests.
    *   **Impacto:** Risco de propagar pesos corrompidos para os pontos da curva de fronteira se o solver convexos sofrer de mal-condicionamento em ativos de crescimento extremo.

---

### 🟡 Média Severidade

1.  **Requirements com Dependências Pesadas não Utilizadas**
    *   **Arquivo:** [requirements.txt](file:///C:/VSCodeWorkspace/1_TCC_Final/requirements.txt)
    *   **Defeito:** Os pacotes `tensorflow>=2.12`, `keras>=2.12` e `hmmlearn>=0.3` estão listados como requerimentos obrigatórios para o ambiente, porém não há nenhuma chamada ou importação a eles em nenhum dos arquivos do código-fonte do pipeline sob `src/`.
    *   **Impacto:** Inchaço massivo do ambiente de dependências Python, exigindo download e compilação de bibliotecas pesadas de machine learning que não são usadas pelo TCC.

2.  **Parâmetros de Bootstrap Não-Unificados**
    *   **Arquivo/Linha:** [inferencia.py:L114](file:///C:/VSCodeWorkspace/1_TCC_Final/src/09_Inferencia_Econometrica/utils/inferencia.py#L114)
    *   **Defeito:** A função `bootstrap_ic` possui assinatura `seed=7` hardcoded por padrão, enquanto os estimadores de intervalo de confiança de Sharpe de Ledoit-Wolf (`lw_bootstrap_sharpe`) usam `seed=42`. Além disso, a contagem de repetições `B=2000` está declarada diretamente no código em vários pontos, em vez de carregar do `config.json` de forma uniforme.
    *   **Impacto:** Reduz a manutenibilidade e dificulta testes alternativos de sensibilidade.

---

### 🟢 Baixa Severidade

1.  **requirements.txt com Operadores de Piso (>=) em vez de Fixação (==)**
    *   **Arquivo:** [requirements.txt](file:///C:/VSCodeWorkspace/1_TCC_Final/requirements.txt)
    *   **Defeito:** As versões das dependências são declaradas como pisos mínimos de compatibilidade (`pandas>=2.0`) em vez de versões estritamente fixadas (`pandas==2.2.2`).
    *   **Impacto:** Pode comprometer a reprodutibilidade futura caso novas versões introduzam quebras de API ou discrepâncias em estimadores estatísticos (ex: scipy/numpy).

2.  **Duplicação de Otimizadores SLSQP sem Gradientes em `fronteira.py`**
    *   **Arquivo:** [fronteira.py:L51-75](file:///C:/VSCodeWorkspace/1_TCC_Final/src/08_Fronteira_Eficiente/utils/fronteira.py#L51-L75)
    *   **Defeito:** O arquivo `fronteira.py` reimplementa as otimizações `min_var` e `max_sharpe` sem utilizar os gradientes analíticos (Jacobiano) nem o warm-start desenvolvidos em `otimizacao.py` (Proposta 1 e 2).
    *   **Impacto:** Os cálculos de pontos de fronteira por Monte Carlo ou otimização iterativa rodam de forma mais lenta do que poderiam se importassem e reutilizassem a lógica otimizada de `otimizacao.py`.

---

## 4. Reprodutibilidade e Determinismo

*   **Reprodutibilidade das Séries Temporais:** O pipeline é altamente determinístico. Todas as funções que lidam com amostragem estocástica (como bootstrapping no `inferencia.py` e simulação na fronteira) recebem sementes explícitas (`seed`) configuradas na inicialização ou extraídas de `config.json` (`SEED = 42`).
*   **Fontes de Não-Determinismo Mitigadas:** A única fonte potencial de variação exógena seria a atualização retroativa ou indisponibilidade de dados da API SGS do Banco Central (Etapa 4). Isso é blindado na execução ordinária pelo orquestrador de cache baseado no hash MD5 do código, que evita re-execuções desnecessárias a menos que os códigos ou dependências sejam de fato modificados.

---

## 5. Oportunidades de Refatoração

1.  **Unificação do Ledoit-Wolf:** Remover as cópias de `ledoit_wolf` sob `otimizacao.py` e `fronteira.py`, centralizando-o em `covariancia.py`. Importar e utilizar `from utils.covariancia import ledoit_wolf` onde necessário, ajustando o código para ler o primeiro elemento da tupla de retorno.
2.  **Harmonização da Otimização:** Fazer com que `fronteira.py` importe as funções otimizadas de `otimizacao.py` (usufruindo de gradientes analíticos e warm-start), eliminando a duplicação ineficiente de solvers.
3.  **Remoção de Pacotes Mortos:** Excluir `tensorflow`, `keras` e `hmmlearn` do [requirements.txt](file:///C:/VSCodeWorkspace/1_TCC_Final/requirements.txt) para higienizar o ambiente.

---

## 6. Decisão Pendente — MinCDaR em `otimizacao.py`

### Contexto do Problema
O estimador CDaR original do TCC utilizava um processo de riqueza aditivo baseado na soma cumulativa de retornos (`cumsum`). Em janelas expansivas de simulação longas (10 a 15 anos), a magnitude dos preços acumulados de ativos com forte tendência de alta (como `UNIP6`) estourava os limites de estabilidade numérica, fazendo com que o solver linear do CVXPY (Clarabel/ECOS) reportasse falha ou o status degradado `optimal_inaccurate`. Sem travas adicionais, os pesos degenerados eram propagados ao backtest, gerando drawdowns artificiais severos na simulação ( drawdowns que batiam $-84\%$).

### A Solução Aplicada
Para mitigar isso de forma rigorosa, foram introduzidas correções em `otimizacao.py`:
1.  **Processo Multiplicativo:** Substituição por `np.cumprod(1 + R)` para se alinhar fielmente ao cálculo geométrico de drawdown percentual out-of-sample.
2.  **Reescala de Condicionamento:** Divisão da riqueza pelo máximo global observável da janela (`Rcum / G`), mantendo o argmin (pesos ótimos) inalterado, mas trazendo as magnitudes para ordem de $O(1)$.
3.  **Rejeição Estrita de Inacurácia:** Exigência de que o solver atinja status `optimal`. Caso falhe ou caia em `optimal_inaccurate`, a função levanta um erro controlado e cai de volta para a carteira de pesos iguais (`EqualWeight`).

### Opções de Decisão

*   **Opção A (Recomendada — Manter Lógica Corrigida):**
    *   *Benefícios:* Garante correção teórica estrita (drawdown geométrico clássico) e segurança numérica de solvers (zero propagação de pesos corrompidos).
    *   *Impacto:* Os retornos obtidos da estratégia CDaR são baixos no mercado brasileiro (CAGR de 5,36% a.a. e Sharpe de -0,1050), o que exige que o autor ajuste as passagens de texto que comparavam a performance de forma diferente na versão preliminar da entrega.
*   **Opção B (Reverter para Lógica Aditiva e Aceitar `optimal_inaccurate`):**
    *   *Benefícios:* Mantém os números da simulação originais sem exigir que o texto do TCC seja reescrito nessa seção.
    *   *Custos:* Propaga um erro metodológico de cálculo de drawdown e assume como válidas otimizações que o próprio solver CVXPY declara numericamente inacuradas.

---

*O relatório detalhado está disponível em [RELATORIO_CODIGO.md](file:///C:/VSCodeWorkspace/1_TCC_Final/docs/auditoria/RELATORIO_CODIGO.md) para análise e decisões de gates antes da Fase P2.*
