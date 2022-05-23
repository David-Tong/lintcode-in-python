class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coin_change(self, coins, amount):
        # write your code here
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for x in range(1, amount + 1):
            for y in coins:
                if x - y >= 0:
                    dp[x] = min(dp[x], dp[x - y])
            dp[x] += 1
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]


coins = [1, 2, 5]
amount = 11

coins = [2]
amount = 3

coins = [2, 5, 7]
amount = 27

solution = Solution()
print(solution.coin_change(coins, amount))
