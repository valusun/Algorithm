# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_6_D

# ----- 入力 ----- #
N = int(input())
A = list(map(int,input().split()))


# ----- 最小コストソート ----- #
B = sorted(A)
Minimum = B[0]
Ans = 0

for i in range(N):
    x = B.index(A[i])
    if x == i:
        continue
    Loop_cnt = 0
    Loop_sum = 0
    Loop_in_minimum = A[i]
    j = i
    while x != i:
        Loop_cnt += 1
        Loop_sum += A[j]
        A[x],A[j] = A[j],A[x]
        x = B.index(A[j])
        Loop_in_minimum = min(Loop_in_minimum, A[j])
    Ans += min(Loop_sum+Loop_cnt*Loop_in_minimum, Loop_sum+(Loop_in_minimum+Minimum)*2+Loop_cnt*Minimum)

print(Ans)