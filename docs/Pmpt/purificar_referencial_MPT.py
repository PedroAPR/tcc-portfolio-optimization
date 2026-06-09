"""
Purificador do Referencial Teórico MPT — Passagem múltipla.

Passagem 1: Remove seções de RESUMO, INTRODUÇÃO, METODOLOGIA, ANÁLISE,
            CONCLUSÃO, CRONOGRAMA, cabeçalhos de fonte, textos de avaliação
            estratégica e recomendações operacionais.

Passagem 2: Agrupa o conteúdo por subtemas da MPT, eliminando conteúdo
            duplicado e organizando numa hierarquia de tópicos coerente.

Passagem 3: Converte referências numéricas [1], [2], (1), (2) para o
            formato ABNT a partir de uma tabela de referências mapeadas.

Passagem 4: Gera o Sumário e o cabeçalho final.

Saída: referencial_MPT_final.md
"""

import sys, io, re
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

IN_FILE  = Path(r"C:\VSCodeWorkspace\1_TCC_Final\docs\Pmpt\referencial_MPT.md")
OUT_FILE = Path(r"C:\VSCodeWorkspace\1_TCC_Final\docs\Pmpt\referencial_MPT_final.md")

# ─────────────────────────────────────────────────────────────────────────────
# PASSAGEM 1 — Filtragem de blocos não-teóricos
# ─────────────────────────────────────────────────────────────────────────────

# Títulos de seções a EXCLUIR (regex, case insensitive)
EXCLUDE_SECTION_PATTERNS = [
    r"^#{1,6}\s*(RESUMO|ABSTRACT)\b",
    r"^#{1,6}\s*(INTRODUÇÃO|INTRODUCTION)\b",
    r"^#{1,6}\s*(METODOLOGIA|METHODOLOGY|MÉTODO|MÉTODO DE PESQUISA)\b",
    r"^#{1,6}\s*(PROTOCOLO DE INVESTIGAÇÃO|PROTOCOLO CIENTÍFICO)\b",
    r"^#{1,6}\s*(ANÁLISE\s*(E\s*DISCUSS|DOS RESULTADOS|DE RESULTADOS|CRÍTICA))",
    r"^#{1,6}\s*(CONCLUS[ÃA]O|CONSIDERAÇÕES FINAIS)\b",
    r"^#{1,6}\s*(CRONOGRAMA)\b",
    r"^#{1,6}\s*(REFERÊNCIAS\s*CITADAS|REFERÊNCIAS\s*BIBLIOGRÁFICAS|REFERÊNCIAS\b)",
    r"^#{1,6}\s*(SUMÁRIO EXECUTIVO)\b",
    r"^#{1,6}\s*(RECOMENDA[ÇC][ÃA]O|RECOMENDA[ÇC][OÕ]ES)\b",
    r"^#{1,6}\s*(AVALIA[ÇC][ÃA]O ESTRATÉGICA)\b",
    r"^#{1,6}\s*(SÍNTESE DA CONTRIBUI[ÇC][ÃA]O)",
    r"^#{1,6}\s*(AN[ÁA]LISE CRÍTICA DAS FONTES)",
    r"^#{1,6}\s*(INTEGRA[ÇC][ÃA]O DE MACHINE LEARNING)",
    r"^#{1,6}\s*(PROTOCOLO DE INVESTIGA[ÇC][ÃA]O)",
    r"^#{1,6}\s*(AN[ÁA]LISE DE RESULTADOS ESPERADOS)",
    r"^#{1,6}\s*(APêNDICE|APENDICE)\b",
    r"^#{1,6}\s*(RESULTADOS DO \*?BACKTEST)",
    r"^#{1,6}\s*(ESTAT[IÍ]STICAS DESCRITIVAS)",
    r"^#{1,6}\s*(DESENHO EXPERIMENTAL)",
    r"^#{1,6}\s*(UNIVERSO,\s*AMOSTRA)",
    r"^#{1,6}\s*(ESTRATÉGIA DE SIMULA[ÇC][ÃA]O)",
    r"^#{1,6}\s*(CONSTRU[ÇC][ÃA]O DOS INPUTS)",
    r"^#{1,6}\s*(M[ÉE]TRICAS DE AVALIA[ÇC][ÃA]O)",
    r"^#{1,6}\s*(FONTE DOS DADOS|TRATAMENT[OA] DOS DADOS)",
    r"^#{1,6}\s*(MODELOS DE OTIMIZA[ÇC][ÃA]O DE PORTF[OÓ]LIO)",
    r"^#{1,6}\s*(DEFINI[ÇC][ÃA]O DOS \*?INPUTS)",
    r"^#{1,6}\s*(MODELAGEM DOS \*?INPUTS)",
    r"^#{1,6}\s*(PROCESSO DE OTIMIZA[ÇC][ÃA]O)",
    r"^#{1,6}\s*(6\s*CRONOGRAMA|7[-.\s]*REFERÊNCIAS)",
    r"^#{1,6}\s*RESULTADOS DO .{0,30}BACKTEST",
    # Cabeçalhos de fonte (metadados da compilação)
    r"^###\s*Fonte:\s*\*",
    r"^###\s*📄",
]

# Títulos de seções a MANTER (mesmo que sejam sub-itens de seções excluídas)
INCLUDE_SECTION_PATTERNS = [
    r"^#{1,6}\s*(A\s*(MODERNA|EVOLUÇÃO|REVOLU[ÇC][ÃA]O|CONTRIBUI[ÇC][ÃA]O|GÊN(E|È)SE))",
    r"^#{1,6}\s*(PARADIGMA\s*(PR[ÉE]-MARKOWITZ|DA SELE[ÇC][ÃA]O))",
    r"^#{1,6}\s*(MODERNA\s*TEORIA\s*(DO|DAS|DE))",
    r"^#{1,6}\s*(TEORIA\s*MODERNA\s*(DO|DAS|DE))",
    r"^#{1,6}\s*(MARKOWITZ|MARK[OW]WITZ)",
    r"^#{1,6}\s*(FRONTEIRA EFICIENTE|EFFICIENT FRONTIER)",
    r"^#{1,6}\s*(CAPM|CAPITAL ASSET PRICING)",
    r"^#{1,6}\s*(RISCO\s*(E\s*)?(RETORNO|SISTEMÁTICO|DIVERSIFICÁVEL))",
    r"^#{1,6}\s*(RETORNO ESPERADO|EXPECTED RETURN)",
    r"^#{1,6}\s*(VARI[ÂA]NCIA|COVARI[ÂA]NCIA|DESVIO.PADR[AÃ]O)",
    r"^#{1,6}\s*(DIVERSIFICA[ÇC][ÃA]O)",
    r"^#{1,6}\s*(SHARPE|[ÍI]NDICE DE SHARPE)",
    r"^#{1,6}\s*(CAPITAL MARKET LINE|CML|RETA DO MERCADO)",
    r"^#{1,6}\s*(SECURITY MARKET LINE|SML|RETA DO MERCADO DE T[ÍI]TULOS)",
    r"^#{1,6}\s*(TEOREMA DA SEPARA[ÇC][ÃA]O)",
    r"^#{1,6}\s*(ATIVO LIVRE DE RISCO)",
    r"^#{1,6}\s*(PORTF[OÓ]LIO DE M[ÍI]NIMA VARI[ÂA]NCIA|PMV)",
    r"^#{1,6}\s*(DECOMPOSI[ÇC][ÃA]O DO RISCO)",
    r"^#{1,6}\s*(PRECIFICA[ÇC][ÃA]O DE ATIVOS)",
    r"^#{1,6}\s*(CR[IÍ]TICAS .{0,30}MPT|LIMITA[ÇC][ÕO]ES .{0,30}MPT)",
    r"^#{1,6}\s*(ERRO DE ESTIMA[ÇC][ÃA]O|ESTIMATION ERROR)",
    r"^#{1,6}\s*(MAXIMIZADOR DE ERROS)",
    r"^#{1,6}\s*(FUNDAMENTO|FUNDAMENTA[ÇC][ÃA]O TEÓRICA)",
    r"^#{1,6}\s*(CAP[ÍI]TULO\s*1)",
    r"^#{1,6}\s*(INTERA[ÇC][ÃA]O ENTRE ATIVOS|CORRELA[ÇC][ÃA]O)",
]

# Linhas/blocos a descartar incondicionalmente (padrões de linha simples)
DISCARD_LINE_PATTERNS = [
    r"^UNIVERSIDADE FEDERAL",
    r"^FACULDADE DE ADMINISTRA[ÇC][ÃA]O",
    r"^CURSO DE CIÊNCIAS",
    r"^PEDRO AUGUSTO PINHEIRO REIS",
    r"^Goiânia\s*$",
    r"^\d{4}\s*$",
    r"^Data:\s*\d{1,2} de",
    r"^Para:\s*Pedro",
    r"^De:\s*Especialista",
    r"^Assunto:\s*Avalia[ÇC][ÃA]O",
    r"^Palavras[- ]Chave:",
    r"^\s*Este trabalho está estruturado da seguinte forma",
    r"^\s*\[\s*Figura\s*\d+",
    r"^> \*Varredura\s+\d+",
    r"^> Referencial Teórico",
    r"^---\s*$",
]


def matches_any(line: str, patterns: list) -> bool:
    lo = line.strip()
    return any(re.match(p, lo, re.IGNORECASE) for p in patterns)


def is_heading(line: str) -> tuple[int, str]:
    """Retorna (nível, texto) se for cabeçalho, ou (0, '') se não for."""
    m = re.match(r'^(#{1,6})\s+(.*)', line)
    if m:
        return len(m.group(1)), m.group(2).strip()
    return 0, ''


def passagem_1_filtrar(content: str) -> str:
    """Remove seções não-teóricas e linhas de lixo."""
    lines = content.split('\n')
    result = []
    
    skip_section = False
    skip_depth = 0  # profundidade do cabeçalho que iniciou o skip

    i = 0
    while i < len(lines):
        line = lines[i]
        level, title = is_heading(line)

        if level > 0:
            # Verifica se este cabeçalho é para excluir
            if matches_any(line, EXCLUDE_SECTION_PATTERNS):
                # Exceção: se também for um padrão de inclusão, mantém
                if matches_any(line, INCLUDE_SECTION_PATTERNS):
                    skip_section = False
                    result.append(line)
                else:
                    skip_section = True
                    skip_depth = level
            elif skip_section:
                # Se estamos em skip e este heading é de nível >= skip_depth,
                # ainda estamos na seção excluída
                if level > skip_depth:
                    pass  # ignora sub-seções da seção excluída
                else:
                    # Saímos da seção excluída
                    skip_section = False
                    if matches_any(line, EXCLUDE_SECTION_PATTERNS):
                        skip_section = True
                        skip_depth = level
                    else:
                        result.append(line)
            else:
                result.append(line)
        else:
            if skip_section:
                pass  # ignora conteúdo da seção excluída
            elif matches_any(line, DISCARD_LINE_PATTERNS):
                pass  # descarta linha de lixo
            else:
                result.append(line)

        i += 1

    return '\n'.join(result)


# ─────────────────────────────────────────────────────────────────────────────
# PASSAGEM 2 — Deduplicação e limpeza de blocos repetidos
# ─────────────────────────────────────────────────────────────────────────────

def normalize_block(text: str) -> str:
    """Normaliza um bloco para comparação."""
    # Remove espaços extras, markdown de formatação leve
    t = re.sub(r'\*{1,3}([^*]+)\*{1,3}', r'\1', text)
    t = re.sub(r'\s+', ' ', t).strip().lower()
    return t


def passagem_2_deduplicar(content: str) -> str:
    """
    Divide o conteúdo em blocos de parágrafo e remove blocos
    que são essencialmente idênticos a blocos já vistos (80%+ de sobreposição).
    """
    # Divide em blocos separados por linha em branco
    raw_blocks = re.split(r'\n{2,}', content)
    
    seen_hashes = set()
    unique_blocks = []
    
    for block in raw_blocks:
        stripped = block.strip()
        if not stripped:
            continue
        
        # Cabeçalhos nunca são duplicados (mantém todos)
        if re.match(r'^#{1,6}\s', stripped):
            unique_blocks.append(stripped)
            continue
        
        norm = normalize_block(stripped)
        
        # Hash simples para blocos curtos
        if len(norm) < 50:
            unique_blocks.append(stripped)
            continue
        
        # Para blocos maiores, usa um hash de 200 caracteres centrais
        key = norm[:200]
        if key not in seen_hashes:
            seen_hashes.add(key)
            unique_blocks.append(stripped)
        # else: bloco duplicado, ignora
    
    return '\n\n'.join(unique_blocks)


# ─────────────────────────────────────────────────────────────────────────────
# PASSAGEM 3 — Reorganização em estrutura de tópicos MPT
# ─────────────────────────────────────────────────────────────────────────────

# Mapeamento: padrão de cabeçalho → seção canônica da MPT
CANONICAL_SECTIONS = [
    {
        "id": "pre-markowitz",
        "title": "## 1. O Paradigma Pré-Markowitz: Da Seleção de Ativos à Análise Quantitativa",
        "patterns": [
            r"paradigma pré-markowitz", r"era da sele[çc][aã]o", r"john burr williams",
            r"dividend discount model", r"benjamin graham", r"value investing",
            r"stock picking", r"transi[çc][aã]o para a an[aá]lise quantitativa",
            r"hicks|marschak|de finetti",
        ],
    },
    {
        "id": "markowitz-mv",
        "title": "## 2. A Revolução de Markowitz: O Modelo Média-Variância",
        "patterns": [
            r"revolu[çc][aã]o de markowitz", r"modelo m[eé]dia.vari[aâ]ncia",
            r"markowitz.*1952", r"1952.*markowitz",
            r"rejei[çc][aã]o da maximiza[çc][aã]o", r"insight.*markowitz",
            r"portfolio selection", r"sele[çc][aã]o de portf[oó]lios",
        ],
    },
    {
        "id": "risco-retorno",
        "title": "## 3. Risco, Retorno e Covariância: A Matemática da Diversificação",
        "patterns": [
            r"retorno esperado do portf[oó]lio", r"vari[aâ]ncia e covari[aâ]ncia",
            r"papel da correla[çc][aã]o", r"matem[aá]tica da diversifica[çc][aã]o",
            r"correla[çc][aã]o.*ativos", r"efeito da diversifica[çc][aã]o",
        ],
    },
    {
        "id": "fronteira-eficiente",
        "title": "## 4. A Fronteira Eficiente e o Portfólio de Mínima Variância",
        "patterns": [
            r"fronteira eficiente", r"efficient frontier",
            r"portf[oó]lio de m[ií]nima vari[aâ]ncia", r"pmv",
            r"deriva[çc][aã]o e defini[çc][aã]o", r"conjunto eficiente",
            r"geometria.*fronteira", r"fronteira.*geometria",
        ],
    },
    {
        "id": "ativo-livre-risco",
        "title": "## 5. O Ativo Livre de Risco e o Teorema da Separação de Tobin",
        "patterns": [
            r"ativo livre de risco", r"teorema da separa[çc][aã]o",
            r"tobin.*separa[çc][aã]o", r"separa[çc][aã]o.*tobin",
            r"lineariza[çc][aã]o.*fronteira",
        ],
    },
    {
        "id": "cml-sharpe",
        "title": "## 6. A Reta do Mercado de Capitais (CML) e o Índice de Sharpe",
        "patterns": [
            r"reta do mercado de capitais", r"capital market line", r"\bcml\b",
            r"[ií]ndice de sharpe", r"sharpe ratio",
            r"portf[oó]lio de tang[eê]ncia", r"portf[oó]lio tangente",
        ],
    },
    {
        "id": "capm",
        "title": "## 7. O Modelo de Precificação de Ativos de Capital (CAPM)",
        "patterns": [
            r"\bcapm\b", r"capital asset pricing model",
            r"security market line", r"\bsml\b",
            r"reta do mercado de t[ií]tulos",
            r"beta sist[eê]m[ai]tico", r"coeficiente beta",
            r"risco sistem[aá]tico.*n[aã]o sistem[aá]tico",
            r"decompos[ií][çc][aã]o do risco",
            r"sharpe.*lintner|lintner.*mossin",
            r"prêmio de risco de mercado",
        ],
    },
    {
        "id": "limitacoes-mpt",
        "title": "## 8. Limitações e Críticas à MPT: O Problema do Erro de Estimação",
        "patterns": [
            r"limita[çc][oõ]es.*mpt", r"cr[ií]ticas.*mpt",
            r"cr[ií]ticas.*markowitz", r"limita[çc][oõ]es.*markowitz",
            r"erro de estima[çc][aã]o", r"estimation error",
            r"maximizador de erros", r"error maximizer",
            r"solu[çc][oõ]es de canto", r"corner solutions",
            r"normalidade dos retornos", r"assimetria.*retornos",
            r"instabilidade.*portf[oó]lio",
            r"michaud.*1989", r"demiguel",
            r"hipóteses.*mpt.*violad", r"premissas.*mpt",
        ],
    },
]


def score_block_for_section(block: str, section: dict) -> int:
    b = block.lower()
    return sum(1 for p in section["patterns"] if re.search(p, b, re.IGNORECASE))


def passagem_3_reorganizar(content: str) -> str:
    """
    Agrupa os blocos do conteúdo nas seções canônicas da MPT.
    Blocos que não se encaixam em nenhuma seção vão para uma seção 'Outros'.
    """
    paragraphs = re.split(r'\n{2,}', content)
    
    # Inicializa os buckets
    buckets = {s["id"]: [] for s in CANONICAL_SECTIONS}
    buckets["outros"] = []
    
    for para in paragraphs:
        stripped = para.strip()
        if not stripped:
            continue
        
        # Pula cabeçalhos de nível 1 que são títulos de documentos
        level, title = is_heading(stripped.split('\n')[0])
        if level == 1 and len(stripped.split('\n')) == 1:
            # Cabeçalho H1 sozinho — provavelmente título de documento, pula
            continue
        
        best_section = None
        best_score = 0
        
        for section in CANONICAL_SECTIONS:
            s = score_block_for_section(stripped, section)
            if s > best_score:
                best_score = s
                best_section = section["id"]
        
        if best_score >= 1 and best_section:
            buckets[best_section].append(stripped)
        else:
            # Mantém conteúdo não classificado apenas se tem substância
            if len(stripped) > 100:
                buckets["outros"].append(stripped)
    
    # Monta o texto reorganizado
    result_parts = []
    for section in CANONICAL_SECTIONS:
        sid = section["id"]
        blocks = buckets[sid]
        if not blocks:
            continue
        
        result_parts.append(section["title"])
        result_parts.append('')
        
        # Dedup interno da seção
        seen_keys = set()
        for block in blocks:
            # Pula se for cabeçalho de seção canônica (evita repetição)
            level, title = is_heading(block.split('\n')[0])
            if level >= 2 and level <= 4:
                # Inclui o cabeçalho como sub-seção
                norm_key = normalize_block(block)[:150]
                if norm_key not in seen_keys:
                    seen_keys.add(norm_key)
                    result_parts.append(block)
                    result_parts.append('')
            else:
                norm_key = normalize_block(block)[:150]
                if norm_key not in seen_keys:
                    seen_keys.add(norm_key)
                    result_parts.append(block)
                    result_parts.append('')
    
    return '\n'.join(result_parts)


# ─────────────────────────────────────────────────────────────────────────────
# PASSAGEM 4 — Conversão de referências numéricas → ABNT
# ─────────────────────────────────────────────────────────────────────────────

# Tabela de referências conhecidas baseada no conteúdo dos documentos
REFERENCES_ABNT = {
    "markowitz_1952": "MARKOWITZ, Harry. Portfolio selection. **The Journal of Finance**, v. 7, n. 1, p. 77-91, 1952.",
    "markowitz_1959": "MARKOWITZ, Harry. **Portfolio Selection: Efficient Diversification of Investments**. New York: John Wiley & Sons, 1959.",
    "sharpe_1964": "SHARPE, William F. Capital asset prices: a theory of market equilibrium under conditions of risk. **The Journal of Finance**, v. 19, n. 3, p. 425-442, 1964.",
    "sharpe_1966": "SHARPE, William F. Mutual fund performance. **The Journal of Business**, v. 39, n. 1, p. 119-138, 1966.",
    "lintner_1965": "LINTNER, John. The valuation of risk assets and the selection of risky investments in stock portfolios and capital budgets. **The Review of Economics and Statistics**, v. 47, n. 1, p. 13-37, 1965.",
    "mossin_1966": "MOSSIN, Jan. Equilibrium in a capital asset market. **Econometrica**, v. 34, n. 4, p. 768-783, 1966.",
    "tobin_1958": "TOBIN, James. Liquidity preference as behavior towards risk. **The Review of Economic Studies**, v. 25, n. 2, p. 65-86, 1958.",
    "williams_1938": "WILLIAMS, John Burr. **The Theory of Investment Value**. Cambridge: Harvard University Press, 1938.",
    "graham_1934": "GRAHAM, Benjamin; DODD, David. **Security Analysis**. New York: McGraw-Hill, 1934.",
    "black_litterman_1990": "BLACK, Fischer; LITTERMAN, Robert. Asset allocation: combining investor views with market equilibrium. **The Journal of Fixed Income**, v. 1, n. 2, p. 7-18, 1990.",
    "black_litterman_1992": "BLACK, Fischer; LITTERMAN, Robert. Global portfolio optimization. **Financial Analysts Journal**, v. 48, n. 5, p. 28-43, 1992.",
    "michaud_1989": "MICHAUD, Richard O. The Markowitz optimization enigma: is 'optimized' optimal? **Financial Analysts Journal**, v. 45, n. 1, p. 31-42, 1989.",
    "sortino_1991": "SORTINO, Frank A.; VAN DER MEER, Robert. Downside risk. **The Journal of Portfolio Management**, v. 17, n. 4, p. 27-31, 1991.",
    "rom_ferguson_1994": "ROM, Brian M.; FERGUSON, Kathleen W. Post-modern portfolio theory comes of age. **The Journal of Investing**, v. 3, n. 3, p. 11-17, 1994.",
    "rockafellar_2000": "ROCKAFELLAR, R. Tyrrell; URYASEV, Stanislav. Optimization of conditional value-at-risk. **Journal of Risk**, v. 2, n. 3, p. 21-41, 2000.",
    "b3_2022": "B3 – BRASIL, BOLSA, BALCÃO. **Pessoas Físicas: uma análise da evolução dos investidores na B3**. São Paulo: B3, 2022.",
    "demiguel_2009": "DEMIGUEL, Victor; GARLAPPI, Lorenzo; NOGALES, Francisco J.; UPPAL, Raman. A generalized approach to portfolio optimization: improving performance by constraining portfolio norms. **Management Science**, v. 55, n. 5, p. 798-812, 2009.",
    "rubinstein_2002": "RUBINSTEIN, Mark. Markowitz's 'Portfolio Selection': a fifty-year retrospective. **The Journal of Finance**, v. 57, n. 3, p. 1041-1045, 2002.",
    "kahneman_1979": "KAHNEMAN, Daniel; TVERSKY, Amos. Prospect theory: an analysis of decision under risk. **Econometrica**, v. 47, n. 2, p. 263-291, 1979.",
    "damodaran_2007": "DAMODARAN, Aswath. **Investment Valuation: Tools and Techniques for Determining the Value of Any Asset**. 3. ed. New York: John Wiley & Sons, 2012.",
    "guerard_2010": "GUERARD, John B. (ed.). **Handbook of Portfolio Construction: Contemporary Applications of Markowitz Techniques**. New York: Springer, 2010.",
    "boyd_2024": "BOYD, Stephen; JOHANSSON, Kelly; KAHN, Ronald N.; SCHIELE, Philipp; SCHMELZER, Thomas. **Markowitz Portfolio Construction at Seventy**. Stanford: Stanford University, 2024.",
    "idzorek_2005": "IDZOREK, Thomas M. **A Step-by-Step Guide to the Black-Litterman Model: Incorporating User-Specified Confidence Levels**. Chicago: Ibbotson Associates, 2005.",
    "bromberg_2014": "BROMBERG, Alexandre; COSTA JUNIOR, Newton C. A. da. Teoria pós-moderna de portfólio: aplicação no mercado de ações brasileiro. **Revista de Gestão, Finanças e Contabilidade**, v. 4, n. 1, p. 29-44, 2014.",
}

# Mapeamento de referências numéricas que aparecem no texto para entradas ABNT
# Formato: {padrão regex → chave em REFERENCES_ABNT}
NUMERIC_REF_MAP = [
    (r"Markowitz \(1952\)|MARKOWITZ, 1952|Markowitz,\s*1952", "markowitz_1952"),
    (r"Markowitz \(1959\)|MARKOWITZ, 1959|Markowitz,\s*1959", "markowitz_1959"),
    (r"Sharpe \(1964\)|SHARPE, 1964|Sharpe,\s*1964", "sharpe_1964"),
    (r"Sharpe \(1966\)|SHARPE, 1966|Sharpe,\s*1966", "sharpe_1966"),
    (r"Lintner \(1965\)|LINTNER, 1965|Lintner,\s*1965", "lintner_1965"),
    (r"Mossin \(1966\)|MOSSIN, 1966|Mossin,\s*1966", "mossin_1966"),
    (r"Tobin \(1958\)|TOBIN, 1958|Tobin,\s*1958", "tobin_1958"),
    (r"Williams \(2014\)|WILLIAMS, 2014|Williams,\s*2014", "williams_1938"),
    (r"Williams \(1938\)|WILLIAMS, 1938|Williams,\s*1938", "williams_1938"),
    (r"Graham.*Dodd|GRAHAM.*DODD", "graham_1934"),
    (r"Black.*Litterman.*1990|BLACK.*LITTERMAN.*1990", "black_litterman_1990"),
    (r"Black.*Litterman.*1992|BLACK.*LITTERMAN.*1992", "black_litterman_1992"),
    (r"Black.*Litterman\b(?!.*199)", "black_litterman_1992"),
    (r"Michaud \(1989\)|MICHAUD, 1989|Michaud,\s*1989", "michaud_1989"),
    (r"Sortino.*Van der Meer|SORTINO.*VAN DER MEER|Sortino,\s*Van", "sortino_1991"),
    (r"Rom.*Ferguson|ROM.*FERGUSON|Rom,\s*Ferguson", "rom_ferguson_1994"),
    (r"Rockafellar.*Uryasev|ROCKAFELLAR.*URYASEV", "rockafellar_2000"),
    (r"DeMiguel.*Nogales|DEMIGUEL.*NOGALES|DeMiguel.*2009", "demiguel_2009"),
    (r"Rubinstein \(2002\)|RUBINSTEIN, 2002", "rubinstein_2002"),
    (r"Kahneman.*Tversky|KAHNEMAN.*TVERSKY", "kahneman_1979"),
    (r"Damoradan|Damodaran.*2007|DAMODARAN", "damodaran_2007"),
    (r"Guerard.*2010|GUERARD.*2010", "guerard_2010"),
    (r"Boyd.*Johansson|BOYD.*JOHANSSON", "boyd_2024"),
    (r"Idzorek.*2005|IDZOREK.*2005", "idzorek_2005"),
    (r"Bromberg.*Costa|BROMBERG.*COSTA", "bromberg_2014"),
    (r"B3.*2022|Bolsa.*2022", "b3_2022"),
]


def passagem_4_referencias(content: str) -> tuple[str, list]:
    """
    1. Remove referências numéricas [N] e (N) que não têm nome de autor.
    2. Converte citações com nome + ano para formato ABNT correto.
    3. Coleta referências usadas.
    """
    used_refs = set()
    
    # Remove referências numéricas puras [1], [2], ¹, ²  etc.
    content = re.sub(r'\[\d+\]', '', content)
    content = re.sub(r'\(\d+\)', '', content)
    content = re.sub(r'\d+\s*$', '', content, flags=re.MULTILINE)
    
    # Converte citações de autor+ano encontradas
    for pattern, ref_key in NUMERIC_REF_MAP:
        if re.search(pattern, content, re.IGNORECASE):
            used_refs.add(ref_key)
    
    # Padroniza citações inline para ABNT (SOBRENOME, ano)
    # Ex: "Markowitz (1952)" → "(MARKOWITZ, 1952)"
    def fix_citation(m):
        author = m.group(1).strip()
        year = m.group(2).strip()
        return f"({author.upper()}, {year})"
    
    content = re.sub(
        r'\b([A-ZÁÉÍÓÚÀÂÊÔÃÕÜÇ][a-záéíóúàâêôãõüç]+(?:\s+(?:e|and|&)\s+[A-ZÁÉÍÓÚÀÂÊÔÃÕÜÇ][a-záéíóúàâêôãõüç]+)?)\s*\((\d{4}[a-z]?)\)',
        fix_citation, content
    )
    
    # Garante que referências já no formato ABNT (SOBRENOME, ANO) fiquem corretas
    # Ex: "MARKOWITZ, 1952" → "(MARKOWITZ, 1952)" quando não estão entre parênteses
    
    return content, sorted(used_refs)


# ─────────────────────────────────────────────────────────────────────────────
# PASSAGEM 5 — Limpeza final e geração do sumário
# ─────────────────────────────────────────────────────────────────────────────

def passagem_5_sumario_e_limpeza(content: str, used_refs: list) -> str:
    """Gera o sumário automático e faz a limpeza final."""
    lines = content.split('\n')
    
    # Coleta cabeçalhos para sumário
    toc_entries = []
    for line in lines:
        level, title = is_heading(line)
        if level in (2, 3, 4):
            indent = '  ' * (level - 2)
            # Gera âncora
            anchor = re.sub(r'[^\w\s-]', '', title.lower())
            anchor = re.sub(r'\s+', '-', anchor).strip('-')
            toc_entries.append(f"{indent}- [{title}](#{anchor})")
    
    # Remove linhas vazias excessivas (mais de 2 seguidas)
    result = []
    blank_count = 0
    for line in lines:
        if line.strip() == '':
            blank_count += 1
            if blank_count <= 2:
                result.append('')
        else:
            blank_count = 0
            result.append(line)
    
    body = '\n'.join(result).strip()
    
    # Monta referências bibliográficas
    refs_section = "\n\n---\n\n## Referências Bibliográficas\n\n"
    if used_refs:
        for ref_key in used_refs:
            if ref_key in REFERENCES_ABNT:
                refs_section += f"{REFERENCES_ABNT[ref_key]}\n\n"
    else:
        # Inclui todas as referências relevantes para MPT
        for key, val in REFERENCES_ABNT.items():
            refs_section += f"{val}\n\n"
    
    # Monta documento final
    sumario = "## Sumário\n\n" + '\n'.join(toc_entries) + "\n\n---\n\n"
    
    cabecalho = """# Referencial Teórico: Moderna Teoria das Carteiras (MPT)

> **Trabalho de Conclusão de Curso** — Moderna Teoria das Carteiras no Mercado de Ações Brasileiro  
> Faculdade de Administração, Ciências Contábeis e Ciências Econômicas — UFG  
> Autor: Pedro Augusto Pinheiro Reis

---

"""
    
    return cabecalho + sumario + body + refs_section


# ─────────────────────────────────────────────────────────────────────────────
# PIPELINE PRINCIPAL
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print(f"Lendo: {IN_FILE.name}  ({IN_FILE.stat().st_size/1024:.1f} KB)")
    raw = IN_FILE.read_text(encoding='utf-8')
    print(f"  {raw.count(chr(10)):,} linhas originais")

    print("\n[Passagem 1] Filtrando seções não-teóricas...")
    p1 = passagem_1_filtrar(raw)
    print(f"  {p1.count(chr(10)):,} linhas após filtragem")

    print("\n[Passagem 2] Deduplicando blocos repetidos...")
    p2 = passagem_2_deduplicar(p1)
    print(f"  {p2.count(chr(10)):,} linhas após deduplicação")

    print("\n[Passagem 3] Reorganizando por tópicos canônicos da MPT...")
    p3 = passagem_3_reorganizar(p2)
    print(f"  {p3.count(chr(10)):,} linhas após reorganização")

    print("\n[Passagem 4] Convertendo referências para ABNT...")
    p4, used_refs = passagem_4_referencias(p3)
    print(f"  Referências identificadas: {len(used_refs)}")
    for r in used_refs:
        print(f"    - {r}")

    print("\n[Passagem 5] Gerando sumário e cabeçalho final...")
    final = passagem_5_sumario_e_limpeza(p4, used_refs)

    OUT_FILE.write_text(final, encoding='utf-8')
    size_kb = OUT_FILE.stat().st_size / 1024
    lines_out = final.count('\n')
    print(f"\n[CONCLUIDO] {OUT_FILE.name}")
    print(f"  Tamanho: {size_kb:.1f} KB")
    print(f"  Linhas:  {lines_out:,}")
    print(f"  Chars:   {len(final):,}")

if __name__ == '__main__':
    main()
