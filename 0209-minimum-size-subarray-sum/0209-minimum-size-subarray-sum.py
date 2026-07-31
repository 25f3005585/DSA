class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        curr_sum = 0
        length = float("inf")

        for right in range(n):
            curr_sum += nums[right]

            while curr_sum >= target:
                length = min(length, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        length = length if length != float("inf") else 0

        return length
