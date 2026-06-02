"""Orquestração da ingestão das taxas livres de risco (CDI e SELIC over).

Módulo de orquestração/I-O: combina a extração via API SGS com o fallback
offline, padroniza nomes de colunas e acrescenta a fração diária decimal.
Emite log de progresso (aceitável em camada de I/O).
"""
from __future__ import annotations

import pandas as pd

from .config_loader import CODIGO_CDI, CODIGO_SELIC
from .conversoes import para_fracao_diaria
from .sgs_api import baixar_serie_sgs, fallback_offline_bcb


def _padronizar(df: pd.DataFrame, col_pct: str, col_frac: str) -> pd.DataFrame:
    """Renomeia a coluna `valor` e acrescenta a fração diária decimal."""
    df = df.rename(columns={"valor": col_pct})
    df[col_frac] = para_fracao_diaria(df[col_pct])
    return df


def carregar_taxas(data_inicio: str, data_fim: str) -> tuple[pd.DataFrame, pd.DataFrame, bool]:
    """Baixa CDI (série 12) e SELIC over (série 11), com contingência offline.

    Devolve `(cdi, selic, modo_offline)`. Em caso de falha na API, recorre ao
    gerador sintético baseado no calendário Copom e sinaliza `modo_offline=True`.
    As colunas resultantes são `data`, `<serie>_diario_pct` e `<serie>_diario`.
    """
    try:
        print(">>> Baixando CDI (série 12)...")
        cdi = baixar_serie_sgs(CODIGO_CDI, data_inicio, data_fim)
        print(f"    Total: {len(cdi):,} observações\n")

        print(">>> Baixando SELIC over (série 11)...")
        selic = baixar_serie_sgs(CODIGO_SELIC, data_inicio, data_fim)
        print(f"    Total: {len(selic):,} observações")
        modo_offline = False
    except Exception as e:
        print(f"\nERRO no download: {type(e).__name__}: {e}")
        cdi, selic = fallback_offline_bcb()
        modo_offline = True

    cdi = _padronizar(cdi, "cdi_diario_pct", "cdi_diario")
    selic = _padronizar(selic, "selic_diario_pct", "selic_diario")

    print(f"\nCDI:   {cdi['data'].min().date()} → {cdi['data'].max().date()}  ({len(cdi):,} obs.)")
    print(f"SELIC: {selic['data'].min().date()} → {selic['data'].max().date()}  ({len(selic):,} obs.)")
    return cdi, selic, modo_offline
