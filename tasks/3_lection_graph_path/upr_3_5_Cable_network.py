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
    start_nodes=set()
    for _ in range(edges):
        input_info=[x for x in input().split(" ")]
        first, second, weight = [int(x) for x in input_info[:3]]
        if len(input_info)==3:
            edge = Edge(first, second, weight)
        else:
            edge = Edge(first, second, weight,True)
            start_nodes.add(first)
            start_nodes.add(second)

        if first not in graph:
            graph[first] = []
        if second not in graph:
            graph[second] = []
        graph[first].append(edge)
        graph[second].append(edge)
    return graph,start_nodes

def prim(forest,graph):
    used_budget=0
    pq=PriorityQueue()
    for node in forest: # store the start networt to the queue
        for edge in graph[node]:
            pq.put(edge)
    while not pq.empty():
        min_edge=pq.get()
        non_tree_node=None
        if min_edge.first in forest and min_edge.second not in forest:
            non_tree_node=min_edge.second
        elif min_edge.second in forest and min_edge.first not in forest:
            non_tree_node=min_edge.first
        if non_tree_node==None :
            continue
        if used_budget+min_edge.weight>budget:
            break
        used_budget+=min_edge.weight
        forest.add(non_tree_node)
        for edge in graph[non_tree_node]:
            pq.put(edge)
    return used_budget





budget=int(input())
nodes=int(input())
edges=int(input())
graph,all_start_connected_nodes=fill_graph(edges)
sum_=prim(all_start_connected_nodes,graph)
print(f"Budget used: {sum_}")

