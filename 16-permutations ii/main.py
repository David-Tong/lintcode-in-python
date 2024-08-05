class Solution:
    """
    @param nums: A list of integers
    @return: A list of unique permutations
             we will sort your return value in output
    """
    def permute_unique(self, nums):
        # write your code here
        N = len(nums)
        self.ans = list()

        def permute(permutation, selected, count):
            if count == N:
                from copy import deepcopy
                if permutation not in self.ans:
                    self.ans.append(deepcopy(permutation))
                return

            for idx in range(N):
                if not selected[idx]:
                    selected[idx] = True
                    permute(permutation + [nums[idx]], selected, count + 1)
                    selected[idx] = False

        selected = [False] * N
        permute(list(), selected, 0)
        return self.ans


nums = [1,1]
#nums = [1,2,2]
nums = [1,2,3,4,5]

solution = Solution()
print(solution.permute_unique(nums))
