def dfs(node, graph, visited):
    if node in visited:
        return
    visited.add(node)
    for kids in graph[node]:
        dfs(kids, graph, visited)

    return visited

graph={}
lenght_graph=int(input())
for node in range(lenght_graph):
    chi=input()
    children=[] if chi =="" else [int(x.strip()) for x in chi.split(" ") ]
    graph[node]=children


#graph={0: [3, 6], 1: [3, 4, 5, 6], 2: [8], 3: [0, 1, 5], 4: [1, 6], 5: [1, 3], 6: [0, 1, 4], 7: [], 8: [2]}

visited=set()
separated_groups=[]
current_group = set()

for node in graph:
    a=dfs(node,graph,visited)
    if a:
        group=a.difference(current_group)
        separated_groups.append(group)
        current_group=a.copy()

for each in separated_groups:
    print(f"Connected component: {' '.join([str(x) for x in each])}")