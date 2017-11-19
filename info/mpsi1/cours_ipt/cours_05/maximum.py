def maximum(t):
    """Maximum de t
    Préconditions : t tableau non vide de nombres"""
    M = t[0]
    n = len(t)
    for i in range(1,n):
        # Inv : M = max(t[:i])
        if t[i] > M :
            M = t[i]
    return M

def maximum_bis(t):
    """Maximum de t
    Préconditions : t tableau non vide de nombres"""
    M = t[0]
    n = len(t)
    for x in t[1:]:
        # Inv : M = max(????)
        if x > M :
            M = x
    return M

t = [-1,3,42,0]

def indice_maximum(t):
    """Un indice du maximum de t
    Préconditions : t tableau non vide de nombres"""
    iM = 0 
    n = len(t)
    for i in range(1,n) :
        # Inv : t[iM] = max(t[:i])
        if t[i] > t[iM] :
            iM = i
    return iM

