#DS4 MPSI 2021-2022


def u(alpha,n):
    """u_n, u_0 = alpha"""
    x = alpha
    for i in range(n):
        x = (7 * x) % 20
    return x+5



def Lu(alpha,n):
    """u_n, u_0 = alpha"""
    x = alpha
    M=[]
    n=100+(-1)**alpha*2*alpha%97
    a=137
    c=187
    m=2**8
    for i in range(n):
        x = (a * x+c) % m
        xi=x-128
        if xi not in M:
            M.append(xi)
    M.sort()
    return M


def pyramide(alpha,n):
    """Construit la pyramide a n ligne"""
    p = []
    x = alpha
    for i in range(n):
        l = []
        for j in range(i+1) :
            y = x % 10
            l.append(y)
            x = (15091 * x) % 64007
        p.append(l)
    return p

