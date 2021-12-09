##effet d'un filtre sur un signal périodique

##ex du signal créneau et des filtres passe bas et passe haut du premier ordre (variable fo)

##importation des bibliothèques

import numpy as np
import matplotlib.pyplot as plt

##spectre du signal d'entrée créneau:

fs=1e3# fréquence du signal
nmax=1000 # rang de l'harmonique max
N=np.arange(1,nmax,2) #sélectiondes harmoniques impaires uniquement

Ae=np.array([4/(np.pi*n) for n in N]) # les amplitudes
Phie=np.array([3*np.pi/2 for n in N]) # Les phases
A0= 1 #valeur moyenne
F=np.array([n*fs for n in N])

##definition des filtres du premier ordre :

j=complex(0,1) # définition du complexe j tq j²=-1

# passe bas du premier ordre
def H(f,fc):
    s=1/(1+j*f/fc)
    return s

fc=1e1 #fréquence de coupure

gain=np.array([np.abs(H(n*fs,fc)) for n in N]) # calcul du gain
Phase=np.array([np.angle(H(n*fs,fc))for n in N]) # calcul de la phase

# passe haut du premier ordre
def Hh(f,fc):
    s=(j*f/fc)/(1+j*f/fc)
    return s


gainh=np.array([np.abs(Hh(n*fs,fc)) for n in N]) # calcul du gain
Phaseh=np.array([np.angle(Hh(n*fs,fc))for n in N]) # calcul de la phase


##calcul du spectre en sortie

# passe bas du premier ordre
As=Ae*gain #les amplitudes
Phis=Phie+Phase #les phases
A0s = np.abs(H(0,fc))*A0 #la valeur moyenne

# passe haut du premier ordre
Ash=Ae*gainh #les amplitudes
Phish=Phie+Phaseh #les phases
A0sh = np.abs(Hh(0,fc))*A0 #la valeur moyenne

##Calcul des tensions

t=np.linspace(0,2/fs,500) #on trace deux périodes
e=np.array([A0+np.sum(Ae*np.cos(2*np.pi*fs*temps*N+Phie)) for temps in t])# tension d'entrée
s=np.array([A0s+np.sum(As*np.cos(2*np.pi*fs*temps*N+Phis)) for temps in t])#tension de sortie pour le filtre passe bas

sh=np.array([A0sh+np.sum(Ash*np.cos(2*np.pi*fs*temps*N+Phish)) for temps in t])#tension de sortie pour le filtre passe haut

##tracé des courbes

plt.figure()
plt.plot(t,e,'r',label='entrée')
plt.plot(t,s,'g',label='sortie filtre passe bas')
plt.legend()
plt.xlabel('temps (s)')
plt.ylabel('signaux')
plt.grid()
plt.show()

plt.figure()
plt.bar(F,Ae,100,color='r',label='Ae')
plt.bar(F,As,100,color='g',label='As')

plt.xlabel('frequences')
plt.ylabel('Amplitudes')
plt.xlim([0,30*fs])
plt.ylim([0,Ae[0]])
plt.title('spectres de fréquence et filtre passe bas')
plt.grid()
plt.show()

plt.figure()
plt.plot(t,e,'r',label='entrée')
plt.plot(t,sh,'g',label='sortie filtre passe haut')
plt.legend()
plt.xlabel('temps (s)')
plt.ylabel('signaux')
plt.grid()
plt.show()

plt.figure()
plt.bar(F,Ae,100,color='r',label='Ae')
plt.bar(F,Ash,100,color='g',label='Ash')

plt.xlabel('frequences')
plt.ylabel('Amplitudes')
plt.xlim([0,30*fs])
plt.ylim([0,Ae[0]])
plt.title('spectres de fréquence et filtre passe haut')
plt.grid()
plt.show()
