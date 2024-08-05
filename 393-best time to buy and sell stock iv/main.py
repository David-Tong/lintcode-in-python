class Solution:
    """
    @param k: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def max_profit(self, k, prices):
        # write your code here
        L = len(prices)

        # corner case
        if k > L / 2:
            ans = 0
            for x in range(1, L):
                if prices[x] - prices[x - 1] > 0:
                    ans += prices[x] - prices[x - 1]
            return ans

        # init
        prev_hold = [float("-inf")] * (k + 1)
        prev_sold = [float("-inf")] * (k + 1)
        prev_sold[0] = 0

        curr_hold = [0] * (k + 1)
        curr_sold = [0] * (k + 1)

        # dp
        for x in range(L):
            for y in range(k):
                curr_hold[y + 1] = max(prev_hold[y + 1], prev_sold[y] - prices[x])
                curr_sold[y + 1] = max(prev_sold[y + 1], prev_hold[y + 1] + prices[x])
            prev_hold = curr_hold
            prev_sold = curr_sold
            curr_hold = [0] * (k + 1)
            curr_sold = [0] * (k + 1)

        # ans
        ans = max(0, max(max(prev_hold), max(prev_sold)))
        return ans


k = 2
prices = [4, 4, 6, 1, 1, 4, 2 ,5]

k = 1
prices = [3, 2, 1]

k = 2
prices = [2, 4, 1]

k = 2
prices = [3, 2, 6, 5, 0, 3]

k = 3
prices = [3, 5, 7, 9, 11, 0, 2, 5, 0, 2]

k = 1
prices = [2, 1, 5]

k = 100
prices = [2, 4, 5, 1, 6]

k = 10
prices = []

solution = Solution()
print(solution.max_profit(k, prices))
