import matplotlib.pyplot as plt
import numpy as np
import math as m

# Premier exemple

plt.clf()
x = [0,1,2,5]
y = [-1,4,2,5]
plt.plot(x,y)
plt.savefig("ex_plot_1.png")

# Second exemple

plt.clf()
x = [0,1,2,5,42] # x de longueur 5
y = [-1,4,2,5] # y de longueur 4
# plt.plot(x,y) # erreur produite : longueurs différentes

# Troisième exemple

plt.clf()
x1 = [0,1,2,5]
y1 = [-1,4,2,5]
x2 = [1,5]
y2 = [5,1]
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.savefig("ex_plot_2.png")

#Quatrième exemple

plt.clf()
x = [0,1,1,2,5]
y = [0,-1,4,2,5]
plt.plot(x,y)
plt.savefig("ex_plot_3.png")

# Cinquième exemple

plt.clf()
x1 = [0,1,2,5]
y1 = [-1,4,2,5]
x2 = [1,5]
y2 = [5,1]
plt.plot(x1,y1,marker='*',linestyle='--',color='r')
plt.plot(x2,y2,marker='x',linestyle='-.',color='m')
plt.savefig("ex_plot_4.png")

# Exemple de tracé de fonction n°1 :

plt.clf()
x = np.linspace(-3,3,10)
y = [m.atan(t) for t in x]
plt.plot(x,y)
plt.savefig('ex_plot_5.png')


# Exemple de tracé de fonction n°2 :

plt.clf()
x = np.linspace(-3,3,100)
y = [m.atan(t) for t in x]
plt.plot(x,y)
plt.savefig('ex_plot_6.png')
