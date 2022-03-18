# https://algo-method.com/tasks/302

N,X,Y = map(int,input().split())

dp = [0]*N
dp[0] = X
dp[1] = Y

for i in range(2, N):
    dp[i] = (dp[i-2]+dp[i-1])%100
print(dp[N-1])