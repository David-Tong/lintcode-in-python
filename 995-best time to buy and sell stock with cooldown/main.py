class Solution:
    """
    @param prices: a list of integers
    @return: return a integer
    """
    def max_profit(self, prices):
        # write your code here
        # init
        L = len(prices)
        hold = [0] * (L + 1)
        sold = [0] * (L + 1)
        rest = [0] * (L + 1)
        hold[0] = float("-inf")
        sold[0] = float("-inf")
        rest[0] = 0

        # dp
        for x in range(1, L + 1):
            # case 1 : hold[x] = max(hold[x - 1], rest[x - 1] - prices[x - 1]
            hold[x] = max(hold[x - 1], rest[x - 1] - prices[x - 1])
            # case 2 : sold[x] = hold[x - 1] + prices[x - 1]
            sold[x] = hold[x - 1] + prices[x - 1]
            # case 3 : rest[x] = max(rest[x - 1], sold[x - 1])
            rest[x] = max(rest[x - 1], sold[x - 1])

        # ans
        return max(sold[L], rest[L])


prices = [1,2,3,0,2]
prices = [3,2,6,5,0,3]

solution = Solution()
print(solution.max_profit(prices))
