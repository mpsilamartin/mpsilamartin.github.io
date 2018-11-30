def egalite(a,b):
    """Teste a==b pour deux chaînes a,b
    Précondition : a,b de même longueur"""
    n = len(a)
    for i in range(n):
        if a[i] != b[i]:
            return False
    return True

def recherche(m,s):
    """Recherche le mot m dans la chaîne s"""
    long_s = len(s)
    long_m = len(m)
    for i in range(long_s-long_m+1):
        if egalite(s[i:i+long_m],m):
            return True
    return False

s = "Abracadabra !!!!"
m1 = s
m2 = "bra"
m3 = "gabuzomeu"
