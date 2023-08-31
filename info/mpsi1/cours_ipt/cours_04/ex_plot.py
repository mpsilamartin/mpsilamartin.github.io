import matplotlib.pyplot as plt

# Un premier tracé

plt.clf() # On efface

x = [0,0,1,2,2]
y = [0,2,1,2,0]

plt.plot(x,y)
plt.savefig("ex_plot_1.png")

# En réglant la fenêtre

plt.clf() # On efface

x = [0,0,1,2,2]
y = [0,2,1,2,0]

plt.plot(x,y)
plt.axis([-1,3,-1,3])
plt.savefig("ex_plot_2.png")

# On représente les points

plt.clf() # On efface

x = [0,0,1,2,2]
y = [0,2,1,2,0]

plt.plot(x,y,marker='x')
plt.axis([-1,3,-1,3])
plt.savefig("ex_plot_3.png")

# Pour tracer un nuage de points

plt.clf() # On efface

x = [0,0,1,2,2]
y = [0,2,1,2,0]

plt.plot(x,y,linestyle = '',marker='x')
plt.axis([-1,3,-1,3])
plt.savefig("ex_plot_4.png")

# Pour superposer deux tracés

plt.clf() # On efface

x = [0,0,1,2,2]
y = [0,2,1,2,0]

plt.plot(x,y,linestyle = '',marker='x')
plt.plot([-3,3],[-3,3])
plt.axis([-1,3,-1,3])
plt.savefig("ex_plot_5.png")

# Pour tracer des fonctions ?
# Arc sinus : asin du module math

from math import sin, asin, pi

x = [-1,-.8,-.6,-.4,-.2,0,.2,.4,.6,.8,1]
# x : subdivision du [-1,1] avec 11 pts - 10 segments
y = [asin(t) for t in x]

plt.clf()
plt.plot(x,y)
plt.savefig('ex_asin_1.png')

# Pour créer une subdivision : fonction linspace de la bibliothèque numpy

from numpy import linspace

x = linspace(-1,1,200)
y = [asin(t) for t in x]

plt.clf()
plt.plot(x,y)
plt.savefig('ex_asin_2.png')

# Avec le sinus

plt.clf()

x = linspace(-1,1,200)
y = [asin(t) for t in x]
plt.plot(x,y)

x = linspace(-.5*pi,.5*pi,200)
y = [sin(t) for t in x]
plt.plot(x,y)

plt.savefig('ex_asin_3.png')

# Avec légende, titres etc.

plt.clf()

x = linspace(-1,1,200)
y = [asin(t) for t in x]
plt.plot(x,y,label='Arcsin(t)')

x = linspace(-.5*pi,.5*pi,200)
y = [sin(t) for t in x]
plt.plot(x,y,label='sin(t)')

plt.legend(loc=0)
plt.xlabel('t')
plt.title("Tracés du sinus et de l'arc sinus")
plt.savefig('ex_asin_4.png')