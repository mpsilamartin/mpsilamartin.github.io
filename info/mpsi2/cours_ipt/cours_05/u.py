def u(n):
    """u_n, u_0=5 et u_k+1 = 2*(u_k)-k-3"""
    a = 5 # a = u(0)
    for i in range(n):
        # Inv : a = u(i)
        a = 2*a-i-3
        # Inv : a = u(i+1)
    # Au dernier tour de boucle, i=n-1, donc a = u(n)
    return a
