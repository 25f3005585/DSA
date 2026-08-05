class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maximum = 0
        arr = [0] * 26
        left = 0

        for right in range(n):
            index = ord(s[right]) - ord('A')
            arr[index] += 1

            maxfreq = 0
            for i in range(26):
                maxfreq = max(maxfreq, arr[i])
            
            change_need = (right - left + 1) - maxfreq

            if change_need > k:
                left_index = ord(s[left]) - ord('A')
                arr[left_index] -= 1
                left+=1

            maximum = max(maximum,right - left + 1)
        return maximum