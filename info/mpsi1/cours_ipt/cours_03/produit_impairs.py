def produit_impairs(n):
    """1*3*...*(2n+1)
    Précondition : n entier"""
    p = 1
    # p == 1*3*...*(2k-1) pour k==1
    # (initialisation de l'invariant)
    for k in range(1,n+1):
        # Inv : p == 1*3*...*(2k-1)
        p = p*(2*k+1)
        # Inv : p == 1*3*...*(2k+1)
    # Au dernier tour de boucle k==n
    # Donc p == 1*3*...*(2n+1)
    return p
