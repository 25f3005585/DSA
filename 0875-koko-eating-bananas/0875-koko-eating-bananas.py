import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = max(piles)
        
        start = 1
        end = maximum
        speed = maximum

        while start <= end:
            mid = (start + end) // 2
            total_time = 0

            for pile in piles:
                total_time += (pile + mid - 1) // mid

                if total_time > h:
                    break
            
            if total_time <= h:
                end = mid - 1
                speed = mid
            else:
                start = mid + 1
        return speed