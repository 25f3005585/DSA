class Solution:
    def next_smaller(self, heights,n):
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
    
    def previous_smaller(self,heights, n):
        arr = [0] * n

        stack = []

        for i in range(n):
            elem = heights[i]

            while stack and stack[-1][0] > elem:
                stack.pop()
            
            if stack:
                arr[i] = stack[-1][1]
            else:
                arr[i] = -1
            
            stack.append((elem,i))
        return arr

    def next_greater(self, heights,n):
        arr = [0] * n
        stack = []

        for i in range(n-1, -1 , -1):
            elem = heights[i]

            while stack and stack[-1][0] <= elem:
                stack.pop()
            
            if stack:
                arr[i] = stack[-1][1]
            else:
                arr[i] = -1
            
            stack.append((elem, i))
        return arr
    
    def previous_greater(self,heights, n):
        arr = [0] * n

        stack = []

        for i in range(n):
            elem = heights[i]

            while stack and stack[-1][0] < elem:
                stack.pop()
            
            if stack:
                arr[i] = stack[-1][1]
            else:
                arr[i] = -1
            
            stack.append((elem,i))
        return arr

    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        total_sum = 0

        previous_elem = self.previous_smaller(arr, n)
        next_elem = self.next_smaller(arr, n)

        for i in range(n):
            pr_index = previous_elem[i]
            next_index = next_elem[i] if next_elem[i] != -1 else n

            contribution = (next_index - i) * (i - pr_index)
            total_sum += contribution * arr[i]
        
        return total_sum
    
    def sumSubarrayMax(self, arr: List[int]) -> int:
        n = len(arr)
        total_sum = 0

        previous_elem = self.previous_greater(arr, n)
        next_elem = self.next_greater(arr, n)

        for i in range(n):
            pr_index = previous_elem[i]
            next_index = next_elem[i] if next_elem[i] != -1 else n

            contribution = (next_index - i) * (i - pr_index)
            total_sum += contribution * arr[i]
        return total_sum

    def subArrayRanges(self, nums: List[int]) -> int:
        return self.sumSubarrayMax(nums) - self.sumSubarrayMins(nums)