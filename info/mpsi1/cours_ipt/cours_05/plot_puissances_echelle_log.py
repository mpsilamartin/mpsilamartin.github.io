import matplotlib.pyplot as plt
from numpy import linspace
import math as m 

x = linspace(0,5,200)
y1 = [m.sqrt(10**t) for t in x]
y2 = [(10**t)**2 for t in x]
y3 = [10**t for t in x]

plt.clf()
plt.plot(y3,y1,label="Racine carrée")
plt.plot(y3,y2,label="$x^2$")
plt.plot(y3,y3,label="$x$")
plt.xlabel("$x$")
plt.xscale("log")
plt.yscale("log")
plt.legend(loc=0)
plt.savefig("plot_puissances_echelle_log.png")



