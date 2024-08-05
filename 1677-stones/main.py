class Solution:
    """
    @param p: the position of the i-th stone
    @param d: how far the stones can be stone
    @return: the distance from the start point to the farthest stone.
    """
    def get_distance(self, p, d):
        # Write your code here.
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        for pi, di in zip(p, d):
            heappush(heap, (pi, di))

        steps = 1
        ans = 0
        while heap:
            pi, di = heappop(heap)
            if steps % 2 == 1:
                heappush(heap, (pi + di, di))
            ans = max(ans, pi)
            steps += 1
        return ans


p = [1, 2]
d = [5, 4]

p = [1, 6]
d = [5, 6]

p = [1, 5, 2, 6, 6, 8]
d = [5, 3, 2, 1, 7, 12]

solution = Solution()
print(solution.get_distance(p, d))
