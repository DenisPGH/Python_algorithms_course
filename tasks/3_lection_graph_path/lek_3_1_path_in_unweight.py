from collections import deque

def create_graph(edges):
    graph = {}
    for _ in range(edges):
        source, destination = [int(x) for x in input().split(" ")]
        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []
        graph[source].append(destination)

    return graph


def find_shortest_way(start_node,destination_node,graph,nodes):
    visited = [False] * (nodes + 1)
    parent = [None] * (nodes + 1)
    visited[start_node] = True
    queue_ = deque([start_node])
    while queue_:
        node = queue_.popleft()
        if node == destination_node:
            break
        for child in graph[node]:
            if visited[child]:
                continue
            visited[child] = True
            queue_.append(child)
            parent[child] = node

    return visited, parent


def print_way(parent):
    path = deque()
    node = destination_node

    while node is not None:
        path.appendleft(node)
        node = parent[node]
    return path





nodes=int(input())
edges=int(input())
graph= create_graph(edges)
start_node=int(input())
destination_node=int(input())
_,parent=find_shortest_way(start_node,destination_node,graph,nodes)
path_to_target=print_way(parent)
print(f"Shortest path length is: {len(path_to_target)-1}")
print(*path_to_target,sep=' ')




