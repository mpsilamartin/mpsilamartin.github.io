from math import sqrt

u = 1
n = 1

while u < 1000:
    n = n+1
    u = u + 1 / sqrt(n)

def verif(n):
    """somme des 1 / sqrt(k) pour 1 <= k <=n"""
    s = 0
    for k in range(1,n+1):
        s = s + 1/sqrt(k)
    return s 
