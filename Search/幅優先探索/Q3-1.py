# https://algo-method.com/tasks/414

N,M = map(int,input().split())
Graph = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    Graph[a].append(b)
    Graph[b].append(a)

node = [[] for _ in range(N+1)]
node[0].append(0)

end = [0]*(N+1)
end[0] = 1

for i in range(N):
    for j in node[i]:
        for v in Graph[j]:
            if end[v]:
                continue
            node[i+1].append(v)
            end[v] = 1

for i in range(N):
    node[i].sort()
    print(*node[i])