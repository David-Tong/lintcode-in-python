class Solution:
    """
    @param a: the array a
    @return: return the maximum profit
    """
    def get_ans(self, a):
        # write your code here
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        ans = 0
        for item in a:
            if heap and item > heap[0]:
                ans += item - heappop(heap)
                heappush(heap, item)
            heappush(heap, item)
        return ans


a = [1,2,10,9]
a = [9,5,9,10,5]
a = [1,2,3,4,5,6,7,8,9]
#a = [9,8,7,6,5,4,3,2,1]

solution = Solution()
print(solution.get_ans(a))
