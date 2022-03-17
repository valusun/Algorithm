# https://algo-method.com/tasks/307

N = int(input())
A = list(map(int,input().split()))

dp = [0]
for i in range(N):
    dp.append(max(dp[i], dp[i]+A[i]))
print(dp[N])