import pandas as pd
from pathlib import Path

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
