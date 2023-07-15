from itertools import accumulate


def main():
    N = int(input())

    # クラスごとに点数を分配する
    class1, class2 = [], []
    for _ in range(N):
        c, p = map(int, input().split())
        if c == 1:
            c1_p, c2_p = p, 0
        else:
            c1_p, c2_p = 0, p
        class1.append(c1_p)
        class2.append(c2_p)

    # 各クラスの累積和
    cu_sum1 = [0] + list(accumulate(class1))
    cu_sum2 = [0] + list(accumulate(class2))

    # Queryの処理
    Q = int(input())
    for _ in range(Q):
        left, right = map(int, input().split())
        print(f"{cu_sum1[right] - cu_sum1[left-1]} {cu_sum2[right] - cu_sum2[left-1]}")


if __name__ == "__main__":
    main()
