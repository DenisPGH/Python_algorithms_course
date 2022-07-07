

def find_factoriel(num):
    fac=num
    if num==1:
         return fac
    return fac *find_factoriel(num-1)




number=int(input())

print(find_factoriel(number))