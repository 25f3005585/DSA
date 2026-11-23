class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        INF = float("inf")
        dist = [[INF] * n for _ in range(n)]

        count = [0] * n

        for i in range(n):
            dist[i][i] = 0
        
        for u , v , wt in edges:
            dist[u][v] = min(dist[u][v] , wt)
            dist[v][u] = min(dist[v][u] , wt)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i] != INF and dist[j] != INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                
                if dist[i][j] <= distanceThreshold:
                    count[i] += 1
        
        minimumValue = float("inf")
        number = -1

        for i in range(n):
            if count[i] <= minimumValue:
                minimumValue = count[i]
                number = i
        
        return number