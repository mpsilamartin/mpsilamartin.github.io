def appartient(e,t):
    """Renvoie "e in t"
    Préconditions : t tableau"""
    for x in t :
        if x==e:
            return True
        # Surtout pas de else !
    return False

t = [42,0,1515,[],True]

def appartient2(e,t):
    """Renvoie "e in t"
    Préconditions : t tableau"""
    drapeau = False
    for x in t :
        if x==e:
            drapeau = True # On lève le drapeau
        # Surtout pas de else !
    return drapeau
