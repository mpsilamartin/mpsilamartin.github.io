def calc_b2_tresnaif(a):
    """Renvoie n, représenté en binaire par a"""
    n = 0
    for i in range(len(a)):
        n = n + int(a[len(a)-i-1])*(2**i)
    return n

def calc_b2_naif(a):
    """Renvoie n, représenté en binaire par a"""
    n = 0
    x = 1
    for i in range(len(a)):
        n = n + int(a[len(a)-i-1])*x
        x = 2*x
    return n
