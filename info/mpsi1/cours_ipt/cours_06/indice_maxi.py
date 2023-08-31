def maxi(t):
    """Maximum du tableau t
       Précondition : t tableau de nombres non vide"""
    m = t[0] # Maximum de la tranche déjà inspectée
    for x in t:
        if x > m:
            m = x
    return m

def maxi2(t):
    """Maximum du tableau t
       Précondition : t tableau de nombres non vide"""
    n = len(t)
    m = t[0] # Maximum de la tranche déjà inspectée
    for i in range(n):
        if t[i] > m:
            m = t[i]
    return m

def indice_maxi(t):
    """indice du maximum du tableau t
       Précondition : t tableau de nombres non vide"""
    n = len(t)
    im = 0 # Indice du maximum de la tranche déjà inspectée
    for i in range(n):
        if t[i] > t[im]: # Renvoie la première occurence
            im = i
    return im

t = [-1,0,42,1,42,3,42,5]






