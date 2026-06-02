"""Sincronismo de índices temporais e alinhamento cronológico.

Módulo de Alinhamento: isola a lógica de interseção de calendários
e consolidação temporal do painel multi-ativos.
"""
from __future__ import annotations

import pandas as pd


def obter_calendario_comum(dfs_ou_series: list[pd.DataFrame | pd.Series]) -> pd.DatetimeIndex:
    """Retorna o índice cronológico ordenado da interseção de todas as séries."""
    if not dfs_ou_series:
        raise ValueError("A lista de DataFrames/Séries não pode estar vazia.")
    
    # Inicializa o calendário com o índice do primeiro elemento
    calendario = dfs_ou_series[0].index
    
    # Executa a interseção sucessiva com todos os outros elementos
    for item in dfs_ou_series[1:]:
        calendario = calendario.intersection(item.index)
        
    return pd.DatetimeIndex(calendario).sort_values()


def alinhar_painel(
    precos_acoes: pd.DataFrame,
    ibov_close: pd.Series,
    cdi_diario: pd.Series,
    selic_diario: pd.Series,
    calendario: pd.DatetimeIndex
) -> pd.DataFrame:
    """Reindexa todos os componentes para o calendário comum e os concatena.

    Garante que não restem valores nulos (NaN) no painel consolidado.
    """
    # Reindexa as ações e adiciona o prefixo ACAO_
    acoes_alinhadas = precos_acoes.reindex(calendario)
    acoes_alinhadas.columns = [f"ACAO_{c}" if not c.startswith("ACAO_") else c for c in acoes_alinhadas.columns]
    
    # Reindexa os benchmarks
    ibov_alinhado = ibov_close.reindex(calendario).rename("IBOV_close")
    cdi_alinhado = cdi_diario.reindex(calendario).rename("CDI_diario")
    selic_alinhado = selic_diario.reindex(calendario).rename("SELIC_diario")
    
    # Concatena todos os ativos
    painel = pd.concat([ibov_alinhado, cdi_alinhado, selic_alinhado, acoes_alinhadas], axis=1)
    painel.index.name = "data"
    
    # Valida presença de NaNs
    n_nan = int(painel.isna().sum().sum())
    if n_nan > 0:
        raise ValueError(f"Ocorreu a introdução de {n_nan} NaNs no painel durante o alinhamento.")
        
    return painel
