# https://algo-method.com/tasks/429

import sys
sys.setrecursionlimit(10**9)

def func(n,l,r):
    if l>r:
        return []
    if n==0:
        return [""]
    ans = []
    for x in func(n-1,l,r):
        ans.append(str(l)+x)
    for x in func(n,l+1,r):
        ans.append(x)
    return ans

L,R = map(int,input().split())

ans = 0
for i in func(10,0,9):
    if L<=int(i)<=R:
        ans+=int(i)
print(ans)