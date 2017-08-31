with open("etudiants_mpsi2.csv",'r') as f:
    L = f.readlines()

titres = L[0].strip('\n').split(',')

etudiants = [x.strip('\n').split(',') for x in 
L[1:]]

trinomes = [[] for k in range(14)]

for x in etudiants:
    trinomes[int(x[6].strip('T'))-1].append(x[:2]+[x[6]])

with open('trinomes_etudiants.csv','w') as f :
    f.write('Groupes,Noms,Prénoms\n')
    for T in trinomes :
        for e in T :
            f.write(e[2]+','+e[0]+','+e[1]+'\n')
