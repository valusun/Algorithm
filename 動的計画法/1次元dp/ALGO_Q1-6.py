# https://algo-method.com/tasks/323

N,M = map(int,input().split())
D = list(map(int, input().split()))

dp = [0]*(N+1)
dp[0] = 1
for i in range(N):
    if dp[i]:
        for j in range(M):
            if i+D[j]>N:
                continue
            dp[i+D[j]] = 1
if dp[N]:
    print("Yes")
else:
    print("No")