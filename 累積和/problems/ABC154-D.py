from itertools import accumulate

# 区間の期待値の最大値を求めたい(→ 区間計算を行うので、累積和で解けないかを考えてみる)
# まずは各サイコロの期待値を求める。
# その後は累積和を取って、K個のサイコロを選んだ時の期待値の総和を算出する


def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))

    # 期待値の算出
    expected_values = []
    for p_ in p:
        # 期待値 = 1 * (1/p_) + ... + p_ * (1/p_) = (1+...+p_) * (1/p_)
        sum_ = (p_ * (p_ + 1)) // 2
        expected_values.append(sum_ * (1 / p_))

    # 累積和
    cu_sum = [0] + list(accumulate(expected_values))

    # 区間の期待値 = cu_sum[i] - cu_sum[i-K]
    ans = 0
    for i in range(K, N + 1):
        ans = max(ans, cu_sum[i] - cu_sum[i - K])
    print(ans)


if __name__ == "__main__":
    main()
