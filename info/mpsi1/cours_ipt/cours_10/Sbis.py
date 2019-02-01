def Sbis(n):
    """Renvoie S_n"""
    S = 42
    v = 42
    # Inv : v = v_0, S = S_0
    for k in range(n):
        # Inv : v = v_k et S = S_k
        v = 15091 * v % 64007
        # Inv : v = v_k+1 et S = S_k
        S = S +v
        # Inv : v = v_k+1 et S = S_k+1
    # Au dernier tout, k = n-1 donc S = S_n
    return S

# Chaque tour s'effectue en temps O(1).
# n tours de boucle : la boucle s'effectue en temps O(n)
# En dehors : 2 opérations en temps constant.
# Complexité totale : O(n) + O(1) = O(n).
