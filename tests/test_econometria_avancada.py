"""
tests/test_econometria_avancada.py
═══════════════════════════════════════════════════════════════════════
Testes econométricos avançados baseados no Plano de Testes Ampliado.
Cobre: Deflated Sharpe Ratio (DSR), CAPM com erros HAC (Newey-West),
Jobson-Korkie/Memmel e Bootstrap não-paramétrico.
"""
import numpy as np
import pandas as pd
import pytest
import statsmodels.api as sm

from utils.inferencia import (
    calcular_dsr, deflated_sharpe_ratio,
    _wald_spanning, _jk_memmel,
    lw_bootstrap_sharpe, lw_bootstrap_sortino,
    matriz_correlacao_significancia,
    regressao_multifatorial,
    spanning_multivariado
)

SEED = 42


# ───────────────────────────────────────────────────────────────────
# 1. Testes do Deflated Sharpe Ratio (DSR)
# ───────────────────────────────────────────────────────────────────

class TestDeflatedSharpeRatio:

    def test_dsr_propriedades_fundamentais(self):
        """
        Valida que o DSR atende a propriedades estatísticas esperadas:
        - Monotonicidade com T: DSR aumenta com maior tamanho amostral T (ceteris paribus).
        - Sensibilidade com N: DSR diminui à medida que o número de testes N aumenta.
        """
        # Parâmetros base
        sharpe_best = 1.5
        sharpes = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.5]
        skew = -0.2
        kurt = 3.5  # curtose real ( Fisher + 3 )
        
        # 1. Monotonicidade com T
        dsr_t100 = calcular_dsr(sharpe_best, sharpes, T=100, skew=skew, kurt=kurt, N=7)
        dsr_t1000 = calcular_dsr(sharpe_best, sharpes, T=1000, skew=skew, kurt=kurt, N=7)
        assert dsr_t1000 > dsr_t100, f"DSR(T=1000)={dsr_t1000:.4f} <= DSR(T=100)={dsr_t100:.4f}"
        
        # 2. Sensibilidade com N (número de tentativas)
        dsr_n7 = calcular_dsr(sharpe_best, sharpes, T=500, skew=skew, kurt=kurt, N=7)
        # Se adicionarmos muitos testes ruins, a variância dos Sharpe Ratios pode mudar.
        # Mantendo std_sr constante mas alterando N diretamente na fórmula:
        dsr_n100 = calcular_dsr(sharpe_best, sharpes, T=500, skew=skew, kurt=kurt, N=100)
        assert dsr_n100 < dsr_n7, f"DSR(N=100)={dsr_n100:.4f} >= DSR(N=7)={dsr_n7:.4f}"

    def test_dsr_sensibilidade_cauda(self):
        """
        Valida que o DSR penaliza distribuições com assimetria negativa e curtose alta.
        """
        sharpe_best = 1.0
        sharpes = [0.1, 0.2, 0.3, 0.4, 0.5, 1.0]
        T = 252
        N = 6
        
        # Caso 1: Retornos normais simétricos (skew=0, kurt=3)
        dsr_normal = calcular_dsr(sharpe_best, sharpes, T, skew=0.0, kurt=3.0, N=N)
        
        # Caso 2: Cauda pesada e assimetria negativa (skew=-1.0, kurt=6.0)
        dsr_ruim = calcular_dsr(sharpe_best, sharpes, T, skew=-1.0, kurt=6.0, N=N)
        
        # Caudas piores aumentam a variância do Sharpe estimado, reduzindo o z-score
        # e, consequentemente, o DSR.
        assert dsr_ruim < dsr_normal, f"DSR cauda pesada ({dsr_ruim:.4f}) >= DSR normal ({dsr_normal:.4f})"

    def test_dsr_retornos_reais_mock(self):
        """
        Testa o cálculo do DSR a partir de uma série temporal de retornos.
        """
        rng = np.random.default_rng(SEED)
        # Melhor estratégia: Sharpe diário ~ 0.08 / 0.15 * sqrt(252) ~ 1.5
        ret_best = rng.normal(0.001, 0.012, 500)
        all_sharpes = [0.1, 0.3, 0.5, 0.8, 1.2, 1.45]
        
        dsr = deflated_sharpe_ratio(ret_best, all_sharpes)
        assert 0.0 <= dsr <= 1.0, f"DSR={dsr} fora do intervalo [0, 1]"


# ───────────────────────────────────────────────────────────────────
# 2. Testes de Regressão CAPM com Erros HAC (Newey-West)
# ───────────────────────────────────────────────────────────────────

class TestCAPMHAC:

    def test_wald_spanning_hac(self):
        """
        Verifica que _wald_spanning executa OLS com covariância robusta HAC
        e calcula a estatística de Wald sem levantar erros numéricos.
        """
        rng = np.random.default_rng(SEED)
        T = 200
        # Gera retornos excedentes de uma carteira com alfa = 0.5% a.a. e beta = 0.8
        ret_m = rng.normal(0.0003, 0.015, T)
        residuos = rng.normal(0.0, 0.008, T)
        ret_p = 0.00002 + 0.8 * ret_m + residuos
        
        # Adiciona constante para regressão
        X_const = sm.add_constant(ret_m)
        
        res, stat, p_val = _wald_spanning(ret_p, X_const, maxlags=3)
        
        # Validações
        assert res is not None
        assert res.cov_type == "HAC"
        assert not np.isnan(stat)
        assert 0.0 <= p_val <= 1.0
        assert len(res.params) == 2
        # O beta estimado deve estar próximo de 0.8
        assert abs(res.params[1] - 0.8) < 0.15


# ───────────────────────────────────────────────────────────────────
# 3. Testes Comparativos Par a Par (Jobson-Korkie e Bootstrap)
# ───────────────────────────────────────────────────────────────────

class TestComparativosEconometricos:

    def test_comparacao_sharpe_bootstrap(self):
        """
        Verifica que lw_bootstrap_sharpe roda sem erros, é determinístico dado o seed,
        e diferencia séries com Sharpe populacionalmente distintos.
        """
        rng = np.random.default_rng(SEED)
        T = 150
        # Série 1: Sharpe alto
        r1 = rng.normal(0.002, 0.010, T)
        # Série 2: Sharpe baixo
        r2 = rng.normal(-0.001, 0.015, T)
        
        diff_anual, p_val1 = lw_bootstrap_sharpe(r1, r2, bloco=5, reps=200, seed=SEED)
        _, p_val2 = lw_bootstrap_sharpe(r1, r2, bloco=5, reps=200, seed=SEED)
        
        # Reprodutibilidade
        assert p_val1 == p_val2, "lw_bootstrap_sharpe não determinístico com mesma seed"
        assert 0.0 <= p_val1 <= 1.0
        assert diff_anual > 0.0  # Sharpe de r1 deve ser maior que r2

    def test_comparacao_sortino_bootstrap(self):
        """
        Verifica que lw_bootstrap_sortino computa a diferença de Sortino sob bootstrap.
        """
        rng = np.random.default_rng(SEED)
        T = 150
        r1 = rng.normal(0.001, 0.012, T)
        r2 = rng.normal(0.000, 0.012, T)
        
        diff_anual, p_val = lw_bootstrap_sortino(r1, r2, rf=0.0, bloco=5, reps=200, seed=SEED)
        assert 0.0 <= p_val <= 1.0
        assert not np.isnan(diff_anual)


# ───────────────────────────────────────────────────────────────────
# 4. Testes de Matriz de Correlação e Significância
# ───────────────────────────────────────────────────────────────────

class TestMatrizCorrelacaoSignificancia:

    def test_matriz_propriedades(self):
        """
        Verifica que a matriz de correlação e p-valores é calculada corretamente,
        mantendo simetria física e p-valores na diagonal nulos.
        """
        rng = np.random.default_rng(SEED)
        T = 100
        x1 = rng.normal(0.0005, 0.01, T)
        # x2 altamente correlacionado com x1
        x2 = 0.8 * x1 + rng.normal(0.0, 0.003, T)
        # x3 independente
        x3 = rng.normal(-0.0002, 0.015, T)
        
        df = pd.DataFrame({"x1": x1, "x2": x2, "x3": x3})
        corr, p_vals = matriz_correlacao_significancia(df)
        
        # 1. Simetria
        assert np.allclose(corr.values, corr.values.T)
        assert np.allclose(p_vals.values, p_vals.values.T)
        
        # 2. Valores na diagonal devem ser nulos para p-valores
        assert np.allclose(np.diag(p_vals.values), 0.0)
        
        # 3. p-valor entre x1 e x2 deve ser altamente significativo (próximo de zero)
        assert p_vals.loc["x1", "x2"] < 0.001
        
        # 4. p-valor entre x1 e x3 deve ser não significativo (> 0.05)
        assert p_vals.loc["x1", "x3"] > 0.10


# ───────────────────────────────────────────────────────────────────
# 5. Testes de Regressão Multifatorial HAC (Newey-West)
# ───────────────────────────────────────────────────────────────────

class TestRegressaoMultifatorial:

    def test_decomposicao_fatores(self):
        """
        Verifica se a regressão multifatorial estima corretamente os Betas
        e retorna as estatísticas do modelo sob dependência linear simulada.
        """
        rng = np.random.default_rng(SEED)
        T = 200
        # Fatores simulados
        mkt = rng.normal(0.0003, 0.015, T)
        smb = rng.normal(0.0001, 0.008, T)
        hml = rng.normal(-0.0001, 0.010, T)
        df_fat = pd.DataFrame({"MKT": mkt, "SMB": smb, "HML": hml})
        
        # Ativo simulado com Betas: MKT=0.8, SMB=0.4, HML=-0.2 e alfa=0.0001
        ret_p = pd.Series(0.0001 + 0.8 * mkt + 0.4 * smb - 0.2 * hml + rng.normal(0.0, 0.002, T))
        
        res = regressao_multifatorial(ret_p, df_fat, maxlags=3)
        
        assert "const" in res["params"]
        assert "MKT" in res["params"]
        assert "SMB" in res["params"]
        assert "HML" in res["params"]
        
        # Validação de coeficientes estimadores
        assert abs(res["params"]["MKT"]["coef"] - 0.8) < 0.05
        assert abs(res["params"]["SMB"]["coef"] - 0.4) < 0.05
        assert abs(res["params"]["HML"]["coef"] - (-0.2)) < 0.05
        assert res["r2"] > 0.80
        assert res["nobs"] == T


# ───────────────────────────────────────────────────────────────────
# 6. Testes do Spanning Multivariado (Huberman & Kandel, 1987)
# ───────────────────────────────────────────────────────────────────

class TestSpanningMultivariado:

    def test_spanning_ativos_teste(self):
        """
        Valida que o teste multivariado de Spanning responde corretamente:
        - Não deve rejeitar H0 (spanning) se os ativos teste são meras combinações lineares dos benchmarks.
        - Deve rejeitar H0 (spanning) se os ativos teste possuem alfa (performance fora da fronteira).
        """
        rng = np.random.default_rng(SEED)
        T = 300
        # 2 benchmarks
        b1 = rng.normal(0.0004, 0.012, T)
        b2 = rng.normal(0.0002, 0.015, T)
        df_bench = pd.DataFrame({"B1": b1, "B2": b2})
        
        # Caso A: Spanning é verdadeiro (ativos teste são combinações dos benchmarks + ruído)
        t1 = 0.6 * b1 + 0.4 * b2 + rng.normal(0.0, 0.001, T)
        t2 = 0.2 * b1 + 0.8 * b2 + rng.normal(0.0, 0.001, T)
        df_teste_true = pd.DataFrame({"T1": t1, "T2": t2})
        
        _, p_val_true = spanning_multivariado(df_teste_true, df_bench, maxlags=3)
        # Sob spanning verdadeiro, não devemos rejeitar a nula (p-valor > 0.05)
        assert p_val_true > 0.05, f"Rejeitado spanning sob H0 verdadeiro (p={p_val_true:.4f})"
        
        # Caso B: Spanning é falso (ativos teste possuem intercepto alfa significativo, expandindo a fronteira)
        t1_fake = 0.005 + 0.6 * b1 + 0.4 * b2 + rng.normal(0.0, 0.001, T)  # alfa massivo
        t2_fake = -0.003 + 0.2 * b1 + 0.8 * b2 + rng.normal(0.0, 0.001, T) # alfa massivo
        df_teste_fake = pd.DataFrame({"T1": t1_fake, "T2": t2_fake})
        
        _, p_val_fake = spanning_multivariado(df_teste_fake, df_bench, maxlags=3)
        # Sob spanning falso, devemos rejeitar a nula (p-valor < 0.01)
        assert p_val_fake < 0.01, f"Falhou em rejeitar spanning sob H1 (p={p_val_fake:.4f})"

