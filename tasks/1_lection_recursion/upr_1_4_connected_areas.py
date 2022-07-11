def for_print(mat):
    for row in mat:
        print(' '.join([str(a) for a in row]))
    print()

def can_count_this_cell(row,col,field,cells,stars):
    if (row,col) in cells:
        return False
    if row < 0 or col < 0 or row >= len(field) or col >= len(field[0]):
        return False
    if field[row][col]=='*':
        #stars.add((row,col))
        return False
    if field[row][col]=='v':
        return False

    # if field[row][col]=='-':
    #     return True
    return True


def mark_cell(row, col, board, cells,stars):
    board[row][col]='v'
    cells.add((row,col))



def unmark_cell(row, col, board, cells,stars):
    board[row][col]='v'
    # for r,c in stars:
    #     board[r][c]='r'




class Counter:
    COUNTER=0
    STARS=set()





def find_areas_in_matrix(row,col,field,cells,stars):
    # if field[row][col]=='-':
    #     pass
    for coll in range(len(field)):
        if can_count_this_cell(row,coll,field,cells,stars):
            mark_cell(row, coll, field, cells,stars)
            find_areas_in_matrix(row+1,coll,field,cells,stars)
            find_areas_in_matrix(row-1,coll,field,cells,stars)
            find_areas_in_matrix(row,coll+1,field,cells,stars)
            find_areas_in_matrix(row,coll-1,field,cells,stars)
            unmark_cell(row, coll, field, cells,stars)
        # if field[row][coll]=='*':
        #     print('again')
            #unmark_cell(row, coll, field, cells)

    Counter.COUNTER=len(cells)
    Counter.STARS=stars









def all_fields(row,col,field):

    if row < 0 or col < 0 or row >= len(field) or col >= len(field[0]):
        return

    if field[row][col]=='*':
        #field[row][col]='M'
        return
    if field[row][col]=='v':
        return

    if field[row][col]=='-':
        field[row][col]='v'
        all_fields(row-1,col,field)
        all_fields(row+1,col,field)
        all_fields(row,col-1,field)
        all_fields(row,col+1,field)
        #print('back')
        Counter.COUNTER += 1
        #field[row][col] = 'M'
        #field[row][col] = '-'
        all_fields(row, col, field)

    else:
        print('pass')











matrix=[]
row=4 #int(input())
col=9 #int(input())

found_fields_dict={} # { random:{x:1,y:1,size:1}}
x,y,size='x','y','size'


# for r in range(row):
#     matrix.append(list(input()))


#print(matrix)
matrix=[
    list('---*---*-'),
    list('---*---*-'),
    list('---*---*-'),
    list("----*-*--")
]

matrix=[
    list('--**---*-'),
    list('****---*-'),
    list('****---*-'),
    list("----*-*--")
]


# for_print(matrix)
# find_areas_in_matrix(0,0,matrix,set(),set())
# for_print(matrix)


for_print(matrix)
all_fields(0,0,matrix)
for_print(matrix)


# printing
print(f"Total areas found: {len(found_fields_dict)}")
counter=0
for key, value in sorted(found_fields_dict.items(),key= lambda x:(-x[1][size],x[1][x])):
    print(f"Area #{counter} at ({value[x]}, {value[y]}), size: {value[size]}")


print(Counter.COUNTER)
print(Counter.STARS)

"""
4
9
---*---*-
---*---*-
---*---*-
----*-*--

"""