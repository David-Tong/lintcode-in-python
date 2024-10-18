class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longest_palindrome(self, s):
        # write your code here
        # dp init
        # dp[x][y] - is s[x:y+1] a palindrome
        L = len(s)
        if L == 0:
            return ""
        dp = [[True] * L for _ in range(L)]

        # dp transfer
        # if s[x] == s[y] and s[x + 1][y - 1] is a palindrome, dp[x][y] = True
        ans = s[0]
        for x in range(L - 1, -1, -1):
            for y in range(x + 1, L):
                dp[x][y] = dp[x + 1][y - 1] and s[x] == s[y]
                if dp[x][y]:
                    if y - x + 1 > len(ans):
                        ans = s[x:y+1]
        return ans


s = "abcdzdcab"
s = "aba"
s = ""
s = "cbabadabab"
s = "a"
s = "abc"
s = "cbc9119119"
s = "aa"

solution = Solution()
print(solution.longest_palindrome(s))
