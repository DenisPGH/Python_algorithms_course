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


def find_node_without_parent(dependency):
    for node,depend in dependency.items():
        if depend==0:
            return node
    return None

graph={}
while True:
    node = input()
    if node=='End':
        break
    v,e=node.split("-")
    children=[] if e =="" else [e]
    graph[v]=children
dependency=find_dependency(graph)



cycle=False
for each in dependency:
    node=find_node_without_parent(dependency)
    if node is None:
        cycle=True
        break

if cycle:
    print(f'Acyclic: No')
else:
    print(f"Acyclic: Yes")