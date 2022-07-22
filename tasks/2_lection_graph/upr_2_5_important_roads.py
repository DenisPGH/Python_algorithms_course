def dfs_find_all_members(node,destination, graph, visited):
    if node in visited:
        return
    visited.add(node)
    if node==destination:
        return
    for kids in graph[node]:
        dfs_find_all_members(kids, destination,graph, visited)


def path_exist(source, destination,graph):
    visited=set()
    dfs_find_all_members(source, destination, graph, visited)
    return  destination in visited



graph={}
number_nodes=int(input())
number_edges=int(input())
roads=[]
for ed in range(number_edges):
    a,b=[int(x) for x in input().split(" - ")]
    if a not in graph:
        graph[a]=[]
    if b not in graph:
        graph[b]=[]
    graph[a].append(b)
    graph[b].append(a)
    roads.append((min(a,b),max(a,b)))




# graph={'1': ['0', '2'], '0': ['1', '2', '3'], '2': ['0', '1'], '3': ['0', '4'], '4': ['3']}
# roads=[(0, 1), (0, 2), (1, 2), (0, 3), (3, 4)]
# roads=[(str(x),str(y)) for x,y in roads]


print('Important streets:')
for source, destination in roads:
    graph[source].remove(destination)
    graph[destination].remove(source)
    if not path_exist(source,destination,graph):
        #print(source,destination)
        print(f"{source} {destination}")
    else:
        graph[source].append(destination)
        graph[destination].append(source)

