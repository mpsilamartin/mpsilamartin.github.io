def liste_imax(t):
    """Liste des indices où le max de t est atteint
    Précondition : t tableau de nombres"""
    m = t[0]
    L = [0]
    for k in range(1,len(t)):
        if t[k] == m :
            L.append(k)
        elif t[k] >  m :
            m = t[k]
            L = [k]
    return L

t = [4,3,2,1,0]
tbis = [0,42,5,8,42,-1,3,5,42]
