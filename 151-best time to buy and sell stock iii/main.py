class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def max_profit(self, prices):
        # write your code here
        M = len(prices) + 1
        N = 5

        # init
        dp = [[0] * N for _ in range(M)]
        dp[0][0] = 0
        for x in range(1, 5):
            dp[0][x] = float("-inf")

        # dp
        for x in range(1, M):
            # case 1: dp[x][y] = max(dp[x - 1][y], dp[x - 1][y - 1] + prices[x - 1] - prices[x - 2])
            for y in range(0, 5, 2):
                if y > 0 and x > 1:
                    dp[x][y] = max(dp[x - 1][y], dp[x - 1][y - 1] + prices[x - 1] - prices[x - 2])
            # case 2: dp[x][y] = max(dp[x - 1][y] + prices[x - 1] - prices[x - 2], dp[x - 1][y - 1])
            for y in range(1, 5, 2):
                if y > 0 and x > 1:
                    dp[x][y] = max(dp[x - 1][y] + prices[x - 1] - prices[x - 2], dp[x - 1][y - 1])

        # ans
        return max(dp[M - 1][0], dp[M - 1][2], dp[M - 1][4])


prices = [4,4,6,1,1,4,2,5]
prices = [2,3,4,5,6,7,1,2,3]

solution = Solution()
print(solution.max_profit(prices))
