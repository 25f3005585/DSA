class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        if n > m:
            return ""

        string = ""
        min_length = float("inf")
        count = 0
        hash_map = {}
        left = 0

        for i in range(n):
            hash_map[t[i]] = hash_map.get(t[i],0) + 1
        
        for right in range(m):
            if s[right] in hash_map:
                if hash_map[s[right]] > 0:
                    count += 1
                hash_map[s[right]] -= 1
            else:
                hash_map[s[right]] = -1


            while count == n:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    string = s[left:right+1]
                
                hash_map[s[left]] += 1
                if s[left] in hash_map and hash_map[s[left]] > 0:
                    count -= 1
                left+=1

        return string


        