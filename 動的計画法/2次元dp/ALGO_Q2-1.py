# https://algo-method.com/tasks/324

dp = [list(map(int,input().split()))]
for _ in range(3): dp.append([0]*4)

for i in range(1, 4):
    for j in range(4):
        dp[i][j] = dp[i-1][j]
        if j>0:
            dp[i][j] += dp[i-1][j-1]
        if j<3:
            dp[i][j] += dp[i-1][j+1]
    
print(dp[3][3])