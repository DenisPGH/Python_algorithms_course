def dfs_find_all_members(node, graph, visited):
    if node in visited:
        return
    visited.add(node)
    for kids in graph[node]:
        dfs_find_all_members(kids, graph, visited)
    return visited

def find_dependency(graph):
    depend_dict={}
    for node,childen in graph.items():
        if node not in depend_dict:
            depend_dict[node]=0
        for child in childen:
            if child not in depend_dict:
                depend_dict[child]=0
            depend_dict[child]+=1
    return depend_dict

def find_node_to_break_cycle(dependency):
    """ it find the node with most parents and return it"""
    for node,depend in sorted(dependency.items(), key=lambda x: (-x[1],x[0])):
        return node


def separate_the_graph_into_connected_groups(graph):
    group_graphs = []
    visited = set()
    current_group = set()
    for node in graph:
        a = dfs_find_all_members(node, graph, visited)
        if a:
            group = a.difference(current_group)
            group_graphs.append(group)
            current_group = a.copy()
    return group_graphs

def delete_connection_between_two_nodes(graph, node,dep):
    pair_node=sorted(graph[node])[0]
    graph[node].remove(pair_node)
    graph[pair_node].remove(node)
    dep[node]-=1
    dep[pair_node]-=1
    return pair_node

def find_node_without_parent(dependency):
    for node,depend in dependency.items():
        if depend==0:
            return node
    return None


# graph={}
# count_nodes=int(input())
# for node in range(count_nodes):
#     v,e=input().split(" -> ")
#     children=[] if e=="" else [x for x in e.split(' ')]
#     graph[v]=children
#
# print(graph)
graph={'K': ['X', 'J'], 'J': ['K', 'N'], 'N': ['J', 'X', 'L', 'M'], 'X': ['K', 'N', 'Y'], 'M': ['N', 'I'], 'Y': ['X', 'L'], 'L': ['N', 'I', 'Y'], 'I': ['M', 'L'], 'A': ['Z', 'Z', 'Z'], 'Z': ['A', 'A', 'A'], 'F': ['E', 'B', 'P'], 'E': ['F', 'P'], 'P': ['B', 'F', 'E'], 'B': ['F', 'P']}

#graph={1: [2, 5, 4], 2: [1, 3], 3: [2, 5], 4: [1], 5: [1, 3], 6: [7, 8], 7: [6, 8], 8: [6, 7]}
 # {1: 3, 2: 2, 5: 2, 4: 1, 3: 2, 6: 2, 7: 2, 8: 2}
groups=separate_the_graph_into_connected_groups(graph)





all_pair_for_removing=[]
for each_graph in groups:
    current_graph={}
    for node in each_graph:
        current_graph[node]=graph[node]
    dependency_cur_graph = find_dependency(current_graph)
    #print(dependency_cur_graph)
    cycle=find_node_without_parent(dependency_cur_graph)
    #print(cycle)
    while True:
        cut_node = find_node_to_break_cycle(dependency_cur_graph)
        #print(cut_node)
        pair_node=delete_connection_between_two_nodes(current_graph,cut_node,dependency_cur_graph)
        #print(cut_node,pair_node)
        all_pair_for_removing.append((cut_node,pair_node))

    #print(dependency_cur_graph)


print(f"Edges to remove: {len(all_pair_for_removing)}")
for pair in all_pair_for_removing:
    print(f"{pair[0]} - {pair[1]}")

#print(graph)




