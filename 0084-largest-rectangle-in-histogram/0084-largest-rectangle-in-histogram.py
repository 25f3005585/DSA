class Solution:
    def next_smaller_element(self, heights):
        n = len(heights)
        arr = [0] * n
        stack = []

        for i in range(n-1, -1 , -1):
            elem = heights[i]

            while stack and stack[-1][0] >= elem:
                stack.pop()
            
            if stack:
                arr[i] = stack[-1][1]
            else:
                arr[i] = -1
            
            stack.append((elem, i))
        return arr
    
    def previous_smaller_element(self, heights):
        n = len(heights)
        arr = [0] * n

        stack = []

        for i in range(n):
            elem = heights[i]

            while stack and stack[-1][0] >= elem:
                stack.pop()
            
            if stack:
                arr[i] = stack[-1][1]
            else:
                arr[i] = -1
            
            stack.append((elem,i))
        return arr

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        next_smaller_element_arr = self.next_smaller_element(heights)
        previous_smaller_element_arr = self.previous_smaller_element(heights)

        for i in range(n):
            elem = heights[i]
            right = next_smaller_element_arr[i] if next_smaller_element_arr[i] != -1 else n
            left = previous_smaller_element_arr[i]
            area = elem * (right - left - 1)
            
            maxArea = max(maxArea, area)
        
        return maxArea