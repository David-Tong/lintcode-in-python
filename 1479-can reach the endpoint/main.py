class Solution:
    """
    @param map: the map
    @return: can you reach the endpoint
    """
    def reach_endpoint(self, map):
        # Write your code here
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        M = len(map)
        N = len(map[0])

        from collections import deque
        bfs = deque()
        visited = [[False] * N for _ in range(M)]
        bfs.append((0 ,0))
        visited[0][0] = True

        while bfs:
            (x, y) = bfs.popleft()
            print((x, y))
            for dx, dy in DIRECTIONS:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < M and 0 <= ny < N:
                    if map[nx][ny] == 9:
                        return True
                    if map[nx][ny] == 1:
                        if not visited[nx][ny]:
                            bfs.append((nx, ny))
                            visited[nx][ny] = True
        return False


map = [[1,1,1],[1,0,0],[1,0,9]]
map = [[1,1,1],[1,1,9]]

solution = Solution()
print(solution.reach_endpoint(map))
