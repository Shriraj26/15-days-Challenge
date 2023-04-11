class UnionFind:

    def __init__(self, size):
        self.rank = [1] * size
        self.rootArr = [i for i in range(size)]
        # Store the connected components number
        self.count = size

    def find(self, x):

        if x == self.rootArr[x]:
            return x

        rootNode = self.find(self.rootArr[x])
        self.rootArr[x] = rootNode
        return rootNode

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.rootArr[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.rootArr[rootX] = rootY
            else:
                self.rootArr[rootY] = rootX
                self.rank[rootX] += 1

            # Decrement the count only if their rank is different
            self.count -= 1

    def getCount(self):
        return self.count


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n)

        for i, j in edges:
            uf.union(i, j)

        return uf.getCount()
