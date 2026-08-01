class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        n = len(s)

        for i in range(n):
            number = ord(s[i])
            if (65 <= number <= 90) or (97 <= number <= 122) or (48 <= number <= 57):
                t += s[i].lower()

        n = len(t)
        
        if n == 0:
            return True

        start = 0
        end = n - 1

        while start < end:
            if t[start] == t[end]:
                start += 1
                end -= 1
            else:
                return False

        return True
