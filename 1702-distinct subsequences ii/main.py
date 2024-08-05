class Solution:
    """
    @param s: The string s
    @return: The number of distinct, non-empty subsequences of S.
    """
    def distinct_subseq_i_i(self, s):
        # Write your code here
        MODULO = 10**9 + 7
        M = len(s)
        L = 26

        # dp
        # dp[c] - the number of different sequences ended with character c
        dp = [0] * L
        for x in range(M):
            c = ord(s[x]) - ord('a')
            dp[c] = (sum(dp) + 1) % MODULO

        ans = sum(dp) % MODULO
        return ans


s = "abc"
s = "aba"
s = "aaa"
s = "abab"

solution = Solution()
print(solution.distinct_subseq_i_i(s))
