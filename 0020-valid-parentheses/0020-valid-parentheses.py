class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)

        if n == 1:
            return False

        for i in range(n):
            elem = s[i]

            if elem in ["(", "{", "["]:
                stack.append(elem)
            else:
                if stack:
                    peak = stack[len(stack)-1]
                else:
                    return False
                if (
                    (elem == ")" and peak == "(")
                    or (elem == "}" and peak == "{")
                    or (elem == "]" and peak == "[")
                ):
                    stack.pop()
                else:
                    break

        return len(stack) == 0
