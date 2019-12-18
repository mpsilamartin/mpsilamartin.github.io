# https://en.wikipedia.org/wiki/Linear_congruential_generator
# MMIX by Donald Knuth

m=2**64
a=6364136223846793005
c=1442695040888963407

def next(x):
    return (a*x+c) % m

def conv(x, n):
    return int((x*n) // m) # on reconvertit en "petit" entier si possible

def cree_tableau(alpha):
    x = alpha
    x = next(x)
    x = next(x)
    n = 1000 + conv(x, 1000)
    t = [0] * n
    for i in range(n):
      x = next(x)
      t[i] = conv(x, 5000)
    return t

