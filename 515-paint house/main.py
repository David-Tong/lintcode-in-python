class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def min_cost(self, costs):
        # write your code here
        if len(costs) == 0:
            return 0
        dp = [[0] * 3 for cost in costs]
        # dp[x][0] - min cost for house x painted in red, dp[x][1] in blue, dp[x][2] in green
        dp[0] = costs[0]
        for x in range(1, len(costs)):
            dp[x][0] = min(dp[x-1][1], dp[x-1][2]) + costs[x][0]
            dp[x][1] = min(dp[x-1][0], dp[x-1][2]) + costs[x][1]
            dp[x][2] = min(dp[x-1][0], dp[x-1][1]) + costs[x][2]
        return min(dp[len(costs) - 1])


costs = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
costs = [[1, 2, 3], [1, 4, 6]]
costs = [[1, 2, 3]]

solution = Solution()
print(solution.min_cost(costs))
