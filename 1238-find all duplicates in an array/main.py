class Solution:
    """
    @param nums: a list of integers
    @return: return a list of integers
             we will sort your return value in output
    """
    def find_duplicates(self, nums):
        # write your code here
        for num in nums:
            nums[int(num) - 1] += 0.1

        ans = list()
        for idx, num in enumerate(nums):
            if abs(num - int(num) - 0.2) < 10e-9:
                ans.append(idx + 1)
        return ans


nums = [4,3,2,7,8,2,3,1]
#nums = [10,2,5,10,9,1,1,4,3,7]

solution = Solution()
print(solution.find_duplicates(nums))
