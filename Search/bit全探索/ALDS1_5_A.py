def main():
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    B = list(map(int, input().split()))

    choose_A_sum = set()
    for i in range(1, 2**n):
        sum = 0
        for j in range(n):
            if i & (1 << j):
                sum += A[j]
        choose_A_sum.add(sum)

    for i in range(q):
        if B[i] in choose_A_sum:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    main()
