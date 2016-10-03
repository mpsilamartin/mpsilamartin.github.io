def est_premier(n):
    """Teste si n est premier"""
    b = True
    for d in range(2,n):
        if n % d == 0 :
            b = False
    return b


def est_premier_bis(n):
    """Teste si n est premier"""
    for d in range(2,n):
        if n % d == 0 :
            return False
    return True
