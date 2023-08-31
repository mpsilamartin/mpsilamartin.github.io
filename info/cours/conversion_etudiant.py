# -*- coding: utf-8 -*-

## importation des modules
import numpy as np
from representation_binaire import show_float
from numpy import pi

## déclaration des fonctions
def int2bin(n):
    return "{:b}".format(n)

## programme principal

# affiche dans la console le contenu mémoire correspondant au nombre
# pi au format simple précision ("e" pour demi-précision, "d" pour double
# précision)
show_float("f", np.float32(pi))

