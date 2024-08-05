class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def back_pack_v(self, nums, target):
        # write your code here
        # dp[x] - number of plan to fill the backpack with size x
        dp = [0] * (target + 1)
        dp[0] = 1

        for num in nums:
            for x in range(target, -1, -1):
                if x - num >= 0:
                    dp[x] += dp[x - num]
        print(dp)
        return dp[target]


nums = [1,2,3,3,7]
target = 7

solution = Solution()
print(solution.back_pack_v(nums, target))
