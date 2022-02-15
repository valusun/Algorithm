# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_A

# ----- 入力 ----- #
N = int(input())
A = list(map(int,input().split()))


# ----- 挿入ソート ----- #
for i in range(N):
    
    # 入れ替え対象の要素をTargetに格納しておく
    Target = A[i]

    # 0 ~ [i-1]までは整列済み
    j = i-1

    # 入れ替え対象の要素の格納位置を求める
    while j>=0 and A[j] > Target:
        A[j+1] = A[j]
        j-=1
    
    # 入れ替え対象の要素の挿入
    A[j+1] = Target


    # ----- 出力 ----- #
    print(*A)