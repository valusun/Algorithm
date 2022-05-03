def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    INF = 10**9
    costs = [INF] * N
    costs[0] = 0
    for i in range(N - 1):
        for j in range(1, K + 1):
            if i + j < N:
                costs[i + j] = min(costs[i + j], costs[i] + abs(H[i] - H[i + j]))
    print(costs[N - 1])


if __name__ == "__main__":
    main()
