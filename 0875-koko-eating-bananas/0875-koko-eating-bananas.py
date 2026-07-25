import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        maximum = float("-inf")

        for i in range(n):
            maximum = max(maximum, piles[i])
        
        start = 1
        end = maximum
        speed = maximum

        while start <= end:
            mid = (start + end) // 2
            total_time = 0

            for i in range(n):
                value = math.ceil(piles[i] / mid)
                total_time += value

                if total_time > h:
                    break
            
            if total_time <= h:
                end = mid - 1
                speed = mid
            else:
                start = mid + 1
        return speed