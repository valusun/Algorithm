# https://algo-method.com/tasks/427

import sys
sys.setrecursionlimit(10**9)

N,X = map(int,input().split())
A = list(map(int,input().split()))

def func(i,j):
    if i==0:
        if j==0:
            return True
        else:
            return False
    else:
        if j>=A[i-1] and func(i-1, j-A[i-1]) or func(i-1, j):
            return True
        else:
            return False
    
if func(N, X):
    print("Yes")
else:
    print("No")