class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1 = len(s)
        n2 = len(p)

        if n2 > n1:
            return []
        
        arr1 = [0] * 26
        arr2 = [0] * 26

        left = 0
        result = []

        for i in range(n2):
            index = ord(p[i]) - ord('a')
            arr2[index] += 1

        for right in range(n1):
            index = ord(s[right]) - ord('a')
            arr1[index] += 1

            if right - left + 1 > n2:
                left_index = ord(s[left]) - ord('a')
                arr1[left_index] -= 1
                left += 1
            
            is_anagram = True
            for i in range(26):
                if arr1[i] != arr2[i]:
                    is_anagram = False
                    break
            
            if is_anagram:
                result.append(left)
        
        return result
