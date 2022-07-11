def can_count_this_cell(row,col,field,cells):
    if (row,col) in cells:
        return False
    if row < 0 or col < 0 or row >= len(field) or col >= len(field[0]):
        return False
    if field[row][col]=='*':
        print('a')
        return False
    if field[row][col]=='v':
        return False
    return True


def mark_cell(row, col, board, cells):
    board[row][col]='v'
    cells.add((row,col))



def unmark_cell(row, col, board, rows, cols):
    board[row][col]='-'
    cols.remove(col)
    rows.remove(row)








def find_areas_in_matrix(row,field,cells):
    if row>=len(field):
        print(len(cells))
        return

    for coll in range(len(field)):
        if can_count_this_cell(row,coll,field,cells):
            mark_cell(row, coll, field, cells)
            find_areas_in_matrix(row+1,field,cells)
            # unmark_cell(row, coll, field, rows, cols)







def all_fields(row,col,field):
    if row < 0 or col < 0 or row >= len(field) or col >= len(field[0]):
        return

    if field[row][col]=='*':
        return
    if field[row][col]=='v':
        return

    if field[row][col]=='r':
        print('dd')
        return

    else:
        field[row][col]='v'
        all_fields(row-1,col,field)
        all_fields(row+1,col,field)
        all_fields(row,col-1,field)
        all_fields(row,col+1,field)
        field[row][col] = '-'







matrix=[]
row=int(input())
col=int(input())

found_fields_dict={} # { random:{x:1,y:1,size:1}}
x,y,size='x','y','size'


for r in range(row):
    matrix.append(list(input()))


#print(matrix)

find_areas_in_matrix(0,matrix,set())
#all_fields(0,0,matrix)


# printing
print(f"Total areas found: {len(found_fields_dict)}")
counter=0
for key, value in sorted(found_fields_dict.items(),key= lambda x:(-x[1][size],x[1][x])):
    print(f"Area #{counter} at ({value[x]}, {value[y]}), size: {value[size]}")



"""
4
9
---*---*-
---*---*-
---*---*-
----*-*--

"""