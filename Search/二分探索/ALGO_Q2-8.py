# https://algo-method.com/tasks/369

N,K = map(int, input().split())
L = list(map(int,input().split()))

ok = 0
ng = 10**5
while abs(ok-ng)>1:
    mid = (ok+ng)/2
    cut_cnt = 0
    for i in range(N):
        cut_cnt += L[i]//mid
    if cut_cnt > K:
        ng = mid
    else:
        ok = mid

print(ok)