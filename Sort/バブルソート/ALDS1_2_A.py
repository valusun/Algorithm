# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_A

# ----- 入力 ----- #
N = int(input())
A = list(map(int,input().split()))

Ans = 0

# ----- バブルソート ----- #
for i in range(N-1):
    for j in range(N-1):
        if A[j] > A[j+1]:
            A[j],A[j+1] = A[j+1],A[j]
            Ans+=1

# ----- 入力 ----- #
print(*A)
print(Ans)