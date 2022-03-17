# https://algo-method.com/tasks/381

from bisect import bisect_left

N,K = map(int,input().split())
A = sorted(list(map(int,input().split())))

ans = 0
for i in range(N):
    target = K-A[i]
    x = bisect_left(A, target)
    ans += N-x
print(ans)