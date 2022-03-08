# https://algo-method.com/tasks/428

import sys
sys.setrecursionlimit(10**9)

N,L,R = map(int,input().split())

def func(n,l,r):
    if l>r:
        return []
    if n==0:
        return [[]]
    ans = []
    for x in func(n-1,l,r):
        to = [l]
        to.extend(x)
        ans.append(to)
    ans.extend(func(n,l+1,r))

    return ans

for x in func(N,L,R):
    print(*x)