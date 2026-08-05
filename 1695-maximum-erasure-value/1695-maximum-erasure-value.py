class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        total = 0
        max_total = 0

        left = 0
        hash_map = {}

        for right in range(n):
            hash_map[nums[right]] = hash_map.get(nums[right], 0) + 1

            while right - left + 1 != len(hash_map):
                total -= nums[left]
                hash_map[nums[left]] -= 1
                if hash_map[nums[left]] == 0:
                    del hash_map[nums[left]]
                left += 1
            
            total += nums[right]
            max_total = max(max_total, total)
        
        return max_total