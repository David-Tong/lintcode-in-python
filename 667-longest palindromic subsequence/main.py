class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longest_palindrome_subseq(self, s):
        # write your code here
        # dp init
        # dp[x][y] - the longest length palindromic subsequence of s[x:y+1]
        L = len(s)
        if L == 0:
            return 0
        dp = [[0] * L for _ in range(L)]
        for x in range(L):
            dp[x][x] = 1

        # dp transfer
        # when s[x] == s[y], dp[x][y] = dp[x + 1][y - 1] + 2
        # when s[x] != s[y], dp[x][y] = max(dp[x][y - 1], dp[x + 1][y])
        for x in range(L - 1, -1, -1):
            for y in range(x + 1, L):
                if s[x] == s[y]:
                    dp[x][y] = dp[x + 1][y - 1] + 2
                else:
                    dp[x][y] = max(dp[x][y - 1], dp[x + 1][y])
        return dp[0][L - 1]


s = "bbbab"
s = "bbbbb"

solution = Solution()
print(solution.longest_palindrome_subseq(s))
