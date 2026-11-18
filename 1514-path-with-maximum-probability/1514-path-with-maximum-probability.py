class Solution:
    def build_adj_list(self, n, edges, succProb):
        adj_list = [[] for _ in range(n)]

        for i, (u, v) in enumerate(edges):
            weight = succProb[i]

            adj_list[u].append((v, weight))
            adj_list[v].append((u, weight))

        return adj_list

    def maxProbability(
        self,
        n: int,
        edges: list[list[int]],
        succProb: list[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adj = self.build_adj_list(n, edges, succProb)
        heap = [(-1, start_node)]
        visited = set()

        while heap:
            prob , node = heapq.heappop(heap)
            visited.add(node)

            if node == end_node:
                return -prob

            for neig, wt in adj[node]:
                if neig not in visited:
                    heapq.heappush(heap, (prob * wt , neig))
        
        return 0
                    