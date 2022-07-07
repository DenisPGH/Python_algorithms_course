def all_paths_in_labirint(row,col,labirint,direction,path):
    if row<0 or col<0 or row>=len(labirint) or col>=len(labirint[0]):
        return

    if labirint[row][col]=='*':
        return
    if labirint[row][col]=='v':
        return
    path.append(direction)
    if labirint[row][col]=='e':
        print(''.join(path))

    else:
        labirint[row][col]='v'
        all_paths_in_labirint(row-1,col,labirint,'U',path)
        all_paths_in_labirint(row+1,col,labirint,'D',path)
        all_paths_in_labirint(row,col-1,labirint,'L',path)
        all_paths_in_labirint(row,col+1,labirint,'R',path)
        labirint[row][col] = '-'

    path.pop()




matrix=[]
row=int(input())
col=int(input())
for r in range(row):
    matrix.append(list(input()))

#print(matrix)

all_paths_in_labirint(0,0,matrix,'',[])

"""
3
3
---
-*-
--e

"""