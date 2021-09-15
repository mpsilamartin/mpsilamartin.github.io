import numpy as np
import matplotlib.pyplot as plt

# Positions de des points

A = 11.1 # cm
B = 19.5 # cm

# Entrez les précisions

DeltaA = 0.5 # cm
DeltaB = 0.5 # cm

# Entrez la fonction de composition

def ecart(a,b):
    return b-a

# Entrez le nombre de simulation que vous voulez effectuer

N = 100000

# Calculs avec une distribution de probabilité uniforme
Difference = []

for i in range(0,N):
    a = np.random.uniform(A-DeltaA,A+DeltaA)
    b = np.random.uniform(B-DeltaB,B+DeltaB)
    Difference.append(ecart(a,b))

plt.figure(1)
plt.hist(Difference,bins = 'rice')
plt.title('Résultat du tirage aléatoire de la différence après simulation')
plt.xlabel("b-a (cm)")
plt.show()

# Calcul et affichage moyenne et écart type

moy = np.mean(Difference)
std = np.std(Difference,ddof=1)

print("Moyenne = {:.2f} cm".format(moy))
print("Ecart type = {:.2f} cm".format(std))

######### Utilisation de la formule du programme #########

uA = DeltaA / np.sqrt(3)
uB = DeltaB / np.sqrt(3)

uDiff= np.sqrt(uA**2 + uB**2)


print("Incertitude de type somme avec la fomule = {:.2f} cm".format(uDiff))