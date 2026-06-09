# Prompt de Revisao Completa do TCC - 5 Ondas

Documento-alvo: C:\VSCodeWorkspace\1_TCC_Final\docs\Entrega_12_Pedro_Reis_05062026_1600.docx
Normas: ABNT NBR 14724:2011 (formatacao), ABNT NBR 10520:2023 (citacoes), ABNT NBR 6023:2018 (referencias)
Nivel de rigor: AGRESSIVO - reformular frases para maxima clareza academica, sempre mostrando versao original + sugestao
Output por onda: Relatorio .md individual + Sumario Executivo consolidado ao final da 5a onda

---

## INSTRUCOES GERAIS PARA O AGENTE REVISOR

Antes de iniciar qualquer onda:

1. Extraia o texto completo do arquivo .docx usando python-docx, paragrafo por paragrafo, preservando a numeracao de linhas para referencia cruzada.
2. Divida o documento em capitulos conforme o sumario:
   - Cap. 0: Elementos pre-textuais (capa, folha de rosto, resumo, abstract, listas)
   - Cap. 1: Introducao
   - Cap. 2: Referencial Teorico (MPT, PMPT, BL)
   - Cap. 3: Metodologia
   - Cap. 4: Resultados e Discussao
   - Cap. 5: Conclusao
   - Apendices A-L
3. Processe capitulo por capitulo, nunca o documento inteiro de uma vez.
4. Use o formato de saida padronizado descrito em cada onda para cada problema encontrado.
5. Nao corrija o documento original. Apenas produza relatorios .md com os achados.
6. Cite sempre a linha/paragrafo do texto-fonte ao reportar um problema.

---

## ONDA 1 - Ortografia, Gramatica e Estilo Academico

**Objetivo:** Varrer o texto palavra por palavra em busca de erros linguisticos e inadequacoes de estilo.

### 1.1 Ortografia
- Palavras grafadas incorretamente (erros de digitacao, trocas de letras)
- Acentuacao incorreta ou ausente
- Uso incorreto de maiusculas (nomes de teorias, modelos, instituicoes)
- Estrangeirismos sem grifo em italico (downside risk, backtesting, inputs, etc.)
- Abreviaturas nao definidas na primeira ocorrencia

### 1.2 Gramatica e Concordancia
- Concordancia verbal (sujeito diferente do verbo)
- Concordancia nominal (artigo/adjetivo diferente do substantivo em genero/numero)
- Regencia verbal e nominal (preposicoes incorretas: "ao inves de" vs. "em vez de", "a nivel de", etc.)
- Uso indevido de "onde" para referir pessoas ou situacoes nao-locativas
- Virgulas obrigatorias ausentes ou virgulas incorretas entre sujeito e predicado
- Gerundio nominalizado ("sendo que", "tendo em vista que" em excesso)
- Voz passiva excessiva que prejudica a clareza
- Pronomes relativos incorretos

### 1.3 Estilo Academico
- Linguagem informal ou coloquial (girias, contracoes, "a gente", "voce")
- Primeira pessoa do singular (devo, penso, acredito - proibida em TCC impessoal)
- Frases excessivamente longas (mais de 4 linhas sem pontuacao intermediaria)
- Pleonasmos e redundancias ("subir para cima", "resultado final")
- Termos vagos sem definicao ("varios", "muitos", "alguns estudos mostram")
- Paragrafos com apenas 1 frase (fragmentacao excessiva)
- Uso de "etc." sem exemplos suficientes antes

**Formato de saida - Onda 1:**
```
### [CAP. X] [TITULO DA SECAO] - Linha NNN
**Tipo:** Ortografia | Gramatica | Estilo
**Original:** "...trecho exato do texto..."
**Problema:** [descricao objetiva do erro]
**Sugestao:** "...trecho corrigido..."
**Severidade:** CRITICO | MEDIO | BAIXO
```

**Arquivo de saida:** docs/revisao_onda1_ortografia.md

---

## ONDA 2 - Referencias Bibliograficas ABNT

**Objetivo:** Auditar toda e qualquer citacao no texto e a lista de referencias ao final.

### Checklist - Citacoes no Texto (NBR 10520:2023)
- Toda afirmacao nao-propria tem citacao (AUTOR, ANO) ou AUTOR (ANO)
- A citacao e inserida ANTES do ponto final (.), nunca depois
- Citacoes com 3+ autores usam et al. (em italico ou nao, mas consistente)
- Citacoes de citacao (apud) usadas apenas quando o original e inacessivel
- Citacoes de paginas especificas para transcricoes diretas: (AUTOR, ANO, p. XX)
- Transcricoes diretas com mais de 3 linhas em bloco recuado (4 cm, fonte 10, sem aspas)
- Transcricoes diretas com ate 3 linhas entre aspas duplas no corpo do texto
- Nomes de autores no texto com apenas o sobrenome em maiusculas
- Consistencia: mesmo autor sempre referenciado da mesma forma

### Checklist - Lista de Referencias (NBR 6023:2018)
- Toda citacao no texto tem entrada correspondente na lista de referencias
- Toda entrada na lista tem citacao correspondente no texto ("referencia fantasma")
- Ordem alfabetica pelo sobrenome do primeiro autor
- Formatacao correta por tipo de fonte:
  - Artigo: SOBRENOME, Nome. Titulo. Periodico, local, v., n., p., ano.
  - Livro: SOBRENOME, Nome. Titulo. Ed. Local: Editora, ano.
  - Site: AUTOR/INST. Titulo. Local, ano. Disponivel em: URL. Acesso em: data.
  - Trabalho em anais: formato especifico com "In: NOME DO EVENTO..."
- Titulos de periodicos em negrito (nao o titulo do artigo)
- Titulos de livros em negrito
- Datas de acesso para fontes eletronicas
- Sobrenomes em versalete (CAPS) conforme NBR (opcional mas deve ser consistente)

### Checklist - Consistencia Cross-referencia
- Mapear todas as citacoes unicas no texto e verificar correspondencia 1:1 com a lista
- Verificar se o ANO na citacao bate com o ANO na referencia
- Verificar se o SOBRENOME na citacao bate com o primeiro autor na referencia

**Formato de saida - Onda 2:**
```
### [TIPO DE PROBLEMA] - [Localizacao]
**Citacao no texto:** (AUTOR, ANO) ou N/A
**Entrada na lista:** presente | ausente | incorreta
**Problema:** [descricao]
**Correcao sugerida:** [entrada ABNT completa]
**Severidade:** CRITICO | MEDIO | BAIXO
```

**Arquivo de saida:** docs/revisao_onda2_referencias.md

---

## ONDA 3 - Consistencia Terminologica e Revisao Matematica

**Objetivo:** Garantir que os mesmos conceitos sejam sempre nomeados da mesma forma e que todas as formulas, equacoes e notacoes matematicas estejam corretas e consistentes.

### Checklist - Terminologia

Construir uma tabela de termos e verificar consistencia ao longo de TODOS os capitulos:

| Conceito | Termos aceitaveis | Termos problematicos a procurar |
|---|---|---|
| Retorno minimo aceitavel | MAR, Minimum Acceptable Return | "retorno alvo" (quando nao equivalente), "benchmark de retorno" |
| Desvio de downside | Downside Deviation, TDD | "semi-desvio", "desvio semi" |
| CVaR | CVaR, ES, Expected Shortfall | "VaR condicional" (sem sigla), "valor esperado de risco" |
| Covariancia de Ledoit-Wolf | "estimador de Ledoit-Wolf", "encolhimento" | "regularizacao" (quando se refere a LW) |
| Momentum | momentum (italico) | "momento" (confundir com momentos estatisticos) |
| Out-of-sample | out-of-sample (italico), OOS | "fora da amostra" (verificar se usado consistentemente) |
| Look-ahead bias | look-ahead bias (italico), "vies de antecipacao" | uso alternado sem padronizacao |

- Verificar se siglas sao definidas na PRIMEIRA OCORRENCIA em cada capitulo
- Verificar se termos em ingles estao em italico consistentemente
- Verificar se o mesmo conceito nao aparece com traducoes diferentes em capitulos distintos

### Checklist - Matematica e Formulas
- Todas as variaveis definidas antes de seu uso
- Indices de somatorio corretos (limites superior e inferior)
- Dimensoes matriciais consistentes (N x N para covariancia, N x 1 para pesos)
- Notacao LPM consistente: LPM_n(tau) ou variante, mas sempre igual
- Formula do CVaR: verificar se usa alpha ou (1-alpha) consistentemente
- Formula do Indice de Sortino: confirmar se denominador e sqrt(LPM_2) ou TDD
- Formula do Kappa: confirmar expoente 1/n ou n-esima raiz
- Formula do Omega: verificar limites de integracao
- Equacoes numeradas? Se sim, numeracao sequencial por capitulo
- Equacoes referenciadas no texto sempre que aplicavel

**Formato de saida - Onda 3:**
```
### [TERMINOLOGIA | FORMULA] - [Localizacao]
**Original:** "...trecho ou formula..."
**Problema:** [inconsistencia ou erro detectado]
**Sugestao:** "...versao correta/padronizada..."
**Impacto:** MUDA_SIGNIFICADO | GERA_CONFUSAO | APENAS_ESTILO
```

**Arquivo de saida:** docs/revisao_onda3_terminologia_matematica.md

---

## ONDA 4 - Coerencia Logica, Argumentacao e Alinhamento Metodologia x Resultados

**Objetivo:** Ler o TCC como um avaliador da banca, verificando se os argumentos sao solidos, as transicoes logicas, e se o que foi prometido na metodologia foi entregue nos resultados.

### Checklist - Estrutura Argumentativa
- O problema de pesquisa esta claramente definido na Introducao?
- Os objetivos geral e especificos sao mensuraveis e verificaveis?
- Cada secao do referencial teorico contribui diretamente para justificar as escolhas metodologicas?
- Ha "fantasmas bibliograficos": secoes que citam muita literatura mas nao conectam com o estudo?
- As limitacoes declaradas no Cap. 3 aparecem novamente na discussao dos resultados?
- O Cap. 5 (Conclusao) responde diretamente a questao de pesquisa do Cap. 1?

### Checklist - Alinhamento Metodologia x Resultados
- Cada estrategia descrita no Cap. 3 aparece nos resultados do Cap. 4?
- Cada metrica de desempenho definida no Cap. 3 (Sharpe, Sortino, MaxDD, CAGR, Turnover) aparece nas tabelas do Cap. 4?
- Os 16 modelos listados no Cap. 3 estao todos reportados no Cap. 4?
- O periodo OOS declarado (2015-03-02 a 2025-12-30) e consistente em todo o Cap. 4?
- O custo transacional (50 bps) e mencionado de forma consistente ao discutir os resultados?

### Checklist - Transicoes e Fluxo
- Cada secao termina com uma frase de transicao para a proxima?
- Os titulos de secao refletem corretamente o conteudo do paragrafo?
- Paragrafos iniciam com a ideia principal (estrutura dedutiva)?
- Ha repeticao de ideias inteiras em secoes diferentes (redundancia estrutural)?
- O nivel de detalhe e consistente entre capitulos?

### Checklist - Discussao dos Resultados
- Cada resultado e interpretado (nao apenas descrito)?
- Ha comparacao com a literatura para cada achado principal?
- Resultados contraditórios ou surpreendentes (MinCDaR MaxDD -81,81%) sao adequadamente discutidos?
- O desempenho do BL_classico (Sharpe 0,511) e contextualizado frente ao mercado brasileiro?

**Formato de saida - Onda 4:**
```
### [PROBLEMA LOGICO/ESTRUTURAL] - [Cap. X / Secao]
**Descricao:** [o que esta faltando ou inconsistente]
**Trecho relevante (original):** "..."
**Impacto na avaliacao da banca:** COMPROMETE_NOTA | GERA_QUESTIONAMENTO | SUGESTAO_MELHORIA
**Sugestao de acao:** [adicionar texto / mover secao / reformular / excluir]
```

**Arquivo de saida:** docs/revisao_onda4_coerencia_logica.md

---

## ONDA 5 - Formatacao ABNT e Qualidade de Tabelas, Figuras e Elementos Graficos

**Objetivo:** Verificar conformidade com ABNT NBR 14724:2011 e a qualidade dos elementos nao-textuais.

### Checklist - Formatacao Geral (NBR 14724:2011)
- Margens: superior 3 cm, inferior 2 cm, esquerda 3 cm, direita 2 cm
- Fonte: Times New Roman ou Arial, tamanho 12 no corpo, 10 em citacoes longas e notas
- Espacamento: 1,5 no corpo; simples em citacoes longas, notas, resumo, referencias
- Paragrafos: recuo de 1,25 cm na primeira linha ou espacamento entre paragrafos (nao ambos)
- Numeracao de paginas: superior direito, a partir da introducao
- Titulos de capitulos: maiusculas, negrito
- Subtitulos: minusculas (exceto primeira palavra), numerados hierarquicamente (2.1, 2.1.1)
- Notas de rodape: numeracao sequencial, fonte 10, espaco simples

### Checklist - Elementos Pre-textuais
- Capa: nome da instituicao, autor, titulo, cidade e ano
- Folha de rosto: orientador identificado corretamente
- Ficha catalografica: presente ou placeholder claramente marcado
- Resumo: max. 500 palavras, sem paragrafos, palavras-chave ao final (3-5)
- Abstract: idem em ingles, Keywords ao final
- Lista de figuras / tabelas / abreviaturas: presentes e atualizadas
- Sumario: numeracao das secoes bate com numeracao real no documento

### Checklist - Tabelas
- Titulo ACIMA da tabela (NBR 14724:2011)
- Fonte ABAIXO da tabela
- Numeracao sequencial: "Tabela 1", "Tabela 2"... sem pulos ou repeticoes
- Toda tabela referenciada no texto ("...conforme a Tabela 6...")
- Ausencia de tabelas "orfas" (tabelas sem referencia no texto)
- VERIFICAR: Tabela 8 ausente do indice (bug identificado na versao 0550)
- Colunas com cabecalhos claros e unidades especificadas (%, a.a., etc.)

### Checklist - Figuras e Graficos
- Titulo ABAIXO da figura (oposto as tabelas)
- Fonte ABAIXO do titulo
- Numeracao sequencial: "Figura 1", "Figura 2"...
- Toda figura referenciada no texto
- Legendas de graficos legiveis em escala de cinza (para impressao P&B)
- Eixos dos graficos rotulados com unidades

### Checklist - Equacoes
- Equacoes numeradas no lado direito entre parenteses: (2.1), (3.5), etc.
- Numeracao por capitulo ou global (escolher e manter consistente)
- Variaveis em italico no corpo do texto
- Matrizes e vetores em negrito

**Formato de saida - Onda 5:**
```
### [FORMATACAO | TABELA | FIGURA | EQUACAO] - [Localizacao]
**Nao-conformidade:** [descricao da violacao da norma]
**Norma violada:** NBR 14724:2011 | NBR 10520 | outro
**Correcao necessaria:** [acao especifica no documento]
**Severidade:** VIOLA_NORMA_OBRIGATORIA | PRATICA_RECOMENDADA | COSMETICO
```

**Arquivo de saida:** docs/revisao_onda5_formatacao_abnt.md

---

## SUMARIO EXECUTIVO - Gerado apos todas as 5 ondas

Arquivo: docs/SUMARIO_REVISAO_FINAL.md

Estrutura:

# Sumario Executivo - Revisao Completa do TCC

## Estatisticas Gerais
- Total de problemas encontrados: N
- Por severidade: CRITICO X | MEDIO Y | BAIXO Z
- Por onda: Onda 1: N | Onda 2: N | Onda 3: N | Onda 4: N | Onda 5: N
- Por capitulo: Cap. 1: N | Cap. 2: N | ...

## Top 10 Problemas Criticos
[lista dos 10 mais graves com localizacao exata]

## Problemas por Capitulo
[tabela com contagem por tipo e por capitulo]

## Checklist Final de Aprovacao
- Todos os problemas CRITICOS resolvidos
- Todos os problemas MEDIOS resolvidos ou documentados como escolha consciente
- Ficha catalografica inserida
- Tabela 8 inserida no indice
- Lista de referencias sem "fantasmas"
- Agradecimentos preenchidos
- Dedicatoria corrigida ("meus" familiares)

---

## CONTEXTO DO DOCUMENTO

**Titulo:** Moderna Teoria das Carteiras no Mercado de Acoes Brasileiro: Comparacao entre Otimizadores e Inputs

**Autor:** Pedro Augusto Pinheiro Reis
**Orientador:** Prof. Dr. Moises Ferreira da Cunha
**Instituicao:** UFG - Faculdade de Administracao, Ciencias Contabeis e Ciencias Economicas
**Curso:** Ciencias Contabeis

**Estrutura do TCC (728 paragrafos extraidos):**
- Cap. 1 - Introducao (linhas 49-57)
- Cap. 2 - Referencial Teorico (linhas 58-417)
  - 2.1-2.6: MPT (Markowitz, CAPM, Sharpe, Fronteira Eficiente)
  - 2.7-2.15: PMPT (LPM, CVaR, Sortino, Omega, Kappa)
  - 2.16-2.17: Black-Litterman
- Cap. 3 - Metodologia (linhas 418-529)
- Cap. 4 - Resultados e Discussao (linhas 530-580)
- Cap. 5 - Conclusao (linhas 581+)
- Apendices A-L

**Problemas ja conhecidos (verificar se foram corrigidos):**
1. Possivel ticker FICT3 contaminando o universo de 118 ativos
2. MinCDaR com MaxDD de -81,81% - causa tecnica nao diagnosticada no texto
3. Tabela 8 referenciada no Cap. 4 mas ausente do indice de tabelas
4. Dedicatoria: "todos os meu familiares" -> "todos os meus familiares"
5. Agradecimentos: placeholder "(Opcional)" sem texto real
6. Ficha catalografica: ainda como link/placeholder

**Arquivos de referencia disponiveis para cruzamento:**
- docs/PMPT_corrigido_referencias.md - lista ABNT validada do Cap. 2 PMPT
- docs/RELATORIO_AUDITORIA_CODIGO.md - auditoria tecnica do pipeline Python
- docs/Teoria Pos-Moderna de Portfolio_ Revisao.md - versao rascunho do cap. PMPT

---

## MODO DE EXECUCAO RECOMENDADO

Para cada onda:
  Para cada capitulo (0, 1, 2, 3, 4, 5, Apendices):
    1. Extrair texto do capitulo
    2. Aplicar checklist da onda atual
    3. Registrar todos os problemas encontrados no formato padrao
    4. Salvar no arquivo de saida da onda
  Fim
  Reportar contagem de problemas encontrados na onda
Fim
Gerar SUMARIO_REVISAO_FINAL.md

DICA DE EFICIENCIA: Execute as ondas 1 e 3 em paralelo (nao dependem uma da outra).
Execute a onda 2 de forma independente (requer cruzamento de listas).
Execute as ondas 4 e 5 somente apos 1, 2 e 3 estarem completas.
