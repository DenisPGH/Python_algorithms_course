

def calculation_fibbonacci(num):
    fib_0=1
    fib_1=1
    result=0
    for _ in range(num-1):
        result=fib_0+fib_1
        fib_0,fib_1=fib_1,result
    return result

n=int(input())
res=calculation_fibbonacci(n)
print(res)