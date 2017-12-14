def nb_motifs_avec_chevauchements(s,m):
    """Nb d'occurences de m dans s, avec chevauchement
    Préconditions : m,s sont des chaînes"""
    Lm, Ls = len(m), len(s)
    n = 0
    for i in range(Ls-Lm+1):
        if s[i:i+Lm] == m:
            n = n+1
    return n

s = "abracadabra"
m = "ra"

def nb_motifs_sans_chevauchements(s,m):
    """Nb d'occurences de m dans s, sans chevauchement
    Préconditions : m,s sont des chaînes"""
    Lm, Ls = len(m), len(s)
    n,i = 0,0
    while i <= Ls-Lm :
        if s[i:i+Lm] == m :
            n = n+1
            i = i+Lm
        else :
            i = i+1
    return n

s1 = "aaaabaa"
m1 = "aa"
