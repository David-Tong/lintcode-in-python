class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kth_smallest(self, matrix, k):
        # write your code here
        ROWS = len(matrix)
        COLUMNS = len(matrix[0])

        from collections import deque
        bfs = deque()
        bfs.append((matrix[0][0], 0, 0))
        visited = set()
        visited.add((0, 0))

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        count = 1
        while True:
            size = len(bfs)
            for x in range(size):
                val, row, col = bfs.popleft()
                heappush(heap, val)
                if row + 1 < ROWS:
                    if (row + 1, col) not in visited:
                        bfs.append((matrix[row + 1][col], row + 1, col))
                        visited.add((row + 1, col))
                if col + 1 < COLUMNS:
                    if (row, col + 1) not in visited:
                        bfs.append((matrix[row][col + 1], row, col + 1))
                        visited.add((row, col + 1))

            val = heappop(heap)
            if count == k:
                return val
            count += 1


matrix = [
  [1 ,5 ,7],
  [3 ,7 ,8],
  [4 ,8 ,9],
]
k = 4

matrix = [
  [1, 2],
  [3, 4]
]
k = 3

matrix = [[1],[2],[3],[100],[101],[1000],[9999]]
k = 5

matrix = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]]
k = 19

solution = Solution()
print(solution.kth_smallest(matrix, k))
