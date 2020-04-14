import heapq
def lastStoneWeight(stones):
    stones = [-val for val in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        max_one = heapq.heappop(stones)
        max_two = heapq.heappop(stones)
        if max_one != max_two:
            heapq.heappush(stones,-abs(max_one-max_two))
    if len(stones) == 0:
        return 0
    print( -stones[0])

if __name__ == "__main__":
    s = list(map(int, input().strip().split()))
    lastStoneWeight(s)
