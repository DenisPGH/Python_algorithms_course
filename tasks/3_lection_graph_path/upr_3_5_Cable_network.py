from queue import PriorityQueue


class Edge:
    def __init__(self,first, second, weight,connection=False):
        self.first = first
        self.second = second
        self.weight = weight
        self.connected=connection
    def __gt__(self, other):
        return self.weight>other.weight


def fill_graph(edges):
    graph={}
    for _ in range(edges):
        input_info=[x for x in input().split(" ")]
        first, second, weight = [int(x) for x in input_info[:3]]
        if len(input_info)==3:
            edge = Edge(first, second, weight)
        else:
            edge = Edge(first, second, weight,True)

        if first not in graph:
            graph[first] = []
        if second not in graph:
            graph[second] = []

        graph[first].append(edge)
        graph[second].append(edge)
    return graph

def prim(node,graph,forest,forest_edges):
    forest.add(node)
    pq=PriorityQueue()
    for edge in graph[node]:
        pq.put(edge)
    while not pq.empty():
        min_edge=pq.get()
        non_tree_node=-1
        # if min_edge.connected==True:
        #     break
        if min_edge.first in forest and min_edge.second not in forest :
            non_tree_node=min_edge.second
        elif min_edge.second in forest and min_edge.first not in forest :
            non_tree_node=min_edge.first
        if non_tree_node==-1:
            continue
        forest.add(non_tree_node)
        print(non_tree_node)
        if min_edge.connected==False:
            forest_edges.append(min_edge)
        #print(forest_edges)
        for edge in graph[non_tree_node]:
            pq.put(edge)




budget=int(input())
nodes=int(input())
edges=int(input())
graph=fill_graph(edges)
#print(graph)

forest=set()
forest_edges=[]
for node in graph:
    # if node in forest:
    #     print(node)
    #     continue
    prim(node,graph,forest,forest_edges)


for edge in forest_edges:
    print(f"{edge.first} - {edge.second}==weight=  {edge.weight}")
