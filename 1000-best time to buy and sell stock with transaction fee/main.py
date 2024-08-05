class Solution:
    """
    @param prices: a list of integers
    @param fee: a integer
    @return: return a integer
    """
    def max_profit(self, prices, fee):
        # write your code here
        # init
        L = len(prices)
        hold = [0] * (L + 1)
        sold = [0] * (L + 1)
        hold[0] = float("-inf")
        sold[0] = 0

        # dp
        for x in range(1, L + 1):
            hold[x] = max(hold[x - 1], sold[x - 1] - prices[x - 1])
            sold[x] = max(sold[x - 1], hold[x] + prices[x - 1] - fee)

        # ans
        return sold[L]


prices = [1, 3, 2, 8, 4, 9]
fee = 2

prices = [1, 4, 6, 2, 8, 3, 10, 14]
fee = 3

solution = Solution()
print(solution.max_profit(prices, fee))
