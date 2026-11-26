class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.components = n
        self.size = [1] * n

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        self.components -= 1
        return True

    def find(self, x):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def countComponents(self):
        return self.components


class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        row = 0
        col = 0
        n = len(stones)

        for x in stones:
            row = max(row, x[0])
            col = max(col, x[1])

        dsu = DSU(row + col + 2)

        stoneNodes = set()

        for i in range(n):
            newRow = stones[i][0]
            newCol = stones[i][1] + row + 1

            dsu.union(newRow, newCol)

            stoneNodes.add(newRow)
            stoneNodes.add(newCol)

        cnt = 0

        for node in stoneNodes:
            if dsu.find(node) == node:
                cnt += 1

        return n - cnt
