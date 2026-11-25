class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.components = n
        self.size = [1] * n

    def union(self, a , b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.size[root_a] < self.size[root_b]:
            root_a , root_b = root_b, root_a


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
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        dsu = DSU(n)
        extraEdges = 0

        for u , v in connections:
            if dsu.find(u) != dsu.find(v):
                dsu.union(u, v)
            else:
                extraEdges += 1
        
        nc = dsu.countComponents() - 1
        
        if extraEdges >= nc:
            return nc
        else:
            return -1