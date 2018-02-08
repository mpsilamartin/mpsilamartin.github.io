def Sbis(n):
    """Renvoie Sn"""
    S = 42
    v = 42
    for k in range(n):
        # Inv : S = S_n et v = u_n
        v = 15091 * v % 64007
        # Inv : S = S_n et v = u_{n+1}
        S = S + v
        # Inv : S = S_{n+1} et v = u_{n+1}
    return S
