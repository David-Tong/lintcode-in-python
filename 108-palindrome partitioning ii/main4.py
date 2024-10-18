class Solution:
    """
    @param s: A string
    @return: An integer
    """
    def min_cut(self, s):
        # write your code here
        # helper function
        def is_palindrome(x, y):
            left, right = x, y
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        # dp init
        L = len(s)
        dp = [[float("inf")] * L for _ in range(L)]
        for x in range(L):
            dp[x][x] = 0

        # dp transfer
        for l in range(2, L + 1):
            for x in range(L - l + 1):
                y = x + l - 1
                if is_palindrome(x, y):
                    dp[x][y] = 0
                else:
                    for k in range(x + 1, y + 1):
                        dp[x][y] = min(dp[x][y], dp[x][k-1] + dp[k][y] + 1)
        return dp[0][L - 1]


s = "a"
s = "aab"
s = "abacabac"

solution = Solution()
print(solution.min_cut(s))
