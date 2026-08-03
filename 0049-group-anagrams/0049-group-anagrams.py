class Solution:
    def get_encoded_string(self,string):
        hash_map = {}

        for i in range(len(string)):
            if string[i] in hash_map:
                hash_map[string[i]] += 1
            else:
                hash_map[string[i]] = 1
        
        return "".join(ch + str(hash_map[ch]) for ch in sorted(hash_map))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if n == 1:
            return [[strs[0]]]

        answer = []
        hash_map = {}

        for i in range(n):
            string = strs[i]
            encoded_string = self.get_encoded_string(string)

            if encoded_string in hash_map:
                hash_map[encoded_string].append(string)
            else:
                hash_map[encoded_string] = [string]
        
        for value in hash_map.values():
            answer.append(value)

        return answer
