# -*- coding: utf-8 -*-

## importation des modules
import numpy as np

## déclaration des fonctions

## programme principal

# importation des approximations rationnelles de pi
num, den = np.loadtxt(
    "approximation_rationelle_pi.txt",
    dtype = np.uint64,
    delimiter = ";",
    skiprows = 1,
    unpack = True)
