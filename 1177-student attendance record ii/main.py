class Solution:
    """
    @param n: an integer
    @return: return an integer
    """
    def check_record(self, n):
        # write your code here
        MOD = 10 ** 9 + 7

        # dp[x][y][z] - x + 1 records with y 'A' records and ended with z continuous 'L' records
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1
        dp[0][1] = 1
        dp[0][2] = 0
        dp[1][0] = 1
        dp[1][1] = 0
        dp[1][2] = 0

        for x in range(1, n):
            ndp = [[0] * 3 for _ in range(2)]
            # ended with P
            for y in range(2):
                for z in range(3):
                    ndp[y][0] = (ndp[y][0] + dp[y][z]) % MOD
            # ended with A
            for z in range(3):
                ndp[1][0] = (ndp[1][0] + dp[0][z]) % MOD
            # ended with L
            for y in range(2):
                for z in range(2):
                    ndp[y][z + 1] = (ndp[y][z + 1] + dp[y][z]) % MOD

            dp = ndp

        ans = 0
        for y in range(2):
            for z in range(3):
                ans = (ans + dp[y][z]) % MOD
        return ans


n = 1
n = 2
n = 3

n = 100000

solution = Solution()
print(solution.check_record(n))
