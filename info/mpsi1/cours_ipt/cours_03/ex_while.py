def somme(n):
    """1+2+...+n"""
    s = 0
    for k in range(n+1):
        s = s + k
    return s

def depasse1(M):
    """Plus petit n tq 1+2+...+n >= M"""
    n = 0
    s = somme(n)
    while s < M:
        n = n+1
        s = somme(n)
    return n
    

def depasse2(M):
    """Plus petit n tq 1+2+...+n >= M"""
    n = 0
    s = 0
    while s < M : 
        n = n+1
        s = s + n
    return n

def boucle_infinie():
    n = 2
    while n > 1 :
        n = n +2
    return n
