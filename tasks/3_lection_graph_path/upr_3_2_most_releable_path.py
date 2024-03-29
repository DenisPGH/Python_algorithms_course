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
        graph[destination].append(Edge(source, destination, weight))
        #graph[destination].append(Edge(destination,source , weight))

    return graph

def find_all_ways(start,nodes,target,graph):
    percent={}
    parents={}
    visited={}
    for nod in graph:
        percent[nod]=float('-inf')
        parents[nod]=None
        visited[nod]=False
    percent[start] = 100
    #pq = DualPriorityQueue(maxPQ=True)
    pq=PriorityQueue()
    pq.put((-100, start))
    while not pq.empty():
        max_percent, node = pq.get()  # get the max value in the queue
        #print(max_percent)
        if node==target:
            break
        #print(percent)
        for edge in graph[node]:
            child=edge.destination if edge.source==node else edge.source
            # if visited[node] != False:
            #     continue
            new_distance = -max_percent * edge.weight /100
            if new_distance > percent[child]:
                percent[child] = new_distance
                parents[child] = node
                # visited[edge.source]=True
                pq.put((-new_distance, child))
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
start_=int(input()) # declare the start point
target=int(input()) # declare the target point

#print(graph)
percents,parents=find_all_ways(start_,nodes,target,graph)
#print(percents)
#print(parents)

if percents[target]== float('inf'):
    print('There is no such path') # return no mach

else:

    path=list(generate_path_source_to_target(target,parents))
    print(f"Most reliable path reliability: {(percents[target]):.2f}%")
    print(*path,sep=" -> ")




