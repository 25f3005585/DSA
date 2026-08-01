class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 1
        ans = ""
        ans += s[0]

        n = len(s)

        for i in range(1, n):
            if s[i] == s[i-1]:
                count += 1

                if count == 3:
                    count -= 1
                    continue
                
                ans += s[i]
                
            else:
                count = 1
                ans += s[i]
            
        return ans