import matplotlib.pyplot as plt

def euler(F, a, b, y0, h):
    """Solution de y'=F(y,t) sur [a,b], y(a) = y0, pas h"""
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

def f4(y,t):
    return t-y**2

t4,y4=euler(f4, 0, 10, 1, 0.01)

plt.clf()

plt.plot(t4,y4)

#plt.show()


from numpy import array
v = array([1.,2.])
v
array([ 1., 2.])
w = array([-5,2.5])
v + 3*w
array([-14. , 9.5])


def F(X,t):
    y,yp=X
    ypp=-2*yp-y+5
    return array([yp,ypp])
