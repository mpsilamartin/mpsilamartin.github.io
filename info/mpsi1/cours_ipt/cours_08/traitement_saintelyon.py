## 1) Lecture

with open('sainte_lyon.csv','r',encoding='utf8') as f:
    titres = f.readline()
    T = f.readlines()

## 2) Traitement

for i in range(len(T)):
    T[i] = T[i].strip().split(';')
    h,m,s = T[i][1].split(':')
    # Calcul du temps en s
    t = int(h)*3600 + int(m)*60 + int(s)
    T[i][1] = t
    # Ajout de la vitesse à la fin de la ligne
    T[i].append(3600*72 / t)

## 3) Ecriture

with open('sainte_lyon_vitesse.csv','w',encoding='utf8') as f:
    f.write(titres.strip() + ' en s;Vitesse en km/h')
    for L in T:
        f.write('\n')
        ligne = ';'.join([str(x) for x in L])
        f.write(ligne)
