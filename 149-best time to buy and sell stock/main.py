class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def max_profit(self, prices):
        # write your code here
        L = len(prices)

        mini = float("inf")
        ans = 0
        for x in range(L):
            mini = min(mini, prices[x])
            ans = max(ans, prices[x] - mini)
        return ans


prices = [3, 2, 3, 1, 2]
prices = [1, 2, 3, 4, 5]
prices = [5, 4, 3, 2, 1]

solution = Solution()
print(solution.max_profit(prices))
