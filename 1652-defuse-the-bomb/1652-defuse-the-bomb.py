class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            for i in range(n):
                code[i] = 0
            return code

        if k > 0:
            ans = []
            curr_sum = 0
            for i in range(1, k + 1):
                curr_sum += code[i]

            ans.append(curr_sum)

            for i in range(k + 1, k + n):
                curr_sum += code[i % n] - code[(i - k) % n]
                ans.append(curr_sum)

            return ans
        else:
            ans = [0] * n
            index = n - 1
            k = abs(k)
            curr_sum = 0

            for i in range(n - 2, n - 2 - k, -1):
                curr_sum += code[i]

            ans[index] = curr_sum
            index += -1

            for i in range(n - 2 - k, - k - 2 , -1):
                curr_sum += code[i] - code[i + k]
                ans[index] = curr_sum
                index += -1

            return ans
