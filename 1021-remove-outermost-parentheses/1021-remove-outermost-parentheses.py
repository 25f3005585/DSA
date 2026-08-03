class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = []

        for ch in s:
            if ch == "(":
                if stack:
                    ans.append(ch)
                stack.append(ch)
            else:
                stack.pop()
                if stack:
                    ans.append(ch)

        return "".join(ans)