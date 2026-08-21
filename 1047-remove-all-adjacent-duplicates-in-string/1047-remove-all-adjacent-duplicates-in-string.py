class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        n = len(s)

        if n == 1:
            return s

        stack.append(s[0])

        for i in range(1, n):
            elem = s[i]
            if stack:
                peak = stack[len(stack)-1]

                if elem == peak:
                    stack.pop()
                else:
                    stack.append(elem)
            else:
                stack.append(elem)
        
        return "".join(stack)