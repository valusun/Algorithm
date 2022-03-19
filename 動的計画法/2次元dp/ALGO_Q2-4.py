# https://algo-method.com/tasks/329

N = int(input())
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i+1!=N:
            dp[i+1][j] += dp[i][j]
        if j+1!=N:
            dp[i][j+1] += dp[i][j]

print(dp[N-1][N-1])