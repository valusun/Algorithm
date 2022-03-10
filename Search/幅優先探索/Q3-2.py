# https://algo-method.com/tasks/418

from collections import deque

N,M = map(int,input().split())
Graph = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    Graph[a].append(b)
    Graph[b].append(a)

Q = deque()
Q.append(0)
dist = [-1]*N
dist[0] = 0

while Q:
    v = Q.popleft()
    for u in Graph[v]:
        if dist[u] != -1:
            continue
        dist[u] = dist[v]+1
        Q.append(u)

print(max(dist))