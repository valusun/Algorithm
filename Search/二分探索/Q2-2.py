# https://algo-method.com/tasks/367

N,M = map(int,input().split())

l = 0
r = 100000
while (r-l)*100000>1:
    x = (r+l)/2
    now = N+1
    for _ in range(5):
        now = now*x+1
    if now<M:
        l = x
    else:
        r = x
print(l)