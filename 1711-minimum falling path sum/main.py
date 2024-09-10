class Solution:
    """
    @param a: the given array
    @return: the minimum sum of a falling path
    """
    def min_falling_path_sum(self, a):
        # Write your code here
        # dp init
        # dp[x][y] - the minimum sum of a falling path at a[x][y]
        M = len(a)
        N = len(a[0])
        dp = [[float("inf")] * N for _ in range(M)]
        for y in range(N):
            dp[0][y] = a[0][y]

        # dp transfer
        # dp[x][y] = min(dp[x][y], min(dp[x-1][y-1], dp[x-1][y], dp[x-1][y+1]) + a[x][y])
        for x in range(1, M):
            for y in range(N):
                dp[x][y] = dp[x - 1][y]
                if y > 0:
                    dp[x][y] = min(dp[x][y], dp[x - 1][y - 1])
                if y < N - 1:
                    dp[x][y] = min(dp[x][y], dp[x - 1][y + 1])
                dp[x][y] += a[x][y]

        # dp answer
        ans = min(dp[M - 1])
        return ans


a = [[1,2,3],[4,5,6],[7,8,9]]
a = [[35,94,-89,35,69],[-32,-50,19,-12,-65],[-6,-18,14,2,-38],[-29,68,-50,12,-98],[49,-33,-91,-44,-52]]
# a = [[3] * 100 for _ in range(100)]

solution = Solution()
print(solution.min_falling_path_sum(a))
