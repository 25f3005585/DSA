class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curr_sum = sum(nums[:k])
        avg_sum = curr_sum / k

        for i in range(k, n):
            curr_sum = curr_sum + nums[i] - nums[i - k]
            avg_sum = max(curr_sum / k, avg_sum)

        return avg_sum
