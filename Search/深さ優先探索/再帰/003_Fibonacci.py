# https://algo-method.com/tasks/425

import sys
sys.setrecursionlimit(10**9)

def func(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return func(n-1)+func(n-2)

N = int(input())
print(func(N))