from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dq = deque(maxlen=k)
        result = []
        left = 0

        for right in range(n):
            while dq and nums[dq[-1]] < nums[right]:
                x = dq.pop()

            dq.append(right)

            if right - left + 1 > k:
                if dq[0] == left:
                    dq.popleft()
                left+=1

            if right -left + 1 == k:
                result.append(nums[dq[0]])
        
        return result
