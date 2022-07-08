def for_print(mat):
    for row in mat:
        print(' '.join([str(a) for a in row]))
    print()


def can_put_the_queen_on_that_place(row,col,rows,cols,left_diagonals,right_diagonals):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row+col) in right_diagonals:
        return False

    if (row-col) in left_diagonals:
        return False
    return True


def set_queen(row, col, board, rows, cols,  left_diagonals, right_diagonals):
    board[row][col]='*'
    cols.add(col)
    rows.add(row)
    left_diagonals.add(row-col)
    right_diagonals.add(row+col)

def remove_queen(row, col, board, rows, cols, left_diagonals, right_diagonals):
    board[row][col] = '-'
    cols.remove(col)
    rows.remove(row)
    left_diagonals.remove(row - col)
    right_diagonals.remove(row + col)






def put_queen(row,board,rows,cols,left_diagonals,right_diagonals):
    if row==8:
        for_print(board)
        return
    for col in range(8):
        if can_put_the_queen_on_that_place(row,col,rows,cols,left_diagonals,right_diagonals):
            set_queen(row,col, board,rows, cols, left_diagonals, right_diagonals)
            put_queen(row+1, board, rows, cols,  left_diagonals, right_diagonals)
            remove_queen(row, col, board ,rows, cols,  left_diagonals, right_diagonals)



board=[]
for a in range(8):
    board.append(['-']*8)

#for_print(board)
put_queen(0,board,set(),set(),set(),set())




