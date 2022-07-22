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


count_nodes=int(input())
graph={}
egdes=[]
# store in the graph
for node in range(count_nodes):
    v,e=input().split(" -> ")
    children=[] if e=="" else [x for x in e.split(' ')]
    graph[v]=children
    for child in children:
        egdes.append((v,child))


# print(graph)
# print(egdes)

removed_edges=[]


for source, destination in sorted(egdes,key=lambda x: (x[0],x[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue
    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exist(source,destination,graph):
        #print(source,destination)
        removed_edges.append((source,destination))
    else:
        graph[source].append(destination)
        graph[destination].append(source)



print(f"Edges to remove: {len(removed_edges)}")
for a,b in removed_edges:
    print(f"{a} - {b}")