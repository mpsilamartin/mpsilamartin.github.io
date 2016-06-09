import matplotlib.pyplot as plt
from numpy import sin

n = 20
x = [k*10/n for k in range(n)]
y = [sin(t) for t in x]

plt.clf()
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()
