def dfs(node, graph, visited):
    if node in visited:
        return
    visited.append(node)
    for kids in graph[node]:
        dfs(kids, graph, visited)

    return visited





graph={
    1:[2,3,4],
    2:[3],
    3:[],
    4:[],

}



visited=[]

for node in graph:
    a=dfs(node,graph,visited)
    if a:
        print(a)

