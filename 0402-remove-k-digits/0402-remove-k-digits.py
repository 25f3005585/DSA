class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)

        if k == n:
            return "0"

        stack = []
        i = 0
        temp = k

        while i < n:
            elem = num[i]

            if temp == 0:
                break

            while stack and temp > 0:
                top = stack[-1]

                if top > elem:
                    stack.pop()
                    temp -= 1
                else:
                    break

            stack.append(elem)
            i += 1

        while i < n:
            elem = num[i]
            stack.append(elem)
            i += 1

        while temp > 0:
            stack.pop()
            temp -= 1

        string = ""

        for i in range(len(stack)):
            string += stack[i]

        j = 0
        while j < len(string) and string[j] == "0":
            j += 1

        return string[j:] if string[j:] else "0"
