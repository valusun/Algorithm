# https://algo-method.com/tasks/368

N = int(input())

l = 0
r = 100
while (r-l)*100000>1:
    x = (l+r)/2
    res = x*(x*(x+1)+2)+3
    if N-res < 0:
        r = x
    else:
        l = x
print(l)