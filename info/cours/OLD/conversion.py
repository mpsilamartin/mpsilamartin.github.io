# -*- coding: utf-8 -*-

## importation des modules
import numpy as np
from representation_binaire import show_float
from numpy import pi

## déclaration des fonctions
def int2bin(n):
    return "{:b}".format(n)

def nb2sme(x):
    if x < 0:
        s = 1
        x *= -1
    else:
        s = 0
    # x est positif
    e = 0
    if x >= 2:
        while x >= 2:
            x /= 2
            e += 1
    elif x < 1:
        while x < 1:
            x *= 2
            e -= 1
    # x est compris entre 1 inclus et 2 exclu
    return s, x, e


## programme principal

# affiche dans la console le contenu mémoire correspondant au nombre
# pi au format simple précision ("e" pour demi-précision, "d" pour double
# précision)
show_float("f", np.float32(pi))
s, m, e = nb2sme(np.float32(pi))
quatre_octets = int2bin(s) + int2bin(e+127) + int2bin(int(m*2**23))[1:]
print(quatre_octets)

x = 1e-3
show_float("f", np.float32(x))
s, m, e = nb2sme(np.float32(x))
s = int2bin(s)
e = int2bin(e+127)
e = '0'*(8 - len(e)) + e
m = int2bin(int(m*2**23))[1:]
quatre_octets = s + e + m
print(quatre_octets)

