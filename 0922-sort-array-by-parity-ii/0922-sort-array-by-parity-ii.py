class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        n = len(nums)
        for i in range(n):
            elem = nums[i]
            if elem & 1 == 1:
                odd.append(elem)
            else:
                even.append(elem)

        i = 0
        j = 0
        index = 0

        while i < len(even) and j < len(odd):
            if index & 1 == 0:
                nums[index] = even[i]
                i += 1
            else:
                nums[index] = odd[j]
                j += 1
            index += 1

        while i < len(even):
            nums[index] = even[i]
            i += 1
            index += 1

        while j < len(odd):
            nums[index] = odd[j]
            j += 1
            index += 1

        return nums
