# https://algo-method.com/tasks/366

def func(x):
    return x*(x+1)//2

def binary_search(n):
    ok = 0
    ng = 10**18
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if func(mid) >= n:
            ng = mid
        else:
            ok = mid
    return ok+1

N = int(input())
X = list(map(int,input().split()))
for i in range(N):
    print(binary_search(X[i]))