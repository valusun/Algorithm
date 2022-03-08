# https://algo-method.com/tasks/430

import sys
sys.setrecursionlimit(10**9)

def func(n,l,r):
    if n==0:
        return 1
    
    if l>r:
        return 0
    
    ans = func(n-1,l+1,r)+func(n,l+1,r)

    return ans

N,L,R = map(int,input().split())
print(func(N,L,R))
