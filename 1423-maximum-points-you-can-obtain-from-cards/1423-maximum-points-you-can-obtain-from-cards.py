class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == n:
            return sum(nums)

        if k == 1:
            if nums[0] > nums[n - 1]:
                return nums[0]
            else:
                return nums[n - 1]

        curr_sum = 0
        for i in range(n - k, n):
            curr_sum += nums[i]

        max_sum = curr_sum

        for i in range(n, n + k):
            curr_sum += nums[i % n] - nums[(i - k) % n]
            max_sum = max(max_sum, curr_sum)

        return max_sum
