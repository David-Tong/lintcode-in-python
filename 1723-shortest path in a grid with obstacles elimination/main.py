class Solution:
    """
    @param grid: a list of list
    @param k: an integer
    @return: Return the minimum number of steps to walk
    """
    def shortest_path(self, grid, k):
        # write your code here
        M = len(grid)
        N = len(grid[0])

        if M == 1 and N == 1:
            if grid[0][0] <= k:
                return 0
            else:
                return -1

        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        from collections import deque
        bfs = deque()
        bfs.append((0, 0, 0))
        from collections import defaultdict
        visited = [[float("inf")] * N for _ in range(M)]
        visited[0][0] = grid[0][0]

        steps = 0
        while bfs:
            size = len(bfs)
            steps += 1
            for n in range(size):
                x, y, o = bfs.popleft()
                for dx, dy in DIRECTIONS:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < M and 0 <= ny < N:
                        no = o + grid[nx][ny]
                        if no <= k:
                            if nx == M - 1 and ny == N - 1:
                                return steps
                            if no < visited[nx][ny]:
                                visited[nx][ny] = no
                                bfs.append((nx, ny, no))
        return -1


"""
grid = [[0,0,0],
        [1,1,0],
        [0,0,0],
        [0,1,1],
        [0,0,0]]
k = 1

grid = [[0,1,1],
        [1,1,1],
        [1,0,0]]
k = 1
"""

grid = [[0, 0]]
grid = [[0], [1]]
grid = [[0]]
k = 1

grid = [[0,1,0,0,0,1,1,1,1,1,0,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1],[1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,1,1],[1,0,0,1,1,0,0,0,1,1,1,0,1,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,1,1,0,0],[1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,0,0,0,0,1,0,0,1,0,1,0,1,1,0,1,0],[0,1,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,1,1,0,1,0,0,1,1,0,1,1,1,0,0,1],[0,0,1,1,1,0,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0,1,1,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0]]
k = 215

solution = Solution()
print(solution.shortest_path(grid, k))