class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)

        start = 1
        end = 10 ** 7
        index = -1

        while start <= end:
            mid = (start + end) // 2
            total_time = 0

            for i in range(n):
                if i == n - 1:
                    total_time += (dist[i] / mid)
                else:
                    total_time += (dist[i] + mid - 1) // mid
                
                if total_time > hour:
                    break
                    
            if total_time <= hour:
                end = mid - 1
                index = mid
            else:
                start = mid + 1
        
        return index