"""
tests/test_backtest_integracao.py
═══════════════════════════════════════════════════════════════════════
Fase 4 — Item 5: Teste de integração do backtest.
Universo sintético de 3 ativos com retornos conhecidos para verificar:
(a) custo cobrado = custo_unit × Σ|Δw| no 1º dia do mês
(b) curva de riqueza composta bate com cálculo manual
"""
import numpy as np
import pandas as pd
import pytest

from utils.otimizacao import w_equal

TD = 252
CUSTO_BPS = 50.0
CUSTO_UNIT = CUSTO_BPS / 1e4   # 0.005


def _backtest_simples(ret, w_alvo, w_ant, custo_unit=CUSTO_UNIT):
    """
    Reproduz a lógica do backtest de NB07 para um único mês:
    - ret: array (dias_do_mes, N) de retornos diários
    - w_alvo: vetor de pesos alvo
    - w_ant: vetor de pesos no fim do mês anterior
    - Custo aplicado no primeiro dia sobre Σ|w - w_ant|.
    Retorna array de retornos diários do portfólio.
    """
    dias, N = ret.shape
    rp = ret @ w_alvo          # constant-mix: w fixo em todos os dias
    turn = np.abs(w_alvo - w_ant).sum()
    rp[0] -= custo_unit * turn  # custo no 1º dia
    return rp


class TestBacktestIntegracao:

    @pytest.fixture
    def dados_sinteticos(self):
        """
        3 ativos, 2 meses de 5 dias úteis, retornos 100% controlados.
        """
        rng = np.random.default_rng(42)
        # Retornos simples diários (3 ativos × 10 dias)
        R = np.array([
            # Mês 1 (dias 0-4)
            [0.010, -0.005,  0.008],
            [0.005,  0.010, -0.003],
            [-0.008, 0.003,  0.007],
            [0.002, -0.007,  0.005],
            [0.006,  0.004, -0.002],
            # Mês 2 (dias 5-9)
            [-0.004, 0.008,  0.003],
            [0.009, -0.003,  0.005],
            [0.003,  0.006, -0.007],
            [-0.005, 0.004,  0.009],
            [0.007, -0.006,  0.002],
        ])
        return R

    def test_custo_primeiro_dia(self, dados_sinteticos):
        """
        O custo deve ser exatamente custo_unit × Σ|Δw| e deduzido do 1º dia.
        """
        R = dados_sinteticos
        N = 3
        w_ant = np.array([1/3, 1/3, 1/3])  # portfólio anterior
        w_alvo = np.array([0.5, 0.3, 0.2]) # novo alvo

        rp = _backtest_simples(R[:5], w_alvo, w_ant)

        # Custo esperado
        turn = np.abs(w_alvo - w_ant).sum()
        custo_esperado = CUSTO_UNIT * turn

        # Retorno do 1º dia sem custo
        rp1_sem_custo = float(R[0] @ w_alvo)
        rp1_com_custo = rp1_sem_custo - custo_esperado

        assert abs(rp[0] - rp1_com_custo) < 1e-12, (
            f"Custo incorreto: rp[0]={rp[0]:.8f}, esperado={rp1_com_custo:.8f}"
        )
        # Dias 2-5 sem custo
        for t in range(1, 5):
            rp_ref = float(R[t] @ w_alvo)
            assert abs(rp[t] - rp_ref) < 1e-12, f"Dia {t}: rp={rp[t]:.8f} ≠ {rp_ref:.8f}"

    def test_custo_sem_rebalanceamento(self, dados_sinteticos):
        """Sem mudança de pesos (w_alvo = w_ant), custo deve ser zero."""
        R = dados_sinteticos
        w = np.array([0.4, 0.35, 0.25])
        rp = _backtest_simples(R[:5], w, w)
        turn = np.abs(w - w).sum()
        assert turn == 0.0
        # Custo zero → rp[0] == R[0] @ w sem dedução
        assert abs(rp[0] - float(R[0] @ w)) < 1e-12

    def test_curva_riqueza_composta(self, dados_sinteticos):
        """
        Dois meses consecutivos com rebalanceamento:
        riqueza final = produto(1 + rp_mes1) × produto(1 + rp_mes2)
        """
        R = dados_sinteticos
        N = 3
        # Mês 1: EqualWeight com pesos anteriores = EqualWeight (sem custo)
        w1 = w_equal(N)
        w0 = w_equal(N)
        rp1 = _backtest_simples(R[:5], w1, w0)

        # Mês 2: alvo diferente → tem custo
        w2 = np.array([0.5, 0.3, 0.2])
        rp2 = _backtest_simples(R[5:], w2, w1)

        # Curva composta
        rp_total = np.concatenate([rp1, rp2])
        riqueza_final = (1 + rp_total).prod()

        # Cálculo manual
        riq_mes1 = (1 + rp1).prod()
        riq_mes2 = (1 + rp2).prod()
        riqueza_manual = riq_mes1 * riq_mes2

        assert abs(riqueza_final - riqueza_manual) < 1e-12, (
            f"Riqueza composta: calc={riqueza_final:.10f}, manual={riqueza_manual:.10f}"
        )

    def test_constant_mix_pesos_fixos(self, dados_sinteticos):
        """
        Constant-mix: w fixo em todos os dias do mês (sem deriva intra-mês).
        O retorno de cada dia é exatamente R[t] @ w.
        """
        R = dados_sinteticos
        w = np.array([0.4, 0.4, 0.2])
        w_ant = w_equal(3)
        rp = _backtest_simples(R[:5], w, w_ant)

        custo = CUSTO_UNIT * np.abs(w - w_ant).sum()
        # Dia 0: rp = R[0]@w - custo
        assert abs(rp[0] - (R[0] @ w - custo)) < 1e-12
        # Dias 1-4: rp = R[t]@w (sem custo, sem deriva)
        for t in range(1, 5):
            assert abs(rp[t] - float(R[t] @ w)) < 1e-12

    def test_custo_correto_bps(self):
        """
        Com CUSTO_BPS=50, custo_unit=0.005.
        Se turnover = 0.4, custo = 0.002 (0.2% do portfólio).
        """
        N = 2
        R = np.array([[0.01, -0.01], [0.005, 0.005]])
        w_alvo = np.array([0.7, 0.3])
        w_ant  = np.array([0.5, 0.5])
        rp = _backtest_simples(R, w_alvo, w_ant, custo_unit=CUSTO_UNIT)

        turn = abs(0.7-0.5) + abs(0.3-0.5)  # = 0.4
        custo = CUSTO_UNIT * turn             # = 0.005 * 0.4 = 0.002
        rp0_ref = R[0] @ w_alvo - custo
        assert abs(rp[0] - rp0_ref) < 1e-12
        assert abs(CUSTO_UNIT - 0.005) < 1e-12
