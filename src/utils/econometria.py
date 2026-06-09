import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.stats.diagnostic import acorr_ljungbox

def fmt_p(p: float) -> str:
    """Formata representação do p-valor com significância clássica de estrelas."""
    if p < 0.001: return "< 0,001 ***"
    if p < 0.01:  return f"{p:.4f} ***"
    if p < 0.05:  return f"{p:.4f} **"
    if p < 0.10:  return f"{p:.4f} *"
    return f"{p:.4f}"

def descritiva(df: pd.DataFrame, col: str, nome: str) -> dict:
    """Afeire estatísticas descritivas diárias em nível e variação."""
    s = df[col]
    ds = s.diff().dropna()
    return {
        "Série": nome,
        "N":              int(s.count()),
        "Média (%)":      float(s.mean()),
        "Mediana (%)":    float(s.median()),
        "Std (%)":        float(s.std()),
        "Mín / Máx (%)":  f"{s.min():.4f} / {s.max():.4f}",
        "Assim. nível":   float(s.skew()),
        "Curt. nível":    float(s.kurt()),
        "Std variação":   float(ds.std()),
        "Assim. variação":float(ds.skew()),
        "Curt. variação": float(ds.kurt()),
    }

def teste_estacionariedade(serie: pd.Series, nome: str) -> list[dict]:
    """Afeire estacionariedade e perfil de integração temporal usando testes ADF e KPSS."""
    nivel = serie.dropna()
    delta = serie.diff().dropna()
    
    adf_n = adfuller(nivel, autolag="AIC")
    adf_d = adfuller(delta, autolag="AIC")
    
    # Adicionando tratamento de warnings para KPSS caso necessário
    kpss_n = kpss(nivel, regression="c", nlags="auto")
    kpss_d = kpss(delta, regression="c", nlags="auto")
    
    return [
        {"Série": nome, "Transformação": "Nível",  "Teste": "ADF",
         "H₀": "raiz unitária",     "Estat.": adf_n[0],  "p-valor": fmt_p(adf_n[1])},
        {"Série": nome, "Transformação": "Nível",  "Teste": "KPSS",
         "H₀": "estacionariedade",  "Estat.": kpss_n[0], "p-valor": fmt_p(kpss_n[1])},
        {"Série": nome, "Transformação": "Δ (1ª)", "Teste": "ADF",
         "H₀": "raiz unitária",     "Estat.": adf_d[0],  "p-valor": fmt_p(adf_d[1])},
        {"Série": nome, "Transformação": "Δ (1ª)", "Teste": "KPSS",
         "H₀": "estacionariedade",  "Estat.": kpss_d[0], "p-valor": fmt_p(kpss_d[1])},
    ]

def teste_jarque_bera_normalidade(serie: pd.Series) -> tuple[float, float]:
    """Calcula estatística Jarque-Bera e p-valor para normalidade dos resíduos."""
    delta = serie.diff().dropna()
    jb_stat, jb_p = stats.jarque_bera(delta)
    return jb_stat, jb_p

def teste_ljung_box_autocorrelacao(serie: pd.Series, lags: list = [10, 20]) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Calcula estatística Ljung-Box para autocorrelação em nível e em volatilidade."""
    delta = serie.diff().dropna()
    lb_d  = acorr_ljungbox(delta,    lags=lags, return_df=True)
    lb_d2 = acorr_ljungbox(delta**2, lags=lags, return_df=True)
    return lb_d, lb_d2

def testes_comparacao_distribuicoes(cdi_col: pd.Series, selic_col: pd.Series) -> tuple[float, float, float, float]:
    """Executa Wilcoxon pareado e teste t-relativo de Welch para igualdade de médias."""
    w_stat, w_p = stats.wilcoxon(cdi_col, selic_col)
    t_stat, t_p = stats.ttest_rel(cdi_col, selic_col)
    return w_stat, w_p, t_stat, t_p


def medias_por_regime(serie: pd.Series, candidatas: list[str],
                      inicio: str = "2010-01-01", fim: str = "2030-12-31") -> pd.DataFrame:
    """Segmenta a série em regimes delimitados por datas candidatas de quebra.

    `serie` deve ser indexada por data. Devolve count/mean/std por regime,
    com rótulos derivados das datas de corte.
    """
    bins = [pd.Timestamp(inicio)] + [pd.Timestamp(d) for d in candidatas] + [pd.Timestamp(fim)]
    labels = (
        [f"<{candidatas[0]}"]
        + [f"{candidatas[i]}–{candidatas[i + 1]}" for i in range(len(candidatas) - 1)]
        + [f">{candidatas[-1]}"]
    )
    grupo = pd.cut(serie.index, bins=bins, labels=labels, right=False)
    return serie.groupby(grupo).agg(["count", "mean", "std"])
