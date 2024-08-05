class Solution:
    """
    @param amount: a total amount of money amount
    @param coins: the denomination of each coin
    @return: the number of combinations that make up the amount
    """
    def change(self, amount, coins):
        # write your code here
        # dp[x] - the number of combinations that make up the amount x
        dp = [0] * (amount + 1)
        dp[0] = 1

        # dp transfer
        for coin in coins:
            for x in range(amount + 1):
                if x - coin >= 0:
                    dp[x] += dp[x - coin]
        return dp[amount]


amount = 10
coins = [10]

amount = 8
coins = [2, 3, 8]

amount = 100
coins = [2,3,5,10,15,20]

solution = Solution()
print(solution.change(amount, coins))
