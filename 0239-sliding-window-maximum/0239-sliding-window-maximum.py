from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left = 0
        ans = []
        dq = deque()

        for right in range(n):
            while dq and dq[-1] < nums[right]:
                dq.pop()
            
            dq.append(nums[right])

            if right - left + 1 > k:
                if dq[0] == nums[left]:
                    dq.popleft()

                left+=1

            if right - left + 1 == k:
                ans.append(dq[0])
        
        return ans