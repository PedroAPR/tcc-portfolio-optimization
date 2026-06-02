"""
Suíte de validação da implementação vetorizada de Ledoit-Wolf (2004).
Execução: python test_ledoit_wolf.py (dentro de 06_Estimacao_Covariancia/)
"""
import sys
import numpy as np

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, ".")
from utils.covariancia import ledoit_wolf, estimar_sigma, condicionamento

rng = np.random.default_rng(42)
passed = []
failed = []

def check(name, ok, detail=""):
    status = "[OK]    " if ok else "[FALHOU]"
    (passed if ok else failed).append(name)
    print(f"  {status} {name}  {detail}")


# ── T0: Paridade com sklearn até epsilon de máquina ───────────────────────
print("=== T0: Paridade com sklearn ===")
try:
    from sklearn.covariance import ledoit_wolf as sklearn_lw
    T, N = 300, 50
    X = rng.standard_normal((T, N))
    S_sk, delta_sk = sklearn_lw(X, assume_centered=False)
    S_custom, delta_custom = ledoit_wolf(X)
    diff_mat   = float(np.max(np.abs(S_sk - S_custom)))
    diff_delta = abs(delta_custom - delta_sk)
    check(
        "Paridade sklearn — matriz (diff < 1e-10)",
        diff_mat < 1e-10,
        f"max_diff={diff_mat:.2e}  delta_custom={delta_custom:.6f}"
        f"  delta_sk={delta_sk:.6f}  ddelta={diff_delta:.2e}",
    )
except ImportError:
    print("  [SKIP] sklearn não instalado — instale com: pip install scikit-learn")


# ── T1: Estabilidade espectral — lam_min > 1e-8 em qualquer regime T/N ──────
print("\n=== T1: Estabilidade espectral (lam_min > 1e-8) ===")
for label, (t, n) in [
    ("T >> N (252×50)", (252, 50)),
    ("T  = N  (50×50)", (50,  50)),
    ("T  < N  (30×50)", (30,  50)),
]:
    X = rng.standard_normal((t, n))
    S, delta = ledoit_wolf(X)
    lam_min = float(np.linalg.eigvalsh(S).min())
    check(
        f"lam_min > 1e-8  [{label}]",
        lam_min > 1e-8,
        f"lam_min={lam_min:.2e}  delta={delta:.4f}",
    )


# ── T2: Simetria perfeita ─────────────────────────────────────────────────
print("\n=== T2: Simetria |S − Sᵀ| < 1e-14 ===")
X = rng.standard_normal((500, 80))
S, _ = ledoit_wolf(X)
diff_sym = float(np.max(np.abs(S - S.T)))
check("Simetria  |S − Sᵀ| < 1e-14", diff_sym < 1e-14, f"diff={diff_sym:.2e}")


# ── T3: Dimensões N×N ─────────────────────────────────────────────────────
print("\n=== T3: Dimensões (N×N) ===")
for t, n in [(200, 40), (100, 100), (50, 30)]:
    X = rng.standard_normal((t, n))
    S, _ = ledoit_wolf(X)
    check(f"shape=({n},{n})  [T={t}]", S.shape == (n, n), f"obtido={S.shape}")


# ── T4: Conservação do traço ──────────────────────────────────────────────
print("\n=== T4: Conservação do traço  Tr(Sigma_LW) == Tr(S_ddof0) ===")
T4, N4 = 400, 60
X = rng.standard_normal((T4, N4))
Xc = X - X.mean(0)
S_ddof0 = (Xc.T @ Xc) / T4
S_lw, _ = ledoit_wolf(X)
diff_tr = abs(np.trace(S_ddof0) - np.trace(S_lw))
check(
    "Traço conservado (diff < 1e-10)",
    diff_tr < 1e-10,
    f"Tr(S_ddof0)={np.trace(S_ddof0):.6f}  Tr(S_LW)={np.trace(S_lw):.6f}  diff={diff_tr:.2e}",
)


# ── T5: Monotonia do delta com dados correlacionados ─────────────────────
# Usa estrutura de fator comum (retornos de ações reais), não i.i.d.
# Com dados i.i.d. N(0,1), b2bar >> d2 e delta satura em 1.0 para janelas
# grandes, mascarando a monotonia. Com correlação (fator de mercado), o
# comportamento esperado pela teoria é recuperado corretamente.
print("\n=== T5: Monotonia do delta (dados correlacionados) ===")
fator  = rng.standard_normal(500)
betas  = rng.uniform(0.3, 1.2, 80)
ret_sim = np.outer(fator, betas) * 0.01 + rng.standard_normal((500, 80)) * 0.02
deltas = {}
for t in [500, 252, 126, 63]:
    _, d = ledoit_wolf(ret_sim[-t:])
    deltas[t] = d
monotone = all(deltas[a] < deltas[b] for a, b in zip([500, 252, 126], [252, 126, 63]))
detalhe = "  ".join([f"T={t}:delta={deltas[t]:.4f}" for t in [500, 252, 126, 63]])
check("delta cresce com janela menor (correlação de mercado)", monotone, detalhe)


# ── T6: estimar_sigma anualiza por TRADING_DAYS ───────────────────────────
print("\n=== T6: estimar_sigma anualiza por TRADING_DAYS=252 ===")
X = rng.standard_normal((300, 30))
S_diaria, _ = ledoit_wolf(X)
S_anual = estimar_sigma(X, "ledoit_wolf", 252)
diff_an = float(np.max(np.abs(S_anual - S_diaria * 252)))
check("estimar_sigma == LW × 252", diff_an < 1e-12, f"diff={diff_an:.2e}")


# ── T7: Vetorizado == Loop — precisão 10⁻¹² ──────────────────────────────
print("\n=== T7: Vetorizado vs Loop original — precisão ===")

def ledoit_wolf_loop(X):
    """Implementação de referência com loop Python explícito (O(T·N²))."""
    X = np.asarray(X, float)
    T, N = X.shape
    Xc = X - X.mean(0)
    S  = (Xc.T @ Xc) / T
    mu = np.trace(S) / N
    F  = mu * np.eye(N)
    d2 = np.sum((S - F) ** 2) / N
    if d2 == 0:
        return S, 0.0
    b2bar = 0.0
    for t in range(T):
        xi   = Xc[t]
        outer = np.outer(xi, xi)
        b2bar += np.sum((outer - S) ** 2) / N
    b2bar /= T ** 2
    b2    = min(b2bar, d2)
    delta = b2 / d2
    return delta * F + (1.0 - delta) * S, delta

X_v = rng.standard_normal((200, 40))
S_vec,  d_vec  = ledoit_wolf(X_v)
S_loop, d_loop = ledoit_wolf_loop(X_v)
diff_impl  = float(np.max(np.abs(S_vec - S_loop)))
diff_delta = abs(d_vec - d_loop)
check(
    "Vetorizado == Loop  (diff < 1e-12)",
    diff_impl < 1e-12,
    f"diff_matrix={diff_impl:.2e}  d_vec={d_vec:.10f}  d_loop={d_loop:.10f}  ddelta={diff_delta:.2e}",
)


# ── T8: Edge case T=2 (mínimo válido) ────────────────────────────────────
print("\n=== T8: Edge case T=2 (mínimo válido) ===")
try:
    X = rng.standard_normal((2, 5))
    S, d = ledoit_wolf(X)
    check("T=2 não crasha", True, f"shape={S.shape}  delta={d:.4f}")
except Exception as e:
    check("T=2 não crasha", False, str(e))


# ── T9: Edge case T=1 deve levantar ValueError ────────────────────────────
print("\n=== T9: Edge case T=1 levanta ValueError ===")
try:
    ledoit_wolf(rng.standard_normal((1, 5)))
    check("T=1 levanta ValueError", False, "nenhuma exceção lançada")
except ValueError:
    check("T=1 levanta ValueError", True, "ValueError lançado corretamente")
except Exception as e:
    check("T=1 levanta ValueError", False, f"exceção errada: {type(e).__name__}: {e}")


# ── T10: condicionamento retorna κ e lam_min corretos ───────────────────────
print("\n=== T10: condicionamento(S) retorna (κ, lam_min) ===")
X = rng.standard_normal((300, 30))
S, _ = ledoit_wolf(X)
kappa, lam_min = condicionamento(S * 252)
ev = np.linalg.eigvalsh(S * 252)
kappa_ref  = ev.max() / max(ev.min(), 1e-18)
lam_min_ref = ev.min()
check(
    "κ e lam_min corretos (diff < 1e-10)",
    abs(kappa - kappa_ref) < 1e-10 and abs(lam_min - lam_min_ref) < 1e-10,
    f"κ={kappa:.2f}  lam_min={lam_min:.4e}",
)


# ── Resultado final ───────────────────────────────────────────────────────
print()
print("=" * 60)
print(f"RESULTADO: {len(passed)} aprovados / {len(failed)} reprovados")
if failed:
    print(f"FALHAS   : {failed}")
    sys.exit(1)
else:
    print("TODOS OS TESTES APROVADOS")
print("=" * 60)
