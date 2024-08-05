class Solution:
    """
    @param n: The param n means 2*n rectangular square.
    @return: Return the total schemes.
    """
    def get_total_schemes(self, n):
        # Write your code here.
        # dp[x] - the number of paving schemes for a 2 * x rectangular
        dp = [0] * 50
        dp[0] = 1
        dp[1] = 2

        for x in range(2, n):
            dp[x] = dp[x - 1] + dp[x - 2]
        return dp[n - 1]


n = 2
n = 3
n = 50

solution = Solution()
print(solution.get_total_schemes(n))
