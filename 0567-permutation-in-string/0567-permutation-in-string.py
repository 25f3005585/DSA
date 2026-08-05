class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        k = len(p)
        n = len(s)

        arr1 = [0] * 26
        arr2 = [0] * 26
        ans = []

        for i in range(k):
            index = ord(p[i]) - ord('a')
            arr1[index] += 1

        left = 0

        for right in range(n):
            index = ord(s[right]) - ord('a')
            arr2[index] += 1

            if right - left + 1 > k:
                left_index = ord(s[left]) - ord('a')
                arr2[left_index] -= 1
                left += 1

            if right - left + 1 == k:
                is_anagram = True
                for i in range(26):
                    if arr1[i] != arr2[i]:
                        is_anagram = False
                        break
                
                if is_anagram:
                    return True

        return False