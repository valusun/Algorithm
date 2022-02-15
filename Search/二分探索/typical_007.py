# https://atcoder.jp/contests/typical90/tasks/typical90_g

from bisect import bisect_right

# ----- 入力 ----- #
N = int(input())
A = sorted(list(map(int,input().split())))
Q = int(input())

# ----- Queryごとの二分探索 ----- #
for i in range(Q):
    B = int(input())
    x = bisect_right(A, B)
    if x == 0:
        print(abs(B-A[0]))
    elif x == N:
        print(abs(B-A[N-1]))
    else:
        print(min(abs(B-A[x-1]), abs(B-A[x])))