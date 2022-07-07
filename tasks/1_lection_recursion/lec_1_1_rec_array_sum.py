

def calc_num(ind:int,numbers:list):
    sum_=0

    if ind==len(numbers):
        return sum_
    sum_ += numbers[ind]
    return numbers[ind]+ calc_num(ind+1,numbers)




list_nums=[int(x) for x in input().split(" ")]

print(calc_num(0,list_nums))
