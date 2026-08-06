class Solution:
    def atMostKOdds(self, nums, k):
        left = 0
        count =  0
        oddCount = 0
        n = len(nums)

        for right in range(n):
            if nums[right] % 2 == 1:
                oddCount += 1
            
            while oddCount > k:
                if nums[left] % 2 == 1:
                    oddCount -= 1
                left+=1
            
            count += right - left + 1
        
        return count

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMostKOdds(nums, k) - self.atMostKOdds(nums, k-1)
