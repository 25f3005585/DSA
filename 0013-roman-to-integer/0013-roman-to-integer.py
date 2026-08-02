class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0

        n = len(s)

        i = n - 1

        while i >= 0:
            elem = s[i]

            if elem == "V" or elem == "X":
                if i > 0 and s[i-1] == "I":
                    result += (hash_map[elem] - 1)
                    i-=2
                    continue

            if elem == "L" or elem == "C":
                if i > 0 and s[i-1] == "X":
                    result += (hash_map[elem] - 10)
                    i-=2
                    continue
            
            if elem == "D" or elem == "M":
                if i > 0 and s[i-1] == "C":
                    result += (hash_map[elem] - 100)
                    i-=2
                    continue
            
            result += hash_map[elem]
            i-=1
        
        return result
            