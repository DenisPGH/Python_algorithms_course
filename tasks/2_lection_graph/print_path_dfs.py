def dfs_find_all_members(node,destination, graph, visited,path):
    if node in visited:
        return
    visited.add(node)
    if node==destination:
        return
    path.append(node)

    for kids in graph[node]:
        dfs_find_all_members(kids, destination,graph, visited,path)



def path_find(source, destination,graph):
    visited=set()
    path=[]
    dfs_find_all_members(source, destination, graph, visited,path)
    print(path)







graph={'1': ['0', '2'], '0': ['1', '2', '3'], '2': ['0', '1'], '3': ['0', '4'], '4': ['3']}




path_find('1','2',graph)
