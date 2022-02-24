from bisect import bisect_left

# ----- input ----- #
n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))

# ----- binary search ----- #
ans = 0
for i in range(q):
    X = bisect_left(S, T[i])
    if X<n and T[i] == S[X]:
        ans+=1
print(ans)