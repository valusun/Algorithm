# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_6_A

# ----- 入力 ----- #
N = int(input())
A = list(map(int,input().split()))


# ----- カウント ----- #
Count_A = [0]*(max(A)+1)
for i in range(N):
    Count_A[A[i]]+=1


# ----- ソート ----- #
Ans = []
for i in range(max(A)+1):
    while Count_A[i]:
        Ans.append(i)
        Count_A[i]-=1
print(*Ans)
