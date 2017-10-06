def appartient_drapeau(e,t):
    """Indique si e est dans le tableau t"""
    drapeau = False
    i = 0
    while (not drapeau) and i < len(t):
        if t[i] == e:
            drapeau = True
        i = i+1
    return drapeau

def appartient(e,t):
    """Indique si e est dans le tableau t"""
    for x in t:
        if x == e:
            return True
    return False

def ind_appartient(e,t):
    """Indice d'une occurence de e dans t"""
    for i in range(len(t)):
        if t[i] == e:
            return i
    return None

t = [k**2 for k in range(42)]
