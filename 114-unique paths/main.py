class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def unique_paths(self, m, n):
        # write your code here
        dp = [[0] * n for x in range(m)]
        dp[0][0] = 1
        for x in range(m):
            for y in range(n):
                if x >= 1:
                    if y >= 1:
                        dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
                    else:
                        dp[x][y] = dp[x - 1][y]
                else:
                    if y >= 1:
                        dp[x][y] = dp[x][y - 1]
        return dp[m - 1][n - 1]


n = 1
m = 3

n = 3
m = 3

solution = Solution()
print(solution.unique_paths(m, n))
