class Solution:
    """
    @param height: An integer
    @param width: An integer
    @param bricks: An integer array
    @return: The number of ways to build a sturdy wall
    """
    def build_wall(self, height, width, bricks):
        # write your code here
        # use bitmask to represent a way to build brick wall
        # suppose we will have a wall with width 8
        # the way to build wall using 2, 5, 1
        # xx xxxxx x - bitmask for 010000

        # pre-process
        MODULO = 10 ** 9 + 7
        bricks = set(bricks)
        plans = list()
        for plan in range(2 ** (width - 1)):
            x = plan
            ones = [-1]
            for bit in range(width - 1):
                if x & 1:
                    ones.append(bit)
                x >>= 1
            ones.append(width - 1)

            # make plan
            valid = True
            for x in range(1, len(ones)):
                if ones[x] - ones[x - 1] not in bricks:
                    valid = False
                    continue
            if valid:
                plans.append(plan)

        # process
        # dp init
        # dp[x][y] - the number of ways to build x row with the last row using plan y
        from collections import defaultdict
        dp = [defaultdict(int) for _ in range(height)]
        for plan in plans:
            dp[0][plan] = 1

        # dp transfer
        # dp[x][y] = dp[x - 1][plan in plans] if y & plan == 0
        for x in range(1, height):
            for y in plans:
                for z in plans:
                    if y & z == 0:
                        dp[x][y] += dp[x - 1][z]
                        dp[x][y] %= MODULO
        ans = sum(dp[height - 1].values()) % MODULO
        return ans


height = 2
width = 3
bricks = [1, 2]

height = 1
width = 1
bricks = [5]

height = 10
width = 5
bricks = [1,2,3,4,5]

"""
height = 100
width = 10
bricks = [1,2,3,4,5,6,7,8,9,10]
"""

solution = Solution()
print(solution.build_wall(height, width, bricks))
