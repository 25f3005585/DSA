class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        j = n - 1

        while j >= 0 and s[j] == " ":
            j-=1

        start = j

        j = 0

        while j <= n - 1 and s[j] == " ":
            j += 1
        
        end = j

        if start < end:
            return ""

        ans = []
        word = []

        for i in range(start, end - 1, -1):
            if s[i] != " ":
                word.append(s[i])
            else:
                if s[i] == s[i + 1]:
                    continue

                while word:
                    ans.append(word.pop())

                ans.append(" ")

        while word:
            ans.append(word.pop())

        return "".join(ans)