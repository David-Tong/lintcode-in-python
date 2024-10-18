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
        self.ans = list()

        def do_subsets(idx, selected):
            if idx == L:
                self.ans.append(selected)
            else:
                do_subsets(idx + 1, selected + [nums[idx]])
                do_subsets(idx + 1, selected)

        # process
        do_subsets(0, list())
        return self.ans


nums = [0]
nums = [1,2,3]

solution = Solution()
print(solution.subsets(nums))
