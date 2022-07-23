from collections import  deque
from queue import PriorityQueue
class Edge:
    def __init__(self,source,destination,weight):
        self.source = source
        self.destination = destination
        self.weight = weight



edges=int(input()) # give here value of the edges
graph={}

for _ in range(edges):
    source, destination,weight= [int(x) for x in input().split(", ")]
    if source not in graph:
        graph[source]=[]
    if destination not in graph:
        graph[destination]=[]
    graph[source].append(Edge(source,destination,weight))


start=int(input()) # declare the start point
target=int(input()) # declare the target point

value_of_nodes_in_graph=len(graph)
distances=[float('inf')]*(value_of_nodes_in_graph+1) # array to store all nodes , and distance to start
parents=[None]*(value_of_nodes_in_graph+1)

distances[start]=0 # declare the start node with distance 0

pq=PriorityQueue()

pq.put((0,start))

while not pq.empty():
    min_distance_to_the_node,node=pq.get() # get the min value in the queue
    if node ==target:
        break
    for edge in graph[node]:
        new_distance= min_distance_to_the_node+edge.weight
        if new_distance < distances[edge.destination]:
            distances[edge.destination]=new_distance
            parents[edge.destination]=node
            pq.put((new_distance,edge.destination))

if distances[target]== float('inf'):
    print('There is no such path') # return no mach

else:
    print(distances[target])

    path=deque()
    node=target
    while node is not None:
        path.appendleft(node)
        node=parents[node]
    print(*path,sep=" ")


