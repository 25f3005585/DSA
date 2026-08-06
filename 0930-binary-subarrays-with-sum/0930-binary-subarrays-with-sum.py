class Solution:
    def atMostSumK(self, nums, goal):
        if goal < 0:
            return 0
        
        n = len(nums)
        left = 0
        total = 0
        count = 0

        for right in range(n):
            total += nums[right]

            while total > goal:
                total -= nums[left]
                left+=1
            
            count += right - left + 1
        
        return count


    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atMostSumK(nums, goal) - self.atMostSumK(nums, goal-1)