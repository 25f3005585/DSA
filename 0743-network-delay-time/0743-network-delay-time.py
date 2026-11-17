import heapq
class Solution:
    def build_adj_list(self, n , edges):
        adj_list = [[] for _ in range(n)]
        
        for v,u, wt in edges:
            adj_list[v-1].append((u-1,wt))
        
        return adj_list

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = self.build_adj_list(n,times)
        dist = [float("inf")] * n
        dist[k-1] = 0
        heap = []

        heapq.heappush(heap, (0, k-1))
        
        while heap:
            distance , node = heapq.heappop(heap)

            for v , wt in adj[node]:
                if dist[v] > distance + wt:
                    dist[v] = distance + wt
                    heapq.heappush(heap, (distance + wt, v))
        
        maximum = float("-inf")
        for i in range(n):
            if dist[i] == float("inf"):
                return -1
            
            maximum = max(maximum, dist[i])
        
        return maximum