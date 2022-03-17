# https://algo-method.com/tasks/407

def func(n,k):
    cnt = 0
    for i in range(n):
        cnt += min(n, k//(i+1))
    return cnt

N,K = map(int,input().split())

ok = 0
ng = N*N
while abs(ok-ng)>1:
    mid = (ok+ng)//2
    if func(N, mid) >= K:
        ng = mid
    else:
        ok = mid

print(ok+1)
    
