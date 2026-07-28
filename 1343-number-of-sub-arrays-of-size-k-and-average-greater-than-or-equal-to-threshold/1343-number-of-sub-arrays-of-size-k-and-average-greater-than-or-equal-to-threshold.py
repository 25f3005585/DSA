class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        n = len(nums)
        count = 0
        curr_sum = 0

        for i in range(k):
            curr_sum += nums[i]

        if (curr_sum / k) >= threshold:
            count += 1

        for i in range(k, n):
            curr_sum = curr_sum - nums[i - k] + nums[i]
            if (curr_sum / k) >= threshold:
                count += 1

        return count
