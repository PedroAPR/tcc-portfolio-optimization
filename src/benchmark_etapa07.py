"""
benchmark_etapa07.py
====================
Compara o tempo de execução dos otimizadores da etapa 07 entre:
  - baseline : otimizacao_baseline.py  (diferenças finitas, tolerância 1e-5, sem warm-start)
  - otimizado: otimizacao.py           (gradientes analíticos, tol 1e-4, warm-start)

Roda N_PERIODOS períodos sintéticos com T e N representativos do backtest real,
mede o tempo de cada otimizador separadamente e imprime a tabela de speedup.

Uso:
    cd C:\\VSCodeWorkspace\\1_TCC_Final\\src\\07_Otimizacao_Carteiras
    python ../../benchmark_etapa07.py
"""

import sys, time, copy
from pathlib import Path
import numpy as np

# ─── Garante importação dos dois módulos ────────────────────────────────────
HERE   = Path(__file__).resolve().parent
OPT07  = HERE / "07_Otimizacao_Carteiras"
UTILS  = OPT07 / "utils"
sys.path.insert(0, str(OPT07))
sys.path.insert(0, str(UTILS))

# Importa versão otimizada (este branch)
import otimizacao as OPT

# Importa versão baseline criada em paralelo (cópia do master)
BASELINE_PATH = HERE / "otimizacao_baseline.py"
if not BASELINE_PATH.exists():
    print(f"[AVISO] {BASELINE_PATH} não encontrado.")
    print("        Rode: git show master:src/07_Otimizacao_Carteiras/utils/otimizacao.py > src/otimizacao_baseline.py")
    print("        Abortando benchmark.")
    sys.exit(1)

import importlib.util
spec = importlib.util.spec_from_file_location("otimizacao_baseline", BASELINE_PATH)
BASE = importlib.util.module_from_spec(spec)
spec.loader.exec_module(BASE)

# ─── Parâmetros do benchmark ─────────────────────────────────────────────────
RNG          = np.random.default_rng(42)
N_ATIVOS     = 118          # dimensão real do backtest
T_PERIODOS   = [252, 756, 1260, 2016, 2520]   # janelas crescentes (anos 1→10)
TRADING_DAYS = 252
RF_A         = 0.093        # CDI ~9.3% a.a.
MAR          = RF_A / TRADING_DAYS
TETO         = 0.10
ALPHA        = 0.95
N_REP        = 3            # repetições por célula (mediana para robustez)

KAPPA_ORDENS = {"MaxOmega": 1, "MaxSortino": 2, "MaxKappa3": 3}

print("=" * 72)
print("BENCHMARK ETAPA 07 — gradientes analíticos + warm-start + tol CVXPY")
print("=" * 72)
print(f"N_ATIVOS={N_ATIVOS} | repetições por célula={N_REP}")
print()

# ─── Helpers ─────────────────────────────────────────────────────────────────
def _gerar_dados(T, N, rng):
    """Gera retornos sintéticos realistas (média ~0, vol ~1.2%/dia)."""
    R = rng.normal(0.0004, 0.012, (T, N))
    return R

def _medir(fn, *args, reps=N_REP, **kw):
    """Retorna o tempo mediano de `reps` chamadas a fn(*args, **kw)."""
    tempos = []
    for _ in range(reps):
        t0 = time.perf_counter()
        fn(*args, **kw)
        tempos.append(time.perf_counter() - t0)
    return float(np.median(tempos))

# ─── Loop de benchmark ───────────────────────────────────────────────────────
resultados = []

for T in T_PERIODOS:
    R   = _gerar_dados(T, N_ATIVOS, RNG)
    S   = OPT.ledoit_wolf(R)           # mesma Σ para ambas as versões
    mu  = R.mean(axis=0) * TRADING_DAYS
    w0  = OPT.w_equal(N_ATIVOS)        # warm-start inicial = 1/N

    row = {"T": T, "anos": round(T / TRADING_DAYS, 1)}

    # ── MinVar ──────────────────────────────────────────────────────────────
    t_base = _medir(BASE.w_min_var, S, None)
    t_opt  = _medir(OPT.w_min_var,  S, None, w0=w0)
    row["MinVar_base_s"]  = round(t_base, 4)
    row["MinVar_opt_s"]   = round(t_opt,  4)
    row["MinVar_speedup"] = round(t_base / t_opt, 2) if t_opt > 0 else float("inf")

    # ── MaxSharpe ────────────────────────────────────────────────────────────
    t_base = _medir(BASE.w_max_sharpe, mu, S, RF_A, None)
    t_opt  = _medir(OPT.w_max_sharpe,  mu, S, RF_A, None, w0=w0)
    row["MaxSharpe_base_s"]  = round(t_base, 4)
    row["MaxSharpe_opt_s"]   = round(t_opt,  4)
    row["MaxSharpe_speedup"] = round(t_base / t_opt, 2) if t_opt > 0 else float("inf")

    # ── Kappa n=2 (Sortino) ──────────────────────────────────────────────────
    t_base = _medir(BASE.w_max_kappa, R, 2, MAR, None)
    t_opt  = _medir(OPT.w_max_kappa,  R, 2, MAR, None, w0=w0)
    row["Sortino_base_s"]  = round(t_base, 4)
    row["Sortino_opt_s"]   = round(t_opt,  4)
    row["Sortino_speedup"] = round(t_base / t_opt, 2) if t_opt > 0 else float("inf")

    # ── Kappa n=1 (Omega) ────────────────────────────────────────────────────
    t_base = _medir(BASE.w_max_kappa, R, 1, MAR, None)
    t_opt  = _medir(OPT.w_max_kappa,  R, 1, MAR, None, w0=w0)
    row["Omega_base_s"]  = round(t_base, 4)
    row["Omega_opt_s"]   = round(t_opt,  4)
    row["Omega_speedup"] = round(t_base / t_opt, 2) if t_opt > 0 else float("inf")

    # ── MinCVaR (se cvxpy disponível) ───────────────────────────────────────
    if OPT.CVXPY_OK and BASE.CVXPY_OK:
        t_base = _medir(BASE.w_min_cvar, R, ALPHA, None, reps=1)  # lento: 1 rep
        t_opt  = _medir(OPT.w_min_cvar,  R, ALPHA, None, reps=1)
        row["CVaR_base_s"]  = round(t_base, 3)
        row["CVaR_opt_s"]   = round(t_opt,  3)
        row["CVaR_speedup"] = round(t_base / t_opt, 2) if t_opt > 0 else float("inf")
    else:
        row.update({"CVaR_base_s": "n/a", "CVaR_opt_s": "n/a", "CVaR_speedup": "n/a"})

    resultados.append(row)

    # Imprime linha imediatamente para feedback em tempo real
    print(f"T={T:>5} ({row['anos']:>4} anos) | "
          f"MinVar  {row['MinVar_base_s']:.4f}s→{row['MinVar_opt_s']:.4f}s "
          f"({row['MinVar_speedup']:.2f}×) | "
          f"MaxSharpe {row['MaxSharpe_base_s']:.4f}s→{row['MaxSharpe_opt_s']:.4f}s "
          f"({row['MaxSharpe_speedup']:.2f}×) | "
          f"Sortino {row['Sortino_base_s']:.4f}s→{row['Sortino_opt_s']:.4f}s "
          f"({row['Sortino_speedup']:.2f}×)")

# ─── Tabela resumo ────────────────────────────────────────────────────────────
print()
print("=" * 72)
print("RESUMO — SPEEDUP POR OTIMIZADOR")
print("=" * 72)
print(f"{'T':>6} | {'anos':>5} | {'MinVar':>8} | {'MaxSharpe':>9} | {'Sortino':>8} | {'Omega':>7} | {'CVaR':>8}")
print("-" * 72)
for r in resultados:
    cvar_str = f"{r['CVaR_speedup']:.2f}×" if isinstance(r['CVaR_speedup'], float) else r['CVaR_speedup']
    print(f"{r['T']:>6} | {r['anos']:>5} | "
          f"{r['MinVar_speedup']:>7.2f}× | "
          f"{r['MaxSharpe_speedup']:>8.2f}× | "
          f"{r['Sortino_speedup']:>7.2f}× | "
          f"{r['Omega_speedup']:>6.2f}× | "
          f"{cvar_str:>8}")

# ─── Verificação de consistência dos pesos ───────────────────────────────────
print()
print("=" * 72)
print("VERIFICAÇÃO DE CONSISTÊNCIA DOS PESOS (T=756, N=118)")
print("=" * 72)
T_chk, N_chk = 756, N_ATIVOS
R_chk = _gerar_dados(T_chk, N_chk, np.random.default_rng(99))
S_chk = OPT.ledoit_wolf(R_chk)
mu_chk = R_chk.mean(0) * TRADING_DAYS
w0_chk = OPT.w_equal(N_chk)

checks = [
    ("MinVar",    BASE.w_min_var(S_chk, None),              OPT.w_min_var(S_chk, None, w0=w0_chk)),
    ("MaxSharpe", BASE.w_max_sharpe(mu_chk, S_chk, RF_A),   OPT.w_max_sharpe(mu_chk, S_chk, RF_A, w0=w0_chk)),
    ("Sortino",   BASE.w_max_kappa(R_chk, 2, MAR),          OPT.w_max_kappa(R_chk, 2, MAR, w0=w0_chk)),
    ("Omega",     BASE.w_max_kappa(R_chk, 1, MAR),          OPT.w_max_kappa(R_chk, 1, MAR, w0=w0_chk)),
]

for nome, w_b, w_o in checks:
    max_diff = np.abs(w_b - w_o).max()
    budget_ok  = abs(w_o.sum() - 1.0) < 1e-6
    longonly_ok = (w_o >= -1e-9).all()
    status = "✅ OK" if max_diff < 1e-3 else f"⚠️  diff={max_diff:.2e}"
    print(f"  {nome:<12}: max|Δw|={max_diff:.2e}  budget={'OK' if budget_ok else 'FAIL'}  "
          f"long-only={'OK' if longonly_ok else 'FAIL'}  {status}")

print()
print("Benchmark concluído.")
print("Para comparar resultados matemáticos completos (130 períodos reais),")
print("execute o notebook completo e compare desempenho_estrategias.csv entre os branches.")
