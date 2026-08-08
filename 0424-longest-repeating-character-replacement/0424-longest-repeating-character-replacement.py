class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        max_length = 0
        arr = [0] * 26

        for right in range(n):
            index = ord(s[right]) - ord('A')
            arr[index] += 1

            maxFreq = arr[0]

            for i in range(26):
                maxFreq = max(maxFreq, arr[i])
            
            while right - left + 1 - maxFreq > k:
                left_index = ord(s[left]) - ord('A')
                arr[left_index] -= 1
                left += 1

                for i in range(26):
                    maxFreq = max(maxFreq, arr[i])
            
            max_length = max(max_length, right - left + 1)
        
        return max_length