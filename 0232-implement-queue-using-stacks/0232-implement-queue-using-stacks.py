class MyQueue:

    def __init__(self):
        self.main_stack = []
        self.helper_stack = []

    def push(self, x: int) -> None:
        self.main_stack.append(x)
        return

    def pop(self) -> int:
        if self.empty():
            return -1
        while self.main_stack:
            self.helper_stack.append(self.main_stack.pop())
        
        elem = self.helper_stack.pop()

        while self.helper_stack:
            self.main_stack.append(self.helper_stack.pop())
        
        return elem
        

    def peek(self) -> int:
        while self.main_stack:
            self.helper_stack.append(self.main_stack.pop())
        
        elem = self.helper_stack[-1]

        while self.helper_stack:
            self.main_stack.append(self.helper_stack.pop())
        
        return elem

    def empty(self) -> bool:
        return len(self.main_stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()