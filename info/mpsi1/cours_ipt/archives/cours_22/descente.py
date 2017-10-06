from remontee import *

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

def echange_lignes(A, i, j):
  """Échange les lignes i et j de la matrice,
  représentée comme liste de lignes de type array
  Attention : modifie A"""
  # on COPIE les éléments de la ligne j :
  t = A[j,:].copy()
  # avant de l'écraser:
  A[j,:] = A[i,:]
  A[i,:] = t
  return None

def descente(A, b):
  """Applique la méthode du pivot pour résoudre Ax = b.
  Pratique uniquement la phase de descente.
  Précondition : A et b sont de type array,
  A est inversible, b a même nombre de lignes que A.
  Attention: cette fonction modifie A et b."""
  n = len(A)
  for i in range(n):
    j = cherche_pivot(A, i)
    # on met en place la ligne du pivot :
    echange_lignes(A, i, j)
    echange_lignes(b, i, j)
    p = A[i, i] # le pivot
    for j in range(i+1, n):
      b[j,:] -= (A[j,i] / p) * b[i,:]
      A[j,:] -= (A[j,i] / p) * A[i,:]
  return None

A = np.array([[8., 5., 8.],
         [4., 5., 2.],
         [4., 3., 2.]])
Ac = np.array([[8., 5., 8.],
         [4., 5., 2.],
         [4., 3., 2.]])
b = np.array([[1.],[2.],[3.]])
bc = np.array([[1.],[2.],[3.]])

descente(Ac,bc)
X = remontee(Ac,bc)
A.dot(X)

C = np.array([[1.,-1.],[2.,5.],[3.,42.]])
Cc = np.array([[1.,-1.],[2.,5.],[3.,42.]])
Ac = np.array([[8., 5., 8.],
         [4., 5., 2.],
         [4., 3., 2.]])
descente(Ac,Cc)
Y = remontee(Ac,Cc)
A.dot(Y)
