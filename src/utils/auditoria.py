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


def diagnosticar_retornos_impossiveis(
    ret_simples: pd.DataFrame,
    painel_precos: pd.DataFrame,
    limiar: float = 1.0
) -> pd.DataFrame:
    """Verifica se há retornos simples com valor absoluto superior ao limiar econômico impossível.

    Retorna um DataFrame contendo estatísticas dos ativos sinalizados.
    """
    impossiveis = (ret_simples.abs() > limiar).sum()
    flag = impossiveis[impossiveis > 0].sort_values(ascending=False)
    
    if len(flag) == 0:
        return pd.DataFrame()
        
    colunas_painel = [col for col in flag.index if col in painel_precos.columns]
    preco_mediano = painel_precos[colunas_painel].median()
    
    maior_ret = ret_simples[flag.index].abs().max() * 100
    
    audit = pd.DataFrame({
        "dias_|R|>100%": flag,
        "maior_|R|_%": maior_ret.round(0),
        "preco_mediano_R$": preco_mediano
    })
    return audit


def gerar_log_winsorizacao(
    relatorio_itens: list[dict],
    caminho_saida: Path
) -> pd.DataFrame:
    """Grava o log de winsorizações comparativas de ativos em CSV."""
    df_rel = pd.DataFrame(relatorio_itens).set_index("ativo")
    df_rel["reducao"] = df_rel["n_winsor_com_zeros"] - df_rel["n_winsor_v2"]
    df_rel.to_csv(caminho_saida, float_format="%.8f")
    return df_rel


def exportar_verificacao_corporativa(
    caminho_saida: Path
) -> pd.DataFrame:
    """Cria e persiste o log descritivo com a checagem manual de eventos corporativos na B3."""
    verificacao = pd.DataFrame([
        {"ticker": "FICT3", "empresa": "Fictor Alimentos (ex-ATOM3)",
         "evento": "IPO reverso (troca de controle/ticker) + RJ da holding (2026); penny stock < R$1",
         "natureza_extremo": "Distress real + mudanca de base acionaria", "decisao": "Manter (ativo real)"},
        {"ticker": "GOLL54", "empresa": "Gol Linhas Aereas",
         "evento": "Reestruturacao/distress (2024-25); salto +1847% = provavel grupamento nao-ajustado",
         "natureza_extremo": "Artefato de evento (denominador ~centavo)",
         "decisao": "Manter; ideal ajustar preco a montante pelo grupamento"},
        {"ticker": "LUPA3", "empresa": "Lupatech",
         "evento": "RJ 2015-2023 c/ conversao de ~85% da divida em acoes (forte diluicao); nova RE 2026",
         "natureza_extremo": "Diluicao/distress real", "decisao": "Manter"},
        {"ticker": "TELB4", "empresa": "Telebras (PN)",
         "evento": "Multiplos splits/grupamentos no historico; liquidez muito baixa",
         "natureza_extremo": "Artefato de split/grupamento + iliquidez", "decisao": "Manter; conferir datas"},
        {"ticker": "AMER3", "empresa": "Americanas",
         "evento": "Fraude contabil 11/01/2023 -> RJ 19/01/2023; grupamento 100:1 em ago/2024",
         "natureza_extremo": "Crash real (fraude) + nivel ajustado inflado pelo inplit 100:1",
         "decisao": "Manter (anti-sobrevivencia)"},
    ]).set_index("ticker")
    
    verificacao.to_csv(caminho_saida)
    return verificacao
