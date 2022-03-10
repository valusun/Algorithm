# https://algo-method.com/tasks/536

from collections import deque

N,M = map(int, input().split())
Graph = [[] for _ in range(N)]
Dep_cnt = [0]*N
for i in range(M):
    f,s = map(int,input().split())
    Graph[f].append(s)
    Dep_cnt[s]+=1

Q = deque()
for i in range(N):
    if Dep_cnt[i] == 0:
        Q.append(i)

while Q:
    v = Q.popleft()
    for u in Graph[v]:
        Dep_cnt[u]-=1
        if Dep_cnt[u]==0:
            Q.append(u)

for i in range(N):
    if Dep_cnt[i] != 0:
        print("No")
        break
else:
    print("Yes")