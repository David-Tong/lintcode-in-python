class Solution:
    """
    @param citations: a list of integers
    @return: return a integer
    """
    def h_index(self, citations):
        # write your code here
        N = len(citations)
        citations = sorted(citations, reverse=True)
        for x in range(N):
            if citations[x] < x + 1:
                return x
        return N


citations = [3, 0, 6, 1, 5]
citations = [5, 5, 5, 5, 5]

solution = Solution()
print(solution.h_index(citations))
