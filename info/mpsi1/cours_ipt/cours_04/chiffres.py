import math  

def base10(n):
    """Renvoie le nombre de chiffres de n
    Précondition : n entier naturel"""
    m = 0
    while m <= math.log10(n):
        m = m+1
    print(m)

## Deux problèmes :
    # la fonction renvoie None
    # on utilise des flottants

# Correction

def nb_chiffres(n):
    """Renvoie le nombre de chiffres de n
    Précondition : n entier naturel non nul"""
    k = 0
    while 10**k <= n:
        k = k+1
    return k

# Pb : on calcule 10**k à nouveau depuis le début

def nb_chiffres2(n):
    """Renvoie le nombre de chiffres de n
    Précondition : n entier naturel non nul"""
    k = 0
    p = 1
    # Inv : p = 10**k
    while p <= n:
        # Inv : p = 10**k
        # Variant : n-p
        p = p*10
        k = k+1
    # p = 10**k et p > n et p/10 <= n
    return k

# Et pour les entiers négatifs ?

def nb_chiffres3(n):
    """Renvoie le nombre de chiffres de n
    Précondition : n entier naturel non nul"""
    if n == 0 :
        return 1
    elif n < 0 :
        m = -n
    else :
        m = n
    k = 0
    p = 1
    while p <= m:
        p = p*10
        k = k+1
    return k
