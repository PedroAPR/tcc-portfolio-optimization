"""Conversões de taxas e preços (puras, sem efeitos colaterais).

Reúne as transformações matemáticas aplicadas a preços e taxas, isolando a
conversão de retornos e a convenção de anualização do restante do pipeline.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .config_loader import TRADING_DAYS


def anualizar(taxa_diaria_pct, trading_days: int = TRADING_DAYS):
    """Anualiza uma taxa expressa em percentual ao dia (% a.d.).

    Aceita escalar ou `pandas.Series`/`numpy.ndarray`.
    Convenção: (1 + r_d)^252 - 1, com r_d em fração.
    """
    return ((1 + taxa_diaria_pct / 100) ** trading_days - 1) * 100


def para_fracao_diaria(taxa_diaria_pct):
    """Converte taxa em percentual ao dia para fração decimal (÷100)."""
    return taxa_diaria_pct / 100


def calcular_retornos_simples(precos: pd.DataFrame | pd.Series) -> pd.DataFrame | pd.Series:
    """Calcula os retornos discretos (simples) diários, removendo a primeira linha (NaN)."""
    return precos.pct_change().iloc[1:]


def calcular_retornos_log(precos: pd.DataFrame | pd.Series) -> pd.DataFrame | pd.Series:
    """Calcula os log-retornos contínuos diários, removendo a primeira linha (NaN)."""
    return np.log(precos).diff().iloc[1:]

