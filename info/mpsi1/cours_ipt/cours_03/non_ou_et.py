def neg(b):
    """Négation de b
    Précondition : b booléen"""
    if b :
        return False
    else :
        return True

def ou(a,b):
    """Renvoie a ou b
    Précondition : a,b booléens"""
    if a :
        return True
    elif b :
        return True
    else :
        return False

def et(a,b):
    """Renvoie a et b
    Précondition : a,b booléens"""
    if a :
        if b :
            return True
        else :
            return False
    else :
        return False
        
def et2(a,b):
    """Renvoie a et b
    Précondition : a,b booléens"""
    if a==b==True :
        return True
    else :
        return False
