class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        maximum = max(nums)

        start = 1
        end = maximum

        while start <= end:
            mid = (start + end) // 2
            total_sum = 0

            for num in nums:
                total_sum += (num + mid - 1) // mid

                if total_sum > threshold:
                    break

            if total_sum <= threshold:
                end = mid - 1
            else:
                start = mid + 1

        return start
