import sys
from math import log

# ----- 入力高速化用 ----- #
input = sys.stdin.readline


# ----- 入力 ----- #
N = int(input())
A = [int(input()) for _ in range(N)]


# ----- 間隔を求める ----- #
# m:間隔数 / spaces:間隔(狭めていきたいので降順にしておく)
m = int(log(2*N+1) / log(3))
spaces = [(3**k-1)//2 for k in range(m, 0, -1)]
cnt = 0


# ----- 挿入ソート ----- #
def insertion_sort(space):
    global cnt
    
    for i in range(space, N):
        Target = A[i]
        j = i-space
        # 挿入位置を求める
        while j>=0 and A[j]>Target:
            A[j+space] = A[j]
            j-=space
            cnt+=1
        A[j+space] = Target


# ----- シェルソート ----- #
for space in spaces:
    insertion_sort(space)


# ----- 出力 ----- #
print(m)
print(*spaces)
print(cnt)
print(*A,sep="\n")