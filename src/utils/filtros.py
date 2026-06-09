import logging
import pandas as pd
import numpy as np

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] - %(message)s")

def filtrar_presenca(df: pd.DataFrame, limiar: float = 0.95) -> tuple[pd.Series, list[str], pd.Series]:
    """
    Mede a assiduidade e filtra ativos de acordo com o limiar mínimo de pregões com negócio.
    
    Args:
        df: DataFrame contendo o painel temporal de cotações.
        limiar: Percentual mínimo de presença exigido (ex: 0.95 para 95%).
        
    Returns:
        proporcao: Série com o percentual de presença de cada ativo.
        aprovados: Lista de tickers que passaram no filtro.
        reprovados: Série de tickers reprovados e suas respectivas taxas de presença.
    """
    proporcao = df.notna().sum() / len(df)
    aprovados = proporcao[proporcao >= limiar].index.tolist()
    reprovados = proporcao[proporcao < limiar]
    return proporcao, aprovados, reprovados

def filtrar_integridade_ipo(df: pd.DataFrame) -> tuple[pd.Timestamp, list[str], pd.Series]:
    """
    Verifica se a data do primeiro pregão com negócio do ativo é igual ou anterior ao início da janela.
    
    Args:
        df: DataFrame de preços de fechamento.
        
    Returns:
        data_inicio_efetiva: Data de início do primeiro pregão do painel.
        integros: Lista de tickers que contam com histórico desde o t0.
        ipo_tardio: Série contendo a primeira data observada para os ativos excluídos.
    """
    data_inicio_efetiva = df.index.min()
    # Otimização vetorizada usando first_valid_index
    primeiro_pregao_ativo = df.apply(lambda s: s.first_valid_index())
    
    integros = primeiro_pregao_ativo[primeiro_pregao_ativo <= data_inicio_efetiva].index.tolist()
    ipo_tardio = primeiro_pregao_ativo[primeiro_pregao_ativo > data_inicio_efetiva]
    return data_inicio_efetiva, integros, ipo_tardio

def filtrar_adtv_formacao(
    df_volumes_all: pd.DataFrame, 
    ativos_filtrados: list[str], 
    ano_formacao: int, 
    percentil_corte: float
) -> tuple[pd.Series, float, list[str], pd.Series]:
    """
    Mede a liquidez longitudinal média ex-ante do ano de formação e expurga o decil inferior.
    
    Args:
        df_volumes_all: DataFrame com as séries brutas de volumes.
        ativos_filtrados: Lista de ativos pré-selecionados na etapa anterior.
        ano_formacao: Ano de referência da liquidez.
        percentil_corte: Limiar de exclusão transversal (ex: 0.10 para quantil de 10%).
        
    Returns:
        adtv_serie: Série com o volume diário médio do ano de formação por ticker.
        limiar: Valor do corte obtido a partir do quantil.
        liquidos: Lista de ativos aprovados.
        iliquidos: Série de ativos reprovados e seus respectivos volumes médios.
    """
    cal_formacao = df_volumes_all.loc[str(ano_formacao)].index
    # Assume volume nulo para dias sem negociação ativa
    vol_formacao = df_volumes_all.reindex(index=cal_formacao, columns=ativos_filtrados).fillna(0.0)
    adtv_serie = vol_formacao.mean().rename(f"ADTV_{ano_formacao}")
    
    limiar = adtv_serie.quantile(percentil_corte)
    liquidos = adtv_serie[adtv_serie >= limiar].index.tolist()
    iliquidos = adtv_serie[adtv_serie < limiar].sort_values()
    return adtv_serie, limiar, liquidos, iliquidos

def executar_testes_integridade(df: pd.DataFrame, adtv_serie: pd.Series, limiar: float) -> None:
    """
    Executa rotinas formais de asserção lógica sobre o dataset sanitizado.
    
    Args:
        df: DataFrame final de preços sanitizados.
        adtv_serie: Série original do ADTV.
        limiar: Limiar de corte do ADTV.
    """
    assert df.isna().sum().sum() == 0, "Falha T1: NaNs remanescentes"
    assert not df.index.has_duplicates, "Falha T2: Índice temporal com duplicatas"
    assert df.index.is_monotonic_increasing, "Falha T3: Índice não-cronológico crescente"
    assert (df > 0).all().all(), "Falha T4: Preços menores ou iguais a zero"
    assert ((df.notna().sum() / len(df)) == 1.0).all(), "Falha T5: Ativos com presença menor que 100%"
    assert (adtv_serie[df.columns] >= limiar).all(), "Falha T6: Ativo com liquidez abaixo da especificada"
    print("[OK] Matriz sanitizada aprovada em todos os testes (T1-T6).")
