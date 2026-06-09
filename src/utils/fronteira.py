import numpy as np
from scipy.optimize import minimize
from pathlib import Path

try:
    import cvxpy as cp
    CVXPY_OK = True
    _SOLVERS = [s for s in ("CLARABEL", "ECOS", "SCS") if s in cp.installed_solvers()]
except Exception:
    CVXPY_OK = False
    _SOLVERS = []

# Importa a implementação canônica e otimizações locais
from .covariancia import ledoit_wolf as _ledoit_wolf_canonical
from .otimizacao import w_max_sharpe, _resolver_robusto, _pesos_validos

def ledoit_wolf(X):
    """
    Estimador de encolhimento (shrinkage) de Ledoit & Wolf (2004).
    Invoca a implementação canônica de covariancia.py.
    """
    return _ledoit_wolf_canonical(X)[0]

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
    cons = [{"type": "eq", "fun": lambda w: w.sum() - 1.0, "jac": lambda w: np.ones(n)}]
    if ret_alvo is not None:
        cons.append({"type": "eq", "fun": lambda w: w @ mu - ret_alvo, "jac": lambda w: mu})
        
    r = minimize(
        lambda w: w @ Sig @ w,
        w0,
        method="SLSQP",
        jac=lambda w: 2.0 * Sig @ w,  # ← gradiente analítico!
        bounds=_bounds(n, teto),
        constraints=cons,
        options={"maxiter": 600, "ftol": 1e-11}
    )
    return r.x / r.x.sum()

def max_sharpe(mu, Sig, rf_anual, teto=None):
    """Calcula carteira de Máximo Índice de Sharpe usando a implementação robusta com gradiente analítico."""
    return w_max_sharpe(mu, Sig, rf_anual, teto)

def min_cvar(R, mu, alpha=0.95, ret_alvo=None, teto=None):
    """Calcula a carteira de Mínimo CVaR usando programação linear com CVXPY e validação robusta."""
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
    
    status = _resolver_robusto(prob, tol=1e-6)  # tolerância estrita de cauda
    w_val = None if w.value is None else np.asarray(w.value, float).flatten()
    
    if status != "optimal" or not _pesos_validos(w_val):
        return None
        
    x = np.clip(w_val, 0.0, None)
    return x / x.sum()

def cvar_diario(w, R, alpha=0.95):
    """Retorna o CVaR diário para um determinado vetor de pesos."""
    perdas = -R @ w
    var = np.quantile(perdas, alpha)
    return float(perdas[perdas >= var].mean())
