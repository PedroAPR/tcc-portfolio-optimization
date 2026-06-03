"""
tests/test_metricas.py
═══════════════════════════════════════════════════════════════════════
Fase 4 — Item 4: Testes de corretude das métricas em inferencia.py.
Cobre sharpe, sortino, cagr, max_drawdown contra cálculo manual,
e consistência de anualização.
"""
import numpy as np
import pandas as pd
import pytest

from utils.inferencia import (
    sharpe, sortino, cagr, max_drawdown,
    sharpe_de_excesso, sortino_de_excesso, _jk_memmel
)

TD = 252  # trading days


# ───────────────────────────────────────────────────────────────────
# Helpers
# ───────────────────────────────────────────────────────────────────

def _make_series(vals, rf=None):
    """Cria pd.Series de retornos e, opcionalmente, taxa rf."""
    r = pd.Series(vals, dtype=float)
    if rf is None:
        return r
    return r, pd.Series([rf] * len(vals), dtype=float)


# ───────────────────────────────────────────────────────────────────
# Sharpe
# ───────────────────────────────────────────────────────────────────

class TestSharpe:

    def test_calculo_manual(self):
        """
        Série conhecida: retornos = [0.01, 0.02, -0.01], rf = 0.
        SR = mean(exc) / std(exc, ddof=1) * sqrt(252)
        """
        vals = [0.01, 0.02, -0.01]
        r = pd.Series(vals)
        sr = sharpe(r, rf=0.0)
        exc = r - 0.0
        sr_ref = exc.mean() / exc.std() * np.sqrt(TD)
        assert abs(sr - sr_ref) < 1e-12

    def test_retorno_zero_sharpe_zero(self):
        """Série constante → SR = 0."""
        r = pd.Series([0.005] * 20)
        sr = sharpe(r, rf=0.005)
        assert sr == 0.0

    def test_anualiza_por_sqrt252(self):
        """Verificar que a anualização usa √252."""
        np.random.seed(42)
        r = pd.Series(np.random.normal(0.001, 0.01, 252))
        rf_val = 0.0003
        sr = sharpe(r, rf=rf_val)
        exc = r - rf_val
        sr_ref = exc.mean() / exc.std() * np.sqrt(252)
        assert abs(sr - sr_ref) < 1e-10

    def test_consistente_com_sharpe_de_excesso(self):
        """sharpe(r, rf) deve igualar sharpe_de_excesso(r - rf)."""
        np.random.seed(42)
        r = pd.Series(np.random.normal(0.001, 0.01, 100))
        rf = 0.0003
        s1 = sharpe(r, rf=rf)
        s2 = sharpe_de_excesso(r - rf)
        assert abs(s1 - s2) < 1e-10

    def test_rf_none_usa_fallback(self):
        """rf=None deve usar fallback_rf=0.000369 sem crash."""
        r = pd.Series(np.random.normal(0.001, 0.01, 100))
        sr = sharpe(r, rf=None)
        assert not np.isnan(sr)

    def test_rf_series(self):
        """rf como pd.Series com DatetimeIndex deve funcionar."""
        idx = pd.date_range("2020-01-01", periods=50, freq="B")
        r  = pd.Series(np.random.normal(0.001, 0.01, 50), index=idx)
        rf = pd.Series([0.0003] * 50, index=idx)
        sr = sharpe(r, rf=rf)
        assert not np.isnan(sr)


# ───────────────────────────────────────────────────────────────────
# Sortino
# ───────────────────────────────────────────────────────────────────

class TestSortino:

    def test_calculo_manual(self):
        """
        Sortino = mean(exc) / sqrt(mean(clip(exc, upper=0)²)) * sqrt(252).
        """
        vals = [0.02, -0.01, 0.03, -0.02, 0.01]
        r  = pd.Series(vals)
        rf = 0.005
        so = sortino(r, rf=rf)
        exc = r - rf
        dd = np.sqrt(np.mean(np.clip(exc, None, 0) ** 2))
        so_ref = (exc.mean() / dd) * np.sqrt(TD)
        assert abs(so - so_ref) < 1e-12

    def test_sem_retornos_downside_retorna_inf(self):
        """Sem retornos abaixo do MAR → desvio downside = 0 → Sortino = inf."""
        r = pd.Series([0.01, 0.02, 0.03])
        so = sortino(r, rf=0.005)
        assert so == np.inf

    def test_consistente_com_sortino_de_excesso(self):
        np.random.seed(42)
        r  = pd.Series(np.random.normal(0.001, 0.01, 100))
        rf = 0.0003
        s1 = sortino(r, rf=rf)
        s2 = sortino_de_excesso(r - rf)
        assert abs(s1 - s2) < 1e-10


# ───────────────────────────────────────────────────────────────────
# CAGR
# ───────────────────────────────────────────────────────────────────

class TestCAGR:

    def test_calculo_manual(self):
        """CAGR = (produto(1+r))^(252/n) - 1."""
        r = pd.Series([0.01, -0.005, 0.02, 0.01])
        n = len(r)
        c = cagr(r)
        c_ref = float((1 + r).prod() ** (TD / n) - 1)
        assert abs(c - c_ref) < 1e-12

    def test_serie_vazia(self):
        """Série vazia deve retornar 0."""
        assert cagr(pd.Series([], dtype=float)) == 0.0

    def test_retorno_zero(self):
        """Série toda zero → CAGR = 0."""
        r = pd.Series([0.0] * 252)
        assert abs(cagr(r)) < 1e-14

    def test_retorno_constante(self):
        """Retorno diário constante r → CAGR = (1+r)^252 - 1."""
        r_d = 0.001
        r = pd.Series([r_d] * 252)
        c = cagr(r)
        c_ref = (1 + r_d)**252 - 1
        assert abs(c - c_ref) < 1e-10


# ───────────────────────────────────────────────────────────────────
# Max Drawdown
# ───────────────────────────────────────────────────────────────────

class TestMaxDrawdown:

    def test_calculo_manual(self):
        """
        Curva de riqueza conhecida:
        W = [1.0, 1.1, 1.05, 0.9, 0.95]
        Peak = [1.0, 1.1, 1.1, 1.1, 1.1]
        DD = [(1-1)/1, (1.1-1.1)/1.1, (1.05-1.1)/1.1, (0.9-1.1)/1.1, (0.95-1.1)/1.1]
             = [0, 0, -0.0455, -0.1818, -0.1364]
        MaxDD = -0.1818
        """
        # Constrói retornos que produzem essa curva
        r = pd.Series([0.10, -0.10/1.1, 0.9/1.05 - 1, 0.95/0.9 - 1])
        # Curva: 1 → 1.1 → 1.0 → 0.9 → 0.855 (aproximado)
        # Usa série de retornos direta
        r2 = pd.Series([0.10, -4.545/100, -14.286/100, 5.556/100])
        W = (1 + r2).cumprod()
        peak = W.cummax()
        dd_ref = float(((W - peak) / peak).min())
        md = max_drawdown(r2)
        assert abs(md - dd_ref) < 1e-8

    def test_serie_crescente_sem_drawdown(self):
        """Série sempre crescente → MaxDD = 0."""
        r = pd.Series([0.001, 0.002, 0.003, 0.001])
        md = max_drawdown(r)
        assert md >= -1e-12, f"MaxDD de série crescente deve ser ≈ 0, obtido {md}"

    def test_negativo_ou_zero(self):
        """MaxDD deve ser ≤ 0."""
        np.random.seed(42)
        r = pd.Series(np.random.normal(0.001, 0.02, 500))
        md = max_drawdown(r)
        assert md <= 0.0

    def test_queda_total(self):
        """Queda de 50% → MaxDD ≈ -0.5."""
        r = pd.Series([0.0, 0.0, -0.5, 0.0])
        md = max_drawdown(r)
        assert abs(md - (-0.5)) < 1e-10

    def test_serie_vazia(self):
        assert max_drawdown(pd.Series([], dtype=float)) == 0.0


# ───────────────────────────────────────────────────────────────────
# _jk_memmel
# ───────────────────────────────────────────────────────────────────

class TestJkMemmel:

    def test_serie_constante_retorna_sem_nan(self):
        """[FIX G1b] Série constante (std(ddof=1)==0) → (z=0, p=1.0) sem NaN.

        Importante: re-importa o módulo para garantir que a versão corrigida
        (com proteção std==0) está em uso, não uma versão em cache.
        """
        import importlib
        import utils.inferencia as inf_mod
        importlib.reload(inf_mod)
        _jk_local = inf_mod._jk_memmel

        exc_a = pd.Series([0.001] * 10)  # std(ddof=1) == 0
        exc_b = pd.Series([0.001, -0.002, 0.003, -0.001, 0.002,
                           0.001, -0.001, 0.002, 0.0, 0.001])
        # std(ddof=1) pode não ser exatamente 0 em float64 (pode ser ~1e-19)
        # mas é menor que a tolerância 1e-14 usada no guard de _jk_memmel
        assert exc_a.std(ddof=1) <= 1e-14, "exc_a deveria ter std~0"
        z, p = _jk_local(exc_a, exc_b)
        assert not np.isnan(z), "z não deve ser NaN"
        assert not np.isnan(p), "p não deve ser NaN"
        assert z == 0.0, f"z={z} esperado 0.0"
        assert p == 1.0, f"p={p} esperado 1.0"

    def test_iguais_z_zero(self):
        """Séries idênticas → z ≈ 0, p ≈ 1."""
        np.random.seed(42)
        exc = pd.Series(np.random.normal(0.001, 0.01, 100))
        z, p = _jk_memmel(exc, exc)
        assert abs(z) < 1e-10
        assert abs(p - 1.0) < 1e-10

    def test_pvalor_entre_0_e_1(self):
        """p-valor sempre em [0, 1]."""
        np.random.seed(42)
        exc_a = pd.Series(np.random.normal(0.002, 0.01, 200))
        exc_b = pd.Series(np.random.normal(0.001, 0.01, 200))
        z, p = _jk_memmel(exc_a, exc_b)
        assert 0.0 <= p <= 1.0

    def test_bicaudal(self):
        """Teste bicaudal: p = 2*(1 - Phi(|z|)), então p ≤ 1 sempre."""
        from scipy import stats
        np.random.seed(42)
        exc_a = pd.Series(np.random.normal(0.003, 0.01, 300))
        exc_b = pd.Series(np.random.normal(0.001, 0.01, 300))
        z, p = _jk_memmel(exc_a, exc_b)
        p_ref = 2 * (1 - stats.norm.cdf(abs(z)))
        assert abs(p - p_ref) < 1e-10
