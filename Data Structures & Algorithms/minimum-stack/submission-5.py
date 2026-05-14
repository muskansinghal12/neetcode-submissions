from collections import deque
class MinStack:

    def __init__(self):
        self.stack = []
        self.supporting_stack = []

    def push(self, val: int) -> None:
        if not self.stack or val <= self.supporting_stack[-1]:
            self.supporting_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.supporting_stack[-1]:
                self.stack.pop()
                self.supporting_stack.pop()
            else:
                self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1
        

    def getMin(self) -> int:
        if self.supporting_stack:
            return self.supporting_stack[-1]
        return -1
        
