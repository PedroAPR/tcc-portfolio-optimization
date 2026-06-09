import pandas as pd
import os
import pyarrow

def filtrar_ativos():
    """
    Script que le o arquivo Parquet master, extrai a lista de ativos alvo
    do diagnostico econometrico, filtra as colunas correspondentes e
    salva a base de dados filtrada nos formatos Parquet e CSV.
    """
    # Configuracao de diretorios e nomes dos arquivos
    diretorio_dados = r"C:\VSCodeWorkspace\TCC_Final\data"
    arquivo_parquet_original = 'lista_economatica_dados_Jan_2010_Dezembro_2025.parquet'
    arquivo_ativos_alvo = 'diagnostico_econometrico_130_ativos.csv'
    
    arquivo_saida_parquet = 'lista_economatica_dados_filtrados.parquet'
    arquivo_saida_csv = 'lista_economatica_dados_filtrados.csv'
    
    print("--------------------------------------------------")
    print("Passo 1: Lendo a lista de ativos alvo...")
    caminho_diagnostico = os.path.join(diretorio_dados, arquivo_ativos_alvo)
    
    try:
        df_diagnostico = pd.read_csv(caminho_diagnostico)
        # Limpando os underscores espurios (como WEGE3_ -> WEGE3)
        tickers_alvo = df_diagnostico['Ativo'].str.rstrip('_').tolist()
        print(f"[OK] Total de ativos identificados no diagnostico: {len(tickers_alvo)}")
        
        print("\n--------------------------------------------------")
        print("Passo 2: Lendo arquivo Parquet master original...")
        caminho_parquet = os.path.join(diretorio_dados, arquivo_parquet_original)
        df_original = pd.read_parquet(caminho_parquet, engine='pyarrow')
        print(f"[OK] Leitura concluida! Shape original: {df_original.shape}")
        
        print("\n--------------------------------------------------")
        print("Passo 3: Filtrando colunas correspondentes aos ativos alvo...")
        colunas_disponiveis = df_original.columns.tolist()
        ativos_encontrados = [t for t in tickers_alvo if t in colunas_disponiveis]
        ativos_faltantes = [t for t in tickers_alvo if t not in colunas_disponiveis]
        
        print(f"Ativos encontrados na base de dados: {len(ativos_encontrados)} / {len(tickers_alvo)}")
        if ativos_faltantes:
            print(f"[AVISO] Atencao: {len(ativos_faltantes)} ativos nao foram encontrados na base Parquet: {ativos_faltantes}")
        else:
            print("[OK] Excelente! Todos os 130 ativos estao presentes no arquivo Parquet original.")
            
        # Garante que a coluna 'Data' seja a primeira
        colunas_filtradas = ['Data'] + ativos_encontrados
        df_filtrado = df_original[colunas_filtradas]
        print(f"[OK] Nova base filtrada criada com shape: {df_filtrado.shape}")
        
        print("\n--------------------------------------------------")
        print("Passo 4: Salvando os arquivos filtrados...")
        caminho_saida_parquet = os.path.join(diretorio_dados, arquivo_saida_parquet)
        caminho_saida_csv = os.path.join(diretorio_dados, arquivo_saida_csv)
        
        # Salvando Parquet
        print(f"Salvando Parquet em: {caminho_saida_parquet}")
        df_filtrado.to_parquet(caminho_saida_parquet, index=False, engine='pyarrow')
        print("[OK] Parquet salvo com sucesso!")
        
        # Salvando CSV
        print(f"Salvando CSV em: {caminho_saida_csv}")
        df_filtrado.to_csv(caminho_saida_csv, index=False, sep=';', decimal=',')
        print("[OK] CSV salvo com sucesso!")
        
        print("\n--------------------------------------------------")
        print("Passo 5: Validacao Rapida dos Resultados")
        print(f"Shape final: {df_filtrado.shape}")
        print(f"Numero de colunas: {len(df_filtrado.columns)}")
        print(f"Ativos listados (excluindo Data): {len(df_filtrado.columns) - 1}")
        print(f"Data Inicial: {df_filtrado['Data'].iloc[0]}")
        print(f"Data Final: {df_filtrado['Data'].iloc[-1]}")
        print("\nVisualizando as primeiras 5 linhas:")
        print(df_filtrado.head())
        print("--------------------------------------------------")
        
    except FileNotFoundError as e:
        print(f"Erro de arquivo nao encontrado: {e}")
    except Exception as e:
        print(f"Erro inesperado durante a execucao: {e}")

if __name__ == "__main__":
    filtrar_ativos()
