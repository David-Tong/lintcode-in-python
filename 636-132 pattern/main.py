class Solution:
    """
    @param nums: a list of n integers
    @return: true if there is a 132 pattern or false
    """
    def find132pattern(self, nums):
        # write your code here
        two = float("-inf")
        stack = list()
        for num in nums[::-1]:
            if num < two:
                return True
            while stack and stack[-1] < num:
                two = max(two, stack.pop())
            stack.append(num)
        return False


nums = [1, 2, 3, 4]
#nums = [3, 1, 4, 2]
solution = Solution()

print(solution.find132pattern(nums))
