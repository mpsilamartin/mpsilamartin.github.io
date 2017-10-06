def recherche(m,s):
    """Recherche le mot m dans la chaine s"""
    Ls, Lm = len(s), len(m)
    for i in range(Ls-Lm):
        # Inv : m n'est pas dans s[i:i+Lm-1]
        drapeau = True
        for k in range(Lm):
            # Inv : drapeau ???
            if m[k] != s[i+k]:
                drapeau = False
        # m == s[i:i+Lm] ssi drapeau == True
        if drapeau :
            return True
    return False

def recherche_naif(m,s):
    """Recherche le mot m dans la chaine s"""
    Ls, Lm = len(s), len(m)
    for i in range(Ls-Lm):
        # Inv : m n'est pas dans s[i:i+Lm-1]
        if s[i:i+Lm] == m:
            return True
    return False

s = "Souvent pour s'amuser les hommes d'équipage\nprennent des albatros, vastes oiseaux des mers"

