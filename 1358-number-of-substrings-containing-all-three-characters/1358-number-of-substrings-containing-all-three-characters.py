class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        arr = [-1, -1 , -1]

        n = len(s)
        count = 0

        for i in range(n):
            index = ord(s[i]) - ord('a')
            arr[index] = i

            if arr[0] != -1 and arr[1] != -1 and arr[2] != -1:
                count += 1 + min(arr[0], arr[1], arr[2])
        
        return count