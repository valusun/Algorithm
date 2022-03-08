# https://algo-method.com/tasks/438

import sys
sys.setrecursionlimit(10**9)

N,X = map(int,input().split())
A = list(map(int,input().split()))

memo = [[-1]*(X+1) for _ in range(N+1)]
memo[0][0] = 1

def func(i,j):
    if memo[i][j]!=-1:
        return memo[i][j]

    if i==0:
        if j==0:
            memo[i][j] = 1
        else:
            memo[i][j] = 0
    else:
        if j>=A[i-1] and func(i-1, j-A[i-1]) or func(i-1, j):
            memo[i][j] = 1
        else:
            memo[i][j] = 0
    return memo[i][j]
    
if func(N, X):
    print("Yes")
else:
    print("No")