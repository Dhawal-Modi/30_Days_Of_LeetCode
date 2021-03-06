class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)
        

    def pop(self) -> None:
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []

    def top(self) -> int:
        if not self.is_empty():
            return self.items[-1]
        

    def getMin(self) -> int:
        return min(self.items)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
