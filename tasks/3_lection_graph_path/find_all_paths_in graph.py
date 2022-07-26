def dfs(start,node, graph, visited,path):
    if node in visited:
        print(path)
        return
    if node not in start:
        return
    visited.append(node)
    path.append(node)
    for kids in graph[node]:
        dfs(start,kids, graph, visited,path)
    return visited

graph={0:[1,2,3],
       1:[0,3],
       2:[0,3],
       3:[0,1,2]}


visited=[]

all_paths=[]
end=False
while True:
   for node in graph:
       visited = []
       path=[]
       a=dfs(graph[node],node,graph,visited,path)
       if a:
           if a in all_paths:
                  end=True

           print(a)
           all_paths.append(a)
   if end:
          break


print(len(all_paths))
