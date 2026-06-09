# Setup da Fase P0 — Guardrails e Regressão Numérica

**TCC:** Moderna Teoria das Carteiras no Mercado de Ações Brasileiro  
**Autor:** Pedro Augusto Pinheiro Reis | UFG — Ciências Contábeis  
**Data:** 2026-06-09  
**Branch:** `tcc-aprimoramento`  
**Baseline Git Tag:** `entrega-12-submetida`

---

## 1. Artefatos Criados no Setup

Todos os guardrails e arquivos de orquestração de testes numéricos previstos na Fase P0 foram implementados:

1.  **Invariantes de Projeto:** Acrescentados com sucesso ao final de [CLAUDE.md](file:///C:/VSCodeWorkspace/1_TCC_Final/CLAUDE.md), listando de forma explícita os parâmetros metodológicos canônicos, o universo de 102 ativos investíveis, as 16 estratégias sob teste, regras de não-escrita e o gate numérico de validação.
2.  **Agentes de Auditoria Customizados (Fases Read-Only):**
    *   [.claude/agents/auditor-codigo.md](file:///C:/VSCodeWorkspace/1_TCC_Final/.claude/agents/auditor-codigo.md): Para auditoria de bugs e problemas de solver.
    *   [.claude/agents/auditor-texto.md](file:///C:/VSCodeWorkspace/1_TCC_Final/.claude/agents/auditor-texto.md): Para análise de formatação ABNT e consistência textual-numérica.
    *   [.claude/agents/conferente-referencias.md](file:///C:/VSCodeWorkspace/1_TCC_Final/.claude/agents/conferente-referencias.md): Para reconciliação de citações e referências bibliográficas.
    *   [.claude/agents/rastreador-teoria.md](file:///C:/VSCodeWorkspace/1_TCC_Final/.claude/agents/rastreador-teoria.md): Para a matriz de rastreabilidade teoria-implementação.
3.  **Hooks de Proteção de Escrita:**
    *   [.claude/hooks/protege.sh](file:///C:/VSCodeWorkspace/1_TCC_Final/.claude/hooks/protege.sh): Script shell com permissão de execução (`chmod +x`) que bloqueia alterações no diretório protegido `data/` e em tags preservadas.
    *   [.claude/settings.json](file:///C:/VSCodeWorkspace/1_TCC_Final/.claude/settings.json): Registra o hook `PreToolUse` para interceptar comandos que modifiquem os caminhos protegidos.
4.  **Base de Regressão Numérica (Golden Master):**
    *   [docs/auditoria/golden_master.json](file:///C:/VSCodeWorkspace/1_TCC_Final/docs/auditoria/golden_master.json): Compilado a partir das saídas existentes em disco.
5.  **Script Orquestrador de Regressões:**
    *   [docs/auditoria/revalidar.py](file:///C:/VSCodeWorkspace/1_TCC_Final/docs/auditoria/revalidar.py): Executa apenas as etapas afetadas a jusante de qualquer mudança de código e compara as novas métricas e dimensões contra o Golden Master (com tolerância relativa estrita de $10^{-6}$).

---

## 2. Veredito sobre o `src/test_pipeline.py`

Inspecionamos detalhadamente a suíte de testes existente em [test_pipeline.py](file:///C:/VSCodeWorkspace/1_TCC_Final/src/test_pipeline.py) para determinar sua abrangência (comparação de valores vs. consistência dimensional/financeira geral):

*   **Veredito:** **O script atual valida apenas Dimensões, Sanidade e Contratos, mas NÃO compara valores financeiros específicos (Sharpe/CAGR) das estratégias.**
*   **Mapeamento por linha de código:**
    *   `test_static_imports()` ([L31-70](file:///C:/VSCodeWorkspace/1_TCC_Final/src/test_pipeline.py#L31-L70)): Verifica de forma estática se as importações de utilitários nos notebooks Jupyter apontam para arquivos locais válidos e existentes nas subpastas locais.
    *   `test_config_resolution()` ([L73-105](file:///C:/VSCodeWorkspace/1_TCC_Final/src/test_pipeline.py#L73-L105)): Altera temporariamente a configuração central (`K_MAD`) para assegurar que todas as etapas resolvem o arquivo `src/config.json` de forma dinâmica.
    *   `test_data_consistency()` ([L108-147](file:///C:/VSCodeWorkspace/1_TCC_Final/src/test_pipeline.py#L108-L147)): Garante o alinhamento dimensional dos tickers investíveis (matriz de preços) e valida a presença de dados macro do painel (como taxas livres de risco de referência).
    *   `test_math_assertions()` ([L150-185](file:///C:/VSCodeWorkspace/1_TCC_Final/src/test_pipeline.py#L150-L185)): Valida a finitude dos dados e se a identidade matemática geométrica básica do retorno de log é atendida ($r_{log} = \ln(1+R_{simples})$).
    *   `test_covariance_regularization()` ([L188-250](file:///C:/VSCodeWorkspace/1_TCC_Final/src/test_pipeline.py#L188-L250)): Valida a consistência teórica da matriz de covariância regularizada (Ledoit-Wolf) por meio de simetria, posto completo, autovalores estritamente positivos ($\lambda_{min} > 10^{-8}$) e conservação do traço estatístico.
    *   `test_backtest_outputs()` ([L255-301](file:///C:/VSCodeWorkspace/1_TCC_Final/src/test_pipeline.py#L255-L301)): Assegura que todas as 16 estratégias de simulação foram geradas e que os arquivos de pesos e retornos não estão vazios.
    *   `test_portfolio_constraints()` ([L304-334](file:///C:/VSCodeWorkspace/1_TCC_Final/src/test_pipeline.py#L304-L334)): Testa se as carteiras respeitam o orçamento de pesos somando 100%, o regime estrito long-only ($w_i \ge 0$) e os limites regulatórios de concentração de teto de 10% (CVM 175) aplicados às estratégias correspondentes.
    *   `test_efficient_frontier()` ([L338-358](file:///C:/VSCodeWorkspace/1_TCC_Final/src/test_pipeline.py#L338-L358)) e `test_econometric_inference()` ([L362-389](file:///C:/VSCodeWorkspace/1_TCC_Final/src/test_pipeline.py#L362-L389)): Apenas validam a existência dos CSVs e se os p-valores econométricos (Jobson-Korkie/CAPM) estão no domínio matemático lógico de $[0, 1]$.

**Conclusão:** Não existe nenhuma comparação de tolerância numérica para métricas financeiras finais (como Sharpe de 0,6110 para o Black-Litterman clássico) nesta suíte. Por isso, a criação do validador `revalidar.py` vs. `golden_master.json` é de extrema relevância, pois impede que alterações posteriores nos scripts de otimização distorçam os resultados sem que a auditoria detecte.

---

## 3. Conteúdo Consolidado do Golden Master

As métricas numéricas extraídas e gravadas em `docs/auditoria/golden_master.json` que agora servem como target numérico são:

### Mapeamento das 16 Estratégias + IBOV (Período OOS: 2015-03-02 a 2025-12-30)

| Estratégia | CAGR (ret_anual) | Volatilidade | Sharpe | Sortino | Max Drawdown | Turnover Anual |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **EqualWeight** | 13.91% | 19.56% | 0.2902 | 0.4027 | -35.54% | 0.8293 |
| **InvVol** | 14.65% | 18.90% | 0.3276 | 0.4554 | -34.28% | 0.7881 |
| **MinVar** | 13.00% | 12.95% | 0.2931 | 0.4003 | -25.05% | 0.8009 |
| **MinVar_c10** | 13.17% | 12.98% | 0.3044 | 0.4154 | -25.00% | 0.7856 |
| **MaxSharpe** | 13.96% | 17.54% | 0.3046 | 0.4302 | -22.76% | 1.2187 |
| **MaxSharpe_c10** | 12.99% | 16.54% | 0.2606 | 0.3649 | -23.89% | 1.5076 |
| **MaxOmega** | 10.71% | 21.23% | 0.1487 | 0.2103 | -30.67% | 2.2408 |
| **MaxSortino** | 13.53% | 17.79% | 0.2812 | 0.3973 | -23.26% | 1.3100 |
| **MaxKappa3** | 13.64% | 18.26% | 0.2843 | 0.4029 | -22.55% | 1.3375 |
| **MinCVaR** | 12.57% | 12.88% | 0.2644 | 0.3626 | -26.44% | 1.1056 |
| **MinCDaR** | 5.36% | 19.82% | -0.1050 | -0.1454 | -62.46% | 1.4735 |
| **BL_classico** | 24.31% | 25.97% | 0.6110 | 0.8902 | -38.93% | 7.9819 |
| **BL_classico_c10** | 20.44% | 20.20% | 0.5632 | 0.7916 | -33.60% | 6.2942 |
| **BL_downside** | 22.91% | 32.17% | 0.5138 | 0.7532 | -57.41% | 9.4819 |
| **BL_downside_c10** | 16.87% | 22.30% | 0.3951 | 0.5543 | -38.01% | 7.3287 |
| **IBOV** | 11.26% | 23.32% | 0.1777 | 0.2445 | -46.82% | - |
| **EqualWeight_BuyHold** | 17.28% | 19.28% | 0.4429 | 0.6206 | -33.00% | 0.0000 |

### Dimensões de Arquivos de Referência (Shapes)
*   **Matriz_precos_sanitizada.csv:** `[3967, 103]` (102 ativos + index)
*   **painel_alinhado.csv:** `[3967, 106]` (102 ativos + benchmarks + index)
*   **retornos_simples_saneado.parquet:** `[3966, 102]`
*   **retornos_log_saneado.parquet:** `[3966, 102]`
*   **sigma_amostral_anual.parquet:** `[102, 102]`
*   **sigma_ledoitwolf_anual.parquet:** `[102, 102]`
*   **strategy_returns.parquet:** `[2690, 17]` (16 estratégias + IBOV)
*   **pesos_historico.csv:** `[55159, 4]`

### Hashes dos Arquivos de Entrada e Universo
*   `universo_pos_liquidez.csv` $\rightarrow$ `8dfaa7d6f3b938b1ec2535dd2dfb38af`
*   `tickers_finais.csv` $\rightarrow$ `6db82eac5dba2f840b897ace1421c8a3`
*   `tickers_excluidos_integridade.csv` $\rightarrow$ `514dab9d5e396b5e758582d8b50fc6e3`

---

## 4. Validação da Infraestrutura
O script de validação foi testado em modo de verificação de conformidade:
```bash
python docs/auditoria/revalidar.py --check-only
```
O resultado obteve **100% de PASS** em todas as métricas e dimensões de shape, confirmando que a infraestrutura de validação está pronta e calibrada.
