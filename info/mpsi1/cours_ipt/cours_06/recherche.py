def recherche_naif(s,m):
    """Renvoie la valeur de vérité de 'm in s'
    Préconditions : s,m de type str"""
    ls, lm = len(s), len(m)
    for i in range(ls - lm):
        if s[i:i+lm] == m:
            return True
    return False

s = 'Bonjour tout le monde'

def recherche(s,m):
    """Renvoie la valeur de vérité de 'm in s'
    Préconditions : s,m de type str"""
    ls, lm = len(s), len(m)
    for i in range(ls - lm):
        j = 0
        while j < lm and m[j] == s[i+j]:
            j = j+1
        if j == lm :
            # On a trouvé m
            return True
    return False
