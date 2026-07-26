class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 1:
            return sum(nums)

        if k == n:
            return max(nums)

        start = max(nums)
        end = sum(nums)

        while start <= end:
            mid = (start + end) // 2

            subarray = 1
            subarray_sum = 0

            for i in range(n):
                if subarray_sum + nums[i] <= mid:
                    subarray_sum += nums[i]
                else:
                    subarray += 1
                    if subarray > k:
                        break
                    subarray_sum = nums[i]

            if subarray <= k:
                end = mid - 1
            else:
                start = mid + 1

        return start
