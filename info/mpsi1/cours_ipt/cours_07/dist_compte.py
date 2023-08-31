def dist_compte(m,s):
    """Nb d'occurences de m dans s, sans chevauchement"""
    c = 0 # Compteur
    i = 0
    while i <= len(s)-len(m):
        if s[i:i+len(m)] == m :
            i = i+len(m)
            c = c+1
        else :
            i = i+1
    return c

s = "aaaaaaaa"
m = "aa"
