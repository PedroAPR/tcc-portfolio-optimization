# Plano de Auditoria e Aprimoramento do TCC — Pacote de Prompts para Claude Code

**Objetivo:** elevar o TCC a nível de excelência (alvo Qualis A1 / submissão a periódico), via auditoria completa e separada de **código** e **texto**, cruzamento teoria↔implementação, e refatoração com re-validação numérica — sem destruir a versão já entregue.

**Decisões já tomadas (incorporadas):**
- Texto em **Word (.docx)** → auditores leem via `python-docx`.
- Apetite: **refatorar a fundo na branch**, com **gate de re-validação obrigatório** a cada mudança de código.
- Plágio: relatório oficial vem do **Turnitin/iThenticate da UFG**; aqui fazemos só **higiene de originalidade interna**.
- `test_pipeline.py`: **conteúdo desconhecido** → P0 inspeciona e, se necessário, cria o **golden master**.
- `otimizacao.py`/MinCDaR: **decisão pós-P1** (não assumir aplicado).
- P5 (teoria↔código): **mapear e reportar**, sem gerar tarefas.
- Norma: **ABNT** (NBR 10520 para citações; NBR 6023 para referências).

**Como usar:** branch `tcc-aprimoramento` já criada. Execute os prompts **em ordem**. Após cada fase, **me devolva o relatório gerado** (`docs/auditoria/*.md`) — eu reviso e decidimos os gates (especialmente o do MinCDaR após P1). Cole cada bloco `═══ PROMPT Pn ═══` como uma mensagem no Claude Code.

---

## REGRAS GLOBAIS (válidas para todos os prompts — cole no topo de cada sessão se necessário)

```
REGRAS GLOBAIS DESTA OPERAÇÃO (não violar):
1. Trabalhe SOMENTE na branch 'tcc-aprimoramento'. Confirme com `git branch --show-current` antes de qualquer escrita.
2. NUNCA modifique: arquivos sob data/ (somente leitura), nem a tag 'entrega-12-submetida'. Para editar o .docx, trabalhe sobre uma CÓPIA em docs/auditoria/.
3. Fases de AUDITORIA são read-only: geram relatórios, não alteram código nem texto.
4. Fases de REFATORAÇÃO só escrevem após o relatório correspondente existir, e cada mudança de código passa pelo GATE DE RE-VALIDAÇÃO (ver P0) antes do commit.
5. Toda afirmação factual num relatório precisa de evidência: arquivo:linha (código) ou arquivo:parágrafo/tabela (texto). O que não puder confirmar vai para uma seção "NÃO VERIFICADO".
6. NÃO execute notebooks sem autorização explícita do prompt. Quando precisar de execução, use os outputs já salvos em disco; se for inevitável re-executar, re-execute SÓ o(s) notebook(s) afetado(s).
7. Relatórios em PT-BR, gravados em docs/auditoria/. Não invente números — use os reais das saídas/tabelas.
8. Commits pequenos e descritivos. Nunca faça force-push, rebase destrutivo, nem delete a tag/branch de preservação.
```

---

## ARTEFATOS DO P0 (conteúdo pronto — o P0 manda o Claude Code criar estes arquivos)

### `CLAUDE.md` — seção de invariantes (acrescentar, mantendo o arquivo enxuto)
```markdown
## Invariantes do projeto (NÃO violar)
- Universo final: **102 ativos** (118 pós-liquidez − 16 por integridade). Nunca reintroduzir os 16 excluídos
  (FICT3, GOLL54, VSTE3, PDTC3, LIGT3, PMAM3, RPMG3, RSID3, ETER3, AMER3, LUPA3, NEXP3, OIBR3, OIBR4, PDGR3, VIVR3).
- Parâmetros canônicos: WARMUP=60 meses; CUSTO_BPS=50; TETO_PESO=0.10; ALPHA_PMPT=0.95; SEED=42;
  K_MAD=3.5; C_MAD=0.6745; BOOTSTRAP_REPS=2000; bloco médio=10; TRADING_DAYS=252;
  OOS = 2015-03-02 a 2025-12-30 (2.690 pregões, 130 rebalanceamentos).
- 16 estratégias: EqualWeight, EqualWeight_BuyHold, InvVol, MinVar, MinVar_c10, MaxSharpe, MaxSharpe_c10,
  MaxOmega, MaxSortino, MaxKappa3, MinCVaR, MinCDaR, BL_classico, BL_classico_c10, BL_downside, BL_downside_c10.
- Norma de escrita: ABNT (NBR 10520 citações; NBR 6023 referências).
- NÃO EDITAR: data/ (somente leitura); tag entrega-12-submetida.
- Toda mudança de código → re-validar contra docs/auditoria/golden_master.json (tolerância relativa 1e-6) antes do commit.
```

### `.claude/agents/auditor-codigo.md`
```markdown
---
name: auditor-codigo
description: Auditoria read-only de qualidade, integridade e reprodutibilidade do código Python/notebooks do src.
tools: Read, Grep, Glob, Bash
model: inherit
---
Você audita código quantitativo financeiro sem alterá-lo. Para cada arquivo do src: liste propósito, I/O,
parâmetros (com valores reais), e defeitos (sintaxe morta, duplicação, imports não usados, seeds ausentes,
status de solver não verificado, dependências não fixadas). Toda constatação com arquivo:linha. Nunca escreva
em data/ nem execute notebooks. Reporte; não corrija.
```

### `.claude/agents/auditor-texto.md`
```markdown
---
name: auditor-texto
description: Auditoria read-only do TCC (.docx) — fonte, formatação, ABNT, sintaxe, semântica, coesão/coerência, consistência numérica texto↔tabelas.
tools: Read, Grep, Glob, Bash
model: inherit
---
Você revisa um TCC em .docx (via python-docx) sem alterá-lo. Verifique: padronização de fonte/estilos,
hierarquia de títulos, numeração de seções/figuras/tabelas/equações, sumário, ABNT, legendas, coesão e
coerência entre seções, e — crítico — se TODO número citado na prosa bate com as tabelas do próprio documento.
Cada achado com parágrafo/tabela de referência. Reporte; não corrija.
```

### `.claude/agents/conferente-referencias.md`
```markdown
---
name: conferente-referencias
description: Reconcilia citações no texto x lista de referências e verifica existência/correção das referências (web).
tools: Read, Grep, Glob, Bash, WebFetch, WebSearch
model: inherit
---
Você confere referências de um TCC ABNT. (1) Liste toda citação no corpo e toda entrada na lista; aponte
órfãs (citadas e não listadas) e fantasmas (listadas e não citadas). (2) Para cada referência, verifique
existência e correção (autores, ano, título, periódico, DOI) via web; marque divergências. (3) Cheque formato
ABNT NBR 6023. Não invente DOIs; o que não confirmar, marque "NÃO VERIFICADO". Reporte; não corrija.
```

### `.claude/agents/rastreador-teoria.md`
```markdown
---
name: rastreador-teoria
description: Cruza o Referencial Teórico com a implementação no src; produz matriz de rastreabilidade (map-only).
tools: Read, Grep, Glob, Bash
model: inherit
---
Você cruza teoria e código. Para cada modelo/método/equação descrito no Referencial Teórico e na Metodologia,
encontre a implementação correspondente no src (arquivo:linha) OU registre "NÃO IMPLEMENTADO". Não decida nem
implemente nada — apenas mapeie e reporte lacunas (ex.: Idzorek, Fama-French 3/5 fatores).
```

### `.claude/hooks/protege.sh` + registro em `.claude/settings.json`
```bash
#!/usr/bin/env bash
# Bloqueia escrita em data/ e em arquivos da versão preservada.
payload="$(cat)"; path="$(echo "$payload" | grep -oE '"file_path"[^,]*' | head -1)"
case "$path" in
  *"/data/"*|*"entrega-12-submetida"*) echo "BLOQUEADO: caminho protegido ($path)"; exit 2;;
esac
exit 0
```
```json
{ "hooks": { "PreToolUse": [ { "matcher": "Write|Edit",
  "hooks": [ { "type": "command", "command": "bash .claude/hooks/protege.sh" } ] } ] } }
```

---

## ═══ PROMPT P0 — Setup, guardrails e golden master ═══

```
[Cole as REGRAS GLOBAIS acima primeiro.]

Você está preparando uma operação de auditoria/refatoração do meu TCC nesta branch. Tarefas:

1. Confirme a branch atual (tcc-aprimoramento) e que a tag entrega-12-submetida existe. Se a branch não existir, PARE e me avise.
2. Crie os artefatos cujo conteúdo eu forneço a seguir, exatamente: CLAUDE.md (seção de invariantes — acrescente sem inchar o arquivo), .claude/agents/{auditor-codigo,auditor-texto,conferente-referencias,rastreador-teoria}.md, .claude/hooks/protege.sh (chmod +x) e o bloco de hooks em .claude/settings.json. [COLE AQUI os 6 blocos de artefato da seção "ARTEFATOS DO P0".]
3. Inspecione src/.../test_pipeline.py e me diga, com evidência (arquivo:linha), se ele compara VALORES (Sharpe/CAGR com tolerância) ou só dimensões/sanidade.
4. GOLDEN MASTER: a partir dos outputs já salvos em disco (strategy_returns, desempenho_estrategias, pesos_historico, fronteira, apêndices de inferência), gere docs/auditoria/golden_master.json contendo, por estratégia: CAGR, Vol, Sharpe, Sortino, MaxDD, Turnover; além de shapes das matrizes-chave e hashes dos CSVs de universo. NÃO re-execute notebooks — leia os arquivos.
5. Crie docs/auditoria/revalidar.py: script que, dado o nome de um notebook/módulo alterado, re-executa SOMENTE os estágios a jusante afetados e compara os resultados ao golden_master.json (tolerância relativa 1e-6), imprimindo PASS/FAIL por métrica. Documente o grafo de dependências usado.
6. Gere docs/auditoria/00_setup.md resumindo o que foi criado, o veredito sobre o test_pipeline.py, e o conteúdo do golden master.

NÃO altere código de pipeline nem o texto nesta fase.
```

---

## ═══ PROMPT P1 — Auditoria de código (arquivo por arquivo do src) ═══

```
[REGRAS GLOBAIS no topo.] Use o subagente auditor-codigo (read-only).

Audite TODOS os arquivos sob src/ e utils/, um a um. Para CADA arquivo, registre:
- Propósito, inputs, outputs, parâmetros-chave (valores reais, arquivo:linha).
- Defeitos por severidade (ALTA/MÉDIA/BAIXA): sintaxe/dead code; duplicação (ex.: múltiplas cópias de ledoit_wolf);
  imports/dependências não usados; requirements não fixados; aleatoriedade sem seed; I/O frágil; e — atenção —
  verificação de status de solver (cvxpy): localize TODA aceitação de 'optimal_inaccurate' e pesos consumidos sem
  guarda. Documente o caso do MinCDaR (otimizacao.py: w_min_cdar) com evidência.
- Reprodutibilidade: o pipeline é determinístico dado SEED? Aponte fontes de não-determinismo.
- Oportunidades de refatoração (DRY, funções longas, acoplamento), SEM aplicar nada.

Saída: docs/auditoria/RELATORIO_CODIGO.md com: sumário executivo; tabela por arquivo; registro de defeitos
priorizado; e uma seção "Decisão pendente — MinCDaR/otimizacao.py" resumindo o problema e as opções (aplicar o
fix de status+reescala+fallback vs. manter), para EU decidir. Não rode notebooks. Não corrija nada.
```

> **GATE pós-P1:** me devolva `RELATORIO_CODIGO.md`. Decidimos juntos (a) aplicar ou não o `otimizacao.py` corrigido e (b) a lista priorizada de refatorações. Só então as fases de escrita começam, sempre com `revalidar.py` após cada mudança.

---

## ═══ PROMPT P2 — Casos de teste e integridade (por arquivo do src) ═══

```
[REGRAS GLOBAIS no topo.]

Com base no RELATORIO_CODIGO.md, proponha e implemente uma suíte de testes em tests/ (pytest), SEM alterar o
código de produção. Para cada módulo/notebook relevante, cubra:
- Dimensional: shapes coerentes (102 ativos propagando do universo ao backtest).
- Financeiro/sanidade: pesos somam 1 e long-only; retornos finitos; datas monotônicas; matriz de covariância PSD.
- Numérico (golden master): métricas-título dentro da tolerância de docs/auditoria/golden_master.json.
- Property-based (hypothesis, se disponível): invariantes dos otimizadores sob entradas aleatórias controladas
  (ex.: w_min_var nunca retorna peso negativo; CDaR cai para fallback quando o solve não é 'optimal').
- Reprodutibilidade: rodar duas vezes com SEED fixo dá resultado idêntico.
Marque com @pytest.mark.slow os testes que exigem re-execução pesada. Gere docs/auditoria/RELATORIO_TESTES.md
listando cobertura por arquivo e lacunas. Rode apenas os testes rápidos; os lentos, só sob autorização.
```

---

## ═══ PROMPT P3 — Auditoria do texto (.docx) ═══

```
[REGRAS GLOBAIS no topo.] Use o subagente auditor-texto. Trabalhe sobre uma CÓPIA do .docx em docs/auditoria/.

Audite o TCC e gere docs/auditoria/RELATORIO_TEXTO.md cobrindo:
- Formatação/fonte: padronização de fonte, tamanho, espaçamento, estilos; hierarquia e numeração de títulos
  (sem duplicação); numeração e referência cruzada de figuras, tabelas e equações; sumário/listas coerentes (ABNT).
- Sintaxe e semântica: erros gramaticais, regência, concordância, ambiguidades, termos inconsistentes
  (ex.: "carteira" vs "portfólio"), siglas usadas antes de definidas.
- Coesão e coerência: fluxo entre capítulos/seções; promessas da introdução cumpridas; metodologia ↔ resultados ↔ conclusão alinhados.
- CONSISTÊNCIA NUMÉRICA (crítico): cruze TODO número citado na prosa com as Tabelas do próprio documento.
  Liste cada divergência (parágrafo → valor no texto → valor na tabela). [Pré-achados a confirmar: parágrafos da
  Análise Comparativa com Sharpe/CAGR de uma rodada anterior — ex.: MinVar 0,217 vs 0,293; CDaR −1,75%/−81,81%
  vs 5,36%/−62,46%; EqualWeight −0,075 vs 0,290; e a afirmação de que a 1/N rebalanceada estaria "entre as piores".]
Cada achado com referência de parágrafo/tabela. Reporte; não corrija o documento nesta fase.
```

---

## ═══ PROMPT P4 — Referências e originalidade ═══

```
[REGRAS GLOBAIS no topo.] Use o subagente conferente-referencias.

Gere docs/auditoria/RELATORIO_REFERENCIAS.md:
1. Reconciliação citação↔lista: toda citação no corpo com entrada na lista (órfãs) e vice-versa (fantasmas).
2. Verificação externa (web): para cada referência, confirmar existência e correção de autores/ano/título/periódico/DOI;
   marcar divergências; NÃO inventar DOIs (NÃO VERIFICADO quando não confirmar).
3. Conformidade ABNT NBR 6023 (formato das entradas) e NBR 10520 (formato das citações no texto).
4. Higiene de originalidade INTERNA: duplicação de trechos entre seções; auto-plágio; paráfrase colada demais de
   fonte citada (quando a fonte for acessível); citações diretas sem aspas/recuo/página. (O relatório oficial de
   similaridade virá do Turnitin/iThenticate da UFG — aqui é só higiene interna.)
Não altere o texto. Reporte com evidência (parágrafo/entrada).
```

---

## ═══ PROMPT P5 — Rastreabilidade teoria ↔ implementação (map-only) ═══

```
[REGRAS GLOBAIS no topo.] Use o subagente rastreador-teoria.

Gere docs/auditoria/RELATORIO_TEORIA_CODIGO.md com uma MATRIZ DE RASTREABILIDADE: cada modelo/método/equação do
Referencial Teórico e da Metodologia → implementação correspondente (arquivo:linha) OU "NÃO IMPLEMENTADO".
Cubra explicitamente: MV/MaxSharpe/MinVar; PMPT (Omega, Sortino, Kappa, CVaR, CDaR); Black-Litterman (prior,
visões de momentum 12-1, calibração de incerteza das visões — Idzorek); fatores (Fama-French 3/5, WML).
Para cada "NÃO IMPLEMENTADO" (ex.: Idzorek, FF3/FF5), registre onde o texto o menciona e se está declarado como
limitação. APENAS mapeie e reporte — não decida nem implemente.
```

---

## ═══ PROMPT P6 — Tabelas, figuras, abreviaturas e checklist de nível A1 ═══

```
[REGRAS GLOBAIS no topo.]

Gere docs/auditoria/RELATORIO_A1.md com recomendações (sem alterar o documento):
- Tabelas/figuras sugeridas que faltam para padrão de periódico: curvas de riqueza acumulada; gráfico "underwater"
  de drawdown; heatmap de evolução de pesos; Sharpe móvel (rolling); matriz estratégia×métrica; matriz de
  significância (p-valores par a par); tabela consolidada de parâmetros; tabela de turnover×custo.
- Lista de abreviaturas e siglas (compilar todas as usadas, com definição na primeira ocorrência).
- Checklist de excelência A1/periódico, com status atual e gap:
  * Reprodutibilidade: seeds, requirements FIXADOS (remover tensorflow/keras/hmmlearn não usados), script único de
    reprodução, declaração de disponibilidade de dados/código.
  * Robustez: sensibilidade a custo (0/25/50/100 bps); estabilidade por subperíodo; taxa livre de risco alternativa;
    correção de múltiplos testes (Holm-Bonferroni — já há); e, contra data-snooping em 16 estratégias,
    Deflated Sharpe Ratio (Bailey & López de Prado) e/ou SPA de Hansen / Reality Check de White.
  * Transparência: limitações declaradas (viés de sobrevivência da Etapa VI; nomes de baixa liquidez mantidos;
    Idzorek e FF3/FF5 não implementados; turnover/custo do BL).
Priorize cada item por (impacto na avaliação) × (esforço até 29).
```

---

## ═══ PROMPT P7 — Síntese e backlog priorizado ═══

```
[REGRAS GLOBAIS no topo.]

Consolide RELATORIO_CODIGO, _TESTES, _TEXTO, _REFERENCIAS, _TEORIA_CODIGO e _A1 em docs/auditoria/PLANO_DE_ACAO.md:
- Backlog único priorizado (ALTA/MÉDIA/BAIXA) por impacto×esforço, com prazo até 29.
- Caminho crítico: o que TEM de entrar na "nova versão" da apresentação vs. o que pode ir só na versão final.
- Dependências entre tarefas (ex.: aplicar otimizacao.py → re-validar → atualizar Tabelas 9/10 → reescrever seção 4.x do CDaR).
- Riscos e gates de re-validação.
Não execute as tarefas; só organize o plano.
```

---

## Recursos do Claude Code recomendados nesta operação

- **Subagente Explore (read-only)** e os 4 customizados acima: rodam auditorias pesadas sem poluir o contexto principal; até 10 em paralelo.
- **`/loop`**: na fase de refatoração, para o ciclo "corrige → roda `revalidar.py` → re-checa" até a checklist passar (exige terminal aberto; é por sessão).
- **`/ultrareview`** (opcional, pago): uma passada multiagente de revisão de código na branch — bom complemento ao P1 antes de refatorar.
- **Hooks** (P0): blindam `data/` e a versão preservada contra escrita acidental.
- **Skills**: depois, dá para promover as checklists recorrentes (consistência numérica, conferência ABNT) a `.claude/skills/<nome>/SKILL.md` e invocá-las como comando.
- **worktree**: mantém a entrega 12 intacta numa pasta separada durante todo o trabalho.

## Fluxo e gates (o que me devolver)
1. P0 → me mande `00_setup.md` (veredito do test_pipeline + golden master).
2. P1 → me mande `RELATORIO_CODIGO.md`; **decidimos o MinCDaR** e a lista de refatoração.
3. P3/P4/P5/P6 podem rodar em paralelo (são read-only). Me mande os relatórios.
4. P7 → fechamos o backlog priorizado e atacamos por ordem, sempre com `revalidar.py` após cada mudança de código.
