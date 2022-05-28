import sys

sys.setrecursionlimit(10**9)


def CalculateSum(number: int) -> int:
    """1からの引数までの総和を求める

    Args:
        number (int): 上限値

    Returns:
        int: 引数までの総和
    """

    if number == 1:
        return 1
    return CalculateSum(number - 1) + number


def main():
    N = int(input())
    print(CalculateSum(N))


if __name__ == "__main__":
    main()
