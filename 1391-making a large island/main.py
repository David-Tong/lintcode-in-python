class UnionFindSet(object):
    def __init__(self, M, N, grid):
        self.size = M * N
        self.parents = [x for x in range(self.size)]
        self.ranks = [0] * self.size
        self.grid = [0] * self.size
        for x in range(M):
            for y in range(N):
                self.grid[x * N + y] = grid[x][y]

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        elif self.ranks[px] < self.ranks[py]:
            self.parents[px] = py
        else:
            self.parents[py] = px
            self.ranks[px] += 1
        return True

    def update_areas(self):
        from collections import defaultdict
        areas = defaultdict(int)
        for x in range(self.size):
            if self.grid[x] == 1:
                areas[self.parents[x]] += 1

        self.areas = [0] * self.size
        for x in range(self.size):
            self.areas[x] = areas[self.parents[x]]
        return max(self.areas)

    def get_area(self, x):
        return (self.parents[x], self.areas[x])

class Solution:
    """
    @param grid:
    @return:
    """
    def largest_island(self, grid):
        #
        M = len(grid)
        N = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        ufs = UnionFindSet(M, N, grid)

        def search_island(grid, x, y):
            if grid[x][y] == 0:
                return

            from collections import deque
            bfs = deque()
            visited = set()
            bfs.append((x, y))
            visited.add((x, y))

            while bfs:
                x, y = bfs.popleft()
                for dx, dy in DIRECTIONS:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < M and 0 <= ny < N:
                        if (nx, ny) not in visited and grid[nx][ny] == 1:
                            bfs.append((nx, ny))
                            visited.add((nx, ny))
                            ufs.union(x * N + y, nx * N + ny)

        def make_larger_island(ufs, x, y):
            from collections import defaultdict
            areas = defaultdict(int)
            for dx, dy in DIRECTIONS:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < M and 0 <= ny < N:
                    parent, area = ufs.get_area(nx * N + ny)
                    areas[parent] = area

            ans = 0
            for area in areas.values():
                ans += area
            return ans + 1


        zeros = list()
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    search_island(grid, x, y)
                else:
                    zeros.append((x, y))


        for x in range(M):
            for y in range(N):
                ufs.find(x * N + y)

        ans = ufs.update_areas()
        for x, y in zeros:
            ans = max(ans, make_larger_island(ufs, x, y))
        return ans


grid = [[1, 0], [0, 1]]
grid = [[1, 1], [1, 0]]
grid = [[1, 1], [1, 1]]

solution = Solution()
print(solution.largest_island(grid))
