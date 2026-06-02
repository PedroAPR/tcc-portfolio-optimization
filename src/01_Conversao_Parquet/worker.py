import openpyxl
import pandas as pd
from pathlib import Path

def extrair_ticker_do_nome_da_planilha(caminho_arquivo: Path) -> str:
    """
    Abre uma planilha Excel em modo 'read_only' para extrair o ticker a partir do nome da planilha ativa (aba).

    Args:
        caminho_arquivo (Path): Caminho para a planilha .xlsx.

    Returns:
        str: Ticker do ativo limpo (ex: 'PETR4').
    """
    # Abre o arquivo com openpyxl de forma eficiente para ler o nome da aba
    livro = openpyxl.load_workbook(caminho_arquivo, read_only=True)
    planilha = livro.active

    nome_aba = planilha.title
    livro.close()

    if not nome_aba or not isinstance(nome_aba, str):
        raise ValueError(f"O nome da planilha ativa está vazio ou não contém texto no arquivo: {caminho_arquivo.name}")

    # Limpeza: pega o primeiro token (ex: 'PETR4' de 'PETR4 PN' ou 'VALE3' de 'VALE3 ON')
    ticker = nome_aba.split()[0].strip().upper()

    # Remove caracteres que não sejam alfanuméricos
    ticker = "".join(char for char in ticker if char.isalnum())

    return ticker

def processar_e_salvar_dados(caminho_arquivo: Path, pasta_destino: Path) -> str:
    """
    Lê os dados da planilha Economatica a partir da linha 4 (cabeçalho),
    limpa e salva em Parquet e CSV individuais na pasta_destino.

    Args:
        caminho_arquivo (Path): Caminho do arquivo Excel de origem.
        pasta_destino (Path): Pasta de destino para os arquivos Parquet/CSV.

    Returns:
        str: O Ticker extraído do ativo.
    """
    ticker = extrair_ticker_do_nome_da_planilha(caminho_arquivo)

    # Leitura do Excel a partir da linha 4 (0-indexed index 3)
    # O pandas pula as 3 primeiras linhas ('skiprows=3') e lê o cabeçalho completo.
    # Converte '-' em NaN de forma explícita
    df = pd.read_excel(
        caminho_arquivo,
        skiprows=3,
        header=0,
        na_values=['-'],
        keep_default_na=True
    )

    # Tratamento e validação de nomes das colunas
    colunas_esperadas = ['Data', 'Q Negs', 'Q Títs', 'Volume$', 'Fechamento', 'Abertura', 'Mínimo', 'Máximo', 'Médio']

    # Ajusta espaçamentos nas colunas do Excel lido
    df.columns = [c.strip() for c in df.columns]

    # Verifica se as colunas essenciais estão presentes
    for col in colunas_esperadas:
        if col not in df.columns:
            raise KeyError(f"Coluna esperada '{col}' não foi encontrada no arquivo: {caminho_arquivo.name}")

    # Seleciona apenas as colunas esperadas
    df = df[colunas_esperadas].copy()

    # Coerção explícita de tipos de dados
    df['Data'] = pd.to_datetime(df['Data'], errors='coerce')

    # Remove registros com Data nula (linhas vazias no Excel)
    df = df.dropna(subset=['Data'])

    for col in colunas_esperadas[1:]:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Remove registros onde todas as colunas de dados (exceto a Data) estão nulas
    df = df.dropna(subset=colunas_esperadas[1:], how='all')

    # ORDENAÇÃO TEMPORAL EXPLÍCITA E RÍGIDA
    # Passo fundamental para evitar look-ahead bias em cálculos sequenciais ou filtros
    df = df.sort_values(by="Data").reset_index(drop=True)

    # Persistência em múltiplos formatos
    pasta_ticker = pasta_destino / ticker
    pasta_ticker.mkdir(parents=True, exist_ok=True)
    caminho_parquet = pasta_ticker / f"{ticker}.parquet"
    caminho_csv = pasta_ticker / f"{ticker}.csv"

    df.to_parquet(caminho_parquet, index=False)
    df.to_csv(caminho_csv, index=False, sep=";", encoding="utf-8")

    return ticker

def processar_wrapper(args):
    """Wrapper executado por processo-filho: isola falhas individuais por arquivo.
    Como o ProcessPoolExecutor map envia argumentos compactos, empacotamos em tupla.
    """
    arq, pasta_tratados = args
    try:
        ticker = processar_e_salvar_dados(arq, pasta_tratados)
        return True, ticker, None
    except Exception as e:
        return False, arq.name, str(e)
