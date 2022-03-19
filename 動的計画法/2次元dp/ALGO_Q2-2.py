# https://algo-method.com/tasks/325

N = int(input())
dp = []
for i in range(N):
    if i:
        dp.append([0]*N)
    else:
        dp.append(list(map(int,input().split())))

for i in range(1, N):
    for j in range(N):
        dp[i][j] = dp[i-1][j]
        if j>0:
            dp[i][j] = (dp[i][j]+dp[i-1][j-1])%100
        if j<N-1:
            dp[i][j] = (dp[i][j]+dp[i-1][j+1])%100

print(dp[N-1][N-1])