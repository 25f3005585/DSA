from collections import deque
class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        hash_map = {}
        q = deque()

        for i in range(n):
            if s[i] in hash_map:
                hash_map[s[i]] += 1
            else:
                hash_map[s[i]] = 1
                q.append((s[i], i))
        
    
        while q and hash_map[q[0][0]] > 1:
            q.popleft()

        if not q:
            return -1
        
        return q[0][1]