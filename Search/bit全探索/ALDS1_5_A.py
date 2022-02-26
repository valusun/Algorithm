n = int(input())
A = list(map(int,input().split()))
q = int(input())
B = list(map(int,input().split()))

Choose_A_Sum = set()
for i in range(1, 2**n):
    sum = 0
    for j in range(n):
        if i&(1<<j):
            sum+=A[j]
    Choose_A_Sum.add(sum)

for i in range(q):
    if B[i] in Choose_A_Sum:
        print("yes")
    else:
        print("no")