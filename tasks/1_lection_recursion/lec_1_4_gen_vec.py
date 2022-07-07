# def gen_vectors_1_0(index,vector):
#     if index >=len(vector):
#         print(*vector,sep='')
#         return
#     for num in range(2):
#         vector[index]=num
#         gen_vectors_1_0(index+1,vector)
#
#
# number=int(input())
# vector=[None]*number
# gen_vectors_1_0(0,vector)


def gen_vectors_1_0(index,vector):
    if index >=len(vector):
        print(*vector,sep='')
        return
    for num in range(2):
        vector[index]=num
        gen_vectors_1_0(index+1,vector)


number=int(input())
vector=[None]*number
gen_vectors_1_0(0,vector)

