class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        minimum = float("inf")
        total_sum = 0

        nums.sort()

        for i in range(n):
            j = i + 1
            k = n - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                diff = abs(sum - target)

                if diff == 0:
                    return sum

                if diff < minimum:
                    minimum = diff
                    total_sum = sum

                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    j += 1
                    k -= 1
        return total_sum
