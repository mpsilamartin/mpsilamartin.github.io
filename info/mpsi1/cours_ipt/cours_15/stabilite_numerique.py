import numpy as np

A = np.array([[1,1, 1],
              [1,10**(-17), 0], 
              [1, 0, 0]])
print("A = \n",A)
A[1,:] = A[1,:] - A[0,:]
A[2,:] = A[2,:] - A[0,:]
print("A = \n",A)
# A n'est plus inversible ! 
