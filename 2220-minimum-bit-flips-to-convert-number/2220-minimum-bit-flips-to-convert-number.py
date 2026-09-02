class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while start or goal:
            st = start & 1
            go = goal & 1

            if st != go:
                count += 1
            
            start = start >> 1
            goal = goal >> 1
        
        return count