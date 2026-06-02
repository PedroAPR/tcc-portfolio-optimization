import numpy as np
from scipy.optimize import minimize

try:
    import cvxpy as cp
    CVXPY_OK = True
    _SOLVERS = [s for s in ("CLARABEL", "ECOS", "SCS") if s in cp.installed_solvers()]
except Exception:
    CVXPY_OK = False
    _SOLVERS = []

def ledoit_wolf(X):
    """
    Estimador de encolhimento (shrinkage) de Ledoit & Wolf (2004).
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
        
    # b2bar: Cálculo vetorizado de O(T * N)
    term1 = np.sum(np.sum(Xc ** 2, axis=1) ** 2)
    term2 = T * np.sum(S ** 2)
    b2bar = (term1 - term2) / (T ** 2 * N)
    
    b2 = min(b2bar, d2)
    delta = b2 / d2
    return delta * F + (1.0 - delta) * S

def _bounds(n, teto=None):
    hi = teto if teto is not None else 1.0
    return [(0.0, hi)] * n

def port_ret(w, mu):
    return float(w @ mu)

def port_vol(w, Sig):
    return float(np.sqrt(w @ Sig @ w))

def min_var(Sig, mu, teto=None, ret_alvo=None):
    """Calcula carteira de Mínima Variância com restrição de retorno opcional."""
    n = Sig.shape[0]
    w0 = np.repeat(1.0 / n, n)
    cons = [{"type": "eq", "fun": lambda w: w.sum() - 1.0}]
    if ret_alvo is not None:
        cons.append({"type": "eq", "fun": lambda w: w @ mu - ret_alvo})
        
    r = minimize(lambda w: w @ Sig @ w, w0, method="SLSQP", bounds=_bounds(n, teto),
                 constraints=cons, options={"maxiter": 600, "ftol": 1e-11})
    return r.x / r.x.sum()

def max_sharpe(mu, Sig, rf_anual, teto=None):
    """Calcula carteira de Máximo Índice de Sharpe."""
    n = len(mu)
    w0 = np.repeat(1.0 / n, n)
    cons = [{"type": "eq", "fun": lambda w: w.sum() - 1.0}]
    
    def neg_sharpe(w):
        vol = port_vol(w, Sig)
        return -((w @ mu - rf_anual) / vol) if vol > 0 else 0.0
        
    r = minimize(neg_sharpe, w0, method="SLSQP", bounds=_bounds(n, teto),
                 constraints=cons, options={"maxiter": 800, "ftol": 1e-11})
    return r.x / r.x.sum()

def min_cvar(R, mu, alpha=0.95, ret_alvo=None, teto=None):
    """Calcula a carteira de Mínimo CVaR usando programação linear com CVXPY."""
    if not CVXPY_OK:
        return None
        
    T, n = R.shape
    w = cp.Variable(n)
    z = cp.Variable()
    u = cp.Variable(T, nonneg=True)
    
    cons = [cp.sum(w) == 1, u >= (-R @ w) - z, w >= 0]
    if teto:
        cons.append(w <= teto)
    if ret_alvo is not None:
        cons.append(w @ mu >= ret_alvo)
        
    cvar = z + (1.0 / ((1 - alpha) * T)) * cp.sum(u)
    prob = cp.Problem(cp.Minimize(cvar), cons)
    
    for solver_name in _SOLVERS:
        try:
            if solver_name == "CLARABEL":
                prob.solve(solver=cp.CLARABEL, tol_gap_abs=1e-6, tol_gap_rel=1e-6, verbose=False)
            elif solver_name == "ECOS":
                prob.solve(solver=cp.ECOS, abstol=1e-6, reltol=1e-6, verbose=False)
            else:
                prob.solve(solver=getattr(cp, solver_name))
            if prob.status in ("optimal", "optimal_inaccurate"):
                break
        except Exception:
            continue
            
    if w.value is None:
        return None
    return np.clip(np.asarray(w.value).flatten(), 0, None)

def cvar_diario(w, R, alpha=0.95):
    """Retorna o CVaR diário para um determinado vetor de pesos."""
    perdas = -R @ w
    var = np.quantile(perdas, alpha)
    return float(perdas[perdas >= var].mean())
