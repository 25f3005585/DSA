class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        hash_map = {}

        string = ""

        for i in range(n):
            hash_map[s[i]] = hash_map.get(s[i], 0) + 1

        for key, value in sorted(hash_map.items(), key=lambda x: x[1], reverse=True):
            string += key * value

        return string
