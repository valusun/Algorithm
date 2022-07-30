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
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        graph[a - 1].append([c, b - 1])
        graph[b - 1].append([c, a - 1])
    Q, K = map(int, input().split())
    dijkstra = Dijkstra(N, N - 1, graph)
    dist, _ = dijkstra.GetShortestPaths(K - 1)
    for _ in range(Q):
        x, y = map(int, input().split())
        print(dist[x - 1] + dist[y - 1])


if __name__ == "__main__":
    main()
