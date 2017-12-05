def compte(t,e):
    """Nombre d'occurences de e dans t
    Précondition : t tableau"""
    n = len(t)
    N = 0 # nb d'occurences de e
    for i in range(n):
        if t[i]  == e :
            N = N + 1
    return N

t = [42,0,8,5,0,3,7,0]

def compte_bis(t,e):
    """Nombre d'occurences de e dans t
    Précondition : t tableau"""
    N = 0 # nb d'occurences de e
    for x in t:
        if x == e :
            N = N + 1
    return N
