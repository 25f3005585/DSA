from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = deque()
        n = len(nums)
        answer = float("-inf")

        for i in range(n):
            while q and q[0][1] < i - k:
                q.popleft()
            
            best_previous = 0
            if q:
                best_previous = q[0][0]
            
            best_previous = max(0, best_previous)
            current = nums[i] + best_previous
            answer = max(answer, current)

            while q and q[-1][0] <= current:
                q.pop()
            
            q.append((current, i))
        
        return answer



