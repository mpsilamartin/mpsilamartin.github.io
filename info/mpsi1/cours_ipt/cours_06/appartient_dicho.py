def appartient_dicho(e,t):
    """Renvoie un booléen indiquant si e est dans t
       Préconditions : t est un tableau de nombres trié par ordre croissant
                       e est un nombre"""
    g = 0 # Limite gauche de la tranche où l'on recherche e
    d = len(t)-1 # Limite droite de la tranche où l'on recherche e
    while g <= d: # La tranche où l'on cherche e n'est pas vide
        m = (g+d)//2 # Milieu de la tranche où l'on recherche e
        pivot = t[m] 
        if e == pivot: # On a trouvé e
            return True
        elif e < pivot: 
            d = m-1 # On recherche e dans la partie gauche de la tranche
        else:
            g = m+1 # On recherche e dans la partie droite de la tranche
    return False

t = [-1,5,10,42,1515]
