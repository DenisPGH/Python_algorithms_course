

def return_with_recursion(numbers:list,max_ind,result):

    if max_ind<0:
        print(' '.join([str(x) for x in result]))
        return
    result.append(numbers[max_ind])
    return_with_recursion(numbers,max_ind-1,result)



list_nums=[int(n) for n in input().split(' ')]
#list_nums=[1,2,3,4,5,6]

return_with_recursion(list_nums,len(list_nums)-1,[])

