import matplotlib.pyplot as plt

plt.clf()
x = [4,1,6,8]
y = [0,2,-1,5]
plt.plot(x,y)
plt.savefig("ex_1.png")


plt.clf()
x = [4,1,6,8]
y = [0,2,-1,5]
plt.plot(x,y,marker="*")
plt.savefig("ex_2.png")

plt.clf()
x = [4,1,6,8]
y = [0,2,-1,5]
plt.plot(x,y,marker="*",linestyle="")
plt.savefig("ex_3.png")


plt.clf()
x = [4,1,6,8]
y = [0,2,-1,5]
plt.plot(x,y,marker="*",linestyle="",markersize=10)
plt.axis([0,9,-2,6])
plt.savefig("ex_4.png")


plt.clf()
x = [4,1,6,8]
y = [0,2,-1,5]
plt.plot(x,y,marker="*",linestyle="",markersize=10)
plt.plot([1,8],[-1,5],linestyle=":",color="r")
plt.axis([0,9,-2,6])
plt.savefig("ex_5.png")

# Pour tracer le graphe d'une fonction
# Ex : Arcsin (asin de la bib. math)

from math import asin

x = [-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1]
y = [asin(t) for t in x]

plt.clf()
plt.plot(x,y)
plt.savefig("ex_asin_1.png")

def subdivision(a,b,p):
    """Subdivision de [a,b] de pas p"""
    L = [a]
    x = a
    while x+p <= b:
        x = x+p
        L.append(x)
    return L

x = subdivision(-1,1,0.01)
y = [asin(t) for t in x]

plt.clf()
plt.plot(x,y)
plt.savefig("ex_asin_2.png")

from numpy import linspace

x = linspace(-1,1,1000)
y = [asin(t) for t in x]

plt.clf()
plt.plot(x,y)
plt.savefig("ex_asin_3.png")


plt.clf()
plt.plot(x,y,label="Arcsin(t)")
plt.xlabel("t")
plt.legend()
plt.savefig("ex_asin_4.png")


