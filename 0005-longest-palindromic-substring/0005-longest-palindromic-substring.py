class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        res_len = 0

        for i in range(n):
            low = i
            high = i

            while low >= 0 and high < n and s[low] == s[high]:
                if high - low + 1 > res_len:
                    res_len = high - low + 1
                    res = s[low:high+1]

                low -= 1
                high += 1
            
            low = i
            high = i+1

            while low >= 0 and high < n and s[low] == s[high]:
                if high - low + 1 > res_len:
                    res_len = high - low + 1
                    res = s[low:high+1]

                low -= 1
                high += 1
        
        return res

                