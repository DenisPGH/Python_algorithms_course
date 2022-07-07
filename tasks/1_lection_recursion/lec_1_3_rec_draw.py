

def draw_figure(num):
    if num==0:
        return
    print('*'*num)
    draw_figure(num-1)
    print('#' * num)

num=int(input())
draw_figure(num)