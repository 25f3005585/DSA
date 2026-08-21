class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        n = len(s)

        for i in range(n):
            elem = s[i]

            if not stack:
                stack.append(elem)
            else:
                if elem == '(':
                    stack.append(elem)
                else:
                    peak = stack[len(stack)-1]
                    if peak == '(':
                        stack.pop()
                    else:
                        stack.append(elem)

        return len(stack)