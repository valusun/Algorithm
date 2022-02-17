# https://atcoder.jp/contests/typical90/tasks/typical90_j

# ----- input ----- #
N = int(input())
Class1 = []
Class2 = []
for i in range(N):
    c,p = map(int,input().split())
    if c==1:
        Class1.append(p)
        Class2.append(0)
    else:
        Class1.append(0)
        Class2.append(p)

# ----- Cusum ----- #
Class1_sum = [0]
Class2_sum = [0]
for i in Class1:
    Class1_sum.append(Class1_sum[-1]+i)
for i in Class2:
    Class2_sum.append(Class2_sum[-1]+i)

# ----- Query ----- #
Q = int(input())
for i in range(Q):
    l,r = map(int,input().split())
    print(Class1_sum[r]-Class1_sum[l-1], Class2_sum[r]-Class2_sum[l-1])