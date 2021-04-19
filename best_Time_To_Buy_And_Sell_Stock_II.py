def maxProfit(prices):
    diff = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            diff += prices[i]-prices[i-1]
    return diff


if __name__ == "__main__":
    n = list(map(int, input().split()))
    maxProfit(n)
