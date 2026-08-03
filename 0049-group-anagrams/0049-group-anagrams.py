class Solution:
    def get_encoded_string(self,string):
        hash_map = {}

        for ch in string:
            if ch in hash_map:
                hash_map[ch] += 1
            else:
                hash_map[ch] = 1
        
        return "".join(ch + str(hash_map[ch]) for ch in sorted(hash_map))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if n == 1:
            return [[strs[0]]]
            
        hash_map = {}

        for i in range(n):
            string = strs[i]
            encoded_string = self.get_encoded_string(string)

            if encoded_string in hash_map:
                hash_map[encoded_string].append(string)
            else:
                hash_map[encoded_string] = [string]
        
        return list(hash_map.values())