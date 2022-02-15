# https://atcoder.jp/contests/typical90/tasks/typical90_a

# ----- 入力 ----- #
N,L = map(int,input().split())
K = int(input())
A = list(map(int,input().split()))


# ----- ピース1個分の長さを求めておく ----- #
piece = [A[0]]
for i in range(1, N):
    piece.append(A[i]-A[i-1])
piece.append(L-A[-1])


ans = 0


# ----- 二分探索 ----- #
ok = 0
ng = L
while abs(ok-ng)>1:

    # 最小のピースの大きさ
    mid = (ok+ng)//2

    # 現在のピースの長さ / 切った回数
    now = 0
    cut_cnt = 0
    
    # midを超えたら切っていく
    for i in range(N):
        now+=piece[i]
        # 切った回数は必ずKを超えてはいけない
        if cut_cnt < K and now >= mid:
            cut_cnt+=1
            now = 0
    
    # 切った回数がKに達していない = まだ小さく切れる
    if cut_cnt < K:
        ng = mid
    else:
        # 最後のピースを足して、midに満たしていない = まだ小さく切れる
        if now+piece[-1] < mid:
            ng = mid
        else:
            ans = max(ans, mid)
            ok = mid


# ----- 出力 ----- #
print(ans)
