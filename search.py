class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if (nums == None or len(nums) == 0):
            return -1
        
        left = 0
        right = len(nums)-1
        
        while left < right:
            midpoint = left + (right - left)//2
            if(nums[midpoint]>nums[right]):
                left = midpoint+1
            else:
                right = midpoint
                
        start = left
        left = 0
        right = len(nums) - 1
        
        if (target >=nums[start] and target <= nums[right]):
            left = start
        else:
            right = start
            
        while(left <= right):
            midpoint = left + (right - left)//2
            if (nums[midpoint] == target):
                return midpoint
            elif (nums[midpoint] < target):
                left = midpoint+1
            else:
                right = midpoint-1
        return -1

test_list = [4,5,6,7,0,1,2]
print(search(test_list, 3))
print(search(test_list, 6))
