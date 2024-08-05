class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def back_pack_i_v(self, nums, target):
        # write your code here
        # dp[x] - the plans number
        L = len(nums)

        dp = [0] * (target + 1)
        dp[0] = 1

        for num in nums:
            for y in range(num, target + 1):
                dp[y] += dp[y - num]
        return dp[target]


nums = [2,3,6,7]
target = 7

nums = [2,3,4,5]
target = 7

solution = Solution()
print(solution.back_pack_i_v(nums, target))
