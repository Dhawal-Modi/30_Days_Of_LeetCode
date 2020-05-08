class FirstUnique:

    def __init__(self, nums: List[int]):
        self.lkp = {}
        self.dk = collections.deque()
        
        for n in nums:
            self.add(n)
        

    def showFirstUnique(self) -> int:
        if len(self.dk) == 0:
            return -1
        while len(self.dk) > 0 and self.dk[0] in self.lkp and self.lkp[self.dk[0]] >= 2:
            self.dk.popleft()
            
        if len(self.dk) == 0:
            return -1
        return self.dk[0]
        

    def add(self, value: int) -> None:
        if value in self.lkp:
            self.lkp[value] += 1
        else:
            self.lkp[value] = 1
        self.dk.append(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
