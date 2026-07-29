class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
            
        n = len(nums)
        if 2 * k + 1 > n:
            return [-1] * n

        ans = [0] * n

        j = 0
        while j - k < 0:
            ans[j] = -1
            j += 1

        left = j

        j = n - 1
        while j + k > n - 1:
            ans[j] = -1
            j -= 1

        right = j
        index = left
        avg = 0
        curr_sum = 0
        for i in range(left - k, left + k + 1):
            curr_sum += nums[i]

        avg = curr_sum // (2 * k + 1)
        ans[index] = avg
        index += 1

        for i in range(left + k + 1, left + k + 1 + right - left):
            curr_sum += nums[i] - nums[i - 2 * k - 1]
            avg = curr_sum // (2 * k + 1)
            ans[index] = avg
            index += 1

        return ans
