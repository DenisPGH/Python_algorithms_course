def dfs(node,graph,visited,cycle):
    if node in cycle:
        raise Exception
    if node in visited:
        return
    visited.add(node)
    cycle.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, cycle)

    cycle.remove(node)


graph={1: [2, 5, 4], 2: [1, 3], 3: [2, 5], 4: [1], 5: [1, 3], 6: [7, 8], 7: [6, 8], 8: [6, 7]}

visited=set()
cycle=set()
try:
    for each in graph:
        dfs(each, graph, visited, cycle)
except:
    print('acyclic no')

