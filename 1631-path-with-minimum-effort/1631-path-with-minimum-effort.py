import heapq


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        heap = []

        dist = [[float("inf")] * n for _ in range(m)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        dist[0][0] = 0
        heapq.heappush(heap, (0, 0, 0))

        while heap:
            distance, row, col = heapq.heappop(heap)

            for dr, dc in directions:
                nr = dr + row
                nc = dc + col

                if 0 <= nr < m and 0 <= nc < n:
                    heightDiff = abs(heights[row][col] - heights[nr][nc])
                    maxdiff = max(distance, heightDiff)
                    if dist[nr][nc] > maxdiff:
                        dist[nr][nc] = maxdiff
                        heapq.heappush(heap, (maxdiff, nr, nc))
        
        return dist[m-1][n-1]