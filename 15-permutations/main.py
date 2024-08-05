class Solution:
    """
    @param nums: A list of integers.
    @return: A list of permutations.
             we will sort your return value in output
    """
    def permute(self, nums):
        # write your code here
        L = len(nums)
        self.ans = list()
        def doPermute(permutation, mask, step):
            if step == L:
                self.ans.append(permutation)
            else:
                for idx, num in enumerate(nums):
                    if (mask >> idx) & 1:
                        pass
                    else:
                        doPermute(permutation + [num], mask | (1 << idx), step + 1)

        doPermute(list(), 0, 0)
        return self.ans


nums = [1]
nums = [1, 2, 3]

solution = Solution()
print(solution.permute(nums))
