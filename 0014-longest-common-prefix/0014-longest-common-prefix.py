class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)

        if n == 1:
            return strs[0]

        ans = strs[0]

        if ans == "":
            return ""

        for i in range(1, n):
            elem = strs[i]

            if elem == "":
                return ""

            result = ""

            ans_len = len(ans)
            elem_len = len(elem)

            j = 0
            k = 0

            while j < elem_len and k < ans_len:
                if elem[j] == ans[k]:
                    result += elem[j]
                    j += 1
                    k += 1
                else:
                    ans = result
                    break
            
            ans = result

        return ans
