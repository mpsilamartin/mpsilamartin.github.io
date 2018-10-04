def somme(n):
    """1+2+...+n"""
    s = 0
    # Inv : s == 1+2+...+(k-1) avec k==1
    for k in range(1,n+1):
        # Inv : s == 1+2+...+(k-1)
        s = s + k
        # Inv : s == 1+2+...+k
    # Au dernier tour, k == n
    # donc s == 1+2+...+n
    return s

# Écrire une fonction depasse(M) renvoyant
# le plus petit n tq somme(n) >= M

def depasse1(M):
    """Plus petit n tq somme(n) >=M
    Précondition : M nombre"""
    S,n = 0,0
    # S == 1+...+n pour n == 0
    while S < M:
        # On a S < M
        #Inv : S = 1+2+...+n
        # Variant : floor(M)-S
        n = n+1
        #Inv : S = 1+2+...+n-1
        S = somme(n)
        # S = 1+2+..+n
    # On a bien S >= M, au tour précédent S<M
    #Inv : S = 1+2+...+n
    return n

# Attention : on recalcule à chaque fois entièrement 1+2+...+n
# Cela donne une complexité très mauvaise, de l'ordre de n**2

def depasse2(M):
    """Plus petit n tq somme(n) >=M
    Précondition : M nombre"""
    S,n = 0,0
    # S == 1+...+n pour n == 0
    while S < M:
        # Inv : S == 1+...+n
        n = n+1
        # Inv : S == 1+...+n-1
        S = S + n
        # Inv : S == 1+...+n
    # S >=M, au tour précédent S<M
    # Inv : S == 1+...+n
    return n
        

# Une autre boucle :

def exemple():
 
    while a > 0:
        a = a+1
