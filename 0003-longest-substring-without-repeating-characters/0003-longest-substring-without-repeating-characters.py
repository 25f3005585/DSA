class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        hash_map = {}
        maximum = 0

        for right in range(n):
            hash_map[s[right]] = hash_map.get(s[right],0) + 1

            while right - left + 1 != len(hash_map):
                hash_map[s[left]]-=1

                if hash_map[s[left]] == 0:
                    del hash_map[s[left]]

                left+=1

            
            if right - left + 1 > maximum:
                maximum = right - left + 1
        
        return maximum