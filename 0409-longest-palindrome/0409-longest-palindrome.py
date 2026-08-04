class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)

        if n == 1:
            return 1
        
        hash_map = {}

        for i in range(n):
            if s[i] in hash_map:
                hash_map[s[i]] += 1
            else:
                hash_map[s[i]] = 1
        
        is_all_even = True
        sum_value = 0
        for value in hash_map.values():
            if value % 2 == 0:
                sum_value += value
            else:
                sum_value += (value - 1)
                is_all_even = False
        
        if not is_all_even:
            sum_value += 1
        
        return sum_value
        
