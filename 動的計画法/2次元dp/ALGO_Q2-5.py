# https://algo-method.com/tasks/333

N = int(input())
Field = [list(input()) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if Field[i][j] == '#':
            continue
        if i+1<N and Field[i+1][j] == '.':
            dp[i+1][j] += dp[i][j]
        if j+1<N and Field[i][j+1] == '.':
            dp[i][j+1] += dp[i][j]

print(dp[N-1][N-1])