

# #matrix = [
#     ['A', 'B', 'C', 'D'],
#     ['E', 'F', 'G', 'H'],
#     ['I', 'J', 'K', 'L'],
#     ['M', 'N', 'O', 'P']
# ]
matrix=[["*************************************************************************************"],
        ["*---------------------------------*------------------------*------------------------*"],
        ["*---------------------------------*------------------------*------------------------*"],
        ["*---------------------------------*------------------------*------------------------*"],
        ["*---------------------------------*-------------------------------------------------*"],
        ["*---------------------------------*-------------------------------------------------*"],
        ["*----------------------------------------------------------*------------------------*"],
        ["*----------------------------------------------------------*------------------------*"],
        ["*-----*******************************************************************************"],
        ["*-----------------------------------------------------------------------------------*"],
        ["*-----------------------------------------------------------------------------------*"],
        ["*--------------------------------**-------------------------------------------------*"],
        ["*--------------------------------**-------------------------------------------------*"],
        ["*--------------------------------**-------------------------------------------------*"],
        ["*--------------------------------**-------------------------------------------------*"],
        ["*--------------------------------**-------------------------*************************"],
        ["*--------------------------------**-------------------------**----------------------*"],
        ["*--------------------------------**-------------------------**----------------------*"],
        ["*--------------------------------**----------------------------------------e--------*"],
        ["*--------------------------------**-------------------------------------------------*"],
        ["*--------------------------------**-------------------------**----------------------*"],
        ["*************************************************************************************"],
        ]
matrix=[list(x[0]) for x in matrix]
print(matrix)
# matrix = [
#     ['A', 'B', 'C', 'D'],
#     ['E', 'F', 'G', 'H'],
#     ['I', 'J', 'K', 'L'],
#     ['M', 'N', 'O', 'P']
# ]
# print(matrix[0])
def add(adj_list, a, b):
    adj_list.setdefault(a, []).append(b)
    adj_list.setdefault(b, []).append(a)

adj_list = {}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j < len(matrix[i]) - 1:
            add(adj_list, matrix[i][j], matrix[i][j+1])
        if i < len(matrix[i]) - 1:
            try:
                for x in range(max(0, j - 1), min(len(matrix[i+1]), j+2)):
                    add(adj_list, matrix[i][j], matrix[i+1][x])
            except:
                print('error')

import pprint
pprint.pprint(adj_list)