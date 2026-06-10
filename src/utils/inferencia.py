import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.diagnostic import acorr_ljungbox

# Dias de negociação padrão por ano
TRADING_DAYS = 252

def _alinhar_rf(rf, retornos):
    """Alinha rf à série de retornos. rf pode ser float ou Series indexada por data."""
    if isinstance(rf, pd.Series):
        if isinstance(retornos.index, pd.DatetimeIndex):
            return rf.reindex(retornos.index).ffill().bfill()
        return pd.Series(rf.values[-len(retornos):], index=retornos.index)
    return pd.Series(float(rf), index=retornos.index)

def sharpe(retornos, rf, fallback_rf=0.000369):
    """Calcula o Sharpe Ratio anualizado."""
    if rf is None:
        rf = fallback_rf
    rf_a = _alinhar_rf(rf, retornos)
    excesso = retornos - rf_a
    std_val = excesso.std()
    if std_val == 0:
        return 0.0
    return float(excesso.mean() / std_val * np.sqrt(TRADING_DAYS))

def sortino(retornos, rf, fallback_rf=0.000369):
    """Calcula o Sortino Ratio anualizado com MAR = rf."""
    if rf is None:
        rf = fallback_rf
    rf_a = _alinhar_rf(rf, retornos)
    excesso = retornos - rf_a
    dd = np.sqrt((excesso.clip(upper=0) ** 2).mean())
    if dd == 0:
        return np.inf
    return float(excesso.mean() / dd * np.sqrt(TRADING_DAYS))

def sharpe_de_excesso(excesso):
    std_val = excesso.std()
    if std_val == 0:
        return 0.0
    return float(excesso.mean() / std_val * np.sqrt(TRADING_DAYS))

def sortino_de_excesso(excesso):
    dd = np.sqrt((excesso.clip(upper=0) ** 2).mean())
    if dd == 0:
        return np.inf
    return float(excesso.mean() / dd * np.sqrt(TRADING_DAYS))

def cagr(retornos):
    n = len(retornos)
    if n == 0:
        return 0.0
    return float((1 + retornos).prod() ** (TRADING_DAYS / n) - 1)

def max_drawdown(retornos):
    eq = (1 + retornos).cumprod()
    if len(eq) == 0:
        return 0.0
    return float(((eq - eq.cummax()) / eq.cummax()).min())

def fmt_pvalor(p):
    """Formata p-valor com sinalização de significância clássica do R/Stata."""
    if p < 0.001:
        return "< 0,001 ***"
    if p < 0.01:
        return f"{p:.4f} ***"
    if p < 0.05:
        return f"{p:.4f} **"
    if p < 0.10:
        return f"{p:.4f} *"
    return f"{p:.4f}"

def _wald_spanning(y, X_const, maxlags=5):
    """Teste conjunto H0: alpha=0 e beta=1 (Huberman-Kandel) com erros NW robustos."""
    res = sm.OLS(y, X_const).fit(cov_type="HAC", cov_kwds={"maxlags": maxlags})
    w = res.wald_test((np.eye(2), np.array([0.0, 1.0])), use_f=True, scalar=True)
    return res, float(np.asarray(w.statistic).flatten()[0]), float(np.asarray(w.pvalue).flatten()[0])

def _jk_memmel(exc_a, exc_b):
    """Jobson-Korkie com correção de Memmel (2003) para comparação de Sharpe.

    [FIX G1b] Proteção contra std==0 (série de excesso constante): retorna
    z=0, p=1.0 (não rejeita H0), evitando NaN/inf que mascaravam resultados.
    """
    std_a = exc_a.std(ddof=1)
    std_b = exc_b.std(ddof=1)
    if std_a <= 1e-14 or std_b <= 1e-14:
        return 0.0, 1.0
    SRa = exc_a.mean() / std_a
    SRb = exc_b.mean() / std_b
    rho = exc_a.corr(exc_b)
    T = len(exc_a)
    theta = (1.0 / T) * (2 - 2 * rho + 0.5 * (SRa ** 2 + SRb ** 2 - 2 * SRa * SRb * (rho ** 2)))
    if theta <= 0:
        return 0.0, 1.0
    z = (SRa - SRb) / np.sqrt(theta)
    return float(z), float(2 * (1 - stats.norm.cdf(abs(z))))

def stationary_bootstrap_idx(n, block_mean, rng):
    """Gera índices para o Stationary Bootstrap (Politis & Romano, 1994)."""
    p = 1.0 / block_mean
    idx = np.empty(n, dtype=np.int64)
    idx[0] = rng.integers(0, n)
    for t in range(1, n):
        if rng.random() < p:
            idx[t] = rng.integers(0, n)
        else:
            idx[t] = (idx[t-1] + 1) % n
    return idx

def bootstrap_ic(serie, fn, B=1000, block_mean=21, seed=7):
    """Calcula intervalos de confiança de 95% via bootstrap percentil."""
    rng = np.random.default_rng(seed)
    n = len(serie)
    arr = serie.values if isinstance(serie, pd.Series) else np.asarray(serie)
    estats = np.empty(B)
    for b in range(B):
        amostra = arr[stationary_bootstrap_idx(n, block_mean, rng)]
        estats[b] = fn(pd.Series(amostra))
    return np.percentile(estats, [2.5, 50, 97.5])

def diagnosticos_serie(r, alpha_sig=0.05):
    """
    Bateria de diagnósticos para uma série de retornos de carteira:
    Jarque-Bera, Ljung-Box(10), ARCH-LM(10) e ADF.
    Justifica o uso de bootstrap em vez de testes paramétricos de Sharpe.
    """
    from statsmodels.stats.stattools import jarque_bera as _jb
    from statsmodels.stats.diagnostic import het_arch
    from statsmodels.tsa.stattools import adfuller
    arr = np.asarray(r, float); arr = arr[~np.isnan(arr)]
    jb_stat, jbp, sk, ku = _jb(arr)
    lbp   = float(acorr_ljungbox(arr, lags=[10], return_df=True)["lb_pvalue"].iloc[0])
    archp = float(het_arch(arr, nlags=10)[1])
    adfp  = float(adfuller(arr, autolag="AIC")[1])
    return {"assimetria": float(sk), "curtose": float(ku),
            "JB_p": float(jbp), "LjungBox_p": lbp,
            "ARCH_p": archp, "ADF_p": adfp,
            "normal?": "não" if jbp < alpha_sig else "sim"}

def lw_bootstrap_sharpe(ri, rj, bloco=10, reps=2000, seed=42):
    """
    Ledoit-Wolf (2008) via bootstrap estacionário para diferença de Sharpe diário.
    Retorna (dSR_anualizado, p_valor_bicaudal).
    """
    ri = np.asarray(ri, float); rj = np.asarray(rj, float)
    def _sr(x): s = x.std(ddof=1); return float(x.mean() / s) if s > 0 else 0.0
    diff_obs = _sr(ri) - _sr(rj)
    rng = np.random.default_rng(seed); n = len(ri)
    diffs = np.empty(reps)
    for b in range(reps):
        idx = stationary_bootstrap_idx(n, bloco, rng)   # mesmo índice para ambas as séries
        diffs[b] = _sr(ri[idx]) - _sr(rj[idx])
    se = diffs.std(ddof=1)
    z  = diff_obs / se if se > 0 else 0.0
    return float(diff_obs * np.sqrt(TRADING_DAYS)), float(2 * (1 - stats.norm.cdf(abs(z))))

def lw_bootstrap_sortino(ri, rj, rf=0.0, bloco=10, reps=2000, seed=42):
    """
    Bootstrap estacionário para diferença de Sortino diário.
    Retorna (dSortino_anualizado, p_valor_bicaudal).
    """
    ri = np.asarray(ri, float); rj = np.asarray(rj, float); rf = float(rf)
    def _so(x):
        exc = x - rf; dn = np.sqrt(np.mean(np.clip(exc, None, 0) ** 2))
        return float(exc.mean() / dn) if dn > 0 else 0.0
    diff_obs = _so(ri) - _so(rj)
    rng = np.random.default_rng(seed); n = len(ri)
    diffs = np.empty(reps)
    for b in range(reps):
        idx = stationary_bootstrap_idx(n, bloco, rng)   # mesmo índice para ambas as séries
        diffs[b] = _so(ri[idx]) - _so(rj[idx])
    se = diffs.std(ddof=1)
    z  = diff_obs / se if se > 0 else 0.0
    return float(diff_obs * np.sqrt(TRADING_DAYS)), float(2 * (1 - stats.norm.cdf(abs(z))))

def diagnostico_residuos(res, nome):
    """Executa diagnósticos de resíduos padronizados do modelo GARCH."""
    z = res.std_resid.dropna()
    # Efetua teste de Ljung-Box sobre resíduos e resíduos ao quadrado
    lb_z = acorr_ljungbox(z, lags=[10], return_df=True).iloc[0]
    lb_z2 = acorr_ljungbox(z ** 2, lags=[10], return_df=True).iloc[0]
    return {
        "Modelo": nome,
        "AIC": float(res.aic),
        "BIC": float(res.bic),
        "Log-Lik": float(res.loglikelihood),
        "LB Q(10) em z": float(lb_z["lb_pvalue"]),
        "LB Q(10) em z²": float(lb_z2["lb_pvalue"])
    }

def calcular_dsr(sharpe_best, sharpes, T, skew, kurt, N):
    """
    Calcula o Deflated Sharpe Ratio (DSR) de Bailey & López de Prado (2012).
    
    Args:
        sharpe_best (float): Sharpe Ratio anualizado da melhor estratégia.
        sharpes (list/np.ndarray): Sharpe Ratios anualizados de todas as estratégias testadas.
        T (int): Comprimento da amostra (número de dias úteis).
        skew (float): Assimetria (skewness) dos retornos diários da melhor estratégia.
        kurt (float): Curtose (kurtosis) dos retornos diários da melhor estratégia (não-excedente).
        N (int): Número de estratégias testadas.
        
    Returns:
        float: DSR (probabilidade em [0, 1]).
    """
    std_sr = np.std(sharpes, ddof=1) if len(sharpes) > 1 else 0.0
    if std_sr <= 1e-14:  # tolerância de ponto flutuante (convenção do projeto)
        return 0.0
        
    euler = 0.5772156649
    q = 1.0 - 1.0 / N
    q_e = 1.0 - 1.0 / (N * np.e)
    
    # expected max SR under H0 (independent trials)
    sr0 = std_sr * ((1.0 - euler) * stats.norm.ppf(q) + euler * stats.norm.ppf(q_e))
    
    if kurt < 1.0: # safety guard
        kurt = 3.0
        
    # daily equivalent values
    sr_d = sharpe_best / np.sqrt(TRADING_DAYS)
    sr0_d = sr0 / np.sqrt(TRADING_DAYS)
    
    # variance of daily Sharpe ratio estimate
    var_srd = (1.0 - skew * sr_d + (kurt - 1.0) / 4.0 * sr_d**2) / (T - 1.0)
    
    if var_srd <= 0.0:
        return 0.0
        
    z = (sr_d - sr0_d) / np.sqrt(var_srd)
    return float(stats.norm.cdf(z))

def deflated_sharpe_ratio(retornos_best, all_sharpes):
    """
    Calcula o Deflated Sharpe Ratio (DSR) de Bailey & López de Prado (2012).
    
    Args:
        retornos_best (pd.Series/np.ndarray): Série de retornos diários da melhor estratégia.
        all_sharpes (list/np.ndarray): Sharpe Ratios anualizados de todas as estratégias testadas.
        
    Returns:
        float: DSR (probabilidade em [0, 1]).
    """
    r = np.asarray(retornos_best, float)
    r = r[~np.isnan(r)]
    T = len(r)
    if T <= 2:
        return 0.0
        
    s = r.std(ddof=1)
    if s == 0:
        return 0.0
    sr_best_daily = float(r.mean() / s)
    sr_best = sr_best_daily * np.sqrt(TRADING_DAYS)
    
    skew = float(stats.skew(r))
    kurt = float(stats.kurtosis(r, fisher=False)) # actual kurtosis (Fisher=False means normal=3)
    
    N = len(all_sharpes)
    
    return calcular_dsr(sr_best, all_sharpes, T, skew, kurt, N)

def matriz_correlacao_significancia(df_retornos):
    """
    Calcula a matriz de correlação de Pearson e a correspondente matriz de p-valores
    para testar H0: rho = 0 (sem correlação linear) de forma bilateral.
    
    Args:
        df_retornos (pd.DataFrame): DataFrame com retornos das estratégias (T x N).
        
    Returns:
        tuple[pd.DataFrame, pd.DataFrame]: (matriz_correlação, matriz_pvalores).
    """
    corr = df_retornos.corr()
    p_values = pd.DataFrame(np.zeros_like(corr.values), columns=corr.columns, index=corr.index)
    T = len(df_retornos)
    if T <= 2:
        return corr, p_values
        
    for i in corr.index:
        for j in corr.columns:
            if i == j:
                p_values.loc[i, j] = 0.0
            else:
                r = corr.loc[i, j]
                denom = np.sqrt(1.0 - r**2)
                if denom <= 1e-15:
                    p_values.loc[i, j] = 0.0
                else:
                    t_stat = r * np.sqrt((T - 2) / (1.0 - r**2))
                    p_values.loc[i, j] = float(2.0 * (1.0 - stats.t.cdf(abs(t_stat), df=T-2)))
    return corr, p_values

def regressao_multifatorial(ret_carteira, df_fatores, maxlags=5):
    """
    Roda regressão OLS multifatorial com constante e estimador HAC de Newey-West.
    
    Args:
        ret_carteira (pd.Series): Retornos da carteira.
        df_fatores (pd.DataFrame): DataFrame contendo os fatores de risco (ex: MKT, SMB, HML).
        maxlags (int): Defasagem para o estimador Newey-West.
        
    Returns:
        dict: Resultados estatísticos consolidados.
    """
    dados = pd.concat([ret_carteira.rename("ret_p"), df_fatores], axis=1, join="inner").dropna()
    y = dados["ret_p"]
    X = dados.drop(columns=["ret_p"])
    X_const = sm.add_constant(X)
    
    res = sm.OLS(y, X_const).fit(cov_type="HAC", cov_kwds={"maxlags": maxlags})
    
    params = {}
    for idx, name in enumerate(X_const.columns):
        params[name] = {
            "coef": float(res.params.iloc[idx]),
            "std_err": float(res.bse.iloc[idx]),
            "t_stat": float(res.tvalues.iloc[idx]),
            "p_value": float(res.pvalues.iloc[idx])
        }
        
    return {
        "params": params,
        "r2": float(res.rsquared),
        "r2_adj": float(res.rsquared_adj),
        "f_pvalue": float(res.f_pvalue) if hasattr(res, "f_pvalue") else None,
        "nobs": int(res.nobs)
    }

def spanning_multivariado(df_ativos_teste, df_benchmarks, maxlags=5):
    """
    Realiza o teste multivariado de Spanning de Portfólio de Huberman & Kandel (1987)
    com suporte a erros padrão HAC (Newey-West) e correlação contemporânea entre ativos (SUR stacked OLS).
    
    Args:
        df_ativos_teste (pd.DataFrame): DataFrame com retornos das carteiras teste (T x N).
        df_benchmarks (pd.DataFrame): DataFrame com retornos dos benchmarks de referência (T x K).
        maxlags (int): Defasagem de Newey-West.
        
    Returns:
        tuple[float, float]: (estatística_Wald, p-valor).
    """
    dados = pd.concat([df_ativos_teste, df_benchmarks], axis=1, join="inner").dropna()
    N = df_ativos_teste.shape[1]
    K = df_benchmarks.shape[1]
    T = len(dados)
    
    Y = dados[df_ativos_teste.columns].values
    X = dados[df_benchmarks.columns].values
    X_const = np.column_stack([np.ones(T), X])
    
    y_stacked = Y.T.flatten()
    
    from scipy.sparse import block_diag
    X_stacked = block_diag([X_const] * N).toarray()
    
    res = sm.OLS(y_stacked, X_stacked).fit(cov_type="HAC", cov_kwds={"maxlags": maxlags})
    
    num_vars_eq = K + 1
    R_joint = np.zeros((2 * N, N * num_vars_eq))
    r_joint = np.zeros(2 * N)
    
    for i in range(N):
        R_joint[2 * i, i * num_vars_eq] = 1.0
        r_joint[2 * i] = 0.0
        
        for j in range(1, num_vars_eq):
            R_joint[2 * i + 1, i * num_vars_eq + j] = 1.0
        r_joint[2 * i + 1] = 1.0
        
    wald = res.wald_test((R_joint, r_joint), use_f=True, scalar=True)
    return float(np.asarray(wald.statistic).flatten()[0]), float(np.asarray(wald.pvalue).flatten()[0])



