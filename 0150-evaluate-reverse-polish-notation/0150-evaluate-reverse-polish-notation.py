class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)

        for i in range(n):
            elem = tokens[i]

            if elem not in ['+','-','*','/']:
                integer = int(elem)
                stack.append(integer)
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if elem == '+':
                    stack.append(num1 + num2)
                elif elem == '-':
                    stack.append(num1 - num2)
                elif elem == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
        
        return stack[0]