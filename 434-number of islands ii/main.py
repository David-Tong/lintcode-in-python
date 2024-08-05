class UnionFindSet:
    def __init__(self, size):
        self.size = size
        self.parents = [_ for _ in range(size)]
        self.ranks = [0] * size

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        else:
            if self.ranks[px] > self.ranks[py]:
                self.parents[py] = px
            elif self.ranks[px] < self.ranks[py]:
                self.parents[px] = py
            else:
                self.parents[py] = px
                self.ranks[px] += 1
            return True


"""
from lintcode import (
    Point,
)
"""

# Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def num_islands2(self, n, m, operators):
        # write your code here
        # pre-process
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        L = n * m
        maps = [[0] * m for _ in range(n)]
        ufs = UnionFindSet(L)

        # process
        islands = 0
        ans = list()
        for operator in operators:
            if maps[operator.x][operator.y] != 1:
                maps[operator.x][operator.y] = 1
                idx = operator.x * m + operator.y
                islands += 1
                for dx , dy in DIRECTIONS:
                    nx, ny = operator.x + dx, operator.y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if maps[nx][ny] == 1:
                            if ufs.union(idx, nx * m + ny):
                                islands -= 1
            ans.append(islands)
        return ans


n = 4
m = 5
A = [Point(1,1), Point(0,1), Point(3,3), Point(3,4)]

n = 3
m = 3
A = [Point(0,0), Point(0,1), Point(2,2), Point(2,1)]

n = 4
m = 5
A = [Point(1,1), Point(0,1), Point(2,0), Point(2,1)]

n = 3
m = 3
A = [Point(0,0), Point(0,1), Point(2,2), Point(2,2)]

n = 3
m = 3
A = [Point(0,0), Point(0,2), Point(0,1)]

n = 3
m = 3
A = [Point(0,0), Point(1,1), Point(1,0), Point(0,1)]

solution = Solution()
print(solution.num_islands2(n, m, A))
