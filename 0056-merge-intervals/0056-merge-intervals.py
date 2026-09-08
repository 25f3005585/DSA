class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        ans = []
        ans.append(intervals[0])
        index = 0
        
        for i in range(1,n):
            if intervals[i][0] <= ans[index][1]:
                ans[index][1] = max(intervals[i][1], ans[index][1])
            else:
                ans.append(intervals[i])
                index+=1
        return ans