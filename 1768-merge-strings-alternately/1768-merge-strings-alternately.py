class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)

        result = [0] * (n1 + n2)
        index = 0

        i = 0
        j = 0

        while i < n1 and j < n2:
            result[index] = word1[i]
            index += 1
            result[index] = word2[j]
            index += 1
            i+=1
            j+=1
        
        while i < n1:
            result[index] = word1[i]
            index += 1
            i+=1

        while j < n2:
            result[index] = word2[j]
            index += 1
            j+=1

        return "".join(result)