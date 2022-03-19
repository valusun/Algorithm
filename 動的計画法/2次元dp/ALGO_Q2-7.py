# https://algo-method.com/tasks/335

N = int(input())
Number = [list(map(int,input().split())) for _ in range(N)]

INF = 10**10
dp = [[INF]*N for _ in range(N)]
dp[0][N-1] = Number[0][N-1]

for i in range(N):
    for j in range(N-1,-1,-1):
        if i+1<N:
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+Number[i+1][j])
        if j+1>=0:
            dp[i][j-1] = min(dp[i][j-1], dp[i][j]+Number[i][j-1])
        
print(dp[N-1][0])