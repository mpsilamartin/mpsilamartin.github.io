"""Définit quelques matrices à coefficients aléatoires"""

import numpy as np
import random as rd

def rmatrix(n,p, m):
    '''Renvoie une matrice de dimensions (n,p) avec des coefficients uniformes entre 0 et m'''
    return np.array([[rd.uniform(0,m) for j in range(p)] for i in range(n)])

def rmatrixcarree(n, m):
    '''Renvoie une matrice carrée d'ordre n avec des coefficients uniformes entre 0 et m'''
    return np.array([[rd.uniform(0,m) for j in range(n)] for i in range(n)])

def rmatrixTU(n, m):
    '''Renvoie une matrice carrée d'ordre n, triangulaire supérieure, avec des coefficients uniformes entre 0 et m'''
    return np.array( [ [0]*i+[rd.uniform(0,m) for j in range(i,n)] for i in range(n)] )

def rmatrixTL(n, m):
    '''Renvoie une matrice carrée d'ordre n, triangulaire inférieure, avec des coefficients uniformes entre 0 et m'''
    return np.array( [ [rd.uniform(0,m) for j in range(i+1)]+[0]*(n-i-1) for i in range(n)] )

def rvector(n, m):
    '''Renvoie un vecteur colonne de taille n, avec des coefficients uniformes entre 0 et m'''
    return np.array([[rd.uniform(0,m)] for i in range(n)])


        
