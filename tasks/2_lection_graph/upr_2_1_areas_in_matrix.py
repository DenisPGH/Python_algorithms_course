def for_print(mat):
    for row in mat:
        print(' '.join([str(a) for a in row]))
    print()



def count_fileds(row, col, matrix,current_sign):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    # if matrix[row][col]== current_sign:
    #     return 1
    if matrix[row][col] !=current_sign:
        return 0
    if matrix[row][col] =='*':
        return 0
    else:
        result=1
        matrix[row][col]='*'
        result+=count_fileds(row+1, col, matrix,current_sign)
        result+=count_fileds(row-1, col, matrix,current_sign)
        result+=count_fileds(row, col+1, matrix,current_sign)
        result+=count_fileds(row, col-1, matrix,current_sign)
        return result


found_fields_dict={} # { random:{x:1,y:1,size:1}}
x,y,size='x','y','size'
letter='letter'
found_fields=[]
counter_all_found_fields=0

matrix=[]
row=int(input())
col=int(input())
for r in range(row):
    matrix.append(list(input()))
#matrix=['aacccaac',
'baaaaccc',
'baabaccc',
'bbdaaccc',
'ccdccccc',
'ccdccccc'
        #]
#matrix=['aaa','aaa','aaa']
#matrix=[list(x) for x in matrix]



#for_print(matrix)
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        curent_sign=matrix[row][col]
        size_=count_fileds(row, col, matrix,curent_sign)
        if size_ !=0:
            counter_all_found_fields+=1
            if curent_sign not in found_fields_dict:
                found_fields_dict[curent_sign]=0
            found_fields_dict[curent_sign]+=1
            #print(size_)

#for_print(matrix)
#print(found_fields_dict)

print(f'Areas: {counter_all_found_fields}')
for k, v in sorted(found_fields_dict.items(),key=lambda x:(x[0])):
    print(f"Letter '{k}' -> {v}")

"""
6
8
aacccaac
baaaaccc
baabaccc
bbdaaccc
ccdccccc
ccdccccc

"""








