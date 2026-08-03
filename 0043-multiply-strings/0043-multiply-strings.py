class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "" or num2 == "":
            return "0"

        if num1 == "0" or num2 == "0":
            return "0"

        n1 = len(num1)
        n2 = len(num2)

        result = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                digit_1 = ord(num1[i]) - ord("0")
                digit_2 = ord(num2[j]) - ord("0")
                mul = digit_1 * digit_2
                total = mul + result[i + j + 1]
                result[i + j + 1] = total % 10
                result[i + j] += total // 10

        res_len = len(result)
        k = 0
        while k < res_len and result[k] == 0:
            k += 1

        string = ""
        for i in range(k, res_len):
            string += str(result[i])

        return string
