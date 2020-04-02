from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mp = defaultdict(lambda:0)
        n = len(nums)
        
        for i in range(n):
            mp[nums[i]] += 1
            
        for i in range(n):
            if mp[nums[i]] == 1:
                return nums[i]
        return -1
