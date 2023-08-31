def appartient_dicho(e : int , t : list) -> bool:
    """Renvoie un booléen indiquant si e est
    dans t. Préconditions : t est un tableau
    de nombres trié par ordre croissant e est
    un nombre"""
    # Limite gauche de la tranche où l'on recherche e
    g = 0
    # Limite droite de la tranche où l'on recherche e
    d = len(t)-1
    # La tranche où l'on cherche e n'est pas vide
    while g <= d:
        # Milieu de la tranche où l'on recherche e
        m = (g+d)//2
        pivot = t[m]
        if e == pivot: # On a trouvé e
            return True
        elif e < pivot:
        # On recherche e dans la partie gauche de la tranche
            d = m-1
        else:
        # On recherche e dans la partie droite de la tranche
            g = m+1
    return False

def appartient_dicho_rec(e : int , t : list) -> bool:
    '''
    Cette fonction renvoie un booléen selon que l'élément qu'on cherche est dans le tableau t ou non
    '''
    print(t)
    # Limite gauche de la tranche où l'on recherche e
    g = 0
    # Limite droite de la tranche où l'on recherche e
    d = len(t)-1
    # La tranche où l'on cherche e n'est pas vide
    # Milieu de la tranche où l'on recherche e
    m = (g+d)//2
    if t==[]:#e n'est pas dans t
        return False
    elif t[m]==e:#e est dans t
        return True
    elif t[m]<e:#On recherche à droite
        return appartient_dicho_rec(e, t[m+1:])
    elif t[m]>e:#On recherche à gauche
        return appartient_dicho_rec(e, t[:m])

import random as rd
import numpy as np

L=[np.random.randint(50) for k in range(10)]
L.sort()




