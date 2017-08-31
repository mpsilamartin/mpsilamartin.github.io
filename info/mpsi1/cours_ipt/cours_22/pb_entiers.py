import numpy as np

A = np.array([[8, 5, 8],
         [4, 5, 2],
         [4, 3, 2]])

print("0.5*L0 = ",0.5*A[0,:])
print("L1 - 0.5*L1 =", A[1,:] - 0.5*A[0,:])
print("On effectue cela")
A[1,:] = A[1,:] - 0.5*A[0,:]
print("A = ",A)

