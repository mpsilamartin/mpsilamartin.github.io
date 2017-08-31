def calc_b2_horner(a):
    """Renvoie n, représenté en binaire par a"""
    n = int(a[0])
    for c in a[1:]:
        n = int(c) + 2*n
    return n
