def inverse(a,eps,x0):
    u = x0
    v = u*(2-a*u)
    while abs(u-v) > eps:
        u,v = v, v*(2-a*v)
    return u
