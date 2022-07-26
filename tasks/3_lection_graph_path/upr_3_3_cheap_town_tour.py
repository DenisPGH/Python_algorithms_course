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
    sum_path=0
    while not pq.empty():
        min_distance_to_the_node,node=pq.get() # get the min value in the queue
        # if node ==target:
        #     break
        for edge in graph[node]:
            #if node == edge:
            if all([x for x in visited.values()]):
                cycle=True
                break
            child = edge.destination if edge.source == node else edge.source

            new_distance= min_distance_to_the_node+edge.weight
            if new_distance < distances[child]:
                sum_path+=new_distance
                distances[child]=new_distance
                parents[child]=node
                visited[child]=True
                pq.put((new_distance,child))
            #print(visited)
        # if all([x for x in visited.values()]):
        #     return distances, parents


        if cycle:
            # got cycle
            break
    #print(sum_path)
    return distances,parents


towns=4 #int(input()) #
streets=5 #int(input()) #
graph=my_input_data_to_graph(streets)
#print(graph)
dict_min_value_pair={}
town_pair=[]
counter=0
#while True:
for town in graph:
    counter+=1
    if counter>5:
        break
    #print(town)
    #town=0

    from_town=town
    to_town=town
    costs,parents=find_all_ways_cheapest(from_town,to_town,graph)
    #a=max(costs.items())[1]
    #a=min(costs.values())
    smallest_value=min(i for i in costs.values() if i > 0)
    next_town=''
    for k,v in sorted(costs.items(),key=lambda x: (x[1])):
        if v==0:
            continue
        next_town=k
        break

    print(f"now go to {next_town}")
    #town=next_town

    print(costs)



#print(dict_min_value_pair)
#print(town_pair)

# visited=[True,True]
# if all([x for x in visited]):
#     raise Exception('all visited')

""""
    for each_town in costs:
       #print(each_town)
        #pair=f"{min(town,each_town)}-{max(each_town,town)}"
        pair=f"{town}-{each_town}"
        if pair not in dict_min_value_pair:
            dict_min_value_pair[pair]=0
        if costs[each_town]>dict_min_value_pair[pair]:
            dict_min_value_pair[pair]=costs[each_town]
            town_pair.append({pair:costs[each_town]})
            #print(path)
    #print(sum(costs.values()))
    #print(parents)
"""



