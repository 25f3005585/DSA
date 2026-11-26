class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.components = n
        self.size = [1] * n

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        self.components -= 1
        return True

    def find(self, x):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def countComponents(self):
        return self.components


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        hash_map = {}
        n = len(accounts)
        dsu = DSU(n)
        ans = []

        for i in range(n):
            arr = accounts[i]
            for j in range(1, len(arr)):
                if accounts[i][j] in hash_map:
                    dsu.union(hash_map[accounts[i][j]], i)
                else:
                    hash_map[accounts[i][j]] = i

        mp = {}
        for key, value in hash_map.items():
            parent = dsu.find(value)
            if parent not in mp:
                mp[parent] = [key]
            else:
                mp[parent].append(key)

        for i in range(n):
            if i not in mp:
                continue
            
            arr = []
            arr.append(accounts[i][0])
            arr += sorted(mp[i])
            ans.append(arr)
        
        return ans