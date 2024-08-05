class Solution:
    """
    @param maze_map: a 2D grid
    @return: return the minium distance
    """
    def get_min_distance(self, maze_map):
        # write your code here
        M = len(maze_map)
        N = len(maze_map[0])

        from collections import defaultdict
        travels = defaultdict(list)

        start = ()
        for x in range(M):
            for y in range(N):
                if maze_map[x][y] > 0:
                    travels[maze_map[x][y]].append((x, y))
                elif maze_map[x][y] == -2:
                    start = (x, y)

        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        from collections import deque
        bfs = deque()
        bfs.append(start)
        visited = [[False] * N for _ in range(M)]
        visited[start[0]][start[1]] = True

        steps = 0
        while bfs:
            size = len(bfs)
            steps += 1
            for _ in range(size):
                x, y = bfs.popleft()

                # normal search
                for dx, dy in DIRECTIONS:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < M and 0 <= ny < N:
                        # reach ending grid
                        if maze_map[nx][ny] == -3:
                            return steps

                        if maze_map[nx][ny] != -1:
                            if not visited[nx][ny]:
                                visited[nx][ny] = True
                                bfs.append((nx, ny))

                # travel search
                if maze_map[x][y] > 0:
                    if maze_map[x][y] in travels:
                        for nx, ny in travels[maze_map[x][y]]:
                            # reach ending grid
                            if maze_map[nx][ny] == -3:
                                return steps

                            if not visited[nx][ny]:
                                visited[nx][ny] = True
                                bfs.append((nx, ny))
                        del travels[maze_map[x][y]]
        return -1


maze_map = [[1,0,-1,1],[-2,0,1,-3],[2,2,0,0]]
maze_map = [[1,0,-1,1],[-2,0,-1,-3],[2,2,0,0]]
maze_map = [[1,0,-1,-1,1],[-2,3,0,0,0],[1,0,0,3,-1],[-1,-1,-1,3,0],[0,0,0,0,-3]]

solution = Solution()
print(solution.get_min_distance(maze_map))
