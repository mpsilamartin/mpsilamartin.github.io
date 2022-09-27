def appartient_dicho(e,t):
    """Renvoie un booléen indiquant si e est dans t
    Préconditions : t est un tableau de nombres trié par ordre croissant
    e est un nombre"""
    g = 0 # Limite gauche de la tranche où l'on recherche e
    d = len(t)-1 # Limite droite de la tranche où l'on recherche e
    k=0
    while g < d: # La tranche où l'on cherche e n'est pas vide
        print(d-g,(len(t)-1)//2**k,k)
        m = (g+d)//2 # Milieu de la tranche où l'on recherche e
        pivot = t[m]
        k+=1
        if e == pivot: # On a trouvé e
            return True
        elif e < pivot:
            d = m-1 # On recherche e dans la partie gauche de la tranche
        else:
            g = m+1 # On recherche e dans la partie droite de la tranche
    return False

t=[1,3,9,10,15,17,29,31]
e=10
