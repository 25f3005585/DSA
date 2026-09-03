class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        xor = 0

        for num in nums:
            xor ^= num
        
        rightmost = xor & -xor

        b1 = 0
        b2 = 0

        for num in nums:
            if num & rightmost:
                b1 = b1 ^ num
            else:
                b2 = b2 ^ num

        return [b1,b2]