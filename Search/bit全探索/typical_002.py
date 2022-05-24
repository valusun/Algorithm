def CheckParentheses(parentheses: str) -> bool:
    """正しいカッコ列かチェックする

    Args:
        parentheses (str): カッコ列

    Returns:
        bool : 正しいカッコ列のときTrue
    """

    length = len(parentheses)
    left_cnt, right_cnt = 0, 0
    for p in parentheses:
        if p == "(":
            left_cnt += 1
        else:
            right_cnt += 1
        if left_cnt > length // 2 or left_cnt < right_cnt:
            return False
    return True


def main():
    N = int(input())
    ans = []
    for i in range(2**N):
        tmp = ""
        for j in range(N):
            if i & (1 << j):
                tmp += "("
            else:
                tmp += ")"
        if CheckParentheses(tmp):
            ans.append(tmp)
    ans.sort()
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
