class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        n = len(arr)
         
        hash_map = {}

        for i in range(n):
            if arr[i] in hash_map:
                hash_map[arr[i]] += 1
            else:
                hash_map[arr[i]] = 1

        count = k

        result = ""

        for i in range(n):
            if hash_map[arr[i]] == 1:
                count -= 1

                if count == 0:
                    result += arr[i]
                    break
                    
        return result