# https://atcoder.jp/contests/typical90/tasks/typical90_c

from collections import deque

# ----- 入力 ----- #
N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    A,B = map(int,input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)


# ----- vから一番遠い地点とその距離を返す関数 ----- #
def Get_Farthest_from_v(v):

    ret_v,ret_d = v,0

    # ----- bfs ----- #
    Q = deque()
    Q.append((v,0))
    visited = [False]*N
    visited[v] = True

    while Q:
        v,d = Q.popleft()
        for u in graph[v]:
            if visited[u]: continue
            visited[u] = True
            if d+1 > ret_d:
                ret_v = u
                ret_d = d+1
            Q.append((u,d+1))
    
    return ret_v, ret_d


# ----- 出力 ----- #
print(Get_Farthest_from_v(Get_Farthest_from_v(0)[0])[1]+1)