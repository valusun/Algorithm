class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # Returns the root of the tree to which x belongs
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # Union x-tree and y-tree
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    N, M = map(int, input().split())
    graph = []
    for _ in range(M):
        v, u, c = map(int, input().split())
        graph.append([c, v, u])
    graph.sort()
    UF = UnionFind(N)
    total = 0
    for g in graph:
        c, v, u = g
        if not UF.same(v, u):
            UF.union(v, u)
            total += c
    print(total)


if __name__ == "__main__":
    main()
