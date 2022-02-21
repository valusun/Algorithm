# ----- input ----- #
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# ----- sort ----- #
A.sort()
B.sort()

# ----- greedy ----- #
Ans = 0
for i in range(N):
    Ans += abs(A[i]-B[i])

print(Ans)