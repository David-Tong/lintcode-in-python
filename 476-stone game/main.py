class Solution:
    """
    @param a: An integer array
    @return: An integer
    """
    def stone_game(self, a):
        # write your code here
        # cost function
        def cost(x, y):
            return sum(a[x: y + 1])

        # dp init
        L = len(a)
        if L == 0:
            return 0
        dp = [[float("inf")] * L for _ in range(L)]
        for x in range(L):
            dp[x][x] = 0

        # dp transfer
        for s in range(2, L + 1):
            for x in range(L - s + 1):
                y = x + s - 1
                for k in range(x + 1, y + 1):
                    dp[x][y] = min(dp[x][y], dp[x][k - 1] + dp[k][y] + cost(x, y))
        return dp[0][L - 1]


a = [3, 4, 3]
a = [4, 1, 1, 4]
a = [45,6,7,8,11,23,2,2,45,7]

solution = Solution()
print(solution.stone_game(a))
