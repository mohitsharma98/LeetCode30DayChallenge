"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minVal = float("inf")
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x < self.minVal:
            self.minVal = x

            
    def UpdateMin(self):
        newMin = float("inf")
        for i in self.stack:
            if i < newMin:
                newMin = i
        self.minVal = newMin
        

    def pop(self) -> None:
        item = self.stack.pop(-1)
        if item == self.minVal:
            self.UpdateMin()
            

    def top(self) -> int:
        if len(self.stack)!=0:
            return self.stack[-1]
        else:
            return 0


    def getMin(self) -> int:
        return self.minVal