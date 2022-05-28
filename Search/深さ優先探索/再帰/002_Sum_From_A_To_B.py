import sys

sys.setrecursionlimit(10**9)


def CalculateSum(start_num: int, end_num: int) -> int:
    """引数間の総和を求める

    Args:
        start_num (int): 開始値
        end_num (int): 終了値

    Returns:
        int: 開始値から終了値までの総和
    """

    if end_num == start_num:
        return start_num
    return CalculateSum(start_num, end_num - 1) + end_num


def main():
    A, B = map(int, input().split())
    print(CalculateSum(A, B))


if __name__ == "__main__":
    main()
