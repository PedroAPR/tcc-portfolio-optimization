"""Winsorização robusta baseada em escala robusta (MAD).

Módulo de Winsorização: isola os algoritmos matemáticos de cercas
de dispersão pelo escore Z modificado de Iglewicz e Hoaglin (1993) e clip.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def cercas_mad(
    serie: pd.Series | np.ndarray,
    k: float = 3.5,
    c: float = 0.6745,
    nao_nulos: bool = True
) -> tuple[float | None, float | None]:
    """Calcula os limites de corte robustos baseados no Desvio Absoluto Mediano (MAD).

    Se nao_nulos for True, a Mediana e o MAD são estimados exclusivamente sobre
    as observações não-nulas da série, mitigando a contração artificial de escala
    gerada por dias sem negociação (preenchidos via forward-fill).
    """
    # Garante valores float e array 1D
    x = np.asarray(serie, dtype=float)
    
    # Filtra observações não-nulas se configurado
    base = x[x != 0] if nao_nulos else x
    
    if base.size == 0:
        return None, None
        
    med = np.median(base)
    mad = np.median(np.abs(base - med))
    
    if mad == 0:
        return None, None
        
    # Z-score modificado: cerca = med +- k * mad / c
    corte = k * mad / c
    return float(med - corte), float(med + corte)


def winsorizar_painel_log(
    df_log_ret: pd.DataFrame,
    k: float = 3.5,
    c: float = 0.6745,
    nao_nulos: bool = True
) -> tuple[pd.DataFrame, list[dict]]:
    """Aplica winsorização robusta em todas as colunas de um DataFrame de log-retornos.

    Retorna uma tupla contendo:
    1. DataFrame contendo os retornos saneados (truncados).
    2. Lista de dicionários contendo o relatório de winsorização por coluna (ativo).
    """
    df_saneado = df_log_ret.copy()
    relatorio = []
    
    for col in df_log_ret.columns:
        lo, hi = cercas_mad(df_log_ret[col], k=k, c=c, nao_nulos=nao_nulos)
        lo0, hi0 = cercas_mad(df_log_ret[col], k=k, c=c, nao_nulos=False)
        
        n_zeros = 0 if lo0 is None else int(((df_log_ret[col] < lo0) | (df_log_ret[col] > hi0)).sum())
        
        if lo is None or hi is None:
            relatorio.append({
                "ativo": col,
                "n_winsor_v2": 0,
                "n_winsor_com_zeros": n_zeros,
                "mad_zero": True
            })
            continue
            
        n_v2 = int(((df_log_ret[col] < lo) | (df_log_ret[col] > hi)).sum())
        df_saneado[col] = df_log_ret[col].clip(lower=lo, upper=hi)
        
        relatorio.append({
            "ativo": col,
            "n_winsor_v2": n_v2,
            "n_winsor_com_zeros": n_zeros,
            "mad_zero": False
        })
        
    return df_saneado, relatorio
