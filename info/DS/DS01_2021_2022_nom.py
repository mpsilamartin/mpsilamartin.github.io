from math import sqrt, floor, ceil, log

def u(alpha,n):
    """u_n, u_0 = alpha"""
    x = alpha
    for i in range(n):
        x = (15091 * x) % 64007
    return x


