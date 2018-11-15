import matplotlib.pyplot as plt
from numpy import linspace
from math import atan

x = linspace(-10,10,100)
y = [atan(t) for t in x]

plt.clf()
plt.plot(x,y)
plt.title("Tracé de l'arctangente sur [-10,10]")
plt.savefig("plot_arctan.png")

