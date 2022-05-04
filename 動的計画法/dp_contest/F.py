def main():
    s = input()
    t = input()
    len_s, len_t = len(s), len(t)
    dp = [[0] * (len_t + 1) for _ in range(len_s + 1)]
    for i in range(len_s):
        for j in range(len_t):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    ans = ""
    len_ans = dp[len_s][len_t]
    i, j = len_s, len_t
    while len_ans:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            ans += s[i - 1]
            len_ans -= 1
            i -= 1
            j -= 1
    print(ans[::-1])


if __name__ == "__main__":
    main()
