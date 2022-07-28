import numpy as np
import networkx as nx
#import pylab as plt

A = np.array([[0,0,1,0],[1,0,0,0],[1,0,0,1],[1,0,0,0]])
G = nx.DiGraph(A)

#pos = [[0,0], [0,1], [1,0], [1,1]]
#nx.draw(G,pos)
#plt.show()