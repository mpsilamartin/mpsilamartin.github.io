### Lecture ###

# Une manière d'ouvrir le fichier :

f = open(r'U:\Cours_ipt\cours_07\groupes_mpsi1_s1.csv','r',encoding='utf8')
titres = f.readline() # Une ligne
lignes = f.readlines() # Toutes les lignes restantes
f.close()

# Une autre manière strictement équivalente

with open('groupes_mpsi1_s1.csv','r',encoding='utf8') as f:
    titres = f.readline() # Une ligne
    lignes = f.readlines() # Toutes les lignes restantes
# Le fichier est fermé automatiquement

### Traitement ###

trinomes = [[] for i in range(15)]
# pas [[]]*15 : attention aux alias !

for e in lignes :
    n = int(e.strip().split(',')[-1].strip('T'))
    # n : numéro du trinôme de l'étudiant e
    trinomes[n-1].append(e)
    # On range e dans la liste des étudiants du trinôme n

### Ecriture ###

with open('trinomes_mpsi1.csv','w',encoding='utf8') as f:
    f.write(titres)
    for t in trinomes :
        for e in t :
            f.write(e)

