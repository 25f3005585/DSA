class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        max_window_size = 0
        left = 0
        hash_map = {}

        n = len(nums)

        for right in range(n):
            hash_map[nums[right]] = hash_map.get(nums[right],0) + 1

            while len(hash_map) > 2:
                hash_map[nums[left]] -= 1

                if hash_map[nums[left]] == 0:
                    del hash_map[nums[left]]
                
                left += 1
            
            max_window_size = max(max_window_size, right - left+1)
        return max_window_size