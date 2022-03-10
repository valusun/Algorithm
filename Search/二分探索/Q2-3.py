# https://algo-method.com/tasks/370

from bisect import bisect_left

N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

for i in range(M):
    print(bisect_left(A, B[i]))