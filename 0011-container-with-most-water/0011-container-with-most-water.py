class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = float("-inf")
        n = len(height)
        i = 0
        j = n - 1

        while i < j:
            min_height = min(height[i],height[j])
            diff = j - i
            area = min_height * diff
            maxArea = max(maxArea, area)

            if height[i] <= height[j]:
                i+=1
            else:
                j-=1
        
        return maxArea