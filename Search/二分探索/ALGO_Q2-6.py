# https://algo-method.com/tasks/399

from bisect import bisect_left

N = int(input())
A = list(map(int,input().split()))
A_sort = sorted(A)

for i in range(N):
    print(bisect_left(A_sort, A[i]))