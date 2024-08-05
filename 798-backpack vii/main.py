class Solution:
    """
    @param n: the money of you
    @param prices: the price of rice[i]
    @param weight: the weight of rice[i]
    @param amounts: the amount of rice[i]
    @return: the maximum weight
    """
    def back_pack_v_i_i(self, n, prices, weight, amounts):
        # write your code here
        L = len(prices)

        # pre-process
        new_prices = list()
        new_weight = list()
        for x in range(L):
            new_prices += [prices[x]] * amounts[x]
            new_weight += [weight[x]] * amounts[x]

        # dp[x] - max weight rice can be bought with n yuan
        L = len(new_prices)
        dp = [0] * (n + 1)
        for x in range(L):
            for y in range(n, -1, -1):
                if y - new_prices[x] >= 0:
                    dp[y] = max(dp[y], dp[y - new_prices[x]] + new_weight[x])
        return max(dp)


n = 8
prices = [3,2]
weights = [300,160]
amounts = [1,6]

solution = Solution()
print(solution.back_pack_v_i_i(n, prices, weights, amounts))
