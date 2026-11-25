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
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        dsu = DSU(n)

        for u , v in edges:
            u = u - 1
            v = v - 1

            if dsu.find(u) != dsu.find(v):
                dsu.union(u, v)
            else:
                return [u+1 , v+1]