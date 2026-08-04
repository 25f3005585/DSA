class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        for index in range(n):
            i = index
            j = index

            while i >= 0 and j < n and s[i] == s[j]:
                count += 1
                i-=1
                j+=1
            
            i = index
            j = index + 1

            while i >= 0 and j < n and s[i] == s[j]:
                count += 1
                i-=1
                j+=1
                
        return count