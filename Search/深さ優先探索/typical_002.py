import sys

sys.setrecursionlimit(10**9)


def dfs(lenght: int, parenthese: str, left: int, right: int) -> None:
    """正しいカッコ列を生成する

    Args:
        lenght (int): カッコ列の長さ
        parenthese (str): "(" と ")" で構成された文字列
        left (int): "(" の数
        right (int): ")"の数
    """

    if left + right == lenght:
        print(parenthese)
        return

    if left < lenght // 2:
        dfs(lenght, parenthese + "(", left + 1, right)

    if left > right:
        dfs(lenght, parenthese + ")", left, right + 1)


def main():
    N = int(input())
    dfs(N, "", 0, 0)


if __name__ == "__main__":
    main()
