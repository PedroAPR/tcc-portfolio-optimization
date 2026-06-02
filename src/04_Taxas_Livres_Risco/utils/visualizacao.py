"""Visualização e configuração de exibição.

Concentra a parametrização de aparência (matplotlib/pandas) e a geração das
figuras de referência do notebook.
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd

from .conversoes import anualizar


def configurar_exibicao() -> None:
    """Aplica os padrões de exibição usados ao longo do notebook."""
    pd.set_option("display.float_format", lambda x: f"{x:,.6f}")
    plt.rcParams.update({"figure.dpi": 110, "figure.figsize": (11, 4), "axes.grid": True})


def plotar_taxas_anualizadas(cdi: pd.DataFrame, selic: pd.DataFrame):
    """Plota CDI e SELIC over anualizadas (convenção de 252 dias úteis).

    Devolve o objeto `Figure` para que o notebook controle a exibição.
    """
    fig, ax = plt.subplots(figsize=(12, 4.5))
    ax.plot(cdi["data"], anualizar(cdi["cdi_diario_pct"]),
            lw=0.9, label="CDI (anualizado)", color="#1F3864")
    ax.plot(selic["data"], anualizar(selic["selic_diario_pct"]),
            lw=0.9, label="SELIC over (anual.)", color="#C00000", ls="--", alpha=0.7)
    ax.set_title("CDI e SELIC over — Taxas anualizadas (Convenção 252 dias úteis)")
    ax.set_ylabel("% a.a.")
    ax.legend()
    fig.tight_layout()
    return fig
