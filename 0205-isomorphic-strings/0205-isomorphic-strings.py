class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map = {}
        n = len(s)

        for i in range(n):
            first_elem = s[i]
            second_elem = t[i]

            if first_elem in hash_map:
                if hash_map[first_elem] != second_elem:
                    return False
            else:
                hash_map[first_elem] = second_elem
        
        hash_map = {}

        for i in range(n):
            first_elem = t[i]
            second_elem = s[i]

            if first_elem in hash_map:
                if hash_map[first_elem] != second_elem:
                    return False
            else:
                hash_map[first_elem] = second_elem

        return True