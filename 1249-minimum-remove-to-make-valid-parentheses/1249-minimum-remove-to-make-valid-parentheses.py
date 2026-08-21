class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        ans = []

        n = len(s)

        for i in range(n):
            elem = s[i]

            if elem == '(':
                stack.append(len(ans))
                ans.append(elem)
            elif elem == ')':
                if stack:
                    stack.pop()
                    ans.append(elem)
            else:
                ans.append(elem)
            
        for num in stack:
            ans[num] = ''

        return "".join(ans)