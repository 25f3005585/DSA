class Solution:
    def build_adj_list(self, n , edges):
        adj_list = [[] for _ in range(n)]
        
        for v,u, wt in edges:
            adj_list[v].append((u,wt))
            adj_list[u].append((v,wt))
        
        return adj_list
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        adj = self.build_adj_list(n, roads)

        heap = []
        INF = float("inf")
        dist = [INF] * n
        dist[0] = 0
        ways = [0] * n
        ways[0] = 1
        heapq.heappush(heap , (0, 0))

        mod = 10 ** 9 + 7

        while heap:
            distance , node = heapq.heappop(heap)

            for u , weight in adj[node]:
                if distance + weight < dist[u]:
                    dist[u] = distance + weight
                    heapq.heappush(heap , (distance + weight, u))
                    ways[u] = ways[node]
                elif distance + weight == dist[u]:
                    ways[u] = (ways[u] + ways[node]) % mod
        
        return (ways[n-1] % mod)