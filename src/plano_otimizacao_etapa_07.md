# Plano de Otimização da Etapa 07 (Otimização de Carteiras)

Este plano descreve as alterações propostas no notebook [07_01_Otimizacao_Carteiras.ipynb](file:///c:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/07_01_Otimizacao_Carteiras.ipynb) e seu script auxiliar [otimizacao.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/utils/otimizacao.py) para reduzir drasticamente o tempo de execução (de ~35 minutos para menos de 3 minutos), sem alterar os resultados matemáticos finais do TCC.

## User Review Required

> [!IMPORTANT]
> **Preservação dos Resultados Metodológicos:**
> Todas as propostas foram validadas matematicamente (erro flutuante inferior a $10^{-8}$ nos testes de gradiente). A única alteração que pode causar micro-divergências marginais (na 4ª ou 5ª casa decimal) é o ajuste de tolerância nos solvers convexos (de `1e-5` para `1e-4`). Como o teto regulatório CVM 175 é de 10% (0,10), essa alteração não afeta a conformidade fiduciária das carteiras e acelera substancialmente o tempo de convergência.

## proposed Changes

Otimizaremos as rotinas matemáticas no arquivo de funções utilitárias e ajustaremos o notebook para carregar os dados em memória e repassar fatias (*slices*) de arrays NumPy pré-calculados para os trabalhadores paralelos, em vez de fazer I/O de disco repetitivo em cada processo.

---

### Componente: Otimização Matemática e I/O de Processos

#### [MODIFY] [otimizacao.py](file:///c:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/utils/otimizacao.py)
* **Gradientes Analíticos (`jac`):**
  * Modificar `w_min_var` para incluir a derivada analítica da variância do portfólio: $\nabla f(w) = 2 \boldsymbol{\Sigma} w$.
  * Modificar `w_max_sharpe` para incluir a derivada analítica do Índice de Sharpe:
    $$\nabla f(w) = -\frac{\boldsymbol{\mu} (w^T \boldsymbol{\Sigma} w) - (w^T \boldsymbol{\mu} - r_f) \boldsymbol{\Sigma} w}{(w^T \boldsymbol{\Sigma} w)^{1.5}}$$
  * Modificar `w_max_kappa` para incluir a derivada analítica exata das medidas Kappa (de ordens 1, 2 e 3) calculada a partir do limite condicional do downside.
* **Eliminar I/O Repetitivo na Task:**
  * Alterar a assinatura e a implementação da função `otimizar_mes_task(args)` para receber arrays NumPy pré-fatiados (`Jv`, `S`, `SigD`, `mu`, `rf_a`, `mar_d`) em vez de strings de caminhos e parâmetros de leitura de arquivo.
* **Ajuste de Tolerância no CVXPY:**
  * Modificar `w_min_cvar` e `w_min_cdar` para utilizar tolerância de gap absoluto/relativo de `1e-4` no solver Clarabel/ECOS.

#### [MODIFY] [07_01_Otimizacao_Carteiras.ipynb](file:///c:/VSCodeWorkspace/1_TCC_Final/src/07_Otimizacao_Carteiras/07_01_Otimizacao_Carteiras.ipynb)
* **Preparação Centralizada dos Dados:**
  * Alterar o loop de preparação de `tarefas_args` (Célula 20) para fatiar `ret` e `rf` localmente no processo pai e empacotar diretamente os arrays NumPy necessários de cada iteração.
  * Remover os parâmetros redundantes de caminhos físicos (`str(DIR_RETORNOS)`) e métodos de covariância que eram recalculados a cada iteração de forma ineficiente pelos filhos.

---

## Verification Plan

### Automated Tests
* Executar a suíte de testes de integridade `test_pipeline.py` para garantir que os novos pesos das carteiras cumprem rigorosamente com todos os contratos matemáticos e restrições regulatórias da CVM 175:
  ```powershell
  python src/test_pipeline.py
  ```
* Validar que os pesos das carteiras otimizadas são idênticos aos anteriores e que a identidade de orçamento ($\sum w_i = 1$) e o limite de peso ($w_i \le 10\%$ nas carteiras limitadas) persistem.

### Manual Verification
* Comparar o tempo de execução total da etapa 7 antes (~2117 segundos) e após a implementação da aceleração para certificar o ganho de velocidade.
