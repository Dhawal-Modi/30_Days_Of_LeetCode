def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = max_sum
    for i in range(1,len(nums)):
        current_sum = max(nums[i] + current_sum,nums[i])
        max_sum = max(max_sum,current_sum)
    return max_sum

if __name__ == "__main__":
    n = list(map(int,input()))
    maxSubArray(n)
