# https://algo-method.com/tasks/306

N,M = map(int,input().split())
A = list(map(int,input().split()))

dp = [10**10]*N
dp[0] = 0
dp[1] = A[1]
for i in range(2, N):
    for j in range(1, min(i+1, M+1)):
        dp[i] = min(dp[i], dp[i-j]+A[i]*j)
print(dp[N-1])