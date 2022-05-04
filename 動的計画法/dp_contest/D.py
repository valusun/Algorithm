def main():
    N, W = map(int, input().split())
    weight, value = [0] * N, [0] * N
    for i in range(N):
        weight[i], value[i] = map(int, input().split())
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(W + 1):
            if j < weight[i]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - weight[i]] + value[i])
    print(dp[N][W])


if __name__ == "__main__":
    main()
