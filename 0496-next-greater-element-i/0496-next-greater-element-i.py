class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hash_map = {}

        hash_map[nums2[len(nums2)-1]] = -1
        stack.append(nums2[len(nums2)-1])

        for i in range(len(nums2)-2, -1, -1):
            elem = nums2[i]

            while stack and stack[len(stack)-1] < elem:
                stack.pop()

            if stack:
                hash_map[nums2[i]] = stack[len(stack)-1]
            else:
                hash_map[nums2[i]] = -1

            stack.append(nums2[i])

        ans = []
        for i in range(len(nums1)):
            ans.append(hash_map[nums1[i]])
        
        return ans