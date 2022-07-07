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
import time

class Counter:
    def __init__(self):
        self.VALUE=0
        self.RANGE=49
        self.VECTOR=6

c=Counter()


def gen_vectors_1_0(index,vector):
    if index >=len(vector):
        #print(*vector,sep='')
        c.VALUE+=1
        return
    for num in range(1,c.RANGE):
        vector[index]=num
        gen_vectors_1_0(index+1,vector)




vector=[None]*c.VECTOR
start=time.time()
gen_vectors_1_0(0,vector)

print(f"all variation= {c.VALUE}, time={(time.time()-start):.3f} sec")
