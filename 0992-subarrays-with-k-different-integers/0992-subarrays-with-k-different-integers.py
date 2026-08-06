class Solution:
    def atMostKDistinct(self, nums, k):
        left = 0
        count =  0
        hash_map = {}
        
        n = len(nums)

        for right in range(n):
            hash_map[nums[right]] = hash_map.get(nums[right],0) + 1
            while len(hash_map) > k:
                hash_map[nums[left]] -= 1
                if hash_map[nums[left]] == 0:
                    del hash_map[nums[left]]
                left+=1
            
            count += (right - left + 1)
        
        return count

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostKDistinct(nums,k) - self.atMostKDistinct(nums, k-1)