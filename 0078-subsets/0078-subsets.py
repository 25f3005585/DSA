class Solution:
    def all_subsets(self, nums, index, ans, temp):
        if index == len(nums):
            ans.append(temp.copy())
            return
        temp.append(nums[index])
        self.all_subsets(nums, index + 1, ans, temp)
        temp.pop()
        self.all_subsets(nums, index + 1, ans, temp)
        return

    def subsets(self, nums):
        ans = []
        self.all_subsets(nums, 0, ans, [])
        return ans