class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        k = 0
        while True:
            if n > m:
                k += 1
            else:
                return m << k
            m = m >> 1
            n = n >> 1
