class Counter:
    _COUNTER=0

def all_paths_in_labirint(row,col,labirint):
    if row<0 or col<0 or row>=len(labirint) or col>=len(labirint[0]):
        return
    if row==len(labirint)-1 and col==len(labirint[0])-1:
        #print('1 path')
        Counter._COUNTER+=1
    else:
        labirint[row][col]='v'
        all_paths_in_labirint(row+1,col,labirint) # move down
        all_paths_in_labirint(row,col+1,labirint) # move right
        labirint[row][col] = '-'



def create_matrix_from_row_and_col(row,col):
    mat=[]
    for r in range(row):
        mat.append(['-']*col)
    return mat




def solve(row,col):
    matrix=create_matrix_from_row_and_col(row,col)
    all_paths_in_labirint(0, 0, matrix)
    return Counter._COUNTER


row=int(input())
col=int(input())
# row=3
# col=5

res=solve(row,col)

print(res)
