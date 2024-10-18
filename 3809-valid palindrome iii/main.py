class Solution:
    """
    @param s: a string
    @param k: can delete k characters
    @return: whether you can make s a palindrome by deleting at most k characters
    """
    def is_valid_palindrome(self, s, k):
        # write your code here
        # dp init
        L = len(s)
        dp = [[0] * L for _ in range(L)]
        for x in range(L):
            dp[x][x] = 1

        # dp transfer
        for x in range(L - 1, -1, -1):
            for y in range(x + 1, L):
                if s[x] == s[y]:
                    dp[x][y] = dp[x + 1][y - 1] + 2
                else:
                    dp[x][y] = max(dp[x + 1][y], dp[x][y - 1])
        maxi = dp[0][L - 1]

        return True if L - maxi <= k else False


s = "abcdeca"
k = 2

s = "abcdefed"
k = 2

s = "abccba"
k = 4

solution = Solution()
print(solution.is_valid_palindrome(s, k))
