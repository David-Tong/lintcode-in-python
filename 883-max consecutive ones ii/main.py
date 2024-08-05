class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def find_max_consecutive_ones(self, nums):
        # write your code here
        L = len(nums)
        left = 0
        right = 0

        zeros = 0
        ans = 0
        while right < L:
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            right += 1
            ans = max(ans, right - left)
        return ans


nums = [1,0,1,1,0]
nums = [1,0,1,0,1]

solution = Solution()
print(solution.find_max_consecutive_ones(nums))
