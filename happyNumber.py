def pdi(self,n):
    base = 10
    total = 0
    while n > 0:
        total = total + pow(n % base,2)
        n = n // base
    return total
    
def isHappy(self, n: int) -> bool:
    n_list = []
    while n > 1 and n not in n_list:
        n_list.append(n)
        n = self.pdi(n)
    return n == 1
