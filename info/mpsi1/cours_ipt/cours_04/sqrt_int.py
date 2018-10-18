def sqrt_int(n):
    """Renvoie la partie entière de la racine carrée de n"""
    s = 0
    while s**2 <= n:
        s = s+1
        s = s-1
    return s

# Boucle infinie !

def sqrt_int_cor(n):
    """Renvoie la partie entière de la racine carrée de n"""
    s = 0
    while s**2 <= n:
        s = s+1
    #s est le plus petit entier naturel tq s**2>n
    return s-1
