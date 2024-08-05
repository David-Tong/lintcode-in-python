class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climb_stairs(self, n):
        # write your code here
        # shortcut
        if n == 0:
            return 0
        elif n == 1:
            return 1

        # dp[x] - ways to climb x stairs
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1

        for x in range(2, n + 1):
            dp[x] = dp[x - 1] + dp[x - 2]
        return dp[n]


n = 3

solution = Solution()
print(solution.climb_stairs(n))
