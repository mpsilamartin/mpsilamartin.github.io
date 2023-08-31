def compte(m,s):
    """Nb d'occurences de m dans s, avec chevauchement"""
    c = 0 # Compteur
    for i in range(len(s)-len(m)+1):
        if s[i:i+len(m)] == m:
            c = c+1
    return c

s = "aaaaaaaa"
m = "aa"
