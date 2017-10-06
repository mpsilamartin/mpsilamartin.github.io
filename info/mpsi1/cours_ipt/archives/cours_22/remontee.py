import numpy as np

def remontee(U,B):
  """Résout le système UX = b.
  Préconditions: U triangulaire supérieure
  et b a autant de lignes que U."""
  n, q = B.shape # On résout q systèmes
  X = np.zeros((n, q))
  for k in range(n-1, -1, -1):
    # Invariant X[k+1:] est correct
    s = U[k, k+1:].dot(X[k+1:])
    X[k] = (B[k] - s) / U[k, k]
  return X

U = np.array([[1.,2.,3.],[0.,4.,5.],[0.,0.,6.]])
B = np.array([[24., 2.],[24.,4.],[24.,6.]])
X = remontee(U,B)
U.dot(X)
