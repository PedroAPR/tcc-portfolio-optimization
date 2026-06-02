import json
from pathlib import Path

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Notebook 8 — Fronteira Eficiente: Média-Variância e Média-CVaR\n",
                "\n",
                "**TCC — Pedro Augusto Pinheiro Reis · Ciências Contábeis · UFG**\n",
                "\n",
                "Este notebook calcula a fronteira eficiente clássica (média-variância de Markowitz) e a fronteira da teoria pós-moderna (média-CVaR) para o universo investível da B3. Também gera a nuvem de carteiras simuladas por Monte Carlo e exporta as carteiras canônicas e imagens consolidadas para tabulação e escrita do TCC."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 1. Importações e Configurações"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import sys\n",
                "from pathlib import Path\n",
                "import numpy as np\n",
                "import pandas as pd\n",
                "import matplotlib.pyplot as plt\n",
                "\n",
                "from utils.config_loader import carregar_parametros\n",
                "from utils.fronteira import (\n",
                "    ledoit_wolf,\n",
                "    min_var,\n",
                "    max_sharpe,\n",
                "    min_cvar,\n",
                "    cvar_diario,\n",
                "    port_ret,\n",
                "    port_vol,\n",
                "    CVXPY_OK\n",
                ")\n",
                "\n",
                "# Carrega configurações centrais\n",
                "cfg = carregar_parametros()\n",
                "SEED = cfg.get(\"SEED\", 42)\n",
                "N_MONTECARLO = cfg.get(\"N_MONTECARLO\", 50000)\n",
                "N_PONTOS_FRONT = cfg.get(\"N_PONTOS_FRONT\", 60)\n",
                "ATIVOS_NUVEM = cfg.get(\"ATIVOS_NUVEM\", 10)\n",
                "ALPHA = cfg.get(\"ALPHA_PMPT\", 0.95)\n",
                "TETO_PESO = cfg.get(\"TETO_PESO\", 0.10)\n",
                "DIRICHLET_ALPHA = cfg.get(\"DIRICHLET_ALPHA\", 0.30)\n",
                "TRADING_DAYS = 252\n",
                "\n",
                "np.random.seed(SEED)\n",
                "\n",
                "project_root = Path.cwd().parent.parent\n",
                "DIR_RETORNOS = project_root / \"data\" / \"Retornos\"\n",
                "OUTPUT_DIR = project_root / \"data\" / \"Estrategias\"\n",
                "OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n",
                "\n",
                "print(f\"✓ Configurações carregadas. CVXPY disponível: {CVXPY_OK}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Leitura dos Retornos e Taxa de Juros"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "def _ler(nome, col=None):\n",
                "    pq = DIR_RETORNOS / f\"{nome}.parquet\"\n",
                "    csv = DIR_RETORNOS / f\"{nome}.csv\"\n",
                "    df = pd.read_parquet(pq) if pq.exists() else pd.read_csv(csv, index_col=0, parse_dates=True)\n",
                "    df.index = pd.to_datetime(df.index)\n",
                "    return df[col] if col else df\n",
                "\n",
                "ret = _ler(\"retornos_simples_saneado\").sort_index()\n",
                "try:\n",
                "    rf_d = _ler(\"rf_diario\", \"cdi_diario\").reindex(ret.index).dropna()\n",
                "    rf_anual = float(rf_d.mean() * TRADING_DAYS)\n",
                "except Exception:\n",
                "    rf_anual = 0.10\n",
                "\n",
                "N = ret.shape[1]\n",
                "print(f\"Retornos: {ret.shape[0]} pregões × {N} ativos | rf anualizado usado = {rf_anual:.4f}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Estimação de Parâmetros (Média e Covariância via Ledoit-Wolf)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "R = ret.values\n",
                "mu = R.mean(axis=0) * TRADING_DAYS\n",
                "Sig = ledoit_wolf(R) * TRADING_DAYS\n",
                "\n",
                "print(f\"μ média anualizada: {mu.mean():.4f} [{mu.min():.3f}, {mu.max():.3f}]\")\n",
                "print(f\"Vol média anualizada dos ativos: {np.sqrt(np.diag(Sig)).mean():.4f}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. Nuvem Monte Carlo de Oportunidades Viáveis"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "rng = np.random.default_rng(SEED)\n",
                "# Seleciona subconjunto de ativos de forma uniforme em termos de volatilidade para visualização\n",
                "ordem = np.argsort(np.diag(Sig))\n",
                "idx_sub = ordem[np.linspace(0, N-1, ATIVOS_NUVEM).astype(int)]\n",
                "mu_s = mu[idx_sub]\n",
                "Sig_s = Sig[np.ix_(idx_sub, idx_sub)]\n",
                "\n",
                "W = rng.dirichlet(np.full(ATIVOS_NUVEM, DIRICHLET_ALPHA), size=N_MONTECARLO)\n",
                "mc_ret = W @ mu_s\n",
                "mc_vol = np.sqrt(np.einsum('ij,jk,ik->i', W, Sig_s, W))\n",
                "mc_sharpe = (mc_ret - rf_anual) / mc_vol\n",
                "\n",
                "print(f\"Nuvem: {N_MONTECARLO} carteiras simuladas sobre {ATIVOS_NUVEM} ativos.\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 5. Fronteira Média-Variância e Carteiras Canônicas"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "w_mvp = min_var(Sig, mu)\n",
                "w_tan = max_sharpe(mu, Sig, rf_anual)\n",
                "w_tan10 = max_sharpe(mu, Sig, rf_anual, TETO_PESO)\n",
                "\n",
                "alvos = np.linspace(port_ret(w_mvp, mu), mu.max() * 0.98, N_PONTOS_FRONT)\n",
                "fmv = []\n",
                "for a in alvos:\n",
                "    w = min_var(Sig, mu, ret_alvo=a)\n",
                "    if abs(port_ret(w, mu) - a) < 1e-3:\n",
                "        fmv.append((port_vol(w, Sig), port_ret(w, mu)))\n",
                "fmv = np.array(fmv)\n",
                "\n",
                "print(f\"Fronteira MV: {len(fmv)} pontos obtidos.\")\n",
                "print(f\"MVP:      vol={port_vol(w_mvp, Sig):.4f} ret={port_ret(w_mvp, mu):.4f}\")\n",
                "print(f\"Tangente: vol={port_vol(w_tan, Sig):.4f} ret={port_ret(w_tan, mu):.4f}\")\n",
                "print(f\"Tangente (Cap 10%): vol={port_vol(w_tan10, Sig):.4f} ret={port_ret(w_tan10, mu):.4f}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 6. Fronteira Média-CVaR (PMPT)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "fcvar = []\n",
                "w_mincvar = None\n",
                "if CVXPY_OK:\n",
                "    w_mincvar = min_cvar(R, mu, ALPHA)\n",
                "    if w_mincvar is not None:\n",
                "        w_mincvar = w_mincvar / w_mincvar.sum()\n",
                "        # Varre retornos-alvo para traçar a fronteira média-CVaR\n",
                "        for a in np.linspace(port_ret(w_mincvar, mu), mu.max() * 0.95, max(20, N_PONTOS_FRONT // 2)):\n",
                "            w = min_cvar(R, mu, ALPHA, ret_alvo=a)\n",
                "            if w is not None and abs(w.sum() - 1.0) < 1e-3:\n",
                "                fcvar.append((cvar_diario(w / w.sum(), R, ALPHA), port_ret(w / w.sum(), mu)))\n",
                "        fcvar = np.array(fcvar)\n",
                "        print(f\"Fronteira média-CVaR: {len(fcvar)} pontos obtidos.\")\n",
                "        print(f\"Min-CVaR: CVaR_diário={cvar_diario(w_mincvar, R, ALPHA):.5f} ret={port_ret(w_mincvar, mu):.4f}\")\n",
                "else:\n",
                "    print(\"[AVISO] cvxpy ou solvers ausentes. Fronteira CVaR pulada.\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 7. Gráficos Consolidados (Espaço MPT e PMPT)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "n_panels = 2 if (CVXPY_OK and len(fcvar) > 0) else 1\n",
                "fig, axs = plt.subplots(1, n_panels, figsize=((13, 5.2) if n_panels == 2 else (7.5, 5.5)))\n",
                "axes = np.atleast_1d(axs)\n",
                "ax0 = axes[0]\n",
                "\n",
                "sc = ax0.scatter(mc_vol, mc_ret, c=mc_sharpe, s=6, alpha=0.35, cmap=\"viridis\", rasterized=True)\n",
                "ax0.plot(fmv[:, 0], fmv[:, 1], \"-\", color=\"crimson\", lw=2.2, label=\"Fronteira MV (118 ativos)\")\n",
                "ax0.scatter([port_vol(w_mvp, Sig)], [port_ret(w_mvp, mu)], marker=\"D\", s=90, color=\"navy\", zorder=5, label=\"Mínima Variância (MVP)\")\n",
                "ax0.scatter([port_vol(w_tan, Sig)], [port_ret(w_tan, mu)], marker=\"*\", s=240, color=\"gold\", edgecolor=\"black\", zorder=5, label=\"Tangente (Máx. Sharpe)\")\n",
                "ax0.scatter([port_vol(w_tan10, Sig)], [port_ret(w_tan10, mu)], marker=\"P\", s=120, color=\"darkorange\", edgecolor=\"black\", zorder=5, label=\"Tangente c/ teto 10% (CVM)\")\n",
                "\n",
                "# Plota a Capital Market Line (CML)\n",
                "x_cml = np.linspace(0, port_vol(w_tan, Sig) * 1.4, 50)\n",
                "sh_t = (port_ret(w_tan, mu) - rf_anual) / port_vol(w_tan, Sig)\n",
                "ax0.plot(x_cml, rf_anual + sh_t * x_cml, \"--\", color=\"gray\", lw=1.6, label=\"Capital Market Line\")\n",
                "ax0.scatter([0], [rf_anual], marker=\"o\", s=50, color=\"black\", zorder=5)\n",
                "\n",
                "ax0.annotate(f\"Tangente concentrada\\n(maior peso {w_tan.max():.0%}, {(w_tan>0.01).sum()} ativos>1%)\\n→ 'maximização de erros'\",\n",
                "             xy=(port_vol(w_tan, Sig), port_ret(w_tan, mu)),\n",
                "             xytext=(port_vol(w_tan, Sig) * 1.05, port_ret(w_tan, mu) * 0.78),\n",
                "             fontsize=8, arrowprops=dict(arrowstyle=\"->\", color=\"black\"))\n",
                "\n",
                "ax0.set_xlabel(\"Volatilidade anual (σ)\")\n",
                "ax0.set_ylabel(\"Retorno esperado anual (μ)\")\n",
                "ax0.set_title(\"Espaço média-variância (MPT)\")\n",
                "ax0.legend(fontsize=7.5, loc=\"lower right\")\n",
                "ax0.grid(alpha=0.3)\n",
                "fig.colorbar(sc, ax=ax0, label=\"Sharpe\", fraction=0.046, pad=0.04)\n",
                "\n",
                "if CVXPY_OK and len(fcvar) > 0:\n",
                "    ax1 = axes[1]\n",
                "    ax1.plot(fcvar[:, 0], fcvar[:, 1], \"-o\", color=\"teal\", ms=3, lw=2, label=\"Fronteira média-CVaR (118 ativos)\")\n",
                "    ax1.scatter([cvar_diario(w_mincvar, R, ALPHA)], [port_ret(w_mincvar, mu)], marker=\"D\", s=90, color=\"purple\", zorder=5, label=\"Mínimo CVaR\")\n",
                "    ax1.set_xlabel(f\"CVaR diário (α={ALPHA:.0%})\")\n",
                "    ax1.set_ylabel(\"Retorno esperado anual (μ)\")\n",
                "    ax1.set_title(\"Espaço média-CVaR (PMPT)\")\n",
                "    ax1.legend(fontsize=8)\n",
                "    ax1.grid(alpha=0.3)\n",
                "    FIGURA_COMPLETA = True\n",
                "else:\n",
                "    FIGURA_COMPLETA = False\n",
                "    motivo = \"CVXPY ausente ou erros de convergência\"\n",
                "    ax0.text(0.5, -0.16,\n",
                "             f\"⚠ FIGURA PARCIAL — painel média-CVaR (PMPT) NÃO gerado: {motivo}.\\n\",\n",
                "             transform=ax0.transAxes, ha=\"center\", va=\"top\", fontsize=9, color=\"darkred\")\n",
                "\n",
                "_titulo = \"Fronteira Eficiente — universo investável da B3 (in-sample, 2010–2025)\"\n",
                "if not FIGURA_COMPLETA:\n",
                "    _titulo += \"  [PARCIAL: sem painel CVaR]\"\n",
                "fig.suptitle(_titulo, fontsize=12, color=(\"black\" if FIGURA_COMPLETA else \"darkred\"))\n",
                "fig.tight_layout()\n",
                "plt.savefig(OUTPUT_DIR / \"fronteira_eficiente.png\", dpi=150, bbox_inches=\"tight\")\n",
                "plt.savefig(OUTPUT_DIR / \"fronteira_eficiente.svg\", bbox_inches=\"tight\")\n",
                "print(\"[OK] Imagens salvas com sucesso em:\", OUTPUT_DIR)\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 8. Exportação dos Resultados (CSV)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "pd.DataFrame(fmv, columns=[\"vol\", \"ret\"]).to_csv(OUTPUT_DIR / \"fronteira_mv_pontos.csv\", index=False)\n",
                "if CVXPY_OK and len(fcvar) > 0:\n",
                "    pd.DataFrame(fcvar, columns=[\"cvar_diario\", \"ret\"]).to_csv(OUTPUT_DIR / \"fronteira_cvar_pontos.csv\", index=False)\n",
                "\n",
                "canon = {\"MVP\": w_mvp, \"Tangente\": w_tan, \"Tangente_c10\": w_tan10}\n",
                "if CVXPY_OK and w_mincvar is not None:\n",
                "    canon[\"MinCVaR\"] = w_mincvar\n",
                "\n",
                "linhas = []\n",
                "for nome, w in canon.items():\n",
                "    linhas.append({\n",
                "        \"carteira\": nome,\n",
                "        \"ret_anual\": port_ret(w, mu),\n",
                "        \"vol_anual\": port_vol(w, Sig),\n",
                "        \"sharpe\": (port_ret(w, mu) - rf_anual) / port_vol(w, Sig),\n",
                "        \"maior_peso\": float(w.max()),\n",
                "        \"n_ativos_>1pct\": int((w > 0.01).sum())\n",
                "    })\n",
                "\n",
                "pd.DataFrame(linhas).to_csv(OUTPUT_DIR / \"carteiras_canonicas.csv\", index=False, float_format=\"%.6f\")\n",
                "print(\"✓ Resultados salvos com sucesso em:\", OUTPUT_DIR)"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.11.9"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
}

nb_folder = Path("src/08_Fronteira_Eficiente")
nb_folder.mkdir(parents=True, exist_ok=True)
with open(nb_folder / "08_01_Fronteira_Eficiente.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=1)

print("✓ Stage 8 notebook generated successfully!")
