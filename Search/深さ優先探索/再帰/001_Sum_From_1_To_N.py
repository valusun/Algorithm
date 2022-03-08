# https://algo-method.com/tasks/422

import sys
sys.setrecursionlimit(10**9)

def func(n):
    if n==0:
        return 0
    return func(n-1)+n

N = int(input())
print(func(N))