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
            all_connected_nodes.add(first)
            all_connected_nodes.add(second)
            network.append((first,second))

        if first not in graph:
            graph[first] = []
        if second not in graph:
            graph[second] = []

        graph[first].append(edge)
        graph[second].append(edge)

    return graph

def prim_old(node,graph,forest,forest_edges):
    sum_=0
    forest.add(node)
    pq=PriorityQueue()
    for edge in graph[node]:
        pq.put(edge)
    while not pq.empty():
        min_edge=pq.get()
        non_tree_node=-1
        if min_edge.first in forest and min_edge.second not in forest :
            non_tree_node=min_edge.second
        elif min_edge.second in forest and min_edge.first not in forest :
            non_tree_node=min_edge.first
        if non_tree_node==-1:
            continue
        if non_tree_node not in all_connected_nodes:
            forest.add(non_tree_node)
            all_connected_nodes.add(node)
            network.append((node,non_tree_node))
            sum_=min_edge.weight
            print(sum_)
        #if min_edge.connected==False: #and min_edge.first not in all_connected_nodes and min_edge.second not in all_connected_nodes:
        #if (node,non_tree_node) not in network:
        if (min_edge.first,min_edge.second) in network:
            continue
        forest_edges.append(min_edge)
        #print(min_edge.first,min_edge.second)
        #print(forest_edges)
        for edge in graph[non_tree_node]:
            if (edge.first,edge.second) in network:
                pq.put(edge)


def prim(node,graph,forest,forest_edges):
    forest.add(node)
    pq=PriorityQueue()
    for edge in graph[node]:
        if edge.connected==False:
            pq.put(edge)
    while not pq.empty():
        min_edge=pq.get()
        non_tree_node=-1
        if min_edge.first in forest and min_edge.second not in forest:
            non_tree_node=min_edge.second
        elif min_edge.second in forest and min_edge.first not in forest:
            non_tree_node=min_edge.first
        if non_tree_node==-1:
            continue
        forest.add(non_tree_node)
        forest_edges.append(min_edge)
        for edge in graph[non_tree_node]:
            pq.put(edge)





budget=int(input())
nodes=int(input())
edges=int(input())
all_connected_nodes=set()
network=[]
graph=fill_graph(edges)
#print(graph)
# print(all_connected_nodes)
# print(network)
forest=set()
forest_edges=[]
sum_=0
for node,edges_ in graph.items():
    # if node not in all_connected_nodes:
    #     continue
    if node in forest:
        #print(node)
        continue
    prim(node,graph,forest,forest_edges)
    #print(node)


for edge in sorted(forest_edges,key= lambda x:( x.weight)):
    if edge.weight<=budget:
        budget-=edge.weight
        sum_+=edge.weight
        #print(f"{edge.first} - {edge.second}==weight=  {edge.weight}")

print(f"Budget used: {sum_}")
# print(all_connected_nodes)
# print(network)

