def appartient_dicho(e,t):
    """Indique si e est dans le tableau t
       Précondition : t est un tableau de nombres
       trié par ordre croissant"""
    g , d = 0 , len(t)-1
    # g,d : bornes g/d de la tranche de recherche
    while g <= d:
        # Si e in t : t[g] <= e <= t[d]
        # Variant : d-g
        m = (g+d) // 2
        pivot = t[m]
        if pivot == e:
            return True
        elif pivot < e:
            # On recherche e à droite
            g = m+1
        else :
            # On recherche à gauche
            d = m-1
    return False

t = [k**2 for k in range(100)]
