class Solution:
    """
    @param s: A string containing only lowercase letters
    @return: Minimum number of operations required
    """
    def clear_string(self, s):
        # write your code here
        # dp init
        L = len(s)
        dp = [[float("inf")] * L for _ in range(L)]

        # dp transfer
        for l in range(1, L + 1):
            for x in range(L - l + 1):
                y = x + l - 1
                if l == 1:
                    dp[x][y] = 1
                else:
                    dp[x][y] = 1 + dp[x + 1][y]
                    for k in range(x + 1, y + 1):
                        if s[x] == s[k]:
                            if k - 1 > x:
                                cost = dp[x + 1][k - 1]
                            else:
                                cost = 0
                            dp[x][y] = min(dp[x][y], cost + dp[k][y])
        return dp[0][L - 1]


s = "abcddcba"
s = "abaca"
s = "aaacaaaaaacaaaa"

solution = Solution()
print(solution.clear_string(s))
