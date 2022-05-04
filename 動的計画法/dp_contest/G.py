import sys

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    Graph = [[] for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        Graph[x - 1].append(y - 1)
    dp = [[0] for _ in range(N)]
    visited = [False] * N

    def dfs(v):
        if visited[v]:
            return dp[v]
        visited[v] = True
        route_count = 0
        for u in Graph[v]:
            route_count = max(route_count, dfs(u) + 1)
        dp[v] = route_count
        return dp[v]

    ans = 0
    for i in range(N):
        ans = max(ans, dfs(i))
    print(ans)


if __name__ == "__main__":
    main()
