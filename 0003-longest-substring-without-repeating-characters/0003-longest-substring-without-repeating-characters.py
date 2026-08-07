class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n == 0:
            return 0

        left = 0
        maximum_length = 1
        hash_map = {}

        for right in range(n):
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1

            while right - left + 1 > len(hash_map):
                hash_map[s[left]] -= 1

                if hash_map[s[left]] == 0:
                    del hash_map[s[left]]
                left += 1

            maximum_length = max(maximum_length, (right - left + 1))
        return maximum_length