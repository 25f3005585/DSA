class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        j = 0
        curr_sum = 0
        max_avg = float("-inf")

        for i in range(n):
            curr_sum += nums[i]

            if i - j + 1 > k:
                curr_sum -= nums[j]
                j+=1

            if i - j + 1 == k:
                max_avg = max(max_avg, curr_sum / k)
        
        return max_avg