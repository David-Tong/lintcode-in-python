class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def max_profit(self, prices):
        # write your code here
        L = len(prices)

        ans = 0
        for x in range(L - 1):
            if prices[x] < prices[x + 1]:
                ans += prices[x + 1] - prices[x]
        return ans


prices = [2, 1, 2, 0, 1]
prices = [4, 3, 2, 1]
prices = [1, 2, 3, 4]

solution = Solution()
print(solution.max_profit(prices))
