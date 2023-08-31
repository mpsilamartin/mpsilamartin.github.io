import numpy as np

def remontee(U,B):
    """Résout le système UX = b.
    Préconditions: U triangulaire supérieure
                   b a autant de lignes que U."""
    n, m = B.shape
    X = np.zeros((n, m))
    for k in range(n):
        i = n-1-k
        # Lien avec le tableau : k = n-1-i
        # Invariant X[n-i:] est correct
        s = U[i, i+1:].dot(X[i+1:])
        X[i] = (B[i] - s) / U[i, i]
    return X

U = np.array([[1.,2.,3.],[0.,4.,5.],[0.,0.,6.]])
B = np.array([[24., 2.],[24.,4.],[24.,6.]])
X = remontee(U,B)
U.dot(X)
