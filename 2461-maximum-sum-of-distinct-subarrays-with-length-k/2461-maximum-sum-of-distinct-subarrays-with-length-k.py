class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hash_map = {}
        curr_sum = 0

        for i in range(k):
            element = nums[i]
            curr_sum += nums[i]
            if element in hash_map:
                hash_map[element] += 1
            else:
                hash_map[element] = 1
        
        max_sum = 0
        if len(hash_map) == k:
            max_sum = curr_sum
        
        for i in range(k, n):
            left = nums[i-k]
            
            if hash_map[left] == 1:
                del hash_map[left]      
            else:
                hash_map[left] -=1

            right = nums[i]

            if right in hash_map:
                hash_map[right] += 1
            else:
                hash_map[right] = 1
            
            curr_sum = curr_sum - left + right
            if len(hash_map) == k:
                max_sum = max(max_sum, curr_sum) 
            
        return max_sum