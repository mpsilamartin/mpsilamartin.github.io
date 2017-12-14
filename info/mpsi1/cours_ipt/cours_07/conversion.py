def conv_b2(p):
    """Écrit p en base """
    s = ''
    x = p
    while x > 1 :
        s = str(x%2) + s
        x = x // 2
    return str(x) + s

def calc_b2_tresnaif(s):
    n = len(s)
    p = 0
    for i in range(n):
        p = p + int(s[n-1-i])*2**i
    return p

def calc_b2_naif(s):
    n = len(s)
    p = 0
    e = 1 # 2**0
    for i in range(n):
        # Inv : e = 2**i
        p = p + int(s[n-1-i])*e
        e = 2*e
    return p

def calc_b2_horner(s):
    n = len(s)
    p = int(s[0])
    for i in range(1,n):
        p = 2*p + int(s[i])
    return p
