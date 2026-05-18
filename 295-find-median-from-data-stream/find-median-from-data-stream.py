import heapq

class MedianFinder:

    def __init__(self):

        # Max heap (store negative values)
        self.small = []

        # Min heap
        self.large = []

    def addNum(self, num):

        # Add to max heap
        heapq.heappush(self.small, -num)

        # Balance values between heaps
        if self.small and self.large and (-self.small[0] > self.large[0]):

            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        # Balance sizes
        if len(self.small) > len(self.large) + 1:

            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        if len(self.large) > len(self.small):

            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self):

        # Odd number of elements
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        # Even number of elements
        return (-self.small[0] + self.large[0]) / 2.0