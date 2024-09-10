class Solution:
    """
    @param n: An integer
    @return: a square matrix
    """
    def generate_matrix(self, n):
        # write your code here
        # shortcut
        if n == 0:
            return []

        # pre-process
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        ans = [[0] * n for _ in range(n)]

        x, y = 0, 0
        val = 1
        ans[x][y] = val * val

        # process
        # initial move
        step = n - 1
        d = 0
        for _ in range(step):
            dx, dy = DIRECTIONS[d]
            x, y = x + dx, y + dy
            val += 1
            ans[x][y] = val
        d = (d + 1) % 4

        # go spiral
        while step:
            for _ in range(2):
                for _ in range(step):
                    dx, dy = DIRECTIONS[d]
                    x, y = x + dx, y + dy
                    val += 1
                    ans[x][y] = val
                d = (d + 1) % 4
            step -= 1

        return ans


n = 0
#n = 2
#n = 3

solution = Solution()
print(solution.generate_matrix(n))
