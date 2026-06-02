import pandas as pd
from pathlib import Path

def gerar_auditoria_exclusoes(
    df_sanitizado: pd.DataFrame,
    reprovados_presenca: pd.Series,
    ativos_ipo_tardio: pd.Series,
    ativos_iliquidos: pd.Series,
    proporcao_presenca: pd.Series,
    adtv: pd.Series,
    limiar_presenca: float,
    percentil_liquidez: float,
    diretorio_destino: Path,
    aprovados_presenca: list,
    ativos_integros: list,
    ativos_liquidos: list
) -> None:
    """Gera o log de exclusões consolidado em formato CSV e imprime o funil metodológico de ativos."""
    log_exclusoes = []
    
    # 1. Filtro de Presença
    for ticker, p in reprovados_presenca.items():
        log_exclusoes.append({
            "ticker": ticker, "presenca_pct": round(p*100, 2), "adtv_2010": None,
            "motivo": f"Presença em pregão < {limiar_presenca:.0%}"
        })
        
    # 2. Filtro de IPO Tardio (Lookahead Bias)
    for ticker, d in ativos_ipo_tardio.items():
        log_exclusoes.append({
            "ticker": ticker, "presenca_pct": round(proporcao_presenca[ticker]*100, 2), "adtv_2010": None,
            "motivo": "IPO posterior à data inicial da janela (lookahead bias)"
        })
        
    # 3. Filtro de ADTV (Liquidez Financeira ex-ante)
    for ticker, v in ativos_iliquidos.items():
        log_exclusoes.append({
            "ticker": ticker, "presenca_pct": round(proporcao_presenca[ticker]*100, 2), "adtv_2010": round(float(v), 2),
            "motivo": f"ADTV 201 diário inferior ao percentil p{percentil_liquidez*100:.0f}"
        })
        
    df_log = pd.DataFrame(log_exclusoes)
    df_log.to_csv(diretorio_destino / "tickers_excluidos.csv", index=False)
    adtv.sort_values(ascending=False).to_csv(diretorio_destino / "adtv_formacao_2010.csv")
    
    print(f"[OK] Matriz final salva: {df_sanitizado.shape[1]} ativos × {df_sanitizado.shape[0]} pregões")
    print(f"[OK] Log de exclusões salvo contendo {len(log_exclusoes)} registros.")
    print("\n" + "="*50)
    print("FUNIL METODOLÓGICO DE ATIVOS")
    print("="*50)
    print(f"  Universo Bruto Ingerido:          {len(proporcao_presenca)}")
    print(f"  Após Filtro de Presença (IV):     {len(aprovados_presenca)}")
    print(f"  Após Filtro de Integridade (V):   {len(ativos_integros)}")
    print(f"  Após Filtro de ADTV (VI):         {len(ativos_liquidos)}  <- Universo Investível Final")
    print("==================================================")
