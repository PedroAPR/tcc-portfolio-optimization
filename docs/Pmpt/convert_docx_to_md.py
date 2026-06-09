"""
Converte todos os arquivos .docx de uma pasta para arquivos .md em outra pasta.
Usa python-docx para extrair o conteúdo e gera markdown compatível.
"""

import sys
import os
import re

# Garante saída UTF-8 no console do Windows
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
from pathlib import Path
from docx import Document
from docx.oxml.ns import qn


INPUT_DIR = Path(r"C:\VSCodeWorkspace\1_TCC_Final\docs\Pmpt\docx")
OUTPUT_DIR = Path(r"C:\VSCodeWorkspace\1_TCC_Final\docs\Pmpt\md")


def get_table_md(table) -> str:
    """Converte uma tabela docx em markdown."""
    lines = []
    for i, row in enumerate(table.rows):
        cells = [cell.text.replace('\n', ' ').replace('|', '\\|').strip() for cell in row.cells]
        lines.append('| ' + ' | '.join(cells) + ' |')
        if i == 0:
            # Linha separadora de cabeçalho
            lines.append('| ' + ' | '.join(['---'] * len(cells)) + ' |')
    return '\n'.join(lines)


def get_image_placeholder(para) -> str | None:
    """Detecta se o parágrafo contém uma imagem."""
    for run in para.runs:
        if run._r.findall(qn('a:blip'), namespaces={'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}):
            return '![Imagem]'
        # Verifica drawing inline
        drawings = run._r.findall('.//' + qn('w:drawing'))
        if drawings:
            return '![Imagem]'
    return None


def run_has_bold(run) -> bool:
    return run.bold is True


def run_has_italic(run) -> bool:
    return run.italic is True


def get_run_text(run) -> str:
    text = run.text
    if not text.strip():
        return text
    if run_has_bold(run) and run_has_italic(run):
        return f'***{text}***'
    elif run_has_bold(run):
        return f'**{text}**'
    elif run_has_italic(run):
        return f'*{text}*'
    return text


def get_paragraph_md(para) -> str:
    """Converte um parágrafo docx em linha markdown."""
    style_name = para.style.name if para.style else ''

    # Detecta imagem inline
    img = get_image_placeholder(para)
    if img:
        return img

    # Monta o texto com formatação inline
    inline_text = ''.join(get_run_text(r) for r in para.runs)

    # Cabeçalhos
    heading_map = {
        'Heading 1': '# ',
        'Heading 2': '## ',
        'Heading 3': '### ',
        'Heading 4': '#### ',
        'Heading 5': '##### ',
        'Heading 6': '###### ',
        'Title': '# ',
        'Subtitle': '## ',
    }
    for key, prefix in heading_map.items():
        if style_name.startswith(key):
            return prefix + inline_text.strip()

    # Lista com marcadores
    if style_name.startswith('List Bullet') or style_name.startswith('List Paragraph'):
        # Verifica o nível de indentação
        level = 0
        if para.paragraph_format.left_indent:
            try:
                level = int(para.paragraph_format.left_indent.pt // 36)
            except Exception:
                level = 0
        indent = '  ' * level
        # Verifica se é lista numerada
        numPr = para._p.find(qn('w:numPr'))
        if numPr is not None:
            return f'{indent}1. {inline_text.strip()}'
        return f'{indent}- {inline_text.strip()}'

    # Lista numerada
    if style_name.startswith('List Number'):
        return f'1. {inline_text.strip()}'

    # Parágrafo normal
    return inline_text


def docx_to_md(docx_path: Path, md_path: Path):
    """Converte um arquivo .docx para .md."""
    doc = Document(docx_path)
    md_lines = []

    # Itera por todos os elementos do body preservando a ordem
    body = doc.element.body
    for child in body.iterchildren():
        tag = child.tag.split('}')[-1] if '}' in child.tag else child.tag

        if tag == 'p':
            # Parágrafo
            from docx.text.paragraph import Paragraph
            para = Paragraph(child, doc)
            line = get_paragraph_md(para)
            md_lines.append(line)

        elif tag == 'tbl':
            # Tabela
            from docx.table import Table
            table = Table(child, doc)
            md_lines.append('')
            md_lines.append(get_table_md(table))
            md_lines.append('')

        elif tag == 'sdt':
            # Structured Document Tag (conteúdo estruturado) - pula
            pass

    # Remove linhas em branco excessivas (mais de 2 seguidas)
    result = []
    blank_count = 0
    for line in md_lines:
        if line.strip() == '':
            blank_count += 1
            if blank_count <= 2:
                result.append('')
        else:
            blank_count = 0
            result.append(line)

    md_content = '\n'.join(result).strip() + '\n'

    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(md_content, encoding='utf-8')


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    docx_files = sorted(INPUT_DIR.glob('*.docx'))
    txt_files = sorted(INPUT_DIR.glob('*.txt'))

    print(f"Encontrados {len(docx_files)} arquivo(s) .docx e {len(txt_files)} arquivo(s) .txt")
    print(f"Destino: {OUTPUT_DIR}\n")

    success = 0
    errors = []

    # Converte .docx
    for docx_path in docx_files:
        md_name = docx_path.stem + '.md'
        md_path = OUTPUT_DIR / md_name
        try:
            docx_to_md(docx_path, md_path)
            print(f"  [OK] {docx_path.name}  ->  {md_name}")
            success += 1
        except Exception as e:
            print(f"  [ERRO] {docx_path.name}  ->  {e}")
            errors.append((docx_path.name, str(e)))

    # Converte .txt → .md (cópia simples)
    for txt_path in txt_files:
        md_name = txt_path.stem + '.md'
        md_path = OUTPUT_DIR / md_name
        try:
            content = txt_path.read_text(encoding='utf-8', errors='replace')
            md_path.write_text(content, encoding='utf-8')
            print(f"  [OK] {txt_path.name}  ->  {md_name}")
            success += 1
        except Exception as e:
            print(f"  [ERRO] {txt_path.name}  ->  {e}")
            errors.append((txt_path.name, str(e)))

    print(f"\n{'='*60}")
    print(f"Convertidos com sucesso: {success}")
    if errors:
        print(f"Erros ({len(errors)}):")
        for name, err in errors:
            print(f"  - {name}: {err}")
    else:
        print("Nenhum erro!")


if __name__ == '__main__':
    main()
