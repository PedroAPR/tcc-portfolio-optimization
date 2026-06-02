# Modelo — Ten Simple Rules para Notebooks Jupyter

Rubrica reutilizável para auditar qualquer notebook do pipeline contra as
**"Ten Simple Rules for Writing and Sharing Computational Analyses in Jupyter Notebooks"**.

> **Referência (citar no TCC):** Rule A, Birmingham A, Zuniga C, Altintas I, Huang S-C, Knight R,
> Moshiri N, Nguyen MH, Rosenthal SB, Pérez F, Rose PW. *Ten simple rules for writing and sharing
> computational analyses in Jupyter Notebooks.* PLOS Computational Biology. 2019;15(7):e1007007.
> https://doi.org/10.1371/journal.pcbi.1007007

As regras se organizam em três fases do ciclo de desenvolvimento (Fig. 1 do artigo):
**Organizar e documentar** (Regras 1–3) → **Padrões de qualidade do código** (Regras 4–7) →
**Disponibilizar e compartilhar** (Regras 8–10).

## Como usar este modelo

1. Copie a seção "Ficha de Avaliação" abaixo para um arquivo por notebook.
2. Para cada regra, preencha **Evidência** (onde, no notebook, a regra é/​não é atendida) e
   atribua um **Status**: `✅ Atende` · `🟡 Parcial` · `🔴 Não atende` · `⚪ N/A / Não verificável`.
3. Liste as **Ações** concretas para subir de nível.
4. Consolide no quadro-resumo ao final.

---

## Ficha de Avaliação — `<nome_do_notebook>.ipynb`

### Fase I — Organizar e documentar

#### Regra 1 — *Tell a story for an audience*
Texto interleaveado deve contar uma história com **início** (apresenta o tema), **meio** (descreve os passos)
e **fim** (interpreta os resultados). Descrever não só *o que* foi feito, mas *por quê*, como os passos se
conectam e o que significam. Calibrar o nível de explicação ao público (aqui: banca de TCC; e o "eu do futuro").

- **Status:**
- **Evidência:**
- **Ações:**

#### Regra 2 — *Document the process, not just the results*
Documentar o raciocínio e as decisões no momento em que ocorrem (inclusive becos sem saída). Fazer toda a
limpeza dentro do notebook (sem ajuste manual de figuras/arquivos). Incluir **nome, contato e datas** da análise.

- **Status:**
- **Evidência:**
- **Ações:**

#### Regra 3 — *Use cell divisions to make steps clear*
Cada célula = um passo significativo (um "parágrafo"/uma função/uma tarefa). Markdown rotulando a célula acima;
documentação de baixo nível em comentários de código. Evitar células longas (> ~100 linhas/1 página).
Cabeçalhos descritivos + sumário; dividir notebooks longos e manter um índice.

- **Status:**
- **Evidência:**
- **Ações:**

### Fase II — Padrões de qualidade do código

#### Regra 4 — *Modularize code*
Evitar código duplicado: encapsular o que se repete em **funções**; o que é reusado entre projetos/notebooks
vira **módulo/pacote/biblioteca**. Modularizar economiza espaço, facilita manutenção e depuração.

- **Status:**
- **Evidência:**
- **Ações:**

#### Regra 5 — *Record dependencies*
Registrar dependências e **versões** de forma legível por máquina (ex.: `requirements.txt`, `environment.yml`,
ou impressão das versões no próprio notebook). Sem isso, a análise não é re-executável de forma confiável.

- **Status:**
- **Evidência:**
- **Ações:**

#### Regra 6 — *Use version control*
Manter o notebook sob controle de versão (Git). Atenção: o diff nativo do `.ipynb` (JSON) é ilegível — usar
ferramentas como `nbdime`/`jupytext` e limpar *outputs* antes de commitar ajuda. Permite recuperar passos perdidos.

- **Status:**
- **Evidência:**
- **Ações:**

#### Regra 7 — *Build a pipeline*
Quando a análise vira recorrente, transformá-la em pipeline: **parametrizar** (constantes no topo, não espalhadas),
garantir execução ponta-a-ponta reproduzível, e — em projetos multi-notebook — manter um notebook-índice
(*workflow*) que orquestra/aponta para as etapas.

- **Status:**
- **Evidência:**
- **Ações:**

### Fase III — Disponibilizar e compartilhar

#### Regra 8 — *Share and explain your data*
Disponibilizar os dados necessários para rodar (ou explicar onde obtê-los), com **descrição, local e data de
download**, dicionário de variáveis e licença. Quando os dados forem proprietários, declarar isso e documentar
a origem mesmo sem redistribuir.

- **Status:**
- **Evidência:**
- **Ações:**

#### Regra 9 — *Design your notebooks to be read, run, and explored*
Projetar para ser **lido** (narrativa), **executado** (Kernel → Restart & Run All sem erros; sem *hidden state*)
e **explorado** (parâmetros ajustáveis; opcionalmente Binder/ambiente pronto). Pré-requisitos de execução documentados.

- **Status:**
- **Evidência:**
- **Ações:**

#### Regra 10 — *Advocate for open research*
Compartilhar publicamente quando possível, com **licença** explícita (código e, quando permitido, dados),
favorecendo reprodutibilidade e reuso. Em TCC: repositório público do código mesmo que a base seja restrita.

- **Status:**
- **Evidência:**
- **Ações:**

---

## Quadro-resumo

| Regra | Tema | Status | Ação prioritária |
| :---: | :--- | :---: | :--- |
| 1 | Contar uma história | | |
| 2 | Documentar o processo | | |
| 3 | Divisão clara de células | | |
| 4 | Modularizar código | | |
| 5 | Registrar dependências | | |
| 6 | Controle de versão | | |
| 7 | Construir um pipeline | | |
| 8 | Compartilhar/explicar dados | | |
| 9 | Ler, rodar e explorar | | |
| 10 | Pesquisa aberta | | |

**Legenda:** ✅ Atende · 🟡 Parcial · 🔴 Não atende · ⚪ N/A / Não verificável

> Observação de manutenção: as Regras 1, 2 e 8 (texto/narrativa/dados) são as que mais sofrem *drift* ao longo
> do tempo, porque misturam prosa estática com resultados gerados. Reexecutar e re-sincronizar antes de fechar.
