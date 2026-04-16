class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif val <= self.min_stack[-1]:
            self.min_stack.append(val)
    def pop(self) -> None:
        if not self.stack:
            return
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
            self.stack.pop()
        else:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        if not self.min_stack:
            return
        else:
            return self.min_stack[-1]
