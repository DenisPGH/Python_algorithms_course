from collections import  deque
from queue import PriorityQueue


class Edge:
    def __init__(self,source,destination,weight):
        self.source = source
        self.destination = destination
        self.weight = weight

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

def my_input_data_to_graph(edges):
    input_=[['0 - 1 - 10'],
            ['0 - 2 - 6'],
            ['0 - 3 - 5'],
            ['1 - 3 - 15'],
            ['2 - 3 - 4']
            ]
    graph={}

    for index in range(len(input_)):
        source, destination, weight = [int(y) for y in input_[index][0].split(' - ')]
        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []
        graph[source].append(Edge(source, destination, weight))
        graph[destination].append(Edge(source, destination, weight))
        #graph[destination].append(Edge( destination,source, weight))

    return graph

def store_data_to_graph(edges):
    graph={}

    for _ in range(edges):
        source, destination, weight = [int(x) for x in input().split(" - ")]
        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []
        graph[source].append(Edge(source, destination, weight))
        graph[destination].append(Edge(source, destination, weight))

    return graph

def find_all_ways_cheapest(start,target,graph):

    distances = {}
    parents = {}
    visited = {}
    for nod in graph:
        distances[nod] = float('inf')
        parents[nod] = None
        visited[nod] = False

    distances[start]=0 # declare the start node with distance 0
    pq=PriorityQueue()
    pq.put((0,start))
    visited[start]=True
    cycle=False
    while not pq.empty():
        min_distance_to_the_node,node=pq.get() # get the min value in the queue
        for edge in graph[node]:
            if all([x for x in visited.values()]):
                cycle=True
                break
            child = edge.destination if edge.source == node else edge.source

            new_distance= min_distance_to_the_node+edge.weight
            if new_distance < distances[child]:
                distances[child]=new_distance
                parents[child]=node
                visited[child]=True
                pq.put((new_distance,child))
                print(visited)



        if cycle:
            # got cycle
            break
    return distances,parents


towns=4 #int(input()) #
streets=5 #int(input()) #
graph=my_input_data_to_graph(streets)
#print(graph)
dict_min_value_pair={}

for town in graph:
    print(town)
    from_town=town
    to_town=town
    costs,parents=find_all_ways_cheapest(from_town,to_town,graph)

    print(costs)

    #print(sum(costs.values()))
    #print(parents)







