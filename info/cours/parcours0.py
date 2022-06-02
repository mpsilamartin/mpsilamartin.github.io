import matplotlib.pyplot as plt
import networkx as nx

G=[[0,1,1],[1,0,1],[1,0,0]]


# plt.clf()
# plt.figure('graphe exemple')
# plot_graphe(G)
# dist=distances(G,1)

for element in G:
    print (element)


def aretes(G:list)->list:
    L=[]
    for i in range(len(G)):
        for j in range(len(G)):
            if not G[i][j]==0:
                L.append((i,j))
    return L

def plot_graphe(G):
    Gx=nx.DiGraph()
    edges=aretes(G)
    Gx.add_edges_from(edges)

    nx.draw(Gx,with_labels = True)
    plt.show()

def plot_graphe_ld(G):
    Gx=nx.DiGraph()
    edges=aretes_ld(G)
    Gx.add_edges_from(edges)

    nx.draw(Gx,with_labels = True)
    plt.show()


G={"S0":["S1","S5","S6"],"S1":["S0","S2","S6"],"S2":["S1","S3"],"S3":["S2","S4"],"S4":["S3","S5"],"S5":["S4","S0"],"S6":["S1","S0"]}


def aretes_l(G:list)->list:
    '''Fonction qui construit à partir d'une liste d'adjacence la liste des arêtes sans doublon
    entrée :
    G : list, liste d'adjacence
    sortie :
    L : list, liste des couples de sommets voisins
    '''
    L=[]
    for i in range(len(G)):
        for j in range(len(G[i])):
            if i<G[i][j]:
                L.append((i,G[i][j]))
    return L

def aretes_ld(G:list)->list:
    '''Fonction qui construit à partir d'une liste d'adjacence la liste des arêtes sans doublon
    entrée :
    G : list, liste d'adjacence
    sortie :
    L : list, liste des couples de sommets voisins
    '''
    L=[]
    for sommet,voisins in G.items():
        for v in voisins:
            L.append((sommet,v))
    return L


plt.figure('graphe exemple')
plot_graphe_ld(G)

from collections import deque

def bfs(G, s) -> None:
    """
    G : graphe sous forme de dictionnaire d'adjacence
    s : sommet du graphe (Chaine de caractere du type "S1").
    """
    visited = {}
    for sommet,voisins in G.items():
        visited[sommet]=False
    # Le premier sommet àvisiter entre dans la file
    q = deque([s])
    while len(q) > 0:
        print(visited,q)
        # On visite la tête de file
        u = q.pop()
        # On vérifier qu'elle n'a pas été visitée
        if not visited[u]:
            # Si on l'avait pas visité, maintenant c'est le cas :)
            visited[u] = True
            # On met les voisins de u dans la file
            for v in G[u]:
                q.appendleft(v)

bfs(G,'S0')




