Fichier = open("CoMax.txt",'r')
data = []

for k in range(2):
    Fichier.readline()

temps=[]; q_exp=[]
for lu in Fichier:
    ligne = lu.split("\t")
    temps.append(float(ligne[1]))
    q_exp.append(float(ligne[2]))