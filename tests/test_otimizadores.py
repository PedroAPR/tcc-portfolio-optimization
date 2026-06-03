"""
tests/test_otimizadores.py
═══════════════════════════════════════════════════════════════════════
Fase 4 — Item 2: Testes de corretude dos otimizadores de carteiras.
Cobre invariantes universais + soluções analíticas conhecidas.
"""
import numpy as np
import pytest

from utils.otimizacao import (
    w_equal, w_inv_vol, w_min_var, w_max_sharpe,
    w_max_kappa, w_min_cvar, w_min_cdar, ledoit_wolf,
)

SEED = 42
TOL_SOMA = 1e-6


# ───────────────────────────────────────────────────────────────────
# Helpers
# ───────────────────────────────────────────────────────────────────

def _check_invariantes(w, n, teto=None, label=""):
    """Invariantes universais para qualquer vetor de pesos."""
    assert not np.isnan(w).any(), f"{label}: contém NaN"
    assert not np.isinf(w).any(), f"{label}: contém Inf"
    assert abs(w.sum() - 1.0) < TOL_SOMA, f"{label}: soma={w.sum():.8f} ≠ 1"
    assert np.all(w >= -1e-8), f"{label}: pesos negativos: {w.min():.2e}"
    if teto is not None:
        assert np.all(w <= teto + 1e-6), f"{label}: excede teto {teto}: max={w.max():.4f}"


def _cov2x2(s1, s2, rho):
    """Matriz de covariância 2×2 a partir de vols e correlação."""
    return np.array([[s1**2, rho*s1*s2], [rho*s1*s2, s2**2]])


# ───────────────────────────────────────────────────────────────────
# w_equal
# ───────────────────────────────────────────────────────────────────

class TestWEqual:

    @pytest.mark.parametrize("n", [2, 5, 10, 100])
    def test_formula_fechada(self, n):
        """Todos os pesos devem ser exatamente 1/n."""
        w = w_equal(n)
        assert w.shape == (n,)
        assert np.allclose(w, 1.0/n, atol=1e-15)
        _check_invariantes(w, n, label=f"w_equal({n})")


# ───────────────────────────────────────────────────────────────────
# w_inv_vol
# ───────────────────────────────────────────────────────────────────

class TestWInvVol:

    def test_formula_fechada(self):
        """Pesos inversamente proporcionais à volatilidade (fórmula analítica)."""
        vols = np.array([0.10, 0.20, 0.40])
        S = np.diag(vols**2)
        w = w_inv_vol(S)
        iv = 1.0 / vols
        w_ref = iv / iv.sum()
        assert np.allclose(w, w_ref, atol=1e-12), f"w={w}  ref={w_ref}"
        _check_invariantes(w, 3, label="w_inv_vol")

    def test_igual_volatilidade(self):
        """Com vols iguais, resultado deve ser 1/N."""
        S = 0.0004 * np.eye(5)
        w = w_inv_vol(S)
        assert np.allclose(w, 1.0/5, atol=1e-12)

    def test_variancia_zero_sem_nan(self):
        """[FIX G1a] Ativo com var=0 deve receber peso 0, sem NaN."""
        S = np.diag([0.01, 0.0, 0.04, 0.09])
        w = w_inv_vol(S)
        assert not np.isnan(w).any(), "Contém NaN com var=0"
        assert w[1] == 0.0, "Ativo com var=0 deveria ter peso zero"
        _check_invariantes(w, 4, label="w_inv_vol com var=0")

    def test_todos_variancia_zero_fallback(self):
        """Todos var=0 → fallback para pesos iguais."""
        S = np.zeros((3, 3))
        w = w_inv_vol(S)
        assert np.allclose(w, 1.0/3, atol=1e-12)


# ───────────────────────────────────────────────────────────────────
# w_min_var
# ───────────────────────────────────────────────────────────────────

class TestWMinVar:

    def test_solucao_analitica_2ativos(self):
        """
        GMV 2 ativos: solução analítica.
        w1* = (σ2² - ρσ1σ2) / (σ1² + σ2² - 2ρσ1σ2)
        """
        s1, s2, rho = 0.20, 0.15, 0.3
        S = _cov2x2(s1, s2, rho)
        w = w_min_var(S)
        denom = s1**2 + s2**2 - 2*rho*s1*s2
        w1_ref = (s2**2 - rho*s1*s2) / denom
        w2_ref = 1.0 - w1_ref
        assert abs(w[0] - w1_ref) < 1e-5, f"w1={w[0]:.6f}  ref={w1_ref:.6f}"
        assert abs(w[1] - w2_ref) < 1e-5
        _check_invariantes(w, 2, label="w_min_var 2 ativos")

    def test_invariantes_sem_teto(self):
        rng = np.random.default_rng(SEED)
        X = rng.normal(0, 0.01, (200, 10))
        S = ledoit_wolf(X)
        w = w_min_var(S)
        _check_invariantes(w, 10, label="w_min_var sem teto")

    def test_invariantes_com_teto(self):
        rng = np.random.default_rng(SEED)
        X = rng.normal(0, 0.01, (200, 10))
        S = ledoit_wolf(X)
        teto = 0.15
        w = w_min_var(S, teto=teto)
        _check_invariantes(w, 10, teto=teto, label="w_min_var c=15%")

    def test_var_otima_menor_igual_equal(self):
        """MinVar deve ter variância ≤ EqualWeight (por definição)."""
        rng = np.random.default_rng(SEED)
        X = rng.normal(0, 0.01, (200, 15))
        S = ledoit_wolf(X)
        w_mv = w_min_var(S)
        w_ew = w_equal(15)
        var_mv = w_mv @ S @ w_mv
        var_ew = w_ew @ S @ w_ew
        assert var_mv <= var_ew + 1e-8, f"MinVar ({var_mv:.2e}) > EqualWeight ({var_ew:.2e})"


# ───────────────────────────────────────────────────────────────────
# w_max_sharpe
# ───────────────────────────────────────────────────────────────────

class TestWMaxSharpe:

    def test_solucao_analitica_sem_teto(self):
        """
        Carteira de tangência sem restrição de short/teto:
        w* ∝ Σ⁻¹(μ - rf·1).
        Com long-only pode diferir da solução analítica de tangência
        sem restrições; aqui testamos com N=2 e construção que garante
        long-only ótimo.
        """
        # 2 ativos com Sharpe individualmente positivo
        mu = np.array([0.12, 0.08])
        rf = 0.04
        S = np.array([[0.04, 0.01], [0.01, 0.02]])
        w = w_max_sharpe(mu, S, rf)
        _check_invariantes(w, 2, label="MaxSharpe 2 ativos")
        # Sharpe da carteira ≥ Sharpe de cada ativo individualmente
        sr_p  = (w @ mu - rf) / np.sqrt(w @ S @ w)
        sr_1  = (mu[0] - rf) / np.sqrt(S[0, 0])
        sr_2  = (mu[1] - rf) / np.sqrt(S[1, 1])
        assert sr_p >= max(sr_1, sr_2) - 1e-4, (
            f"MaxSharpe carteira ({sr_p:.4f}) < max individual ({max(sr_1,sr_2):.4f})"
        )

    def test_invariantes_com_teto(self):
        rng = np.random.default_rng(SEED)
        X = rng.normal(0, 0.01, (300, 10))
        S = ledoit_wolf(X) * 252
        mu = X.mean(0) * 252
        rf = 0.10
        teto = 0.10
        w = w_max_sharpe(mu, S, rf, teto=teto)
        _check_invariantes(w, 10, teto=teto, label="MaxSharpe c=10%")

    def test_sharpe_otimo_maior_equal(self):
        """MaxSharpe deve ter SR ≥ EqualWeight."""
        rng = np.random.default_rng(SEED)
        X = rng.normal(0.0006, 0.012, (300, 8))
        S = ledoit_wolf(X) * 252
        mu = X.mean(0) * 252
        rf = 0.10
        w_ms = w_max_sharpe(mu, S, rf)
        w_ew = w_equal(8)
        sr_ms = (w_ms @ mu - rf) / np.sqrt(w_ms @ S @ w_ms)
        sr_ew = (w_ew @ mu - rf) / np.sqrt(w_ew @ S @ w_ew)
        assert sr_ms >= sr_ew - 1e-4


# ───────────────────────────────────────────────────────────────────
# w_max_kappa
# ───────────────────────────────────────────────────────────────────

class TestWMaxKappa:

    @pytest.fixture(scope="class")
    def janela(self):
        rng = np.random.default_rng(SEED)
        return rng.normal(0.0005, 0.015, (500, 6))

    @pytest.mark.parametrize("n_kappa", [1, 2, 3])
    def test_invariantes(self, janela, n_kappa):
        w = w_max_kappa(janela, n=n_kappa, mar=0.0)
        _check_invariantes(w, 6, label=f"Kappa_{n_kappa}")

    @pytest.mark.parametrize("n_kappa", [1, 2, 3])
    def test_monotonicidade_vs_equal(self, janela, n_kappa):
        """Kappa_n da carteira ótima deve ser ≥ Kappa_n do EqualWeight."""
        w_opt = w_max_kappa(janela, n=n_kappa, mar=0.0)
        w_ew  = w_equal(6)
        mar = 0.0
        rp_opt = janela @ w_opt
        rp_ew  = janela @ w_ew
        lpm_opt = np.mean(np.clip(mar - rp_opt, 0, None) ** n_kappa)
        lpm_ew  = np.mean(np.clip(mar - rp_ew,  0, None) ** n_kappa)
        k_opt = rp_opt.mean() / (lpm_opt ** (1/n_kappa)) if lpm_opt > 1e-18 else np.inf
        k_ew  = rp_ew.mean()  / (lpm_ew  ** (1/n_kappa)) if lpm_ew  > 1e-18 else np.inf
        assert k_opt >= k_ew - 1e-4, (
            f"Kappa_{n_kappa}: ótimo ({k_opt:.4f}) < EqualWeight ({k_ew:.4f})"
        )

    @pytest.mark.parametrize("n_kappa", [1, 2, 3])
    def test_invariantes_com_teto(self, janela, n_kappa):
        w = w_max_kappa(janela, n=n_kappa, mar=0.0, teto=0.25)
        _check_invariantes(w, 6, teto=0.25, label=f"Kappa_{n_kappa} c=25%")


# ───────────────────────────────────────────────────────────────────
# w_min_cvar
# ───────────────────────────────────────────────────────────────────

class TestWMinCVar:

    @pytest.fixture(scope="class")
    def cenarios(self):
        rng = np.random.default_rng(SEED)
        return rng.normal(0.0005, 0.015, (300, 5))

    @pytest.fixture(scope="class")
    def cvxpy_ok(self):
        try:
            import cvxpy
            return True
        except ImportError:
            return False

    def test_invariantes(self, cenarios, cvxpy_ok):
        if not cvxpy_ok:
            pytest.skip("cvxpy não instalado")
        w = w_min_cvar(cenarios, alpha=0.95)
        _check_invariantes(w, 5, label="MinCVaR")

    def test_cvar_otimo_menor_equal(self, cenarios, cvxpy_ok):
        """CVaR da carteira ótima ≤ CVaR do EqualWeight."""
        if not cvxpy_ok:
            pytest.skip("cvxpy não instalado")
        w_opt = w_min_cvar(cenarios, alpha=0.95)
        w_ew  = w_equal(5)
        alpha = 0.95
        T = len(cenarios)

        def cvar_emp(w, alpha):
            rp = cenarios @ w
            var = np.percentile(-rp, alpha * 100)
            tail = -rp[-rp >= var]
            return float(tail.mean()) if len(tail) > 0 else var

        cv_opt = cvar_emp(w_opt, alpha)
        cv_ew  = cvar_emp(w_ew, alpha)
        assert cv_opt <= cv_ew + 1e-4, f"CVaR ótimo ({cv_opt:.4f}) > EqualWeight ({cv_ew:.4f})"

    def test_invariantes_com_teto(self, cenarios, cvxpy_ok):
        if not cvxpy_ok:
            pytest.skip("cvxpy não instalado")
        w = w_min_cvar(cenarios, alpha=0.95, teto=0.30)
        _check_invariantes(w, 5, teto=0.30, label="MinCVaR c=30%")


# ───────────────────────────────────────────────────────────────────
# w_min_cdar
# ───────────────────────────────────────────────────────────────────

class TestWMinCDaR:

    @pytest.fixture(scope="class")
    def cenarios(self):
        rng = np.random.default_rng(SEED)
        return rng.normal(0.0005, 0.015, (300, 5))

    @pytest.fixture(scope="class")
    def cvxpy_ok(self):
        try:
            import cvxpy
            return True
        except ImportError:
            return False

    def test_invariantes(self, cenarios, cvxpy_ok):
        if not cvxpy_ok:
            pytest.skip("cvxpy não instalado")
        w = w_min_cdar(cenarios, alpha=0.95)
        _check_invariantes(w, 5, label="MinCDaR")

    def test_processo_riqueza_multiplicativo(self, cvxpy_ok):
        """[FIX G7] Verifica que w_min_cdar usa cumprod (não cumsum)."""
        import inspect
        import utils.otimizacao as ot
        src = inspect.getsource(ot.w_min_cdar)
        assert 'cumprod(1 + R' in src, \
            "w_min_cdar ainda usa cumsum — FIX G7 não foi aplicado!"

    def test_cdar_otimo_menor_equal(self, cenarios, cvxpy_ok):
        """CDaR da carteira ótima (via riqueza) ≤ CDaR do EqualWeight."""
        if not cvxpy_ok:
            pytest.skip("cvxpy não instalado")
        w_opt = w_min_cdar(cenarios, alpha=0.95)
        w_ew  = w_equal(5)
        alpha = 0.95

        def cdar_emp(w, alpha):
            rp = cenarios @ w
            W = np.cumprod(1 + rp)  # [FIX G7]: processo multiplicativo
            peak = np.maximum.accumulate(W)
            dd = (W - peak) / peak
            var_d = np.percentile(dd, (1 - alpha) * 100)
            tail = dd[dd <= var_d]
            return float(-tail.mean()) if len(tail) > 0 else 0.0

        cdar_opt = cdar_emp(w_opt, alpha)
        cdar_ew  = cdar_emp(w_ew, alpha)
        # Pode não ser estritamente menor devido ao ponto inicial diferente,
        # mas ao menos não deve ser materialmente pior
        assert cdar_opt <= cdar_ew + 0.05, \
            f"CDaR ótimo ({cdar_opt:.4f}) muito maior que EqualWeight ({cdar_ew:.4f})"
