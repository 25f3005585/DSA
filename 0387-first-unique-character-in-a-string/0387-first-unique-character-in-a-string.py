class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}

        n = len(s)

        for i in range(n):
            if s[i] in hash_map:
                hash_map[s[i]] += 1
            else:
                hash_map[s[i]] = 1

        for i in range(n):
            if hash_map[s[i]]==1:
                return i
        
        return -1