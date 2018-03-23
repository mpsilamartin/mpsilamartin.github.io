import numpy as np

U = np.array([1,2,3])
B = np.array([[2],[-3],[4]])
print("U =\n",U)
print("B =\n",B)
print("U.B =\n",U.dot(B))

N = np.zeros(shape = (3,2))
print("Matrice nulle 3x2 :\n",N)

M = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print("M = \n",M)
print("Première ligne de M :",M[0])
print("Coefficient 0,1 de M :",M[0,1])
print("Première ligne de M :",M[0,:])
print("Première colonne de M :",M[:,0])
print("Première ligne de M (matrice) :",M[[0],:])
print("Première colonne de M (matrice) :",M[:,[0]])

# Attention, M est à coefficients entiers !
M[2,:] = .5 * M[2,:]
print(M)
