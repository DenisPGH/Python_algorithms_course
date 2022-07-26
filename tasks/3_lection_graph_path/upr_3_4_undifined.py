from collections import deque


class Edge:
    def __init__(self,source,destination,weight):
        self.source = source
        self.destination = destination
        self.weight = weight


def store_data_to_graph(edges):
    graph = []
    for _ in range(edges):
        source, destination, weight = [int(x) for x in input().split(" ")]
        graph.append(Edge(source, destination, weight))

    return graph


def find_all_ways(start,graph,nodes):
    """
    1. got graph dict with all nodes, weighs
    2. return 2 collections:
    - distance(all short distance between start and custom node)
    - parents( each node and its parents node, from it came from)
    """
    distances=[float('inf')]*(nodes+1) # array to store all nodes , and distance to start
    parents=[None]*(nodes+1)
    distances[start]=0 # declare the start node with distance 0
    for _ in range(nodes-1):
        updated=False
        for edge in graph:
            if distances[edge.source]==float('inf'):
                continue
            new_distance=distances[edge.source]+edge.weight
            if new_distance<distances[edge.destination]:
                distances[edge.destination]=new_distance
                parents[edge.destination]=edge.source
                updated=True
        if not updated:
            break
    return distances,parents

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
        if node in path:
            return
    return path




nodes=int(input()) #
edges=int(input()) #
graph=store_data_to_graph(edges)
start_=int(input()) # declare the start point
target=int(input()) # declare the target point

#print(graph)

distances,parents=find_all_ways(start_,graph,nodes)
path=generate_path_source_to_target(target,parents)
if path:
    print(*list(path),sep=' ')
    print(distances[target])
else:
    print("Undefined")

