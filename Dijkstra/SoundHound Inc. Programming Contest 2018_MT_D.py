from dataclasses import dataclass, field
from heapq import heappop, heappush
from typing import ClassVar, Tuple, Optional, List


@dataclass
class Dijkstra:
    vertex_cnt: int
    edge_cnt: int
    graph: List[List[int]] = field(default_factory=list)
    INF: ClassVar[int] = float("inf")

    def GetShortestPaths(
        self, start: int, goal: Optional[int] = None
    ) -> Tuple[List[int], List[int]]:
        """各辺の最短経路を求める

        Returns:
            Tuple[list[int], list[int]: 最短経路 | 直前にどこを通ったかを示す
        """
        goal = self.INF if goal is None else goal
        dist = [self.INF] * self.vertex_cnt
        done = [False] * self.vertex_cnt
        prev = [-1] * self.vertex_cnt
        cost_and_vertex = [(0, start)]
        dist[start] = 0
        while cost_and_vertex:
            now_cost, now_vertex = heappop(cost_and_vertex)
            if done[now_vertex]:
                continue
            if now_vertex == goal:
                break
            for next_cost, next_vertex in self.graph[now_vertex]:
                cost = now_cost + next_cost
                if cost < dist[next_vertex]:
                    dist[next_vertex] = cost
                    prev[next_vertex] = now_vertex
                    heappush(cost_and_vertex, (cost, next_vertex))
            done[now_vertex] = True
        return dist, prev

    def RestoreRoute(
        self, prev: List[int], start: int, goal: int
    ) -> Optional[List[int]]:
        """ゴール地点からスタート地点までの経路を復元する"""
        route = []
        vertex = goal
        while prev[vertex] != -1:
            if vertex == start:
                break
            route.append(vertex)
            vertex = prev[vertex]
        route.append(vertex)
        if route[-1] == start:
            return route[::-1]
        return None


def main():
    n, m, s, t = map(int, input().split())
    yen = [[] for _ in range(n)]
    snuuk = [[] for _ in range(n)]
    for _ in range(m):
        u, v, a, b = map(int, input().split())
        yen[u - 1].append([a, v - 1])
        yen[v - 1].append([a, u - 1])
        snuuk[u - 1].append([b, v - 1])
        snuuk[v - 1].append([b, u - 1])
    yen_dijkstra = Dijkstra(n, m, yen)
    snuuk_dijkstra = Dijkstra(n, m, snuuk)
    yen_dist, _ = yen_dijkstra.GetShortestPaths(s - 1)
    snuuk_dist, _ = snuuk_dijkstra.GetShortestPaths(t - 1)
    money = 10**15
    now_ans = 0
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        now_ans = max(now_ans, money - yen_dist[i] - snuuk_dist[i])
        ans[i] = now_ans
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
