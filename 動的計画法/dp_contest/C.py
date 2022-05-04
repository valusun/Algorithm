def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * 3 for _ in range(N)]
    dp[0] = A[0]
    for i in range(1, N):
        dp[i][0] = A[i][0] + max(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = A[i][1] + max(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = A[i][2] + max(dp[i - 1][0], dp[i - 1][1])
    print(max(dp[N - 1]))


if __name__ == "__main__":
    main()
