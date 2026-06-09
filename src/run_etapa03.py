"""
run_etapa03.py
==============
Orquestrador da Etapa 3 do pipeline de otimização de carteiras.

Problema que resolve
--------------------
O NB03 original (03_01_Ingestao_Filtro_Liquidez_v3.ipynb) precisava rodar em DUAS
PASSAGENS com o Classificador de Integridade no meio, mas o orquestrador tratava
tudo como um único bloco atômico — e o Classificador gravava os resultados em
`data/` enquanto o NB03 os buscava em `data/Tickers/` (path mismatch).

Solução
-------
O NB03 foi dividido em três notebooks físicos:

  03_01a_Pre_Integridade.ipynb    — filtros de presença, IPO e ADTV;
                                    exporta universo_pos_liquidez.csv
  (03_01b)  ← Classificador v2   — lê universo_pos_liquidez.csv;
                                    grava tickers_excluidos_integridade.csv
  03_01c_Pos_Integridade.ipynb    — aplica a lista de exclusão;
                                    grava a matriz final e os logs de auditoria

Este script garante a execução nessa ordem e resolve o path mismatch injetando
a variável PASTA_SAIDA correta no Classificador via parâmetro de linha de comando
(nbconvert --ExecutePreprocessor.timeout e --parameters quando disponível, ou via
substituição temporária de célula).

Uso
---
  python run_etapa03.py               # executa a sequência completa
  python run_etapa03.py --dry-run     # imprime o plano sem executar
  python run_etapa03.py --skip-cache  # ignora cache e força re-execução

Integração com run_pipeline_force.py
-------------------------------------
O run_pipeline_force.py chama este script como subprocesso na posição da Etapa 3,
substituindo as duas entradas problemáticas do NB03 e do Classificador.
"""

import sys
import os
import time
import json
import hashlib
import shutil
import subprocess
import argparse
import tempfile
from pathlib import Path

# ── Encoding UTF-8 no Windows ─────────────────────────────────────────────────
sys.stdout.reconfigure(encoding="utf-8")

# ── Caminhos ──────────────────────────────────────────────────────────────────
SRC_DIR      = Path(__file__).resolve().parent
PROJECT_ROOT = SRC_DIR.parent
DATA_DIR     = PROJECT_ROOT / "data"
DIR_TICKERS  = DATA_DIR / "Tickers"

NB03A = SRC_DIR / "03_Filtro_Liquidez" / "03_01a_Pre_Integridade.ipynb"
NB03B = SRC_DIR / "11_Classificador_Integridade" / "Apendice_Classificador_Integridade_Universo_v2.ipynb"
NB03C = SRC_DIR / "03_Filtro_Liquidez" / "03_01c_Pos_Integridade.ipynb"

# Artefatos que fazem a ponte entre os três notebooks
ARQ_UNIVERSO = DIR_TICKERS / "universo_pos_liquidez.csv"
ARQ_EXCL     = DIR_TICKERS / "tickers_excluidos_integridade.csv"
ARQ_MATRIZ   = DATA_DIR / "Matriz_Precos" / "Matriz_precos_sanitizada.csv"

# Arquivo de cache desta etapa
CACHE_FILE   = SRC_DIR / ".etapa03_cache.json"


# ─────────────────────────────────────────────────────────────────────────────
# Utilidades
# ─────────────────────────────────────────────────────────────────────────────

def md5_nb_source(path: Path) -> str:
    """Hash MD5 do código-fonte do notebook (ignora outputs e metadados)."""
    hasher = hashlib.md5()
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
        for cell in nb.get("cells", []):
            hasher.update(cell.get("cell_type", "").encode())
            hasher.update("".join(cell.get("source", [])).encode())
    except Exception:
        hasher.update(path.read_bytes())
    return hasher.hexdigest()


def load_cache() -> dict:
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def save_cache(data: dict) -> None:
    try:
        CACHE_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except Exception as e:
        print(f"  [!] Não foi possível salvar o cache: {e}")


def run_notebook(nb_path: Path, label: str) -> bool:
    """Executa um notebook Jupyter via nbconvert --inplace."""
    cmd = [
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute",
        "--inplace",
        "--ExecutePreprocessor.timeout=3600",  # 1h máx
        str(nb_path),
    ]
    print(f"\n  [RUN] {label}")
    print(f"        {nb_path.relative_to(PROJECT_ROOT)}")
    t0 = time.perf_counter()
    try:
        result = subprocess.run(
            cmd,
            cwd=str(nb_path.parent),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        elapsed = time.perf_counter() - t0
        if result.returncode != 0:
            print(f"\n  [-] FALHA em {nb_path.name} após {elapsed:.1f}s")
            print("  ── STDERR ──────────────────────────────────────────────")
            # Exibe somente as últimas 40 linhas do stderr (nbconvert é verboso)
            lines = result.stderr.strip().splitlines()
            for line in lines[-40:]:
                print(f"    {line}")
            print("  ────────────────────────────────────────────────────────")
            return False
        print(f"  [OK] {label} concluído em {elapsed:.1f}s")
        return True
    except Exception as e:
        print(f"  [-] Falha crítica ao lançar nbconvert: {e}")
        return False


def patch_nb03b_pasta_saida(original: Path) -> Path:
    """
    Cria uma cópia temporária do Classificador v2 com PASTA_SAIDA corrigido para
    data/Tickers/ — resolve o path mismatch sem editar o notebook original (.ipynb
    não pode ser editado diretamente pela ferramenta de escrita de arquivos).

    Retorna o caminho da cópia temporária (que deve ser deletada após uso).
    """
    nb = json.loads(original.read_text(encoding="utf-8"))

    target_line_fragment = "PASTA_SAIDA"
    correct_value = str(DIR_TICKERS).replace("\\", "\\\\")

    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", []))
        if target_line_fragment not in source:
            continue

        new_source_lines = []
        for line in cell["source"]:
            if "PASTA_SAIDA" in line and "=" in line:
                # Substitui qualquer valor atual pelo caminho correto
                new_source_lines.append(
                    f"PASTA_SAIDA    = Path(r\"{DIR_TICKERS}\")  "
                    "# corrigido pelo run_etapa03.py\n"
                )
            else:
                new_source_lines.append(line)
        cell["source"] = new_source_lines
        break  # Só há uma célula de configuração

    # Grava em arquivo temporário no mesmo diretório (garante caminhos relativos)
    tmp_path = original.parent / "_nb03b_patched_temp.ipynb"
    tmp_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
    return tmp_path


def verificar_prereqs() -> None:
    """Verifica que os três notebooks físicos existem."""
    ausentes = [nb for nb in (NB03A, NB03B, NB03C) if not nb.exists()]
    if ausentes:
        for nb in ausentes:
            print(f"  [-] Notebook não encontrado: {nb}")
        raise SystemExit(
            "\n[ERRO] Um ou mais notebooks da Etapa 3 estão ausentes. "
            "Verifique os caminhos acima."
        )


# ─────────────────────────────────────────────────────────────────────────────
# Lógica principal
# ─────────────────────────────────────────────────────────────────────────────

def main(dry_run: bool = False, skip_cache: bool = False) -> None:
    banner = "=" * 70
    print(banner)
    print("  ORQUESTRADOR DA ETAPA 3 — FILTRO DE LIQUIDEZ + INTEGRIDADE")
    print(banner)
    print(f"  Projeto: {PROJECT_ROOT}")
    print(f"  Modo:    {'DRY-RUN (sem execução)' if dry_run else 'EXECUÇÃO REAL'}")
    print()

    # ── Valida notebooks ──────────────────────────────────────────────────────
    verificar_prereqs()

    # ── Cache ─────────────────────────────────────────────────────────────────
    cache = {} if skip_cache else load_cache()

    hash_03a = md5_nb_source(NB03A)
    hash_03b = md5_nb_source(NB03B)
    hash_03c = md5_nb_source(NB03C)

    cache_key = f"{hash_03a}|{hash_03b}|{hash_03c}"
    outputs_ok = ARQ_UNIVERSO.exists() and ARQ_EXCL.exists() and ARQ_MATRIZ.exists()

    if not skip_cache and cache.get("combined_hash") == cache_key and outputs_ok:
        print("  [SKIP] Código inalterado e todos os artefatos presentes.")
        print("         Use --skip-cache para forçar re-execução.")
        print(banner)
        return

    if dry_run:
        print("  Sequência que seria executada:")
        print(f"    1. {NB03A.relative_to(PROJECT_ROOT)}")
        print(f"    2. {NB03B.relative_to(PROJECT_ROOT)}  [com PASTA_SAIDA={DIR_TICKERS}]")
        print(f"    3. {NB03C.relative_to(PROJECT_ROOT)}")
        print(banner)
        return

    t_total = time.perf_counter()

    # ─────────────────────────────────────────────────────────────────────────
    # PASSO 1 — 03a: filtros de liquidez → exporta universo_pos_liquidez.csv
    # ─────────────────────────────────────────────────────────────────────────
    print("\n[1/3] 03a — Filtros de Presença / IPO / ADTV")
    DIR_TICKERS.mkdir(parents=True, exist_ok=True)
    ok = run_notebook(NB03A, "03_01a_Pre_Integridade")
    if not ok:
        raise SystemExit("[ERRO] Etapa 3a falhou. Pipeline interrompido.")

    if not ARQ_UNIVERSO.exists():
        raise SystemExit(
            f"[ERRO] 03a não gerou {ARQ_UNIVERSO.name}. "
            "Verifique o stdout do notebook acima."
        )
    print(f"  [OK] {ARQ_UNIVERSO.name} gerado com "
          f"{len(open(ARQ_UNIVERSO).readlines())-1} ativos")

    # ─────────────────────────────────────────────────────────────────────────
    # PASSO 2 — 03b (Classificador v2): avalia universo → tickers_excluidos_integridade.csv
    # ─────────────────────────────────────────────────────────────────────────
    print("\n[2/3] 03b — Classificador de Integridade (COTAHIST)")
    print(f"       PASTA_SAIDA será corrigido para: {DIR_TICKERS}")

    tmp_nb = None
    try:
        tmp_nb = patch_nb03b_pasta_saida(NB03B)
        ok = run_notebook(tmp_nb, "Classificador_Integridade_v2 [patch temporário]")
    finally:
        if tmp_nb and tmp_nb.exists():
            for attempt in range(5):
                try:
                    tmp_nb.unlink()
                    break
                except PermissionError:
                    time.sleep(1.0)
            else:
                print(f"  [!] Não foi possível remover {tmp_nb.name} (bloqueado pelo sistema).")

    if not ok:
        raise SystemExit("[ERRO] Etapa 3b (Classificador) falhou. Pipeline interrompido.")

    if not ARQ_EXCL.exists():
        raise SystemExit(
            f"[ERRO] Classificador não gerou {ARQ_EXCL.name} em {DIR_TICKERS}.\n"
            "Verifique o PASTA_SAIDA dentro do notebook original e os logs acima."
        )
    n_excl = len(open(ARQ_EXCL, encoding="utf-8").readlines()) - 1
    print(f"  [OK] {ARQ_EXCL.name} gerado: {n_excl} tickers a excluir")

    # ─────────────────────────────────────────────────────────────────────────
    # PASSO 3 — 03c: aplica exclusões → grava matriz final
    # ─────────────────────────────────────────────────────────────────────────
    print("\n[3/3] 03c — Aplicação das Exclusões e Gravação da Matriz Final")
    ok = run_notebook(NB03C, "03_01c_Pos_Integridade")
    if not ok:
        raise SystemExit("[ERRO] Etapa 3c falhou. Pipeline interrompido.")

    if not ARQ_MATRIZ.exists():
        raise SystemExit(
            f"[ERRO] 03c não gerou {ARQ_MATRIZ.name}. "
            "Verifique o stdout do notebook acima."
        )

    # ─────────────────────────────────────────────────────────────────────────
    # Conclusão
    # ─────────────────────────────────────────────────────────────────────────
    elapsed_total = time.perf_counter() - t_total

    save_cache({"combined_hash": cache_key, "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")})

    print()
    print(banner)
    print("  ETAPA 3 CONCLUÍDA COM SUCESSO")
    print(f"  Tempo total: {elapsed_total:.1f}s")
    print()
    print(f"  Artefatos gerados:")
    print(f"    - {ARQ_UNIVERSO.relative_to(PROJECT_ROOT)}")
    print(f"    - {ARQ_EXCL.relative_to(PROJECT_ROOT)}")
    print(f"    - {ARQ_MATRIZ.relative_to(PROJECT_ROOT)}")
    print(f"    - {(DIR_TICKERS / 'tickers_finais.csv').relative_to(PROJECT_ROOT)}")
    print(banner)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Orquestrador da Etapa 3: Filtro de Liquidez + Integridade (3 passagens)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Imprime o plano de execução sem rodar nenhum notebook.",
    )
    parser.add_argument(
        "--skip-cache",
        action="store_true",
        help="Ignora o cache e força a re-execução dos três notebooks.",
    )
    args = parser.parse_args()
    main(dry_run=args.dry_run, skip_cache=args.skip_cache)
