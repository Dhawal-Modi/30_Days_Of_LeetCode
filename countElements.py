class Solution:
    def countElements(self, arr: List[int]) -> int:
        d = {}
        count = 0
        for i in arr:
            d[i] = 1

        for x in arr:
            if x+1 in d.keys():
                count += 1
        return count
