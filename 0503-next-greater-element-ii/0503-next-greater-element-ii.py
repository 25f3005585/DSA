class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        stack = []

        for i in range(2*n - 1, -1, -1):
            index = i%n
            elem = nums[index]
            while stack and stack[-1] <= elem:
                stack.pop()

            if stack:
                result[index] = stack[-1]
            else:
                result[index] = -1
            
            stack.append(elem)

        return result