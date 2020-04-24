from collections import defaultdict

def subarraySum(nums, k):
    cur_sum = 0
    result = 0
    prev_sum = defaultdict(lambda: 0)
    for i in range(0, len(nums)):
        cur_sum += nums[i]

        if cur_sum == k:
            result += 1

        if cur_sum - k in prev_sum:
            result += prev_sum[cur_sum - k]

        prev_sum[cur_sum] += 1

    return result

if __name__ == "__main__":
    arr = [10, 2, -2, -20, 10]
    Sum = -10
    print(subarraySum(arr, Sum))
