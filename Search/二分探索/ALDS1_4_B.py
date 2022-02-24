# ----- input ----- #
n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))

# ----- binary search ----- #
ans = 0
for i in range(q):
    r = n-1
    l = 0
    while l<=r:
        m = (l+r)//2
        if T[i] == S[m]:
            ans+=1
            break
        if T[i] < S[m]:
            r = m-1
        else:
            l = m+1
    
print(ans)