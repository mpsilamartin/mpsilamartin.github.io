import numpy as np
from descente import *
from remontee import *

def inverse(M):
    """Calcule l'inverse de M par le pivot de Gauss
    Précondition : M est carrée"""
    n,_ = M.shape
    Mc = M.copy()
    b = np.eye(n)
    descente(Mc,b)
    return remontee(Mc,b)


M1 = np.array([[4. ,-1.,1.], 
               [4. ,1. ,3.],
               [-1.,0. ,0.]])
N1 = inverse(M1)
M2 = np.array([[9, 2, 9], 
               [5, 5, 8], 
               [6, 3, 0]])
N2 = inverse(M2)
# Attention : M2 est à coefficients entiers
