# ----- 入力 ----- #
N = int(input())
A = list(map(int,input().split()))

cnt = 0

# ----- 選択ソート ----- #
for i in range(N-1):
    j_min = i
    swap_flag = False
    for j in range(i+1, N):
        if A[j] < A[j_min]:
            j_min = j
            swap_flag = True
    if swap_flag:
        A[i],A[j_min] = A[j_min],A[i]
        cnt+=1

# ----- 出力 ----- #
print(*A)
print(cnt)