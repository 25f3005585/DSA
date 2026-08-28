from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_dq = deque()
        min_dq = deque()

        length = 0
        n = len(nums)
        left = 0

        for right in range(n):
            while max_dq and max_dq[-1] < nums[right]:
                max_dq.pop()
            
            while min_dq and min_dq[-1] > nums[right]:
                min_dq.pop()
            
            max_dq.append(nums[right])
            min_dq.append(nums[right])

            while max_dq and min_dq and max_dq[0] - min_dq[0] > limit:
                if nums[left] == max_dq[0]:
                    max_dq.popleft()
                if nums[left] == min_dq[0]:
                    min_dq.popleft()
                left+=1
            
            length = max(length, right - left + 1)
        return length