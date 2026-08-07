class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        length = float("inf")
        total_sum = 0 

        for right in range(n):
            total_sum += nums[right]

            while total_sum >= target:
                length = min(length , right - left + 1)

                total_sum -= nums[left]
                left += 1
        length = length if length != float("inf") else 0
        return length