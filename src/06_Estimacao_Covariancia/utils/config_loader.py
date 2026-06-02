"""Carregamento de parâmetros metodológicos e resolução de caminhos do projeto.
"""
from __future__ import annotations

import json
from pathlib import Path

# Constante de dias de negociação padrão
TRADING_DAYS = 252

def carregar_parametros(caminho: str | Path | None = None) -> dict:
    """Lê o `config.json` centralizado na raiz de src/ e devolve os parâmetros."""
    if caminho is None or caminho == "config.json" or Path(caminho).name == "config.json":
        # Resolve config.json na pasta src/ (três níveis acima deste utilitário)
        caminho = Path(__file__).resolve().parent.parent.parent / "config.json"
    else:
        caminho = Path(caminho)
        
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)
