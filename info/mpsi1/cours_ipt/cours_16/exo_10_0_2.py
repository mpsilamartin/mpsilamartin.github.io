from descente import resout

from numpy import array

A = array([[3.,-2.,5.],
           [-4.,1.,1.],
           [2.,3.,-2.]])
           
B = array([[20.,-21.,-12.,6.],
           [-2.,23.,17.,-2.],
           [-7.,-1.,4.,3.]])
           
X = resout(A,B)