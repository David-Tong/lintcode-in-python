from mailcap import subst


class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    def subsets(self, nums):
        # write your code here
        # pre-process
        L = len(nums)
        nums = sorted(nums)
        N = 2 ** L

        def decode(num):
            subset = list()
            idx = 0
            while num:
                if num & 1:
                    subset.append(nums[idx])
                num >>= 1
                idx += 1
            return subset

        # process
        ans = list()
        for x in range(N):
            ans.append(decode(x))
        return ans


nums = [1,2,3]

solution = Solution()
print(solution.subsets(nums))
