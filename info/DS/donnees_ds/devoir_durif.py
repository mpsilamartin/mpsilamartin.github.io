with open('mesure_accelero_1.txt','r',encoding='utf8') as f:
    data=f.readlines()
    dt,ax,ay,az=[],[],[],[]
    for ligne in data:
        ligne=ligne.split(',')
        dt.append(float(ligne[0]))
        ax.append(float(ligne[1]))
        ay.append(float(ligne[2]))
        az.append(float(ligne[3]))

t=[0]
for dt1 in dt[1:]:
    t.append((t[-1]+dt1*1e-6))


import matplotlib.pyplot as plt



plt.clf()
plt.plot(t,ax)
plt.plot(t,ay)
plt.plot(t,az)