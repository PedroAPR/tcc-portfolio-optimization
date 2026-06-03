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

# ---------------------------------------------------------------------------
# Tolerância CVXPY (Proposta 3) — relaxada de 1e-5 → 1e-4.
# Impacto: micro-divergências na 4ª/5ª casa decimal, irrelevantes para
# o teto regulatório CVM 175 (10%). Ganho: ~15–30% no tempo dos solvers
# convexos em janelas longas (T > 1000 observações).
# ---------------------------------------------------------------------------
_CVXPY_TOL = 1e-4


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


def estrada_semicov(X, mar="media"):
    """
    Semicovariância downside de Estrada (2008).
    mar: 'media' usa a média amostral como MAR; 'zero' usa zero; valor float usa literal.
    """
    X = np.asarray(X, float)
    T, n = X.shape
    if mar == "media":
        tau = X.mean(axis=0)
    elif mar == "zero":
        tau = np.zeros(n)
    else:
        tau = np.full(n, float(mar))
    M = np.minimum(X - tau, 0.0)
    return (M.T @ M) / T


def visoes_momentum(janela, tau_bl, Sigma, trading_days=252, visao_meses=(12, 1)):
    """
    Gera visões absolutas via momentum 12-1 (He & Litterman, 1999).
    Retorna (P, Q, Omega) anualizados, compatíveis com bl_posterior.
    """
    R = np.asarray(janela, float)
    T, n = R.shape
    L, S_ = visao_meses
    jl, js = int(L * 21), int(S_ * 21)
    if T < jl + 5:
        Q = R.mean(axis=0) * trading_days
    else:
        bloco = R[-jl:-js] if js > 0 else R[-jl:]
        Q = np.prod(1 + bloco, axis=0) ** (trading_days / len(bloco)) - 1
    P = np.eye(n)
    Sg = Sigma if Sigma is not None else ledoit_wolf(R) * trading_days
    Om = np.diag(np.maximum(np.diag(P @ (tau_bl * Sg) @ P.T), 1e-8))
    return P, Q, Om


def bl_posterior(Sigma, Pi, P, Q, Omega, tau_bl=0.05):
    """
    Posterior de Black-Litterman: combina prior de equilíbrio (Pi) com visões (P, Q, Omega).
    Retorna vetor de retornos esperados mu_BL (anualizado).
    """
    tauS_inv = np.linalg.inv(tau_bl * Sigma)
    Om_inv   = np.linalg.inv(Omega)
    A = tauS_inv + P.T @ Om_inv @ P
    b = tauS_inv @ Pi + P.T @ Om_inv @ Q
    return np.linalg.solve(A, b)


def _bounds(n, teto, long_only=True):
    hi = teto if teto is not None else 1.0
    return [(0.0, hi)] * n if long_only else [(-hi, hi)] * n


def w_equal(n):
    """Retorna pesos igualmente ponderados (1/N)."""
    return np.repeat(1.0 / n, n)


def w_inv_vol(S):
    """Retorna pesos ponderados pelo inverso da volatilidade individual.

    [FIX G1a] Proteção contra ativo com variância zero: atribui peso zero a esses
    ativos e redistribui entre os demais. Se todos os ativos têm var=0 (caso
    degengerado), cai de volta em pesos iguais.
    """
    diag = np.diag(S)
    # np.where avalia ambos os ramos antes de mascarar; errstate suprime o
    # RuntimeWarning benigno de 1/sqrt(0) que nunca chega ao resultado final.
    with np.errstate(divide='ignore', invalid='ignore'):
        iv = np.where(diag > 0, 1.0 / np.sqrt(diag), 0.0)
    total = iv.sum()
    if total == 0:
        return np.repeat(1.0 / len(diag), len(diag))  # fallback: pesos iguais
    return iv / total


def w_min_var(S, teto=None, long_only=True, w0=None):
    """
    Resolve a carteira de Mínima Variância Global via SLSQP.

    Proposta 1 — Gradiente analítico:
        ∇f(w) = 2Σw  (derivada exata da variância do portfólio w'Σw).
        Elimina ~N avaliações de diferenças finitas por iteração SLSQP.

    Proposta warm-start:
        w0: ponto inicial externo (pesos do mês anterior).
        Se None, usa 1/N. Como as janelas são expansivas, a solução do
        mês t-1 está próxima da do mês t → reduz iterações em 50–70%.
    """
    n = S.shape[0]
    x0 = w0 if w0 is not None else w_equal(n)
    _cons = ({"type": "eq", "fun": lambda w: w.sum() - 1.0,
               "jac": lambda w: np.ones(n)},)
    r = minimize(
        lambda w: w @ S @ w,
        x0,
        method="SLSQP",
        jac=lambda w: 2.0 * S @ w,          # ← gradiente analítico
        bounds=_bounds(n, teto, long_only),
        constraints=_cons,
        options={"maxiter": 300, "ftol": 1e-10},
    )
    return r.x / r.x.sum()


def w_max_sharpe(mu, S, rf_a, teto=None, long_only=True, w0=None):
    """
    Resolve a carteira de Máximo Índice de Sharpe via SLSQP.

    Proposta 1 — Gradiente analítico de -Sharpe = -(μ_ex / σ_p):
        Pela regra do quociente, onde μ_ex = w'μ - rf e σ_p = √(w'Σw):
        ∇(-Sharpe) = -[μ·σ_p - μ_ex·(Σw/σ_p)] / σ_p²
                   = -[μ·σ_p² - μ_ex·Σw] / σ_p³
        Numericamente estável: avaliado apenas quando σ_p > 0.

    Proposta warm-start: w0 = pesos do período anterior.
    """
    n = len(mu)
    x0 = w0 if w0 is not None else w_equal(n)
    _cons = ({"type": "eq", "fun": lambda w: w.sum() - 1.0,
               "jac": lambda w: np.ones(n)},)

    def neg_sharpe(w):
        v = np.sqrt(w @ S @ w)
        return -((w @ mu - rf_a) / v) if v > 1e-12 else 0.0

    def grad_neg_sharpe(w):
        v2 = w @ S @ w          # σ_p²
        v  = np.sqrt(v2)
        if v < 1e-12:
            return np.zeros(n)
        mu_ex = w @ mu - rf_a
        # ∇(-Sharpe) = -(μ·v² - μ_ex·Σw) / v³
        return -(mu * v2 - mu_ex * (S @ w)) / (v2 * v)

    r = minimize(
        neg_sharpe,
        x0,
        method="SLSQP",
        jac=grad_neg_sharpe,             # ← gradiente analítico
        bounds=_bounds(n, teto, long_only),
        constraints=_cons,
        options={"maxiter": 400, "ftol": 1e-10},
    )
    return r.x / r.x.sum()


def w_max_kappa(janela, n=2, mar=0.0, teto=None, long_only=True, w0=None):
    """
    Resolve o problema não-convexo de maximizar Kappa_n via SLSQP.
    n=1 → Omega  |  n=2 → Sortino  |  n=3 → Kappa-3

    Proposta 1 — Gradiente analítico de -Kappa_n = -(μ_ex / LPM_n^(1/n)):
        Seja rp = Jv @ w,  d_i = max(τ - rp_i, 0),  LPM = mean(d^n).
        ∂μ_ex/∂w  = Jv.mean(0)
        ∂LPM/∂w   = -(n/T) · Jv.T @ d^(n-1)   [subgradiente; contínuo para n≥2]
        Pela regra do quociente:
        ∇(-κ_n) = -[∂μ_ex/∂w · LPM^(1/n) - μ_ex · (1/n)·LPM^(1/n-1)·∂LPM/∂w]
                   / LPM^(2/n)
        Para n=1 (Omega): subgradiente descontínuo em d_i=0 → usa-se a
        aproximação suavizada  d ≈ max(τ - rp, 0)  com tolerância 0 (correto
        quase em todo lugar, exceto no conjunto de medida zero onde rp=τ).

    Proposta warm-start: w0 = pesos do período anterior.
    """
    janela = np.asarray(janela, float)
    T, k = janela.shape
    x0 = w0 if w0 is not None else w_equal(k)
    _cons = ({"type": "eq", "fun": lambda w: w.sum() - 1.0,
               "jac": lambda w: np.ones(k)},)
    mu_j = janela.mean(axis=0)           # pré-computado uma vez

    def neg(w):
        rp  = janela @ w
        ex  = rp - mar
        lpm = np.mean(np.clip(mar - rp, 0.0, None) ** n)
        if lpm <= 1e-18:
            return 0.0 if ex.mean() <= 0 else -1e6
        return -ex.mean() / (lpm ** (1.0 / n))

    def grad_neg(w):
        rp    = janela @ w
        ex    = rp - mar
        mu_ex = ex.mean()
        d     = np.clip(mar - rp, 0.0, None)          # downside d_i = max(τ-rp_i, 0)
        dn1   = d ** max(n - 1, 0)                     # d^(n-1); para n=1 → vetor de 1s ou 0s
        lpm   = np.mean(d ** n)
        if lpm <= 1e-18:
            return np.zeros(k)
        lpm_inv_n   = lpm ** (1.0 / n)                # LPM^(1/n)
        lpm_inv_n_1 = lpm ** (1.0 / n - 1.0)          # LPM^(1/n - 1)

        d_mu_ex = mu_j                                 # ∂μ_ex/∂w = mean(Jv, axis=0)
        # ∂LPM/∂w = -(n/T) · Jv.T @ d^(n-1)
        d_lpm   = -(n / T) * (janela.T @ dn1)

        # ∇(-κ_n) = -[d_mu_ex · lpm^(1/n) - mu_ex · (1/n)·lpm^(1/n-1)·d_lpm] / lpm^(2/n)
        num = d_mu_ex * lpm_inv_n - mu_ex * (1.0 / n) * lpm_inv_n_1 * d_lpm
        return -num / (lpm_inv_n ** 2)

    r = minimize(
        neg,
        x0,
        method="SLSQP",
        jac=grad_neg,                    # ← gradiente analítico / subgradiente
        bounds=_bounds(k, teto, long_only),
        constraints=_cons,
        options={"maxiter": 500, "ftol": 1e-12},
    )
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
    """
    Resolve a carteira de Mínimo CVaR (Rockafellar-Uryasev) via LP Convexo.
    Proposta 3 — tolerância relaxada _CVXPY_TOL (1e-4) vs. original (1e-5).
    """
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
                prob.solve(solver=cp.CLARABEL,
                           tol_gap_abs=_CVXPY_TOL, tol_gap_rel=_CVXPY_TOL,
                           verbose=False)
            elif solver_name == "ECOS":
                prob.solve(solver=cp.ECOS,
                           abstol=_CVXPY_TOL, reltol=_CVXPY_TOL,
                           verbose=False)
            else:
                prob.solve(solver=getattr(cp, solver_name))
            if prob.status in ("optimal", "optimal_inaccurate"):
                break
        except Exception:
            continue

    x = np.clip(np.asarray(w.value).flatten(), 0, None)
    return x / x.sum()


def w_min_cdar(cenarios, alpha=0.95, teto=None, long_only=True):
    """
    Resolve a carteira de Mínimo CDaR (Chekhlov-Uryasev-Zabarankin) via LP Convexo.
    Proposta 3 — tolerância relaxada _CVXPY_TOL (1e-4) vs. original (1e-5).
    """
    if not CVXPY_OK:
        raise RuntimeError("cvxpy indisponível para CDaR")
    R = np.asarray(cenarios, float); T, k = R.shape
    # [FIX G7] Processo de riqueza multiplicativo (cumprod) em vez de aditivo (cumsum).
    # O drawdown é definido como queda percentual do pico da riqueza acumulada.
    # cumsum aproxima log(riqueza) apenas para retornos próximos de zero; para
    # janelas longas (T~1260) o erro é material. cumprod(1+R) é o processo correto,
    # consistente com max_drawdown() em inferencia.py (que usa cumprod).
    Rcum = np.cumprod(1 + R, axis=0)
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
                prob.solve(solver=cp.CLARABEL,
                           tol_gap_abs=_CVXPY_TOL, tol_gap_rel=_CVXPY_TOL,
                           verbose=False)
            elif solver_name == "ECOS":
                prob.solve(solver=cp.ECOS,
                           abstol=_CVXPY_TOL, reltol=_CVXPY_TOL,
                           verbose=False)
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

    Warm-start (melhoria vs. original):
        O dicionário `w_prev` (pesos do mês anterior, por estratégia) é incluído
        nos args e repassado como w0 para os otimizadores SLSQP. Para o 1º mês
        (w_prev=None) o fallback é 1/N. Reduz iterações ~50-70% nos meses seguintes
        pois as janelas expansivas mudam pouco entre rebalanceamentos consecutivos.
    """
    (i, data_rebal, dir_retornos_str, N, ALPHA, TETO_PESO, KAPPA_ORDENS,
     CVXPY_OK, REBAL, WARMUP_MESES, TRADING_DAYS, METODO_COV, MAR_MODO,
     DELTA, TAU, MAR_ESTRADA, VISAO_MOMENTUM_MESES, w_prev) = args

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

    periodos  = ret.index.to_period(REBAL)
    uperiodos = pd.Index(periodos.unique())

    fim_prev = ret.index[periodos == uperiodos[i - 1]][-1]
    janela   = ret.loc[:fim_prev]

    Jv  = janela.values
    S   = estimar_sigma(Jv, metodo=METODO_COV)
    mu  = janela.mean().values * TRADING_DAYS
    rf_j = rf.reindex(janela.index).dropna()
    rf_a = rf_j.mean() * TRADING_DAYS
    mar_d = float(rf_j.mean()) if MAR_MODO == "cdi" else 0.0

    # Extrai warm-start do mês anterior (None no 1º período → usa 1/N dentro das funções)
    _w0 = w_prev if w_prev is not None else {}

    alvos = {
        "EqualWeight":   w_equal(N),
        "InvVol":        w_inv_vol(S),
        "MinVar":        w_min_var(S, None,      w0=_w0.get("MinVar")),
        "MinVar_c10":    w_min_var(S, TETO_PESO, w0=_w0.get("MinVar_c10")),
        "MaxSharpe":     w_max_sharpe(mu, S, rf_a, None,      w0=_w0.get("MaxSharpe")),
        "MaxSharpe_c10": w_max_sharpe(mu, S, rf_a, TETO_PESO, w0=_w0.get("MaxSharpe_c10")),
    }

    for nome, n_k in KAPPA_ORDENS.items():
        alvos[nome] = w_max_kappa(Jv, n=n_k, mar=mar_d, teto=None, w0=_w0.get(nome))

    if CVXPY_OK:
        try:
            alvos["MinCVaR"] = w_min_cvar(Jv, ALPHA, None)
        except Exception as e:
            import warnings
            warnings.warn(f"[otimizar_mes_task] CVaR falhou (i={i}): {e}. Usando EqualWeight.")
            alvos["MinCVaR"] = w_equal(N)
        try:
            alvos["MinCDaR"] = w_min_cdar(Jv, ALPHA, None)
        except Exception as e:
            import warnings
            warnings.warn(f"[otimizar_mes_task] CDaR falhou (i={i}): {e}. Usando EqualWeight.")
            alvos["MinCDaR"] = w_equal(N)

    # --- Black-Litterman: prior clássico (Σ_LW) e prior downside (Σ_D) ---
    try:
        SigD = estrada_semicov(Jv, MAR_ESTRADA) * TRADING_DAYS
        # [FIX D1] Sigma clássico deve estar em escala ANUAL antes de entrar em
        # visoes_momentum (que produz Q anual) e em bl_posterior.
        # Anteriormente, S diário era passado → Omega ficava 252× menor que Q,
        # fazendo o posterior colapsar artificialmente para as visões de momentum.
        # Agora S_anual garante que Π, Q e Ω estão na mesma base temporal.
        S_anual = S * TRADING_DAYS
        wm   = np.repeat(1.0 / N, N)
        P, Q, Om = visoes_momentum(Jv, TAU, S_anual, TRADING_DAYS, VISAO_MOMENTUM_MESES)
        for nome, Sg, Pi in [("classico", S_anual, DELTA * S_anual @ wm),
                              ("downside", SigD,    DELTA * SigD    @ wm)]:
            mu_bl = bl_posterior(Sg, Pi, P, Q, Om, TAU)
            alvos[f"BL_{nome}"]     = w_max_sharpe(mu_bl, Sg, rf_a, None,
                                                    w0=_w0.get(f"BL_{nome}"))
            alvos[f"BL_{nome}_c10"] = w_max_sharpe(mu_bl, Sg, rf_a, TETO_PESO,
                                                    w0=_w0.get(f"BL_{nome}_c10"))
    except Exception as e:
        import warnings
        warnings.warn(f"[otimizar_mes_task] Black-Litterman falhou (i={i}): {e}. Usando EqualWeight.")
        for k in ("BL_classico", "BL_classico_c10", "BL_downside", "BL_downside_c10"):
            alvos[k] = w_equal(N)

    return i, data_rebal, alvos
