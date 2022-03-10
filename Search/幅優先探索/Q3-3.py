# https://algo-method.com/tasks/424

from collections import deque

H,W = map(int,input().split())
sx,sy,gx,gy = map(int,input().split())
Field = [list(input()) for _ in range(H)]
dist = [[-1]*W for _ in range(H)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

Q = deque()
Q.append((sx, sy))
dist[sx][sy] = 0
while Q:
    x,y = Q.popleft()
    if x==gx and y==gy:
        print(dist[gx][gy])
        break
    for i in range(4):
        next_x = x+dx[i]
        next_y = y+dy[i]
        if 0<=next_x<H and 0<=next_y<W and Field[next_x][next_y]=="W" and dist[next_x][next_y]==-1:
            dist[next_x][next_y] = dist[x][y]+1
            Q.append((next_x, next_y))
