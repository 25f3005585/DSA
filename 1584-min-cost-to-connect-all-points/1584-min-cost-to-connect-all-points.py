class Solution:
    def prism_algothrim(self,points, n):
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

    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        cost = self.prism_algothrim(points, n)
        return cost
