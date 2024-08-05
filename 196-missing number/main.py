class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def find_missing(self, nums):
        # write your code here
        # pre-process
        L = len(nums)
        total = L * (L + 1) // 2

        # process
        return total - sum(nums)


nums = [0,1,3]
nums = [1,2,3]

solution = Solution()
print(solution.find_missing(nums))
