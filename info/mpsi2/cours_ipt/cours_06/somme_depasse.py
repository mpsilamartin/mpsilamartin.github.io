def somme(n):
    """1+2+...+n"""
    S = 0
    for k in range(1,n+1):
        S = S+k
    return S

def somme_depasse_naif(M):
    """Plus petit n tq 1+2+...+n > M"""
    n = 0
    while somme(n) <= M :
        n = n+1
    # somme(n) > M
    return n

def somme_depasse(M):
    """Plus petit n tq 1+2+...+n > M"""
    n = 0
    S = 0
    # S = 0 
    while S <= M :
        # Variant : ceil(M)-S
        # Inv : S = 1+2+....n 
        n = n+1
        # S = 1+2+...+(n-1)
        S = S+n
        # Inv : S = 1+2+...+n
    # Inv : S = 1+2+...+n
    # S > M, et 1+2+...+(n-1) <= M
    return n
