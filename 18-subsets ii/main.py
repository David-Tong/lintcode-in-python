class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
             we will sort your return value in output
    """
    def subsets_with_dup(self, nums):
        # write your code here
        # pre-process
        L = len(nums)
        nums = sorted(nums)
        subsets = set()

        def do_subsets_with_dup(idx, subset):
            if idx == L:
                subsets.add(subset)
            else:
                do_subsets_with_dup(idx + 1, subset + ","+ str(nums[idx]))
                do_subsets_with_dup(idx + 1, subset)

        # process
        do_subsets_with_dup(0, "")

        # post-process
        ans = list()
        for subset in subsets:
            ans.append([int(_) for _ in subset.split(",") if _ != ''])
        return ans


nums = [1,2,2]

solution = Solution()
print(solution.subsets_with_dup(nums))
