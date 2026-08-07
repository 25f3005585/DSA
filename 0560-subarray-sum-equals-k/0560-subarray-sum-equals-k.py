class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hash_map = {}

        hash_map[0] = 1

        prefix_sum = 0
        count = 0

        for i in range(n):
            prefix_sum  += nums[i]

            target = prefix_sum - k

            if target in hash_map:
                count += hash_map[target]

            hash_map[prefix_sum] = hash_map.get(prefix_sum,0) + 1
        
        return count
