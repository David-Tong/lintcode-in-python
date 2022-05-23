class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def max_product(self, nums):
        # write your code here
        dp = [[0] * 2 for num in nums]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        # dp[][0] for min, dp[][1] for max
        for x in range(1, len(nums)):
            dp[x][0] = min(dp[x-1][0] * nums[x], min(dp[x-1][1] * nums[x], nums[x]))
            dp[x][1] = max(dp[x-1][0] * nums[x], max(dp[x-1][1] * nums[x], nums[x]))
        return max([item[1] for item in dp])


nums = [2, 3, -2, 4]
#nums = [-1, 2, 4, 1]
#nums = [-3, 1, -2]


solution = Solution()
print(solution.max_product(nums))
