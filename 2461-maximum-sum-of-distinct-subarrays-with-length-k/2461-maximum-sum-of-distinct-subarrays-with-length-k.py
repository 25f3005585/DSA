class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        hash_map = {}
        curr_sum = 0

        for i in range(k):
            curr_sum += nums[i]
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

        max_sum = 0
        if len(hash_map) == k:
            max_sum = curr_sum

        for i in range(k, len(nums)):
            left = nums[i - k]
            right = nums[i]

            curr_sum += right - left

            hash_map[left] -= 1
            if hash_map[left] == 0:
                del hash_map[left]

            hash_map[right] = hash_map.get(right, 0) + 1

            if len(hash_map) == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum