# Prompt — Relatório Minucioso do TCC (variante Claude Code)

> **Como usar:** abra o Claude Code na raiz do repositório `1_TCC_Final` (branch `auditoria-tcc`).
> Garanta que o `.docx` do TCC esteja acessível (no repo ou em caminho conhecido) e que os dois
> relatórios de auditoria (`RELATORIO_ATUALIZACAO_APENDICES.md`, `Relatorio_Diagnostico_TCC_Pedro.md`)
> estejam na árvore. Cole o prompt abaixo. Ajuste os **[CAMINHOS]** se diferirem.

---

## [CAMINHOS / PARÂMETROS] (edite antes de enviar)

- **Raiz do repositório:** `./` (ex.: `C:\VSCodeWorkspace\1_TCC_Final`)
- **Documento avaliado (.docx):** `./Entrega_12_Pedro_Reis_auditado.docx`
- **Auditoria de código (referência):** `./RELATORIO_ATUALIZACAO_APENDICES.md`
- **Diagnóstico textual (referência):** `./Relatorio_Diagnostico_TCC_Pedro.md`
- **Saída do relatório:** `./RELATORIO_AVALIACAO_TCC.md`
- **Execução de notebooks:** PROIBIDA por padrão (ver regra abaixo). Verificação é estática.

---

## PROMPT

Você é um **engenheiro de pesquisa quantitativa** atuando como arguidor(a) técnico(a) de uma banca de
TCC. Você tem acesso de terminal e leitura a este repositório (`1_TCC_Final`), que contém o pipeline de
um TCC em Ciências Contábeis/Finanças: "Moderna Teoria das Carteiras no Mercado de Ações Brasileiro:
Comparação entre Otimizadores e Inputs". Sua missão é **auditar o trabalho contra o código-fonte e os
artefatos** e gravar um **relatório de avaliação detalhado e minucioso** em `./RELATORIO_AVALIACAO_TCC.md`.

### Regras operacionais (Claude Code)

1. **Não execute nenhum notebook nem célula sem autorização explícita.** Toda a verificação deve ser
   feita por **leitura estática** de código + inspeção de artefatos já existentes em `data/`. Os
   artefatos de desempenho já estão materializados; nenhuma reexecução é necessária para confirmá-los.
   Se em algum ponto você concluir que só a execução fecharia uma lacuna, **pare e pergunte** antes de
   rodar qualquer coisa, descrevendo exatamente o que pretende executar e por quê.
2. **Não modifique** arquivos do repositório, exceto **criar** o arquivo de saída
   `./RELATORIO_AVALIACAO_TCC.md`. Não altere notebooks, código, config ou dados.
3. **Hierarquia de verdade:** código-fonte e artefatos (`src/`, `data/`, `src/config.json`,
   `utils/otimizacao.py`) **prevalecem** sobre o texto do `.docx`. Os dois `.md` de auditoria são ponto
   de partida — **reconfirme cada afirmação deles diretamente no código** e corrija o que estiver
   desatualizado.
4. **Toda afirmação do relatório deve citar evidência rastreável:** `arquivo:linha`, nome de artefato
   (`data/...`) com `shape`/contagem, ou seção/tabela/apêndice do `.docx`. **Nunca invente valores.**
   O que não puder ser confirmado vira `[VERIFICAR — requer leitura de X / autorização para executar Y]`.

### Etapa 0 — Inventário e extração

- Liste a árvore relevante: `src/`, `utils/`, `data/`, `src/config.json`, `requirements.txt`.
- Extraia o texto do `.docx` para análise (sem alterá-lo). Sugestões:
  `python -c "import docx,sys; d=docx.Document(sys.argv[1]); print('\n'.join(p.text for p in d.paragraphs))" Entrega_12_*.docx`
  (ou `pandoc Entrega_12_*.docx -t markdown -o /tmp/tcc.md`). Tabelas do docx podem exigir leitura via
  `python-docx` iterando `document.tables`.
- Leia `src/config.json` e registre os parâmetros canônicos (datas, LIMIAR_PRESENCA, PERCENTIL_LIQUIDEZ,
  K_MAD, C_MAD, CUSTO_BPS, ALPHA_PMPT, WARMUP, SEED, TRADING_DAYS, etc.).

### Etapa 1 — Playbook de verificação (execute estes checks e registre cada resultado)

Para cada item, rode o comando, registre o valor obtido e compare com o que o texto do TCC afirma:

- **N do universo:** `wc -l data/Tickers/tickers_finais.csv` (esperado 119 = 1 cabeçalho + 118).
  Compute C(N,2) e compare com os "8.385 pares" do texto (C(130,2)=8.385; C(118,2)=6.903).
- **Nº de pregões / shape do painel:**
  `python -c "import pandas as pd; print(pd.read_parquet('data/Painel_Dados/painel_alinhado.parquet').shape)"`
  (esperado ≈ (3967, 121)). Compare com "4.030" e "3.967" do texto.
- **Visões do BL / ausência de ML:** `grep -rin "lstm\|arima" src/ utils/` (esperado: sem matches).
  Localize a geração de visões: `grep -rin "momentum\|visoes_momentum" src/ utils/` e leia a função em
  `utils/otimizacao.py`. Confirme `P = I_N` e `Q = momentum 12-1`.
- **Escala de Σ no BL:** `grep -rin "S_anual\|TRADING_DAYS\|\* 252\|\* 21" src/07_*` — confirme
  `S_anual = S * TRADING_DAYS` (×252), não ×21.
- **δ (delta):** `grep -rin "DELTA\|delta" src/07_*` — confirme valor fixo `2.5` (hardcoded), não
  otimização reversa por janela.
- **Prior (w_m):** `grep -rin "wm\|repeat(1.0\|prior" src/07_* utils/otimizacao.py` — confirme
  `wm = np.repeat(1.0/N, N)` (1/N), não capitalização de mercado.
- **Ω (Omega):** confirme construção He-Litterman (`diag(max(diag(P@(tau*Sg)@P.T), 1e-8))`), não Idzorek.
- **Outliers/winsorização:** leia `src/05_*Saneamento*` — confirme **MAD modificado (Iglewicz-Hoaglin,
  K=3,5, c=0,6745)**, não IQR×3,0.
- **Custo transacional / "L1":** `grep -rin "CUSTO_BPS\|custo_unit" src/ config.json` — confirme 50 bps
  (0,5%). Verifique se há de fato regularização L1 na função-objetivo ou apenas custo de giro.
- **Estratégias existentes vs texto:**
  `python -c "import pandas as pd; print(list(pd.read_parquet('data/Estrategias/strategy_returns.parquet').columns))"`
  Confirme que **NÃO existem** colunas `MinVar_L1`/`MaxSharpe_L1`, e que existe a família PMPT completa
  (MaxOmega, MaxSortino, MaxKappa3, MinCVaR, MinCDaR) e as 4 variantes BL.
- **Métricas reais:** leia `data/Estrategias/apendice_H_painel_metricas.csv` e
  `data/Estrategias/desempenho_estrategias.csv` (inclui `turnover_aa`). Use **esses** números no
  relatório, não os do texto.
- **Datas de início do OOS:**
  `python -c "import pandas as pd; df=pd.read_parquet('data/Estrategias/strategy_returns.parquet'); print({c: str(df[c].first_valid_index()) for c in df.columns})"`
  Confirme início único em 2015-03-02 para todas as estratégias (texto sugere set/2015 e jan/2015).
- **Nº de rebalanceamentos OOS:** conte sobre `data/Estrategias/pesos_historico.csv` por estratégia.
- **Ticker GOLL:** `grep -in "GOLL" data/Tickers/tickers_finais.csv` — registre `GOLL54` e seu status.
- **Clusterização Ward (Apêndice I):** `grep -rin "ward\|linkage\|fcluster\|dendrogram" src/`
  — confirme se está implementada (NB08?) ou se é apenas mencionada.
- **Datasets.md (reprodutibilidade):** verifique se o arquivo referenciado existe na árvore.
- **σ_anual:** localize a anualização de volatilidade individual (NB06) e confirme `× sqrt(252)`;
  contraste com o Apêndice F do texto, que traz `× 252` (errado para desvio-padrão).

### Etapa 2 — Redação do relatório (`./RELATORIO_AVALIACAO_TCC.md`)

Escreva o relatório em **português acadêmico**, impessoal e construtivo, nesta ordem (não omita seções):

1. **Ficha técnica e estado de maturidade** (uma frase de veredito geral).
2. **Síntese descritiva, capítulo a capítulo + Apêndices A–J** (o que o trabalho faz; descritivo).
3. **Avaliação do referencial teórico** (cobertura, correção conceitual, atribuições históricas).
4. **Avaliação da metodologia** (filtros de liquidez; saneamento MAD; retornos simples/log; bateria
   econométrica; μ/Σ e Ledoit-Wolf; as 3 famílias e os 15 modelos; construção do BL: prior, visões, Ω,
   τ, δ; backtesting; métricas).
5. **Avaliação dos resultados, tabela a tabela** (preenchimento, coerência, suporte em artefato).
6. **Tabela — Consistência interna** (N; pregões; benchmarks; datas OOS; custo/"L1"; unidades de
   Sharpe/Sortino; tickers), com todos os valores conflitantes e suas localizações no texto, e o valor
   canônico do código.
7. **Tabela — Texto × Código** (colunas: *Parâmetro | Texto afirma | Código/artefato comprova |
   Veredito | Ação no texto*), cobrindo no mínimo: visões LSTM×momentum (e ausência de LSTM/ARIMA),
   escala Σ (×252), δ fixo 2,5, prior 1/N, Ω He-Litterman vs Idzorek, σ_anual √252, e ausência de
   MinVar_L1/MaxSharpe_L1.
8. **Lacunas de fechamento empírico** (PMPT e variantes BL prometidas no escopo mas não reportadas no
   Cap. 4 — destacando que os artefatos do Apêndice H **já contêm** essas métricas, logo o fechamento é
   viável sem reexecução; células interpretativas pendentes; apêndices órfãos).
9. **Citações × referências** (faltantes em ambos os sentidos; divergências de ano).
10. **Estrutura, formatação e ABNT** (títulos duplicados/placeholder no Cap. 4; equações ausentes;
    numeração de tabelas; Sumário e Lista de Tabelas desatualizados; epígrafe; cronograma).
11. **Pontos prováveis de arguição** (8–15 perguntas da mais perigosa à menos, cada uma com a resposta
    defensável e a correção prévia que a blinda).
12. **Veredito, severidade e plano de ação** — classifique cada achado em CRÍTICO/ALTO/MÉDIO/BAIXO;
    encerre com checklist priorizado e acionável, esforço estimado (baixo/médio/alto) por item, sequência
    recomendada, e a decisão estratégica de maior impacto (reportar a família PMPT + variantes BL já
    existentes nos artefatos × reduzir o escopo declarado), com recomendação fundamentada.

### Fechamento

- Use tabelas nas seções 6, 7 e 12; prosa nas demais.
- Reserve incerteza apenas para itens genuinamente marcados `[VERIFICAR]`; onde a evidência permite,
  afirme sem hedge.
- Ao final do relatório, inclua um **apêndice de evidências**: a lista dos comandos executados e o valor
  bruto obtido em cada um (para auditabilidade).
- Termine com um parágrafo de síntese: o que separa este TCC de "consistente e defensável" e as 5
  correções de maior ganho de robustez por unidade de esforço.
- Após gravar o arquivo, **não execute mais nada**; reporte o caminho do relatório e um resumo de 5–8
  linhas dos achados CRÍTICOS na conversa.
