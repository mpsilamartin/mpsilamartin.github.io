def lg(L):
    """Nombre d'éléments de la liste L"""
    compteur = 0
    for x in L:
        # Inv : compteur éléments dans L avant x
        compteur = compteur + 1
    return compteur

t = [4,'a',True]
L = [k ** 2 for k in range(10)]
