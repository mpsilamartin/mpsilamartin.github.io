def unite(a):
    """Chiffre des unités de a
       Précondition : a entier naturel"""
    return a % 10

def effet_de_bord(L):
    L[0] = 42
    return None

# On ne modifie jamais les arguments
# Sauf si c'est demandé.

def dizaine(a):
    """Chiffre des dizaines de a
       Précondition : a entier naturel"""
    s = ( a % 100 ) // 10
    return s
