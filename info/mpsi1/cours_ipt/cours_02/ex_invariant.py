def valeur_u(N):
    """Renvoie u_N, u_0 = 5, u_{k+1} = 2u_k-k-5
    Précondition : n entier naturel"""
    u = 5
    # Inv : u == u_0
    for k in range(N):
        # Inv : u == u_k
        u = 2*u - (k) - 5
        # Inv : u == u_{k+1}
    # Au dernier tour, k == N-1
    # Donc en sortie, u == u_{N-1+1}
    return u
