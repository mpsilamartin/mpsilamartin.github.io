import matplotlib.pyplot as plt
from numpy import linspace
import math as m 

x = linspace(0,1,200)
y1 = [m.sqrt(t) for t in x]
y2 = [t**2 for t in x]

plt.clf()
plt.plot(x,y1,label="Racine carrée")
plt.plot(x,y2,label="$x^2$")
plt.plot([0,1],[0,1],label="$x$")
plt.xlabel("$x$")
#plt.xlim(-1,2)
#plt.ylim(-1,2)
plt.legend(loc=0)
plt.savefig("plot_puissances.png")



