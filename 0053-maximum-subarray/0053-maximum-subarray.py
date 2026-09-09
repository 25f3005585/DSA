class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = float("-inf")
        currSum = 0

        for i in range(n):
            currSum += nums[i]
            maxSum = max(maxSum, currSum)

            if currSum < 0:
                currSum = 0
        
        return maxSum