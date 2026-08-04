class Solution:
    def is_element_exists(self, hash_map, key):
        return hash_map.get(key, False)

    def reverseVowels(self, s: str) -> str:
        hash_map = {
            "a": True,
            "e": True,
            "i": True,
            "o": True,
            "u": True,
            "A": True,
            "E": True,
            "I": True,
            "O": True,
            "U": True,
        }
        
        n = len(s)

        if n == 1:
            return s

        s = list(s)
        i = 0
        j = n - 1

        while i < j:
            if self.is_element_exists(hash_map,s[i]) and self.is_element_exists(hash_map,s[j]):
                s[i] , s[j] = s[j] , s[i]
                i+=1
                j-=1
            elif self.is_element_exists(hash_map,s[i]) and not self.is_element_exists(hash_map,s[j]):
                j-=1
            elif self.is_element_exists(hash_map,s[j]) and not self.is_element_exists(hash_map,s[i]):
                i+=1
            else:
                i+=1
                j-=1
        
        return "".join(s)