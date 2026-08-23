class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * 2*n

        stack = []

        for i in range(2*n - 1, -1, -1):
            elem = nums[i%n]
            while stack and stack[-1] <= elem:
                stack.pop()

            if stack:
                result[i] = stack[-1]
            else:
                result[i] = -1
            
            stack.append(elem)
        print(result)
        for i in range(n):
            result.pop()

        return result