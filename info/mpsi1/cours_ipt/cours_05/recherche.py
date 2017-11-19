def appartient(t,e):
    """Renvoie la valeur de vérité de e in t"""
    n = len(t)
    for i in range(n):
        if t[i] == e :
            return True
    return False

def appartient_bis(t,e):
    """Renvoie la valeur de vérité de e in t"""
    n = len(t)
    drapeau = False
    for i in range(n):
        if t[i] == e :
            drapeau = True
    return drapeau
