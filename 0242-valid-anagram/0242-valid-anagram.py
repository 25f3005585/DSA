class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26

        if len(s) != len(t):
            return False

        n = len(s)

        for i in range(n):
            ch = s[i]
            index = ord(ch) - 97
            arr[index] += 1

        for i in range(n):
            ch = t[i]
            index = ord(ch) - 97
            arr[index] -= 1

        for i in range(26):
            if arr[i] != 0:
                return False
        
        return True