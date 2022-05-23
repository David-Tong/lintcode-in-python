class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def num_decodings(self, s):
        # write your code here
        if len(s) == 0:
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for x in range(1, len(s) + 1):
            if int(s[x-1:x]) > 0:
                dp[x] += dp[x - 1]
            if x > 1:
                if s[x-2] != "0" and int(s[x-2:x]) > 0 and int(s[x-2:x]) <= 26:
                    dp[x] += dp[x-2]
        return dp[len(s)]


s = "12"
#s = "10"
#s = ""
#s = "126265"
#s = "19261001"

solution = Solution()
print(solution.num_decodings(s))
