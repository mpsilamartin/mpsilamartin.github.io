with open("groupes_mpsi1.csv","r",encoding="utf-8") as f:
    T = f.readline() # Titres des colonnes
    L = f.readlines() # Liste des étudiants

trinomes = [[] for i in range(16)]
# Liste des trinômes

for e in L :
    s = e.strip('\n').split(',') # Infos de l'étudiant
    n = int(s[-1].strip('T')) # Numéro de trinôme
    trinomes[n-1].append(s)
    # On range l'étudiant dans son trinôme

with open("trinomes_mpsi1.csv","w",encoding="utf-8") as f :
    f.write(T)
    for t in trinomes:
        for e in t :
            f.write(','.join(e)+'\n')
