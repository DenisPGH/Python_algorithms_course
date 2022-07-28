class Counter:
    COUNTER=0

def all_paths_in_labirint(row,col,labirint,direction,path):
    if row<0 or col<0 or row>=len(labirint) or col>=len(labirint[0]):
        return

    if labirint[row][col]=='*':
        return
    if labirint[row][col]=='v':
        return
    path.append(direction)
    if labirint[row][col]=='e':
        #print(''.join(path))
        Counter.COUNTER+=1

    else:
        labirint[row][col]='v'
        all_paths_in_labirint(row-1,col,labirint,'U',path)
        all_paths_in_labirint(row+1,col,labirint,'D',path)
        all_paths_in_labirint(row,col-1,labirint,'L',path)
        all_paths_in_labirint(row,col+1,labirint,'R',path)
        labirint[row][col] = '-'

    path.pop()






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
#print(matrix)

all_paths_in_labirint(1,1,matrix,'',[])
print(Counter.COUNTER) # taked too long

