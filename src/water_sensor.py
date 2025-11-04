import heapq

"""
HW05 — Water Sensor: Streaming Median

Implement streaming_median(nums) -> list
"""

def streaming_median(nums):
    # max-heap (store negatives)
    low = []
    # min-heap
    high = []

    medians = []

    for x in nums:
        # Step 1: Push new value into correct heap
        if not low or x <= -low[0]:
            heapq.heappush(low, -x)
        else:
            heapq.heappush(high, x)

        # Step 2: Rebalance to maintain size invariant
        if len(low) > len(high) + 1:
            # Move top of low to high
            heapq.heappush(high, -heapq.heappop(low))
        elif len(high) > len(low):
            # Move top of high to low
            heapq.heappush(low, -heapq.heappop(high))

        # Step 3: Record median
        if len(low) > len(high):
            # odd count → median is top of low
            medians.append(float(-low[0]))
        else:
            # even count → average of two tops
            medians.append((-low[0] + high[0]) / 2)

    return medians
