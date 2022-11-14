class Solution:
    """
    @param nums: the given array
    @param s: the given target
    @return: the number of ways to assign symbols to make sum of integers equal to target S
    """
    def find_target_sum_ways(self, nums, s):
        # Write your code here
        L = len(nums)
        LIMIT = 1000
        S = LIMIT * 2 + 1

        if L == 0:
            return 0

        # dp[x][y] - the ways to target sum y after x items in nums
        dp = [[0] * S for _ in range(L + 1)]
        dp[0][LIMIT] = 1

        for x in range(L + 1):
            for y in range(S):
                if y - nums[x - 1] >= 0:
                    dp[x][y] += dp[x - 1][y - nums[x - 1]]
                if y + nums[x - 1] < S:
                    dp[x][y] += dp[x - 1][y + nums[x - 1]]

        if 0 <= LIMIT + s < S:
            return dp[L][LIMIT + s]
        else:
            return 0

nums = [1, 1, 1, 1, 1]
s = 3

nums = [1]
s = 1

solution = Solution()
print(solution.find_target_sum_ways(nums, s))
