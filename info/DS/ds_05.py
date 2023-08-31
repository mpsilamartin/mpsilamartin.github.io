

import numpy as np

import matplotlib.pyplot as plt
fid = open("donnees_ds/mesure_accelero_48.txt",'r')

data = fid.readlines()
fid.close()


def read_data(data):
    DT=[]
    AX=[]
    AY=[]
    AZ=[]
    for ligne in data :
        ligne = ligne.rstrip()
        ligne = ligne.split(",")
        
        DT.append(int(ligne[0]))
        AX.append(int(ligne[1]))
        AY.append(int(ligne[2]))
        AZ.append(int(ligne[3]))
    return DT, AX, AY, AZ
print("NB points de mesure : ",len(data))
dt,ax,ay,az = read_data(data)


def question_2(DT):
    les_temps = [0]
    les_dt = [0]
    tps = 0
    for i in range(1,len(DT)):
        tps=tps + DT[i]/1000000
        les_temps.append(tps)
        les_dt.append(DT[i]/1000000)
    return les_temps
    
les_temps = question_2(dt)
print("Duree de l'essai (s): ",les_temps[-1])

#plt.plot(les_temps)
#plt.show()

def question_3(a):
    les_a = []
    for i in range(len(a)):
        les_a.append(a[i]/255*10)
    return les_a
    ## les_a = [x/255*10 for x in a]
    
les_ax = question_3(ax)
les_ay = question_3(ay)
les_az = question_3(az)
print("Max(ax), Max(ay), Max(az)",max(les_ax),max(les_ay),max(les_az))

# question 4
"""
plt.plot(les_temps,les_ax,".",label="AX")
plt.plot(les_temps,les_ay,".",label="AY")
plt.plot(les_temps,les_az,".",label="AZ")
plt.legend()
plt.show()
"""

#question 5

def question_5(t,x):
    les_int = []
    somme = 0
    for i in range(len(x)-1):
        dt = t[i+1]-t[i]
        int = dt*0.5*(x[i]+x[i+1])
        somme = somme + int
        les_int.append(somme)
    return les_int
    
les_vx = question_5(les_temps,les_ax)
les_vy = question_5(les_temps,les_ay)
les_vz = question_5(les_temps,les_az)
"""
plt.plot(les_temps[:-1],les_vx,label="vx")
plt.plot(les_temps[:-1],les_vy,label="vy")
plt.plot(les_temps[:-1],les_vz,label="vz")
plt.legend()
plt.show()
"""
print("Max(vx), Max(vy), Max(vz)",max(les_vx),max(les_vy),max(les_vz))

# Quesiton 7
def question_7(t,x):
    les_x = []
    i = 0
    while t[i]<2:
        les_x.append(x[i])
        i=i+1
    #plt.plot(x)
    #plt.plot(les_x)
    #plt.show()
    return (sum(les_x)/len(les_x))
ax_moy = question_7(les_temps,les_ax)
ay_moy = question_7(les_temps,les_ay)
az_moy = question_7(les_temps,les_az)

print("moy(ax), moy(ay), moy(az), ",ax_moy,ay_moy,az_moy)
#plt.plot(les_temps,les_ay)
#plt.show()
# Question 8
les_ax = [x-ax_moy for x in les_ax]
les_ay = [x-ay_moy for x in les_ay]
les_az = [x-az_moy for x in les_az]
print("Max(ax), Max(ay), Max(az)",max(les_ax),max(les_ay),max(les_az))
# Question 9
les_vx = question_5(les_temps,les_ax)
les_vy = question_5(les_temps,les_ay)
les_vz = question_5(les_temps,les_az)

# Question 10
"""
plt.plot(les_temps[:-1],les_vx,label="vx")
plt.plot(les_temps[:-1],les_vy,label="vy")
plt.plot(les_temps[:-1],les_vz,label="vz")
plt.legend()
plt.show()
"""

# Question 11
les_x = question_5(les_temps,les_vx)
les_y = question_5(les_temps,les_vy)
les_z = question_5(les_temps,les_vz)

# Question 10
"""
plt.plot(les_temps[:-2],les_x,label="x")
plt.plot(les_temps[:-2],les_y,label="y")
plt.plot(les_temps[:-2],les_z,label="z")
"""
plt.plot(les_x,les_y)
plt.show()

