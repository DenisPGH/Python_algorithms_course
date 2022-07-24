

class Edge:
    def __init__(self,first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

edges=int(input())
graph=[]

max_node=float('-inf')
for a in range(edges):
    first, second, weight= [int(x) for x in input().split(", ")]
    graph.append(Edge(first, second, weight))
    max_node=max(first,second,max_node)

parent=[num for num in range(max_node+1)]
forest=[]


def find__root(parent, node):
    while node != parent[node]:
        node=parent[node]
    return node


for edge in sorted(graph,key=lambda x: (x.weight)):
    first_node_root=find__root(parent,edge.first)
    second_node_root=find__root(parent,edge.second)
    if first_node_root !=second_node_root:
        parent[first_node_root]=second_node_root # conect the both node here
        forest.append(edge)


for ed in forest:
    print(f"{ed.first} - {ed.second}")