class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minNum  = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        print(self.minStack)
        if not self.minStack:
            self.minStack.append(val)   
        else:
            minVal = min(val, self.minStack[-1])
            self.minStack.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

    # def print(self) -> None:
    #     print(self.stack, self.minNum)
        
