"""Persistência das séries tratadas em CSV.

Módulo de I/O: isola a gravação dos artefatos finais consumidos pelos modelos
de Black-Litterman e CAPM.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd


def exportar_serie(df: pd.DataFrame, caminho: str | Path) -> Path:
    """Grava um DataFrame em CSV (separador `;`, UTF-8) e devolve o caminho resolvido."""
    caminho = Path(caminho)
    df.to_csv(caminho, index=False, sep=";", encoding="utf-8")
    return caminho.resolve()


def exportar_taxas(cdi: pd.DataFrame, selic: pd.DataFrame,
                   dir_cdi: str | Path, dir_selic: str | Path,
                   nome_cdi: str = "cdi_diario_bcb_2010_atual.csv",
                   nome_selic: str = "selic_diario_bcb_2010_atual.csv") -> tuple[Path, Path]:
    """Exporta as séries de CDI e SELIC e registra os caminhos gerados."""
    p_cdi = exportar_serie(cdi, Path(dir_cdi) / nome_cdi)
    p_selic = exportar_serie(selic, Path(dir_selic) / nome_selic)
    print(f"[OK] CDI exportado para: {p_cdi}")
    print(f"[OK] SELIC exportado para: {p_selic}")
    return p_cdi, p_selic
