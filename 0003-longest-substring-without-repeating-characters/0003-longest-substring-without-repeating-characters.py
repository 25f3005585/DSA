class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        maxLen = 1
        hash_map = {}
        left = 0

        for right in range(n):
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1

            if right - left + 1 > len(hash_map):
                hash_map[s[left]] -= 1

                if hash_map[s[left]] == 0:
                    del hash_map[s[left]]

                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen
