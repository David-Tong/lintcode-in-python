class Solution:
    """
    @param sticks: the length of sticks
    @return: Minimum Cost to Connect Sticks
    """
    def minimum_cost(self, sticks):
        # write your code here
        # pre-process
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        # process
        for stick in sticks:
            heappush(heap, stick)
        ans = 0
        while len(heap) > 1:
            stick = heappop(heap)
            stick2 = heappop(heap)
            ans += stick + stick2
            heappush(heap, stick + stick2)
        return ans


sticks = [2,4,3]
sticks = [1,8,3,5]
sticks = [25,62,51,92,93,40,23,16,36,32]

solution = Solution()
print(solution.minimum_cost(sticks))
