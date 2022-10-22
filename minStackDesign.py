import sys


class MinStack:

    def __init__(self):
        self.stack = []
        self.min = sys.maxsize

    def push(self, val: int) -> None:
        if val <= self.min:
            self.stack.append(self.min)
            self.min = val

        self.stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min:
            self.min = self.stack.pop()

    def top(self) -> int:
        return self.stack.__getitem__(len(self.stack) - 1)

    def getMin(self) -> int:
        return self.min
