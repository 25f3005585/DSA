class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(1,n,3):
            if nums[i] != nums[i-1]:
                return nums[i-1]
        
        return nums[n-1]