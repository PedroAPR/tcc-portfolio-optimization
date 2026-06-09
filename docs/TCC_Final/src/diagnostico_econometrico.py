import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller, kpss, coint
from statsmodels.stats.diagnostic import acorr_ljungbox, het_arch
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import breaks_cusumolsresid

# Configurar estilo visual premium para os graficos
sns.set_theme(style="whitegrid")
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.titlesize': 16,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.linestyle': '--'
})

def calcular_log_retornos(df_precos):
    """
    Calcula log-retornos diarios para as colunas de ativos.
    Mantem a coluna 'Data' alinhada.
    """
    df_ret = df_precos.copy()
    colunas_ativos = [c for c in df_precos.columns if c != 'Data']
    
    # Calcular retornos logaritmicos: ln(P_t / P_{t-1})
    for col in colunas_ativos:
        df_ret[col] = np.log(df_ret[col] / df_ret[col].shift(1))
        
    return df_ret.dropna().reset_index(drop=True)

def teste_razao_variancia_lo_mackinlay(series, q=5):
    """
    Implementa o Teste de Razao de Variancia de Lo-MacKinlay (1988)
    Sob a hipotese nula de Passeio Aleatorio, VR(q) = 1.
    """
    series = series.dropna().values
    n = len(series)
    mu = np.mean(series)
    
    # Variancia de 1 periodo
    var_1 = np.sum((series - mu) ** 2) / (n - 1)
    
    # Variancia de q periodos
    # Precisamos acumular os retornos em blocos de q periodos
    returns_q = []
    for i in range(q - 1, n):
        returns_q.append(np.sum(series[i - q + 1 : i + 1]))
    returns_q = np.array(returns_q)
    
    m = q * (n - q + 1) * (1 - q / n)
    var_q = np.sum((returns_q - q * mu) ** 2) / m
    
    # Razao de Variancia
    vr = var_q / var_1 if var_1 > 0 else np.nan
    
    # Erro padrao assintotico sob homoscedasticidade
    phi = (2 * (2 * q - 1) * (q - 1)) / (3 * q * n)
    z_stat = (vr - 1) / np.sqrt(phi) if phi > 0 else np.nan
    p_val = 2 * (1 - stats.norm.cdf(abs(z_stat))) if not np.isnan(z_stat) else np.nan
    
    return vr, z_stat, p_val

def calcular_break_chow_manual(series, split_idx):
    """
    Calcula o Teste de Chow manual para quebra estrutural.
    Compara a regressao linear em toda a serie vs as duas subseries.
    """
    y = series.values
    x = np.arange(len(y))
    x = sm.add_constant(x)
    
    # Modelo restrito (toda a serie)
    model_r = sm.OLS(y, x).fit()
    rss_r = model_r.ssr
    
    # Subperiodo 1
    y1, x1 = y[:split_idx], x[:split_idx]
    model_1 = sm.OLS(y1, x1).fit()
    rss_1 = model_1.ssr
    
    # Subperiodo 2
    y2, x2 = y[split_idx:], x[split_idx:]
    model_2 = sm.OLS(y2, x2).fit()
    rss_2 = model_2.ssr
    
    # Estatistica F de Chow
    k = 2  # Numero de parametros (constante + inclinacao)
    n = len(y)
    numerator = (rss_r - (rss_1 + rss_2)) / k
    denominator = (rss_1 + rss_2) / (n - 2 * k)
    
    f_stat = numerator / denominator if denominator > 0 else np.nan
    p_val = 1 - stats.f.cdf(f_stat, k, n - 2 * k) if not np.isnan(f_stat) else np.nan
    
    return f_stat, p_val

def principal_pipeline():
    # Caminhos e diretorios
    pasta_dados = r"C:\VSCodeWorkspace\TCC_Final\data"
    pasta_resultados = r"C:\VSCodeWorkspace\TCC_Final\results\diagnostico"
    os.makedirs(pasta_resultados, exist_ok=True)
    
    caminho_parquet = os.path.join(pasta_dados, "lista_economatica_dados_filtrados.parquet")
    print(f"Lendo dados de: {caminho_parquet}")
    df_precos = pd.read_parquet(caminho_parquet, engine='pyarrow')
    
    # 13. Discussao do Painel Desbalanceado
    print("\n[TESTE 13] Analisando estrutura do painel de dados...")
    total_linhas = len(df_precos)
    total_ativos = len(df_precos.columns) - 1
    total_celulas = total_linhas * total_ativos
    total_missing = df_precos.drop(columns=['Data']).isna().sum().sum()
    pct_missing = (total_missing / total_celulas) * 100
    
    print(f"Estrutura do painel:")
    print(f"- Total de dias: {total_linhas}")
    print(f"- Total de ativos: {total_ativos}")
    print(f"- Total de observacoes potenciais: {total_celulas}")
    print(f"- Total de valores nulos (dados ausentes): {total_missing} ({pct_missing:.2f}%)")
    
    # Calcular retornos
    print("\nCalculando log-retornos...")
    df_retornos = calcular_log_retornos(df_precos)
    
    # =========================================================================
    # PARTE 1: DIAGNOSTICOS DETALHADOS PARA ATIVO CASO DE ESTUDO (PETR4)
    # =========================================================================
    ativo_estudo = 'PETR4'
    print(f"\n==================================================")
    print(f"Iniciando Diagnosticos Detalhados para: {ativo_estudo}")
    print(f"==================================================")
    
    precos_petr = df_precos[ativo_estudo]
    retornos_petr = df_retornos[ativo_estudo]
    
    # 1. ADF em Precos
    adf_pr_stat, adf_pr_p, _, _, adf_pr_crit, _ = adfuller(precos_petr, regression='c')
    print(f"[TESTE 1] ADF em Precos: Stat = {adf_pr_stat:.4f}, p-valor = {adf_pr_p:.4f}")
    
    # 2. ADF em Log-Retornos
    adf_ret_stat, adf_ret_p, _, _, adf_ret_crit, _ = adfuller(retornos_petr, regression='c')
    print(f"[TESTE 2] ADF em Log-Retornos: Stat = {adf_ret_stat:.4f}, p-valor = {adf_ret_p:.4f}")
    
    # 3. KPSS em Precos e Log-Retornos
    kpss_pr_stat, kpss_pr_p, _, kpss_pr_crit = kpss(precos_petr, regression='c', nlags='auto')
    kpss_ret_stat, kpss_ret_p, _, kpss_ret_crit = kpss(retornos_petr, regression='c', nlags='auto')
    print(f"[TESTE 3] KPSS em Precos: Stat = {kpss_pr_stat:.4f}, p-valor = {kpss_pr_p:.4f}")
    print(f"         KPSS em Log-Retornos: Stat = {kpss_ret_stat:.4f}, p-valor = {kpss_ret_p:.4f}")
    
    # Ajustar um modelo AR(1) para obter residuos padronizados
    ar_model = sm.tsa.ARIMA(retornos_petr, order=(1, 0, 0)).fit()
    residuos = ar_model.resid
    residuos_std = residuos / np.std(residuos)
    
    # 4. Ljung-Box nos Residuos do AR(1)
    lb_df = acorr_ljungbox(residuos, lags=[10], return_df=True)
    lb_stat = lb_df['lb_stat'].values[0]
    lb_p = lb_df['lb_pvalue'].values[0]
    print(f"[TESTE 4] Ljung-Box nos Residuos (Lag 10): Stat = {lb_stat:.4f}, p-valor = {lb_p:.4f}")
    
    # 5. ACF/PACF Grafico
    print("[TESTE 5] Gerando graficos de ACF e PACF para PETR4...")
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    plot_acf(retornos_petr, lags=30, ax=axes[0], alpha=0.05, color='#1f77b4')
    axes[0].set_title('Autocorrelacao (ACF) - PETR4')
    axes[0].set_xlabel('Lag')
    plot_pacf(retornos_petr, lags=30, ax=axes[1], alpha=0.05, color='#ff7f0e')
    axes[1].set_title('Autocorrelacao Parcial (PACF) - PETR4')
    axes[1].set_xlabel('Lag')
    plt.tight_layout()
    plt.savefig(os.path.join(pasta_resultados, "1_acf_pacf_petr4.png"), bbox_inches='tight')
    plt.close()
    
    # 6. ARCH LM (Engle) nos Residuos
    lm_stat, lm_p, f_stat, f_p = het_arch(residuos, nlags=10)
    print(f"[TESTE 6] ARCH LM (Engle) (Lag 10): LM Stat = {lm_stat:.4f}, p-valor = {lm_p:.4f}")
    
    # 7 & 8. Chow / CUSUM e Bai-Perron
    # CUSUM dos residuos OLS
    print("[TESTE 7 & 8] Executando analise de quebras estruturais (CUSUM/Chow)...")
    cusum_res = breaks_cusumolsresid(residuos, ddof=1)
    # Chow no meio da serie
    midpoint = len(retornos_petr) // 2
    chow_f, chow_p = calcular_break_chow_manual(retornos_petr, midpoint)
    print(f"         Chow Test (midpoint): F = {chow_f:.4f}, p-valor = {chow_p:.4f}")
    
    # Plot CUSUM
    plt.figure(figsize=(10, 5))
    plt.plot(cusum_res[0], color='#2ca02c', label='CUSUM estatistica')
    plt.axhline(1.36, color='red', linestyle='--', label='Limiar 5% de Significado')
    plt.axhline(-1.36, color='red', linestyle='--')
    plt.title('Teste CUSUM de Estabilidade de Parametros - PETR4')
    plt.xlabel('Observacoes')
    plt.ylabel('CUSUM acumulado')
    plt.legend()
    plt.savefig(os.path.join(pasta_resultados, "5_cusum_structural_breaks.png"), bbox_inches='tight')
    plt.close()
    
    # 9. Jarque-Bera (Normalidade formal)
    jb_stat, jb_p = stats.jarque_bera(retornos_petr)
    print(f"[TESTE 9] Jarque-Bera: JB Stat = {jb_stat:.4f}, p-valor = {jb_p:.4f}")
    
    # 10. ACF dos Retornos ao Quadrado
    print("[TESTE 10] Gerando ACF dos Retornos ao Quadrado...")
    plt.figure(figsize=(10, 5))
    plot_acf(retornos_petr**2, lags=30, alpha=0.05, color='#d62728')
    plt.title('ACF dos Retornos ao Quadrado (Assinatura ARCH) - PETR4')
    plt.xlabel('Lag')
    plt.savefig(os.path.join(pasta_resultados, "2_acf_squared_petr4.png"), bbox_inches='tight')
    plt.close()
    
    # 11. QQ-plot dos Residuos Padronizados
    print("[TESTE 11] Gerando QQ-plot dos Residuos...")
    fig, ax = plt.subplots(figsize=(6, 6))
    sm.qqplot(residuos_std, line='45', ax=ax)
    ax.get_lines()[0].set_color('#1f77b4')
    ax.get_lines()[0].set_markersize(4)
    ax.get_lines()[1].set_color('#d62728')
    ax.get_lines()[1].set_linewidth(2)
    plt.title('QQ-Plot dos Residuos Padronizados - PETR4')
    plt.savefig(os.path.join(pasta_resultados, "3_qqplot_petr4.png"), bbox_inches='tight')
    plt.close()
    
    # 12. Correlacao Rolante (Instabilidade da covariancia)
    print("[TESTE 12] Gerando Correlacao Rolante...")
    if 'VALE3' in df_retornos.columns:
        rolling_corr = df_retornos['PETR4'].rolling(252).corr(df_retornos['VALE3'])
        plt.figure(figsize=(10, 5))
        plt.plot(df_precos['Data'].iloc[df_retornos.index], rolling_corr, color='#9467bd', label='PETR4 vs VALE3 (252-dias)')
        plt.title('Correlacao Rolante Dinamica (Instabilidade de Covariancia)')
        plt.xlabel('Data')
        plt.ylabel('Correlacao de Pearson')
        plt.legend()
        plt.savefig(os.path.join(pasta_resultados, "4_rolling_correlation.png"), bbox_inches='tight')
        plt.close()
        print("[OK] Correlacao rolante PETR4 vs VALE3 gerada!")
        
    # 14. Cointegracao (Johansen e Engle-Granger)
    print("[TESTE 14] Testando cointegracao entre PETR3 e PETR4...")
    if 'PETR3' in df_precos.columns and 'PETR4' in df_precos.columns:
        eg_stat, eg_p, eg_crit = coint(df_precos['PETR3'], df_precos['PETR4'])
        print(f"         Engle-Granger Cointegracao: Stat = {eg_stat:.4f}, p-valor = {eg_p:.4f}")
        
    # 15. Teste de Razao de Variancia (Lo-MacKinlay)
    vr, z_stat, vr_p = teste_razao_variancia_lo_mackinlay(retornos_petr, q=5)
    print(f"[TESTE 15] Teste de Razao de Variancia Lo-MacKinlay (q=5): VR = {vr:.4f}, z-stat = {z_stat:.4f}, p-valor = {vr_p:.4f}")
    
    # 16. IQR nos Retornos
    q75, q25 = np.percentile(retornos_petr, [75 ,25])
    iqr = q75 - q25
    outlier_limite_sup = q75 + 1.5 * iqr
    outlier_limite_inf = q25 - 1.5 * iqr
    outliers = retornos_petr[(retornos_petr > outlier_limite_sup) | (retornos_petr < outlier_limite_inf)]
    pct_outliers = (len(outliers) / len(retornos_petr)) * 100
    print(f"[TESTE 16] Outliers via IQR: IQR = {iqr:.4f}, Total Outliers = {len(outliers)} ({pct_outliers:.2f}%)")
    
    # =========================================================================
    # PARTE 2: DIAGNOSTICOS CONSOLIDADOS PARA O PAINEL DE 130 ATIVOS
    # =========================================================================
    print(f"\n==================================================")
    print(f"Iniciando Testes Consolidados no Painel (130 Ativos)")
    print(f"==================================================")
    
    colunas_ativos = [c for c in df_retornos.columns if c != 'Data']
    lista_diagnosticos = []
    
    for idx, col in enumerate(colunas_ativos):
        precos_col = df_precos[col]
        retornos_col = df_retornos[col]
        
        # ADF em Precos
        try:
            adf_pr_stat, adf_pr_p, _, _, _, _ = adfuller(precos_col, regression='c')
        except:
            adf_pr_stat, adf_pr_p = np.nan, np.nan
            
        # ADF em Retornos
        try:
            adf_ret_stat, adf_ret_p, _, _, _, _ = adfuller(retornos_col, regression='c')
        except:
            adf_ret_stat, adf_ret_p = np.nan, np.nan
            
        # KPSS em Retornos
        try:
            kpss_ret_stat, kpss_ret_p, _, _ = kpss(retornos_col, regression='c', nlags='auto')
        except:
            kpss_ret_stat, kpss_ret_p = np.nan, np.nan
            
        # Jarque-Bera
        try:
            jb_stat, jb_p = stats.jarque_bera(retornos_col)
        except:
            jb_stat, jb_p = np.nan, np.nan
            
        # ARCH-LM
        try:
            # Residuos AR(1)
            ar_fit = sm.tsa.ARIMA(retornos_col, order=(1, 0, 0)).fit()
            lm_stat, lm_p, _, _ = het_arch(ar_fit.resid, nlags=10)
        except:
            lm_stat, lm_p = np.nan, np.nan
            
        # Ljung-Box
        try:
            lb_df = acorr_ljungbox(retornos_col, lags=[10], return_df=True)
            lb_stat = lb_df['lb_stat'].values[0]
            lb_p = lb_df['lb_pvalue'].values[0]
        except:
            lb_stat, lb_p = np.nan, np.nan
            
        # Variance Ratio
        try:
            vr, _, vr_p = teste_razao_variancia_lo_mackinlay(retornos_col, q=5)
        except:
            vr, vr_p = np.nan, np.nan
            
        # IQR Outliers
        try:
            q75, q25 = np.percentile(retornos_col, [75 ,25])
            iqr = q75 - q25
            outliers = retornos_col[(retornos_col > q75 + 1.5*iqr) | (retornos_col < q25 - 1.5*iqr)]
            pct_outliers = (len(outliers) / len(retornos_col)) * 100
        except:
            iqr, pct_outliers = np.nan, np.nan
            
        lista_diagnosticos.append({
            'Ativo': col,
            'ADF_Preco_Stat': adf_pr_stat,
            'ADF_Preco_p': adf_pr_p,
            'ADF_Retorno_Stat': adf_ret_stat,
            'ADF_Retorno_p': adf_ret_p,
            'KPSS_Retorno_Stat': kpss_ret_stat,
            'KPSS_Retorno_p': kpss_ret_p,
            'JarqueBera_Stat': jb_stat,
            'JarqueBera_p': jb_p,
            'ARCH_LM_Stat': lm_stat,
            'ARCH_LM_p': lm_p,
            'LjungBox_Stat': lb_stat,
            'LjungBox_p': lb_p,
            'VarianceRatio': vr,
            'VarianceRatio_p': vr_p,
            'IQR': iqr,
            'Outliers_Pct': pct_outliers
        })
        
        if (idx + 1) % 20 == 0 or (idx + 1) == len(colunas_ativos):
            print(f"Processado: {idx + 1} / {len(colunas_ativos)} ativos...")
            
    df_diagnostico_painel = pd.DataFrame(lista_diagnosticos)
    caminho_saida_csv = os.path.join(pasta_dados, "diagnostico_econometrico_completo.csv")
    df_diagnostico_painel.to_csv(caminho_saida_csv, index=False, sep=';', decimal=',')
    print(f"\n[OK] Diagnostico consolidado salvo em: {caminho_saida_csv}")
    
    # Salvar um grafico demonstrativo sobre missing data no painel
    print("[TESTE 13] Gerando grafico de contagem de dados ausentes...")
    missing_por_ativo = df_precos.drop(columns=['Data']).isna().sum().sort_values(ascending=False)
    plt.figure(figsize=(12, 6))
    missing_por_ativo.head(30).plot(kind='bar', color='#e74c3c')
    plt.title('Top 30 Ativos com Mais Dados Ausentes no Painel (Dias de Negociacao Nulos)')
    plt.ylabel('Valores Ausentes (NaN)')
    plt.xlabel('Ativo')
    plt.savefig(os.path.join(pasta_resultados, "6_panel_data_timeline.png"), bbox_inches='tight')
    plt.close()
    
    print("\n==================================================")
    print("Processamento econometrico concluido com sucesso!")
    print("==================================================")

if __name__ == "__main__":
    principal_pipeline()
