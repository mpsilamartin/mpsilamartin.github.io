from descente import resout
from numpy import array, eye

A = array([[5.,-3.,2.,1.,-1.],
           [3.,6.,8.,1.,-3.],
           [5.,6.,3.,0.,2.],
           [4.,6.,2.,8.,3.],
           [-6.,3.,5.,-1.,-2.]])

I = eye(5)

Ainv = resout(A,I)
