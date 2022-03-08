# https://algo-method.com/tasks/423

import sys
sys.setrecursionlimit(10**9)

N = int(input())
fib = [-1]*(N+1)
fib[0] = 0
fib[1] = 1

def func(n):
    if fib[n]!=-1:
        return fib[n]
    fib[n] = func(n-1)+func(n-2)
    return fib[n]

print(func(N))