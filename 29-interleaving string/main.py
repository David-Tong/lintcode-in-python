class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def is_interleave(self, s1, s2, s3):
        # write your code here
        M = len(s1)
        N = len(s2)
        L = len(s3)

        if M + N <> L:
            return False

        # dp[x][y] - s3[:x + y] is formed by the interleaving of s1[:x] and s2[:y]
        dp = [[False] * (N + 1) for _ in range(M + 1)]

        for x in range(M + 1):
            for y in range(N + 1):
                if x == 0 and y == 0:
                    dp[x][y] = True
                    continue

                if x == 0:
                    if s3[y - 1] == s2[y - 1]:
                        dp[x][y] = dp[x][y - 1] & True
                    continue

                if y == 0:
                    if s3[x - 1] == s1[x - 1]:
                        dp[x][y] = dp[x - 1][y] & True
                    continue

                if s3[x + y - 1] == s1[x - 1]:
                    dp[x][y] = dp[x - 1][y] & True

                if s3[x + y - 1] == s2[y - 1]:
                    dp[x][y] = dp[x][y] | (dp[x][y - 1] & True)

        print(dp)
        return dp[M][N]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

s1 = ""
s2 = ""
s3 = "1"

"""
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
"""

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
s3 = "aadbbbaccc"

"""
s1 = "a"
s2 = ""
#s3 = ""
s3 = "a"

#s1 = "abba"
#s2 = "cddc"
#s3 = "abcdbadc"

#s1 = "aabcc"
#s2 = "dbbca"
#s3 = "aadbcbbcac"

s1 = "db"
s2 = "b"
s3 = "cbb"
"""

solution = Solution()
print(solution.is_interleave(s1, s2, s3))
