class Solution:
    """
    @param obstacle_grid: A list of lists of integers
    @return: An integer
    """
    def unique_paths_with_obstacles(self, obstacle_grid):
        # write your code here
        if obstacle_grid[0][0] == 1:
            return 0
        dp = [[0] * len(obstacle_grid[0]) for x in range(len(obstacle_grid))]
        dp[0][0] = 1

        for x in range(len(obstacle_grid)):
            for y in range(len(obstacle_grid[0])):
                if obstacle_grid[x][y] == 0:
                    if x > 0:
                        dp[x][y] += dp[x-1][y]
                    if y > 0:
                        dp[x][y] += dp[x][y-1]
        return dp[len(obstacle_grid) - 1][len(obstacle_grid[0]) - 1]


obstacleGrid = [[0]]
#obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

solution = Solution()
print(solution.unique_paths_with_obstacles(obstacleGrid))
