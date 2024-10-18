class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def max_coins(self, nums):
        # write your code here
        def do_max_coins(nums):
            key = "-".join([str(_) for _ in nums])
            if key in cache:
                return cache[key]

            L = len(nums)
            if L == 1:
                return nums[0]

            maxi_coins = 0
            for x in range(L):
                if x == 0:
                    burst_coins = nums[x] * nums[x + 1]
                elif x == L - 1:
                    burst_coins = nums[x - 1] * nums[x]
                else:
                    burst_coins = nums[x - 1] * nums[x] * nums[x + 1]
                maxi_coins = max(maxi_coins, do_max_coins(nums[:x] + nums[x + 1:]) + burst_coins)

            cache[key] = maxi_coins
            return maxi_coins

        from collections import defaultdict
        cache = defaultdict(int)
        return do_max_coins(nums)


nums = [3,1,5,8]
# = [3,1,5]
#nums = [4,1,5,10]

solution = Solution()
print(solution.max_coins(nums))
