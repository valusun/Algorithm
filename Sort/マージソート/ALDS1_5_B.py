# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_B&lang=ja

########## スタックオーバーフロー対策 ##########
import sys
sys.setrecursionlimit(10**9)

# ----- input ----- #
N = int(input())
A = list(map(int,input().split()))
cnt = 0

# 番兵
INF = 10**10


# ----- Merge ----- #
def Merge(left, mid, right):
    global cnt
    # 左の要素を格納
    L = A[left:mid]+[INF]
    # 右の要素を格納
    R = A[mid:right]+[INF]
    # LとRの要素を比べながら並び替える
    i,j = 0,0
    for k in range(left, right):
        cnt+=1
        if L[i]<R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1


# ----- MergeSort ----- #
def MergeSort(left, right):
    # 2分割を要素が1になるまで繰り返す
    if abs(right-left)>1:
        mid = (right+left)//2
        MergeSort(left, mid)
        MergeSort(mid, right)
        Merge(left, mid, right)


# ----- Main ----- #
if __name__ == '__main__':
    MergeSort(0, N)
    print(*A)
    print(cnt)