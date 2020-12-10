import matplotlib.pyplot as plt
import numpy as np
def euler(F, a, b, y0, h):
    """Solution de y’=F(y,t) sur [a,b], y(a) = y0, pas h"""
    y = y0
    t = a
    y_list = [y0] # la liste des valeurs renvoyées
    t_list = [a] # la liste des temps
    while t+h <= b:
    # Variant : floor((b-t)/h)
    # Invariant : au tour k, y_list = [y_0,...,y_k], t_list = [t_0,...,t_k]
        y = y + h * F(y, t)
        y_list.append(y)
        t = t + h
        t_list.append(t)
    return t_list, y_list

def F(y,t):
    return y


t1,y1=euler(F, 0, 3, 1, 1)
t2,y2=euler(F, 0, 3, 1, 1/10)
t3,y3=euler(F, 0, 3, 1, 3/100)

# plt.clf()
# plt.plot(np.linspace(0,3,1000),np.exp(np.linspace(0,3,1000)),label='Exponentielle',linewidth=3)
# plt.plot(t1,y1,'g--',label='h=1',linewidth=2)
# plt.plot(t2,y2,'k-.',label='h=1/10',linewidth=2)
# plt.plot(t3,y3,'r:',label='h=3/100',linewidth=2)
# plt.legend(loc='best')
# plt.axis([0,3,0,20])
# plt.show()


y0 = 1 # m
yp0 = 0 # m * s**-1
t0, t1, h = 0, 20, .01 # s
m = 250 # kg
c = 100 # kg * s**-1
k = 1000 # kg * s**-2
def F(X,t) :
    y,yp = X
    ypp = -(k*y + c*yp)/m
    return array([yp,ypp])
X0 = array([y0,yp0])
t_list, X_list = euler(F,t0,t1,X0,h)

y_list = [X[0] for X in X_list]
yp_list = [X[1] for X in X_list]