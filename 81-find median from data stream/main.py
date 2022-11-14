class Solution:
    def __init__(self):
        self.count = 0
        self.median = 0

        from heapq import heapify
        self.min_heap = list()
        self.max_heap = list()
        heapify(self.min_heap)
        heapify(self.max_heap)

    """
    @param val: a num from the data stream.
    @return: nothing
    """
    def add(self, val):
        # write your code here
        from heapq import heappush, heappop
        self.count += 1
        heappush(self.max_heap, val * -1)

        half = self.count // 2
        if len(self.max_heap) > half:
            heappush(self.min_heap, heappop(self.max_heap) * -1)

        if len(self.min_heap) > half:
            self.median = heappop(self.min_heap)
            heappush(self.max_heap, self.median * -1)
        else:
            self.median = heappop(self.max_heap) * -1
            heappush(self.max_heap, self.median * -1)

    """
    @return: return the median of the all numbers
    """
    def getMedian(self):
        # write your code here
        return self.median


solution = Solution()

solution.add(1)
print(solution.getMedian())
solution.add(2)
print(solution.getMedian())
solution.add(3)
print(solution.getMedian())
solution.add(4)
print(solution.getMedian())
solution.add(5)
print(solution.getMedian())


"""
solution.add(1)
print(solution.getMedian())
solution.add(20)
print(solution.getMedian())
solution.add(5)
print(solution.getMedian())
solution.add(15)
print(solution.getMedian())
solution.add(35)
print(solution.getMedian())
"""

"""
solution.add(1)
print(solution.getMedian())
solution.add(0)
print(solution.getMedian())
solution.add(1)
print(solution.getMedian())
"""