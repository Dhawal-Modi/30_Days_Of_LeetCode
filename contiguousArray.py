'''O(n^2) Solution

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum = 0
        maxsize = 0
        n = len(nums)
        for i in range(0, n-1): 
            sum = -1 if(nums[i] == 0) else 1
            for j in range(i + 1, n): 
                sum = sum + (-1) if (nums[j] == 0) else sum + 1
                if (sum == 0 and maxsize < j-i + 1):   
                    maxsize = j - i + 1
                    startindex = i
        return maxsize'''

#O(N) Solution
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
            hash_map = {}
            cur_sum = 0
            max_len = 0
            ending_index = -1
            n = len(nums)
            
            for i in range(0,n):
                if(nums[i]==0):
                    nums[i] = -1
                else:
                    nums[i] = 1
                    
            for i in range(0,n):
                cur_sum = cur_sum + nums[i]
                
                if (cur_sum == 0):
                    max_len = i+1
                    ending_index = i
                
                if cur_sum in hash_map:
                    if max_len < i - hash_map[cur_sum]:
                        max_len = i - hash_map[cur_sum]
                        ending_index = i
                else:
                    hash_map[cur_sum] = i
                    
            for i in range(0,n):
                if(nums[i] == -1):
                    nums[i] = 0
                else:
                    nums[i] = 1
            
            return max_len
