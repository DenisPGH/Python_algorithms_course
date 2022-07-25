from collections import  deque
from queue import PriorityQueue

def store_data_to_graph(edges,graph):
    """
    :param edges: count of the edges in the graph
    :param graph: empty graph
    :return:  filled graph with nodes, and their information
    """
    for _ in range(edges):
        source, destination, weight = [int(x) for x in input().split(" ")]
        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []
        graph[source].append(Edge(source, destination, weight))
        #graph[destination].append(Edge(source, destination, weight))

    return graph

def find_all_ways(nodes,target,graph):
    percent={}
    parents={}
    val='val'
    node_counter="node_counter"
    for nod in graph:
        percent[nod]={}
        percent[nod][val]=float('-inf')
        percent[nod][node_counter]=0
        parents[nod]=None
    percent[start] = 0  # declare the start node with distance 0
    #pq = PriorityQueue()
    pq = DualPriorityQueue(maxPQ=True)
    pq.put(0, start)
    while not pq.empty():
        min_distance_to_the_node, node = pq.get()  # get the min value in the queue
        if node == target:
            break
        for edge in graph[node]:
            new_distance = min_distance_to_the_node + edge.weight
            if new_distance > percent[edge.destination][val]:
                percent[edge.destination][val] = new_distance
                parents[edge.destination] = node
                pq.put(new_distance, edge.destination)
    return percent, parents


def generate_path_source_to_target(target_,parents):
    """
    1.this function got the target and parents lists
    2.return the shortes path to the target
     """
    path = deque()
    node = target_
    while node is not None:
        path.appendleft(node)
        node = parents[node]
    return path





class Edge:
    def __init__(self,source,destination,weight):
        self.source = source
        self.destination = destination
        self.weight = weight


class MaxPriorityQueue:
    def __init__(self,weight,name):
        self.name = name
        self.weight = weight

class DualPriorityQueue(PriorityQueue):
    def __init__(self, maxPQ=False):
        PriorityQueue.__init__(self)
        self.reverse = -1 if maxPQ else 1

    def put(self, priority, data):
        PriorityQueue.put(self, (self.reverse * priority, data))

    def get(self, *args, **kwargs):
        priority, data = PriorityQueue.get(self, *args, **kwargs)
        return self.reverse * priority, data





graph={}
nodes=int(input()) #
edges=int(input()) #
graph=store_data_to_graph(edges,graph)
start=int(input()) # declare the start point
target=int(input()) # declare the target point

print(graph)
distances,parents=find_all_ways(nodes,target,graph)
print(distances)
print(parents)

if distances[target]== float('inf'):
    print('There is no such path') # return no mach

else:

    path=list(generate_path_source_to_target(target,parents))
    print(f"Most reliable path reliability: {(distances[target]['val'] /len(path)):.2f}%")
    print(*path,sep=" -> ")




