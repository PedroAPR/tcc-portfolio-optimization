import time
import requests
import pandas as pd
from datetime import datetime
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BCB_SGS_URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{cod}/dados"

def _sessao_com_retry() -> requests.Session:
    s = requests.Session()
    retry = Retry(
        total=5, backoff_factor=1.5,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("GET",),
    )
    s.mount("https://", HTTPAdapter(max_retries=retry))
    s.headers.update({"User-Agent": "TCC-Pedro-Reis/1.0 (academic research)"})
    return s

def _particionar_periodo(inicio: datetime, fim: datetime, max_anos: int = 9):
    """Quebra o período (inicio, fim) em blocos de até max_anos."""
    blocos, cur = [], inicio
    while cur <= fim:
        try:
            # Substituição robusta considerando anos bissextos
            prox = cur.replace(year=cur.year + max_anos)
        except ValueError:
            # Caso caia em 29 de fevereiro em ano não-bissexto
            prox = cur.replace(year=cur.year + max_anos, day=28)
        bloco_fim = min(prox, fim)
        blocos.append((cur.strftime("%d/%m/%Y"), bloco_fim.strftime("%d/%m/%Y")))
        if bloco_fim == fim:
            break
        cur = datetime.fromordinal(bloco_fim.toordinal() + 1)
    return blocos

def baixar_serie_sgs(codigo: int, inicio_str: str, fim_str: str, timeout: int = 60) -> pd.DataFrame:
    """Baixa uma série SGS do Bacen particionando em blocos para respeitar o limite de paginação."""
    inicio = pd.to_datetime(inicio_str)
    fim = pd.to_datetime(fim_str)
    
    sessao = _sessao_com_retry()
    partes = []
    
    for ini, fim_b in _particionar_periodo(inicio, fim, max_anos=9):
        url = BCB_SGS_URL.format(cod=codigo)
        params = {"formato": "json", "dataInicial": ini, "dataFinal": fim_b}
        print(f"  • Série {codigo}: {ini} → {fim_b} ... ", end="", flush=True)
        r = sessao.get(url, params=params, timeout=timeout)
        r.raise_for_status()
        dados = r.json()
        df = pd.DataFrame(dados)
        df["data"]  = pd.to_datetime(df["data"], dayfirst=True)
        df["valor"] = pd.to_numeric(df["valor"].astype(str).str.replace(",", "."))
        print(f"{len(df):>5} observações")
        partes.append(df)
        time.sleep(0.4)
        
    serie = (pd.concat(partes, ignore_index=True)
               .drop_duplicates(subset="data")
               .sort_values("data")
               .reset_index(drop=True))
    return serie

def fallback_offline_bcb():
    """Gera dados sintéticos baseados no histórico real do COPOM como contingência offline."""
    print("\n[OFFLINE] API indisponível. Gerando sintético baseado em calendário Copom real")
    print("apenas para validação do pipeline. Re-execute em ambiente com internet para baixar")
    print("a série oficial completa.\n")
    copom_hist = [
        ("2010-01-04", 8.75), ("2010-04-29", 9.50),  ("2010-06-10", 10.25),
        ("2010-07-22", 10.75),("2011-01-20", 11.25), ("2011-03-03", 11.75),
        ("2011-04-21", 12.00),("2011-06-09", 12.25), ("2011-07-21", 12.50),
        ("2011-09-01", 12.00),("2011-10-20", 11.50), ("2011-12-01", 11.00),
        ("2012-01-19", 10.50),("2012-03-08", 9.75),  ("2012-04-19", 9.00),
        ("2012-05-31", 8.50), ("2012-07-12", 8.00),  ("2012-08-30", 7.50),
        ("2012-10-11", 7.25), ("2013-04-18", 7.50),  ("2013-05-30", 8.00),
        ("2013-07-11", 8.50), ("2013-08-29", 9.00),  ("2013-10-10", 9.50),
        ("2013-11-28", 10.00),("2014-01-16", 10.50), ("2014-02-27", 10.75),
        ("2014-04-03", 11.00),("2014-10-30", 11.25), ("2014-12-04", 11.75),
        ("2015-01-22", 12.25),("2015-03-05", 12.75), ("2015-04-30", 13.25),
        ("2015-06-04", 13.75),("2015-07-30", 14.25), ("2016-10-20", 14.00),
        ("2016-12-01", 13.75),("2017-01-12", 13.00), ("2017-02-23", 12.25),
        ("2017-04-13", 11.25),("2017-06-01", 10.25), ("2017-07-27", 9.25),
        ("2017-09-07", 8.25), ("2017-10-26", 7.50),  ("2017-12-07", 7.00),
        ("2018-02-08", 6.75), ("2018-03-22", 6.50),  ("2019-08-01", 6.00),
        ("2019-09-19", 5.50), ("2019-10-31", 5.00),  ("2019-12-12", 4.50),
        ("2020-02-06", 4.25), ("2020-03-19", 3.75),  ("2020-05-07", 3.00),
        ("2020-06-18", 2.25), ("2020-08-06", 2.00),  ("2021-03-18", 2.75),
        ("2021-05-06", 3.50), ("2021-06-17", 4.25),  ("2021-08-05", 5.25),
        ("2021-09-23", 6.25), ("2021-10-28", 7.75),  ("2021-12-09", 9.25),
        ("2022-02-03", 10.75),("2022-03-17", 11.75), ("2022-05-05", 12.75),
        ("2022-06-16", 13.25),("2022-08-04", 13.75), ("2023-08-03", 13.25),
        ("2023-09-21", 12.75),("2023-11-02", 12.25), ("2023-12-14", 11.75),
        ("2024-01-31", 11.25),("2024-03-21", 10.75), ("2024-05-09", 10.50),
        ("2024-09-19", 10.75),("2024-11-07", 11.25), ("2024-12-12", 12.25),
        ("2025-01-30", 13.25),("2025-03-20", 14.25), ("2025-05-08", 14.75),
    ]
    fim = pd.Timestamp(datetime.today().strftime("%Y-%m-%d"))
    cal = pd.bdate_range("2010-01-04", fim)
    cal = cal[~((cal.month == 12) & (cal.day == 25))] 
    cal = cal[~((cal.month == 1)  & (cal.day == 1))]  
    df_cal = pd.DataFrame({"data": cal})
    eventos = pd.DataFrame(copom_hist, columns=["data", "meta_anual"])
    eventos["data"] = pd.to_datetime(eventos["data"])
    df_cal = pd.merge_asof(df_cal.sort_values("data"), eventos.sort_values("data"), on="data")
    df_cal["meta_anual"] = df_cal["meta_anual"].ffill().bfill()
    df_cal["valor"] = ((1 + df_cal["meta_anual"]/100)**(1/252) - 1) * 100
    df_cal = df_cal[["data", "valor"]].copy()
    df_cdi = df_cal.copy()
    df_selic = df_cal.copy()
    df_cdi["valor"] = df_cdi["valor"] * 0.99996 
    return df_cdi, df_selic
