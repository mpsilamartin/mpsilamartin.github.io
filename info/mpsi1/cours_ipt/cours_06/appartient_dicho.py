def appartient_dico(t,e):
    """Renvoie la valeur de vérité de 'e in t'
    Préconditions : t tableau de nombre trié par ordre
    croissant
    e est un nombre"""
    g,d = 0,len(t)-1
    while g <= d :
        # Tant que la tranche de recherche n'est pas vide
        # Inv : si e in t, t[g] <= e <= t[d]
        # Var : d-g (longueur de la tranche de recherche)
        p = (g+d) // 2
        # 2g <= g+d <= 2d donc g <= p <= d
        if t[p] == e :
            return True
        elif t[p] > e :
            # On recherche dans la tranche de gauche
            d = p-1
        else :
            # On recherche dans la tranche de droite
            g = p+1
    return False

t = [i**2 for i in range(20)]
