class Solution:
    """
    @param arr: an array of integers
    @param k: an integer
    @return: the Kth smallest element in a specific array
    """
    def kth_smallest(self, arr, k):
        # write your code here
        ROWS = len(arr)

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        for row in range(ROWS):
            if len(arr[row]) > 0:
                heappush(heap, (arr[row][0], row, 0))

        count = 1
        while True:
            val, row, col = heappop(heap)
            if count == k:
                return val
            count += 1

            if col + 1 < len(arr[row]):
                heappush(heap, (arr[row][col + 1], row, col + 1))


arr = [
  [1, 5, 7, 9],
  [3, 4],
  [2, 7, 8]
]
k = 5
k = 2

arr = [[],[],[],[],[28],[],[],[],[],[],[34],[23],[57],[],[96],[],[92],[48],[],[18],[],[],[],[],[],[],[20],[80],[],[52],[],[],[74],[97],[],[12],[42],[78],[],[],[],[51],[98],[32],[27],[71],[72],[],[5],[19],[],[17],[80],[],[],[56],[12],[],[37],[],[],[45],[],[],[],[11],[],[],[],[8],[99],[90],[],[74],[32],[87],[],[],[],[],[],[],[],[20],[],[],[],[],[],[38],[],[83],[96],[11],[35],[90],[],[],[77],[56]]
k = 45

solution = Solution()
print(solution.kth_smallest(arr, k))
