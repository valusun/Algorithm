# Union-Find
from operator import ne


class UnionFind():
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

    # Returns x-tree number of elements in the tree
    def size(self, x):
        return -self.parents[self.find(x)]

    # Are x and y the same tree?
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # Returns the element of the tree to which x belongs
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    # Returns a list of all root elements
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    # Returns Group Count
    def group_count(self):
        return len(self.roots())


# ----- main ----- #
H,W = map(int,input().split())
UF = UnionFind(H*W)

# ----- Color Memo ----- #
Field = [['.']*W for i in range(H)]

# ----- Color Check 4 ----- #
dh = [1,0,-1,0]
dw = [0,1,0,-1]

Q = int(input())
for i in range(Q):
    t,*a = map(int,input().split())
    if t==1:
        h,w = a[0]-1, a[1]-1
        Field[h][w] = "#"
        for i in range(4):
            next_h = h+dh[i]
            next_w = w+dw[i]
            if 0<=next_h<H and 0<=next_w<W and Field[next_h][next_w]=="#":
                UF.union(h*W+w, next_h*W+next_w)
    else:
        h,w,h1,w1 = a[0]-1,a[1]-1,a[2]-1,a[3]-1
        if UF.same(h*W+w, h1*W+w1) and Field[h][w]==Field[h1][w1]=="#":
            print("Yes")
        else:
            print("No")
