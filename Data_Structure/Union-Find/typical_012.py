class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parents = [-1] * n

    def find(self, x: int) -> int:
        """要素が属する木の根を返す

        Args:
            x (int): 探索対象の要素

        Returns:
            int: 引数の要素が属する親
        """

        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x: int, y: int) -> None:
        """引数同士の木の結合を行う

        Args:
            x (int): 木の要素
            y (int): 木の要素
        """

        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x: int) -> int:
        """引数の木が属している要素数を返す

        Args:
            x (int): 要素

        Returns:
            int: 木の要素数
        """

        return -self.parents[self.find(x)]

    def same(self, x: int, y: int) -> bool:
        """同じ木に属しているかの判定を行う

        Args:
            x (int): 木の要素
            y (int): 木の要素

        Returns:
            bool: 同じ木に属しているならばTrue
        """

        return self.find(x) == self.find(y)

    def members(self, x: int) -> list:
        """要素が属する木の要素を取得する

        Args:
            x (int): 要素

        Returns:
            list: 木に属している要素群
        """

        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self) -> list:
        """全ての根の要素を返す

        Returns:
            list: 全ての根の要素
        """

        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self) -> int:
        """木の数を返す

        Returns:
            int: 木の数
        """

        return len(self.roots())


def main():
    H, W = map(int, input().split())
    Q = int(input())
    UF = UnionFind(H * W)
    Field = [["."] * W for i in range(H)]
    dh = [1, 0, -1, 0]
    dw = [0, 1, 0, -1]
    for i in range(Q):
        t, *a = map(int, input().split())
        if t == 1:
            h, w = a[0] - 1, a[1] - 1
            Field[h][w] = "#"
            for i in range(4):
                next_h = h + dh[i]
                next_w = w + dw[i]
                if 0 <= next_h < H and 0 <= next_w < W and Field[next_h][next_w] == "#":
                    UF.union(h * W + w, next_h * W + next_w)
        else:
            h, w, h1, w1 = a[0] - 1, a[1] - 1, a[2] - 1, a[3] - 1
            if UF.same(h * W + w, h1 * W + w1) and Field[h][w] == Field[h1][w1] == "#":
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
