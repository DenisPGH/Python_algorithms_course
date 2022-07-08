def recursive_generation(index, vector,range_):
    if index >= len(vector):
        print(*vector, sep=' ')
        return
    for num in range(1,range_):
        vector[index] = num
        recursive_generation(index + 1, vector,range_)


def print_all_combiantion_in_range_number(num):
    vector=[None]*num
    recursive_generation(0,vector,num+1)




n=int(input())
print_all_combiantion_in_range_number(n)