from collections import  deque

def store_data_to_graph(edges):
    graph = []
    """
    :param edges: count of the edges in the graph
    :param graph: empty graph
    :return:  filled graph with nodes, and their information
    """
    for _ in range(edges):
        source, destination, weight = [int(x) for x in input().split(" ")]
        # if source not in graph:
        #     graph[source] = []
        # if destination not in graph:
        #     graph[destination] = []
        graph.append(Edge(source, destination, weight))

    return graph


def find_all_ways(graph,nodes):
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
    return path





class Edge:
    def __init__(self,source,destination,weight):
        self.source = source
        self.destination = destination
        self.weight = weight


nodes=int(input()) # give here value of the nodes
edges=int(input()) # give here value of the edges
graph=store_data_to_graph(edges)
start=int(input()) # declare the start point
target=int(input()) # declare the target point


distances,parents=find_all_ways(graph,nodes)

for edg in graph:
    new_distance=distances[edg.source]+edg.weight
    if new_distance<edg.destination:
        print("Negative Cycle Detected")
        break
else:
    path=list(generate_path_source_to_target(target,parents))
    print(*path,sep=' ')
    print(distances[target])




