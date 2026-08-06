class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        if n > m:
            return ""

        string = ""
        min_length = float("inf")

        hash_map_t = {}
        hash_map_s = {}
        left = 0

        for i in range(n):
            hash_map_t[t[i]] = hash_map_t.get(t[i],0) + 1
        
        for right in range(m):
            hash_map_s[s[right]] = hash_map_s.get(s[right],0) + 1

            is_window_valid = True
            for key in hash_map_t:
                if hash_map_s.get(key, 0) < hash_map_t[key]:
                    is_window_valid = False
                    break

            while is_window_valid:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    string = s[left:right+1]
                
                hash_map_s[s[left]] -= 1
                if hash_map_s[s[left]] == 0:
                    del hash_map_s[s[left]]
                left += 1

                for key in hash_map_t:
                    if hash_map_s.get(key, 0) < hash_map_t[key]:
                        is_window_valid = False
                        break
            
        return string


        