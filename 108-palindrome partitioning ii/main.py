class Solution:
    """
    @param s: A string
    @return: An integer
    """
    def min_cut(self, s):
        # write your code here
        # step 1, calculate palindrome for all s substrings
        # dp init
        L = len(s)
        palindromes = [[True] * L for _ in range(L)]

        # dp transfer
        for x in range(L - 1, -1, -1):
            for y in range(x + 1, L):
                palindromes[x][y] = palindromes[x + 1][y - 1] and s[x] == s[y]

        # step 2, calculate min cut
        # dp init
        dp = [float("inf")] * L

        # dp transfer
        for x in range(L):
            if palindromes[0][x]:
                dp[x] = 0
            else:
                for y in range(x):
                    if palindromes[y + 1][x]:
                        dp[x] = min(dp[x], dp[y] + 1)
        return dp[L - 1]


s = "a"
s = "aab"
s = "abacabac"
s = "sfsdkjgfuiwbfkwfbvkjfneiwhehfeifhfiefwhihifhhhhhhhhhhhhhhhhhhhhhhhhefwjhweg"

solution = Solution()
print(solution.min_cut(s))
