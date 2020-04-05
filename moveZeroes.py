def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    count = 0
    for i in range(len(nums)):
        if(nums[i] != 0):
            nums[count] = nums[i]
            count += 1
            #print(nums[i])
            #print(nums[count])

    while count < len(nums):
        nums[count] = 0
        count += 1

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    moveZeroes(nums)
