def main():
    N, W = map(int, input().split())
    weight, value = [0] * N, [0] * N
    for i in range(N):
        weight[i], value[i] = map(int, input().split())
    sum_value = sum(value)
    dp = [[10**10] * (sum_value + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(sum_value + 1):
            if j < value[i]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = min(dp[i][j], dp[i][j - value[i]] + weight[i])
    for i in range(sum_value, -1, -1):
        if dp[N][i] <= W:
            print(i)
            break


if __name__ == "__main__":
    main()
