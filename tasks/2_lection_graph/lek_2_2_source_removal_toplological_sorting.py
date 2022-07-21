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
lenght_graph=int(input())
for node in range(lenght_graph):
    v,e=input().split("->")
    children=[] if e =="" else [x.strip() for x in e.split(", ") ]
    graph[v.strip()]=children
#print(graph)

#graph={'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': ['C', 'F'], 'E': ['D'], 'F': []}
order_=[]
dependency=find_dependency(graph) #{'A': 0, 'B': 1, 'C': 2, 'D': 2, 'E': 1, 'F': 2}




cycle=False
while dependency:
    node_to_remove=find_node_without_parent(dependency)
    if node_to_remove is None:
        cycle=True
        break
    del dependency[node_to_remove]
    order_.append(node_to_remove)
    for child in graph[node_to_remove]:
        dependency[child]-=1



#print(order_)

if cycle:
    print('Invalid topological sorting')
else:
    print(f"Topological sorting: {', '.join(order_)}")