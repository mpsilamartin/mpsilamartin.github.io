import matplotlib.pyplot as plt
from numpy import sin, cos, pi

n = 1000
x = [k*4*pi/n for k in range(n+1)]
s = [sin(t) for t in x]
c = [cos(t) for t in x]

plt.clf()
plt.plot(x,s,'-b',label='sin(x)')
plt.plot(x,c,'--r',label='cos(x)')
plt.xlabel('x')
plt.ylabel('Ordonnées')
plt.title('Fonctions sinus et cosinus')
plt.axis([0,4*pi,-1,1])
plt.legend()
plt.savefig('tp05_ex_complet.png')
plt.show()
