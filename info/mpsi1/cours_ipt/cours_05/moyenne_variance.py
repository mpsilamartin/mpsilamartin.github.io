def moyenne_variance(t):
    """Renvoie moyenne et variance de t
       Précondition : t tableau de nombres non vide"""
    S = 0 # Somme des éléments de t
    Sc = 0 # Somme des carrés des éléments de t
    for x in t :
        S = S + x
        Sc = Sc + x**2
    m = S / len(t) # Moyenne de t
    v = Sc / len(t) - m**2 # Variance de t
    return m,v

def moyenne_variance_invariant(t):
    """Renvoie moyenne et variance de t
       Précondition : t tableau de nombres non vide"""
    S = 0 # Somme des éléments de t
    Sc = 0 # Somme des carrés des éléments de t
    n = len(t)
    for i in range(n) :
        # Inv : S = t[0]+...+t[i-1]
        S = S + t[i]
        Sc = Sc + t[i]**2
    m = S / n # Moyenne de t
    v = Sc / n - m**2 # Variance de t
    return m,v
