# Moderna Teoria das Carteiras no Mercado de Ações Brasileiro

**Autor:** Pedro Augusto Pinheiro Reis  
**Instituição:** Universidade Federal de Goiás (UFG) — Ciências Contábeis  
**Título oficial:** Moderna Teoria das Carteiras no Mercado de Ações Brasileiro: Comparação entre Otimizadores e Inputs

---

## Sobre o projeto

Trabalho de Conclusão de Curso que compara estratégias de otimização de portfólios aplicadas ao mercado brasileiro (B3), utilizando dados de 130 ativos entre 2010 e 2025.

### Estratégias implementadas

| Estratégia | Retorno acumulado (out-of-sample) | Turnover médio |
|---|---|---|
| Mínima Variância com regularização L1 | +460% | 0,32%/mês |
| Máximo Índice de Sharpe com L1 | +240% | 4,29%/mês |
| Black-Litterman + LSTM + Fatores FF5 | +56% | ~55%/mês |
| IBOV (benchmark) | +215% | — |
| CDI (referência) | +166–171% | — |

---

## Estrutura do repositório

```
├── data/          Dados brutos e processados (preços, CDI, IBOV, SELIC, fatores NEFIN)
├── src/           Notebooks do pipeline de otimização
├── results/       Curvas de capital, tabelas de métricas e gráficos
├── doc/           Documento TCC (entregas)
├── scratch/       Experimentos e rascunhos
└── requirements.txt
```

---

## Como reproduzir

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

> Python 3.10+ recomendado. TensorFlow/Keras requer Python ≤ 3.11.

### 2. Executar o pipeline base (obrigatório)

```
1_Sanitizacao_Dados.ipynb
2_1_Matriz_de_Retornos.ipynb
3_1_Merge_B3_CDI_SELIC.ipynb
4_Calculo_Premio_Risco.ipynb
5_Matriz_Covariancia_KPIs.ipynb
```

### 3. Executar as estratégias

- **Mínima Variância L1:** notebooks `14_2_1` → `14_2_4`
- **Máximo Sharpe L1:** notebooks `14_1_1` → `14_1_4`
- **Black-Litterman + LSTM:** notebooks `17_*` → `18_*` → `19_*`

---

## Referências principais

- Markowitz (1952) — *Journal of Finance* — fundação da MPT
- Black & Litterman (1992) — *Financial Analysts Journal* — modelo BL
- He & Litterman (1999) — Goldman Sachs WP — calibração delta/tau
- DeMiguel, Garlappi & Uppal (2009) — *Review of Financial Studies* — por que Min Variância vence
- Santos & Tessari (2012) — *RBFin* — otimização na B3
