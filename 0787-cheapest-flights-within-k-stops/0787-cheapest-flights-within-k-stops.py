class Solution:
    def build_adj_list(self, n, edges):
        adj_list = [[] for _ in range(n)]

        for u, v, weight in edges:
            adj_list[u].append((v, weight))

        return adj_list

    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        adj = self.build_adj_list(n, flights)
        q = deque()

        dist = [float("inf")] * n
        dist[src] = 0
        q.append((src, 0, -1))

        while q:
            node, cost, stops = q.popleft()

            for v, wt in adj[node]:
                if dist[v] > cost + wt and stops + 1 <= k:
                    dist[v] = cost + wt
                    q.append((v, cost + wt, stops + 1))

        if dist[dst] == float("inf"):
            return -1

        return dist[dst]
