class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = len(nums) - 1
        for i in range(pos, -1, -1):
            print(i)
            if (i + nums[i] >= pos):
                pos = i
        return pos == 0
