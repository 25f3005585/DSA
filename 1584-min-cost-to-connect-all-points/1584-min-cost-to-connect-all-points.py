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


class Solution:
    def prism_algothrim(self, points, n):
        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                x = abs(points[i][0] - points[j][0])
                y = abs(points[i][1] - points[j][1])
                adj[i].append([j, x + y])
                adj[j].append([i, x + y])

        heap = []
        visited = [False] * n
        heapq.heappush(heap, (0, 0))
        cost = 0

        while heap:
            distance, node = heapq.heappop(heap)
            if visited[node]:
                continue

            cost += distance
            visited[node] = True

            for v, wt in adj[node]:
                if not visited[v]:
                    heapq.heappush(heap, (wt, v))

        return cost

    def kruskal_algothrim(self, points, n):
        edges = []
        cost = 0
        for i in range(n):
            for j in range(i + 1, n):
                x = abs(points[i][0] - points[j][0])
                y = abs(points[i][1] - points[j][1])
                edges.append((i, j, x + y))

        edges.sort(key=lambda x: x[2])
        dsu = DSU(n)

        edges_used = 0

        for u, v, wt in edges:
            if dsu.find(u) != dsu.find(v):
                dsu.union(u, v)
                cost += wt

                edges_used += 1
                if edges_used == n - 1:
                    break

        return cost

    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        # cost = self.prism_algothrim(points, n)
        cost = self.kruskal_algothrim(points, n)
        return cost
