class Solution:
    """
    @param sx: the start x
    @param sy: the start y
    @param dx: the destination x
    @param dy: the destination y
    @return: whether you can reach the destination
    """
    def reach_destination(self, sx, sy, dx, dy):
        # Write your code here.
        def do_reach(x, y):
            if x == sx and y == sy:
                return True
            else:
                if x < sx or y < sy:
                    return False
                else:
                    if x < y:
                        return do_reach(x, y - x)
                    elif x > y:
                        return do_reach(x - y, y)
                    else:
                        return False

        if sx == 1 and sy == 1:
            if dx == 1 or dy == 1:
                return True

        return do_reach(dx, dy)


sx = 1
sy = 1
dx = 3
dy = 5

sx = 2
sy = 3
dx = 7
dy = 11

sx = 3
sy = 7
dx = 221652
dy = 49927

sx = 1
sy = 1
dx = 1
dy = 99999999

solution = Solution()
print(solution.reach_destination(sx, sy, dx, dy))
