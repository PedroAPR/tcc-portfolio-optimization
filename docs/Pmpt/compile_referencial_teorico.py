"""
Compilador de Referencial Teórico do TCC — versão 2.
Realiza 3 varreduras focadas e gera seções bem delimitadas.
"""

import sys, io, re
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

MD_DIR   = Path(r"C:\VSCodeWorkspace\1_TCC_Final\docs\Pmpt\md")
OUT_FILE = Path(r"C:\VSCodeWorkspace\1_TCC_Final\docs\Pmpt\referencial_teorico_TCC.md")

# ─── Classificação manual + por palavras-chave ──────────────────────────────
# Cada arquivo pode pertencer a 1 ou mais temas.
# Prioridade: classificação manual >> score de keywords.

MANUAL_CLASS = {
    # MPT
    "Entrega_4_Pedro_Reis_TMP":           ["MPT"],
    "Entrega_6_Pedro_Reis_TMP":           ["MPT"],
    "Entrega_7_Pedro_Reis_TMP":           ["MPT"],
    "Geração de Texto Final do Capítulo_MPT":    ["MPT"],
    "Estrutura Tópicos Teoria Moderna Portfólio": ["MPT"],
    "Relatório Detalhado_ Teoria Moderna de Portfólio": ["MPT"],
    "Moderna Teoria das Carteiras no Mercado de Ações Brasileiro (Versão Corrigida)": ["MPT"],
    "Esboço":                             ["MPT"],
    "Esboço de Modelo de Portfólio Financeiro": ["MPT"],
    "Esboço de Pesquisa Modelos Financeiros Avançados": ["MPT"],
    "estrutura de topicos":               ["MPT"],
    "Estrutura Tópicos _2026":            ["MPT"],
    # PMPT
    "Capítulo 3_ Teoria Pós-Moderna de Portfólio (PMPT)": ["PMPT"],
    "Teoria Pós-Moderna de Portfólio_ Revisão":           ["PMPT"],
    "Geração de Texto Final do Capítulo_PMPT":            ["PMPT"],
    "Finanças_ FC e Fama-French":                         ["PMPT"],
    "Estrutura Teórica_ Integração FC e Fama-French":     ["PMPT"],
    # BL
    "Capítulo_ O Modelo Black-Litterman (Referencial Teórico)": ["BL"],
    "Condensar Documento_ Black Litterman":   ["BL"],
    "Estrutura Tópica_ Modelo Black-Litterman": ["BL"],
    "Modelo Black-Litterman_ Histórico e Críticas": ["BL"],
    "reescrita black litterman":              ["BL"],
    # Misto (vai aparecer em todas as seções)
    "Avaliação de Arquivos para TCC":         ["MPT", "PMPT", "BL"],
    "Correção de Metodologia e Erro de Servidor": ["MPT", "BL"],
    "Guia Detalhado para Estruturação de TCC": ["MPT"],
    "Manual de Correções e Atualização de Trabalho": ["MPT"],
    "Relatório Crítico de Trabalho Acadêmico": ["MPT", "PMPT"],
    "Tese_ Crítica e Roteiro de Validação":   ["MPT", "PMPT", "BL"],
    "Estrutura Teórica para Tese Financeira": ["MPT", "PMPT", "BL"],
    "Estrutura Teórica  de capitulos":        ["MPT", "PMPT", "BL"],
    "Geração de Texto Final do Capítulo":     ["MPT"],
}

THEMES = {
    "MPT":  "Moderna Teoria das Carteiras (MPT)",
    "PMPT": "Pós-Moderna Teoria das Carteiras (PMPT)",
    "BL":   "Modelo Black-Litterman",
}

# Palavras-chave para extrair seções temáticas de arquivos mistos
SECTION_KEYWORDS = {
    "MPT": [
        "markowitz", "média-variância", "mean-variance", "fronteira eficiente",
        "efficient frontier", "capm", "capital asset pricing", "capital market line",
        "security market line", "sharpe ratio", "mínima variância",
        "portfólio ótimo", "carteira eficiente", "teoria moderna do portfólio",
        "moderna teoria das carteiras", "modern portfolio theory",
        "variância do portfólio", "risco sistemático", "risco não sistemático",
        "diversificação", "retorno esperado", "covariância", "correlação",
    ],
    "PMPT": [
        "pós-moderna", "pos-moderna", "pmpt", "semivariância", "semivariance",
        "downside risk", "sortino", "target return", "retorno alvo",
        "lower partial moment", "upside potential", "fama-french", "fama french",
        "three-factor", "três fatores", "five-factor", "cinco fatores",
        "value at risk", "var ", "cvar", "expected shortfall",
        "risco de queda", "assimetria", "skewness", "curtose", "kurtosis",
    ],
    "BL": [
        "black-litterman", "black litterman", "fisher black", "robert litterman",
        "views do investidor", "investor views", "prior de mercado",
        "retorno de equilíbrio", "market equilibrium", "retorno implícito",
        "implied return", "reverse optimization", "otimização reversa",
        "matriz omega", "tau ", "matriz p", "picking matrix",
        "posterior", "bayesian", "bayesiana", "bl model",
    ],
}


def read_file(path):
    try:
        return path.read_text(encoding='utf-8', errors='replace')
    except Exception as e:
        print(f"  [AVISO] {path.name}: {e}")
        return ""


def normalize_stem(stem: str) -> str:
    """Remove sufixo numérico entre parênteses."""
    return re.sub(r'\s*\(\d+\)$', '', stem).strip()


def score_line(line: str, keywords: list) -> int:
    lo = line.lower()
    return sum(1 for kw in keywords if kw in lo)


def extract_themed_blocks(content: str, theme_key: str) -> str:
    """
    Extrai do conteúdo apenas os parágrafos/seções relevantes para o tema.
    Mantém cabeçalhos pai como contexto.
    """
    keywords = SECTION_KEYWORDS[theme_key]
    lines = content.split('\n')
    
    # Scoring por parágrafo (agrupa linhas não-cabeçalho)
    result = []
    heading_stack = []   # pilha de cabeçalhos ativos
    para_lines = []
    para_score = 0
    
    def flush_para():
        nonlocal para_lines, para_score
        if para_lines and para_score > 0:
            # Inclui heading stack como contexto
            for h in heading_stack:
                if h not in result:
                    result.append(h)
                    result.append('')
            result.extend(para_lines)
            result.append('')
        para_lines = []
        para_score = 0
    
    for line in lines:
        m = re.match(r'^(#{1,6})\s', line)
        if m:
            flush_para()
            level = len(m.group(1))
            # Mantém apenas headings do nível atual e acima
            heading_stack = [h for h in heading_stack
                             if len(re.match(r'^(#+)', h).group(1)) < level]
            heading_stack.append(line)
        else:
            s = score_line(line, keywords)
            para_score += s
            para_lines.append(line)
    
    flush_para()
    
    extracted = '\n'.join(result).strip()
    
    # Se o arquivo inteiro é altamente relevante, retorna completo
    full_score = sum(score_line(l, keywords) for l in lines)
    if full_score >= 25:
        return content.strip()
    
    return extracted


def load_unique_files():
    """Carrega arquivos MD removendo duplicatas pelo nome base."""
    seen = {}
    for f in sorted(MD_DIR.glob('*.md')):
        base = normalize_stem(f.stem)
        if base not in seen:
            content = read_file(f)
            if content.strip():
                seen[base] = (f.name, content)
    return seen  # {base_stem: (filename, content)}


def classify_file(base_stem: str) -> list:
    """Retorna lista de temas para o arquivo."""
    # Busca na tabela manual
    for key, themes in MANUAL_CLASS.items():
        if key.lower() in base_stem.lower() or base_stem.lower() in key.lower():
            return themes
    # Fallback: todos os temas (arquivo genérico)
    return ["MPT", "PMPT", "BL"]


def build_section(theme_key: str, files_data: dict) -> str:
    """Constrói o bloco de conteúdo para um tema."""
    theme_label = THEMES[theme_key]
    print(f"\n{'='*65}")
    print(f"VARREDURA: {theme_label}")
    print(f"{'='*65}")
    
    blocks = []
    
    for base_stem, (filename, content) in files_data.items():
        themes = classify_file(base_stem)
        
        if theme_key not in themes:
            continue
        
        # Se é arquivo exclusivo deste tema → inclui completo
        if len(themes) == 1:
            extracted = content.strip()
            mode = "COMPLETO"
        else:
            # Arquivo misto → extrai apenas seções relevantes
            extracted = extract_themed_blocks(content, theme_key)
            mode = "FILTRADO"
        
        if not extracted:
            print(f"  [VAZIO]   {filename}")
            continue
        
        size = len(extracted)
        print(f"  [{mode}] {filename} ({size:,} chars)")
        
        blocks.append((base_stem, filename, extracted))
    
    print(f"\n  Total de fontes incluidas: {len(blocks)}")
    
    # Monta o texto da seção
    section_parts = []
    for stem, fname, text in blocks:
        sep = f"\n\n---\n\n### Fonte: *{stem}*\n\n"
        section_parts.append(sep + text)
    
    return '\n\n'.join(section_parts)


def main():
    print("Carregando arquivos...")
    files_data = load_unique_files()
    print(f"Arquivos unicos: {len(files_data)}")
    for stem, (fname, content) in files_data.items():
        print(f"  {fname} ({len(content):,} chars)")
    
    sections = {}
    for tk in ["MPT", "PMPT", "BL"]:
        sections[tk] = build_section(tk, files_data)
    
    # ─── Monta documento final ───────────────────────────────────────────────
    print("\n\nGerando documento final...")
    
    doc = f"""# Referencial Teórico — TCC: Otimização de Portfólio

> Documento compilado a partir de {len(files_data)} arquivos de pesquisa.
> Organizado em três blocos temáticos para leitura comparativa.

---

## Sumário

1. [Moderna Teoria das Carteiras (MPT)](#1-moderna-teoria-das-carteiras-mpt)
2. [Pós-Moderna Teoria das Carteiras (PMPT)](#2-pós-moderna-teoria-das-carteiras-pmpt)
3. [Modelo Black-Litterman](#3-modelo-black-litterman)

---

# 1. Moderna Teoria das Carteiras (MPT)

> *Varredura 1 — Conteúdo extraído de fontes com foco em Markowitz, fronteira eficiente, CAPM e otimização média-variância.*

{sections['MPT']}

---

# 2. Pós-Moderna Teoria das Carteiras (PMPT)

> *Varredura 2 — Conteúdo extraído de fontes sobre risco de downside, semivariância, Sortino, Fama-French e CVaR.*

{sections['PMPT']}

---

# 3. Modelo Black-Litterman

> *Varredura 3 — Conteúdo extraído de fontes sobre o modelo BL, views do investidor, equilíbrio de mercado e abordagem bayesiana.*

{sections['BL']}

---

*Fim do Referencial Teórico compilado.*
"""
    
    OUT_FILE.write_text(doc, encoding='utf-8')
    size_kb = OUT_FILE.stat().st_size / 1024
    lines   = doc.count('\n')
    chars   = len(doc)
    
    print(f"\n[CONCLUIDO] {OUT_FILE.name}")
    print(f"  Tamanho: {size_kb:.1f} KB")
    print(f"  Linhas:  {lines:,}")
    print(f"  Chars:   {chars:,}")

if __name__ == '__main__':
    main()
