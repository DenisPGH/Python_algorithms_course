def for_print(mat):
    for row in mat:
        print(' '.join([str(a) for a in row]))
    print()



def count_fileds(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if matrix[row][col]== '*':
        return 0
    if matrix[row][col]== 'v':
        return 0
    result=1
    matrix[row][col]='v'
    result+=count_fileds(row+1, col, matrix)
    result+=count_fileds(row-1, col, matrix)
    result+=count_fileds(row, col+1, matrix)
    result+=count_fileds(row, col-1, matrix)
    return result


found_fields_dict={} # { random:{x:1,y:1,size:1}}
x,y,size='x','y','size'
found_fields=[]

matrix=[]
row=int(input())
col=int(input())
for r in range(row):
    matrix.append(list(input()))


#
# matrix=[
#     list('---*---*-'),
#     list('---*---*-'),
#     list('---*---*-'),
#     list("----*-*--")
# ]
#
# matrix=[
#     list('--**---*-'),
#     list('****---*-'),
#     list('****---*-'),
#     list("----*-*--")
# ]

#for_print(matrix)






counter=0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        counter+=1
        #print(matrix[row][col])
        size_=count_fileds(row, col, matrix)
        if size_ != 0:
           # print(size_)
            found_fields_dict[counter]={}
            found_fields_dict[counter][x]=row
            found_fields_dict[counter][y]=col
            found_fields_dict[counter][size]=size_




#for_print(matrix)

#print(found_fields_dict)
# printing
print(f"Total areas found: {len(found_fields_dict)}")
counter=0
for key, value in sorted(found_fields_dict.items(),key= lambda x:(-x[1][size])):
#for key, value in found_fields_dict.items():
    counter+=1
    print(f"Area #{counter} at ({value[x]}, {value[y]}), size: {value[size]}")




"""
4
9
---*---*-
---*---*-
---*---*-
----*-*--

"""