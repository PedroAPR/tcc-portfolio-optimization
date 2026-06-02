import os
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import minimize

try:
    import cvxpy as cp
    CVXPY_OK = True
    _SOLVERS = [s for s in ("CLARABEL", "ECOS", "SCS") if s in cp.installed_solvers()]
except Exception as e:
    CVXPY_OK = False
    _SOLVERS = []

def ledoit_wolf(X):
    """
    Estimador de encolhimento (shrinkage) de Ledoit & Wolf (2004)
    em direção à matriz de covariância isotrópica média.
    Versão ultra-veloz e vetorizada de complexidade O(T * N).
    """
    X = np.asarray(X, float)
    T, N = X.shape
    if T <= 1:
        raise ValueError("O número de observações (T) deve ser maior que 1.")
        
    Xc = X - X.mean(axis=0)
    S = (Xc.T @ Xc) / T
    
    mu = np.trace(S) / N
    F = mu * np.eye(N)
    
    d2 = np.sum((S - F) ** 2) / N
    if d2 == 0:
        return S
        
    # b2bar: Cálculo vetorizado (sem loops Python)
    term1 = np.sum(np.sum(Xc ** 2, axis=1) ** 2)
    term2 = T * np.sum(S ** 2)
    b2bar = (term1 - term2) / (T ** 2 * N)
    
    b2 = min(b2bar, d2)
    delta = b2 / d2
    return delta * F + (1.0 - delta) * S

def estimar_sigma(janela, metodo="ledoit_wolf"):
    """Retorna a matriz de covariância estimada de acordo com o método selecionado."""
    if metodo == "amostral":
        return np.cov(janela, rowvar=False)
    return ledoit_wolf(janela)

def _bounds(n, teto, long_only=True):
    hi = teto if teto is not None else 1.0
    return [(0.0, hi)] * n if long_only else [(-hi, hi)] * n

def w_equal(n):
    """Retorna pesos igualmente ponderados (1/N)."""
    return np.repeat(1.0 / n, n)

def w_inv_vol(S):
    """Retorna pesos ponderados pelo inverso da volatilidade individual."""
    iv = 1.0 / np.sqrt(np.diag(S))
    return iv / iv.sum()

def w_min_var(S, teto=None, long_only=True):
    """Resolve a carteira de Mínima Variância Global via SLSQP."""
    n = S.shape[0]
    _cons = ({"type": "eq", "fun": lambda w: w.sum() - 1.0},)
    r = minimize(lambda w: w @ S @ w, w_equal(n), method="SLSQP",
                 bounds=_bounds(n, teto, long_only), constraints=_cons,
                 options={"maxiter": 300, "ftol": 1e-10})
    return r.x / r.x.sum()

def w_max_sharpe(mu, S, rf_a, teto=None, long_only=True):
    """Resolve a carteira de Máximo Índice de Sharpe via SLSQP."""
    n = len(mu)
    _cons = ({"type": "eq", "fun": lambda w: w.sum() - 1.0},)
    def neg_sharpe(w):
        v = np.sqrt(w @ S @ w)
        return -((w @ mu - rf_a) / v) if v > 0 else 0.0
    r = minimize(neg_sharpe, w_equal(n), method="SLSQP",
                 bounds=_bounds(n, teto, long_only), constraints=_cons,
                 options={"maxiter": 400, "ftol": 1e-10})
    return r.x / r.x.sum()

def w_max_kappa(janela, n=2, mar=0.0, teto=None, long_only=True):
    """
    Resolve o problem não-convexo de maximizar a medida Kappa de ordem n
    (n=1 Omega, n=2 Sortino, n=3 Kappa-3) via SLSQP.
    """
    janela = np.asarray(janela, float); T, k = janela.shape
    _cons = ({"type": "eq", "fun": lambda w: w.sum() - 1.0},)
    def neg(w):
        rp = janela @ w
        ex = rp - mar
        lpm = np.mean(np.clip(mar - rp, 0.0, None) ** n)
        if lpm <= 1e-18:
            return 0.0 if ex.mean() <= 0 else -1e6
        return -ex.mean() / (lpm ** (1.0 / n))
    r = minimize(neg, w_equal(k), method="SLSQP",
                 bounds=_bounds(k, teto, long_only), constraints=_cons,
                 options={"maxiter": 500, "ftol": 1e-12})
    return r.x / r.x.sum()

def _solve(prob):
    """Tenta resolver o problema convexo usando os solvers disponíveis em ordem de robustez."""
    for s in _SOLVERS:
        try:
            prob.solve(solver=getattr(cp, s))
            if prob.status in ("optimal", "optimal_inaccurate"):
                return True
        except Exception:
            continue
    return False

def w_min_cvar(cenarios, alpha=0.95, teto=None, long_only=True):
    """Resolve a carteira de Mínimo CVaR (Rockafellar-Uryasev) via LP Convexo."""
    if not CVXPY_OK:
        raise RuntimeError("cvxpy indisponível para CVaR")
    R = np.asarray(cenarios, float); T, k = R.shape
    w = cp.Variable(k); zeta = cp.Variable(); u = cp.Variable(T, nonneg=True)
    perdas = -R @ w
    hi = teto if teto is not None else 1.0
    cons = [cp.sum(w) == 1, u >= perdas - zeta]
    if long_only:
        cons += [w >= 0, w <= hi]
    cvar = zeta + (1.0 / ((1 - alpha) * T)) * cp.sum(u)
    prob = cp.Problem(cp.Minimize(cvar), cons)
    
    for solver_name in _SOLVERS:
        try:
            if solver_name == "CLARABEL":
                prob.solve(solver=cp.CLARABEL, tol_gap_abs=1e-5, tol_gap_rel=1e-5, verbose=False)
            elif solver_name == "ECOS":
                prob.solve(solver=cp.ECOS, abstol=1e-5, reltol=1e-5, verbose=False)
            else:
                prob.solve(solver=getattr(cp, solver_name))
            if prob.status in ("optimal", "optimal_inaccurate"):
                break
        except Exception:
            continue
            
    x = np.clip(np.asarray(w.value).flatten(), 0, None)
    return x / x.sum()

def w_min_cdar(cenarios, alpha=0.95, teto=None, long_only=True):
    """Resolve a carteira de Mínimo CDaR (Chekhlov-Uryasev-Zabarankin) via LP Convexo."""
    if not CVXPY_OK:
        raise RuntimeError("cvxpy indisponível para CDaR")
    R = np.asarray(cenarios, float); T, k = R.shape
    Rcum = np.cumsum(R, axis=0)
    w = cp.Variable(k); u = cp.Variable(T); z = cp.Variable(T, nonneg=True); zeta = cp.Variable()
    C = Rcum @ w
    hi = teto if teto is not None else 1.0
    cons = [cp.sum(w) == 1, u >= C, u[1:] >= u[:-1], u[0] >= 0, z >= (u - C) - zeta]
    if long_only:
        cons += [w >= 0, w <= hi]
    cdar = zeta + (1.0 / ((1 - alpha) * T)) * cp.sum(z)
    prob = cp.Problem(cp.Minimize(cdar), cons)
    
    for solver_name in _SOLVERS:
        try:
            if solver_name == "CLARABEL":
                prob.solve(solver=cp.CLARABEL, tol_gap_abs=1e-5, tol_gap_rel=1e-5, verbose=False)
            elif solver_name == "ECOS":
                prob.solve(solver=cp.ECOS, abstol=1e-5, reltol=1e-5, verbose=False)
            else:
                prob.solve(solver=getattr(cp, solver_name))
            if prob.status in ("optimal", "optimal_inaccurate"):
                break
        except Exception:
            continue
            
    x = np.clip(np.asarray(w.value).flatten(), 0, None)
    return x / x.sum()

def otimizar_mes_task(args):
    """
    Task de otimização executada em paralelo para um mês i do backtest.
    Carrega os dados de cotações de forma independente no processo filho
    para evitar overhead de serialização (IPC) e problemas de memória no Windows.
    """
    (i, data_rebal, dir_retornos_str, N, ALPHA, TETO_PESO, KAPPA_ORDENS, 
     CVXPY_OK, REBAL, WARMUP_MESES, TRADING_DAYS, METODO_COV, MAR_MODO) = args
    
    dir_retornos = Path(dir_retornos_str)
    pq_ret = dir_retornos / "retornos_simples_saneado.parquet"
    csv_ret = dir_retornos / "retornos_simples_saneado.csv"
    
    if pq_ret.exists():
        ret = pd.read_parquet(pq_ret)
    else:
        ret = pd.read_csv(csv_ret, index_col=0, parse_dates=True)
    ret.index = pd.to_datetime(ret.index)
    ret = ret.sort_index()
    
    rf_csv = dir_retornos / "rf_diario.csv"
    rf = pd.read_csv(rf_csv, index_col=0, parse_dates=True)["cdi_diario"].sort_index()
    
    periodos = ret.index.to_period(REBAL)
    uperiodos = pd.Index(periodos.unique())
    
    fim_prev = ret.index[periodos == uperiodos[i - 1]][-1]
    janela = ret.loc[:fim_prev]
    
    Jv = janela.values
    S = estimar_sigma(Jv, metodo=METODO_COV)
    mu = janela.mean().values * TRADING_DAYS
    rf_j = rf.reindex(janela.index).dropna()
    rf_a = rf_j.mean() * TRADING_DAYS
    mar_d = float(rf_j.mean()) if MAR_MODO == "cdi" else 0.0
    
    alvos = {
        "EqualWeight":   w_equal(N),
        "InvVol":        w_inv_vol(S),
        "MinVar":        w_min_var(S, None),
        "MinVar_c10":    w_min_var(S, TETO_PESO),
        "MaxSharpe":     w_max_sharpe(mu, S, rf_a, None),
        "MaxSharpe_c10": w_max_sharpe(mu, S, rf_a, TETO_PESO),
    }
    
    for nome, n in KAPPA_ORDENS.items():
        alvos[nome] = w_max_kappa(Jv, n=n, mar=mar_d, teto=None)
        
    if CVXPY_OK:
        try:
            alvos["MinCVaR"] = w_min_cvar(Jv, ALPHA, None)
        except Exception:
            alvos["MinCVaR"] = w_equal(N)
        try:
            alvos["MinCDaR"] = w_min_cdar(Jv, ALPHA, None)
        except Exception:
            alvos["MinCDaR"] = w_equal(N)
            
    return i, data_rebal, alvos
