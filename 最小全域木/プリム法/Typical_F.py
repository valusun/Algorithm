from heapq import heappush, heappop


def prim(n: int, m: int) -> int:
    """最小全域木を求める

    Args:
        n (int): 頂点数
        m (int): 辺の数

    Returns:
        int: 最小コスト
    """

    graph = [[] for _ in range(n)]
    for _ in range(m):
        v, u, c = map(int, input().split())
        graph[v].append([u, c])
        graph[u].append([v, c])
    marked = [False for _ in range(n)]
    marked[0] = True

    que = []
    for u, c in graph[0]:
        heappush(que, (c, u))

    cost = 0
    while que:
        c, v = heappop(que)
        if marked[v]:
            continue
        marked[v] = True
        cost += c
        for u, c in graph[v]:
            if marked[u]:
                continue
            heappush(que, (c, u))

    return cost


def main():
    N, M = map(int, input().split())
    print(prim(N, M))


if __name__ == "__main__":
    main()
