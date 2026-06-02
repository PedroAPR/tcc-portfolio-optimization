"""Carregamento de parâmetros metodológicos e resolução de caminhos do projeto.

Módulo de configuração: centraliza constantes, leitura do `config.json` e a
preparação dos diretórios de saída.
"""
from __future__ import annotations

import json
from pathlib import Path
import pandas as pd

# --- Constantes metodológicas ---
TRADING_DAYS = 252      # Convenção de dias úteis para anualização
CODIGO_CDI = 12         # Série SGS/BCB — CDI diário (% a.d.)
CODIGO_SELIC = 11       # Série SGS/BCB — SELIC diária over (% a.d.)

def carregar_parametros(caminho: str | Path | None = None) -> dict:
    """Lê o `config.json` centralizado na raiz de src/ e devolve os parâmetros."""
    if caminho is None or caminho == "config.json" or Path(caminho).name == "config.json":
        caminho = Path(__file__).resolve().parent.parent.parent / "config.json"
    else:
        caminho = Path(caminho)
        
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def formatar_periodo(config: dict) -> tuple[str, str]:
    """Devolve (data_inicial, data_final) no formato dd/mm/aaaa para exibição."""
    inicio = pd.to_datetime(config["DATA_INICIO"]).strftime("%d/%m/%Y")
    fim = pd.to_datetime(config["DATA_FIM"]).strftime("%d/%m/%Y")
    return inicio, fim

def preparar_diretorios_saida(base: str | Path | None = None) -> tuple[Path, Path]:
    """Cria (se necessário) e devolve os diretórios de saída de CDI e SELIC."""
    raiz = Path(base) if base is not None else Path(__file__).resolve().parent.parent.parent.parent
    dir_cdi = raiz / "data" / "CDI"
    dir_selic = raiz / "data" / "Selic"
    dir_cdi.mkdir(parents=True, exist_ok=True)
    dir_selic.mkdir(parents=True, exist_ok=True)
    return dir_cdi, dir_selic
