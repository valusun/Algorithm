# ----- input ----- #
n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))

# ----- Linear Search ----- #
ans = 0
for i in range(q):
    for j in range(n):
        if T[i] == S[j]:
            ans+=1
            break

print(ans)