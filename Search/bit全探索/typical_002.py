# https://atcoder.jp/contests/typical90/tasks/typical90_b

# ----- 入力 ----- #
N = int(input())

ans = []

# ----- bit全探索 ----- #
for i in range(2**N):
    # 作成したカッコ列を格納
    tmp = ""
    for j in range(N):
        # 1ならば'('を追加する
        if i&(1<<j):
            tmp+='('
        else:
            tmp+=')'
    
    # 作成したカッコ列が正しいか判定
    left, right = 0,0
    for s in tmp:
        if s=='(':
            left+=1
            if left>N//2:
                break
        if s==')':
            right+=1
            if left < right:
                break
    else:
        ans.append(tmp)

# ----- カッコ列を並び替えて出力 ----- #
ans.sort()
print(*ans, sep="\n")