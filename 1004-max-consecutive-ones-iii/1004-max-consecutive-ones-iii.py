class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        maxCount = 0
        maxFreq = 0

        for right in range(n):
            if nums[right] == 1:
                maxFreq += 1

            while right - left + 1 - maxFreq > k:
                if nums[left] == 1:
                    maxFreq -= 1
                left += 1

            maxCount = max(maxCount, right - left + 1)

        return maxCount
