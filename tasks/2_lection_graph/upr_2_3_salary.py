"""
4
NNYN
NNYN
NNNN
NYYN
"""
def for_print(mat):
    for row in mat:
        print(' '.join([str(a) for a in row]))
    print()


def store_in_graph(matrix):
    graph={}
    for node in range(len(matrix)):
        graph[node] = []
        for child in range(len(matrix[node])):
            if matrix[node][child]=='Y':
                graph[node].append(child)
    return graph


matrix=[]
value_nodes=int(input())
for a in range(value_nodes):
    matrix.append(list(input()))


# matrix=['NNYN',
# 'NNYN',
# 'NNNN',
# 'NYYN'
# ]
# matrix=[list(x) for x in matrix]
graph=store_in_graph(matrix)
#print(graph)


def calc_salary_from_children(node,graph):
    salary=0
    if graph[node]==[]:
        return 1
    for child in graph[node]:
        salary+=calc_salary_from_children(child,graph)
    return salary


sum_all_salaries=0
for node in graph:
    salary=calc_salary_from_children(node, graph)
    sum_all_salaries+=salary
    #print(salary)

print(sum_all_salaries)


