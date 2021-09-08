import numpy as np
import matplotlib.pyplot as plt

# Mesure

f = 40983 # Hz
lambd = 0.00840 # m

# Entrez les incertitudes types et précisions

uf = 500 # Hz
ulambd = 0.00048 # m

Deltaf=uf*np.sqrt(3)
Deltalambd=ulambd*np.sqrt(3)

# Entrez la fonction de composition

def produit(a,b):
    return a*b

# Entrez le nombre de simulation que vous voulez effectuer

N = 100000

# Calculs avec une distribution de probabilité uniforme
Celerite = []

for i in range(0,N):
    a = np.random.uniform(f-Deltaf,f+Deltaf)
    b = np.random.uniform(lambd-Deltalambd,lambd+Deltalambd)
    Celerite.append(produit(a,b))

plt.figure(1)
plt.hist(Celerite,bins = 'rice')
plt.title('Résultat du tirage aléatoire du produit après simulation')
plt.xlabel("c (m/s)")
plt.show()

# Calcul et affichage moyenne et écart type

moy = np.mean(Celerite)
std = np.std(Celerite,ddof=1)

print("Moyenne = {:.2f} m/s".format(moy))
print("Ecart type = {:.2f} m/s".format(std))

######### Utilisation de la formule du programme #########

uProd= f*lambd*np.sqrt((uf/f)**2 + (ulambd/lambd)**2)


print("Incertitude de type produit avec la fomule = {:.2f} m/s".format(uProd))