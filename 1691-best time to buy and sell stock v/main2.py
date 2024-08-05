class Solution:
    """
    @param a: the array a
    @return: return the maximum profit
    """
    def get_ans(self, a):
        # write your code here
        N = len(a)

        # dp[x][y] - the max profit when hold y shares of stock after x days
        prev = [float("-inf")] * (N + 1)
        prev[0] = 0

        for idx, stock in enumerate(a):
            curr = [float("-inf")] * (N + 1)
            for x in range(idx + 2):
                if x == 0:
                    curr[x] = max(prev[x], prev[x + 1] + stock)
                elif x == N:
                    curr[x] = max(prev[x], prev[x - 1] - stock)
                else:
                    curr[x] = max(prev[x], max(prev[x + 1] + stock, prev[x - 1] - stock))
            prev = curr
        return prev[0]


a = [1,2,10,9]
a = [9,5,9,10,5]
a = [1,2,3,4,5,6,7,8,9]
#a = [9,8,7,6,5,4,3,2,1]

solution = Solution()
print(solution.get_ans(a))
