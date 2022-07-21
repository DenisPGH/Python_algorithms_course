from collections import deque


def bfs(node, graph, visited):
    if node in visited:
        return
    queue=deque([node])
    visited.add(node)


    while queue:
        current_node=queue.popleft()
        print(current_node)
        for child in graph[current_node]:
            if child not in visited:
                queue.append(child)
                visited.add(child)





graph ={
    1 :[2 ,3 ,4],
    2 :[3],
    3 :[],
    4 :[],

}

visited=set()




for node in graph:
    bfs(node,graph,visited)


