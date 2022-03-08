# https://algo-method.com/tasks/426

import sys
sys.setrecursionlimit(10**9)

A,B = map(int,input().split())

def func(n):
    if n==A:
        return A
    return func(n-1)+n

print(func(B))