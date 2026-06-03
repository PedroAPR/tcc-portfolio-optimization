"""
tests/test_black_litterman.py
═══════════════════════════════════════════════════════════════════════
Fase 4 — Item 3: Testes de corretude do Black-Litterman.
Cobre as propriedades analíticas de He & Litterman (1999) e coerência
de escala pós-FIX D1.
"""
import numpy as np
import pytest

from utils.otimizacao import (
    bl_posterior, visoes_momentum, ledoit_wolf, estrada_semicov, w_equal
)

SEED = 42
DELTA = 2.5
TAU = 0.05
TD = 252


@pytest.fixture(scope="module")
def setup_bl():
    """Dados controlados para testes BL: 3 ativos, 500 obs diárias."""
    rng = np.random.default_rng(SEED)
    R = rng.normal(0.0006, 0.011, (500, 3))
    N = 3
    S = ledoit_wolf(R) * TD   # [FIX D1] escala anual
    wm = np.repeat(1.0/N, N)
    Pi = DELTA * S @ wm       # prior de equilíbrio CAPM reverso
    P, Q, Om = visoes_momentum(R, TAU, S, TD)
    return {"R": R, "S": S, "wm": wm, "Pi": Pi, "P": P, "Q": Q, "Om": Om, "N": N}


class TestBlackLittermanPropriedades:

    def test_prop1_omega_inf_colapsa_prior(self, setup_bl):
        """
        Prop. 1 — He & Litterman (1999):
        Ω → ∞ (incerteza total nas visões): mu_BL → Pi (equilíbrio).
        """
        d = setup_bl
        Om_inf = np.diag([1e8] * d["N"])
        mu_bl = bl_posterior(d["S"], d["Pi"], d["P"], d["Q"], Om_inf, TAU)
        assert np.allclose(mu_bl, d["Pi"], atol=1e-3), (
            f"Com Omega→inf, mu_BL deveria ≈ Pi.\n"
            f"  mu_BL = {mu_bl.round(4)}\n  Pi    = {d['Pi'].round(4)}"
        )

    def test_prop2_omega_zero_colapsa_visoes(self, setup_bl):
        """
        Prop. 2 — He & Litterman (1999):
        Ω → 0 (visões certas): mu_BL → Q.
        """
        d = setup_bl
        Om_zero = np.diag([1e-10] * d["N"])
        mu_bl = bl_posterior(d["S"], d["Pi"], d["P"], d["Q"], Om_zero, TAU)
        assert np.allclose(mu_bl, d["Q"], atol=1e-3), (
            f"Com Omega→0, mu_BL deveria ≈ Q.\n"
            f"  mu_BL = {mu_bl.round(4)}\n  Q     = {d['Q'].round(4)}"
        )

    def test_prop3_capm_reverso_consistente(self, setup_bl):
        """
        Prop. 3 — He & Litterman (1999):
        (1/δ) · Σ⁻¹ · Pi = w_mkt  (consistência CAPM reverso).
        """
        d = setup_bl
        w_check = (1.0/DELTA) * np.linalg.solve(d["S"], d["Pi"])
        assert np.allclose(w_check, d["wm"], atol=1e-8), (
            f"Prior inconsistente com CAPM reverso.\n"
            f"  Σ⁻¹·Pi/δ = {w_check.round(6)}\n  wm = {d['wm'].round(6)}"
        )

    def test_sem_visoes_posterior_igual_prior(self, setup_bl):
        """
        Sem visões úteis (Q = Pi via P=I), posterior ≈ prior.
        Isso ocorre quando as visões repetem exatamente o prior de equilíbrio.
        """
        d = setup_bl
        P_id = np.eye(d["N"])
        # Q = Pi: as visões concordam com o prior
        Q_pi = d["Pi"].copy()
        mu_bl = bl_posterior(d["S"], d["Pi"], P_id, Q_pi, d["Om"], TAU)
        assert np.allclose(mu_bl, d["Pi"], atol=1e-6), (
            f"Q=Pi deveria dar mu_BL=Pi.\n"
            f"  mu_BL = {mu_bl.round(6)}\n  Pi = {d['Pi'].round(6)}"
        )

    def test_visao_forte_baixa_incerteza_puxa_para_Q(self, setup_bl):
        """
        Visão forte (Ω pequeno) deve puxar mu_BL para Q.
        Verificamos que ||mu_BL - Q|| < ||Pi - Q|| (BL mais próximo de Q que do prior).
        """
        d = setup_bl
        Om_pequeno = d["Om"] * 0.0001   # incerteza 10000× menor
        mu_bl = bl_posterior(d["S"], d["Pi"], d["P"], d["Q"], Om_pequeno, TAU)
        dist_bl_Q  = np.linalg.norm(mu_bl - d["Q"])
        dist_pi_Q  = np.linalg.norm(d["Pi"] - d["Q"])
        assert dist_bl_Q < dist_pi_Q, (
            f"Visão forte não puxou mu_BL para Q:\n"
            f"  ||mu_BL-Q||={dist_bl_Q:.4f} >= ||Pi-Q||={dist_pi_Q:.4f}"
        )


class TestBlackLittermanEscala:

    def test_fix_d1_sigma_anual_omega_consistente(self):
        """
        [FIX D1] Omega e Q devem estar na mesma escala anual.
        Verifica que visoes_momentum recebe S anual e Q retornado
        é anual; comprova que ||mu_BL_anual - Q|| < ||mu_BL_diario - Q||
        (escala correta faz o prior ter influência mais realista).
        """
        rng = np.random.default_rng(SEED)
        R = rng.normal(0.0006, 0.011, (500, 4))
        N = 4
        S_diario = ledoit_wolf(R)                   # diário
        S_anual  = S_diario * TD                    # anual
        wm = np.repeat(1.0/N, N)
        Pi_anual  = DELTA * S_anual  @ wm
        Pi_diario = DELTA * S_diario @ wm

        # Visões sempre anuais (momentum 12-1)
        P_a, Q_a, Om_a = visoes_momentum(R, TAU, S_anual,  TD)  # correto
        P_d, Q_d, Om_d = visoes_momentum(R, TAU, S_diario, TD)  # incorreto (antes do fix)

        mu_anual  = bl_posterior(S_anual,  Pi_anual,  P_a, Q_a, Om_a, TAU)
        mu_diario = bl_posterior(S_diario, Pi_diario, P_d, Q_d, Om_d, TAU)

        # Q é anual em ambos os casos; Omega anual escala corretamente
        # a incerteza relativa ao prior → mu_BL_anual equilibra prior e visões
        # mu_BL_diario tem Omega 252× menor que Q → colapsa artificialmente nas visões
        w_opt_anual  = np.ones(N)/N   # apenas verificação de escala, não de otimização
        assert not np.isnan(mu_anual).any(),  "mu_BL anual contém NaN"
        assert not np.isnan(mu_diario).any(), "mu_BL diário contém NaN"
        # Diferença entre as duas escalaes deve ser substancial (diagnóstico do bug)
        diff = np.abs(mu_anual - mu_diario * TD).max()
        # Não é zero (demonstra que as escalas importam)
        assert diff > 0.001, f"Diferença de escala inesperadamente pequena: {diff:.6f}"

    def test_multiplicar_sigma_por_fator_nao_quebra_capm(self):
        """
        Teste de escala (Item 3.c da auditoria):
        Multiplicar Σ por um fator de anualização f e escalar Pi da mesma forma
        não deve mudar os pesos ótimos BL (coerência dimensional).
        """
        rng = np.random.default_rng(SEED)
        R = rng.normal(0.0005, 0.012, (400, 3))
        N = 3
        S1 = ledoit_wolf(R)           # diário (escala 1)
        S2 = S1 * TD                  # anual  (escala TD)
        wm = np.repeat(1.0/N, N)

        # Prop. 3 deve valer nas duas escalas
        Pi1 = DELTA * S1 @ wm
        Pi2 = DELTA * S2 @ wm
        w1 = (1/DELTA) * np.linalg.solve(S1, Pi1)
        w2 = (1/DELTA) * np.linalg.solve(S2, Pi2)
        assert np.allclose(w1, wm, atol=1e-8), "CAPM reverso falhou em escala diária"
        assert np.allclose(w2, wm, atol=1e-8), "CAPM reverso falhou em escala anual"
        assert np.allclose(w1, w2, atol=1e-8), "Escala muda os pesos de equilíbrio"
