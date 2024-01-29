import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def plot_graphe_l(G):
    plt.close()
    Gx = nx.Graph()
    edges = arretes_l(G)
    Gx.add_edges_from(edges)
    nx.draw(Gx,with_labels = True)
    plt.show()


Gd={0:(1,2,3,4),1:(0,2),2:(0,1,3,5),3:(0,2,5,4),4:(0,3,5),5:(2,3,4)}


def arretes_l(Gd:dict):
    arretes=[]
    for e in Gd.keys():
        for x in Gd[e]:
            arretes.append((e,x))
    return arretes


plot_graphe_l(Gd)