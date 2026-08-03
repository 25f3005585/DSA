class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)

        for i in range(n-1,-1,-1):
            number = ord(num[i]) - 48

            if number % 2 == 1:
                return num[:i + 1]
        
        return ""

