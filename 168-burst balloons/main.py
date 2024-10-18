class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def max_coins(self, nums):
        # write your code here
        # pre-process
        nums = [1] + nums + [1]
        L = len(nums)

        # dp init
        dp = [[0] * L for _ in range(L)]

        # dp transfer
        for l in range(1, L - 1):
            for x in range(1, L - l):
                y = x + l - 1
                for k in range(x, y + 1):
                    dp[x][y] = max(dp[x][y], dp[x][k - 1] + dp[k + 1][y] + nums[x - 1] * nums[k] * nums[y + 1])
        return dp[1][L - 2]


nums = [3,1,5,8]
nums = [3,1,5]
nums = [4,1,5,10]

solution = Solution()
print(solution.max_coins(nums))