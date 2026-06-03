# CLAUDE.md — Guia de Desenvolvimento do TCC (1_TCC_Final)

Este arquivo descreve os comandos de execução comuns, a estrutura de diretórios, as convenções de código e os padrões de teste estabelecidos durante a auditoria do pipeline de otimização de carteiras.

---

## 🚀 Comandos de Execução Frequentes

### 1. Executando o Pipeline Completo
O pipeline é orquestrado por um script central com cache inteligente baseado no hash MD5 do código das células dos notebooks e de seus arquivos de dependência:
```bash
python src/run_pipeline.py
```
*Nota: Se os notebooks ou as dependências não forem alterados e as saídas existirem, o orquestrador pulará a execução da etapa automaticamente.*

### 2. Executando os Testes Automatizados (pytest)
Os testes estão localizados na pasta `tests/` e são configurados via `pytest.ini` e `tests/conftest.py`.

- **Apenas testes rápidos (~5 segundos):**
  ```bash
  python -m pytest -m "not slow" -v --tb=short
  ```
- **Todos os testes, incluindo Monte Carlo lento (~3-5 minutos):**
  ```bash
  python -m pytest -v
  ```

### 3. Gerenciamento do Ambiente e Dependências
- Instalação de dependências:
  ```bash
  pip install -r requirements.txt
  ```
- Versão do Python recomendada: `>= 3.10`

---

## 📁 Estrutura do Projeto

```
1_TCC_Final/
├── data/                      # Dados de entrada, saídas intermediárias e finais do pipeline
├── docs/                      # Relatórios da auditoria, arquitetura e achados do projeto
├── pytest.ini                 # Configurações do Pytest (ex. marcação de testes lentos)
├── requirements.txt           # Dependências do Python
├── src/                       # Código-fonte principal do pipeline
│   ├── config.json            # Parâmetros de execução centralizados e compartilhados
│   ├── run_pipeline.py        # Orquestrador das etapas de execução dos notebooks
│   ├── test_pipeline.py       # Testes de integridade do pipeline executados pelo orquestrador
│   ├── 01_Conversao_Parquet/  # Notebooks/Scripts para conversão dos inputs de dados
│   ├── 02_Consolidacao_Dados/ # Consolidação em painel MultiIndex
│   ├── 03_Filtro_Liquidez/    # Aplicação de filtros e sanitização de liquidez B3
│   ├── 04_Taxas_Livres_Risco/ # Ingestão e alinhamento do CDI/Selic diários
│   ├── 05_Alinhamento_Winsor/ # Alinhamento temporal e saneamento/winsorização de outliers
│   ├── 06_Estimacao_Covari/   # Estimação clássica e regularizada (Ledoit-Wolf) de covariância
│   ├── 07_Otimizacao_Carteir/ # Otimização MPT/PMPT com restrições e custos transacionais
│   ├── 08_Fronteira_Eficiente/# Geração da fronteira eficiente e simulação Monte Carlo
│   └── 09_Inferencia_Economi/ # Testes de hipóteses, bootstrap de Sharpe e regressões CAPM/HAC
└── tests/                     # Suíte completa de testes unitários e de integração
    ├── conftest.py            # Adiciona os diretórios 'utils' do src ao sys.path
    ├── test_backtest_integ.py # Testes de integração do loop de backtest
    ├── test_black_litterman.py# Validação matemática das fórmulas de Black-Litterman
    ├── test_estimadores.py    # Corretude de estimadores de covariância e semicovariância
    ├── test_inferencia_calib.py# Testes da calibração bootstrap, size/power de Monte Carlo
    ├── test_metricas.py       # Validação das métricas de risco e retornos (Sharpe, Sortino, MaxDD, etc.)
    └── test_otimizadores.py   # Testes matemáticos dos solvers de otimização (cvxpy)
```

---

## 📐 Diretrizes de Desenvolvimento e Convenções de Código

Ao modificar ou estender a lógica de cálculo do projeto, as seguintes regras são estritas:

### 1. Parâmetros Centralizados (`src/config.json`)
Nunca insira parâmetros de simulação ou calibração de forma hardcoded (ex. número de simulações, limites de peso, taxas livres de risco de fallback). Sempre carregue-os a partir do arquivo de configuração central usando a utilidade de carregamento padrão (`config_loader.py`).

### 2. Convenção de Retornos e Anualização
- **Retornos Simples (`pct_change`):** Utilizados para otimização de carteiras (aditividade transversal) e para o cálculo das curvas de riqueza de backtest.
- **Retornos Logarítmicos (`np.log(df / df.shift(1))`):** Usados estritamente para testes estatísticos e econométricos (estacionaridade, testes ADF, ARCH).
- **Anualização:** O mercado financeiro brasileiro é assumido como tendo **252 dias úteis** por ano:
  - Média anualizada de retornos: $\mu_{\text{anual}} = \mu_{\text{diário}} \times 252$
  - Volatilidade anualizada: $\sigma_{\text{anual}} = \sigma_{\text{diário}} \times \sqrt{252}$
  - Matriz de covariância anualizada: $\Sigma_{\text{anual}} = \Sigma_{\text{diário}} \times 252$

### 3. Prevenção Absoluta de Look-Ahead Bias
No cálculo do retorno de qualquer estratégia ao longo do tempo, os pesos decididos em $t$ só podem ser multiplicados pelos retornos observados em $t+1$. No código, isto exige a aplicação da defasagem nos pesos:
```python
retorno_carteira = (pesos_calculados.shift(1) * retornos_ativos).sum(axis=1)
```

### 4. Robustez contra Ponto Flutuante
Ao realizar verificações lógicas de desvio padrão ou denominadores em divisões, **nunca** compare diretamente com zero (`== 0.0`), pois imprecisões de ponto flutuante em float64 podem resultar em valores residuais (ex. `2e-19`). Use limites de tolerância:
```python
if std_ativo <= 1e-14:
    return 0.0, 1.0  # Fallback de segurança (p-valor=1.0, z-score=0.0)
```

### 5. Importação em Testes Unitários
A estrutura dos testes adiciona os diretórios de utilitários dinamicamente ao `PYTHONPATH`. Para importar módulos dos pacotes utilitários nos arquivos de teste:
```python
from utils.otimizacao import ...
from utils.inferencia import ...
```

---

## 🛠️ Correções Críticas Implementadas na Auditoria

- **Estabilidade Estatística (`_jk_memmel`):** Ajuste de guarda com tolerância `1e-14` para evitar divisão por zero no teste Jobson-Korkie/Memmel quando séries constantes possuem volatilidades numericamente próximas a zero.
- **Fixture de Calibração Reprodutível:** A fixture `pares_sinteticos` do teste de inferência e calibração utiliza seeds explícitas e montagem determinística para blindar a suíte contra ruídos aleatórios de Monte Carlo que causem falsos negativos de Sharpe.
- **Remoção de Código Binário:** O repositório ignora arquivos cache do Python (`__pycache__`, `.pyc`) via `.gitignore` explícito.
