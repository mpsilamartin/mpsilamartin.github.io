# -*- coding: utf-8 -*-
# lignes

# finlignes

# cherche
def cherche_pivot(A, i):
  """Cherche et retourne un j tel que
  abs(A[j][i]) est maximal, avec j>=i"""
  n = len(A)
  best = i
  for j in range(i+1, n):
    # invariant: pour tout k <= j
    # abs(A[best][i]) >= abs(A[k][i])
    if abs(A[j,i]) > abs(A[best,i]):
      best = j
  return best
# fincherche

# utils
from numpy import array, zeros

def matrice(m):
  """Construit une matrice à partir
  d'une liste de listes donnée en argument."""
  return array(m)

def mat_nulle(p, q):
  """Retourne, la matrice nulle de dimension p * q
  sous forme de tableau (array)."""
  return zeros(shape=(p, q))
# finutils

# echange
def echange_lignes(A, i, j):
  """Échange les lignes i et j de la matrice,
  représentée comme liste de lignes de type array"""
  # on COPIE les éléments de la ligne j :
  t = A[j,:].copy()
  # avant de l'écraser:
  A[j,:] = A[i,:]
  A[i,:] = t
# finechange

#  return [ligne_nulle(q) for i in range(p)]

A1 = matrice([[10., 7., 2.], [0., 2., 3.], [0., 0., 5.]])
b1 = matrice([[1., 0.], [0., 0.], [0., 1.]])

A2 = matrice([[0., 3.], [2., 0.]])
b2 = matrice([[7.], [5.]])

# resouttriang
def resout_triang_sup(U,B):
  """Résout le système Ax = b.
  Préconditions: A triangulaire supérieure
  et b a autant de lignes que A."""
  n, m = B.shape
  p, q = U.shape
  assert p == q == n
  X = zeros((n, m))
  for i in range(n-1, -1, -1):
    s = U[i, i+1:].dot(X[i+1:])
    X[i] = (B[i] - s) / U[i, i]
  return X

# finresouttriang

# resoutpivot
def resout(A, b):
  """Applique la méthode du pivot pour résoudre Ax = b.
  Retourne la solution x trouvée.
  Précondition : A et b sont de type array,
  A est inversible, b a même nombre de lignes que A.
  Attention: cette fonction modifie A et b."""
  n = len(A)
  q = len(b)
  A = A.copy()
  b = b.copy()
# milieupivot
  for i in range(n):
    j = cherche_pivot(A, i)
    # on met en place la ligne du pivot :
    echange_lignes(A, i, j)
    echange_lignes(b, i, j)

    p = A[i, i] # le pivot
    for j in range(i+1, n):
      b[j,:] -= A[j,i] / p * b[i,:]
      A[j,:] -= A[j,i] / p * A[i,:]
  return resout_triang_sup(A, b)
# finresoutpivot

# hilbert
n = 5
M = matrice([[ 1/(i+j+1.) for j in range(n)]
               for i in range(n)])
u0 = matrice([[-0.76785474],
       [-0.44579106],
       [-0.32157829],
       [-0.25343894],
       [-0.20982264]])
s0 = resout(M, u0)
u1 = matrice([[-0.76784856],
       [-0.44590775],
       [-0.32107213],
       [-0.25420613],
       [-0.20944639]])
s1 = resout(M, u1)
# finhilbert


