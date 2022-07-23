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
    N, K = map(int, input().split())
    Graph = [[] for _ in range(N)]
    for _ in range(K):
        t, *a = map(int, input().split())
        a[0], a[1] = a[0] - 1, a[1] - 1
        if t == 0:
            dijkstra = Dijkstra(N, K, Graph)
            dist, _ = dijkstra.GetShortestPaths(a[0], a[1])
            print(-1 if dist[a[1]] == dijkstra.INF else dist[a[1]])
        else:
            Graph[a[0]].append([a[2], a[1]])
            Graph[a[1]].append([a[2], a[0]])


if __name__ == "__main__":
    main()
