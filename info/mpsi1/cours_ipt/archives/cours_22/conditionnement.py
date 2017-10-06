from descente import *
from remontee import *

n = 5
M = np.array([[ 1/(i+j+1.) for j in range(n)]
               for i in range(n)])
u0 = np.array([[-0.76785474],
       [-0.44579106],
       [-0.32157829],
       [-0.25343894],
       [-0.20982264]])

Mc, u0c = M.copy(), u0.copy()
descente(Mc,u0c)
s0 = remontee(Mc,u0c)

u1 = np.array([[-0.76784856],
       [-0.44590775],
       [-0.32107213],
       [-0.25420613],
       [-0.20944639]])

Mc, u1c = M.copy(), u1.copy()
descente(Mc,u1c)
s1 = remontee(Mc,u1c)

