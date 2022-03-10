# https://algo-method.com/tasks/382

from bisect import bisect_right

N,M = map(int,input().split())
A = sorted(list(map(int,input().split())))
B = list(map(int,input().split()))

for i in range(M):
    print(bisect_right(A, B[i]))