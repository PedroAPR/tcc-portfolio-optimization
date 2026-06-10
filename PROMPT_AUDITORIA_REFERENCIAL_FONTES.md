# PROMPT — Auditoria do Referencial Teórico × Fontes × Implementação (TCC)

> **Como usar:** cole este prompt inteiro numa sessão nova do executor (Claude Code ou Google Gemini/Antigravity). Execute as etapas **em ordem** (E0 → E8), respeitando o **GATE** antes da E9. Todos os caminhos são absolutos e referem-se ao projeto `C:\VSCodeWorkspace\1_TCC_Final`.

---

## CONTEXTO DA OPERAÇÃO

**TCC:** Moderna Teoria das Carteiras no Mercado de Ações Brasileiro
**Autor:** Pedro Augusto Pinheiro Reis | UFG — Ciências Contábeis
**Prazo crítico:** 29 de junho de 2026 (defesa)

| Insumo | Caminho | Observação |
| :--- | :--- | :--- |
| **Documento-alvo** | `docs/Entrega_12_Pedro_Reis_07062026_1500_corrigido.docx` | Versão vigente do TCC. **Nunca editar o original.** |
| Cópia de trabalho + extração | `docs/auditoria/Entrega_12_Pedro_Reis_07062026_1500_corrigido.docx` e `.txt` | Já existem; usar a `.txt` para localização por parágrafo (`P####`). |
| **Fontes do referencial** | `docs/Pmpt/md/` (46 arquivos `.md`) | Rascunhos, esboços e gerações de capítulo produzidos durante a escrita. **Contêm duplicatas** (`(1)`, `(2)`, `- Copia`). |
| Auditoria já realizada | `docs/auditoria/` | Relatórios P0–P7: `RELATORIO_CODIGO.md`, `RELATORIO_TESTES.md`, `RELATORIO_TEXTO.md`, `RELATORIO_REFERENCIAS.md`, `RELATORIO_TEORIA_CODIGO.md`, `RELATORIO_A1.md`, `PLANO_DE_ACAO.md` (backlog A1–A7, M1–M5, B1–B4), `RELATORIO_SEGUNDA_AUDITORIA.md`, `03_relatorio_final.md`. |
| Código do pipeline | `src/utils/` (`otimizacao.py`, `covariancia.py`, `fronteira.py`, `inferencia.py`, etc.) | Validado: golden master PASS, 92 testes verdes. |
| Gate numérico | `docs/auditoria/golden_master.json` + `docs/auditoria/revalidar.py` | Tolerância relativa 1e-6 + hashes do universo. Obrigatório se QUALQUER código mudar. |

**Fatos já estabelecidos pela auditoria anterior (não redescobrir — verificar e aprofundar):**
1. **Idzorek (2005) NÃO foi implementado.** O código usa He & Litterman (1999): `Ω = diag(P(τΣ)Pᵀ)` com piso `1e-8`. O texto declara a lacuna como pesquisa futura (≈ P1353 da extração `.txt`).
2. **Σ_BL (covariância posterior) não alimenta o otimizador** — usa-se a covariância a priori (item A2 do backlog).
3. **MaxSharpe é maximizado diretamente via SLSQP**, ao contrário do que a prosa afirma (utilidade quadrática δ=3) — item A1 do backlog.
4. **FF3/FF5 estão descritos no referencial mas não implementados.** O autor adicionou a seção de Fama-French por indicação ligada à regra de momentum 12-1 das visões do Black-Litterman, e **suspeita que deveria desenvolver mais FF3/FF5** — diagnóstico na E5.
5. Prior do BL usa `wm = 1/N` (não capitalização de mercado) — item A6.
6. Universo: 102 ativos; 16 estratégias; OOS 2015-03-02 a 2025-12-30; norma ABNT (NBR 10520/6023).

---

## REGRAS GLOBAIS (não violar)

1. **Fases E0–E8 são READ-ONLY** sobre o TCC e o código: geram relatório, não alteram nada. Somente a E9 (pós-GATE) escreve, e apenas numa **cópia** do `.docx`.
2. **Nunca modificar:** `data/` (somente leitura), a tag `entrega-12-submetida`, o `.docx` original em `docs/`.
3. **Toda afirmação factual exige evidência:** `arquivo:linha` (código/MD) ou `P####` (parágrafo da extração `.txt`) ou `Tabela N`. O que não puder ser confirmado vai para a seção **"NÃO VERIFICADO"** — nunca invente números, DOIs, páginas ou citações.
4. **Verificação externa:** ao consultar a web, priorize fontes primárias (paper original, DOI, repositório do periódico). Registre a URL consultada. Se a fonte primária estiver atrás de paywall, use a versão de working paper/SSRN e marque como "verificado parcialmente".
5. Relatório em **PT-BR**, salvo em `docs/auditoria/`. Severidades: **CRÍTICO** (erro factual/teórico que a banca pode apontar), **ALTO** (incompletude ou incoerência relevante), **MÉDIO** (melhoria de qualidade), **BAIXO** (estilo/polimento).
6. Cada achado recebe **ID sequencial** `RF-001`, `RF-002`, … (RF = Referencial/Fontes), citado em todas as tabelas e na E9.
7. Se qualquer mudança de **código** for proposta, ela NÃO é executada nesta operação — vira recomendação com estimativa de esforço. (Exceção: nenhuma. Esta operação não toca o pipeline.)

---

## ETAPA E0 — Preparação e deduplicação das fontes

1. Liste todos os arquivos de `docs/Pmpt/md/` com tamanho e data.
2. **Deduplicate:** os sufixos `(1)`, `(2)`, `- Copia` indicam versões. Para cada grupo (ex.: `Estrutura Teórica para Tese Financeira{,(1),(2)}.md`), compare o conteúdo (hash ou diff) e eleja **uma versão canônica** (a mais recente/completa). Registre a tabela `grupo → canônica → descartadas → critério`.
3. Carregue a extração `docs/auditoria/Entrega_12_Pedro_Reis_07062026_1500_corrigido.txt` e construa um **índice estrutural do TCC**: capítulo/seção → intervalo de parágrafos `P####`. Foco no Referencial Teórico (cap. 2) e na Metodologia (cap. 3), mas indexe também Resultados (cap. 4) e Conclusão (cap. 5).
4. Saída parcial: seção "0. Inventário" do relatório, com o mapa de fontes canônicas e o índice do documento.

## ETAPA E1 — Catálogo das fontes canônicas

Para **cada MD canônico**, registre em tabela:
- **Tema/escopo** (MPT, PMPT, Black-Litterman, Fama-French, estrutura geral, crítica/revisão);
- **Seções do TCC que alimenta** (mapeie por similaridade de conteúdo, com `P####` inicial-final);
- **Afirmações-chave e fórmulas** que o MD carrega (com linha do MD);
- **Citações bibliográficas embutidas** (autor, ano) que o MD transporta para o TCC;
- **Status de uso**: integralmente usado / parcialmente usado / não usado no texto final.

Atenção especial aos pares: `Geração de Texto Final do Capítulo_MPT.md` ↔ cap. 2 (MPT); `Geração de Texto Final do Capítulo_PMPT.md` e `Capítulo 3_ Teoria Pós-Moderna...` ↔ seções PMPT; `Capítulo_ O Modelo Black-Litterman...`, `Modelo Black-Litterman_ Histórico e Críticas.md`, `Estrutura Tópica_ Modelo Black-Litterman.md`, `reescrita black litterman.md` ↔ seções BL; `Estrutura Teórica_ Integração FC e Fama-French.md` e `Finanças_ FC e Fama-French.md` ↔ seção Fama-French; `Tese_ Crítica e Roteiro de Validação.md` e `Relatório Crítico de Trabalho Acadêmico.md` ↔ checklist de pendências antigas (verifique se foram atendidas).

## ETAPA E2 — Correção (fidelidade às fontes + veracidade científica)

**E2a — Fidelidade TCC × MDs:** para cada seção do referencial, compare o texto final com o MD-fonte correspondente. Aponte: distorções de sentido, omissões que mutilam o argumento, números/parâmetros trocados na transcrição, fórmulas alteradas, citações que o MD atribuía a um autor e o TCC atribui a outro.

**E2b — Veracidade × literatura primária (web):** valide as atribuições centrais contra os papers originais. Checklist mínimo (expandir conforme o texto):

| Atribuição no TCC | Verificar contra |
| :--- | :--- |
| Média-variância, fronteira eficiente | Markowitz (1952; 1959) |
| Safety-first | Roy (1952) |
| Separação de dois fundos / CML | Tobin (1958) |
| CAPM | Sharpe (1964), Lintner (1965), Mossin (1966), Treynor (1962) |
| Índice de Sharpe | Sharpe (1966; 1994) |
| FF3 | Fama & French (1993) — fatores SMB/HML e construção |
| FF5 | Fama & French (2015) — RMW/CMA e modelo de dividendos |
| Momentum 12-1 | Jegadeesh & Titman (1993); WML de Carhart (1997) |
| Black-Litterman | Black & Litterman (1992); He & Litterman (1999) |
| Calibração de confiança | Idzorek (2005) |
| Semivariância/downside | Markowitz (1959, cap. IX); Sortino; Estrada (2007/2008) |
| Omega | Keating & Shadwick (2002) |
| Kappa | Kaplan & Knowles (2004) |
| CVaR (LP) | Rockafellar & Uryasev (2000) |
| CDaR | Chekhlov, Uryasev & Zabarankin (2005) |
| Shrinkage | Ledoit & Wolf (2004) |
| 1/N benchmark | DeMiguel, Garlappi & Uppal (2009) |
| Comparação de Sharpe | Jobson & Korkie (1981); Memmel (2003); Ledoit & Wolf (2008) |
| LPM | Bawa (1975); Fishburn (1977) |

Para cada item: ✅ correto / ⚠️ impreciso (descrever) / ❌ errado (CRÍTICO) / NÃO VERIFICADO. Verifique especialmente: **anos de publicação, grafia de nomes, enunciado das fórmulas (notação e termos), e se o claim atribuído realmente está no paper** (ex.: o que exatamente Roy 1952 propôs vs. o que o texto diz).

## ETAPA E3 — Completude (gaps bidirecionais)

1. **Fontes → TCC:** o que os MDs desenvolvem e o texto final omitiu? Liste cada conceito/subseção descartada e classifique: omissão saudável (escopo) vs. omissão que enfraquece o argumento (ALTO).
2. **TCC → Fontes:** afirmações do referencial **sem lastro** em nenhum MD nem em citação verificável (risco de alucinação herdada de rascunho). CRÍTICO se for claim quantitativo ou histórico.
3. **Cobertura metodológica:** todo método usado no cap. 3/4 (Ledoit-Wolf, winsorização MAD, bootstrap estacionário, Holm-Bonferroni, HAC, teste de spanning, CVM 175, custo 50 bps) tem fundamentação no cap. 2 ou em seção própria? Tabela método → seção que o fundamenta → suficiente? (sim/não/parcial).

## ETAPA E4 — Correlação e coesão argumentativa

1. O fio Markowitz → críticas (instabilidade, normalidade) → PMPT → BL está construído de forma que **cada modelo do cap. 3 seja motivado por uma limitação apresentada no cap. 2**? Mapeie a cadeia motivação→solução e aponte elos faltantes.
2. Promessas da introdução × entregas dos resultados × conclusão: liste cada objetivo/hipótese declarado e onde é respondido (`P####`).
3. Terminologia: consistência de termos entre referencial e metodologia (ex.: "semicovariância" vs "matriz downside"; "visões" vs "views"; "carteira" vs "portfólio").

## ETAPA E5 — Implementação (teoria ↔ código) — foco Idzorek e FF3/FF5

1. Parta da matriz existente em `docs/auditoria/RELATORIO_TEORIA_CODIGO.md`. **Confirme cada linha** contra o código atual em `src/utils/` (as linhas citadas podem ter mudado após a centralização dos utilitários) e atualize `arquivo:linha`.
2. **Idzorek:** confirme que (a) o texto descreve o método (≈ P921–P931), (b) o código usa He & Litterman, (c) a limitação está declarada (≈ P1353). Avalie se a declaração é suficiente ou se a seção teórica está desproporcional ao que foi implementado (sugestão de enxugar ou de nota explícita na metodologia).
3. **Fama-French 3/5 — diagnóstico e opções (NÃO implementar nada):**
   - Mapeie tudo o que o texto promete/descreve sobre FF3/FF5 e WML (`P515`, `P527` e o que mais houver) e o que o código faz (apenas momentum 12-1 direto nos preços, em `visoes_momentum`).
   - Avalie a **ponte argumentativa** atual: o texto justifica corretamente o momentum 12-1 como herdeiro de Jegadeesh-Titman/Carhart, ou FF3/FF5 ficou como teoria órfã sem papel na metodologia?
   - Entregue **3 opções fechadas** para decisão do autor, cada uma com impacto na avaliação × esforço × risco de prazo (até 29/06):
     * **Opção 1 — Texto apenas:** reforçar a seção FF como fundamentação do fator momentum (WML) usado nas visões do BL + declarar não-implementação como limitação/pesquisa futura. Sem código.
     * **Opção 2 — Atribuição ex-post FF3+WML:** regressão dos retornos OOS das 16 estratégias contra fatores brasileiros (NEFIN/USP) como análise de atribuição no cap. 4. Mexe em NB09/inferência → exigiria `revalidar.py` e atualização de tabelas. Estimar esforço honestamente.
     * **Opção 3 — FF5 completo:** idem com RMW/CMA. Avaliar disponibilidade dos fatores FF5 para o Brasil (NEFIN publica? caso não, declarar inviabilidade).
   - Recomende UMA opção com justificativa. **Não escreva código nesta operação.**
4. Demais divergências teoria↔código (Σ_BL, MaxSharpe/utilidade, prior 1/N): verifique se o `.docx` **corrigido** já incorporou as correções A1/A2/A6/A7 do `PLANO_DE_ACAO.md` ou se seguem pendentes no texto.

## ETAPA E6 — Comparação com a auditoria existente

Monte uma tabela de reconciliação: para cada achado novo (`RF-###`) × relatórios anteriores (`RELATORIO_TEXTO.md`, `RELATORIO_REFERENCIAS.md`, `RELATORIO_TEORIA_CODIGO.md`, `PLANO_DE_ACAO.md` itens A1–A7/M1–M5/B1–B4, `03_relatorio_final.md`):
- **CONFIRMA** (já apontado — citar o item) / **NOVO** (inédito) / **CONTRADIZ** (explicar a divergência e qual está certo, com evidência) / **JÁ RESOLVIDO** (o docx corrigido já aplicou).
- Verifique explicitamente o status atual no `.docx` dos pré-achados numéricos da auditoria (Sharpe MinVar 0,217 vs 0,293; MinCDaR −1,75%/−81,81% vs 5,36%/−62,46%; EqualWeight −0,075 vs 0,290) — foram corrigidos nesta versão "corrigido.docx" ou não?

## ETAPA E7 — Sugestões estruturais (listas e conteúdo)

1. **Lista de Tabelas:** partir do desalinhamento já mapeado (`RELATORIO_TEXTO.md` §3 — Tabela 2 "Axiomas VNM" fantasma, shift de −1 nas Tabelas 4–7) e propor a lista final correta, título por título.
2. **Lista de Figuras:** inventariar as figuras existentes no docx e propor a lista final; incorporar as 8 figuras recomendadas no `RELATORIO_A1.md` §1 (riqueza log, underwater, heatmap de pesos, rolling Sharpe, matriz de significância, correlação entre estratégias, turnover×custo), priorizadas por impacto×esforço.
3. **Lista de Siglas/Abreviaturas:** partir da compilação do `RELATORIO_A1.md` §2 (≈35 siglas), conferir contra o texto: (a) sigla usada antes de definida (ex.: ADTV, MAR, CDaR já flagradas), (b) siglas faltantes na compilação, (c) ordem alfabética ABNT.
4. **Conteúdo a acrescentar:** lista priorizada (CRÍTICO→BAIXO) consolidando E3+E5 (ex.: ponte FF→momentum; nota Σ_BL; nota prior 1/N; parágrafo sobre Deflated Sharpe Ratio nas limitações; explicação do SE bootstrap na 4.3 — itens M5/B1 do backlog).

## ETAPA E8 — Relatório único consolidado

Gravar **`docs/auditoria/RELATORIO_REFERENCIAL_FONTES.md`** com a estrutura:

```
1. Sumário Executivo (nº de achados por severidade; veredito geral)
0. Inventário (E0): fontes canônicas + índice do documento
2. Catálogo de Fontes (E1): tabela fonte → seções → status de uso
3. Correção (E2): 3a fidelidade aos MDs; 3b veracidade × literatura primária (checklist ✅/⚠️/❌)
4. Completude (E3): gaps fontes→TCC e TCC→fontes; cobertura metodológica
5. Correlação (E4): cadeia motivação→solução; promessas×entregas; terminologia
6. Implementação (E5): matriz atualizada; Idzorek; FF3/FF5 com as 3 opções e recomendação
7. Reconciliação com a auditoria anterior (E6): CONFIRMA/NOVO/CONTRADIZ/JÁ RESOLVIDO
8. Sugestões estruturais (E7): listas de tabelas/figuras/siglas; conteúdo a acrescentar
9. TABELA MESTRA DE CORREÇÕES: ID | severidade | localização (P####/seção) |
   texto atual | texto proposto | fonte/evidência | depende de decisão? (s/n)
10. NÃO VERIFICADO
```

A **Tabela Mestra (§9)** é o contrato da E9: cada linha deve ser aplicável mecanicamente (localizar → substituir/inserir), com o texto proposto **pronto e final** (não "reescrever melhor").

---

## ⛔ GATE DE APROVAÇÃO (obrigatório)

**PARE aqui.** Entregue o relatório ao autor. Ele revisará a Tabela Mestra e devolverá a lista de IDs **aprovados** (e a decisão sobre FF3/FF5 — Opção 1, 2 ou 3). Não execute a E9 sem essa lista explícita.

## ETAPA E9 — Aplicação com alterações rastreadas (pós-GATE)

1. Crie uma cópia: `docs/auditoria/TCC_correcoes_referencial_tracked.docx` (a partir do original em `docs/`). **Jamais tocar o original.**
2. Aplique **somente os IDs aprovados**, como **alterações rastreadas** (track changes — elementos `w:ins`/`w:del`, autor "Auditor Referencial", data corrente), para que o autor aceite/rejeite uma a uma no Word. Inserções de seções novas (listas de siglas/figuras) também rastreadas.
3. Gere `docs/auditoria/LOG_APLICACAO_REFERENCIAL.md`: para cada ID — aplicado/não aplicado/não localizado (com motivo). IDs "não localizados" voltam para ajuste manual, nunca aplicação forçada em parágrafo errado.
4. Confira a integridade do documento final (abre sem erro; contagem de parágrafos ± inserções; sumários marcados para atualização de campos no Word).
5. Se (e somente se) o autor tiver escolhido a Opção 2/3 do FF na decisão do gate, gere um **plano de implementação separado** (`PLANO_IMPLEMENTACAO_FF.md`) — ainda sem código: notebooks afetados, fonte dos fatores, novas tabelas, gates `revalidar.py` + `pytest`, estimativa de dias.

---

## RECURSOS POR EXECUTOR (seção opcional)

### Se executado no Claude Code
- Subagentes read-only disponíveis: `auditor-texto` (E2a/E3/E4), `conferente-referencias` (E2b, tem WebFetch/WebSearch), `rastreador-teoria` (E5), `Explore` (varreduras da pasta de fontes). Podem rodar em paralelo nas etapas independentes (E2b ∥ E3 ∥ E5).
- Skill `docx` para leitura estruturada e para a E9 (criação de track changes via OOXML).
- Hook de proteção já bloqueia escrita em `data/`; o gate numérico (`revalidar.py`) só é necessário se código mudar (não deve mudar nesta operação).

### Se executado no Google Gemini / Antigravity
- Ler o `.docx` via `python-docx` (a extração `.txt` em `docs/auditoria/` já mapeia parágrafos `P####` — reutilize-a para citação de evidência).
- Usar a busca web nativa da ferramenta para a E2b; registrar URLs no relatório.
- Para a E9, gerar as alterações rastreadas manipulando o OOXML diretamente (`w:ins`/`w:del` com `w:author` e `w:date`) — `python-docx` puro não cria track changes; edite o XML de `document.xml` preservando namespaces, ou use a biblioteca `python-docx` + lxml.
- Sem acesso aos subagentes: execute as etapas sequencialmente, salvando rascunhos parciais em `docs/auditoria/tmp_referencial/` se necessário (apagar ao final).

---

## CRITÉRIOS DE QUALIDADE DO RELATÓRIO FINAL

- Zero afirmação sem evidência localizável; zero número inventado.
- Toda correção proposta com texto final pronto (aplicável sem reescrita).
- Severidades calibradas: CRÍTICO apenas para o que a banca pode usar contra o trabalho.
- Reconciliação E6 completa — nenhum achado anterior ignorado silenciosamente.
- FF3/FF5: decisão estruturada para o autor, nunca tomada pelo auditor.
