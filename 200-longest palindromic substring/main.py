class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longest_palindrome(self, s):
        # write your code here
        L = len(s)

        # dp[x][y] - whether s[x:y+1] is palindromic
        dp = [[False] * L for _ in range(L)]

        ans = ""
        maxi = 0
        for y in range(L):
            for x in range(y + 1):
                if y - x == 0:
                    dp[x][y] = True
                else:
                    if s[x] == s[y]:
                        if y - x == 1:
                            dp[x][y] = True
                        else:
                            if dp[x+1][y-1]:
                                dp[x][y] = True
                if dp[x][y]:
                    if y - x + 1 > maxi:
                        maxi = y - x + 1
                        ans = s[x:y+1]
        return ans


s = "abcdzdcab"
#s = "aba"
#s = "cbabadabab"
#s = "a"
s = "cbc9119119"
s = "aa"

solution = Solution()
print(solution.longest_palindrome(s))
