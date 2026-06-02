"""Diagnósticos de integridade das séries de taxas (funções puras).

Cada função recebe DataFrames/Series e devolve estruturas de dados; a
apresentação (impressão/formatação) fica a cargo do notebook.
"""
from __future__ import annotations

import pandas as pd


def pregoes_por_ano(df: pd.DataFrame, col_data: str = "data") -> pd.Series:
    """Mapeia a quantidade de pregões válidos agrupados por ano."""
    return df.groupby(df[col_data].dt.year).size()


def diagnostico_valores(df: pd.DataFrame, col: str, nome: str) -> dict:
    """Executa sanity check básico de integridade numérica em valores diários."""
    s = df[col]
    return {
        "Série": nome,
        "NaN": int(s.isna().sum()),
        "Zeros": int((s == 0).sum()),
        "Negativos": int((s < 0).sum()),
        "Min (%)": float(s.min()),
        "Max (%)": float(s.max()),
        "Média (%)": float(s.mean()),
        "Mediana (%)": float(s.median()),
    }


def listar_transicoes(df: pd.DataFrame, col_valor: str, anos: tuple = (2022, 2023)) -> pd.DataFrame:
    """Identifica as transições de patamar de taxa (degraus do Copom)."""
    d = df.copy()
    d["mudou"] = d[col_valor].diff().fillna(0) != 0
    transicoes = d.loc[d["mudou"] & d["data"].dt.year.isin(anos), ["data", col_valor]].copy()
    transicoes["valor_anterior"] = d[col_valor].shift().loc[transicoes.index]
    transicoes["Δ (bps a.d.)"] = (transicoes[col_valor] - transicoes["valor_anterior"]) * 10000
    return transicoes.reset_index(drop=True)


def construir_comparativo_spread(cdi: pd.DataFrame, selic: pd.DataFrame) -> pd.DataFrame:
    """Funde CDI e SELIC pelos pregões em comum e calcula o spread em bps a.d.

    Devolve um DataFrame com `data`, `cdi_diario_pct`, `selic_diario_pct` e
    `spread_bps` = (cdi − selic) × 10.000.
    """
    comp = cdi[["data", "cdi_diario_pct"]].merge(
        selic[["data", "selic_diario_pct"]], on="data", how="inner"
    )
    comp["spread_bps"] = (comp["cdi_diario_pct"] - comp["selic_diario_pct"]) * 10000
    return comp
