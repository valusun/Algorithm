def main():
    N = int(input())
    H = list(map(int, input().split()))
    INF = 10**9
    costs = [INF] * N
    costs[0] = 0
    for i in range(N - 1):
        costs[i + 1] = min(costs[i + 1], costs[i] + abs(H[i] - H[i + 1]))
        if i + 2 < N:
            costs[i + 2] = min(costs[i + 2], costs[i] + abs(H[i] - H[i + 2]))
    print(costs[N - 1])


if __name__ == "__main__":
    main()
