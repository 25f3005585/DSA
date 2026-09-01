class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        element = nums[0]

        for i in range(1,n):
            element ^= nums[i]
        
        return element