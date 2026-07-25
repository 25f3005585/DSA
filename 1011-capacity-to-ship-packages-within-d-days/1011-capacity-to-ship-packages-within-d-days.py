class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        start = max(weights)
        end = sum(weights)

        while start <= end:
            mid = (start + end) // 2

            time = 1
            total_sum = 0

            for i in range(n):
                if total_sum + weights[i] > mid:
                    time+=1
                    total_sum = 0
                
                total_sum += weights[i]

                if time > days:
                    break
            
            if time <= days:
                end = mid - 1
            else:
                start = mid + 1
            
        return start
                