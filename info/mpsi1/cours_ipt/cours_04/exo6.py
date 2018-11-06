def reponse():
    """Réponse à l'exo 6"""
    S = 0
    n = 1
    # S = u_{n-1}
    while S < 1000:
        # S = u_{n-1}
        S = S + n**(-.5)
        # S = u_n
        n = n+1
        # S = u_{n-1}
    # S = u_{n-1} et c'est la première valeur de u >=1000
    return n-1

def valeur_u(n):
    """Renvoie u_n"""
    S = 0
    for k in range(1,n+1):
        S = S + k**-.5
    return S

def reponse2():
    """Réponse à l'exo 6"""
    S,n = 0,0
    while S < 10**3:
        # Inv : S = u_n
        n = n+1
        S = S + n**-.5
    return n
