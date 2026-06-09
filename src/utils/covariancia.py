import numpy as np

def condicionamento(S):
    """Calcula o número de condição (κ) de uma matriz simétrica S.
    Definido como a razão entre o maior e o menor autovalor.
    
    Args:
        S (np.ndarray): Matriz simétrica.
        
    Returns:
        tuple[float, float]: (número de condição, menor autovalor).
    """
    ev = np.linalg.eigvalsh(S)
    menor_ev = max(ev.min(), 1e-18)
    return ev.max() / menor_ev, ev.min()

def ledoit_wolf(X):
    """Estimador de encolhimento (shrinkage) ótimo de Ledoit e Wolf (2004).
    Regulariza a matriz de covariância amostral combinando-a de forma convexa
    com um alvo de variância média estruturado (identidade escalada).
    
    A implementação é totalmente vetorizada em NumPy, substituindo o loop O(T) original.
    
    Args:
        X (np.ndarray): Matriz T x N de retornos históricos (simples).
        
    Returns:
        tuple[np.ndarray, float]: (Matriz de covariância encolhida diária, delta).
    """
    X = np.asarray(X, float)
    T, N = X.shape
    if T <= 1:
        raise ValueError("O número de observações (T) deve ser maior que 1.")
        
    # Centralização dos dados
    Xc = X - X.mean(axis=0)
    
    # Covariância amostral com ddof=0 para manter paridade exata com sklearn
    S = (Xc.T @ Xc) / T
    
    # Alvo F: identidade escalada pela média do traço
    mu = np.trace(S) / N
    F = mu * np.eye(N)
    
    # d2: ||S - F||_F^2 normalizada por N
    d2 = np.sum((S - F) ** 2) / N
    if d2 == 0:
        return S, 0.0
        
    # b2bar: Cálculo ultra-veloz e vetorizado de b2bar (sem loop Python)
    # Equivalente à média temporal de ||x_t x_t^T - S||_F^2 / N
    term1 = np.sum(np.sum(Xc ** 2, axis=1) ** 2)
    term2 = T * np.sum(S ** 2)
    b2bar = (term1 - term2) / (T ** 2 * N)
    
    # Garante restrição assintótica de variância
    b2 = min(b2bar, d2)
    
    # Intensidade do encolhimento
    delta = b2 / d2
    
    # Combinação convexa regularizada
    Sigma_shrunk = delta * F + (1.0 - delta) * S
    return Sigma_shrunk, delta

def estimar_sigma(janela_retornos, metodo="ledoit_wolf", trading_days=252):
    """Helper para obter a matriz de covariância anualizada de uma janela de retornos simples.
    
    Args:
        janela_retornos (np.ndarray): Janela temporal de retornos simples (T x N).
        metodo (str): Método de estimação ("ledoit_wolf" ou "amostral").
        trading_days (int): Dias úteis no ano para anualização (padrão 252).
        
    Returns:
        np.ndarray: Matriz de covariância anualizada (N x N).
    """
    if metodo == "amostral":
        # np.cov usa ddof=1 por padrão para estatística clássica amostral
        return np.cov(janela_retornos, rowvar=False) * trading_days
    
    # Ledoit-wolf usa ddof=0 internamente
    S, _ = ledoit_wolf(janela_retornos)
    return S * trading_days
