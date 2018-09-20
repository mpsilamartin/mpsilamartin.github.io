def carre(petitcoeur):
    """Renvoie petitcoeur**2
       Précondition : petitcoeur entier ou flottant"""
    ## Très mauvaise idée : petitcoeur = petitcoeur**2
    return petitcoeur**2

def conversion(h,m,s):
    """Convertit la durée h:m:s en s"""
    t = 3600*h+60*m+s
    return t

def somme(a,b):
    """Renvoie a+b
       Précondition : a,b : couples de nombres"""
    a0,a1 = a
    b0,b1 = b
    return a0+b0 , a1+b1

def effet_de_bord(L):
    """Remplace L[0] par 42
       Précondition : L esr une liste non vide"""
    L[0] = 42
    return None # Explicite le fait que la fonction ne renvoie rien
