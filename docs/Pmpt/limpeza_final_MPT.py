"""
Passagem adicional de limpeza no referencial_MPT_final.md:
- Remove sumário redundante (duplicatas de entradas)
- Remove parágrafos sobre instruções/procedimentos de escrita de TCC
- Remove blocos de "Caminho A/B", "Ação Imediata", recomendações operacionais
- Remove texto de "RESUMO (A SER TOTALMENTE REESCRITO)"
- Remove linhas de cronograma/referências inline da entrega
- Reconstrói sumário limpo
"""

import sys, io, re
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

IN_FILE  = Path(r"C:\VSCodeWorkspace\1_TCC_Final\docs\Pmpt\referencial_MPT_final.md")
OUT_FILE = Path(r"C:\VSCodeWorkspace\1_TCC_Final\docs\Pmpt\referencial_MPT_final.md")

content = IN_FILE.read_text(encoding='utf-8')

# ─── BLOCO 1: Remove parágrafos operacionais / instrucionais ─────────────────

# Padrões de parágrafos/blocos que NÃO pertencem ao referencial teórico
PARA_DISCARD_PATTERNS = [
    # Instruções de escrita
    r"\*\*RESUMO \(A SER TOTALMENTE REESCRITO\)\*\*",
    r"Ignorar o Resumo de",
    r"Escrever um novo \(máx\.",
    r"\(Contexto\):",
    r"\(Objetivo\):",
    r"\(Metodologia\):",
    r"\(Resultados\):",
    r"\(Conclusão\):",
    r"\(Ajustar\)\. Sugestões:",
    # Caminho A / Caminho B
    r"Caminho A \(O TCC",
    r"Caminho B \(O TCC",
    r"Este caminho \*abraça\*",
    r"Nova Questão de Pesquisa",
    r"Novo Desenho Experimental",
    r"Ação Imediata",
    r"Ações Imediatas para o Cap\.",
    # Tabela de cronograma
    r"Tabela \d+ - Cronograma da Pesquisa",
    r"Cronograma da Pesquisa",
    # Referências inline de entregas antigas
    r"^7-REFERÊNCIAS\s*$",
    r"^Berk, J\.; Demarzo",
    r"^Bodie, Z\., Kane",
    r"^CHIAN, Swee C\.",
    r"^Damodaran, A\. \. Strategic",
    r"^DEMIGUEL, Victor; NOGALES",
    r"^Elton, E\. J\.",
    r"^Fabozzi, F\. J\.",
    r"^Markowitz, H\. M\. \. Portfolio",
    r"^Markowitz, H\. \. Portfolio",
    r"^Reilly, F\. K\.",
    r"^SANTOS, André A\. P\.",
    r"^Vernimmen, P\.",
    r"^\(Referências sobre PMPT",
    # Diagnóstico/procedimento de correção ABNT
    r"Diagnóstico no TCC:",
    r"Procedimento de Correção:",
    r"\*\*De:\*\* \(MARKOWITZ",
    r"\*\*Para:\*\* \(Markowitz",
    r"\*\*De:\*\* \(BLACK",
    r"\*\*Para:\*\* \(Black",
    r"Incorreto:.*risco sist",
    r"Correto:.*risco sist",
    # Sumário executivo de avaliação (já foi filtrado mas pode restar)
    r"Tabela Sugerida para o TCC",
    r"Proposta de Matriz de Competição",
    r"Implicações deste Desenho",
    r"Ao comparar \*horizontalmente\*",
    r"Ao comparar \*verticalmente\*",
    r"Ao comparar \*diagonalmente\*",
    r"O Portfólio \d+ \(1/N\)",
    r"Este relatório fornece uma análise crítica e recomendações estratégicas",
    r"Este relatório está estruturado em quatro partes:",
    r"\*\*Análise Estrutural:\*\*",
    r"\*\*Auditoria do Referencial",
    r"\*\*Dissecação da Metodologia",
    r"\*\*Recomendações Estratégicas",
    # Texto de manual de procedimentos
    r"Manual de Procedimentos e Prompt Operacional",
    r"Instruções Gerais para o Discente",
    r"FASE \d+: Varredura Normativa",
    r"FASE \d+: Reescrita do Referencial",
    r"FASE \d+: Refinamento Metodológico",
    # Lixo diverso
    r"Tabela \d+: Proposta de Matriz",
    r"Tabela \d+: Matriz de Convergência",
    r"Conclusão do Relatório Crítico",
    r"relatório técnico atua.*como um manual",
    r"objetivos de otimização robustos.*MAD.*CVaR",
]

def should_discard_para(para: str) -> bool:
    """Verifica se o parágrafo deve ser descartado."""
    for pattern in PARA_DISCARD_PATTERNS:
        if re.search(pattern, para, re.IGNORECASE | re.MULTILINE):
            return True
    return False

# ─── BLOCO 2: Remove headings que não são de referencial teórico ─────────────

HEADING_DISCARD_PATTERNS = [
    r"^#{1,6}\s*\d+\.\s*(Pilar Normativo|Pilar Teórico|Pilar Metodológico)",
    r"^#{1,6}\s*(Manual de Procedimentos)",
    r"^#{1,6}\s*(Instruções Gerais)",
    r"^#{1,6}\s*(FASE \d+:)",
    r"^#{1,6}\s*(Diagnóstico no TCC)",
    r"^#{1,6}\s*(Procedimento de Correção)",
    r"^#{1,6}\s*(Conclusão do Relatório Crítico)",
    r"^#{1,6}\s*(Análise Estrutural|Auditoria do|Dissecação da)",
    r"^#{1,6}\s*(Recomendações Estratégicas)",
    r"^#{1,6}\s*(Tabela \d+:.*Cronograma|Cronograma da Pesquisa)",
    r"^#{1,6}\s*\d+\.\s*Introdução:.*Imperativo da Robustez",
    r"^#{1,6}\s*\d+\.\s*Pilar",
    r"^#{1,6}\s*\d+\.\s*A Evolução da Grafia",
    r"^#{1,6}\s*\d+\.\s*A Lógica da Pontuação",
    r"^#{1,6}\s*\d+\.\s*O Uso de.*et al",
    r"^#{1,6}\s*(LSTM e o Espectro|O Desafio do Benchmark|Custos de Transação)",
    r"^#{1,6}\s*(Alpha.*Jensen|Beta.*Coeficiente Beta.*SML)(?!.*CAPM)",
    r"^#{1,6}\s*Referencial Teórico: Moderna Teoria",  # Remove título H1 duplicado
]

def should_discard_heading(line: str) -> bool:
    for pattern in HEADING_DISCARD_PATTERNS:
        if re.match(pattern, line, re.IGNORECASE):
            return True
    return False

# ─── BLOCO 3: Filtragem por parágrafo ────────────────────────────────────────

# Separa o documento em: cabeçalho fixo (até ---), sumário, e corpo
# Para reescrever o sumário corretamente

# Divide em blocos
raw_blocks = re.split(r'\n{2,}', content)

filtered_blocks = []
skip_until_next_heading = False

for block in raw_blocks:
    stripped = block.strip()
    if not stripped:
        continue
    
    # Verifica o primeiro heading do bloco
    first_line = stripped.split('\n')[0]
    level = len(re.match(r'^(#{0,6})', first_line).group(1))
    is_heading = level > 0 and re.match(r'^#{1,6}\s', first_line)
    
    if is_heading:
        if should_discard_heading(first_line):
            skip_until_next_heading = True
            continue
        else:
            skip_until_next_heading = False
    
    if skip_until_next_heading:
        continue
    
    if should_discard_para(stripped):
        continue
    
    # Remove linhas individuais de lixo dentro do bloco
    lines = stripped.split('\n')
    clean_lines = []
    for line in lines:
        discard_line = False
        for pat in PARA_DISCARD_PATTERNS:
            if re.search(pat, line, re.IGNORECASE):
                discard_line = True
                break
        if not discard_line:
            clean_lines.append(line)
    
    if clean_lines:
        filtered_blocks.append('\n'.join(clean_lines))

# ─── BLOCO 4: Reconstrói o documento e gera novo sumário ─────────────────────

body_text = '\n\n'.join(filtered_blocks)

# Extrai cabeçalho fixo (linhas iniciais até o sumário antigo)
# Mantém apenas: título H1, citação de autoria, ---
fixed_header = """# Referencial Teórico: Moderna Teoria das Carteiras (MPT)

> **Trabalho de Conclusão de Curso** — Moderna Teoria das Carteiras no Mercado de Ações Brasileiro  
> Faculdade de Administração, Ciências Contábeis e Ciências Econômicas — UFG  
> Autor: Pedro Augusto Pinheiro Reis

---

"""

# Remove qualquer sumário existente no início do body
body_text = re.sub(
    r'^## Sumário\n.*?---\n\n',
    '',
    body_text,
    flags=re.DOTALL
)

# Remove o cabeçalho H1 duplicado que o script anterior inseriu
body_text = re.sub(
    r'^# Referencial Teórico: Moderna Teoria das Carteiras \(MPT\)\n+.*?---\n+',
    '',
    body_text,
    flags=re.DOTALL
)

# Gera novo sumário a partir dos headings do corpo
lines_for_toc = body_text.split('\n')
toc_entries = []
seen_toc = set()
for line in lines_for_toc:
    m = re.match(r'^(#{2,4})\s+(.*)', line)
    if m:
        level = len(m.group(1))
        title = m.group(2).strip()
        # Limpa title para âncora
        anchor = re.sub(r'[^\w\s-]', '', title.lower())
        anchor = re.sub(r'\s+', '-', anchor).strip('-')
        key = title[:80]
        if key not in seen_toc:
            seen_toc.add(key)
            indent = '  ' * (level - 2)
            toc_entries.append(f"{indent}- [{title}](#{anchor})")

sumario = "## Sumário\n\n" + '\n'.join(toc_entries) + "\n\n---\n\n"

# Remove linhas em branco excessivas
body_lines = body_text.split('\n')
clean_body = []
blank = 0
for l in body_lines:
    if l.strip() == '':
        blank += 1
        if blank <= 2:
            clean_body.append('')
    else:
        blank = 0
        clean_body.append(l)

final_body = '\n'.join(clean_body).strip()

final = fixed_header + sumario + final_body + '\n'

OUT_FILE.write_text(final, encoding='utf-8')
kb = OUT_FILE.stat().st_size / 1024
print(f"[CONCLUIDO] {OUT_FILE.name}")
print(f"  Tamanho: {kb:.1f} KB")
print(f"  Linhas:  {final.count(chr(10)):,}")
print(f"  Sumário: {len(toc_entries)} entradas")
