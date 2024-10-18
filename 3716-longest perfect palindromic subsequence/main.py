class Solution:
    """
    @param s: A string.
    @return: The length of the longest Perfect Palindromic Substring in s.
    """
    def longest_palindrome_subseq(self, s):
        # --- write your code here ---
        # dp init
        L = len(s)
        K = 26
        dp = [[[0] * K for _ in range(L)] for _ in range(L)]

        # dp transfer
        for x in range(L - 1, -1, -1):
            for y in range(x + 1, L):
                if s[x] == s[y]:
                    idx = ord(s[x]) - ord('a')
                    for k in range(K):
                        dp[x][y][k] = max(dp[x][y][k], dp[x + 1][y - 1][k])
                        if idx != k:
                            dp[x][y][idx] = max(dp[x][y][idx], dp[x + 1][y - 1][k] + 2)
                else:
                    for k in range(K):
                        dp[x][y][k] = max(dp[x][y][k], max(dp[x + 1][y][k], dp[x][y - 1][k]))

        # post-process
        ans = 0
        for k in range(K):
            ans = max(ans, dp[0][L - 1][k])
        return ans


s = "bbabab"
s = "dcbccacdb"
s = "abcdb"
s = "cccc"
s = "bccb"
s = "bbcccbbb"
s = "zzaaazzz"
s = "zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez"


solution = Solution()
print(solution.longest_palindrome_subseq(s))
