with open('notes.csv','r') as f :
    _ = f.readline()
    L = f.readlines()

def moyenne(li):
    """Moyenne des nombres inscrits dans la ligne
    li = ['n1','n2',...]"""
    s,n = 0,0
    for note in li :
        if note != '' :
            s = s + float(note)
            n = n+1
    return s / n

with open('moyennes.csv','w') as w :
    w.write('Prénoms,Moyennes\n')
    for etu in L :
        etu = etu.strip('\n').split(',')
        moy = moyenne(etu[1:])
        prenom = etu[0]
        w.write(','.join([prenom, str(moy)])+'\n')

