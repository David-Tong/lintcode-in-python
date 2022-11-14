class Solution:
    """
    @param matrix: a matrix
    @return: return how many square submatrices have all ones
    """
    def count_squares(self, matrix):
        # write your code here
        def get_dp(dp, x, y):
            if 0 <= x < M and 0 <= y < N:
                return dp[x][y]
            else:
                return 0

        M = len(matrix)
        N = len(matrix[0])

        # dp[x][y] - number of matrix with right bottom coordinator of (x, y)
        dp = [[0] * N for _ in range(M)]

        for x in range(M):
            for y in range(N):
                if matrix[x][y] == 1:
                    delta = min(get_dp(dp, x - 1, y - 1), min(get_dp(dp, x - 1, y), get_dp(dp, x, y - 1)))
                else:
                    delta = 0
                dp[x][y] = matrix[x][y] + delta

        ans = 0
        for x in range(M):
            for y in range(N):
                ans += dp[x][y]
        return ans


matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

"""
matrix = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]

matrix = [
    [1,1,1,1,1],
    [1,1,1,1,0],
    [1,1,1,0,0]
]
"""

solution = Solution()
print(solution.count_squares(matrix))
