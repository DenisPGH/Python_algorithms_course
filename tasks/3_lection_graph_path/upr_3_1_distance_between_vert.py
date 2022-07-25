from collections import deque


def find_shortest_way(start_node,destination_node,graph,nodes):
    visited={}
    parent={}
    for n in graph:
        visited[n]=False
        parent[n]=None
    visited[start_node] = True
    queue_ = deque([start_node])
    while queue_:
        node = queue_.popleft()
        if node == destination_node:
            break
        for child in graph[node]:
            if child == None:
                break
            if visited[child]:
                continue
            visited[child] = True
            queue_.append(child)
            parent[child] = node


    return parent

def store_path(parent,destination_node):
    path = deque()
    node = destination_node

    while node is not None:
        path.appendleft(node)
        node = parent[node]
    return path

nodes=int(input())
pairs=(int(input()))
graph={}
for _ in range(nodes):
    source,destination=input().split(":")
    destination=destination.split(" ")
    if source not in graph:
        graph[int(source)]=[]
    if destination[0] !="":
        graph[int(source)].extend([int(x) for x in destination])
    else:
        graph[int(source)].append(None)


#print(graph)

all_couples=[]
for pair in range(pairs):
    cur_pair=[int(x) for x in input().split("-")]
    all_couples.append(cur_pair)
#print(all_couples)


for couple in all_couples:
    a,b=couple
    parent=find_shortest_way(a, b, graph, nodes)
    path=store_path(parent, b)
    #print(path)
    if len(path)>1:
        print(f"{{{a}, {b}}} -> {len(path)-1}")
    else:
        print(f"{{{a}, {b}}} -> -1")





