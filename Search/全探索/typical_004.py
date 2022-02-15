# https://atcoder.jp/contests/typical90/tasks/typical90_d

# ----- 入力 ----- #
H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]


# ----- 行方向の合計 ----- #
row_sum = [sum(A[i]) for i in range(H)]


# ----- 列方向の合計 ----- #
column_sum = [sum(A[i][j] for i in range(H)) for j in range(W)]


# ----- 集計 ----- #
B = [[row_sum[i]+column_sum[j]-A[i][j] for j in range(W)] for i in range(H)]


# ----- 出力 ----- #
print(*B, sep="\n")