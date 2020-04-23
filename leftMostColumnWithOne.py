# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows,columns = binaryMatrix.dimensions()
        cand = -1
        left, right = 0, columns - 1
        while left < rows and right >=0:
            if binaryMatrix.get(left,right) == 1:
                cand = right
                right -= 1
            else:
                left += 1
        return cand
