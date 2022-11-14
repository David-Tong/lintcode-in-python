class Solution:
    """
    @param a: An integer array
    @param target: An integer
    @return: An integer
    """
    def min_adjustment_cost(self, a, target):
        # write your code here
        L = len(a)
        N = 100

        # dp[l][n] - the minimal cost to change the lth a[] element to n
        dp = [[float("inf")] * (N + 1) for _ in range(L + 1)]

        for n in range(N + 1):
            dp[0][n] = 0

        for l in range(1, L + 1):
            for n in range(N + 1):
                left = max(0, n - target)
                right = min(N, n + target)
                for x in range(left, right + 1):
                    dp[l][n] = min(dp[l][n], dp[l-1][x] + abs(a[l-1] - n))

        ans = float("inf")
        for n in range(N + 1):
            ans = min(ans, dp[L][n])
        return ans


a = [1,4,2,3]
target = 1

a = [3,5,4,7]
target = 2

a = [12,3,7,4,5,13,2,8,4,7,6,5,7]
target = 2

solution = Solution()
print(solution.min_adjustment_cost(a, target))
