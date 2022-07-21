#graph={'K': ['X', 'J'], 'J': ['K', 'N'], 'N': ['J', 'X', 'L', 'M'], 'X': ['K', 'N', 'Y'], 'M': ['N', 'I'], 'Y': ['X', 'L'], 'L': ['N', 'I', 'Y'], 'I': ['M', 'L'], 'A': ['Z', 'Z', 'Z'], 'Z': ['A', 'A', 'A'], 'F': ['E', 'B', 'P'], 'E': ['F', 'P'], 'P': ['B', 'F', 'E'], 'B': ['F', 'P']}
graph={1:[2,5],2:[3],3:[4],4:[],5:[]}
def dfs(node, graph, visited,path):
    if node in visited:
        return
    visited.append(node)
    path.clear()
    for kids in graph[node]:
        dfs(kids, graph, visited,path)
        path.add(kids)
        print(path)
    return path


visited=[]
for node in graph:
    path=set()
    a=dfs(node,graph,visited,path)
    #print(a)
    # if a != None:
    #     print(a)


