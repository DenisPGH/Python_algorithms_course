graph={'K': ['X', 'J'], 'J': ['K', 'N'], 'N': ['J', 'X', 'L', 'M'], 'X': ['K', 'N', 'Y'], 'M': ['N', 'I'], 'Y': ['X', 'L'], 'L': ['N', 'I', 'Y'], 'I': ['M', 'L'], 'A': ['Z', 'Z', 'Z'], 'Z': ['A', 'A', 'A'], 'F': ['E', 'B', 'P'], 'E': ['F', 'P'], 'P': ['B', 'F', 'E'], 'B': ['F', 'P']}

def dfs(node, graph, visited):
    if node in visited:
        return
    visited.append(node)
    for kids in graph[node]:
        dfs(kids, graph, visited)
    return visited


visited=[]
for node in graph:
    a=dfs(node,graph,visited)
    print(a)