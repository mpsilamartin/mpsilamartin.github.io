def moyenne(t):
    """moyenne de t
    Préconditions : t tableau non vide de nombres"""
    n = len(t)
    S = 0
    for k in range(n):
        S = S+t[k]
    return S / n

def moyenne_bis(t):
    """moyenne de t
    Préconditions : t tableau non vide de nombres"""
    n = len(t)
    S = 0
    for x in t :
        S = S+x
    return S / n

def moyenne_ter(t):
    """moyenne de t
    Préconditions : t tableau non vide de nombres"""
    n = 0
    S = 0
    for x in t :
        S = S+x
        n = n+1
    return S / n

def variance(t) :
    """Variance de t
    Préconditions : t tableau non vide de nombres"""
    n = len(t)
    S = 0 # Somme des éléments de t
    Sc = 0 # Somme des carrés
    for i in range(n) :
        S = S + t[i]
        Sc = Sc + t[i]**2
    return (Sc / n) + (S / n)**2

