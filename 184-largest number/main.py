class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """
    def largest_number(self, nums):
        # write your code here
        # pre-process
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        nums = [str(_) for _ in nums]
        nums = sorted(nums, cmp=compare)

        # process
        ans = str(int("".join(nums)))
        return ans


nums = [1, 20, 23, 4, 8]
nums = [4, 6, 65]
nums = [0,0,0,0]

solution = Solution()
print(solution.largest_number(nums))
