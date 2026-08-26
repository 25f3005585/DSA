class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = float("inf")

    def push(self, value: int) -> None:
        self.minimum = min(self.minimum, value)
        self.stack.append(value)

    def pop(self) -> None:
        elem = self.stack.pop()
        if elem == self.minimum:
            self.minimum = float("inf")
            for i in range(len(self.stack)):
                self.minimum = min(self.minimum, self.stack[i])

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return 0

    def getMin(self) -> int:
        if self.minimum:
            return self.minimum
        return 0

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()