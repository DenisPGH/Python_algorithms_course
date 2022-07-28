from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self,source,destination,weight):
        self.source = source
        self.destination = destination
        self.weight = weight
        # self.edge_name=''
        # self.edge_row=0
        # self.edge_col=0

def prove_if_coordinates_are_in_range(row,col,rows,cols):
    if 0<= row < rows and 0<= col < cols:
        return True
    else:
        return False

def print_matrix(mat):
    for row in mat:
        print("|".join([str(x) for x in row]))

def number_nodes_in_matrix(mat):
    counter=0
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            if mat[row][col]=="-":
                counter+=1
                mat[row][col]=counter
    return mat

def create_graph_from_matrix(mat):
    graph={}
    rows=len(mat)
    for row in range(rows):
        cols=len(mat[row])
        for col in range(cols):
            if mat[row][col]!="*":
                current_node_name=mat[row][col]
                if current_node_name not in graph:
                    graph[current_node_name]=[]


                if prove_if_coordinates_are_in_range(row - 1, col, rows, cols) and mat[row-1][col]!="*":
                    above_node_name = mat[row - 1][col]
                    graph[current_node_name].append(Edge(current_node_name, above_node_name, 10))
                    if above_node_name not in graph:
                        graph[above_node_name] = []
                    graph[above_node_name].append(Edge(above_node_name,current_node_name,  10))



                if prove_if_coordinates_are_in_range(row + 1, col, rows, cols) and mat[row+1][col]!="*":
                    down_node_name = mat[row + 1][col]
                    graph[current_node_name].append(Edge(current_node_name, down_node_name, 10))
                    if down_node_name not in graph:
                        graph[down_node_name]=[]
                    graph[down_node_name].append(Edge(down_node_name,current_node_name,  10))



                if prove_if_coordinates_are_in_range(row, col-1, rows, cols) and mat[row][-1]!="*":
                    left_node_name = mat[row][col-1]
                    graph[current_node_name].append(Edge(current_node_name, left_node_name, 10))
                    if left_node_name not in graph:
                        graph[left_node_name] = []
                    graph[left_node_name].append(Edge(left_node_name,current_node_name, 10))




                if prove_if_coordinates_are_in_range(row, col+1, rows, cols) and mat[row][+1]!="*":
                    right_node_name = mat[row][col+1]
                    graph[current_node_name].append(Edge(current_node_name, right_node_name, 10))
                    if right_node_name not in graph:
                        graph[right_node_name] = []
                    graph[right_node_name].append(Edge(right_node_name,current_node_name,  10))


    return graph

def find_shortest_way_between_two_nodes(start,target,graph):
    """
    1. got graph dict with all nodes, weighs
    2. return 2 collections:
    - distance(all short distance between start and custom node)
    - parents( each node and its parents node, from it came from)
    """
    distances = {}
    parents = {}
    visited = {}
    for nod in graph:
        distances[nod] = float('-inf')
        parents[nod] = None
        visited[nod] = False
    #value_of_nodes_in_graph=len(graph)
    #distances=[float('inf')]*(value_of_nodes_in_graph+1) # array to store all nodes , and distance to start
    #parents=[None]*(value_of_nodes_in_graph+1)
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
    return distances,parents


def generate_path_from_source_to_target(target_,parents):
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




matrix=[["*************************************************************************************"],
        ["*---------------------------------*------------------------*------------------------*"],
        ["*---------------------------------*------------------------*------------------------*"],
        ["*---------------------------------*------------------------*------------------------*"],
        ["*---------------------------------*-------------------------------------------------*"],
        ["*---------------------------------*-------------------------------------------------*"],
        ["*----------------------------------------------------------*------------------------*"],
        ["*----------------------------------------------------------*------------------------*"],
        ["*-----*******************************************************************************"],
        ["*-----------------------------------------------------------------------------------*"],
        ["*-----------------------------------------------------------------------------------*"],
        ["*--------------------------------**-------------------------------------------------*"],
        ["*--------------------------------**-------------------------------------------------*"],
        ["*--------------------------------**-------------------------------------------------*"],
        ["*--------------------------------**-------------------------------------------------*"],
        ["*--------------------------------**-------------------------*************************"],
        ["*--------------------------------**-------------------------**----------------------*"],
        ["*--------------------------------**-------------------------**----------------------*"],
        ["*--------------------------------**----------------------------------------e--------*"],
        ["*--------------------------------**-------------------------------------------------*"],
        ["*--------------------------------**-------------------------**----------------------*"],
        ["*************************************************************************************"],
        ]
matrix=[list(x[0]) for x in matrix]
new_matrix=number_nodes_in_matrix(matrix)
#print_matrix(new_matrix)
test_matrix=[[1,2,3],
             [4,5,6],
             [7,8,9]]

graph=create_graph_from_matrix(new_matrix)
print_matrix(new_matrix)
print(graph)
start_node=1
target_node=20
distances,parents=find_shortest_way_between_two_nodes(start_node,target_node,graph)
path=list(generate_path_from_source_to_target(target_node,parents))
print(path)



