# https://atcoder.jp/contests/typical90/tasks/typical90_b

# ----- 入力 ----- #
N = int(input())

# ----- dfs ----- #
def dfs(s, left, right):
    
    # カッコ列の生成が完了した
    if left+right == N:
        print(s)
        return
    
    # '('がN/2個なければ追加する
    if left < N//2:
        dfs(s+'(', left+1, right)
    
    # ')'が'('よりも少ない時、'('を追加する
    if left > right:
        dfs(s+')', left, right+1)


# ----- dfsへの送り出し ----- #
dfs('', 0, 0)
